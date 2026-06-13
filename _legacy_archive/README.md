# Legacy Wayback Archive

This folder is for recovering old `bi.snu.ac.kr` material from the Wayback
Machine without affecting the current Jekyll site.

Generated files are intentionally ignored by Git:

- `downloads/`: raw archived files mirrored from Wayback
- `reports/`: inventory, manifest, and summary files

Run from the repository root:

```bash
python _legacy_archive/tools/wayback_archive.py --domain bi.snu.ac.kr --out _legacy_archive --max-urls 0 --to 20241231235959 --inventory-only
```

The downloader uses the Wayback CDX API, stores files under `downloads/`, and
writes reports under `reports/`.

Typical recovery passes:

```bash
# Full legacy inventory, excluding 2025+ captures of the new/current site.
python _legacy_archive/tools/wayback_archive.py --domain bi.snu.ac.kr --out _legacy_archive --max-urls 0 --to 20241231235959 --inventory-only

# High-value legacy paths first.
python _legacy_archive/tools/wayback_archive.py --domain bi.snu.ac.kr --out _legacy_archive --use-inventory --path-regex "(Publications|People|Research|Projects|Info|SEMINAR|Tutorials|NRL|bdm2003|biocomputers2004|~btzhang)" --max-urls 0 --workers 4

# Recompute local coverage after downloads.
python _legacy_archive/tools/wayback_archive.py --domain bi.snu.ac.kr --out _legacy_archive --use-inventory --max-urls 0 --coverage-only

# Publish the recovered mirror and catalog into the Jekyll site.
python _legacy_archive/tools/publish_legacy_site.py
```

If `web.archive.org` returns connection-refused errors, rerun the same command
later with fewer workers. Existing files are skipped.
