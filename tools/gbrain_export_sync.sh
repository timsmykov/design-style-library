#!/usr/bin/env bash
set -euo pipefail
ROOT="${1:-$(pwd)}"
SOURCE_ID="${GBRAIN_SOURCE_ID:-design-style-library}"
EXPORT_DIR="$ROOT/gbrain_export/components"

cd "$ROOT"
./tools/component_index.py "$ROOT"

if command -v gbrain >/dev/null 2>&1; then
  if ! gbrain sources list 2>/dev/null | grep -q "^  ${SOURCE_ID}\\b"; then
    gbrain sources add "$SOURCE_ID" --path "$ROOT/gbrain_export" >/dev/null || true
  fi
  count=0
  while IFS= read -r -d '' file; do
    rel="${file#$ROOT/gbrain_export/}"
    slug="${rel%.md}"
    gbrain capture --file "$file" --slug "$slug" --type design-style-component --source "$SOURCE_ID" --quiet >/dev/null
    count=$((count+1))
  done < <(find "$EXPORT_DIR" -type f -name '*.md' -print0 | sort -z)
  # gbrain capture writes source-local frontmatter (captured_at/ingested_at) back into the source path.
  # Rebuild export afterwards so the git-tracked generated files stay deterministic.
  ./tools/component_index.py "$ROOT" >/dev/null
  echo "PASS: captured $count component slices into Gbrain source $SOURCE_ID"
else
  echo "WARN: gbrain not found; export files generated only"
fi
