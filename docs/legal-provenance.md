# Provenance and Non-Cloning Guardrails

This repository is a local reference and distillation system. It is not a brand-clone kit.

## Allowed

- Store local screenshots/reference images for internal design research.
- Store original source URLs and capture metadata.
- Extract observable design facts: fonts, colors, spacing, radii, shadows, hierarchy, layout mechanisms.
- Translate evidence into an original reusable style system.
- Generate inspired artifacts that avoid logos, protected marks, and exact clones.

## Forbidden

- Use copied proprietary CSS as a runtime dependency.
- Reproduce logos, brand marks, or exact branded pages unless explicitly authorized.
- Pixel-perfect clone proprietary interfaces for deployment.
- Treat extracted classnames/bundles as source code to ship.
- Hide source limitations or confidence levels.

## Required provenance for every source

- source type: mobbin | public_web | browser_probe | manual | generated_eval;
- original URL when applicable;
- local file path;
- captured_at date/time;
- scope and limitations;
- confidence: observed | extracted | inferred | adapted | experimental.
