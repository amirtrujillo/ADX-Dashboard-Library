# User Experience & Session Performance — Azure Data Explorer Dashboard

User Experience & Session Performance is a reusable Azure Data Explorer dashboard
for observability teams using uberAgent telemetry in Azure Data Explorer.

The dashboard consolidates session inventory, resource consumption, Citrix HDX
experience, protocol details, session configuration, virtual channels, process
activity, and running applications into one Schema 78 dashboard.

## Release

- Version: `v0.1.6`
- Dashboard schema: `78`
- Pages: `6`
- Tiles: `42`
- Global parameters: `11`
- Query definitions: `52`
- Status: Public release candidate

## Dashboard pages

1. **User & Session Overview**
   - Users, hosts, sessions, concurrency, connection states, protocols, and transport.

2. **Session Performance**
   - CPU, memory, IOPS, network, process count, trends, and session inventory.

3. **User Experience**
   - RTT, protocol latency, input delay, FPS, reconnects, EDT quality,
     experience score, and severity.

4. **Protocol, Configuration & Virtual Channels**
   - Session reliability, graphics, Thinwire, client redirection, and
     virtual-channel activity.

5. **User & Session Detail**
   - Selected-session experience, configuration, virtual channels, processes,
     UI delay, and foreground application.

6. **Selected Session Applications**
   - Applications and processes running in the selected user session.

## Global parameters

- Time range
- User
- Host
- Session
- Resource metric
- Time bin
- Connection path
- Experience metric
- Severity
- Virtual channel
- Configuration category

## Required ADX tables

- `Session_SessionDetail`
- `Process_ProcessDetail`
- `Process_ProcessStatistics`
- `Application_AppNameIdMapping`
- `Application_UIDelay`
- `CitrixSession_SessionConfig`
- `CitrixSession_VirtualChannelDetail`

## Installation

1. Download `dist/User Experience & Session Performance.adx.json`.
2. Open Azure Data Explorer Dashboards.
3. Import the JSON as a new dashboard.
4. Edit the `ADX_Observability` data source.
5. Enter the target ADX cluster and database.
6. Save the dashboard and validate all six pages.

The public JSON contains generic data-source placeholders and does not expose
the development cluster or database.

## Expected no-data states

Some tiles can return a valid no-data state when the selected session or time
range has no matching processes, applications, reconnects, EDT quality events,
session configuration, or virtual channels.

## Repository contents

- `dist/` — stable and versioned import-ready dashboard JSON
- `source/adx/` — canonical dashboard JSON
- `queries/user-experience-session-performance/parameters/`
- `queries/user-experience-session-performance/tiles/`
- `docs/user-experience-session-performance/`
- `screenshots/user-experience-session-performance/`
- `release-notes/`

## Support statement

This is a community-driven project. It is not maintained or supported by Citrix
or Microsoft. Do not contact vendor support teams for requests or issues related
to this dashboard.

## Security

The public package excludes Splunk XML, raw ADX exports, credentials, tokens,
connection strings, private samples, local Knowledge Base files, validation
packages, usernames, hosts, session identifiers, and internal data.
