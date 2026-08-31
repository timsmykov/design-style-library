# Unified DESIGN.md — Anthropic / Claude Editorial Workbench

This file is the single-pack runtime view for `anthropic-claude`.

Authority inside this file:

1. VoltAgent DESIGN.md baseline gives broad visual grammar.
2. Hermes deep extension overrides baseline with local evidence, tokens, components, eval, and implementation guardrails.
3. Use local paths only; do not call GitHub/Mobbin/web/browser at runtime.

Local extension root: `pack/extensions/anthropic-claude`
Component semantic slices: `pack/components/anthropic-claude`

---

## Baseline: `claude`

Source: `pack/design-md/claude/DESIGN.md`

---
version: alpha
name: Claude-design-analysis
description: A warm-canvas editorial interface for Anthropic's Claude product. The system anchors on a tinted cream canvas with serif display headlines, warm coral CTAs, and dark navy product surfaces (code editor mockups, model showcase cards). Brand voltage comes from the cream/coral pairing — deliberately warm and humanist where most AI brands use cool blue + slate. Type voice runs a slab-serif display ("Copernicus" / Tiempos Headline) for h1/h2 and a humanist sans for body. The signature Anthropic black-radial-spike mark anchors the wordmark.

colors:
  primary: "#cc785c"
  primary-active: "#a9583e"
  primary-disabled: "#e6dfd8"
  ink: "#141413"
  body: "#3d3d3a"
  body-strong: "#252523"
  muted: "#6c6a64"
  muted-soft: "#8e8b82"
  hairline: "#e6dfd8"
  hairline-soft: "#ebe6df"
  canvas: "#faf9f5"
  surface-soft: "#f5f0e8"
  surface-card: "#efe9de"
  surface-cream-strong: "#e8e0d2"
  surface-dark: "#181715"
  surface-dark-elevated: "#252320"
  surface-dark-soft: "#1f1e1b"
  on-primary: "#ffffff"
  on-dark: "#faf9f5"
  on-dark-soft: "#a09d96"
  accent-teal: "#5db8a6"
  accent-amber: "#e8a55a"
  success: "#5db872"
  warning: "#d4a017"
  error: "#c64545"

typography:
  display-xl:
    fontFamily: "Copernicus, Tiempos Headline, serif"
    fontSize: 64px
    fontWeight: 400
    lineHeight: 1.05
    letterSpacing: -1.5px
  display-lg:
    fontFamily: "Copernicus, Tiempos Headline, serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -1px
  display-md:
    fontFamily: "Copernicus, Tiempos Headline, serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-sm:
    fontFamily: "Copernicus, Tiempos Headline, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.3px
  title-lg:
    fontFamily: "StyreneB, Inter, sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "StyreneB, Inter, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "StyreneB, Inter, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "StyreneB, Inter, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  body-sm:
    fontFamily: "StyreneB, Inter, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "StyreneB, Inter, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  caption-uppercase:
    fontFamily: "StyreneB, Inter, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 1.5px
  code:
    fontFamily: "JetBrains Mono, ui-monospace, monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  button:
    fontFamily: "StyreneB, Inter, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0
  nav-link:
    fontFamily: "StyreneB, Inter, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0

rounded:
  xs: 4px
  sm: 6px
  md: 8px
  lg: 12px
  xl: 16px
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
    padding: 12px 20px
    height: 40px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.md}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 12px 20px
    height: 40px
  button-secondary-on-dark:
    backgroundColor: "{colors.surface-dark-elevated}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 12px 20px
  button-text-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button}"
  button-icon-circular:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    size: 36px
  text-link:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.body-md}"
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  hero-band:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: 96px
  hero-illustration-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xl}"
  feature-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.lg}"
    padding: 32px
  product-mockup-card-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.title-md}"
    rounded: "{rounded.lg}"
    padding: 32px
  code-window-card:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.code}"
    rounded: "{rounded.lg}"
    padding: 24px
  model-comparison-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.lg}"
    padding: 32px
  pricing-tier-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-lg}"
    rounded: "{rounded.lg}"
    padding: 32px
  pricing-tier-card-featured:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.title-lg}"
    rounded: "{rounded.lg}"
    padding: 32px
  callout-card-coral:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.title-md}"
    rounded: "{rounded.lg}"
    padding: 32px
  connector-tile:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.lg}"
    padding: 20px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 10px 14px
    height: 40px
  text-input-focused:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
  cookie-consent-card:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    padding: 24px
  category-tab:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    padding: 8px 14px
    rounded: "{rounded.md}"
  category-tab-active:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.md}"
  badge-pill:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.pill}"
    padding: 4px 12px
  badge-coral:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-uppercase}"
    rounded: "{rounded.pill}"
    padding: 4px 12px
  cta-band-coral:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-sm}"
    rounded: "{rounded.lg}"
    padding: 64px
  cta-band-dark:
    backgroundColor: "{colors

