#!/usr/bin/env python3
"""Build import-ready ADX dashboards and extract their KQL queries."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
MAPPING_PATH = ROOT / "mapping.json"


def safe_name(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9]+", "_", value).strip("_") or "Query"


def load_mapping() -> dict[str, Any]:
    try:
        return json.loads(MAPPING_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"Unable to read {MAPPING_PATH}: {exc}") from exc


def load_dashboard(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8-sig"))
    except (OSError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"Unable to read dashboard JSON {path}: {exc}") from exc


def extract_queries(
    dashboard: dict[str, Any],
    output_root: Path,
    version: str,
) -> None:
    if output_root.exists():
        shutil.rmtree(output_root)

    tile_dir = output_root / "tiles"
    parameter_dir = output_root / "parameters"
    tile_dir.mkdir(parents=True, exist_ok=True)
    parameter_dir.mkdir(parents=True, exist_ok=True)

    query_by_id = {
        query["id"]: query
        for query in dashboard.get("queries", [])
        if query.get("id")
    }
    page_by_id = {
        page["id"]: page
        for page in dashboard.get("pages", [])
        if page.get("id")
    }
    page_order = {
        page["id"]: index
        for index, page in enumerate(dashboard.get("pages", []), start=1)
    }

    tile_rows: list[str] = []
    for tile_index, tile in enumerate(dashboard.get("tiles", []), start=1):
        query_id = tile.get("queryRef", {}).get("queryId")
        query = query_by_id.get(query_id)
        if not query:
            continue

        page = page_by_id.get(tile.get("pageId"), {})
        page_name = page.get("name", "Unknown Page")
        filename = (
            f"{page_order.get(tile.get('pageId'), 0):02d}_"
            f"{safe_name(page_name)}__"
            f"{tile_index:02d}_{safe_name(tile.get('title', 'Tile'))}.kql"
        )

        header = (
            f"// Dashboard: {dashboard.get('title', '')}\n"
            f"// Version: {version}\n"
            f"// Page: {page_name}\n"
            f"// Tile: {tile.get('title', '')}\n"
            f"// Query ID: {query_id}\n\n"
        )
        (tile_dir / filename).write_text(
            header + query.get("text", ""),
            encoding="utf-8",
            newline="\n",
        )
        tile_rows.append(
            f"- `{filename}` — {page_name} / {tile.get('title', '')}"
        )

    parameter_rows: list[str] = []
    for parameter_index, parameter in enumerate(
        dashboard.get("parameters", []),
        start=1,
    ):
        query_id = (
            parameter.get("dataSource", {})
            .get("queryRef", {})
            .get("queryId")
        )
        query = query_by_id.get(query_id)
        if not query:
            continue

        filename = (
            f"{parameter_index:02d}_"
            f"{safe_name(parameter.get('displayName', 'Parameter'))}.kql"
        )
        variable = parameter.get("variableName") or (
            f"{parameter.get('beginVariableName', '')} / "
            f"{parameter.get('endVariableName', '')}"
        )
        header = (
            f"// Dashboard: {dashboard.get('title', '')}\n"
            f"// Version: {version}\n"
            f"// Parameter: {parameter.get('displayName', '')}\n"
            f"// Variable: {variable}\n"
            f"// Query ID: {query_id}\n\n"
        )
        (parameter_dir / filename).write_text(
            header + query.get("text", ""),
            encoding="utf-8",
            newline="\n",
        )
        parameter_rows.append(
            f"- `{filename}` — {parameter.get('displayName', '')}"
        )

    readme = [
        f"# Extracted KQL — {dashboard.get('title', '')}",
        "",
        "These files are generated from the canonical dashboard JSON.",
        "Do not edit them directly. Edit the dashboard in `source/adx` and run",
        "`python scripts/build_dist.py`.",
        "",
        "## Tile queries",
        "",
        *tile_rows,
        "",
        "## Parameter queries",
        "",
        *parameter_rows,
        "",
    ]
    (output_root / "README.md").write_text(
        "\n".join(readme),
        encoding="utf-8",
        newline="\n",
    )


def build(selected: str | None = None) -> int:
    mapping = load_mapping()
    dashboards = mapping.get("dashboards", {})

    if not dashboards:
        print("ERROR: mapping.json does not define any dashboards.")
        return 1

    built = 0
    for mapping_name, entry in dashboards.items():
        if selected and selected not in {mapping_name, entry.get("slug")}:
            continue

        source = ROOT / entry["source"]
        destination = ROOT / entry["dist"]
        query_output = ROOT / entry["queries"]

        dashboard = load_dashboard(source)

        expected_title = entry.get("title")
        expected_schema = entry.get("schemaVersion")
        if dashboard.get("title") != expected_title:
            print(
                f"ERROR: {source} title is {dashboard.get('title')!r}; "
                f"expected {expected_title!r}."
            )
            return 1
        if dashboard.get("schema_version") != expected_schema:
            print(
                f"ERROR: {source} schema is {dashboard.get('schema_version')!r}; "
                f"expected {expected_schema!r}."
            )
            return 1

        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
        extract_queries(dashboard, query_output, str(entry.get("version", "")))

        print(f"Built {destination.relative_to(ROOT)}")
        print(f"Extracted queries to {query_output.relative_to(ROOT)}")
        built += 1

    if built == 0:
        print(f"ERROR: dashboard {selected!r} was not found in mapping.json.")
        return 1

    print(f"Build completed. Dashboards built: {built}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--dashboard",
        help="Optional dashboard filename or slug from mapping.json.",
    )
    args = parser.parse_args()
    return build(args.dashboard)


if __name__ == "__main__":
    sys.exit(main())
