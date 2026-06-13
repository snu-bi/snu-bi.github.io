#!/usr/bin/env python3
"""Fold recovered legacy People/*.html pages into current member pages."""

from __future__ import annotations

import re
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PEOPLE = ROOT / "legacy" / "raw" / "bi.snu.ac.kr" / "People"
MEMBERS = ROOT / "_members"
START = "<!-- legacy-profile:start -->"
END = "<!-- legacy-profile:end -->"


PROFILES = {
    "bjlee": {"name": "Beom-Jin Lee", "target": "beom-jin-lee.md"},
    "David": {"name": "Tim Weikersdorfer", "target": "tim-weikersdorfer.md"},
    "hykim": {"name": "Hweyoung Kim", "target": "hweyoung-kim.md"},
    "iykim": {"name": "In-Young Kim", "target": "inyoung-kim.md"},
    "jgjoung": {"name": "Je-Gun Joung", "target": "jegeun-joung.md"},
    "jhkim": {"name": "Jinhan Kim", "target": "jinhan-kim.md"},
    "jhyoo": {"name": "Jun Hee Yoo", "target": "junhee-yoo.md"},
    "jjkim": {"name": "Jung-Jib Kim", "target": "jung-jib-kim.md"},
    "jkim": {"name": "Ji-Seob Kim", "target": "jiseob-kim.md"},
    "jkrhee": {"name": "Je-Keun Rhee", "target": "jekeun-rhee.md"},
    "jmoh": {"name": "Jang-Min Oh", "target": "jangmin-oh.md"},
    "jskim": {"name": "Joon-Shik Kim", "target": "joon-shik-kim.md"},
    "jsnam": {"name": "Jin-Seok Nam", "target": "jinseok-nam.md"},
    "jsyang": {"name": "Jin-San Yang", "target": "jin-san-yang.md"},
    "jsyoo": {"name": "Ji-Seon Yoo", "target": "ji-seon-yoo.md"},
    "jwlee": {"name": "Jong-Woo Lee", "target": "jong-woo-lee.md"},
    "jwleedr": {"name": "Jae-Won Lee", "target": "jae-won-lee.md"},
    "jwnam": {"name": "Jin-Woo Nam", "target": "jinwu-nam.md"},
    "jylee": {"name": "Ji-Youn Lee", "target": "ji-youn-lee.md"},
    "jylee2": {"name": "Jae-Youn Lee", "target": "jae-youn-lee.md"},
    "jypark": {"name": "Ji-Yun Park", "target": "ji-yun-park.md"},
    "krshin": {"name": "Ki-Roo Shin", "target": "kirou-shin.md"},
    "mhkim": {"name": "Min-Hyeok Kim", "target": "minhyuk-kim.md"},
    "shkim2": {"name": "Seok-Hun Kim", "target": "seok-hun-kim.md"},
    "skkim": {"name": "Sung-Kyu Kim", "target": "sungkyu-kim.md"},
    "tspark": {"name": "Tae-Suh Park", "target": "taesuh-park.md"},
}


STOP_HEADINGS = {
    "about me",
    "computer skills",
    "contacts",
    "contatcts",
    "education",
    "experience",
    "experiences",
    "interests",
    "legacy publications",
    "programs",
    "projects",
    "publications",
    "relevant cources",
    "relevant courses",
    "research experience",
    "research interests",
    "teaching",
}


class TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []
        self.skip = False

    def handle_starttag(self, tag: str, attrs) -> None:
        if tag.lower() in {"script", "style"}:
            self.skip = True
        if tag.lower() in {"br", "p", "tr", "li", "div", "h1", "h2", "h3", "table"}:
            self.parts.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() in {"script", "style"}:
            self.skip = False
        if tag.lower() in {"p", "tr", "li", "div", "h1", "h2", "h3", "table"}:
            self.parts.append("\n")

    def handle_data(self, data: str) -> None:
        if not self.skip:
            self.parts.append(data)


