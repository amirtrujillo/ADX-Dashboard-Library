# Architecture

DASH-006 visualizes ICA/HDX and network telemetry stored in Azure Data
Explorer.

Data flow:

EUC/Citrix endpoints -> uberAgent / Citrix telemetry -> Azure ingestion ->
Azure Data Explorer -> KQL -> ADX dashboard

The dashboard is organized into four pages:

1. Protocol & HDX Overview
2. Latency & Transport
3. Reliability & Packet Loss
4. Virtual Channels & Configuration

The dashboard contains 18 validated tiles and six global parameters.

The public JSON preserves the visual types, layouts, and visual options from
the canonical ADX export created after functional validation.
