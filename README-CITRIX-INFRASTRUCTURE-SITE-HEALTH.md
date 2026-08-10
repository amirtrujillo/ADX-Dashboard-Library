# Citrix Infrastructure & Site Health

Azure Data Explorer dashboard for Citrix infrastructure, VDA registration,
capacity, machine catalogs, delivery groups, and published resources.

## Release

- Dashboard ID: DASH-004
- Version: v0.1.0
- ADX dashboard schema: 78
- Pages: 5
- Tiles: 26
- Parameters: 6

## Pages

1. Site Overview
2. Registration & Capacity
3. Catalogs & Delivery Groups
4. VDA Diagnostics
5. Published Resources

## Data

The dashboard uses data from Citrix and uberAgent tables already ingested into
Azure Data Explorer. The public dashboard does not include customer data,
credentials, tokens, private cluster names, or private database names.

## Installation

Import the dashboard JSON from the dist folder into Azure Data Explorer.
Configure the ADX_Observability data source to point to your Azure Data
Explorer cluster and database.

## Query library

Reusable KQL is included under:

queries/citrix-infrastructure-site-health/

## Important

This is a community-driven dashboard package. Validate the queries and
visualizations against your own ADX schema and data before production use.