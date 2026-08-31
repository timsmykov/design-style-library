# Unified DESIGN.md — Linear Operational Workspace

This file is the single-pack runtime view for `linear-operational-workspace`.

Authority inside this file:

1. VoltAgent DESIGN.md baseline gives broad visual grammar.
2. Hermes deep extension overrides baseline with local evidence, tokens, components, eval, and implementation guardrails.
3. Use local paths only; do not call GitHub/Mobbin/web/browser at runtime.

Local extension root: `pack/extensions/linear-operational-workspace`
Component semantic slices: `pack/components/linear-operational-workspace`

---

## Baseline: `linear.app`

Source: `pack/design-md/linear.app/DESIGN.md`

---
version: alpha
name: Linear-design-analysis
description: "A near-black product-focused marketing canvas built around #010102 (the deepest dark surface of any tool in this collection), light gray text (#f7f8f8), and the signature Linear lavender-blue (#5e6ad2) used as the single chromatic accent. The system reads as software-craft documentation: dense, technical, and quietly luxurious. Display type is set in the Linear custom sans (SF Pro Display fallback) at 500–700 with measured negative tracking. Cards live as charcoal panels (#0f1011) with hairline borders. The accent lavender appears on the brand mark, focus rings, and a few intentional CTAs — never decoratively. Page rhythm leans on product UI screenshots framed in dark panels rather than atmospheric color."

colors:
  primary: "#5e6ad2"
  on-primary: "#ffffff"
  primary-hover: "#828fff"
  primary-focus: "#5e69d1"
  ink: "#f7f8f8"
  ink-muted: "#d0d6e0"
  ink-subtle: "#8a8f98"
  ink-tertiary: "#62666d"
  canvas: "#010102"
  surface-1: "#0f1011"
  surface-2: "#141516"
  surface-3: "#18191a"
  surface-4: "#191a1b"
  hairline: "#23252a"
  hairline-strong: "#34343a"
  hairline-tertiary: "#3e3e44"
  inverse-canvas: "#ffffff"
  inverse-surface-1: "#f5f6f6"
  inverse-surface-2: "#f6f7f7"
  inverse-ink: "#000000"
  brand-secure: "#7a7fad"
  semantic-success: "#27a644"
  semantic-overlay: "#000000"

typography:
  display-xl:
    fontFamily: Linear Display
    fontSize: 80px
    fontWeight: 600
    lineHeight: 1.05
    letterSpacing: -3.0px
  display-lg:
    fontFamily: Linear Display
    fontSize: 56px
    fontWeight: 600
    lineHeight: 1.10
    letterSpacing: -1.8px
  display-md:
    fontFamily: Linear Display
    fontSize: 40px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -1.0px
  headline:
    fontFamily: Linear Display
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.20
    letterSpacing: -0.6px
  card-title:
    fontFamily: Linear Display
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: -0.4px
  subhead:
    fontFamily: Linear Display
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.40
    letterSpacing: -0.2px
  body-lg:
    fontFamily: Linear Text
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: -0.1px
  body:
    fontFamily: Linear Text
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: -0.05px
  body-sm:
    fontFamily: Linear Text
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0
  caption:
    fontFamily: Linear Text
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.40
    letterSpacing: 0
  button:
    fontFamily: Linear Text
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.20
    letterSpacing: 0
  eyebrow:
    fontFamily: Linear Text
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.30
    letterSpacing: 0.4px
  mono:
    fontFamily: Linear Mono
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0

rounded:
  xs: 4px
  sm: 6px
  md: 8px
  lg: 12px
  xl: 16px
  xxl: 24px
  pill: 9999px
  full: 9999px

spacing:
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
    rounded: "{rounded.md}"
    padding: 8px 14px
  button-primary-pressed:
    backgroundColor: "{colors.primary-focus}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
  button-secondary:
    backgroundColor: "{colors.surface-1}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 8px 14px
  button-tertiary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 8px 14px
  button-inverse:
    backgroundColor: "{colors.inverse-canvas}"
    textColor: "{colors.inverse-ink}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 8px 14px
  pricing-card:
    backgroundColor: "{colors.surface-1}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.lg}"
    padding: 24px
  pricing-card-featured:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.lg}"
    padding: 24px
  feature-card:
    backgroundColor: "{colors.surface-1}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.lg}"
    padding: 24px
  product-screenshot-card:
    backgroundColor: "{colors.surface-1}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.xl}"
    padding: 24px
  testimonial-card:
    backgroundColor: "{colors.surface-1}"
    textColor: "{colors.ink}"
    typography: "{typography.body-lg}"
    rounded: "{rounded.lg}"
    padding: 32px
  customer-logo-tile:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink-subtle}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 16px
  text-input:
    backgroundColor: "{colors.surface-1}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 8px 12px
  text-input-focused:
    backgroundColor: "{colors.surface-1}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 8px 12px
  pricing-tab-default:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink-subtle}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 6px 14px
  pricing-tab-selected:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 6px 14px
  cta-banner:
    backgroundColor: "{colors.surface-1}"
    textColor: "{colors.ink}"
    typography: "{typography.headline}"
    rounded: "{rounded.lg}"
    padding: 48px
  changelog-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.xs}"
    padding: 24px 0
  status-badge:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.ink-muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.pill}"
    padding: 2px 8px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    height: 56px
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink-subtle}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 64px 32px
---

