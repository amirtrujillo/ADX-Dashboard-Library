# Browser & Web Experience — Architecture

**Dashboard:** DASH-010 — Browser & Web Experience  
**Release:** v0.1.2  
**ADX dashboard schema:** 78

This dashboard visualizes browser and website experience telemetry in Azure Data Explorer.

## Dashboard structure

- 4 pages
- 20 tiles
- 6 parameters
- 25 query definitions
- 12 website cross-filter source tiles

### Pages

1. Overview
2. Page Load & Requests
3. Usage & Foreground
4. Resource & Investigation

### Parameters

- Time Range
- Browser
- Website
- Host
- User
- Request Type

The Website parameter is global. Website-bearing tiles use cross-filter interactions to update that parameter so a selected website can drive analysis across the dashboard.

## Primary ADX tables

- `Application_BrowserWebRequests2`
- `Application_BrowserPerformanceChrome`
- `Application_BrowserPerformanceIE`
- `Session_SessionDetail`

## Data source

The public dashboard contains placeholders:

- Cluster: `https://your-cluster.your-region.kusto.windows.net/`
- Database: `your-database`

Replace them with your Azure Data Explorer cluster and database after import.
