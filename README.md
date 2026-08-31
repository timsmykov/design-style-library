# Design Style Library

Offline, self-contained repository of distilled design style packs for agents.

## Core invariant

Runtime agents use this repository only. Mobbin, Firecrawl, Browser Use, Playwright, CDP, CSS parsers, and vision analysis are **build-time extraction tools**, not runtime dependencies.

A style pack is ready only when a fresh agent can produce a useful interface, presentation, visual note, or data visualization from the local pack without calling Mobbin, web search, Firecrawl, or a browser.


## Unified runtime pack

This repo now exposes one runtime-facing package: `pack/`.

- Local fork: `https://github.com/timsmykov/awesome-design-md`
- Upstream: `https://github.com/VoltAgent/awesome-design-md`
- Unified pack: `pack/`
- Pack contract: `pack/DESIGN.md`
- Pack registry: `pack/registry.json`
- Broad catalog: `pack/design-md/`
- Deep extensions: `pack/styles/<style-id>/DESIGN.md`, `pack/extensions/<style-id>/`, `pack/components/<style-id>/`

VoltAgent is the foundation inside the pack; Hermes deep packs are the build-out/override layer inside the same pack. Historical `baselines/` and `styles/` paths remain source/provenance/build locations, not the runtime mental model.

## What a style pack contains

- local visual corpus exported from Mobbin or other legitimate references;
- local implementation evidence from public web pages where useful: HTML, CSS, fonts, computed styles;
- provenance for every source;
- distilled style DNA: principles, layout, hierarchy, interaction, voice, anti-patterns;
- normalized tokens: color, typography, spacing, radius, border, shadow, semantic roles;
- reusable patterns by medium/component;
- component capsules for targeted retrieval and implementation recipes;
- generated Gbrain export slices for semantic component lookup;
- golden examples and offline eval checklists.

## What it does not contain

- prompt files as canonical source of truth;
- runtime Mobbin/web dependency;
- copied proprietary production CSS as a dependency;
- logo/brand impersonation or pixel-perfect clones.

Prompts, if needed, are derived at runtime from `STYLE.md`, `tokens/`, `patterns/`, and `eval/`.

## Sharing boundary

The GitHub distribution is built as a clean snapshot rather than by pushing the
server repository history. Private G-Brain exports and raw captures containing
embedded client API configuration are excluded. See `SHARING.md` before making
the repository public or redistributing captured reference assets.

## Repository layout

```text
registry.yaml
schemas/
tools/
docs/
styles/
  <style-id>/
    manifest.yaml
    STYLE.md
    agent-contract.md
    evidence/
    dna/
    tokens/
    patterns/
    components/
      component-atlas.md
      capsules/*.md
      component-index.jsonl
    examples/
    eval/
```

## First wave

1. Define the style-pack contract and offline-readiness gate.
2. Create skeleton and evidence archive layout.
3. Define extraction/distillation factory.
4. Rebuild Anthropic/Claude as the first real pack.
5. Build component-level retrieval: repo as source of truth, Gbrain as semantic index over compact generated slices.
6. Distill Perplexity as the second pack to prove the factory generalizes.
