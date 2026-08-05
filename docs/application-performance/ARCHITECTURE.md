# Architecture

## Data flow

EUC endpoints → uberAgent → Azure Event Hubs → Azure Data Explorer →
KQL queries and Azure Data Explorer Dashboards

## Data model

Application names are resolved by correlating `AppId` and `Host` with
`Application_AppNameIdMapping`. When a friendly name is not available,
process-name fallback is used where appropriate.

Process resource data is aggregated by process instance and time bucket before
being summarized by application. This avoids treating raw samples as separate
simultaneous processes.

## Correlation approach

- Application: `Host + AppId + bounded time range`
- Session: `Host + SessionID + bounded time range`
- Process: prefer `ProcGUID`; otherwise use `Host + ProcID + bounded time range`
- Network: `Host + Process + Target + bounded time range`

Timestamp alone is never treated as a correlation key.

## Performance principles

- Apply the time filter before joins.
- Reduce mapping tables using `arg_max`.
- Use bounded dashboard time ranges.
- Keep Top N configurable.
- Aggregate process samples before application totals.
