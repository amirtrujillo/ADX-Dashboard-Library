#!/usr/bin/env python3
"""Validate ADX dashboard JSON and extracted KQL files."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]

NUMERIC_L_SUFFIX = re.compile(r"(?<![A-Za-z0-9_])\d+L\b")
SPLUNK_DEPENDENCY = re.compile(r"\b(?:splunk|sourcetype|index\s*=)\b", re.IGNORECASE)


def duplicates(values: list[str]) -> list[str]:
    counts = Counter(values)
    return sorted(value for value, count in counts.items() if count > 1)


def query_refs(payload: dict[str, Any]) -> list[str]:
    refs: list[str] = []

    for tile in payload.get("tiles", []):
        query_id = tile.get("queryRef", {}).get("queryId")
        if query_id:
            refs.append(query_id)

    for parameter in payload.get("parameters", []):
        query_id = (
            parameter.get("dataSource", {})
            .get("queryRef", {})
            .get("queryId")
        )
        if query_id:
            refs.append(query_id)

    return refs


def validate_dashboard(path: Path) -> list[str]:
    errors: list[str] = []

    try:
        payload = json.loads(path.read_text(encoding="utf-8-sig"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"{path}: invalid JSON: {exc}"]

    required_lists = ["pages", "tiles", "parameters", "queries", "dataSources"]
    for key in required_lists:
        if not isinstance(payload.get(key), list):
            errors.append(f"{path}: {key} must be a list")

    if errors:
        return errors

    if not payload.get("title"):
        errors.append(f"{path}: title is required")

    if payload.get("schema_version") != 78:
        errors.append(
            f"{path}: expected schema_version 78, "
            f"found {payload.get('schema_version')!r}"
        )

    groups = {
        "page": [item.get("id", "") for item in payload["pages"]],
        "tile": [item.get("id", "") for item in payload["tiles"]],
        "parameter": [item.get("id", "") for item in payload["parameters"]],
        "query": [item.get("id", "") for item in payload["queries"]],
        "data source": [item.get("id", "") for item in payload["dataSources"]],
    }

    for label, values in groups.items():
        if any(not value for value in values):
            errors.append(f"{path}: every {label} must have an ID")
        repeated = duplicates(values)
        if repeated:
            errors.append(f"{path}: duplicate {label} IDs: {repeated}")

    page_ids = set(groups["page"])
    query_ids = set(groups["query"])
    data_source_ids = set(groups["data source"])

    for tile in payload["tiles"]:
        if tile.get("pageId") not in page_ids:
            errors.append(
                f"{path}: tile {tile.get('title')!r} references unknown page"
            )

    refs = query_refs(payload)
    repeated_refs = duplicates(refs)
    if repeated_refs:
        errors.append(f"{path}: duplicate query references: {repeated_refs}")

    missing_refs = sorted(set(refs) - query_ids)
    if missing_refs:
        errors.append(f"{path}: missing query references: {missing_refs}")

    for query in payload["queries"]:
        query_id = query.get("id")
        source_id = query.get("dataSource", {}).get("dataSourceId")
        text = query.get("text", "")

        if source_id not in data_source_ids:
            errors.append(
                f"{path}: query {query_id} references unknown data source "
                f"{source_id!r}"
            )
        if NUMERIC_L_SUFFIX.search(text):
            errors.append(f"{path}: query {query_id} uses a numeric L suffix")
        if SPLUNK_DEPENDENCY.search(text):
            errors.append(
                f"{path}: query {query_id} contains a Splunk-specific dependency"
            )

    return errors


def collect_json_files(items: list[str]) -> list[Path]:
    files: list[Path] = []

    for raw in items:
        path = (ROOT / raw).resolve() if not Path(raw).is_absolute() else Path(raw)
        if path.is_dir():
            files.extend(sorted(path.rglob("*.json")))
        elif path.is_file() and path.suffix.lower() == ".json":
            files.append(path)
        else:
            print(f"WARNING: skipped {path}")

    return files


def validate_kql_tree(path: Path) -> list[str]:
    errors: list[str] = []
    if not path.exists():
        return errors

    for kql_file in sorted(path.rglob("*.kql")):
        text = kql_file.read_text(encoding="utf-8-sig")
        if NUMERIC_L_SUFFIX.search(text):
            errors.append(f"{kql_file}: numeric L suffix detected")
        if SPLUNK_DEPENDENCY.search(text):
            errors.append(f"{kql_file}: Splunk-specific dependency detected")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "paths",
        nargs="*",
        default=["source/adx", "dist"],
        help="Dashboard JSON file or directory paths.",
    )
    parser.add_argument(
        "--queries",
        default="queries",
        help="Generated KQL directory.",
    )
    args = parser.parse_args()

    files = collect_json_files(args.paths)
    errors: list[str] = []

    if not files:
        print("ERROR: no dashboard JSON files found")
        return 1

    for path in files:
        print(f"Validating {path.relative_to(ROOT)}")
        errors.extend(validate_dashboard(path))

    errors.extend(validate_kql_tree(ROOT / args.queries))

    if errors:
        print("\nValidation FAILED\n")
        for error in errors:
            print(f"- {error}")
        return 1

    print("\nValidation PASSED")
    print(f"Dashboard JSON files validated: {len(files)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
