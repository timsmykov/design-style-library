# Unified DESIGN.md — Perplexity Answer Engine

This file is the single-pack runtime view for `perplexity-answer-engine`.

Authority inside this file:

1. VoltAgent DESIGN.md baseline gives broad visual grammar.
2. Hermes deep extension overrides baseline with local evidence, tokens, components, eval, and implementation guardrails.
3. Use local paths only; do not call GitHub/Mobbin/web/browser at runtime.

Local extension root: `pack/extensions/perplexity-answer-engine`
Component semantic slices: `pack/components/perplexity-answer-engine`

---

## Baseline

No exact VoltAgent DESIGN.md baseline exists. Use the global pack catalog plus this deep extension.


---

# Hermes deep extension override

## STYLE.md excerpt

# Perplexity Answer Engine

Status: runtime-ready extension inside the unified Hermes design pack.

## Style formula

"Evidence-backed Perplexity Answer Engine style grammar derived from local tokens, component capsules, and captured visual corpus."

This pack is meant for generation, review, and critique. It should give an agent enough local information to design a screen without opening Mobbin, GitHub, a browser, or any external gallery. The goal is style grammar and product-pattern transfer, not brand impersonation or exact screen cloning.

## When to use

Use this style when the requested artifact matches the product job, emotional temperature, and UI density of `perplexity-answer-engine`. If the task names this brand/style directly, use this extension. If the task only names a category, route here when the component set below matches the requested surface better than the other packs.

## Visual and interaction principles

- Start from the user job and select the closest local component capsule before choosing colors or decorative treatment.
- Preserve hierarchy first: primary object, secondary metadata, tertiary controls, then ambient decoration.
- Use the token system rather than ad-hoc colors. Color anchors: `canvas`=#ffffff; `surface`=#f8faf9; `surface_elevated`=#ffffff; `text`=#101817; `muted`=#5f6f6d; `border`=#dbe4e2; `teal`=#208c88; `teal_dark`=#146c69; `citation_bg`=#eef7f6; `warning_soft`=#fff7e6.
- Use the typography roles deliberately. Type anchors: `font_stack`=Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif; `answer_size`=16px; `ui_size`=13px; `caption_size`=12px; `line_height_answer`=1.65.
- Respect the shape and density system: spacing scale present, radius scale present.
- Prefer restrained adaptation over literal copying. Do not reuse logos, exact text, private data, or proprietary screen layout one-to-one.

## Runtime component set

- `answer-results-thread` — answer results thread
- `app-shell-sidebar` — app shell sidebar
- `collections-library` — collections library
- `follow-up-related-questions` — follow up related questions
- `help-article-layout` — help article layout
- `onboarding-auth` — onboarding auth
- `pro-upgrade-pricing` — pro upgrade pricing
- `public-landing-pricing` — public landing pricing
- `search-composer` — search composer
- `settings-account` — settings account
- `sources-citation-strip` — sources citation strip

For each component, load the capsule in `components/capsules/<component-id>.md` first. Then use `components/extracted/` and `evidence/source-map/` only when you need provenance or visual facts. Use `pack/components/perplexity-answer-engine/` for short semantic slices when a retrieval system asks for compact component context.

## Evidence coverage

- Mobbin screens: 45
- Mobbin sections: 4
- Mobbin flow previews: 0
- Public web pages captured: 4
- Authenticated screenshots: 1

These are build-time artifacts already stored locally. Runtime agents must not fetch more evidence unless explicitly asked to run a new extraction wave.

## Agent recipe

1. Read `pack/styles/perplexity-answer-engine/DESIGN.md` for the unified baseline + extension view.
2. Load `pack/extensions/perplexity-answer-engine/tokens/tokens.json` and `tokens/css-vars.css` for implementation values.
3. Pick 1-3 capsules from `pack/extensions/perplexity-answer-engine/components/capsules/` that match the requested screen.
4. Compose with the local style formula and component grammar.
5. Run the result against `pack/extensions/perplexity-answer-engine/eval/checklist.yaml` and `eval/failure-modes.md`.
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

Runtime component atlas for `perplexity-answer-engine`.

Use this file to choose the right capsule before implementation. The capsule is the detailed recipe; this atlas is the router.

## `answer-results-thread` — Answer Results Thread

Use when: the artifact needs `answer results thread` behavior, layout, or decision structure.
Capsule: `components/capsules/answer-results-thread.md`
Semantic slice: `pack/components/perplexity-answer-engine/answer-results-thread.md`
Evidence links recorded: `3` index path groups; see local source map and extracted folders for detail.

