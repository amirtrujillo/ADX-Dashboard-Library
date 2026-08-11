# Endpoint Inventory & Compliance — Architecture

DASH-008 is an Azure Data Explorer dashboard for endpoint inventory and
evidence-backed compliance visibility.

## Data domains

The dashboard uses current ADX schema evidence from:

- System_MachineInventory
- System_MonitorInventory
- System_NetworkConfigInformation
- System_VolumeInventory
- System_DiskInventory
- Application_ApplicationInventory
- Application_SoftwareUpdateInventory

## Dashboard structure

- 4 pages
- 15 tiles
- 6 parameters
- 20 query definitions
- Schema 78

The public release uses a sanitized manual Kusto data source. Replace the
cluster and database placeholders after import.