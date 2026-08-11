# uberAgent Azure Data Explorer Dashboards

Community-built Azure Data Explorer dashboards for observability data collected
by uberAgent. The project provides importable ADX dashboard JSON files and the
KQL behind each tile and parameter.

> This is an independent community project. It is not maintained by Citrix or
> Microsoft. Vendor support teams are not responsible for repository-specific
> issues, installation questions, or custom dashboard behavior.

## Project goal

The goal is to make selected uberAgent observability use cases available
directly in Azure Data Explorer without requiring Splunk or a separate
visualization platform.

The dashboards are intentionally use-case focused. They are practical starting
points that organizations can deploy, study, and adapt to their own ADX schemas
and operational requirements.

## Available dashboards

### Machine Health
- Environment inventory and observability coverage
- Agent heartbeat and missing-agent visibility
- CPU, RAM, disk, network, IOPS, storage, uptime, boot, and GPU analysis
- Machine-specific drillthrough and detail
Current release: **Machine Health v0.4.0**, Schema **78**.

### Application Performance
- Application usage and process resource consumption
- CPU, memory, IOPS, and network rankings
- Stability, errors, UI responsiveness, and input delay
- Startup and network-target performance
- Selected-application detail
Current release: **Application Performance v0.1.1**, Schema **78**.
See `README-APPLICATION-PERFORMANCE.md`.

### User Experience & Session Performance
- Session inventory, concurrency, state, protocol, and transport
- Session CPU, memory, IOPS, network, and process performance
- RTT, protocol latency, input delay, FPS, reconnects, and EDT quality
- Experience score and severity
- Citrix session configuration and virtual channels
- User/session detail and application drill through
See `README-USER-EXPERIENCE-SESSION-PERFORMANCE.md`

### Citrix Infrastructure & Site Health
- Citrix Site overview
- Machine Catalogs, Delivery Groups, Published Apps and Desktops
- VDA Diagnostic, Current sessions and VDA version distribution
- Registration and Capacity
- Published Resources: Desktop assignment, Resource Tag
See `README-CITRIX-INFRASTRUCTURE-SITE-HEALTH.md`

### Logon & Session Lifecycle Performance
- Logon Overview, Duration Overtime
- Logon details by Session
- Logon details by Host
- Group Policy Logon Details by Session
- Session Connection State Distribution
See `README-LOGON-SESSION-LIFECYCLE-PERFORMANCE.md`

### ICA HDX Network Experience
- Protocol and HDX overview
- Latency and Transport
- Reliability and Packet loss
- Virtual channels and configuration
See `README-ICA-HDX-NETWORK-EXPERIENCE.md`

## Repository structure

~~~text
ADX-Dashboard-Library/
├── .github/
├── dist/
├── docs/
│   ├── application-performance/
│   ├── citrix-infrastructure-site-health/
│   ├── ica-hdx-network-experience/
│   ├── logon-session-lifecycle-performance/
│   ├── user-experience-session-performance/
│   └── vda-load-capacity-availability/
├── queries/
│   ├── application-performance/
│   │   ├── parameters/
│   │   └── tiles/
│   ├── citrix-infrastructure-site-health/
│   │   ├── parameters/
│   │   └── tiles/
│   ├── ica-hdx-network-experience/
│   │   ├── parameters/
│   │   └── tiles/
│   ├── logon-session-lifecycle-performance/
│   │   ├── parameters/
│   │   └── tiles/
│   ├── machine-health/
│   │   ├── parameters/
│   │   └── tiles/
│   ├── user-experience-session-performance/
│   │   ├── parameters/
│   │   └── tiles/
│   └── vda-load-capacity-availability/
│       ├── parameters/
│       └── tiles/
├── Readme/
│   ├── README-APPLICATION-PERFORMANCE.md
│   ├── README-CITRIX-INFRASTRUCTURE-SITE-HEALTH.md
│   ├── README-ICA-HDX-NETWORK-EXPERIENCE.md
│   ├── README-LOGON-SESSION-LIFECYCLE-PERFORMANCE.md
│   ├── README-USER-EXPERIENCE-SESSION-PERFORMANCE.md
│   └── README-VDA-LOAD-CAPACITY-AVAILABILITY.md
├── release-notes/
├── screenshots/
│   ├── application-performance/
│   ├── citrix-infrastructure-site-health/
│   ├── ica-hdx-network-experience/
│   ├── logon-session-lifecycle-performance/
│   ├── user-experience-session-performance/
│   └── vda-load-capacity-availability/
├── scripts/
├── source/
│   └── adx/
├── .gitattributes
├── .gitignore
├── CONTRIBUTING.md
├── LICENSE
├── mapping.json
└── README.md
~~~

The repository follows a source-to-distribution model:

1. source/adx contains canonical dashboard JSON.
2. Validation checks source structure and KQL.
3. dist contains import-ready dashboard JSON.
4. queries contains reusable parameter and tile KQL organized by dashboard.
5. Readme contains dashboard-specific README files.
6. docs, screenshots, and elease-notes are organized by use case.
## Installation

1. Download the stable dashboard JSON from `dist`.
2. Open Azure Data Explorer Dashboards.
3. Import the JSON as a new dashboard.
4. Open **Data sources**.
5. Map `ADX_Observability` to the target cluster and database.
6. Save and validate every page and parameter.

## Development workflow

Do not edit JSON files in `dist` directly.

1. Export the accepted dashboard from Azure Data Explorer.
2. Place the canonical JSON under `source/adx`.
3. Review the matching `dist` and `queries` outputs.
4. Run repository validation.
5. Review public/private separation.
6. Commit the source and generated outputs.

## Limitations

- Dashboards cover selected use cases, not every uberAgent metric.
- Compatibility depends on the tables and fields available in the target schema.
- Some tiles can return valid no-data states.
- Operational thresholds should be reviewed for each environment.
- The project does not replace vendor-supported dashboards or support services.

## Roadmap

- Add sanitized dashboard screenshots.
- Add Citrix VDA and site-health dashboards.
- Add ICA/HDX and network-experience dashboards.
- Add endpoint inventory, compliance, security, and browser dashboards.
- Expand automated schema and publication validation.

## Contributing

Read `CONTRIBUTING.md` before opening an issue or pull request.

## License

This project is released under **The Unlicense**.


