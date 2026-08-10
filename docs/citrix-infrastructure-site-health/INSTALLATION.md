# Installation

1. Open Azure Data Explorer.
2. Open Dashboards.
3. Import the dashboard JSON from dist.
4. Configure the ADX_Observability data source.
5. Set the cluster to your ADX cluster.
6. Set the database to the database containing the required Citrix and
   uberAgent tables.
7. Save the dashboard.
8. Confirm the parameters populate.
9. Validate all five pages.

The public JSON uses these placeholders:

- cluster: $PublicCluster
- database: $PublicDatabase

Do not replace the public repository copy with environment-specific values.