# Validation

The release JSON was created from a dashboard exported by Azure Data Explorer
after functional validation.

Validated release structure:

- Schema version: 78
- Pages: 4
- Tiles: 15
- Parameters: 6
- Query-backed parameters: 5
- Query definitions: 20
- Base queries: 0

Before production use, validate that both required ADX tables contain data in
the selected time range and confirm that all filters and visuals return
expected results for your environment.