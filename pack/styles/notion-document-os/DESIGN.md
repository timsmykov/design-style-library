# Unified DESIGN.md — Notion Document OS

This file is the single-pack runtime view for `notion-document-os`.

Authority inside this file:

1. VoltAgent DESIGN.md baseline gives broad visual grammar.
2. Hermes deep extension overrides baseline with local evidence, tokens, components, eval, and implementation guardrails.
3. Use local paths only; do not call GitHub/Mobbin/web/browser at runtime.

Local extension root: `pack/extensions/notion-document-os`
Component semantic slices: `pack/components/notion-document-os`

---

## Baseline: `notion`

Source: `pack/design-md/notion/DESIGN.md`

---
version: alpha
name: Notion-design-analysis
description: Notion presents itself as the all-in-one workspace through a confident, illustration-rich brand voice — anchored by a deep navy hero band ({colors.brand-navy}) decorated with brand-colored sticky-note dots and mesh wire illustrations, a signature purple pill primary CTA ({colors.primary}), and a rich palette of pastel-tinted feature cards that echo the colorful database properties of the live product. The system uses a Notion-Sans (Inter-based) typeface across every UI surface, anchors a 4-tier pricing comparison (Free / Plus / Business / Enterprise), and presents the live workspace UI mockup directly inside the hero band. Coverage spans homepage, Enterprise, Product AI, Product Agents, Startups, and Pricing surfaces.

colors:
  primary: "#5645d4"
  primary-pressed: "#4534b3"
  primary-deep: "#3a2a99"
  on-primary: "#ffffff"
  brand-navy: "#0a1530"
  brand-navy-deep: "#070f24"
  brand-navy-mid: "#1a2a52"
  link-blue: "#0075de"
  link-blue-pressed: "#005bab"
  brand-orange: "#dd5b00"
  brand-orange-deep: "#793400"
  brand-pink: "#ff64c8"
  brand-pink-deep: "#a02e6d"
  brand-purple: "#7b3ff2"
  brand-purple-300: "#d6b6f6"
  brand-purple-800: "#391c57"
  brand-teal: "#2a9d99"
  brand-green: "#1aae39"
  brand-yellow: "#f5d75e"
  brand-brown: "#523410"
  card-tint-peach: "#ffe8d4"
  card-tint-rose: "#fde0ec"
  card-tint-mint: "#d9f3e1"
  card-tint-lavender: "#e6e0f5"
  card-tint-sky: "#dcecfa"
  card-tint-yellow: "#fef7d6"
  card-tint-yellow-bold: "#f9e79f"
  card-tint-cream: "#f8f5e8"
  card-tint-gray: "#f0eeec"
  canvas: "#ffffff"
  surface: "#f6f5f4"
  surface-soft: "#fafaf9"
  hairline: "#e5e3df"
  hairline-soft: "#ede9e4"
  hairline-strong: "#c8c4be"
  ink-deep: "#000000"
  ink: "#1a1a1a"
  charcoal: "#37352f"
  slate: "#5d5b54"
  steel: "#787671"
  stone: "#a4a097"
  muted: "#bbb8b1"
  on-dark: "#ffffff"
  on-dark-muted: "#a4a097"
  semantic-success: "#1aae39"
  semantic-warning: "#dd5b00"
  semantic-error: "#e03131"

typography:
  hero-display:
    fontFamily: Notion Sans
    fontSize: 80px
    fontWeight: 600
    lineHeight: 1.05
    letterSpacing: -2px
  display-lg:
    fontFamily: Notion Sans
    fontSize: 56px
    fontWeight: 600
    lineHeight: 1.10
    letterSpacing: -1px
  heading-1:
    fontFamily: Notion Sans
    fontSize: 48px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  heading-2:
    fontFamily: Notion Sans
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.20
    letterSpacing: -0.5px
  heading-3:
    fontFamily: Notion Sans
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
  heading-4:
    fontFamily: Notion Sans
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.30
  heading-5:
    fontFamily: Notion Sans
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.40
  subtitle:
    fontFamily: Notion Sans
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.50
  body-md:
    fontFamily: Notion Sans
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.55
  body-md-medium:
    fontFamily: Notion Sans
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.55
  body-sm:
    fontFamily: Notion Sans
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.50
  body-sm-medium:
    fontFamily: Notion Sans
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.50
  caption:
    fontFamily: Notion Sans
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.40
  caption-bold:
    fontFamily: Notion Sans
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.40
  micro:
    fontFamily: Notion Sans
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.40
  micro-uppercase:
    fontFamily: Notion Sans
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.40
    letterSpacing: 1px
  button-md:
    fontFamily: Notion Sans
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.30

rounded:
  xs: 4px
  sm: 6px
  md: 8px
  lg: 12px
  xl: 16px
  xxl: 20px
  xxxl: 24px
  full: 9999px

