#!/usr/bin/env python3
"""Move integrated legacy files out of legacy/raw and update site references."""

from __future__ import annotations

import json
import re
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OLD_PREFIX = "legacy/raw/"
NEW_PREFIX = "files/legacy/"
REPORT = ROOT / "_legacy_archive" / "reports" / "moved_integrated_legacy_files.json"

CONTENT_GLOBS = [
    "*.md",
    "_members/*.md",
    "research/*.md",
    "projects/*.md",
    "courses/*.md",
    "team/*.md",
    "contact/*.md",
    "internship/*.md",
]


def content_files() -> list[Path]:
    files: set[Path] = set()
    for pattern in CONTENT_GLOBS:
        files.update(ROOT.glob(pattern))
    return sorted(path for path in files if path.is_file())


def referenced_legacy_paths(files: list[Path]) -> set[str]:
    pattern = re.compile(r"/?legacy/raw/[A-Za-z0-9가-힣ㄱ-ㅎㅏ-ㅣ_./%+()&=,;:' -]+")
    refs: set[str] = set()
    for path in files:
        text = path.read_text(encoding="utf-8")
        for match in pattern.finditer(text):
            raw = match.group(0).strip()
            raw = raw.rstrip('")]}>,.')
            raw = raw.lstrip("/")
            candidate = ROOT / raw
            if candidate.exists() and candidate.is_file():
                refs.add(raw)
    return refs


def safe_path(relative: str) -> Path:
    path = ROOT / relative
    resolved = path.resolve()
    root = ROOT.resolve()
    if root not in resolved.parents and resolved != root:
        raise RuntimeError(f"Refusing path outside workspace: {resolved}")
    return path


def move_files(refs: set[str]) -> list[dict[str, str]]:
    moved = []
    for old_rel in sorted(refs):
        if not old_rel.startswith(OLD_PREFIX):
            continue
        new_rel = NEW_PREFIX + old_rel[len(OLD_PREFIX) :]
        source = safe_path(old_rel)
        target = safe_path(new_rel)

        if not source.exists():
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        if target.exists():
            if target.is_file() and target.stat().st_size == source.stat().st_size:
                source.unlink()
            else:
                raise RuntimeError(f"Target already exists with different content: {new_rel}")
        else:
            shutil.move(str(source), str(target))
        moved.append({"old": old_rel, "new": new_rel})
    return moved


def update_text_references(files: list[Path], moved: list[dict[str, str]]) -> int:
    replacements = []
    for item in moved:
        old = item["old"]
        new = item["new"]
        replacements.append(("/" + old, "/" + new))
        replacements.append((old, new))

    changed = 0
    for path in files:
        text = path.read_text(encoding="utf-8")
        new_text = text
        for old, new in replacements:
            new_text = new_text.replace(old, new)
        if new_text != text:
            path.write_text(new_text, encoding="utf-8")
            changed += 1
    return changed


def update_catalog(moved: list[dict[str, str]]) -> int:
    catalog = ROOT / "legacy" / "catalog.json"
    if not catalog.exists():
        return 0
    mapping = {item["old"]: item["new"] for item in moved}
    data = json.loads(catalog.read_text(encoding="utf-8"))
    updated = 0
    for item in data.get("items", []):
        local = item.get("local")
        if local in mapping:
            item["local"] = mapping[local]
            item["moved_from"] = local
            updated += 1
    if updated:
        catalog.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    return updated


def prune_empty_dirs(root: Path) -> int:
    removed = 0
    if not root.exists():
        return removed
    for path in sorted((p for p in root.rglob("*") if p.is_dir()), key=lambda p: len(p.parts), reverse=True):
        try:
            path.rmdir()
            removed += 1
        except OSError:
            pass
    return removed


def main() -> int:
    files = content_files()
    refs = referenced_legacy_paths(files)
    moved = move_files(refs)
    changed_files = update_text_references(files, moved)
    catalog_updates = update_catalog(moved)
    pruned_dirs = prune_empty_dirs(ROOT / "legacy" / "raw")

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(
        json.dumps(
            {
                "moved_files": len(moved),
                "updated_content_files": changed_files,
                "updated_catalog_entries": catalog_updates,
                "pruned_empty_dirs": pruned_dirs,
                "files": moved,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    print(f"Moved files: {len(moved)}")
    print(f"Updated content files: {changed_files}")
    print(f"Updated catalog entries: {catalog_updates}")
    print(f"Pruned empty legacy/raw dirs: {pruned_dirs}")
    print(f"Wrote {REPORT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
