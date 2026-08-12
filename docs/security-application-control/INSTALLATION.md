# Installation

1. Download `Security & Application Control.adx.json` from the `dist` folder.
2. Open Azure Data Explorer Dashboards.
3. Import the dashboard JSON.
4. Edit the `ADX_Observability` data source.
5. Replace the placeholder cluster URI with your Azure Data Explorer cluster.
6. Replace `your-database` with the database containing the required tables.
7. Save the dashboard and select a time range with available data.

Required ADX tables:

- `ActivityMonitoring_ProcessTagging`
- `System_SecurityInventory`

Query-backed parameters return both `Value` and `Label` and default to `All`.