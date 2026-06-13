#!/usr/bin/env python3
"""
Recover archived files for a domain from the Wayback Machine.

The script is intentionally conservative:
- writes only under the selected output directory
- uses Wayback "id_" raw replay URLs
- keeps a manifest for every attempted download
- limits concurrency by default
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import html
import json
import mimetypes
import os
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable
from urllib.error import HTTPError, URLError
from urllib.parse import quote, unquote, urlparse
from urllib.request import Request, urlopen


CDX = "https://web.archive.org/cdx/search/cdx"
REPLAY = "https://web.archive.org/web/{timestamp}id_/{original}"
USER_AGENT = "snu-bi-legacy-archive/1.0 (+https://snu-bi.github.io)"

TEXT_MIMES = {
    "text/html",
    "text/plain",
    "text/css",
    "text/xml",
    "application/xml",
    "application/xhtml+xml",
    "application/javascript",
    "text/javascript",
}

PRIORITY_EXTENSIONS = {
    ".html",
    ".htm",
    ".shtml",
    ".php",
    ".asp",
    ".txt",
    ".css",
    ".js",
    ".pdf",
    ".doc",
    ".docx",
    ".ppt",
    ".pptx",
    ".xls",
    ".xlsx",
    ".zip",
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".svg",
    ".swf",
}


@dataclass(frozen=True)
class CdxRow:
    timestamp: str
    original: str
    statuscode: str
    mimetype: str
    digest: str
    length: str = ""


def fetch_url(url: str, timeout: int = 60) -> bytes:
    req = Request(url, headers={"User-Agent": USER_AGENT})
    with urlopen(req, timeout=timeout) as response:
        return response.read()


def fetch_text(url: str, timeout: int = 60) -> str:
    return fetch_url(url, timeout=timeout).decode("utf-8", errors="replace")


def cdx_query(domain: str, collapse: str, limit: int, to: str, page_size: int) -> list[CdxRow]:
    rows: list[CdxRow] = []
    resume_key = ""

    while True:
        remaining = limit - len(rows) if limit > 0 else page_size
        if limit > 0 and remaining <= 0:
            break

        batch_limit = min(page_size, remaining) if limit > 0 else page_size
        query = (
            f"{CDX}?url={quote(domain + '/')}"
            "&matchType=prefix"
            "&output=json"
            "&fl=timestamp,original,mimetype,statuscode,digest,length"
            "&filter=statuscode:200"
            f"&collapse={quote(collapse)}"
            f"&limit={batch_limit}"
            "&showResumeKey=true"
        )
        if to:
            query += f"&to={quote(to)}"
        if resume_key:
            query += f"&resumeKey={quote(resume_key)}"

        data = json.loads(fetch_text(query, timeout=180))
        if not data:
            break

        header = data[0]
        next_resume_key = ""
        for raw in data[1:]:
            if not raw:
                continue
            if len(raw) == 1:
                next_resume_key = raw[0]
                continue
            item = dict(zip(header, raw))
            rows.append(
                CdxRow(
                    timestamp=item.get("timestamp", ""),
                    original=item.get("original", ""),
                    statuscode=item.get("statuscode", ""),
                    mimetype=item.get("mimetype", ""),
                    digest=item.get("digest", ""),
                    length=item.get("length", ""),
                )
            )

        if not next_resume_key or next_resume_key == resume_key:
            break
        resume_key = next_resume_key

    return rows


def is_probably_useful(row: CdxRow) -> bool:
    parsed = urlparse(row.original)
    ext = Path(parsed.path).suffix.lower()
    if ext in PRIORITY_EXTENSIONS:
        return True
    if row.mimetype in TEXT_MIMES:
        return True
    if row.mimetype.startswith("image/"):
        return True
    if row.mimetype in {
        "application/pdf",
        "application/msword",
        "application/vnd.ms-powerpoint",
        "application/vnd.ms-excel",
        "application/zip",
    }:
        return True
    # Old PHP boards often have no useful extension but contain query strings.
    if parsed.query and row.mimetype in {"text/html", "warc/revisit"}:
        return True
    return False


def safe_part(value: str, fallback: str = "index") -> str:
    value = unquote(value).strip().replace("\\", "/")
    value = re.sub(r"[^A-Za-z0-9._@+=,-]+", "_", value)
    value = value.strip("._")
    return value or fallback


def local_path_for(row: CdxRow, downloads: Path) -> Path:
    parsed = urlparse(row.original)
    path = parsed.path.strip("/")

    if not path:
        path = "index.html"

    parts = [safe_part(part) for part in path.split("/") if part]
    if not parts:
        parts = ["index.html"]

    leaf = parts[-1]
    suffix = Path(leaf).suffix

    if not suffix:
        guessed = mimetypes.guess_extension(row.mimetype.split(";")[0])
        suffix = guessed or ".html"
        leaf += suffix

    if parsed.query:
        digest = hashlib.sha1(parsed.query.encode("utf-8")).hexdigest()[:12]
        stem = leaf[: -len(suffix)] if suffix else leaf
        leaf = f"{stem}__query-{digest}{suffix}"

    parts[-1] = safe_part(leaf, "index.html")
    local = downloads.joinpath(*parts)

    # Avoid very long Windows paths by hashing the filename.
    if len(str(local)) > 230:
        hashed = hashlib.sha1(row.original.encode("utf-8")).hexdigest()
        local = downloads / "_long_paths" / f"{hashed}{suffix or '.bin'}"

    return local


def write_inventory(rows: Iterable[CdxRow], reports: Path) -> None:
    rows = list(rows)
    reports.mkdir(parents=True, exist_ok=True)
    csv_path = reports / "inventory.csv"
    jsonl_path = reports / "inventory.jsonl"

    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["timestamp", "original", "statuscode", "mimetype", "digest", "length"],
        )
        writer.writeheader()
        for row in rows:
            writer.writerow(row.__dict__)

    with jsonl_path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row.__dict__, ensure_ascii=False) + "\n")


def read_inventory(path: Path) -> list[CdxRow]:
    with path.open("r", newline="", encoding="utf-8") as handle:
        rows = []
        for row in csv.DictReader(handle):
            rows.append(
                CdxRow(
                    timestamp=row.get("timestamp", ""),
                    original=row.get("original", ""),
                    statuscode=row.get("statuscode", ""),
                    mimetype=row.get("mimetype", ""),
                    digest=row.get("digest", ""),
                    length=row.get("length", ""),
                )
            )
        return rows


def download_one(row: CdxRow, downloads: Path, retries: int) -> dict:
    target = local_path_for(row, downloads)
    replay = REPLAY.format(timestamp=row.timestamp, original=row.original)
    record = {
        **row.__dict__,
        "replay": replay,
        "local_path": str(target),
        "bytes": 0,
        "sha256": "",
        "download_status": "pending",
        "error": "",
    }

    if target.exists() and target.stat().st_size > 0:
        data = target.read_bytes()
        record["bytes"] = len(data)
        record["sha256"] = hashlib.sha256(data).hexdigest()
        record["download_status"] = "exists"
        return record

    for attempt in range(max(0, retries) + 1):
        try:
            data = fetch_url(replay, timeout=90)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
            record["bytes"] = len(data)
            record["sha256"] = hashlib.sha256(data).hexdigest()
            record["download_status"] = "downloaded"
            record["error"] = ""
            break
        except HTTPError as exc:
            record["download_status"] = "error"
            record["error"] = f"HTTP {exc.code}: {exc.reason}"
        except (URLError, TimeoutError, OSError) as exc:
            record["download_status"] = "error"
            record["error"] = str(exc)

        if attempt < retries:
            time.sleep(min(30, 2 ** attempt))
    return record


def write_manifest(records: Iterable[dict], reports: Path) -> None:
    records = list(records)
    if not records:
        return

    manifest_csv = reports / "manifest.csv"
    manifest_jsonl = reports / "manifest.jsonl"
    fields = list(records[0].keys())

    with manifest_csv.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for record in records:
            writer.writerow(record)

    with manifest_jsonl.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")


def summarize(rows: list[CdxRow], records: list[dict], reports: Path) -> None:
    by_mime: dict[str, int] = {}
    for row in rows:
        by_mime[row.mimetype] = by_mime.get(row.mimetype, 0) + 1

    by_status: dict[str, int] = {}
    total_bytes = 0
    for record in records:
        by_status[record["download_status"]] = by_status.get(record["download_status"], 0) + 1
        total_bytes += int(record.get("bytes") or 0)

    lines = [
        "# Wayback Recovery Summary",
        "",
        f"- Inventory rows: {len(rows):,}",
        f"- Download attempts: {len(records):,}",
        f"- Downloaded/available bytes: {total_bytes:,}",
        "",
        "## Download Status",
        "",
    ]
    for status, count in sorted(by_status.items()):
        lines.append(f"- {status}: {count:,}")

    lines += ["", "## MIME Types", ""]
    for mime, count in sorted(by_mime.items(), key=lambda item: (-item[1], item[0])):
        lines.append(f"- {mime}: {count:,}")

    examples = [r for r in records if r["download_status"] in {"downloaded", "exists"}][:30]
    if examples:
        lines += ["", "## Example Files", ""]
        for record in examples:
            local = Path(record["local_path"])
            lines.append(f"- `{local.as_posix()}` <- {record['original']}")

    reports.mkdir(parents=True, exist_ok=True)
    (reports / "summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_coverage(rows: list[CdxRow], downloads: Path, reports: Path) -> None:
    records = []
    for row in rows:
        local = local_path_for(row, downloads)
        parsed = urlparse(row.original)
        parts = [part for part in parsed.path.strip("/").split("/") if part]
        folder = parts[0] if parts else "_root"
        exists = local.exists() and local.is_file()
        size = local.stat().st_size if exists else 0
        records.append(
            {
                **row.__dict__,
                "folder": folder,
                "local_path": str(local),
                "exists": str(exists).lower(),
                "bytes": size,
            }
        )

    reports.mkdir(parents=True, exist_ok=True)
    fields = list(records[0].keys()) if records else []
    with (reports / "coverage.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(records)

    by_folder: dict[str, dict[str, int]] = {}
    by_mime: dict[str, dict[str, int]] = {}
    total_bytes = 0
    for record in records:
        folder = record["folder"]
        mime = record["mimetype"]
        by_folder.setdefault(folder, {"total": 0, "exists": 0, "bytes": 0})
        by_mime.setdefault(mime, {"total": 0, "exists": 0, "bytes": 0})
        for bucket in (by_folder[folder], by_mime[mime]):
            bucket["total"] += 1
            if record["exists"] == "true":
                bucket["exists"] += 1
                bucket["bytes"] += int(record["bytes"])
        total_bytes += int(record["bytes"])

    lines = [
        "# Wayback Coverage",
        "",
        f"- Inventory rows: {len(records):,}",
        f"- Local files present: {sum(1 for r in records if r['exists'] == 'true'):,}",
        f"- Local bytes: {total_bytes:,}",
        "",
        "## By Folder",
        "",
        "| Folder | Present | Total | Bytes |",
        "|---|---:|---:|---:|",
    ]
    for folder, values in sorted(
        by_folder.items(), key=lambda item: (-item[1]["bytes"], item[0].lower())
    ):
        lines.append(
            f"| `{folder}` | {values['exists']:,} | {values['total']:,} | {values['bytes']:,} |"
        )

    lines += [
        "",
        "## By MIME",
        "",
        "| MIME | Present | Total | Bytes |",
        "|---|---:|---:|---:|",
    ]
    for mime, values in sorted(
        by_mime.items(), key=lambda item: (-item[1]["bytes"], item[0].lower())
    ):
        lines.append(
            f"| `{mime}` | {values['exists']:,} | {values['total']:,} | {values['bytes']:,} |"
        )

    (reports / "coverage.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--domain", default="bi.snu.ac.kr")
    parser.add_argument("--out", default="_legacy_archive")
    parser.add_argument("--max-urls", type=int, default=2500)
    parser.add_argument("--offset", type=int, default=0)
    parser.add_argument("--workers", type=int, default=6)
    parser.add_argument("--retries", type=int, default=2)
    parser.add_argument("--cdx-page-size", type=int, default=5000)
    parser.add_argument("--to", default="")
    parser.add_argument(
        "--collapse",
        default="urlkey",
        choices=["urlkey", "digest"],
        help="CDX collapse mode. urlkey keeps one capture per URL; digest deduplicates content.",
    )
    parser.add_argument(
        "--inventory-only",
        action="store_true",
        help="Write inventory without downloading files.",
    )
    parser.add_argument(
        "--coverage-only",
        action="store_true",
        help="Read inventory and write local coverage reports without downloading.",
    )
    parser.add_argument(
        "--use-inventory",
        action="store_true",
        help="Read reports/inventory.csv instead of querying CDX again.",
    )
    parser.add_argument(
        "--mime-regex",
        default="",
        help="Only download rows whose CDX mimetype matches this regex.",
    )
    parser.add_argument(
        "--path-regex",
        default="",
        help="Only download rows whose original URL matches this regex.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(args.out)
    downloads = root / "downloads" / args.domain
    reports = root / "reports"

    inventory_path = reports / "inventory.csv"
    if args.use_inventory and inventory_path.exists():
        print(f"Reading existing inventory from {inventory_path} ...", flush=True)
        rows = read_inventory(inventory_path)
    else:
        print(f"Querying CDX for {args.domain} ...", flush=True)
        rows = cdx_query(args.domain, args.collapse, args.max_urls, args.to, args.cdx_page_size)
        rows = [row for row in rows if is_probably_useful(row)]
        rows.sort(key=lambda row: (row.original.lower(), row.timestamp))
        if args.max_urls > 0:
            rows = rows[: args.max_urls]
        write_inventory(rows, reports)

    if args.mime_regex:
        mime_pattern = re.compile(args.mime_regex, re.IGNORECASE)
        rows = [row for row in rows if mime_pattern.search(row.mimetype)]

    if args.path_regex:
        path_pattern = re.compile(args.path_regex, re.IGNORECASE)
        rows = [row for row in rows if path_pattern.search(row.original)]

    if args.use_inventory:
        start = max(0, args.offset)
        stop = start + args.max_urls if args.max_urls > 0 else None
        rows = rows[start:stop]

    print(f"Inventory rows: {len(rows):,}", flush=True)

    if args.inventory_only:
        summarize(rows, [], reports)
        print(f"Wrote reports to {reports}", flush=True)
        return 0

    if args.coverage_only:
        write_coverage(rows, downloads, reports)
        print(f"Wrote coverage reports to {reports}", flush=True)
        return 0

    records: list[dict] = []
    workers = max(1, min(args.workers, 12))
    print(f"Downloading with {workers} workers into {downloads} ...", flush=True)
    started = time.time()

    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = [executor.submit(download_one, row, downloads, args.retries) for row in rows]
        for index, future in enumerate(as_completed(futures), start=1):
            record = future.result()
            records.append(record)
            if index % 50 == 0 or index == len(futures):
                write_manifest(records, reports)
                elapsed = time.time() - started
                print(f"{index:,}/{len(futures):,} complete ({elapsed:.1f}s)", flush=True)

    records.sort(key=lambda record: record["original"].lower())
    write_manifest(records, reports)
    summarize(rows, records, reports)
    print(f"Wrote reports to {reports}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
