# Architecture

## Data flow

EUC / Citrix environment -> uberAgent and Citrix data -> ingestion pipeline ->
Azure Data Explorer -> KQL -> ADX Dashboard

## Dashboard scope

DASH-004 focuses on Citrix infrastructure and site health:

- site-level infrastructure overview;
- VDA registration and availability;
- machine catalogs;
- delivery groups;
- VDA diagnostics;
- published applications and desktops;
- registration and capacity trends.

Generic endpoint CPU, memory, disk, network, and IOPS analysis is intentionally
kept outside this dashboard so it does not duplicate Machine Health.