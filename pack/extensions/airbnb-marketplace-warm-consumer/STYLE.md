# Airbnb Marketplace Warm Consumer

Status: runtime-ready extension inside the unified Hermes design pack.

## Style formula

warm consumer marketplace; photo-first listing cards; search/filter/map rhythm; hospitality trust, reviews and booking clarity; soft neutral canvas with confident coral action

This pack is meant for generation, review, and critique. It should give an agent enough local information to design a screen without opening Mobbin, GitHub, a browser, or any external gallery. The goal is style grammar and product-pattern transfer, not brand impersonation or exact screen cloning.

## When to use

Use this style when the requested artifact matches the product job, emotional temperature, and UI density of `airbnb-marketplace-warm-consumer`. If the task names this brand/style directly, use this extension. If the task only names a category, route here when the component set below matches the requested surface better than the other packs.

## Visual and interaction principles

- Start from the user job and select the closest local component capsule before choosing colors or decorative treatment.
- Preserve hierarchy first: primary object, secondary metadata, tertiary controls, then ambient decoration.
- Use the token system rather than ad-hoc colors. Color anchors: `canvas`=#ffffff; `surface`=#ffffff; `panel`=#f7f7f7; `text`=#222222; `muted`=#717171; `border`=#dddddd; `accent`=#ff385c; `accent2`=#00a699.
- Use the typography roles deliberately. Type anchors: `ui`=Inter/system sans-serif; `mono`=ui-monospace/SFMono-Regular.
- Respect the shape and density system: spacing scale present, radius scale present.
- Prefer restrained adaptation over literal copying. Do not reuse logos, exact text, private data, or proprietary screen layout one-to-one.

## Runtime component set

- `booking-card` — booking card
- `category-tabs` — category tabs
- `checkout-reservation-flow` — checkout reservation flow
- `filter-modal` — filter modal
- `host-profile-card` — host profile card
- `listing-card` — listing card
- `listing-detail-gallery` — listing detail gallery
- `map-results-layout` — map results layout
- `reviews-section` — reviews section
- `search-bar` — search bar

For each component, load the capsule in `components/capsules/<component-id>.md` first. Then use `components/extracted/` and `evidence/source-map/` only when you need provenance or visual facts. Use `pack/components/airbnb-marketplace-warm-consumer/` for short semantic slices when a retrieval system asks for compact component context.

## Evidence coverage

- Mobbin screens: 20
- Mobbin sections: 20
- Mobbin flow previews: 25
- Public web pages captured: 1
- Authenticated screenshots: 1

These are build-time artifacts already stored locally. Runtime agents must not fetch more evidence unless explicitly asked to run a new extraction wave.

## Agent recipe

1. Read `pack/styles/airbnb-marketplace-warm-consumer/DESIGN.md` for the unified baseline + extension view.
2. Load `pack/extensions/airbnb-marketplace-warm-consumer/tokens/tokens.json` and `tokens/css-vars.css` for implementation values.
3. Pick 1-3 capsules from `pack/extensions/airbnb-marketplace-warm-consumer/components/capsules/` that match the requested screen.
4. Compose with the local style formula and component grammar.
5. Run the result against `pack/extensions/airbnb-marketplace-warm-consumer/eval/checklist.yaml` and `eval/failure-modes.md`.
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
