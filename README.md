# uberAgent Azure Data Explorer Dashboards

Community-built Azure Data Explorer dashboards for observability data collected
by uberAgent. The project provides importable ADX dashboard JSON files and the
KQL behind each tile and parameter.

> This is an independent community project. It is not maintained by Citrix or
> Microsoft. Vendor support teams are not responsible for repository-specific
> issues, installation questions, or custom dashboard behavior.

## 🏆 Project goal

The goal is to make selected uberAgent observability use cases available directly
in Azure Data Explorer without requiring Splunk or a separate visualization
platform.

The dashboards are intentionally use-case focused. They are designed as practical
starting points that organizations can deploy, study, and adapt to their own ADX
schemas and operational requirements.

## 💡 Available use cases

### 🖥️ Machine Health

The Machine Health dashboard provides two connected pages:

- **Environment Health** — inventory, observability coverage, agent heartbeat,
  CPU, RAM, disk, network, IOPS, hardware models, operating systems, storage,
  uptime, boot duration, GPU usage, and missing-agent visibility.
- **Machine Detail** — host-specific inventory, agent status, performance,
  selected-metric trends, storage, and missing-agent details.

The dashboard supports:

- CPU, RAM, Disk, Network, and IOPS metric selection.
- Host and hardware-model filters.
- Cross-filter interactions.
- Drillthrough from environment views to Machine Detail.
- Drag-to-filter time-range interactions.
- Five-minute fallback refresh and one-minute minimum refresh.

Current release: **Machine Health v0.4.0**, ADX dashboard schema **78**.

## 📁 Repository structure

```text
ADX-Dashboard-Library/
├── .github/
│   └── workflows/
│       └── build-adx-dashboards.yml
├── dist/
│   ├── Machine Health.adx.json
│   └── README.md
├── queries/
│   └── machine-health/
│       ├── tiles/
│       ├── parameters/
│       └── README.md
├── screenshots/
│   └── README.md
├── scripts/
│   ├── build_dist.py
│   ├── package_release.py
│   └── validate_adx_dashboard.py
├── source/
│   ├── adx/
│   │   └── Machine Health.adx.json
│   └── README.md
├── .gitignore
├── CONTRIBUTING.md
├── LICENSE
├── README.md
└── mapping.json
```

The structure follows a source-to-distribution model:

1. `source/adx` contains the canonical dashboard JSON.
2. GitHub Actions validates the source.
3. `scripts/build_dist.py` generates `dist` and extracts KQL into `queries`.
4. `dist` contains the JSON users import into ADX.
5. Stable versions are published through GitHub Releases.

## ⚙️ Installation

### Requirements

<details>
<summary>Click to expand</summary>

- An Azure subscription.
- An Azure Data Explorer cluster and database.
- uberAgent data ingested into ADX, commonly through Azure Event Hubs.
- Permission to query the required ADX tables.
- Permission to create or import Azure Data Explorer dashboards.
- Table and field compatibility with the queries included in this repository.

The current Machine Health dashboard references these tables:

```text
Application_Errors
License_LicenseInfo
OnOffTransition_BootDetail2
Process_ProcessStatistics
Session_SessionDetail
System_GpuUsage
System_MachineInventory
System_SystemPerformanceSummary2
System_VolumeInventory
```

</details>

### uberAgent and ADX ingestion

Configure uberAgent, Azure Event Hubs, and Azure Data Explorer by following the
current uberAgent backend documentation:

https://docs.citrix.com/en-us/uberagent/8-x/installation/backend/configuring-microsoft-azure-data-explorer-adx-event-hubs.html

### Dashboard installation

1. Download `dist/Machine Health.adx.json` or the latest GitHub Release asset.
2. Open Azure Data Explorer.
3. Go to **Dashboards**.
4. Create a new dashboard by importing the JSON file.
5. Map or update the dashboard data source to your ADX cluster and database.
6. Confirm that the **Environment Health** and **Machine Detail** pages load.
7. Test CPU, RAM, Disk, Network, and IOPS from the **Metric** parameter.
8. Test one Host drillthrough to **Machine Detail**.

Microsoft dashboard documentation:

https://learn.microsoft.com/en-us/azure/data-explorer/azure-data-explorer-dashboards

Microsoft parameter, cross-filter, and drillthrough documentation:

https://learn.microsoft.com/en-us/azure/data-explorer/dashboard-parameters

## 🧰 Development workflow

Do not edit JSON files in `dist` directly.

1. Export the accepted dashboard JSON from Azure Data Explorer.
2. Replace the matching JSON under `source/adx`.
3. Update `mapping.json` only when the dashboard name, version, or output path changes.
4. Run:

```bash
python scripts/build_dist.py
python scripts/validate_adx_dashboard.py source/adx dist
```

5. Review the generated `dist` and `queries` files.
6. Commit the source and generated outputs.
7. Open a pull request.

## 🚧 Limitations

- The dashboards cover selected use cases, not every metric collected by uberAgent.
- Compatibility depends on the tables and fields available in the target ADX schema.
- The included JSON retains the data-source definition from the validated lab
  environment; importers must map it to their own cluster and database.
- Some tiles can show no rows when the selected time range contains no matching data.
- Thresholds are operational defaults and should be reviewed for each environment.
- The project does not replace vendor-supported uberAgent dashboards or support services.

## 🗺️ Roadmap

- Add real dashboard screenshots.
- Add session performance and user-experience dashboards.
- Add application performance dashboards.
- Add Citrix infrastructure and site-health dashboards.
- Add automated schema compatibility checks.
- Generalize ADX data-source remapping during build and import.
- Package all stable dashboards through GitHub Releases.

## 🤝 Contributing

Read `CONTRIBUTING.md` before opening an issue or pull request.

## 📜 License

This project is released under **The Unlicense**.

The source code, KQL queries, dashboard definitions, scripts, and documentation
are dedicated to the public domain to the greatest extent permitted by law.
They may be used, copied, modified, published, distributed, and incorporated
into commercial or non-commercial projects without requesting permission.

This repository is provided as a contribution to the observability and EUC
community. See `LICENSE` for the complete terms.

## 🙏 Acknowledgements

The source, distribution, screenshots, scripts, mapping, and GitHub Actions
organization was inspired by Dominik Britz's community repository:

https://github.com/DominikBritz/uberAgent-grafana-dashboards

This project adapts that pattern for native Azure Data Explorer dashboards and
an ADX-only KQL workflow.
