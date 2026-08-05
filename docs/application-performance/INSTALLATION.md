# Installation

## Prerequisites

- Azure Data Explorer cluster and database
- uberAgent data ingested into the required tables
- Permission to create or import Azure Data Explorer Dashboards

## Import

1. Open Azure Data Explorer Dashboards.
2. Import `dist/Application Performance.adx.json`.
3. Open **Data sources**.
4. Update `ADX_Observability` with the target cluster and database.
5. Save the dashboard.
6. Open each page and validate that no query errors appear.

## Default behavior

- Default lookback: 24 hours
- Default time bin: 5 minutes
- Default Top N: configurable from the dashboard

## Schema

The dashboard uses Azure Data Explorer Dashboard Schema 78.
