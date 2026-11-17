"""MkDocs hook that publishes help pages as raw Markdown.

FlightCoachScore's help panel fetches `<docs base>/help/<name>.md` as plain text.
The file names are a contract with FlightCoachScore/src/routes/help-file.ts
(helpFileName), so renaming a file here breaks the matching client help page.
"""

import shutil
from pathlib import Path


def on_post_build(config, **kwargs):
    docs_dir = Path(config["docs_dir"])
    out_dir = Path(config["site_dir"]) / "help"
    out_dir.mkdir(parents=True, exist_ok=True)
    for src in sorted((docs_dir / "help").glob("*.md")):
        shutil.copyfile(src, out_dir / src.name)
