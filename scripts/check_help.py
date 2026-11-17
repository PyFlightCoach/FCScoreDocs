"""Advisory check that docs/help/ matches the client's help routes.

Mirrors helpFileName() in FlightCoachScore/src/routes/help-file.ts. Each
src/routes/**/+page.svelte maps to one help file name; this reports which
names have a matching docs/help/<name>.md and which help files no route uses.
"""

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS_HELP = ROOT / "docs" / "help"
HELP_FILE_TS = Path("src/routes/help-file.ts")

# Must match helpAliases in help-file.ts.
EXPECTED_ALIASES = {
    "flight_box": "flight_create_box",
    "flight_segmentation": "flight_create_manoeuvres",
}
GROUP_OR_PARAM = re.compile(r"^[\[(].*[\])]$")
ALIAS_PAIR = re.compile(r"""['"]?(\w+)['"]?\s*:\s*['"](\w+)['"]""")


def route_id(page: Path, routes_dir: Path) -> str:
    rel = page.parent.relative_to(routes_dir).as_posix()
    return "/" if rel == "." else "/" + rel


def help_file_name(route: str) -> str:
    segments = [
        s
        for s in route.split("/")
        if s and s != "FlightCoachScore" and not GROUP_OR_PARAM.match(s)
    ]
    name = "_".join(segments)
    return EXPECTED_ALIASES.get(name, name) or "home"


def check_client_shape(help_ts: Path) -> list[str]:
    if not help_ts.is_file():
        return [f"WARNING: {help_ts} not found; alias map not verified"]
    text = help_ts.read_text(encoding="utf-8")
    warnings = []
    if "function helpFileName" not in text:
        warnings.append("WARNING: helpFileName() not found in help-file.ts")
    match = re.search(r"helpAliases[^=]*=\s*\{(.*?)\}", text, re.S)
    if not match:
        warnings.append("WARNING: helpAliases map not found in help-file.ts")
    else:
        pairs = dict(ALIAS_PAIR.findall(match.group(1)))
        if pairs != EXPECTED_ALIASES:
            warnings.append(
                f"WARNING: helpAliases in help-file.ts is {pairs}, "
                f"script expects {EXPECTED_ALIASES}; update scripts/check_help.py"
            )
    return warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--client",
        type=Path,
        default=Path("../FlightCoachScore"),
        help="path to a FlightCoachScore checkout (default: ../FlightCoachScore)",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="exit 1 if any route has no matching help file",
    )
    args = parser.parse_args()

    client = args.client.resolve()
    routes_dir = client / "src" / "routes"
    if not routes_dir.is_dir():
        print(f"ERROR: {routes_dir} not found; pass --client <FlightCoachScore checkout>")
        return 1

    for warning in check_client_shape(client / HELP_FILE_TS):
        print(warning)

    pages = sorted(routes_dir.glob("**/+page.svelte"))
    expected: dict[str, list[str]] = {}
    for page in pages:
        route = route_id(page, routes_dir)
        expected.setdefault(help_file_name(route), []).append(route)

    print("Routes and help files:")
    missing = []
    for name in sorted(expected):
        exists = (DOCS_HELP / f"{name}.md").is_file()
        if not exists:
            missing.append(name)
        for route in expected[name]:
            status = "ok" if exists else "MISSING"
            print(f"  {status:8} {name:32} {route}")

    present = {p.stem for p in DOCS_HELP.glob("*.md")}
    unused = sorted(present - set(expected))
    print("Help files not used by any route:")
    for name in unused:
        print(f"  {name}.md")
    if not unused:
        print("  (none)")

    print(f"Summary: {len(pages)} routes, {len(missing)} missing help file(s), "
          f"{len(unused)} unused help file(s)")
    if args.strict and missing:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
