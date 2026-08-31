# Public publication audit

Audit date: 2026-08-31

## Decision

The curated GitHub snapshot is suitable for public visibility. Local reference
screenshots remain in the repository. Live Mobbin template, flow, screen, and
image URLs have been removed because access to the subscription is no longer
available; all runtime style entrypoints remain self-contained.

## Checks performed

- Gitleaks scanned the complete Git history: no secrets found.
- Gitleaks scanned the current working tree, including uncommitted publication
  changes: no secrets found.
- All eight screenshots under source-side `evidence/authenticated/` were
  reviewed visually and with OCR. They show public pages, login/security
  barriers, cookie dialogs, or disconnected/empty product states; no email
  address or wallet address is visible.
- Text under source-side `evidence/authenticated/` contains no email address.
- Private G-Brain exports remain excluded except for compact generated
  component slices under `gbrain_export/components/`.
- Raw captures previously flagged for embedded client API configuration are not
  present in this GitHub snapshot or its history.
- Repository verification passes with 74 broad styles and 12 deep packs (86
  runtime entrypoints).
- JSON, JSONL, and CSV files were parsed after Mobbin-link removal.
- A repository-wide search confirms zero remaining `mobbin.com` URLs.

## Residual rights boundary

Reference screenshots, captured pages, logos, and other third-party material
remain subject to their owners' rights. Public repository visibility does not
grant a blanket license to reuse those assets. See `SHARING.md`.
