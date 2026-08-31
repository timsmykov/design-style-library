# Source Index — Anthropic / Claude

## Local visual corpus

- Screens: `evidence/mobbin/screens/` — 65 Claude web app/workbench/settings/screens.
- Sections: `evidence/mobbin/sections/` — 34 Claude/Anthropic website sections.
- Flows: `evidence/mobbin/flows/` — 112 flow screenshots across onboarding, login, settings, API onboarding, subscription, and upgrade flows.
- Corpus index: `evidence/mobbin/corpus-index.json`.
- Expanded corpus summary: `evidence/visual-corpus.md`.

Canonical provenance lives in `evidence/sources.yaml`.

## Public web extraction

- `evidence/web/pages/anthropic-claude-product.firecrawl.json` — Firecrawl HTTP 200 for `https://www.anthropic.com/claude`; saved markdown/html/links.
- `evidence/web/pages/claude-ai-home.firecrawl.json` — local direct Firecrawl attempt for `https://claude.ai/`; partial/403 in saved API run, but earlier plugin scrape returned readable content.

## Extracted implementation facts so far

- Claude public HTML exposes `data-theme="claude"`, `data-font="anthropic"`, and `data-density="comfortable"` hints.
- Claude public HTML includes clay accent SVG/CSS variable evidence: `var(--cds-clay, #d97757)`.
- Claude home metadata/theme color includes a warm light background hint: `hsl(60,11%,95%)`.
- Public nav/product IA emphasizes Meet Claude, Platform, Solutions, Pricing, Resources, Contact sales, Try Claude.

## Pending

- Browser/CDP computed styles for buttons, cards, nav, hero title, composer, sidebar selected state.
- CSS bundle extraction/dedup if needed.
- Golden examples and offline fresh-agent eval.
