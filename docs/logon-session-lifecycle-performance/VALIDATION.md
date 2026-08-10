# Validation

The release was functionally validated in Azure Data Explorer before the
canonical export was captured.

Release checks:

- Schema 78
- 4 pages
- 21 tiles
- 4 parameters
- 24 unique query definitions
- 24 unique query references
- no integer L suffix literals
- query-backed parameters return both Value and Label
- User, Host, and Session filters function correctly
- all tiles render successfully in the validation environment

The exported working ADX dashboard is the canonical release source.
