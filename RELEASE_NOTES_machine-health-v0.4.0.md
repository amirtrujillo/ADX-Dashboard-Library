# Machine Health Dashboard v0.4.0

## Overview

The first public release of the Machine Health dashboard for Azure Data Explorer.

## Included capabilities

- Environment Health and Machine Detail pages.
- Machine inventory and observability coverage.
- uberAgent heartbeat and missing-agent analysis.
- CPU, RAM, Disk, Network, and IOPS performance views.
- Dynamic Selected Metric Usage Trend.
- Hardware-model and operating-system inventory.
- Storage capacity and used-space analysis.
- Uptime, boot-duration, and GPU utilization.
- Host and hardware-model cross-filtering.
- Drillthrough to Machine Detail.
- Drag-to-filter time-range interactions.

## Technical summary

- ADX dashboard schema: 78
- Pages: 2
- Tiles: 23
- Parameters: 13
- Query objects: 35
- Fallback refresh: 5 minutes
- Minimum refresh: 1 minute

## Installation

Download and import `Machine Health.adx.json` into Azure Data Explorer Dashboards.
Map the dashboard data source to the target ADX cluster and database when required.

## License

Released under The Unlicense as a contribution to the observability and EUC community.
