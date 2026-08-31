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
