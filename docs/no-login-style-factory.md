# No-login Style Factory

Goal: repeat the Anthropic-style extraction depth for other products without requiring account login or credential submission.

## Decision

Yes, the factory can run without login for most style packs, but the evidence level is `partial/high`, not `offline_ready`, until any authenticated app-only surfaces and fresh-agent eval are done.

## No-login lanes

For each target style, run these lanes:

1. **Mobbin visual corpus**
   - screens: public/app screenshots available in Mobbin;
   - sections: marketing/pricing/docs/product sections;
   - flows: onboarding, upgrade, checkout, setup, cancellation, auth preview flows when available.

2. **Source map**
   - map every local image to Mobbin metadata, original image/API URL when available, local path, source type, flow position, OCR, palette, component match.

3. **Screenshot-derived component facts**
   - OCR text;
   - image dimensions and palette;
   - component classification;
   - token candidates;
   - normalized recipes.

4. **Public original-code evidence**
   - public marketing/pricing/docs pages;
   - DOM snapshots;
   - linked CSS evidence;
   - public Browser/CDP `getComputedStyle` facts for visible elements.

5. **Component capsules + Gbrain slices**
   - keep repo as source of truth;
   - export compact component slices to Gbrain;
   - do not index raw screenshots or large DOM/CSS dumps.

## What no-login cannot honestly capture

No-login mode cannot guarantee exact implementation facts for authenticated/private app interiors:

- logged-in dashboards;
- user-specific settings;
- private billing pages;
- project/workspace data views;
- editor/canvas internals behind auth;
- hover/focus/selected states that require real account state.

For those, create `AUTH_BLOCKERS.md` and leave the pack as `offline_ready: false` until authenticated Browser/CDP extraction and fresh-agent eval pass.

## Target quality bar per pack

Minimum credible pass:

| Layer | Minimum |
|---|---:|
| Local Mobbin refs | 80+ if available; target 150-300 for rich products |
| Source map rows | 100% of local refs |
| Component capsules | 8-15 |
| Public pages | 2-5 |
| Browser/CDP targets | 2-5 public/no-login targets |
| Gbrain slices | 1 per component capsule |
| Golden examples | 1-2 |
| Verifier | PASS |

## Batch targets after Anthropic

The first no-login batch is ten styles:

1. `perplexity-answer-engine`
2. `notion-document-os`
3. `linear-operational-workspace`
4. `stripe-trust-commerce`
5. `metamask-crypto-wallet-trust`
6. `vercel-developer-control-plane`
7. `raycast-command-native`
8. `figma-collaborative-canvas`
9. `airbnb-marketplace-warm-consumer`
10. `cursor-ai-ide`

## Suggested execution order

1. Perplexity — closest to Anthropic; validates answer/search/citation grammar.
2. Notion — document/block OS grammar.
3. Stripe — payments/trust/pricing grammar.
4. Linear — operational workspace grammar.
5. Vercel — developer control plane grammar.
6. Cursor — AI IDE/workbench grammar.
7. Figma — collaborative canvas grammar.
8. Raycast — command-native utility grammar.
9. MetaMask — crypto/wallet/risk grammar.
10. Airbnb — warm consumer marketplace grammar.

## Done criteria for each pack

- `manifest.yaml` status at least `draft`.
- `evidence/mobbin/` contains local refs.
- `evidence/source-map/` covers every local ref.
- `components/extracted/from-mobbin-screenshots/` exists.
- Public DOM/CSS/CDP evidence exists where public pages are available.
- `components/capsules/*.md` exists and component-index builds.
- `gbrain_export/components/<style>/*.md` exists and sync smoke passes.
- `tools/stylepack_verify.py .` passes.
- Known login/auth gaps are recorded, not hidden.
