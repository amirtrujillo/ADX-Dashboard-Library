# Application Performance v0.1.1

Release date: 2026-08-05

## Added

- Five-page Application Performance dashboard
- Application usage and environment overview
- CPU, memory, IOPS, and network analysis
- Application crash and hang analysis
- UI unresponsiveness and input-delay analysis
- Startup-duration and startup-I/O analysis
- Network-target latency, traffic, jitter, and retransmit analysis
- Selected-application detail page
- Eight global parameters
- Application cross-filtering and drillthrough
- Explicit no-data handling

## Validation

- 29 functional KQL queries accepted
- 2 expected no-data cases accepted
- Schema 78 import completed successfully
- Query-reference IDs made unique for all tiles and parameters

## Known limitations

- Faulting-module data depends on event-field availability.
- Network-connection failures display `No data` when the source table is empty.
- Thresholds and severity rules are not enabled in this initial release.