Design job:
- Preserve this style formula: Evidence-backed Perplexity Answer Engine style grammar derived from local tokens, component capsules, and captured visual corpus.
- Keep the component's primary object obvious before adding decoration.
- Use token roles and density from `tokens/tokens.json` instead of inventing ad-hoc values.
- Adapt the grammar to the new product context; do not clone exact evidence screens.

Implementation notes:
- Start with semantic structure and states.
- Add controls, status, metadata, and supporting copy in that order.
- Check responsive behavior and empty/error/loading states when relevant.

Evidence excerpt:
> # Answer Results Thread ## Use when Use this component for answer citations sources follow-up related question thread result in an answer-first, source-backed interface. ## Structure ```text Component ├── concise label/title ├── content or control body ├── evidence/context metadata └── compact action row ``` ## Implementation recipe - Use white or cool-off-white surfaces with thin neutral borders. - Keep typography crisp and utility-sized around the answer body. - Use teal only for active/action

## `app-shell-sidebar` — App Shell Sidebar

Use when: the artifact needs `app shell sidebar` behavior, layout, or decision structure.
Capsule: `components/capsules/app-shell-sidebar.md`
Semantic slice: `pack/components/perplexity-answer-engine/app-shell-sidebar.md`
Evidence links recorded: `3` index path groups; see local source map and extracted folders for detail.

Design job:
- Preserve this style formula: Evidence-backed Perplexity Answer Engine style grammar derived from local tokens, component capsules, and captured visual corpus.
- Keep the component's primary object obvious before adding decoration.
- Use token roles and density from `tokens/tokens.json` instead of inventing ad-hoc values.
- Adapt the grammar to the new product context; do not clone exact evidence screens.

Implementation notes:
- Start with semantic structure and states.
- Add controls, status, metadata, and supporting copy in that order.
- Check responsive behavior and empty/error/loading states when relevant.

Evidence excerpt:
> # App Shell Sidebar ## Use when Use this component for home discover library spaces collections threads sidebar in an answer-first, source-backed interface. ## Structure ```text Component ├── concise label/title ├── content or control body ├── evidence/context metadata └── compact action row ``` ## Implementation recipe - Use white or cool-off-white surfaces with thin neutral borders. - Keep typography crisp and utility-sized around the answer body. - Use teal only for active/action/proof accent

## `collections-library` — Collections Library

Use when: the artifact needs `collections library` behavior, layout, or decision structure.
Capsule: `components/capsules/collections-library.md`
Semantic slice: `pack/components/perplexity-answer-engine/collections-library.md`
Evidence links recorded: `3` index path groups; see local source map and extracted folders for detail.

Design job:
- Preserve this style formula: Evidence-backed Perplexity Answer Engine style grammar derived from local tokens, component capsules, and captured visual corpus.
- Keep the component's primary object obvious before adding decoration.
- Use token roles and density from `tokens/tokens.json` instead of inventing ad-hoc values.
- Adapt the grammar to the new product context; do not clone exact evidence screens.

Implementation notes:
- Start with semantic structure and states.
- Add controls, status, metadata, and supporting copy in that order.
- Check responsive behavior and empty/error/loading states when relevant.

Evidence excerpt:
> # Collections Library ## Use when Use this component for collections library spaces saved threads in an answer-first, source-backed interface. ## Structure ```text Component ├── concise label/title ├── content or control body ├── evidence/context metadata └── compact action row ``` ## Implementation recipe - Use white or cool-off-white surfaces with thin neutral borders. - Keep typography crisp and utility-sized around the answer body. - Use teal only for active/action/proof accents. - Preserve 

## `follow-up-related-questions` — Follow Up Related Questions

Use when: the artifact needs `follow up related questions` behavior, layout, or decision structure.
Capsule: `components/capsul

[truncated in unified pack view; see source file for full content]


## Agent contract excerpt

# Agent contract — Perplexity Answer Engine

This contract tells an agent how to use `perplexity-answer-engine` inside the unified Hermes design pack.

## Required load order

1. `pack/styles/perplexity-answer-engine/DESIGN.md` — unified style entry and broad baseline context.
2. `pack/extensions/perplexity-answer-engine/STYLE.md` — concise runtime formula and operating rules.
3. `pack/extensions/perplexity-answer-engine/tokens/tokens.json` plus `tokens/css-vars.css` — implementation anchors.
4. `pack/extensions/perplexity-answer-engine/components/component-atlas.md` — choose the closest reusable surface.
5. `pack/extensions/perplexity-answer-engine/components/capsules/<component-id>.md` — detailed component grammar.
6. `pack/components/perplexity-answer-engine/<component-id>.md` — compact semantic retrieval slice.
7. `pack/extensions/perplexity-answer-engine/eval/checklist.yaml`, `eval/rubric.md`, and `eval/failure-modes.md` — quality gate.

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
