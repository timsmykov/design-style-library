#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "pack"
REPORT = ROOT / "reports" / "agent-style-usability-audit.md"

REQUIRED_EXTENSION_FILES = [
    "STYLE.md",
    "agent-contract.md",
    "manifest.yaml",
    "tokens/tokens.json",
    "tokens/css-vars.css",
    "patterns/index.md",
    "components/component-atlas.md",
    "components/component-index.jsonl",
    "eval/checklist.yaml",
    "eval/rubric.md",
    "eval/failure-modes.md",
    "evidence/sources.yaml",
    "evidence/observations.yaml",
    "dna/principles.md",
    "dna/layout.md",
    "dna/hierarchy.md",
    "dna/interaction.md",
    "dna/voice.md",
    "dna/anti-patterns.md",
]

GUIDANCE_TERMS = [
    "Authority inside this file",
    "Hermes deep extension overrides",
    "Local extension root",
    "Component semantic slices",
    "Runtime",
    "eval",
]

PLACEHOLDER_RE = re.compile(r"\b(TODO|TBD|LOREM IPSUM|FIXME)\b", re.I)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def json_load(path: Path) -> tuple[Any | None, str | None]:
    try:
        return json.loads(read(path)), None
    except Exception as exc:  # noqa: BLE001
        return None, str(exc)


def count_files(path: Path, patterns: tuple[str, ...]) -> int:
    if not path.exists():
        return 0
    return sum(1 for pattern in patterns for _ in path.glob(pattern))


@dataclass
class StyleAudit:
    style_id: str
    score: int = 100
    blockers: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    facts: dict[str, Any] = field(default_factory=dict)

    def fail(self, message: str, points: int = 20) -> None:
        self.blockers.append(message)
        self.score -= points

    def warn(self, message: str, points: int = 3) -> None:
        self.warnings.append(message)
        self.score -= points

    def clamp(self) -> None:
        self.score = max(0, min(100, self.score))


