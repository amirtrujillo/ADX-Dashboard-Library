# Validation

DASH-008 v0.1.0 was validated as a complete dashboard in Azure Data Explorer.

Validated topology:

- Schema 78
- 4 pages
- 15 tiles
- 6 parameters
- 20 query definitions
- 5 query-backed parameters
- 1 duration parameter

All 15 tiles executed successfully in the validated environment.

Public release sanitization also verifies:

- no private cluster name;
- no private database name;
- no local user path;
- no credentials/tokens;
- public cluster/database placeholders are present.