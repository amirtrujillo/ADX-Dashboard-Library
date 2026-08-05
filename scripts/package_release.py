#!/usr/bin/env python3
"""Create a versioned dashboard release ZIP from dist and extracted KQL."""

from __future__ import annotations

import argparse
import json
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--dashboard",
        required=True,
        help="Dashboard filename or slug from mapping.json.",
    )
    parser.add_argument(
        "--output",
        default="release-assets",
        help="Output directory for release ZIP files.",
    )
    args = parser.parse_args()

    mapping = json.loads((ROOT / "mapping.json").read_text(encoding="utf-8"))
    selected_name = None
    selected = None

    for name, entry in mapping.get("dashboards", {}).items():
        if args.dashboard in {name, entry.get("slug")}:
            selected_name = name
            selected = entry
            break

    if not selected:
        print(f"ERROR: dashboard {args.dashboard!r} was not found")
        return 1

    dist_file = ROOT / selected["dist"]
    queries_dir = ROOT / selected["queries"]
    if not dist_file.exists():
        print("ERROR: dist file is missing. Run scripts/build_dist.py first.")
        return 1

    output_dir = ROOT / args.output
    output_dir.mkdir(parents=True, exist_ok=True)
    zip_path = output_dir / (
        f"{selected['slug']}-v{selected['version']}.zip"
    )

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as archive:
        archive.write(dist_file, arcname=dist_file.name)

        if queries_dir.exists():
            for path in sorted(queries_dir.rglob("*")):
                if path.is_file():
                    archive.write(
                        path,
                        arcname=f"queries/{path.relative_to(queries_dir)}",
                    )

        for extra in ["README.md", "LICENSE", "CONTRIBUTING.md"]:
            path = ROOT / extra
            if path.exists():
                archive.write(path, arcname=extra)

    print(f"Created {zip_path.relative_to(ROOT)} for {selected_name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