def audit_style(entry: dict[str, Any]) -> StyleAudit:
    sid = entry["id"]
    a = StyleAudit(style_id=sid)
    style_design = ROOT / entry["entry"]
    ext = ROOT / entry["extension"]
    comps = ROOT / entry["components"]

    a.facts["baseline_ids"] = entry.get("baseline_ids", [])

    if not style_design.exists():
        a.fail(f"missing unified DESIGN.md: {entry['entry']}")
        design_text = ""
    else:
        design_text = read(style_design)
        a.facts["design_chars"] = len(design_text)
        if len(design_text) < 3000:
            a.warn("unified DESIGN.md is short; agent may not get enough style grammar", 5)
        for term in GUIDANCE_TERMS:
            if term.lower() not in design_text.lower():
                a.warn(f"unified DESIGN.md lacks explicit guidance term: {term}", 2)
        if "do not call github/mobbin/web/browser" not in design_text.lower():
            a.warn("runtime boundary is not explicit enough in unified DESIGN.md", 2)
        stale_refs = [f"styles/{sid}/baseline", "repository root `design.md`"]
        for stale in stale_refs:
            if stale in design_text.lower():
                a.warn(f"unified DESIGN.md contains stale pre-consolidation reference: {stale}", 3)

    if ext.is_symlink() or comps.is_symlink():
        a.fail("pack entry still uses symlink; runtime pack must be self-contained")
    contract_runtime_text = read(ext / "agent-contract.md").lower()
    if f"styles/{sid}/baseline" in contract_runtime_text or "repository root `design.md`" in contract_runtime_text:
        a.warn("agent-contract.md contains stale pre-consolidation path/reference", 3)
    if not ext.exists():
        a.fail(f"missing deep extension directory: {entry['extension']}")
    if not comps.exists():
        a.fail(f"missing component slice directory: {entry['components']}")

    missing = [rel for rel in REQUIRED_EXTENSION_FILES if not (ext / rel).exists()]
    if missing:
        a.fail("missing required extension files: " + ", ".join(missing), 10 + len(missing))

    style_text = read(ext / "STYLE.md")
    contract_text = read(ext / "agent-contract.md")
    atlas_text = read(ext / "components/component-atlas.md")
    checklist_text = read(ext / "eval/checklist.yaml")
    rubric_text = read(ext / "eval/rubric.md")
    failure_text = read(ext / "eval/failure-modes.md")
    sources_text = read(ext / "evidence/sources.yaml")
    observations_text = read(ext / "evidence/observations.yaml")
    patterns_text = read(ext / "patterns/index.md")

    text_blobs = {
        "STYLE.md": style_text,
        "agent-contract.md": contract_text,
        "component-atlas.md": atlas_text,
        "eval/checklist.yaml": checklist_text,
        "eval/rubric.md": rubric_text,
        "eval/failure-modes.md": failure_text,
        "patterns/index.md": patterns_text,
    }
    for name, text in text_blobs.items():
        if not text:
            continue
        hits = PLACEHOLDER_RE.findall(text)
        if hits:
            a.warn(f"placeholder marker in {name}: {sorted(set(h.upper() for h in hits))}", 4)

    a.facts["style_chars"] = len(style_text)
    a.facts["contract_chars"] = len(contract_text)
    a.facts["atlas_chars"] = len(atlas_text)
    a.facts["checklist_chars"] = len(checklist_text)
    a.facts["rubric_chars"] = len(rubric_text)
    a.facts["failure_modes_chars"] = len(failure_text)

    if len(style_text) < 2500:
        a.warn("STYLE.md is thin for agent generation", 4)
    if len(contract_text) < 800:
        a.warn("agent-contract.md is thin; usage contract may be under-specified", 4)
    if len(atlas_text) < 1500:
        a.warn("component atlas is thin", 4)
    if len(checklist_text) < 500 or len(rubric_text) < 700 or len(failure_text) < 500:
        a.warn("eval layer is thin", 5)
    if "local_path:" not in sources_text:
        a.warn("sources.yaml lacks local_path records", 4)
    if len(observations_text) < 500:
        a.warn("observations.yaml is thin", 4)
    if len(patterns_text) < 200:
        a.warn("patterns/index.md is thin", 3)

    tokens, token_err = json_load(ext / "tokens/tokens.json")
    if token_err:
        a.fail(f"invalid tokens.json: {token_err}")
        tokens = {}
    if isinstance(tokens, dict):
        color_count = len(tokens.get("color", tokens.get("colors", {})) or {})
        typo_count = len(tokens.get("typography", {}) or {})
        a.facts["color_tokens"] = color_count
        a.facts["typography_tokens"] = typo_count
        for key in ["spacing", "radius"]:
            if key not in tokens:
                a.warn(f"tokens.json lacks {key} scale", 2)
        if color_count < 6:
            a.warn("too few color tokens for reliable generation", 4)
        if typo_count < 2:
            a.warn("too few typography tokens for reliable generation", 4)

    index_lines = 0
    bad_index = 0
    index_path = ext / "components/component-index.jsonl"
    if index_path.exists():
        for line in read(index_path).splitlines():
            if not line.strip():
                continue
            index_lines += 1
            try:
                json.loads(line)
            except Exception:  # noqa: BLE001
                bad_index += 1
    if bad_index:
        a.fail(f"component-index.jsonl has invalid JSONL lines: {bad_index}")
    a.facts["component_index_lines"] = index_lines

    capsule_count = count_files(ext / "components/capsules", ("*.md",))
    component_slice_count = count_files(comps, ("*.md",))
    a.facts["capsules"] = capsule_count
    a.facts["component_slices"] = component_slice_count
    if capsule_count < 8:
        a.warn("fewer than 8 component capsules", 5)
    if component_slice_count < 8:
        a.warn("fewer than 8 component slices", 5)
    if index_lines and capsule_count and index_lines < capsule_count:
        a.warn("component index has fewer rows than capsules", 3)

    screens = count_files(ext / "evidence/mobbin/screens", ("*.webp", "*.png", "*.jpg", "*.jpeg"))
    sections = count_files(ext / "evidence/mobbin/sections", ("*.webp", "*.png", "*.jpg", "*.jpeg"))
    flows = count_files(ext / "evidence/mobbin/flows", ("*.webp", "*.png", "*.jpg", "*.jpeg"))
    web_pages = count_files(ext / "evidence/web/pages", ("*.html", "*.md", "*.json"))
    auth_shots = count_files(ext / "evidence/authenticated", ("**/*.png", "**/*.webp", "**/*.jpg", "**/*.jpeg"))
    a.facts.update({"mobbin_screens": screens, "mobbin_sections": sections, "mobbin_flows": flows, "web_pages": web_pages, "auth_screenshots": auth_shots})
    visual_total = screens + sections + flows + auth_shots
    if screens < 10 and visual_total < 40:
        a.warn("low visual screen evidence count", 4)
    if sections < 10 and visual_total < 40:
        a.warn("low section evidence count", 3)
    if flows < 10 and visual_total < 40:
        a.warn("low flow evidence count", 3)
    if web_pages < 1:
        a.warn("no public web page source evidence", 3)

    if not entry.get("baseline_ids") and sid != "perplexity-answer-engine":
        a.warn("no mapped broad baseline ids", 2)

    # Guard against runtime instructions drifting back to external source collection.
    lower = design_text.lower()
    bad_runtime = [phrase for phrase in ["at runtime call", "runtime web search", "browse mobbin", "open github"] if phrase in lower]
    if bad_runtime:
        a.fail("unified DESIGN.md contains unsafe runtime external-source instruction: " + ", ".join(bad_runtime))

    a.clamp()
    return a