[truncated in unified pack view; see source file for full content]


---

# Hermes deep extension override

## STYLE.md excerpt

# Anthropic / Claude Editorial Workbench

Status: **draft v0.5** — local Mobbin source map + screenshot-derived facts cover 211 refs; public DOM/CSS and Browser/CDP computed evidence captured for accessible Claude/Anthropic surfaces; authenticated app-only CDP and fresh-agent offline eval still pending.

## Canonical one-liner

**Warm paper editorialism plus disciplined AI workbench:** calm document-like hierarchy, compact command surfaces, sparse artifact panels, low-contrast trust, black/ivory utility, and restrained clay/terracotta accents.

## Use when

- The product needs calm, high-trust AI interaction.
- The output should feel like a thoughtful document/workbench, not a chat toy.
- Scientific notes, explainers, artifact panels, code/file previews, and source-grounded reasoning matter.
- A product page needs premium editorial warmth without glossy SaaS noise.

## Avoid when

- The goal is playful consumer energy.
- The interface needs aggressive conversion pressure.
- The product is a dense operational dashboard with many equal-priority controls.
- The brand requires neon, cyber, gaming, glassmorphism, or glossy 3D AI aesthetics.

## Visual DNA

### Surface

- Warm ivory / off-white canvas, not sterile white.
- White or near-white cards/forms/modals on warm canvas.
- Dark charcoal/black for primary text and primary utility actions.
- Clay/terracotta appears as the identity/action accent, not a full theme wash.

### Layout

- Brand/marketing: editorial page rhythm with large whitespace, strong typographic hierarchy, and concise sections.
- Product cards: large rounded macro-cards with one message, one CTA, one proof/demo visual.
- App/workbench: quiet split-pane shell, compact sidebar, large calm canvas, and a focused composer or artifact area.
- Modals: centered warm rounded cards over dimmed shell, preview/demo first, short explanation, one primary CTA.

### Typography

- Serif or serif-like display type for brand/editorial moments.
- Compact humanist/system sans for UI labels, navigation, buttons, composer controls, chips.
- Monospace only for code/data panels.
- Hierarchy comes from type scale and whitespace more than color.

### Interaction

- One dominant action per decision zone.
- Context controls are embedded quietly: model, repo, branch, environment, file/source chips.
- Trust appears through transparency, familiar auth, privacy/status links, caveats, and recovery paths.
- Avoid pressure, urgency, noisy badges, or redundant CTAs.

## Primary reusable patterns

1. **Editorial hero:** serif headline + concise body + black primary CTA + earthy human/symbolic visual.
2. **Two-column product card:** left copy/CTA + right product proof; light card for user value, dark card for developer/API/code.
3. **AI workbench shell:** compact sidebar + spacious work area + bottom-centered command composer.
4. **Artifact panel:** generated work is a first-class document/code/file surface with header/status/context, not a decorative preview.
5. **Low-friction onboarding:** minimal form, Google/email options, black CTA, quiet privacy note, warm human/editorial image.
6. **Feature modal:** warm rounded dialog, small demo/preview, compact copy, tiny status pill, one CTA.

## Evidence status

- Local Mobbin visual corpus: 211 files.
- Firecrawl public web extraction: saved for Anthropic Claude product page; Claude home direct local scrape is partial/403.
- Component atlas: added at `components/component-atlas.md`.
- Deterministic analysis artifacts: contact sheets + OCR/color metadata under `evidence/analysis/`.
- Computed browser styles: pending.
- Fresh-agent offline eval: pending.


## Component atlas excerpt

# Component Atlas — Anthropic / Claude

Status: draft v0.3, expanded from 211 local Mobbin references + OCR/color metadata.

This atlas is the layer agents should use when they need to build concrete components, not just follow the high-level mood.

## 1. App shell

### Structure

```text
Claude shell
├── Warm left sidebar
│   ├── Claude mark / new chat
│   ├── Search
│   ├── Customize instructions / styles
│   ├── Chats
│   ├── Projects
│   ├── Artifacts
│   └── Code / settings / account affordances
└── Main canvas
    ├── Welcome / current conversation / artifact
    ├── Optional right artifact/work panel
    └── Composer command card
```

### Rules

- Sidebar is compact and quiet; it should not visually compete with the current work.
- Active states prefer pale beige fill or subtle row treatment, not saturated color.
- Icons are thin, utility-first, and usually monochrome.
- The main canvas is intentionally sparse; whitespace is part of the interface.
- Navigation labels are short: `Chats`, `Projects`, `Artifacts`, `Code`, `Customize`.

