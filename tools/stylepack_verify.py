#!/usr/bin/env python3
"""Structural verifier for Design Style Library style packs.

This intentionally uses only Python stdlib so the repo can be checked on a
fresh server. It does not fully parse YAML; it validates required file presence,
JSON syntax, and prompt-directory policy.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

REQUIRED_PACK_FILES = [
    "manifest.yaml",
    "STYLE.md",
    "agent-contract.md",
    "evidence/sources.yaml",
    "evidence/observations.yaml",
    "dna/principles.md",
    "dna/layout.md",
    "dna/hierarchy.md",
    "dna/interaction.md",
    "dna/voice.md",
    "dna/anti-patterns.md",
    "tokens/tokens.json",
    "tokens/css-vars.css",
    "patterns/index.md",
    "components/component-atlas.md",
    "eval/checklist.yaml",
    "eval/rubric.md",
    "eval/failure-modes.md",
]

REQUIRED_EVIDENCE_DIRS = [
    "evidence/mobbin/screens",
    "evidence/mobbin/flows",
    "evidence/mobbin/sections",
    "evidence/web/pages",
    "evidence/web/css",
    "evidence/web/computed",
    "evidence/web/fonts",
]


def check_json(path: Path, errors: list[str]) -> None:
    try:
        json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001 - CLI verifier should print all issues
        errors.append(f"invalid JSON: {path}: {exc}")


def verify_repo(root: Path) -> int:
    errors: list[str] = []
    warnings: list[str] = []

    for rel in ["README.md", "DESIGN.md", "registry.yaml", "docs/style-pack-contract.md", "docs/extraction-pipeline.md", "docs/default-agent-style-workflow.md", "baselines/README.md", "baselines/voltagent-awesome-design-md/baseline-index.json", "baselines/style-baseline-map.json", "pack/README.md", "pack/DESIGN.md", "pack/registry.json"]:
        if not (root / rel).exists():
            errors.append(f"missing repo file: {rel}")

    for schema in (root / "schemas").glob("*.json"):
        check_json(schema, errors)



    pack_dir = root / "pack"
    if pack_dir.exists():
        symlinks = [path for path in pack_dir.rglob("*") if path.is_symlink()]
        if symlinks:
            errors.append("pack/ must be self-contained for runtime; found symlinks: " + ", ".join(str(p.relative_to(root)) for p in symlinks[:10]))

    pack_registry = root / "pack/registry.json"
    if pack_registry.exists():
        try:
            pdata = json.loads(pack_registry.read_text(encoding="utf-8"))
            if pdata.get("id") != "hermes-unified-design-pack":
                errors.append("pack/registry.json must describe hermes-unified-design-pack")
            if pdata.get("source_baseline", {}).get("design_md_count", 0) < 50:
                errors.append("unified pack has too few broad DESIGN.md entries")
            if len(pdata.get("styles", [])) < 10:
                errors.append("unified pack must expose deep style entries")
            declared_broad = pdata.get("source_baseline", {}).get("design_md_count", 0)
            actual_broad = len(list((root / "pack/design-md").glob("*/DESIGN.md")))
            if actual_broad != declared_broad:
                errors.append(
                    f"unified pack broad catalog is incomplete: declared {declared_broad}, found {actual_broad}"
                )

            registry_style_ids = {entry.get("id") for entry in pdata.get("styles", [])}
            source_style_ids = {
                path.name
                for path in (root / "styles").iterdir()
                if path.is_dir() and not path.name.startswith("_")
            }
            if registry_style_ids != source_style_ids:
                missing = sorted(source_style_ids - registry_style_ids)
                extra = sorted(registry_style_ids - source_style_ids)
                errors.append(
                    f"unified deep-style registry mismatch: missing={missing}, extra={extra}"
                )

            for entry in pdata.get("styles", []):
                for field in ("entry", "extension", "components"):
                    rel = entry.get(field)
                    if not rel or not (root / rel).exists():
                        errors.append(
                            f"unified style {entry.get('id')} has missing {field}: {rel}"
                        )
        except Exception as exc:  # noqa: BLE001
            errors.append(f"invalid pack/registry.json: {exc}")

    baseline_index = root / "baselines/voltagent-awesome-design-md/baseline-index.json"
    if baseline_index.exists():
        try:
            data = json.loads(baseline_index.read_text(encoding="utf-8"))
            if data.get("design_md_count", 0) < 50:
                errors.append("VoltAgent baseline index has too few DESIGN.md entries")
            if data.get("license") != "MIT":
                errors.append("VoltAgent baseline license metadata must remain MIT")
        except Exception as exc:  # noqa: BLE001
            errors.append(f"invalid baseline-index.json: {exc}")


    styles_dir = root / "styles"
    if not styles_dir.exists():
        errors.append("missing styles/ directory")
    else:
        packs = [p for p in styles_dir.iterdir() if p.is_dir() and not p.name.startswith("_")]
        if not packs:
            warnings.append("no concrete style packs yet")
        for pack in packs:
            verify_pack(pack, errors, warnings)

    for message in warnings:
        print(f"WARN: {message}")
    for message in errors:
        print(f"ERROR: {message}")
    if errors:
        return 1
    print("PASS: design-style-library structure is valid")
    return 0


def verify_pack(pack: Path, errors: list[str], warnings: list[str]) -> None:
    if (pack / "prompts").exists():
        errors.append(f"{pack.name}: prompts/ is forbidden as a canonical style-pack layer")

    for rel in REQUIRED_PACK_FILES:
        if not (pack / rel).exists():
            errors.append(f"{pack.name}: missing {rel}")

    for rel in REQUIRED_EVIDENCE_DIRS:
        if not (pack / rel).exists():
            errors.append(f"{pack.name}: missing evidence dir {rel}")

    capsules_dir = pack / "components/capsules"
    if not capsules_dir.exists():
        errors.append(f"{pack.name}: missing components/capsules")
    elif not list(capsules_dir.glob("*.md")):
        warnings.append(f"{pack.name}: components/capsules has no capsule markdown files yet")

    component_index = pack / "components/component-index.jsonl"
    if not component_index.exists():
        errors.append(f"{pack.name}: missing components/component-index.jsonl; run tools/component_index.py .")
    else:
        for line_no, line in enumerate(component_index.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                continue
            try:
                json.loads(line)
            except Exception as exc:  # noqa: BLE001
                errors.append(f"{pack.name}: invalid component-index.jsonl line {line_no}: {exc}")

    token_file = pack / "tokens/tokens.json"
    if token_file.exists():
        check_json(token_file, errors)

    sources = pack / "evidence/sources.yaml"
    if sources.exists() and "local_path:" not in sources.read_text(encoding="utf-8"):
        warnings.append(f"{pack.name}: sources.yaml has no local_path records yet")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".", help="repository root")
    args = parser.parse_args()
    return verify_repo(Path(args.root).resolve())


if __name__ == "__main__":
    sys.exit(main())
