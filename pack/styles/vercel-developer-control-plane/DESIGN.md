# Unified DESIGN.md — Vercel Developer Control Plane

This file is the single-pack runtime view for `vercel-developer-control-plane`.

Authority inside this file:

1. VoltAgent DESIGN.md baseline gives broad visual grammar.
2. Hermes deep extension overrides baseline with local evidence, tokens, components, eval, and implementation guardrails.
3. Use local paths only; do not call GitHub/Mobbin/web/browser at runtime.

Local extension root: `pack/extensions/vercel-developer-control-plane`
Component semantic slices: `pack/components/vercel-developer-control-plane`

---

## Baseline: `vercel`

Source: `pack/design-md/vercel/DESIGN.md`

---
version: alpha
name: Vercel-Inspired-design-analysis
description: An inspired interpretation of Vercel's design language — a developer-platform brand whose surface is a stark black-and-ink duet on near-white canvas, broken at hero scale by a multi-color mesh gradient (cyan / blue / magenta / amber) that acts as the entire decorative system, paired with a custom geometric sans for headlines and a monospaced caption face for technical labels.

colors:
  primary: "#171717"
  on-primary: "#ffffff"
  ink: "#171717"
  body: "#4d4d4d"
  mute: "#888888"
  hairline: "#ebebeb"
  hairline-strong: "#a1a1a1"
  canvas: "#ffffff"
  canvas-soft: "#fafafa"
  canvas-soft-2: "#f5f5f5"
  link: "#0070f3"
  link-deep: "#0761d1"
  link-bg-soft: "#d3e5ff"
  success: "#0070f3"
  error: "#ee0000"
  error-soft: "#f7d4d6"
  error-deep: "#c50000"
  warning: "#f5a623"
  warning-soft: "#ffefcf"
  warning-deep: "#ab570a"
  violet: "#7928ca"
  violet-soft: "#d8ccf1"
  violet-deep: "#4c2889"
  cyan: "#50e3c2"
  cyan-soft: "#aaffec"
  cyan-deep: "#29bc9b"
  highlight-pink: "#ff0080"
  highlight-magenta: "#eb367f"
  gradient-develop-start: "#007cf0"
  gradient-develop-end: "#00dfd8"
  gradient-preview-start: "#7928ca"
  gradient-preview-end: "#ff0080"
  gradient-ship-start: "#ff4d4d"
  gradient-ship-end: "#f9cb28"
  selection-bg: "#171717"
  selection-fg: "#f2f2f2"

typography:
  display-xl:
    fontFamily: Geist, Inter, system-ui, -apple-system, sans-serif
    fontSize: 48px
    fontWeight: 600
    lineHeight: 48px
    letterSpacing: -2.4px
  display-lg:
    fontFamily: Geist, Inter, system-ui, -apple-system, sans-serif
    fontSize: 32px
    fontWeight: 600
    lineHeight: 40px
    letterSpacing: -1.28px
  display-md:
    fontFamily: Geist, Inter, system-ui, -apple-system, sans-serif
    fontSize: 24px
    fontWeight: 600
    lineHeight: 32px
    letterSpacing: -0.96px
  display-sm:
    fontFamily: Geist, Inter, system-ui, -apple-system, sans-serif
    fontSize: 20px
    fontWeight: 600
    lineHeight: 28px
    letterSpacing: -0.6px
  body-lg:
    fontFamily: Geist, Inter, system-ui, -apple-system, sans-serif
    fontSize: 18px
    fontWeight: 400
    lineHeight: 28px
    letterSpacing: 0px
  body-md:
    fontFamily: Geist, Inter, system-ui, -apple-system, sans-serif
    fontSize: 16px
    fontWeight: 400
    lineHeight: 24px
  body-md-strong:
    fontFamily: Geist, Inter, system-ui, -apple-system, sans-serif
    fontSize: 16px
    fontWeight: 500
    lineHeight: 24px
  body-sm:
    fontFamily: Geist, Inter, system-ui, -apple-system, sans-serif
    fontSize: 14px
    fontWeight: 400
    lineHeight: 20px
    letterSpacing: -0.28px
  body-sm-strong:
    fontFamily: Geist, Inter, system-ui, -apple-system, sans-serif
    fontSize: 14px
    fontWeight: 500
    lineHeight: 20px
    letterSpacing: -0.28px
  caption:
    fontFamily: Geist, Inter, system-ui, -apple-system, sans-serif
    fontSize: 12px
    fontWeight: 400
    lineHeight: 16px
  caption-mono:
    fontFamily: Geist Mono, ui-monospace, SFMono-Regular, Menlo, Monaco, monospace
    fontSize: 12px
    fontWeight: 400
    lineHeight: 16px
  code:
    fontFamily: Geist Mono, ui-monospace, SFMono-Regular, Menlo, Monaco, monospace
    fontSize: 13px
    fontWeight: 400
    lineHeight: 20px
  button-md:
    fontFamily: Geist, Inter, system-ui, -apple-system, sans-serif
    fontSize: 14px
    fontWeight: 500
    lineHeight: 20px
  button-lg:
    fontFamily: Geist, Inter, system-ui, -apple-system, sans-serif
    fontSize: 16px
    fontWeight: 500
    lineHeight: 24px

