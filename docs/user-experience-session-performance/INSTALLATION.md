# Installation

## Prerequisites

- Azure Data Explorer cluster and database
- uberAgent data ingested into the required ADX tables
- Permission to create or import Azure Data Explorer Dashboards

## Import

1. Open Azure Data Explorer Dashboards.
2. Import `dist/User Experience & Session Performance.adx.json`.
3. Open **Data sources**.
4. Update `ADX_Observability` with the target cluster and database.
5. Save the dashboard.
6. Open every page and confirm that no query errors appear.

## Default behavior

- Default lookback: 24 hours
- Experience-trend bin: 5 minutes
- User, host, session, protocol, connection, path, severity, virtual-channel,
  and configuration filters are available.
- `User=sys` is excluded from the selected-session experience trend.

## Schema

The dashboard uses Azure Data Explorer Dashboard Schema 78.