spacing:
  xxs: 4px
  xs: 8px
  sm: 12px
  md: 16px
  lg: 20px
  xl: 24px
  xxl: 32px
  xxxl: 40px
  section-sm: 48px
  section: 64px
  section-lg: 96px
  hero: 120px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: "10px 18px"
  button-primary-pressed:
    backgroundColor: "{colors.primary-pressed}"
    textColor: "{colors.on-primary}"
  button-primary-disabled:
    backgroundColor: "{colors.hairline}"
    textColor: "{colors.muted}"
  button-dark:
    backgroundColor: "{colors.ink-deep}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: "10px 18px"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: "10px 18px"
    border: "1px solid {colors.hairline-strong}"
  button-on-dark:
    backgroundColor: "{colors.on-dark}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: "10px 18px"
  button-secondary-on-dark:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: "10px 18px"
    border: "1px solid {colors.on-dark-muted}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
  button-link:
    backgroundColor: "transparent"
    textColor: "{colors.link-blue}"
    typography: "{typography.body-sm-medium}"
    padding: "0"
  card-base:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"
    border: "1px solid {colors.hairline}"
  card-feature:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xxl}"
    border: "1px solid {colors.hairline}"
  card-feature-yellow-bold:
    backgroundColor: "{colors.card-tint-yellow-bold}"
    textColor: "{colors.charcoal}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xxl}"
  card-feature-peach:
    backgroundColor: "{colors.card-tint-peach}"
    textColor: "{colors.charcoal}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xxl}"
  card-feature-rose:
    backgroundColor: "{colors.card-tint-rose}"
    textColor: "{colors.charcoal}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xxl}"
  card-feature-mint:
    backgroundColor: "{colors.card-tint-mint}"
    textColor: "{colors.charcoal}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xxl}"
  card-feature-sky:
    backgroundColor: "{colors.card-tint-sky}"
    textColor: "{colors.charcoal}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xxl}"
  card-feature-lavender:
    backgroundColor: "{colors.card-tint-lavender}"
    textColor: "{colors.charcoal}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xxl}"
  card-feature-yellow:
    backgroundColor: "{colors.card-tint-yellow}"
    textColor: "{colors.charcoal}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xxl}"
  card-feature-cream:
    backgroundColor: "{colors.card-tint-cream}"
    textColor: "{colors.charcoal}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xxl}"
  card-agent-tile:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"
    border: "1px solid {colors.hairline}"
  card-template:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.hairline}"
  card-startup-perk:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"
    border: "1px solid {colors.hairline}"
  pricing-card:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xxl}"
    border: "1px solid {colors.hairline}"
  pricing-card-featured:
    backgroundColor: "{co

[truncated in unified pack view; see source file for full content]


---

# Hermes deep extension override

## STYLE.md excerpt

# Notion Document OS

Status: **draft v0.1** — local Mobbin source map and screenshot-derived facts cover the no-login corpus; public Notion homepage/pricing DOM/CDP evidence is captured where accessible; authenticated app internals and fresh-agent eval remain pending.

## Canonical one-liner

**Quiet document/workspace operating system:** a paper-white block canvas wrapped in muted workspace chrome, where pages, databases, templates, and AI assistance feel like editable documents before they feel like software screens.

## Use when

- The product is a document editor, wiki, project OS, lightweight database, or team knowledge surface.
- Users should feel they are arranging information blocks, not operating a heavy dashboard.
- Templates, starter pages, database views, and low-friction collaboration are central.
- AI should appear as a writing/organization assistant inside the document system.

## Avoid when

- You need saturated brand color, game-like energy, or glossy conversion theatre.
- The interface is a high-density analytics/admin tool with many equal-priority metrics.
- The product depends on strong visual illustration more than direct editable content.

## Visual DNA

### Surface

- Default canvas is white or near-white, with subtle gray workspace surfaces.
- Borders are hairline and structural; shadows are rare and soft.
- Color is semantic and small: status tags, selected states, icons, plan accents.

### Layout

- App shell: left workspace rail, large central page/database canvas, optional modal/panel overlays.
- Documents use generous left alignment, compact top metadata, and progressively revealed controls.
- Database views preserve page calm: table/board/calendar chrome is quiet, not spreadsheet-heavy.
- Marketing pages translate document modularity into stacked cards, product proof blocks, and calm CTAs.

### Typography

- System-like sans, strong readable body rhythm, and dense-but-calm labels.
- Hierarchy comes from spacing, weight, indentation, and block structure more than color.
- Titles feel like document headings; labels feel utilitarian and compact.

### Interaction

- Creation starts from blocks/templates; editing controls stay close to the content they affect.
- Hover/proximity reveals add handles, drag handles, block menus, and property controls.
- Workspace actions are small, predictable, and reversible.

