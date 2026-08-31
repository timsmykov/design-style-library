# Build-time Extraction and Distillation Pipeline

## Principle

External tools are used to build and refresh the repository. Runtime agents must not depend on them.

```text
Mobbin visual export + public web extraction + rendered style probes
  -> local evidence archive
  -> observations
  -> distilled DNA/tokens/patterns/eval
  -> offline style pack
```

## Lane A — Mobbin visual corpus

Use Mobbin MCP to find screens, flows, and sections. Export the returned images into the local pack:

```text
evidence/mobbin/screens/
evidence/mobbin/flows/<flow-id>/
evidence/mobbin/sections/
```

For each asset, write a source record in `evidence/sources.yaml` with:

- stable local id;
- original Mobbin URL;
- local file path;
- capture date;
- platform;
- UI moment;
- observed patterns;
- rights/provenance note.

Mobbin links are provenance, not runtime dependencies.

## Lane B — Firecrawl public web extraction

Use Firecrawl for known public URLs after source selection:

- marketing pages;
- docs/product pages;
- pricing/trust pages;
- static HTML/CSS/links/metadata extraction.

Store outputs under:

```text
evidence/web/pages/
evidence/web/css/
evidence/web/fonts/
```

Do not use Firecrawl for login flows, CAPTCHA, paywalls, screenshots, or element actions.

## Lane C — Browser/Playwright/CDP rendered probes

Use Browser/Playwright/CDP when rendered truth matters:

- computed styles of target elements;
- screenshots of public pages;
- DOM structure after JS hydration;
- layout measurements and responsive breakpoints.

Store outputs under:

```text
evidence/web/computed/
evidence/web/screenshots/
```

## Lane D — CSS/token extraction

Parse local CSS and computed-style JSON to propose token candidates:

- colors;
- fonts;
- spacing;
- radius;
- shadows;
- borders;
- breakpoints.

Token candidates must be normalized into semantic roles before becoming `tokens/tokens.json`.

## Distillation loop

1. Export raw local evidence.
2. Add source/provenance index.
3. Write observations by screen/flow/page/component.
4. Cluster observations into mechanisms, not app names.
5. Distill `STYLE.md` and `dna/*.md`.
6. Normalize tokens.
7. Write patterns and anti-patterns.
8. Generate golden examples.
9. Run offline eval.

## Guardrails

- Do not copy proprietary code as a dependency.
- Do not impersonate logos/brands.
- Do not create pixel-perfect clones.
- Extract observable design facts and translate them into original reusable style systems.
- Record limitations and confidence for every source.
