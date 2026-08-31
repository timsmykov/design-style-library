#!/usr/bin/env python3
"""Build component indexes and Gbrain export slices for style packs.

This is intentionally stdlib-only. Component capsules are Markdown files with a
small YAML-like frontmatter block. The script validates required scalar/list
fields, writes `components/component-index.jsonl`, and emits compact Gbrain
export pages under `gbrain_export/components/<style>/`.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys

REQUIRED = ["style_id", "component_id", "title", "component_type", "mediums", "intents", "confidence"]
LIST_FIELDS = {"mediums", "intents", "aliases", "tags", "evidence_paths", "extracted_paths"}


def parse_frontmatter(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"{path}: missing frontmatter")
    try:
        _, fm, body = text.split("---\n", 2)
    except ValueError as exc:
        raise ValueError(f"{path}: invalid frontmatter fence") from exc
    data: dict[str, object] = {}
    current: str | None = None
    for raw in fm.splitlines():
        line = raw.rstrip()
        if not line or line.strip().startswith("#"):
            continue
        m = re.match(r"^([a-zA-Z0-9_]+):\s*(.*)$", line)
        if m:
            key, value = m.groups()
            current = key
            if value == "":
                data[key] = [] if key in LIST_FIELDS else ""
            elif value.startswith("[") and value.endswith("]"):
                data[key] = [v.strip().strip('"\'') for v in value[1:-1].split(",") if v.strip()]
            else:
                data[key] = value.strip().strip('"\'')
            continue
        m = re.match(r"^\s*-\s*(.*)$", line)
        if m and current:
            data.setdefault(current, [])
            if not isinstance(data[current], list):
                raise ValueError(f"{path}: field {current} mixes scalar/list")
            data[current].append(m.group(1).strip().strip('"\''))
            continue
        raise ValueError(f"{path}: cannot parse frontmatter line: {raw}")
    return data, body.strip()


def summarize(body: str) -> str:
    # Keep enough semantic content for retrieval, but not the whole world.
    lines = []
    for line in body.splitlines():
        if line.startswith("#") or line.startswith("-") or line.startswith("|") or line.strip().startswith("`"):
            lines.append(line)
        elif line.strip():
            lines.append(line)
        if len("\n".join(lines)) > 7000:
            break
    return "\n".join(lines).strip()


def build(root: Path) -> int:
    errors: list[str] = []
    capsules = sorted(root.glob("styles/*/components/capsules/*.md"))
    by_style: dict[str, list[dict]] = {}
    export_root = root / "gbrain_export" / "components"
    export_root.mkdir(parents=True, exist_ok=True)

    for path in capsules:
        try:
            meta, body = parse_frontmatter(path)
            for field in REQUIRED:
                if field not in meta or meta[field] in ("", []):
                    raise ValueError(f"{path}: missing required field {field}")
            style_id = str(meta["style_id"])
            component_id = str(meta["component_id"])
            rel = str(path.relative_to(root))
            meta["repo_path"] = rel
            meta.setdefault("aliases", [])
            meta.setdefault("tags", [])
            meta.setdefault("evidence_paths", [])
            meta.setdefault("extracted_paths", [])
            record = dict(meta)
            record["body_excerpt"] = summarize(body)[:2400]
            by_style.setdefault(style_id, []).append(record)

            outdir = export_root / style_id
            outdir.mkdir(parents=True, exist_ok=True)
            export = outdir / f"{component_id}.md"
            export.write_text(
                "---\n"
                f"title: Design Style Component — {style_id} / {component_id}\n"
                f"type: design-style-component\n"
                f"style_id: {style_id}\n"
                f"component_id: {component_id}\n"
                f"component_type: {meta['component_type']}\n"
                f"confidence: {meta['confidence']}\n"
                f"repo_path: {rel}\n"
                f"tags: {', '.join(str(x) for x in meta.get('tags', []))}\n"
                "---\n\n"
                f"# {meta['title']}\n\n"
                f"Style: `{style_id}`\n\n"
                f"Component: `{component_id}`\n\n"
                f"Mediums: {', '.join(str(x) for x in meta.get('mediums', []))}\n\n"
                f"Intents: {', '.join(str(x) for x in meta.get('intents', []))}\n\n"
                f"Aliases: {', '.join(str(x) for x in meta.get('aliases', []))}\n\n"
                f"Repo source: `{rel}`\n\n"
                "## Capsule\n\n"
                f"{summarize(body)}\n",
                encoding="utf-8",
            )
        except Exception as exc:  # noqa: BLE001
            errors.append(str(exc))

    for style_id, records in by_style.items():
        index_path = root / "styles" / style_id / "components" / "component-index.jsonl"
        index_path.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in records), encoding="utf-8")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    total = sum(len(v) for v in by_style.values())
    print(f"PASS: indexed {total} component capsules across {len(by_style)} style packs")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".")
    args = parser.parse_args()
    return build(Path(args.root).resolve())


if __name__ == "__main__":
    sys.exit(main())
