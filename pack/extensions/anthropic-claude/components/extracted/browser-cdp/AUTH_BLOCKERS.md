# Authenticated Claude App CDP Blockers

The local Chrome profile is not authenticated to Claude during this extraction run. No credentials or OAuth actions were submitted.

| Target | Requested | Captured | Result |
|---|---|---|---|
| `claude-new-auth-check` | https://claude.ai/new | https://claude.ai/login?from=logout&reauth=1&returnTo=%2Fnew | redirected to Claude login |
| `claude-settings-auth-check` | https://claude.ai/settings/profile | https://claude.ai/login?from=logout | redirected to Claude login |

To capture app-only surfaces later, Tim must authenticate Claude in the canonical Chrome profile or explicitly approve an authorization flow. Then rerun:

`./tools/cdp_component_extract.py`

Expected app-only components: `app-shell-sidebar`, `composer-command-card`, `artifact-workbench-panel`, `settings-preferences`.
