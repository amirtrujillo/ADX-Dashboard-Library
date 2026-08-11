# ICA/HDX Network Experience

Azure Data Explorer dashboard for Citrix ICA/HDX network observability.

## Release

- Dashboard ID: DASH-006
- Version: v0.1.0
- ADX dashboard schema: 78
- Pages: 4
- Tiles: 18
- Parameters: 6

## Scope

The dashboard provides visibility into ICA/HDX protocol experience, TCP
latency and jitter, network reliability, retransmissions and packet loss,
session network details, virtual channel usage, and HDX/session configuration.

## Dashboard pages

1. Protocol & HDX Overview
2. Latency & Transport
3. Reliability & Packet Loss
4. Virtual Channels & Configuration

## Parameters

- Time range
- User
- Host
- Session
- Target
- Virtual channel

The public dashboard uses a placeholder Azure Data Explorer cluster and
database. Configure the data source after import.

This release is based on the canonical dashboard exported from Azure Data
Explorer after functional validation. Visual changes made during validation
are therefore preserved in the public release.
