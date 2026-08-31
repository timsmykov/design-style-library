# Agent contract — MetaMask / Crypto Wallet Trust

This contract tells an agent how to use `metamask-crypto-wallet-trust` inside the unified Hermes design pack.

## Required load order

1. `pack/styles/metamask-crypto-wallet-trust/DESIGN.md` — unified style entry and broad baseline context.
2. `pack/extensions/metamask-crypto-wallet-trust/STYLE.md` — concise runtime formula and operating rules.
3. `pack/extensions/metamask-crypto-wallet-trust/tokens/tokens.json` plus `tokens/css-vars.css` — implementation anchors.
4. `pack/extensions/metamask-crypto-wallet-trust/components/component-atlas.md` — choose the closest reusable surface.
5. `pack/extensions/metamask-crypto-wallet-trust/components/capsules/<component-id>.md` — detailed component grammar.
6. `pack/components/metamask-crypto-wallet-trust/<component-id>.md` — compact semantic retrieval slice.
7. `pack/extensions/metamask-crypto-wallet-trust/eval/checklist.yaml`, `eval/rubric.md`, and `eval/failure-modes.md` — quality gate.

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