## Primary reusable patterns

1. **Block document canvas:** title, metadata, content blocks, inline add/drag/menu controls.
2. **Workspace sidebar:** compact teamspace/page tree with muted selected states.
3. **Database view:** document-like table/board/list/calendar with property chips and view tabs.
4. **Template gallery:** use-case cards that create a page/workspace rather than sell a feature.
5. **Slash command / block insert:** focused inline command menu with grouped block types.
6. **No-login marketing proof:** product screenshot/card rhythm plus plain copy and black/neutral CTAs.


## Component atlas excerpt

# Component Atlas — Notion Document OS

Status: draft v0.1, distilled from 96 local Mobbin references plus public no-login DOM/CDP evidence.

Agents should use this atlas for component selection, then open the matching capsule for implementation details.

## Document page editor / block canvas

Component id: `document-page-editor`

### Rules

- Evidence refs: 15 local Mobbin rows.
- Keep surfaces white/gray and controls compact.
- Preserve document-first hierarchy and editable structure.
- Avoid saturated dashboard treatments or decorative clone details.

## Workspace app shell / sidebar

Component id: `app-shell-sidebar`

### Rules

- Evidence refs: 11 local Mobbin rows.
- Keep surfaces white/gray and controls compact.
- Preserve document-first hierarchy and editable structure.
- Avoid saturated dashboard treatments or decorative clone details.

## Database view: table, board, list, calendar

Component id: `database-view-table-board`

### Rules

- Evidence refs: 5 local Mobbin rows.
- Keep surfaces white/gray and controls compact.
- Preserve document-first hierarchy and editable structure.
- Avoid saturated dashboard treatments or decorative clone details.

## Template gallery / starter library

Component id: `template-gallery`

### Rules

- Evidence refs: 3 local Mobbin rows.
- Keep surfaces white/gray and controls compact.
- Preserve document-first hierarchy and editable structure.
- Avoid saturated dashboard treatments or decorative clone details.

## Block insert command and inline controls

Component id: `command-block-insert`

### Rules

- Evidence refs: 6 local Mobbin rows.
- Keep surfaces white/gray and controls compact.
- Preserve document-first hierarchy and editable structure.
- Avoid saturated dashboard treatments or decorative clone details.

## Notion AI assistant / rewrite panel

Component id: `ai-assistant-panel`

### Rules

- Evidence refs: 5 local Mobbin rows.
- Keep surfaces white/gray and controls compact.
- Preserve document-first hierarchy and editable structure.
- Avoid saturated dashboard treatments or decorative clone details.

## Onboarding / workspace creation

Component id: `onboarding-workspace`

### Rules

- Evidence refs: 27 local Mobbin rows.
- Keep surfaces white/gray and controls compact.
- Preserve document-first hierarchy and editable structure.
- Avoid saturated dashboard treatments or decorative clone details.

## Pricing / plan comparison

Component id: `pricing-plan-cards`

### Rules

- Evidence refs: 6 local Mobbin rows.
- Keep surfaces white/gray and controls compact.
- Preserve document-first hierarchy and editable structure.
- Avoid saturated dashboard treatments or decorative clone details.

## Marketing hero / product narrative

Component id: `marketing-hero-section`

### Rules

- Evidence refs: 8 local Mobbin rows.
- Keep surfaces white/gray and controls compact.
- Preserve document-first hierarchy and editable structure.
- Avoid saturated dashboard treatments or decorative clone details.

## Docs/wiki/projects feature grid

Component id: `docs-projects-grid`

### Rules

- Evidence refs: 10 local Mobbin rows.
- Keep surfaces white/gray and controls compact.
- Preserve document-first hierarchy and editable structure.
- Avoid saturated dashboard treatments or decorative clone details.


## Agent contract excerpt

# Agent contract — Notion Document OS

This contract tells an agent how to use `notion-document-os` inside the unified Hermes design pack.

## Required load order

1. `pack/styles/notion-document-os/DESIGN.md` — unified style entry and broad baseline context.
2. `pack/extensions/notion-document-os/STYLE.md` — concise runtime formula and operating rules.
3. `pack/extensions/notion-document-os/tokens/tokens.json` plus `tokens/css-vars.css` — implementation anchors.
4. `pack/extensions/notion-document-os/components/component-atlas.md` — choose the closest reusable surface.
5. `pack/extensions/notion-document-os/components/capsules/<component-id>.md` — detailed component grammar.
6. `pack/components/notion-document-os/<component-id>.md` — compact semantic retrieval slice.
7. `pack/extensions/notion-document-os/eval/checklist.yaml`, `eval/rubric.md`, and `eval/failure-modes.md` — quality gate.

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

