# Unified DESIGN.md — Figma Collaborative Canvas

This file is the single-pack runtime view for `figma-collaborative-canvas`.

Authority inside this file:

1. VoltAgent DESIGN.md baseline gives broad visual grammar.
2. Hermes deep extension overrides baseline with local evidence, tokens, components, eval, and implementation guardrails.
3. Use local paths only; do not call GitHub/Mobbin/web/browser at runtime.

Local extension root: `pack/extensions/figma-collaborative-canvas`
Component semantic slices: `pack/components/figma-collaborative-canvas`

---

## Baseline: `figma`

Source: `pack/design-md/figma/DESIGN.md`

---
version: alpha
name: Figma-design-analysis
description: "A confident black-and-white editorial frame interrupted by oversized, hand-cut pastel color blocks. The marketing canvas is rigorously monochrome — figmaSans variable type, pure white surfaces, pure black ink, pill-shaped CTAs — while each story section drops the page into a saturated lime, lavender, cream, mint, or pink panel that reads like a sticky note placed on a clean desk. The result is a design system that feels both technical and joyful — a tool for serious work, made by people who like color."

colors:
  primary: "#000000"
  on-primary: "#ffffff"
  ink: "#000000"
  canvas: "#ffffff"
  inverse-canvas: "#000000"
  inverse-ink: "#ffffff"
  on-inverse-soft: "#ffffff"
  hairline: "#e6e6e6"
  hairline-soft: "#f1f1f1"
  surface-soft: "#f7f7f5"
  block-lime: "#dceeb1"
  block-lilac: "#c5b0f4"
  block-cream: "#f4ecd6"
  block-pink: "#efd4d4"
  block-mint: "#c8e6cd"
  block-coral: "#f3c9b6"
  block-navy: "#1f1d3d"
  accent-magenta: "#ff3d8b"
  semantic-success: "#1ea64a"
  overlay-scrim: "#000000"

typography:
  display-xl:
    fontFamily: figmaSans
    fontSize: 86px
    fontWeight: 340
    lineHeight: 1.00
    letterSpacing: -1.72px
    fontFeature: kern
  display-lg:
    fontFamily: figmaSans
    fontSize: 64px
    fontWeight: 340
    lineHeight: 1.10
    letterSpacing: -0.96px
    fontFeature: kern
  headline:
    fontFamily: figmaSans
    fontSize: 26px
    fontWeight: 540
    lineHeight: 1.35
    letterSpacing: -0.26px
    fontFeature: kern
  subhead:
    fontFamily: figmaSans
    fontSize: 26px
    fontWeight: 340
    lineHeight: 1.35
    letterSpacing: -0.26px
    fontFeature: kern
  card-title:
    fontFamily: figmaSans
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.45
    letterSpacing: 0
    fontFeature: kern
  body-lg:
    fontFamily: figmaSans
    fontSize: 20px
    fontWeight: 330
    lineHeight: 1.40
    letterSpacing: -0.14px
    fontFeature: kern
  body:
    fontFamily: figmaSans
    fontSize: 18px
    fontWeight: 320
    lineHeight: 1.45
    letterSpacing: -0.26px
    fontFeature: kern
  body-sm:
    fontFamily: figmaSans
    fontSize: 16px
    fontWeight: 330
    lineHeight: 1.45
    letterSpacing: -0.14px
    fontFeature: kern
  link:
    fontFamily: figmaSans
    fontSize: 20px
    fontWeight: 480
    lineHeight: 1.40
    letterSpacing: -0.10px
    fontFeature: kern
  button:
    fontFamily: figmaSans
    fontSize: 20px
    fontWeight: 480
    lineHeight: 1.40
    letterSpacing: -0.10px
    fontFeature: kern
  eyebrow:
    fontFamily: figmaMono
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.30
    letterSpacing: 0.54px
    fontFeature: kern
  caption:
    fontFamily: figmaMono
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.00
    letterSpacing: 0.60px
    fontFeature: kern

rounded:
  xs: 2px
  sm: 6px
  md: 8px
  lg: 24px
  xl: 32px
  pill: 50px
  full: 9999px

