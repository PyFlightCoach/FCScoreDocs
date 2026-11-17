# FCScoreDocs

Flight Coach Score Documentation

This site is deployed [here](https://pyflightcoach.github.io/FCScoreDocs/)

## Local development

Install the locked environment (uv 0.13.8, see the pinned version in `.github/workflows/pages.yml`):

```bash
uv sync
```

Serve locally:

```bash
uv run mkdocs serve
```

Build with strict checks:

```bash
uv run mkdocs build --strict
```

`DOCS_SITE_URL` overrides `site_url` in `mkdocs.yml`, for example when building for a preview deployment.

## Help pages

Files in `docs/help/` are not in the navigation. They are copied verbatim to `help/<name>.md` in the built site, because FlightCoachScore's help panel fetches them as raw Markdown. The file names must match the client's `helpFileName()` in `src/routes/help-file.ts`.

Check the help files against a FlightCoachScore checkout:

```bash
uv run python scripts/check_help.py --client ../FlightCoachScore
```

Add `--strict` to fail when a route has no matching help file.
