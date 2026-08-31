# Hermes Unified Design Pack — Default DESIGN.md

Use `pack/` as one consolidated design package.

## What this pack is

This pack is a fork-based expansion of VoltAgent `awesome-design-md`:

- VoltAgent provides broad `DESIGN.md` coverage across many brands and product categories.
- Hermes adds deeper evidence-backed extensions for selected styles: local evidence, tokens, component capsules, DOM/CSS captures, eval gates, and Gbrain component slices.

## Runtime load order

1. Open `pack/registry.json`.
2. Choose a style from `pack/styles/<style-id>/DESIGN.md` when a deep Hermes extension exists.
3. Otherwise choose a broad baseline from `pack/design-md/<brand>/DESIGN.md`.
4. For implementation detail, use `pack/extensions/<style-id>/` and `pack/components/<style-id>/`.

## Authority

A deep Hermes extension overrides broad VoltAgent baseline guidance. The baseline is the foundation; Hermes extension is the build-out.

## Boundary

Runtime agents use local files only. GitHub, Mobbin, Firecrawl, Browser/CDP, and auth sessions are build-time enrichment tools only.