rounded:
  none: 0px
  xs: 4px
  sm: 6px
  md: 8px
  lg: 12px
  xl: 16px
  pill-sm: 64px
  pill: 100px
  full: 9999px

spacing:
  xxs: 4px
  xs: 8px
  sm: 12px
  md: 16px
  lg: 24px
  xl: 32px
  2xl: 40px
  3xl: 48px
  4xl: 64px
  5xl: 96px
  6xl: 128px
  section: 192px

components:
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    height: 64px
    padding: "{spacing.sm} {spacing.lg}"
  nav-link:
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.sm}"
  nav-cta-signup:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm-strong}"
    rounded: "{rounded.sm}"
    padding: "0px {spacing.xs}"
    height: 28px
  nav-cta-login:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm-strong}"
    rounded: "{rounded.sm}"
    padding: "0px {spacing.xs}"
    height: 28px
  nav-cta-ask-ai:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm-strong}"
    rounded: "{rounded.sm}"
    padding: "0px {spacing.xs}"
    height: 28px
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.pill}"
    padding: "0px {spacing.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.pill}"
    padding: "0px {spacing.sm}"
  button-primary-sm:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.pill}"
    padding: "0px {spacing.xs}"
  button-secondary-sm:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.pill}"
    padding: "0px {spacing.xs}"
  tab-ghost:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.pill-sm}"
    padding: "0px {spacing.md}"
  icon-button-circular:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.full}"
  card-marketing:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  card-marketing-large:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"
  card-soft:
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  template-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.md}"
  code-editor-mockup:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.code}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  form-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "0px {spacing.sm}"
    height: 40px
  form-input-sm:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "0px {spacing.sm}"
    height: 32px
  form-input-lg:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "0px {spacing.sm}"
    height: 48px
  badge-secondary:
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "0px {spacing.xs}"
  pricing-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"
  pricing-card-fea

[truncated in unified pack view; see source file for full content]


---

# Hermes deep extension override

## STYLE.md excerpt

# Vercel Developer Control Plane

Status: runtime-ready extension inside the unified Hermes design pack.

## Style formula

black/white developer command surface; sharp grids; deployment status as primary object; mono technical detail; premium gradients used sparingly behind product proof

This pack is meant for generation, review, and critique. It should give an agent enough local information to design a screen without opening Mobbin, GitHub, a browser, or any external gallery. The goal is style grammar and product-pattern transfer, not brand impersonation or exact screen cloning.

## When to use

Use this style when the requested artifact matches the product job, emotional temperature, and UI density of `vercel-developer-control-plane`. If the task names this brand/style directly, use this extension. If the task only names a category, route here when the component set below matches the requested surface better than the other packs.

