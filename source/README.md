# The source Folder

- `source/adx` contains the canonical Azure Data Explorer dashboard JSON files.
- Modify the dashboard in Azure Data Explorer, export the accepted JSON, and
  replace the corresponding file in `source/adx`.
- Do not edit the generated files in `dist` or `queries` directly.
- The GitHub workflow runs `scripts/build_dist.py` to regenerate distribution
  files and extracted KQL.
