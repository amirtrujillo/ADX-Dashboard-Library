# User Experience & Session Performance v0.1.6

Release date: 2026-08-06

## Added

- Six-page User Experience & Session Performance dashboard
- Session inventory and concurrent-session analysis
- CPU, memory, IOPS, network, and process performance
- RTT, protocol latency, input delay, FPS, reconnect, and EDT analysis
- Experience score and severity
- Citrix session configuration and virtual-channel analysis
- Unified user and session detail
- Drillthrough to applications running in the selected session
- Explicit valid no-data handling
- Ten query-backed parameters and 42 tile queries

## Final changes

- User=sys is excluded from Selected Session Experience Trend.
- Unified User and Session Detail displays the selected session or latest match.
- Selected Session Experience Trend drills through to session applications.
- Sessions with no detected issue are classified Healthy.

## Validation

- Schema 78 import completed successfully
- Six pages and 42 tiles validated
- Fifty-two query definitions validated
- No duplicate query references
- No tile overlaps
- No remaining query errors

## Known limitations

- Process and application detail depends on matching Host + SessionID rows
  inside the selected time range.
- Session configuration and virtual-channel tiles can show valid no-data
  results when those sources are not populated.
- Operational thresholds should be reviewed for each environment.
