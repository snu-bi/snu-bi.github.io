# Legacy Wayback Archive

This folder is for recovering old `bi.snu.ac.kr` material from the Wayback
Machine without affecting the current Jekyll site.

Generated files are intentionally ignored by Git:

- `downloads/`: raw archived files mirrored from Wayback
- `reports/`: inventory, manifest, and summary files

Run from the repository root:

```bash
python _legacy_archive/tools/wayback_archive.py --domain bi.snu.ac.kr --out _legacy_archive
```

The downloader uses the Wayback CDX API, stores files under `downloads/`, and
writes reports under `reports/`.