## 2. Composer / command card

### Observed variants

- Welcome-state central prompt.
- Conversation-state bottom composer.
- Workbench-style composer with model/style/source/action controls.
- Attachment affordances: add photos, screenshot, project, connectors, research, style.
- Model selector and usage/plan hints appear as compact secondary controls.

### Component grammar

```text
Composer
├── Input line / textarea
├── Optional mode/context chips
│   ├── model
│   ├── style
│   ├── project/source
│   ├── connector/tool
│   └── research/code/artifact mode
└── Single send/run button
```

### Rules

- Composer is the command center, not a decorative search box.
- Use a warm off-white surface, thin warm-gray border, and minimal shadow.
- Context controls are chips/pills inside or directly under the composer.
- Keep the send/run button small and semantic; do not make it a giant CTA.

## 3. Chat and answer surfaces

### Patterns

- User prompts are compact and subordinate to the answer/work output.
- Assistant output often reads like a document: headings, paragraphs, tables, bullet structures.
- Image analysis / data analysis outputs use structured document cards with tables and section headings.
- Follow-up prompts/suggestions stay secondary.

### Rules

- Do not over-bubble the chat.
- Put generated value into document/artifact surfaces.
- Use tables when the task is analytical, but wrap them in readable prose hierarchy.
- Keep source/status notifications quiet.

## 4. Artifact / workbench panels

### Observed moments

- Image analysis request → structured report.
- Design workflow optimization → artifact-like result.
- Code / skill / file navigator surfaces.
- Claude Code / artifact pages with project-like hierarchy and compact control rows.

### Component grammar

```text
Artifact panel
├── Artifact title / file name
├── Status or context row
├── Main generated object
│   ├── document
│   ├── code
│   ├── table
│   ├── preview
│   └── chart/analysis block
└── Actions: copy, open, edit, publish/share, continue
```

### Rules

- Artifacts are first-class work surfaces; they must look usable, not decorative.
- Use a dark inverse panel only for code/developer/proof surfaces.
- Document artifacts should stay warm/white with subtle borders.
- Avoid heavy dashboard chrome around artifacts.

## 5. Settings, profile, billing, and styles

### Observed components

- Settings modal/page with left tab rail: profile, billing, account, etc.
- Profile fields: full name, what to call you, work description.
- Toggles: prompt suggestions, artifacts, feature preferences.
- Style customization: tabs/options such as `Learning`, `Concise`, `Explanatory`, `Formal`.
- Plan/subscription controls embedded in account/billing contexts.

### Rules

- Settings should be boring, calm, and legible.
- Use a two-column layout: left navigation/tabs, right settings form.
- Preference controls are rows with clear labels and short explanatory helper text.
- Toggles and destructive actions should be isolated from regular profile fields.

## 6. Onboarding / login / verification

### Flow grammar

```text
Auth/onboarding
├── Brand/header/nav
├── Social auth or email field
├── Phone/verification step if required
├── Brief introduction from Claude
├── Safety/privacy capability caveats
├── Plan selection if needed
└── Handoff into app shell
```

### Rules

- Low-friction first: Google/email/SSO before long forms.
- Verification screens are centered, sparse, and reassuring.
- Privacy/safety notes are visible but low-emphasis.
- Claude introduces itself as a working partner, not as a mascot.
- The onboarding tone is patient and calm; no growth-hack urgency.

## 7. Subscription, pricing, and upgrade flows

### Observed components

- Free / Pro / Max cards.
- Monthly/yearly toggle with savings note.
- Feature bullet lists with understated icons/checks.
- Upgrade dialogs and subscription confirmation steps.
- Plan comp

[truncated in unified pack view; see source file for full content]


## Agent contract excerpt

# Agent contract — Anthropic / Claude Editorial Workbench

This contract tells an agent how to use `anthropic-claude` inside the unified Hermes design pack.

## Required load order

1. `pack/styles/anthropic-claude/DESIGN.md` — unified style entry and broad baseline context.
2. `pack/extensions/anthropic-claude/STYLE.md` — concise runtime formula and operating rules.
3. `pack/extensions/anthropic-claude/tokens/tokens.json` plus `tokens/css-vars.css` — implementation anchors.
4. `pack/extensions/anthropic-claude/components/component-atlas.md` — choose the closest reusable surface.
5. `pack/extensions/anthropic-claude/components/capsules/<component-id>.md` — detailed component grammar.
6. `pack/components/anthropic-claude/<component-id>.md` — compact semantic retrieval slice.
7. `pack/extensions/anthropic-claude/eval/checklist.yaml`, `eval/rubric.md`, and `eval/failure-modes.md` — quality gate.

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

