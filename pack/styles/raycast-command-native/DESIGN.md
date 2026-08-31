# Unified DESIGN.md — Raycast Command Native

This file is the single-pack runtime view for `raycast-command-native`.

Authority inside this file:

1. VoltAgent DESIGN.md baseline gives broad visual grammar.
2. Hermes deep extension overrides baseline with local evidence, tokens, components, eval, and implementation guardrails.
3. Use local paths only; do not call GitHub/Mobbin/web/browser at runtime.

Local extension root: `pack/extensions/raycast-command-native`
Component semantic slices: `pack/components/raycast-command-native`

---

## Baseline: `raycast`

Source: `pack/design-md/raycast/DESIGN.md`

---
version: alpha
name: Raycast-design-analysis
属于: A dark-canvas developer-tools system that treats the marketing page like an extended product screenshot — pure-near-black background, command-palette mockups as the hero, Inter typography with the ss03 stylistic set turned on, and a single white CTA pill that doesn't break the inky atmosphere. The chrome reads like Raycast's own command-palette UI scaled up to a marketing page: monochrome dark surfaces with a faint surface ladder (#07080a → #0d0d0d → #101111), tight 6–10px radius on cards, hairline 1px borders in #242728, and rare splashes of saturated accent (Hacker News yellow, Slack red, Mac green, info blue) reserved for product-tile category illustrations. The signature visual moment is a red gradient hero wordmark — three diagonal red stripes laid across the very top of the home page like a launch-banner — paired with full-bleed product UI screenshots that show Raycast's actual command palette, store, and AI chat surfaces.
description: |
  Raycast's marketing system reads like an extended product screenshot. The chrome IS the in-product chrome at marketing scale: pure-near-black canvas, hairline 1px borders, command-palette-style cards, Inter typography with the ss03 stylistic set enabled site-wide, white CTA pill, and a small set of saturated category accent colors (yellow / red / green / blue) reserved for extension and feature illustrations. Section rhythm is generous (~96px) but the page never breaks tonal continuity — the whole site sits in one continuous dark mode.

colors:
  primary: "#ffffff"
  primary-pressed: "#e8e8e8"
  on-primary: "#000000"
  ink: "#f4f4f6"
  body: "#cdcdcd"
  charcoal: "#d3d3d4"
  mute: "#9c9c9d"
  ash: "#6a6b6c"
  stone: "#434345"
  on-dark: "#ffffff"
  on-dark-mute: "rgba(255,255,255,0.72)"
  canvas: "#07080a"
  surface: "#0d0d0d"
  surface-elevated: "#101111"
  surface-card: "#121212"
  button-fg: "#18191a"
  hairline: "#242728"
  hairline-soft: "rgba(255,255,255,0.08)"
  hairline-strong: "rgba(255,255,255,0.16)"
  accent-blue: "#57c1ff"
  accent-blue-soft: "rgba(87,193,255,0.15)"
  accent-red: "#ff6161"
  accent-red-soft: "rgba(255,97,97,0.15)"
  accent-green: "#59d499"
  accent-green-soft: "rgba(89,212,153,0.15)"
  accent-yellow: "#ffc533"
  accent-yellow-soft: "rgba(255,197,51,0.15)"
  hero-stripe-start: "#ff5757"
  hero-stripe-end: "#a1131a"
  key-bg-start: "#121212"
  key-bg-end: "#0d0d0d"

typography:
  display-xl:
    fontFamily: Inter
    fontSize: 64px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: 0
    fontFeature: '"calt", "kern", "liga", "ss03"'
  display-lg:
    fontFamily: Inter
    fontSize: 56px
    fontWeight: 500
    lineHeight: 1.17
    letterSpacing: 0.2px
    fontFeature: '"calt", "kern", "liga", "ss03"'
  heading-xl:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.6
    letterSpacing: 0.2px
    fontFeature: '"calt", "kern", "liga", "ss03"'
  heading-lg:
    fontFamily: Inter
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: 0
    fontFeature: '"calt", "kern", "liga", "ss03"'
  heading-md:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
    fontFeature: '"calt", "kern", "liga", "ss03"'
  heading-sm:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
    fontFeature: '"calt", "kern", "liga", "ss03"'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
    fontFeature: '"calt", "kern", "liga", "ss03"'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
    fontFeature: '"calt", "kern", "liga", "ss03"'
  body-strong:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
    fontFeature: '"calt", "kern", "liga", "ss03"'
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
    fontFeature: '"calt", "kern", "liga", "ss03"'
  body-sm-strong:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.6
    letterSpacing: 0.2px
    fontFeature: '"calt", "kern", "liga", "ss03"'
  caption-md:
    fontFamily: Inter
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.1px
    fontFeature: '"calt", "kern", "liga", "ss03"'
  caption-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.4px
    fontFeature: '"calt", "kern", "liga", "ss03"'
  link-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.3px
    fontFeature: '"calt", "kern", "liga", "ss03"'
  button-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.6
    letterSpacing: 0.2px
    fontFeature: '"calt", "kern", "liga", "ss03"'

rounded:
  none: 0px
  xs: 4px
  sm: 6px
  md: 8px
  lg: 10px
  xl: 16px
  full: 9999px

spacing:
  xxs: 2px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  xxl: 32px
  section: 96px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 8px 16px
    height: 36px
  button-primary-pressed:
    backgroundColor: "{colors.primary-pressed}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 8px 16px
    height: 36px
  button-tertiary:
    backgroundColor: "{colors.surface-elevated}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 8px 16px
    height: 36px
  button-disabled:
    backgroundColor: "{colors.surface-elevated}"
    textColor: "{colors.ash}"
    rounded: "{rounded.md}"
  install-button:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 6px 14px
  text-input:
    backgroundColor: "{colors.surface-elevated}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 8px 12px
    height: 36px
  text-input-focused:
    backgroundColor: "{colors.surface-elevated}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.md}"
  store-search-bar:
    backgroundColor: "{colors.surface-elevated}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 10px 16px
    height: 44px
  command-palette-row:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 6px 10px
  command-palette-row-active:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
  pill-tab:
    backgroundColor: "transparent"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  pill-tab-active:
    backgroundColor: "{colors.surface-elevated}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
  badge-pro:
    backgroundColor: "{colors.surface-elevated}"
    textColor: "{colors.on-dark-mute}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-info-soft:
    backgroundColor: "{colors.accent-blue-soft}"
    textColor: "{colors.accent-blue}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  keycap:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{t

[truncated in unified pack view; see source file for full content]


---

# Hermes deep extension override

## STYLE.md excerpt

# Raycast Command Native

Status: runtime-ready extension inside the unified Hermes design pack.

## Style formula

command palette native utility; dark polished macOS surface; compact rows, icons, shortcuts, extensions and AI actions; speed and keyboard memory as the identity

This pack is meant for generation, review, and critique. It should give an agent enough local information to design a screen without opening Mobbin, GitHub, a browser, or any external gallery. The goal is style grammar and product-pattern transfer, not brand impersonation or exact screen cloning.

## When to use

Use this style when the requested artifact matches the product job, emotional temperature, and UI density of `raycast-command-native`. If the task names this brand/style directly, use this extension. If the task only names a category, route here when the component set below matches the requested surface better than the other packs.

## Visual and interaction principles

- Start from the user job and select the closest local component capsule before choosing colors or decorative treatment.
- Preserve hierarchy first: primary object, secondary metadata, tertiary controls, then ambient decoration.
- Use the token system rather than ad-hoc colors. Color anchors: `canvas`=#0b0b10; `surface`=#15151c; `panel`=#1d1d27; `text`=#f8fafc; `muted`=#a1a1aa; `border`=#2b2b36; `accent`=#ff6363; `accent2`=#8b5cf6.
- Use the typography roles deliberately. Type anchors: `ui`=Inter/system sans-serif; `mono`=ui-monospace/SFMono-Regular.
- Respect the shape and density system: spacing scale present, radius scale present.
- Prefer restrained adaptation over literal copying. Do not reuse logos, exact text, private data, or proprietary screen layout one-to-one.

## Runtime component set

- `ai-action-panel` — ai action panel
- `command-palette` — command palette
- `empty-state-command` — empty state command
- `extension-card-grid` — extension card grid
- `onboarding-install` — onboarding install
- `preferences-modal` — preferences modal
- `pricing-card` — pricing card
- `search-results-list` — search results list
- `shortcut-row` — shortcut row
- `team-admin-table` — team admin table

For each component, load the capsule in `components/capsules/<component-id>.md` first. Then use `components/extracted/` and `evidence/source-map/` only when you need provenance or visual facts. Use `pack/components/raycast-command-native/` for short semantic slices when a retrieval system asks for compact component context.

## Evidence coverage

- Mobbin screens: 20
- Mobbin sections: 20
- Mobbin flow previews: 20
- Public web pages captured: 2
- Authenticated screenshots: 1

These are build-time artifacts already stored locally. Runtime agents must not fetch more evidence unless explicitly asked to run a new extraction wave.

## Agent recipe

1. Read `pack/styles/raycast-command-native/DESIGN.md` for the unified baseline + extension view.
2. Load `pack/extensions/raycast-command-native/tokens/tokens.json` and `tokens/css-vars.css` for implementation values.
3. Pick 1-3 capsules from `pack/extensions/raycast-command-native/components/capsules/` that match the requested screen.
4. Compose with the local style formula and component grammar.
5. Run the result against `pack/extensions/raycast-command-native/eval/checklist.yaml` and `eval/failure-modes.md`.
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

Runtime component atlas for `raycast-command-native`.

Use this file to choose the right capsule before implementation. The capsule is the detailed recipe; this atlas is the router.

## `ai-action-panel` — Raycast Command Native — Ai Action Panel

Use when: the artifact needs `ai action panel` behavior, layout, or decision structure.
Capsule: `components/capsules/ai-action-panel.md`
Semantic slice: `pack/components/raycast-command-native/ai-action-panel.md`
Evidence links recorded: `2` index path groups; see local source map and extracted folders for detail.

Design job:
- Preserve this style formula: command palette native utility; dark polished macOS surface; compact rows, icons, shortcuts, extensions and AI actions; speed and keyboard memory as the identity
- Keep the component's primary object obvious before adding decoration.
- Use token roles and density from `tokens/tokens.json` instead of inventing ad-hoc values.
- Adapt the grammar to the new product context; do not clone exact evidence screens.

Implementation notes:
- Start with semantic structure and states.
- Add controls, status, metadata, and supporting copy in that order.
- Check responsive behavior and empty/error/loading states when relevant.

Evidence excerpt:
> # Ai Action Panel Use this capsule when the artifact needs `ai action panel` behavior in the Raycast Command Native style. ## Grammar - Style formula: command palette native utility; dark polished macOS surface; compact rows, icons, shortcuts, extensions and AI actions; speed and keyboard memory as the identity - Evidence refs: 6 local images. - Token anchors: canvas `#0b0b10`, surface `#15151c`, text `#f8fafc`, accent `#ff6363`. - Preserve information hierarchy and action semantics; adapt the p

## `command-palette` — Raycast Command Native — Command Palette

Use when: the artifact needs `command palette` behavior, layout, or decision structure.
Capsule: `components/capsules/command-palette.md`
Semantic slice: `pack/components/raycast-command-native/command-palette.md`
Evidence links recorded: `2` index path groups; see local source map and extracted folders for detail.

Design job:
- Preserve this style formula: command palette native utility; dark polished macOS surface; compact rows, icons, shortcuts, extensions and AI actions; speed and keyboard memory as the identity
- Keep the component's primary object obvious before adding decoration.
- Use token roles and density from `tokens/tokens.json` instead of inventing ad-hoc values.
- Adapt the grammar to the new product context; do not clone exact evidence screens.

Implementation notes:
- Start with semantic structure and states.
- Add controls, status, metadata, and supporting copy in that order.
- Check responsive behavior and empty/error/loading states when relevant.

Evidence excerpt:
> # Command Palette Use this capsule when the artifact needs `command palette` behavior in the Raycast Command Native style. ## Grammar - Style formula: command palette native utility; dark polished macOS surface; compact rows, icons, shortcuts, extensions and AI actions; speed and keyboard memory as the identity - Evidence refs: 6 local images. - Token anchors: canvas `#0b0b10`, surface `#15151c`, text `#f8fafc`, accent `#ff6363`. - Preserve information hierarchy and action semantics; adapt the p

## `empty-state-command` — Raycast Command Native — Empty State Command

Use when: the artifact needs `empty state command` behavior, layout, or decision structure.
Capsule: `components/capsules/empty-state-command.md`
Semantic slice: `pack/components/raycast-command-native/empty-state-command.md`
Evidence links recorded: `2` index path groups; see local source map and extracted folders for detail.

Design job:
- Preserve this style formula: command palette native utility; dark polished macOS surface; compact rows, icons, shortcuts, extensions and AI actions; speed and keyboard memory as the identity
- Keep the component's primary object obvious before adding decoration.
- Use token roles and density from `tokens/tokens.json` instead of inventing ad-hoc values.
- Adapt the grammar to the new product context; do not clone exact evidence screens.

Implementation notes:
- Start with semantic structure and states.
- Add controls, status, metadata, and supporting copy in that order.
- Check responsive behavior and empty/error/loading states when relevant.

Evidence excerpt:
> # Empty State Command Use this capsule when the artifact needs `empty state command` behavior in the Raycast Command Native style. ## Grammar - Style formula: command palette native utility; dark polished macOS surface; compact rows, icons, shortcuts, extensions and AI actions; speed and keyboard memory as the identity - Evidence refs: 6 local images. - Token anchors: canvas `#0b0b10`, surface `#15151c`, text `#f8fafc`, accent `#ff6363`. - Preserve information hierarchy and action semantics; ada

## `extension-card-grid` — Raycast Command Native — Extension Card G

[truncated in unified pack view; see source file for full content]


## Agent contract excerpt

# Agent contract — Raycast Command Native

This contract tells an agent how to use `raycast-command-native` inside the unified Hermes design pack.

## Required load order

1. `pack/styles/raycast-command-native/DESIGN.md` — unified style entry and broad baseline context.
2. `pack/extensions/raycast-command-native/STYLE.md` — concise runtime formula and operating rules.
3. `pack/extensions/raycast-command-native/tokens/tokens.json` plus `tokens/css-vars.css` — implementation anchors.
4. `pack/extensions/raycast-command-native/components/component-atlas.md` — choose the closest reusable surface.
5. `pack/extensions/raycast-command-native/components/capsules/<component-id>.md` — detailed component grammar.
6. `pack/components/raycast-command-native/<component-id>.md` — compact semantic retrieval slice.
7. `pack/extensions/raycast-command-native/eval/checklist.yaml`, `eval/rubric.md`, and `eval/failure-modes.md` — quality gate.

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