spacing:
  hair: 1px
  xxs: 4px
  xs: 8px
  sm: 12px
  md: 16px
  lg: 24px
  xl: 32px
  xxl: 48px
  section: 96px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 10px 20px
  button-primary-pressed:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 8px 18px 10px
  button-tertiary-text:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.link}"
    rounded: "{rounded.full}"
    padding: 8px 12px
  button-icon-circular:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.full}"
    size: 40px
  button-icon-circular-inverse:
    backgroundColor: "{colors.on-inverse-soft}"
    textColor: "{colors.inverse-ink}"
    typography: "{typography.button}"
    rounded: "{rounded.full}"
    size: 40px
  button-magenta-promo:
    backgroundColor: "{colors.accent-magenta}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 10px 18px
  pricing-tab-default:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 8px 18px
  pricing-tab-selected:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 8px 18px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 12px 14px
  text-input-focused:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 12px 14px
  pricing-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.lg}"
    padding: 24px
  pricing-card-feature-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
  color-block-section:
    backgroundColor: "{colors.block-lime}"
    textColor: "{colors.ink}"
    typography: "{typography.subhead}"
    rounded: "{rounded.lg}"
    padding: 48px
  color-block-section-lilac:
    backgroundColor: "{colors.block-lilac}"
    textColor: "{colors.ink}"
    typography: "{typography.subhead}"
    rounded: "{rounded.lg}"
    padding: 48px
  color-block-section-navy:
    backgroundColor: "{colors.block-navy}"
    textColor: "{colors.inverse-ink}"
    typography: "{typography.subhead}"
    rounded: "{rounded.lg}"
    padding: 48px
  promo-banner-lilac:
    backgroundColor: "{colors.block-lilac}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 16px 24px
  template-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 16px
  feature-illustration-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.eyebrow}"
    rounded: "{rounded.md}"
    padding: 24px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    height: 56px
  marquee-strip:
    backgroundColor: "{colors.inverse-canvas}"
    textColor: "{colors.inverse-ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    height: 36px
  comparison-checkmark:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.semantic-success}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    size: 16px
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 64px 32px
---

## Overview

Figma's marketing canvas is, at the system level, an editor-clean black-and-white frame. The chrome — top nav, body type, footer, primary CTA — is monochrome. Headlines are oversized `{typography.display-xl}` set in `figmaSans` with aggressive negative tracking, body copy hovers around weight 320–340 of the same variable family, and small mono `{typography.eyebrow}` and `{typography.caption}` labels (figmaMono, all-caps, positive tracking) act as section markers. Every CTA is a pill — `{rounded.pill}` — and the primary action across the entire site is the same black `{components.button-primary}` paired with the same white `{components.button-secondary}`.

What makes the design unique is what happens **between** those monochrome bookends: th

[truncated in unified pack view; see source file for full content]


---

# Hermes deep extension override

## STYLE.md excerpt

# Figma Collaborative Canvas

Status: runtime-ready extension inside the unified Hermes design pack.

## Style formula

collaborative canvas product system; editor chrome with toolbars/layers/properties; bright brand shapes outside product; multiplayer comments and precise inspector controls

This pack is meant for generation, review, and critique. It should give an agent enough local information to design a screen without opening Mobbin, GitHub, a browser, or any external gallery. The goal is style grammar and product-pattern transfer, not brand impersonation or exact screen cloning.

## When to use

Use this style when the requested artifact matches the product job, emotional temperature, and UI density of `figma-collaborative-canvas`. If the task names this brand/style directly, use this extension. If the task only names a category, route here when the component set below matches the requested surface better than the other packs.

## Visual and interaction principles

- Start from the user job and select the closest local component capsule before choosing colors or decorative treatment.
- Preserve hierarchy first: primary object, secondary metadata, tertiary controls, then ambient decoration.
- Use the token system rather than ad-hoc colors. Color anchors: `canvas`=#ffffff; `surface`=#f5f5f5; `panel`=#ffffff; `text`=#1f2937; `muted`=#6b7280; `border`=#d1d5db; `accent`=#a259ff; `accent2`=#1abcfe.
- Use the typography roles deliberately. Type anchors: `ui`=Inter/system sans-serif; `mono`=ui-monospace/SFMono-Regular.
- Respect the shape and density system: spacing scale present, radius scale present.
- Prefer restrained adaptation over literal copying. Do not reuse logos, exact text, private data, or proprietary screen layout one-to-one.

## Runtime component set

- `canvas-editor-shell` — canvas editor shell
- `comment-thread` — comment thread
- `figjam-board` — figjam board
- `file-browser-grid` — file browser grid
- `layers-panel` — layers panel
- `multiplayer-presence` — multiplayer presence
- `pricing-plan-grid` — pricing plan grid
- `properties-inspector` — properties inspector
- `prototype-flow` — prototype flow
- `toolbar-controls` — toolbar controls

