# Extracted KQL — Machine Health

These files are generated from the canonical dashboard JSON.
Do not edit them directly. Edit the dashboard in `source/adx` and run
`python scripts/build_dist.py`.

## Tile queries

- `01_Environment_Health__01_Machine_Inventory_Overview.kql` — Environment Health / Machine Inventory Overview
- `01_Environment_Health__02_Host_Observability_Coverage.kql` — Environment Health / Host Observability Coverage
- `01_Environment_Health__03_Agent_Heartbeat_Status.kql` — Environment Health / Agent Heartbeat Status
- `01_Environment_Health__04_Machine_Performance_Summary.kql` — Environment Health / Machine Performance Summary
- `01_Environment_Health__05_Machine_Performance_by_Host.kql` — Environment Health / Machine Performance by Host
- `01_Environment_Health__06_Selected_Metric_Usage_Trend.kql` — Environment Health / Selected Metric Usage Trend
- `01_Environment_Health__07_Performance_by_Hardware_Model.kql` — Environment Health / Performance by Hardware Model
- `01_Environment_Health__08_Top_Hardware_Models.kql` — Environment Health / Top Hardware Models
- `01_Environment_Health__09_Operating_System_Inventory.kql` — Environment Health / Operating System Inventory
- `01_Environment_Health__10_Storage_Inventory_Summary.kql` — Environment Health / Storage Inventory Summary
- `01_Environment_Health__11_Drives_with_the_Least_Free_Space.kql` — Environment Health / Drives with the Least Free Space
- `01_Environment_Health__12_Drives_by_Used_Space_Percentage.kql` — Environment Health / Drives by Used-Space Percentage
- `01_Environment_Health__13_Machine_Uptime_Summary.kql` — Environment Health / Machine Uptime Summary
- `01_Environment_Health__14_Boot_Duration_Summary.kql` — Environment Health / Boot Duration Summary
- `01_Environment_Health__15_GPU_Utilization_by_Adapter.kql` — Environment Health / GPU Utilization by Adapter
- `01_Environment_Health__16_Missing_Agents.kql` — Environment Health / Missing Agents
- `02_Machine_Detail__17_Selected_Machine_Inventory.kql` — Machine Detail / Selected Machine Inventory
- `02_Machine_Detail__18_Selected_Machine_Agent_Status.kql` — Machine Detail / Selected Machine Agent Status
- `02_Machine_Detail__19_Selected_Machine_Performance_Summary.kql` — Machine Detail / Selected Machine Performance Summary
- `02_Machine_Detail__20_Selected_Machine_Performance.kql` — Machine Detail / Selected Machine Performance
- `02_Machine_Detail__21_Selected_Machine_Storage_Summary.kql` — Machine Detail / Selected Machine Storage Summary
- `02_Machine_Detail__22_Selected_Machine_Agent_Details.kql` — Machine Detail / Selected Machine Agent Details
- `02_Machine_Detail__23_Selected_Metric_Usage_Trend.kql` — Machine Detail / Selected Metric Usage Trend

## Parameter queries

- `02_Host.kql` — Host
- `03_OS_platform.kql` — OS platform
- `04_OS_name.kql` — OS name
- `05_OS_version.kql` — OS version
- `06_Hardware_model.kql` — Hardware model
- `07_Metric.kql` — Metric
- `08_Time_bin.kql` — Time bin
- `09_Healthy_threshold.kql` — Healthy threshold
- `10_Warning_threshold.kql` — Warning threshold
- `11_Missing_threshold.kql` — Missing threshold
- `12_Inventory_lookback.kql` — Inventory lookback
- `13_Minimum_volume_size_MB.kql` — Minimum volume size (MB)