def read_html(path: Path) -> str:
    raw = path.read_bytes()
    for encoding in ("utf-8", "cp949", "euc-kr", "latin1"):
        try:
            return raw.decode(encoding)
        except UnicodeDecodeError:
            pass
    return raw.decode("utf-8", errors="replace")


def html_lines(path: Path) -> list[str]:
    parser = TextExtractor()
    parser.feed(read_html(path))
    lines: list[str] = []
    for line in "".join(parser.parts).splitlines():
        line = re.sub(r"\s+", " ", line).strip()
        if not line:
            continue
        if line in lines[-3:]:
            continue
        lines.append(line)
    return lines


def clean(value: str) -> str:
    value = value.replace("\u2018", "'").replace("\u2019", "'")
    value = value.replace("\ufffd", "")
    value = re.sub(r"\s+", " ", value).strip()
    return value


def should_join(previous: str, current: str) -> bool:
    prev = previous.strip()
    cur = current.strip()
    if not prev or not cur or is_heading(cur):
        return False
    if cur[:1].islower():
        return True
    if prev.lower().endswith((" of", " for", " with", " from", " in", " on", " and", " using", " by", " to")):
        return True
    if prev.endswith(("B.-T.", "Prof.", "Dr.", "Bldg.", "No.")):
        return True
    if prev.endswith(":") and len(prev) <= 40:
        return True
    if prev.count("(") > prev.count(")"):
        return True
    return False


def fold_fragments(values: list[str]) -> list[str]:
    out: list[str] = []
    for value in values:
        value = clean(value)
        if not value:
            continue
        if out and should_join(out[-1], value):
            out[-1] = clean(out[-1] + " " + value)
        else:
            out.append(value)
    return out


def is_heading(line: str) -> bool:
    return clean(line).lower().rstrip(":") in STOP_HEADINGS


def collect_after(lines: list[str], heading_pattern: str, limit: int = 10) -> list[str]:
    out: list[str] = []
    pattern = re.compile(heading_pattern, re.I)
    for index, line in enumerate(lines):
        if not pattern.search(line):
            continue
        tail = pattern.sub("", line).strip(" :-")
        if tail:
            out.append(clean(tail))
        for item in lines[index + 1 :]:
            if is_heading(item):
                break
            item = clean(item).strip("· ")
            if not item:
                continue
            out.append(item)
            if len(out) >= limit:
                break
        break
    return dedupe(fold_fragments(out))


def dedupe(values: list[str]) -> list[str]:
    seen = set()
    out = []
    for value in values:
        key = value.lower()
        if key in seen:
            continue
        seen.add(key)
        out.append(value)
    return out


def contact_lines(lines: list[str]) -> list[str]:
    keep = []
    keywords = (
        "Biointelligence",
        "Bio-intelligence",
        "Artificial Intelligence Lab",
        "School of",
        "Seoul National University",
        "Seoul ",
        "Office",
        "Phone",
        "Fax",
        "E-mail",
        "Email",
        "Personal home page",
        "Personal Homepage",
        "Technische",
    )
    for index, line in enumerate(lines):
        if keep and is_heading(line):
            break
        if any(key.lower() in line.lower() for key in keywords):
            item = clean(line)
            if index + 1 < len(lines):
                nxt = clean(lines[index + 1])
                if (
                    item.endswith(("Bldg.", ":", "Fax", "E-mail", "Email"))
                    or item.lower().rstrip(":") in {"fax", "e-mail", "email"}
                ) and not is_heading(nxt):
                    item = clean(item + " " + nxt)
            keep.append(item)
    return dedupe(keep)[:12]


def email_from(lines: list[str]) -> str:
    text = " ".join(lines)
    match = re.search(r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}", text)
    return match.group(0) if match else ""


def home_page_from(lines: list[str]) -> str:
    text = " ".join(lines)
    match = re.search(r"https?://[^\s\]]+", text)
    return match.group(0).rstrip(".,)") if match else ""