## Visual and interaction principles

- Start from the user job and select the closest local component capsule before choosing colors or decorative treatment.
- Preserve hierarchy first: primary object, secondary metadata, tertiary controls, then ambient decoration.
- Use the token system rather than ad-hoc colors. Color anchors: `canvas`=#000000; `surface`=#0a0a0a; `panel`=#111111; `text`=#fafafa; `muted`=#a1a1aa; `border`=#27272a; `accent`=#ffffff; `accent2`=#0070f3.
- Use the typography roles deliberately. Type anchors: `ui`=Inter/system sans-serif; `mono`=ui-monospace/SFMono-Regular.
- Respect the shape and density system: spacing scale present, radius scale present.
- Prefer restrained adaptation over literal copying. Do not reuse logos, exact text, private data, or proprietary screen layout one-to-one.

## Runtime component set

- `analytics-chart` — analytics chart
- `deployment-list` — deployment list
- `docs-code-block` — docs code block
- `domain-settings` — domain settings
- `environment-variable-table` — environment variable table
- `import-project-flow` — import project flow
- `logs-console` — logs console
- `pricing-plan-grid` — pricing plan grid
- `project-card` — project card
- `template-gallery` — template gallery

For each component, load the capsule in `components/capsules/<component-id>.md` first. Then use `components/extracted/` and `evidence/source-map/` only when you need provenance or visual facts. Use `pack/components/vercel-developer-control-plane/` for short semantic slices when a retrieval system asks for compact component context.

## Evidence coverage

- Mobbin screens: 20
- Mobbin sections: 20
- Mobbin flow previews: 20
- Public web pages captured: 3
- Authenticated screenshots: 1

These are build-time artifacts already stored locally. Runtime agents must not fetch more evidence unless explicitly asked to run a new extraction wave.

## Agent recipe

1. Read `pack/styles/vercel-developer-control-plane/DESIGN.md` for the unified baseline + extension view.
2. Load `pack/extensions/vercel-developer-control-plane/tokens/tokens.json` and `tokens/css-vars.css` for implementation values.
3. Pick 1-3 capsules from `pack/extensions/vercel-developer-control-plane/components/capsules/` that match the requested screen.
4. Compose with the local style formula and component grammar.
5. Run the result against `pack/extensions/vercel-developer-control-plane/eval/checklist.yaml` and `eval/failure-modes.md`.
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

Runtime component atlas for `vercel-developer-control-plane`.

Use this file to choose the right capsule before implementation. The capsule is the detailed recipe; this atlas is the router.

## `analytics-chart` — Vercel Developer Control Plane — Analytics Chart

Use when: the artifact needs `analytics chart` behavior, layout, or decision structure.
Capsule: `components/capsules/analytics-chart.md`
Semantic slice: `pack/components/vercel-developer-control-plane/analytics-chart.md`
Evidence links recorded: `2` index path groups; see local source map and extracted folders for detail.

Design job:
- Preserve this style formula: black/white developer command surface; sharp grids; deployment status as primary object; mono technical detail; premium gradients used sparingly behind product proof
- Keep the component's primary object obvious before adding decoration.
- Use token roles and density from `tokens/tokens.json` instead of inventing ad-hoc values.
- Adapt the grammar to the new product context; do not clone exact evidence screens.

Implementation notes:
- Start with semantic structure and states.
- Add controls, status, metadata, and supporting copy in that order.
- Check responsive behavior and empty/error/loading states when relevant.

Evidence excerpt:
> # Analytics Chart Use this capsule when the artifact needs `analytics chart` behavior in the Vercel Developer Control Plane style. ## Grammar - Style formula: black/white developer command surface; sharp grids; deployment status as primary object; mono technical detail; premium gradients used sparingly behind product proof - Evidence refs: 6 local images. - Token anchors: canvas `#000000`, surface `#0a0a0a`, text `#fafafa`, accent `#ffffff`. - Preserve information hierarchy and action semantics;

