# Application Performance — Azure Data Explorer Dashboard

Application Performance is a reusable Azure Data Explorer Dashboard for
observability teams using uberAgent telemetry in Azure Data Explorer.

The dashboard consolidates application usage, process resource consumption,
application stability, UI responsiveness, input delay, startup performance,
and network-target performance into one Schema 78 dashboard.

## Release

- Version: `v0.1.1`
- Dashboard schema: `78`
- Pages: `5`
- Tiles: `35`
- Global parameters: `8`
- Status: Public release candidate pending final functional acceptance

## Dashboard pages

1. **Application Overview**
   - Environment summary
   - Application usage
   - Top applications by CPU, memory, IOPS, and network
   - Resource trend

2. **Resource Performance**
   - Application resource summary
   - CPU, memory, IOPS, and network rankings
   - Selected metric trend

3. **Stability & Responsiveness**
   - Crashes and hangs
   - Error trends
   - UI unresponsiveness
   - Input delay
   - Faulting modules

4. **Startup & Network**
   - Startup KPIs and trends
   - Network-target latency and traffic
   - Connection-failure summary

5. **Application Detail**
   - Selected application health
   - Usage, resource, stability, and startup details

## Global parameters

- Time range
- Host
- User
- Application
- Process
- Metric
- Time bin
- Top N

## Required ADX tables

- `Application_AppNameIdMapping`
- `Application_Errors`
- `Application_NetworkConnectFailure`
- `Application_UIDelay`
- `Process_NetworkTargetPerformance`
- `Process_ProcessDetail`
- `Process_ProcessStartup`
- `Process_ProcessStatistics`
- `Session_SessionDetail`

## Installation

1. Download `dist/Application Performance.adx.json`.
2. Open Azure Data Explorer Dashboards.
3. Import the JSON as a new dashboard.
4. Edit the `ADX_Observability` data source for your cluster and database.
5. Validate all parameters and pages.

The included JSON uses the project lab source as an example:

- Cluster: `https://your-cluster.your-region.kusto.windows.net/`
- Database: `your-database`

Replace those values for other environments.

## Expected no-data states

`Application_NetworkConnectFailure` may have no current rows. The dashboard
returns an explicit `No data` status instead of failing.

`Faulting Module Details` may also be empty when the source events do not
contain faulting-module information.

## Repository contents

- `dist/` — compact import-ready dashboard JSON
- `source/adx/` — formatted dashboard source JSON
- `queries/application-performance/parameters/` — parameter queries
- `queries/application-performance/tiles/` — dashboard tile queries
- `docs/application-performance/` — architecture, installation, and validation
- `screenshots/application-performance/` — dashboard screenshots
- `release-notes/` — version history

## Support statement

This is a community-driven project. It is not maintained or supported by
Citrix. Do not contact Citrix Support for requests or issues related to this
dashboard.

## Security

The public package excludes Splunk XML, raw ADX exports, credentials, tokens,
connection strings, private samples, and local Knowledge Base files.