def verdict(score: int, blockers: list[str]) -> str:
    if blockers:
        return "BLOCKED"
    if score >= 92:
        return "STRONG"
    if score >= 85:
        return "GOOD"
    if score >= 75:
        return "USABLE_WITH_GAPS"
    return "WEAK"


def main() -> int:
    reg_path = PACK / "registry.json"
    reg, err = json_load(reg_path)
    if err or not isinstance(reg, dict):
        print(f"ERROR: invalid pack registry: {err}")
        return 2
    styles = reg.get("styles", [])
    audits = [audit_style(entry) for entry in styles]
    blockers = sum(len(a.blockers) for a in audits)
    avg = round(sum(a.score for a in audits) / max(1, len(audits)), 1)
    weak = [a for a in audits if verdict(a.score, a.blockers) not in {"STRONG", "GOOD"}]

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    lines: list[str] = []
    lines.append("# Agent Style Usability Audit")
    lines.append("")
    lines.append("Audit target: `pack/` unified runtime design pack.")
    lines.append("")
    lines.append(f"- Styles audited: `{len(audits)}`")
    lines.append(f"- Average score: `{avg}`")
    lines.append(f"- Blockers: `{blockers}`")
    lines.append(f"- Non-GOOD styles: `{len(weak)}`")
    lines.append("")
    lines.append("## Score table")
    lines.append("")
    lines.append("| Style | Verdict | Score | Capsules | Component slices | Visual evidence | Web pages | Warnings |")
    lines.append("|---|---:|---:|---:|---:|---:|---:|---:|")
    for a in sorted(audits, key=lambda x: (x.blockers != [], x.score, x.style_id)):
        f = a.facts
        visual = int(f.get("mobbin_screens", 0)) + int(f.get("mobbin_sections", 0)) + int(f.get("mobbin_flows", 0)) + int(f.get("auth_screenshots", 0))
        lines.append(
            f"| `{a.style_id}` | {verdict(a.score, a.blockers)} | {a.score} | {f.get('capsules', 0)} | {f.get('component_slices', 0)} | {visual} | {f.get('web_pages', 0)} | {len(a.warnings)} |"
        )
    lines.append("")
    lines.append("## Findings by style")
    for a in audits:
        lines.append("")
        lines.append(f"### `{a.style_id}` — {verdict(a.score, a.blockers)} `{a.score}`")
        lines.append("")
        lines.append("Facts: " + ", ".join(f"`{k}={v}`" for k, v in sorted(a.facts.items())))
        if a.blockers:
            lines.append("")
            lines.append("Blockers:")
            for item in a.blockers:
                lines.append(f"- {item}")
        if a.warnings:
            lines.append("")
            lines.append("Warnings:")
            for item in a.warnings:
                lines.append(f"- {item}")
        if not a.blockers and not a.warnings:
            lines.append("")
            lines.append("No issues found by automated usability checks.")
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"REPORT: {REPORT}")
    print(f"styles={len(audits)} avg={avg} blockers={blockers} non_good={len(weak)}")
    for a in audits:
        print(f"{a.style_id}\t{verdict(a.score, a.blockers)}\t{a.score}\twarnings={len(a.warnings)}\tblockers={len(a.blockers)}")
    return 1 if blockers or weak else 0


if __name__ == "__main__":
    raise SystemExit(main())