For each component, load the capsule in `components/capsules/<component-id>.md` first. Then use `components/extracted/` and `evidence/source-map/` only when you need provenance or visual facts. Use `pack/components/figma-collaborative-canvas/` for short semantic slices when a retrieval system asks for compact component context.

## Evidence coverage

- Mobbin screens: 20
- Mobbin sections: 20
- Mobbin flow previews: 20
- Public web pages captured: 2
- Authenticated screenshots: 0

These are build-time artifacts already stored locally. Runtime agents must not fetch more evidence unless explicitly asked to run a new extraction wave.

## Agent recipe

1. Read `pack/styles/figma-collaborative-canvas/DESIGN.md` for the unified baseline + extension view.
2. Load `pack/extensions/figma-collaborative-canvas/tokens/tokens.json` and `tokens/css-vars.css` for implementation values.
3. Pick 1-3 capsules from `pack/extensions/figma-collaborative-canvas/components/capsules/` that match the requested screen.
4. Compose with the local style formula and component grammar.
5. Run the result against `pack/extensions/figma-collaborative-canvas/eval/checklist.yaml` and `eval/failure-modes.md`.
6. If the output feels generic, increase fidelity through component structure and hierarchy, not by copying exact source screens.

## Do

- Use local tokens and capsules as the first source of truth.
- Make state, status, and user action obvious.
- Keep density and spacing consistent across related surfaces.
- Use evidence-backed component vocabulary when describing or implementing the UI.

## Do not

- Do not call web search, GitHub, Mobbin, browser/CDP, or external services at runtime for style guidance.
- Do not clone exact production screens, logos, copy, private account data, or proprietary code.
- Do not mix this style with another pack unless the user explicitly asks for a hybrid.
- Do not substitute a moodboard description for component-level structure.


## Component atlas excerpt

# Component atlas

Runtime component atlas for `figma-collaborative-canvas`.

Use this file to choose the right capsule before implementation. The capsule is the detailed recipe; this atlas is the router.

## `canvas-editor-shell` — Figma Collaborative Canvas — Canvas Editor Shell

Use when: the artifact needs `canvas editor shell` behavior, layout, or decision structure.
Capsule: `components/capsules/canvas-editor-shell.md`
Semantic slice: `pack/components/figma-collaborative-canvas/canvas-editor-shell.md`
Evidence links recorded: `2` index path groups; see local source map and extracted folders for detail.

Design job:
- Preserve this style formula: collaborative canvas product system; editor chrome with toolbars/layers/properties; bright brand shapes outside product; multiplayer comments and precise inspector controls
- Keep the component's primary object obvious before adding decoration.
- Use token roles and density from `tokens/tokens.json` instead of inventing ad-hoc values.
- Adapt the grammar to the new product context; do not clone exact evidence screens.

Implementation notes:
- Start with semantic structure and states.
- Add controls, status, metadata, and supporting copy in that order.
- Check responsive behavior and empty/error/loading states when relevant.

Evidence excerpt:
> # Canvas Editor Shell Use this capsule when the artifact needs `canvas editor shell` behavior in the Figma Collaborative Canvas style. ## Grammar - Style formula: collaborative canvas product system; editor chrome with toolbars/layers/properties; bright brand shapes outside product; multiplayer comments and precise inspector controls - Evidence refs: 6 local images. - Token anchors: canvas `#ffffff`, surface `#f5f5f5`, text `#1f2937`, accent `#a259ff`. - Preserve information hierarchy and action

## `comment-thread` — Figma Collaborative Canvas — Comment Thread

Use when: the artifact needs `comment thread` behavior, layout, or decision structure.
Capsule: `components/capsules/comment-thread.md`
Semantic slice: `pack/components/figma-collaborative-canvas/comment-thread.md`
Evidence links recorded: `2` index path groups; see local source map and extracted folders for detail.

Design job:
- Preserve this style formula: collaborative canvas product system; editor chrome with toolbars/layers/properties; bright brand shapes outside product; multiplayer comments and precise inspector controls
- Keep the component's primary object obvious before adding decoration.
- Use token roles and density from `tokens/tokens.json` instead of inventing ad-hoc values.
- Adapt the grammar to the new product context; do not clone exact evidence screens.

