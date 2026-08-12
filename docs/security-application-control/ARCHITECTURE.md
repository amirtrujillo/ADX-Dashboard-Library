# Security & Application Control — Architecture

DASH-009 is an Azure Data Explorer dashboard for endpoint security and
application-control observability.

## Evidence-backed data sources

The dashboard intentionally uses only the ADX tables that were validated during
development:

- `ActivityMonitoring_ProcessTagging`
- `System_SecurityInventory`

The dashboard does not require a cross-table join.

## Functional areas

The four pages are:

1. Security Overview
2. Process Risk & Tagging
3. Security Inventory
4. Investigation Detail

The dashboard includes 15 tiles, one duration parameter, and five query-backed
parameters.

## Security scope boundary

This release does not claim AppLocker-specific coverage. AppLocker event IDs,
rule enforcement modes, allow/deny semantics, publisher/hash/signature
interpretation, threat classification, and custom severity mappings are not
included unless supported by explicit telemetry.

Values such as process risk and security-inventory scores are displayed as
collected. The dashboard does not invent additional severity semantics.