## Overview

Linear's marketing canvas is the deepest dark surface in this collection — `{colors.canvas}` is #010102, essentially pure black with a faint blue tint. On top sits a four-step surface ladder (`{colors.surface-1}` through `{colors.surface-4}`) for cards, panels, and lifted tiles, with hairline borders running from `{colors.hairline}` (#23252a) up through `{colors.hairline-strong}` and `{colors.hairline-tertiary}`. Light gray text (`{colors.ink}` #f7f8f8) carries the body and headlines.

The single chromatic accent is **Linear lavender-blue** `{colors.primary}` (#5e6ad2) — used on the brand mark, focus rings, and the primary CTA button. A lighter hover state (`{colors.primary-hover}` #828fff) and a focus-tinted variant (`{colors.primary-focus}` #5e69d1) extend the same hue. Linear avoids saturated greens, oranges, reds, etc. on the marketing canvas — the only semantic color is `{colors.semantic-success}` (#27a644) for status pills and the rare success indicator.

Display type runs Linear's custom sans (wi

[truncated in unified pack view; see source file for full content]


---

# Hermes deep extension override

## STYLE.md excerpt

# Linear Operational Workspace

Status: runtime-ready extension inside the unified Hermes design pack.

## Style formula

dark precision workspace; quiet purple-blue semantic accents; dense keyboard-native issue/project operations; glassy black marketing gradients; sparse high-signal status metadata

This pack is meant for generation, review, and critique. It should give an agent enough local information to design a screen without opening Mobbin, GitHub, a browser, or any external gallery. The goal is style grammar and product-pattern transfer, not brand impersonation or exact screen cloning.

## When to use

Use this style when the requested artifact matches the product job, emotional temperature, and UI density of `linear-operational-workspace`. If the task names this brand/style directly, use this extension. If the task only names a category, route here when the component set below matches the requested surface better than the other packs.

## Visual and interaction principles

- Start from the user job and select the closest local component capsule before choosing colors or decorative treatment.
- Preserve hierarchy first: primary object, secondary metadata, tertiary controls, then ambient decoration.
- Use the token system rather than ad-hoc colors. Color anchors: `canvas`=#08090d; `surface`=#111217; `panel`=#191a22; `text`=#f7f8ff; `muted`=#9ca3b7; `border`=#2a2d39; `accent`=#5e6ad2; `accent2`=#8b5cf6.
- Use the typography roles deliberately. Type anchors: `ui`=Inter/system sans-serif; `mono`=ui-monospace/SFMono-Regular.
- Respect the shape and density system: spacing scale present, radius scale present.
- Prefer restrained adaptation over literal copying. Do not reuse logos, exact text, private data, or proprietary screen layout one-to-one.

## Runtime component set

- `command-menu` — command menu
- `cycle-status-panel` — cycle status panel
- `integration-settings` — integration settings
- `issue-detail-pane` — issue detail pane
- `issue-list-table` — issue list table
- `onboarding-workspace` — onboarding workspace
- `pricing-feature-grid` — pricing feature grid
- `project-roadmap-board` — project roadmap board
- `status-priority-pill` — status priority pill
- `workspace-sidebar` — workspace sidebar

For each component, load the capsule in `components/capsules/<component-id>.md` first. Then use `components/extracted/` and `evidence/source-map/` only when you need provenance or visual facts. Use `pack/components/linear-operational-workspace/` for short semantic slices when a retrieval system asks for compact component context.

## Evidence coverage

- Mobbin screens: 30
- Mobbin sections: 30
- Mobbin flow previews: 29
- Public web pages captured: 2
- Authenticated screenshots: 1

These are build-time artifacts already stored locally. Runtime agents must not fetch more evidence unless explicitly asked to run a new extraction wave.

## Agent recipe

1. Read `pack/styles/linear-operational-workspace/DESIGN.md` for the unified baseline + extension view.
2. Load `pack/extensions/linear-operational-workspace/tokens/tokens.json` and `tokens/css-vars.css` for implementation values.
3. Pick 1-3 capsules from `pack/extensions/linear-operational-workspace/components/capsules/` that match the requested screen.
4. Compose with the local style formula and component grammar.
5. Run the result against `pack/extensions/linear-operational-workspace/eval/checklist.yaml` and `eval/failure-modes.md`.
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

Runtime component atlas for `linear-operational-workspace`.

Use this file to choose the right capsule before implementation. The capsule is the detailed recipe; this atlas is the router.

## `command-menu` — Linear Operational Workspace — Command Menu

Use when: the artifact needs `command menu` behavior, layout, or decision structure.
Capsule: `components/capsules/command-menu.md`
Semantic slice: `pack/components/linear-operational-workspace/command-menu.md`
Evidence links recorded: `2` index path groups; see local source map and extracted folders for detail.

Design job:
- Preserve this style formula: dark precision workspace; quiet purple-blue semantic accents; dense keyboard-native issue/project operations; glassy black marketing gradients; sparse high-signal status metadata
- Keep the component's primary object obvious before adding decoration.
- Use token roles and density from `tokens/tokens.json` instead of inventing ad-hoc values.
- Adapt the grammar to the new product context; do not clone exact evidence screens.

Implementation notes:
- Start with semantic structure and states.
- Add controls, status, metadata, and supporting copy in that order.
- Check responsive behavior and empty/error/loading states when relevant.

Evidence excerpt:
> # Command Menu Use this capsule when the artifact needs `command menu` behavior in the Linear Operational Workspace style. ## Grammar - Style formula: dark precision workspace; quiet purple-blue semantic accents; dense keyboard-native issue/project operations; glassy black marketing gradients; sparse high-signal status metadata - Evidence refs: 9 local images. - Token anchors: canvas `#08090d`, surface `#111217`, text `#f7f8ff`, accent `#5e6ad2`. - Preserve information hierarchy and action seman

## `cycle-status-panel` — Linear Operational Workspace — Cycle Status Panel

Use when: the artifact needs `cycle status panel` behavior, layout, or decision structure.
Capsule: `components/capsules/cycle-status-panel.md`
Semantic slice: `pack/components/linear-operational-workspace/cycle-status-panel.md`
Evidence links recorded: `2` index path groups; see local source map and extracted folders for detail.

Design job:
- Preserve this style formula: dark precision workspace; quiet purple-blue semantic accents; dense keyboard-native issue/project operations; glassy black marketing gradients; sparse high-signal status metadata
- Keep the component's primary object obvious before adding decoration.
- Use token roles and density from `tokens/tokens.json` instead of inventing ad-hoc values.
- Adapt the grammar to the new product context; do not clone exact evidence screens.

Implementation notes:
- Start with semantic structure and states.
- Add controls, status, metadata, and supporting copy in that order.
- Check responsive behavior and empty/error/loading states when relevant.

Evidence excerpt:
> # Cycle Status Panel Use this capsule when the artifact needs `cycle status panel` behavior in the Linear Operational Workspace style. ## Grammar - Style formula: dark precision workspace; quiet purple-blue semantic accents; dense keyboard-native issue/project operations; glassy black marketing gradients; sparse high-signal status metadata - Evidence refs: 9 local images. - Token anchors: canvas `#08090d`, surface `#111217`, text `#f7f8ff`, accent `#5e6ad2`. - Preserve information hierarchy and 

## `integration-settings` — Linear Operational Workspace — Integration Settings

Use when: the artifact needs `integration settings` behavior, layout, or decision structure.
Capsule: `components/capsules/integration-settings.md`
Semantic slice: `pack/components/linear-operational-workspace/integration-settings.md`
Evidence links recorded: `2` index path groups; see local source map and extracted folders for detail.

Design job:
- Preserve this style formula: dark precision workspace; quiet purple-blue semantic accents; dense keyboard-native issue/project operations; glassy black marketing gradients; sparse high-signal status metadata
- Keep the component's primary object obvious before adding decoration.
- Use token roles and density from `tokens/tokens.json` instead of inventing ad-hoc values.
- Adapt the grammar to the new product context; do not clone exact evidence screens.

Implementation notes:
- Start with semantic structure and states.
- Add controls, status, metadata, and supporting copy in that order.
- Check responsive behavior and empty/error/loading states when relevant.

Evidence excerpt:
> # Integration Settings Use this capsule when the artifact needs `integration settings` behavior in the Linear Operational Workspace style. ## Grammar - Style formula: dark precision workspace; quiet purple-blue semantic accents; dense keyboard-native issue/project operations; glassy black marketing gradients; sparse high-signal status metadata - Evidence refs: 9 local images. - Token anchors: canvas `#08090d`, surface `#111217`, text `#f7f8ff`, accent `#5e6ad2`. - Pre

[truncated in unified pack view; see source file for full content]


## Agent contract excerpt

# Agent contract — Linear Operational Workspace

This contract tells an agent how to use `linear-operational-workspace` inside the unified Hermes design pack.

## Required load order

1. `pack/styles/linear-operational-workspace/DESIGN.md` — unified style entry and broad baseline context.
2. `pack/extensions/linear-operational-workspace/STYLE.md` — concise runtime formula and operating rules.
3. `pack/extensions/linear-operational-workspace/tokens/tokens.json` plus `tokens/css-vars.css` — implementation anchors.
4. `pack/extensions/linear-operational-workspace/components/component-atlas.md` — choose the closest reusable surface.
5. `pack/extensions/linear-operational-workspace/components/capsules/<component-id>.md` — detailed component grammar.
6. `pack/components/linear-operational-workspace/<component-id>.md` — compact semantic retrieval slice.
7. `pack/extensions/linear-operational-workspace/eval/checklist.yaml`, `eval/rubric.md`, and `eval/failure-modes.md` — quality gate.

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
