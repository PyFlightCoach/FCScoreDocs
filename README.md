# FCScoreDocs
Flight Coach Score Documentation

This site is deployed [here](https://pyflightcoach.github.io/FCScoreDocs/)

## Local development

Install dependencies:

```bash
python -m pip install -e .
```

Build docs:

```bash
mkdocs build
```

Serve locally:

```bash
mkdocs serve
```

## Downgrade reference

`docs/downgrades/<discipline>.md` are generated from FCScore's Tuning data
(`packages/Tuning/src/tuning/data/<discipline>/` in FCScoreFuture). Do not edit
them by hand. With an FCScoreFuture checkout next to this repository:

```bash
uv run python scripts/generate_downgrades.py --tuning ../FCScoreFuture/packages/Tuning
```

`--check` exits 1 if a committed page differs from what the Tuning data would
produce (the recorded Tuning commit line is ignored). Run it after changing
Tuning descriptions. The generated pages are committed, so the Pages build does
not need FCScoreFuture. Each downgrade's anchor is its key (`#track_z`,
`#inter.loop_radius`), and each rulebook extract's is `#rb-<judging_guide key>`;
these anchors are a contract for links from the client.

