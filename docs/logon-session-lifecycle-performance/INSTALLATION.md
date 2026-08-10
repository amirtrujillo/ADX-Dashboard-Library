# Installation

1. Download dist/Logon & Session Lifecycle Performance.adx.json.
2. Import it into Azure Data Explorer Dashboards.
3. Edit the ADX_Observability data source.
4. Replace the sample cluster URI and database with your environment.
5. Save the dashboard.
6. Select a time range.
7. Validate the User, Host, and Session parameters.
8. Review the four dashboard pages.

The dashboard is designed to tolerate valid no-data conditions for logon,
Group Policy, and logoff tables when those uberAgent datasets are not enabled
or have no events in the selected time range.
