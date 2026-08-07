# Architecture

## Data flow

EUC endpoints -> uberAgent -> Azure Event Hubs -> Azure Data Explorer ->
KQL queries and Azure Data Explorer Dashboards

## Data model

The dashboard uses `Session_SessionDetail` as the primary session telemetry
source. Session configuration and virtual-channel information are correlated
with `CitrixSession_SessionConfig` and
`CitrixSession_VirtualChannelDetail`.

Applications and processes running in a selected session are resolved through
`Process_ProcessDetail` and `Application_AppNameIdMapping`.

## Correlation approach

- Preferred session key: `SessionGUID`
- Fallback session key: `Host + SessionID`
- Process correlation: `Host + SessionID + bounded time range`
- Application resolution: `Host + AppId + bounded time range`

Timestamp alone is not used as a correlation key.

## Dashboard pages

1. User & Session Overview
2. Session Performance
3. User Experience
4. Protocol, Configuration & Virtual Channels
5. User & Session Detail
6. Selected Session Applications

## Performance principles

- Apply time filters before joins.
- Reduce mapping data with `arg_max`.
- Aggregate process samples before application totals.
- Keep session and application correlations bounded by time.
- Treat valid no-data conditions explicitly.
