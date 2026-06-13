#!/usr/bin/env bash
# Migrate legacy course materials from legacy/raw/bi.snu.ac.kr/Courses/
# into the courses/ Jekyll directory structure.
#
# For fully-migrated courses: delete the source HTML, move supporting files
# For stub-only courses: move everything to the Jekyll course dir
# Old dirs (pre-2007) with no Jekyll pages: leave in legacy/

set -e
cd "$(git rev-parse --show-toplevel)"

LEGACY="legacy/raw/bi.snu.ac.kr/Courses"

move_dir_contents() {
  local SRC="$1"
  local DST="$2"
  local EXCLUDE_HTML="${3:-false}"  # if true, skip .html/.htm files

  if [ ! -d "$SRC" ]; then
    echo "SKIP (no dir): $SRC"
    return
  fi

  mkdir -p "$DST"

  for item in "$SRC"/*/; do
    if [ -d "$item" ]; then
      dirname=$(basename "$item")
      cp -r "$item" "$DST/"
      git add "$DST/$dirname/"
    fi
  done

  for item in "$SRC"/*; do
    [ -d "$item" ] && continue
    fname=$(basename "$item")
    ext="${fname##*.}"
    if [ "$EXCLUDE_HTML" = "true" ] && { [ "$ext" = "html" ] || [ "$ext" = "htm" ]; }; then
      echo "  skip HTML: $fname"
      continue
    fi
    cp "$item" "$DST/"
    git add "$DST/$fname"
  done
}

# ─────────────────────────────────────────────
# FULLY MIGRATED: delete HTML, move supporting files
# ─────────────────────────────────────────────

echo "=== Fully migrated: delete HTML, move supporting files ==="

for entry in \
  "4ai07s:courses/2007-1/artificial-intelligence" \
  "4ai08s:courses/2008-1/artificial-intelligence" \
  "4ai09s:courses/2009-1/artificial-intelligence" \
  "4ai13s:courses/2013-1/artificial-intelligence" \
  "4ai15s:courses/2015-1/artificial-intelligence" \
  "4ai18s:courses/2018-1/artificial-intelligence" \
  "CNC2013:courses/2013-1/cognitive-neural-computation" \
  "aplc12:courses/2012-2/action-perception-learning-cycles" \
  "brain_comp_2009:courses/2009-1/brain-and-computation"
do
  src_dir="${entry%%:*}"
  dst_dir="${entry##*:}"
  echo "  $src_dir → $dst_dir (skip HTML)"
  move_dir_contents "$LEGACY/$src_dir" "$dst_dir" true
  git rm -r "$LEGACY/$src_dir/"
done

# ─────────────────────────────────────────────
# STUB ONLY: move everything to Jekyll course dir
# ─────────────────────────────────────────────

echo "=== Stub-only: move everything ==="

for entry in \
  "4ai08f:courses/2008-2/artificial-intelligence" \
  "4ai09f:courses/2009-2/artificial-intelligence" \
  "4ai10s:courses/2010-1/artificial-intelligence" \
  "4ai10f:courses/2010-2/artificial-intelligence" \
  "4ai11f:courses/2011-2/artificial-intelligence" \
  "4ai12s:courses/2012-1/artificial-intelligence" \
  "4ai12f:courses/2012-2/artificial-intelligence" \
  "4ai14s:courses/2014-1/artificial-intelligence" \
  "4ai16s:courses/2016-1/artificial-intelligence" \
  "4ai21s:courses/2021-1/artificial-intelligence" \
  "4ai22s:courses/2022-1/artificial-intelligence" \
  "brain_comp_2010:courses/2010-1/brain-and-computation" \
  "ann13:courses/2013-2/artificial-neural-networks" \
  "ann15f:courses/2015-2/artificial-neural-networks" \
  "ann17f:courses/2017-2/artificial-neural-networks" \
  "ann19f:courses/2019-2/artificial-neural-networks" \
  "ML2015f:courses/2015-2/machine-learning" \
  "g-ai08_2:courses/2008-2/ai-and-cognitive-process"
do
  src_dir="${entry%%:*}"
  dst_dir="${entry##*:}"
  if [ ! -d "$LEGACY/$src_dir" ]; then
    echo "  SKIP (no dir): $src_dir"
    continue
  fi
  echo "  $src_dir → $dst_dir (move all)"
  move_dir_contents "$LEGACY/$src_dir" "$dst_dir" false
  git rm -r "$LEGACY/$src_dir/"
done

echo ""
echo "Done. Remaining in legacy/raw/bi.snu.ac.kr/Courses/:"
ls "$LEGACY/"
