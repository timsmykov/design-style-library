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
- Plan comparison tables and usage limit explanations.

### Rules

- Pricing cards are clean, text-heavy, and trust-oriented.
- CTA hierarchy stays restrained: one dominant plan action per card or plan row.
- Use the same warm paper/card system, not fintech-blue checkout styling.
- Explain tradeoffs plainly: usage, priority access, model access, projects, memory, connectors, code/research.

## 8. Website hero and editorial sections

### Hero variants

- `Claude is AI for all of us.`
- `Meet your thinking partner.`
- `Break down problems together.`
- `The AI for problem solvers.`
- `Researching at the frontier.`

### Rules

- Large editorial headline, often serif-like or literary.
- Short, human, problem-solving subcopy.
- Warm paper canvas.
- Single black/dark CTA or subtle paired CTA.
- Hero visual is human/symbolic/product-proof, never robot/neon.

## 9. Product tiles and feature blocks

### Observed tiles

- `Talk to Claude` vs `Build with Claude` two-card product split.
- `How you can use Claude`: write, code, research, analyze, create.
- Use-case grid: coding, agents, productivity, customer support.
- Capability grid: reasoning, vision, code generation, multilingual.
- News/resource cards for product announcements and best practices.

### Component grammar

```text
Tile block
├── Section eyebrow / heading
├── 2–4 large cards or 3–6 compact cards
├── Each card: title, short body, small proof visual or icon
└── Optional CTA/link row
```

### Rules

- Tiles are generous and editorial, not dense dashboard widgets.
- Each tile has one idea and one proof cue.
- Use black/ivory contrast for developer/API cards; warm light cards for consumer/productivity.
- Icons are small and often line/symbolic; avoid decorative icon overload.

## 10. Docs, help center, API, and release/news pages

### Observed components

- Docs side navigation + content column.
- Help center search field + topic cards.
- Release/news cards grouped by category/date.
- API/model pricing rows and tables.
- Language selector and support links.

### Rules

- Docs/help surfaces are more utilitarian but still warm.
- Side nav uses compact typography, muted selected states, and lots of whitespace.
- Search input is a core object in help surfaces.
- Release/news cards use editorial card rhythm, not blog-magazine chaos.

## 11. Model family / pricing / graph-like blocks

### Observed patterns

- Model-family comparison: Opus / Sonnet / Haiku ladder or stacked comparison.
- Pricing tables: input/output token pricing, plan comparison, feature lists.
- Capability grids: each capability gets title + explanatory paragraph + compact proof.
- Use-case matrices: rows/cards grouped by user job.

### How to reproduce charts/graphs in this style

- Prefer editorial figure cards over glossy dashboards.
- Use charcoal labels, warm-gray dividers, and one clay highlight for the key takeaway.
- If comparing models, present as a simple vertical ladder or compact table: model name, role, ideal use, price/performance note.
- If comparing plans, use cards first, table second.
- Avoid rainbow series, 3D charts, saturated blue/purple palettes, and over-animated dashboards.

## 12. Anti-patterns exposed by the larger corpus

- Treating Claude as only a beige chat app: the corpus includes docs, pricing, settings, model pages, product cards, help center, and developer surfaces.
- Over-indexing on one hero/product screenshot.
- Missing the settings/style-customization layer: Claude has explicit user style preferences.
- Missing pricing/subscription grammar: Free/Pro/Max and upgrade flows have a distinct trust pattern.
- Missing docs/API side-nav grammar: developer surfaces are more structured and utilitarian than marketing pages.
- Using clay everywhere: in the real corpus, clay is identity/focus, while most structure is neutral.