## `deployment-list` — Vercel Developer Control Plane — Deployment List

Use when: the artifact needs `deployment list` behavior, layout, or decision structure.
Capsule: `components/capsules/deployment-list.md`
Semantic slice: `pack/components/vercel-developer-control-plane/deployment-list.md`
Evidence links recorded: `2` index path groups; see local source map and extracted folders for detail.

Design job:
- Preserve this style formula: black/white developer command surface; sharp grids; deployment status as primary object; mono technical detail; premium gradients used sparingly behind product proof
- Keep the component's primary object obvious before adding decoration.
- Use token roles and density from `tokens/tokens.json` instead of inventing ad-hoc values.
- Adapt the grammar to the new product context; do not clone exact evidence screens.

Implementation notes:
- Start with semantic structure and states.
- Add controls, status, metadata, and supporting copy in that order.
- Check responsive behavior and empty/error/loading states when relevant.

Evidence excerpt:
> # Deployment List Use this capsule when the artifact needs `deployment list` behavior in the Vercel Developer Control Plane style. ## Grammar - Style formula: black/white developer command surface; sharp grids; deployment status as primary object; mono technical detail; premium gradients used sparingly behind product proof - Evidence refs: 6 local images. - Token anchors: canvas `#000000`, surface `#0a0a0a`, text `#fafafa`, accent `#ffffff`. - Preserve information hierarchy and action semantics;

## `docs-code-block` — Vercel Developer Control Plane — Docs Code Block

Use when: the artifact needs `docs code block` behavior, layout, or decision structure.
Capsule: `components/capsules/docs-code-block.md`
Semantic slice: `pack/components/vercel-developer-control-plane/docs-code-block.md`
Evidence links recorded: `2` index path groups; see local source map and extracted folders for detail.

Design job:
- Preserve this style formula: black/white developer command surface; sharp grids; deployment status as primary object; mono technical detail; premium gradients used sparingly behind product proof
- Keep the component's primary object obvious before adding decoration.
- Use token roles and density from `tokens/tokens.json` instead of inventing ad-hoc values.
- Adapt the grammar to the new product context; do not clone exact evidence screens.

Implementation notes:
- Start with semantic structure and states.
- Add controls, status, metadata, and supporting copy in that order.
- Check responsive behavior and empty/error/loading states when relevant.

Evidence excerpt:
> # Docs Code Block Use this capsule when the artifact needs `docs code block` behavior in the Vercel Developer Control Plane style. ## Grammar - Style formula: black/white developer command surface; sharp grids; deployment status as primary object; mono technical detail; premium gradients used sparingly behind product proof - Evidence refs: 6 local images. - Token anchors: canvas `#000000`, surface `#0a0a0a`, text `#fafafa`, accent `#ffffff`. - Preserve information hierarchy and action semantics;

## `domain-settings`

[truncated in unified pack view; see source file for full content]


## Agent contract excerpt

# Agent contract — Vercel Developer Control Plane

This contract tells an agent how to use `vercel-developer-control-plane` inside the unified Hermes design pack.

## Required load order

1. `pack/styles/vercel-developer-control-plane/DESIGN.md` — unified style entry and broad baseline context.
2. `pack/extensions/vercel-developer-control-plane/STYLE.md` — concise runtime formula and operating rules.
3. `pack/extensions/vercel-developer-control-plane/tokens/tokens.json` plus `tokens/css-vars.css` — implementation anchors.
4. `pack/extensions/vercel-developer-control-plane/components/component-atlas.md` — choose the closest reusable surface.
5. `pack/extensions/vercel-developer-control-plane/components/capsules/<component-id>.md` — detailed component grammar.
6. `pack/components/vercel-developer-control-plane/<component-id>.md` — compact semantic retrieval slice.
7. `pack/extensions/vercel-developer-control-plane/eval/checklist.yaml`, `eval/rubric.md`, and `eval/failure-modes.md` — quality gate.

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