def yaml_escape(value: str) -> str:
    return "'" + value.replace("'", "''") + "'"


def new_member_frontmatter(name: str, code: str, lines: list[str]) -> str:
    email = email_from(lines)
    homepage = home_page_from(lines)
    link_lines = []
    if email:
        link_lines.append(f"  email: {email}")
    if homepage:
        link_lines.append(f"  home-page: {homepage}")
    if not link_lines:
        link_lines.append("  home-page:")
    links = "\n".join(link_lines)
    return f"""---
aliases:
- {yaml_escape(name)}
- {code}
description: Legacy BI/SCAI profile recovered from the former bi.snu.ac.kr site
image: images/photo.jpg
links:
{links}
name: {yaml_escape(name)}
role: legacy-member
status: 졸업
---
"""


def source_link(path: Path) -> str:
    rel = path.relative_to(ROOT).as_posix()
    return '{{ "/' + rel + '" | relative_url }}'


def profile_section(code: str, name: str, source: Path, lines: list[str]) -> str:
    contact = contact_lines(lines)
    research = collect_after(lines, r"^research\s*interests?", limit=12)
    projects = collect_after(lines, r"^(research\s*)?projects?", limit=10)
    education = collect_after(lines, r"^education", limit=8)
    experience = collect_after(lines, r"^(research\s*)?experience", limit=10)
    teaching = collect_after(lines, r"^teaching", limit=6)
    publications = collect_after(lines, r"^publications?", limit=12)

    parts = [
        START,
        "",
        "## Historical BI Profile",
        "",
        (
            f"The recovered legacy page for {name} has been folded into this member record. "
            "The details below reflect the old BI/SCAI site and may not be current."
        ),
        "",
    ]

    if contact:
        parts += ["### Historical Contact", "", *[f"- {item}" for item in contact], ""]
    if research:
        parts += ["### Research Interests", "", *[f"- {item}" for item in research], ""]
    if education:
        parts += ["### Education", "", *[f"- {item}" for item in education], ""]
    if projects:
        parts += ["### Legacy Projects", "", *[f"- {item}" for item in projects], ""]
    if experience:
        parts += ["### Experience", "", *[f"- {item}" for item in experience], ""]
    if teaching:
        parts += ["### Teaching", "", *[f"- {item}" for item in teaching], ""]
    if publications:
        parts += ["### Legacy Publications", "", *[f"- {item}" for item in publications], ""]

    parts += [
        "### Recovered Materials",
        "",
        f"- [Preserved legacy profile page]({source_link(source)})",
    ]

    for image in sorted(source.parent.glob(f"{code}*")):
        if image.suffix.lower() in {".jpg", ".jpeg", ".gif", ".png"}:
            parts.append(f"- [Recovered profile image]({source_link(image)})")

    parts += ["", END]
    return "\n".join(parts).strip() + "\n"


def strip_existing_section(text: str) -> str:
    pattern = re.compile(r"\n?" + re.escape(START) + r".*?" + re.escape(END) + r"\n?", re.S)
    return pattern.sub("\n", text).rstrip() + "\n"


def main() -> int:
    updated = 0
    created = 0
    skipped = []

    for code, info in PROFILES.items():
        source = PEOPLE / f"{code}.html"
        if not source.exists():
            skipped.append(code)
            continue
        lines = html_lines(source)
        target = MEMBERS / info["target"]
        section = profile_section(code, info["name"], source, lines)

        if target.exists():
            text = target.read_text(encoding="utf-8")
            text = strip_existing_section(text).rstrip() + "\n\n" + section
            target.write_text(text, encoding="utf-8")
            updated += 1
        else:
            text = new_member_frontmatter(info["name"], code, lines).rstrip() + "\n\n" + section
            target.write_text(text, encoding="utf-8")
            created += 1

    print(f"Updated existing member pages: {updated}")
    print(f"Created legacy member pages: {created}")
    if skipped:
        print("Skipped missing sources: " + ", ".join(skipped))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
