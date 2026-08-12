# Validation — Browser & Web Experience

The canonical release was functionally validated in Azure Data Explorer before publication.

Validated areas:

- all 20 tiles return data in the validated lab dataset;
- Browser values render friendly names such as Chrome and Edge;
- Website cross-filter selections update the global Website parameter;
- all 20 tile queries consume the Website selection;
- Request Type `All` state is handled correctly;
- query references and parameter references are valid;
- no KQL integer literal uses the `L` suffix;
- Schema 78 object model is preserved.

Environment-specific results depend on the telemetry available in the target ADX database.