Implementation notes:
- Start with semantic structure and states.
- Add controls, status, metadata, and supporting copy in that order.
- Check responsive behavior and empty/error/loading states when relevant.

Evidence excerpt:
> # Comment Thread Use this capsule when the artifact needs `comment thread` behavior in the Figma Collaborative Canvas style. ## Grammar - Style formula: collaborative canvas product system; editor chrome with toolbars/layers/properties; bright brand shapes outside product; multiplayer comments and precise inspector controls - Evidence refs: 6 local images. - Token anchors: canvas `#ffffff`, surface `#f5f5f5`, text `#1f2937`, accent `#a259ff`. - Preserve information hierarchy and action semantics

## `figjam-board` — Figma Collaborative Canvas — Figjam Board

Use when: the artifact needs `figjam board` behavior, layout, or decision structure.
Capsule: `components/capsules/figjam-board.md`
Semantic slice: `pack/components/figma-collaborative-canvas/figjam-board.md`
Evidence links recorded: `2` index path groups; see local source map and extracted folders for detail.

Design job:
- Preserve this style formula: collaborative canvas product system; editor chrome with toolbars/layers/properties; bright brand shapes outside product; multiplayer comments and precise inspector controls
- Keep the component's primary object obvious before adding decoration.
- Use token roles and density from `tokens/tokens.json` instead of inventing ad-hoc values.
- Adapt the grammar to the new product context; do not clone exact evidence screens.

Implementation notes:
- Start with semantic structure and states.
- Add controls, status, metadata, and supporting copy in that order.
- Check responsive behavior and empty/error/loading states when relevant.

Evidence excerpt:
> # Figjam Board Use this capsule when the artifact needs `figjam board` behavior in the Figma Collaborative Canvas style. ## Grammar - Style formula: collaborative canvas product system; editor chrome with toolbars/layers/properties; bright brand shapes outside product; multiplayer comments and precise inspector controls - Evidence refs: 6 local images. - Token anchors: canvas `#ffffff`, surface `#f5f5f5`, text `#1f2937`, accent `#a259ff`. - Preserve information hierarchy and action semantics; ad

## `file-browser-grid` — Fi

[truncated in unified pack view; see source file for full content]


## Agent contract excerpt

# Agent contract — Figma Collaborative Canvas

This contract tells an agent how to use `figma-collaborative-canvas` inside the unified Hermes design pack.

## Required load order

1. `pack/styles/figma-collaborative-canvas/DESIGN.md` — unified style entry and broad baseline context.
2. `pack/extensions/figma-collaborative-canvas/STYLE.md` — concise runtime formula and operating rules.
3. `pack/extensions/figma-collaborative-canvas/tokens/tokens.json` plus `tokens/css-vars.css` — implementation anchors.
4. `pack/extensions/figma-collaborative-canvas/components/component-atlas.md` — choose the closest reusable surface.
5. `pack/extensions/figma-collaborative-canvas/components/capsules/<component-id>.md` — detailed component grammar.
6. `pack/components/figma-collaborative-canvas/<component-id>.md` — compact semantic retrieval slice.
7. `pack/extensions/figma-collaborative-canvas/eval/checklist.yaml`, `eval/rubric.md`, and `eval/failure-modes.md` — quality gate.

## Authority rule

The deep Hermes extension overrides the broad VoltAgent baseline whenever they differ. The baseline provides vocabulary; this extension provides implementation constraints, local evidence, component structure, and failure modes.

## Runtime boundary

Use local files only. GitHub, Mobbin, Firecrawl, Browser/CDP, Playwright, and authenticated sessions are build-time enrichment lanes. Runtime style use should remain offline, deterministic, and repo-first.

## Generation protocol

- Identify the product job and information hierarchy before styling.
- Select the nearest component capsule by semantic job, not by visual decoration.
- Apply tokens exactly where possible; when adapting, keep role semantics stable.
- Preserve accessibility basics: readable contrast, usable target sizes, clear focus/selected/error states.
- State uncertainty if the requested surface has no matching capsule, then compose from the closest primitives.

## Review protocol

A result is acceptable only if it passes the local eval layer and can name which capsules/tokens shaped it. If it cannot cite local pack paths, it did not really use the style system.

## Safety

Adapt style grammar. Do not impersonate the brand, reuse logos, reproduce exact screens, copy private data, or import proprietary source code.
