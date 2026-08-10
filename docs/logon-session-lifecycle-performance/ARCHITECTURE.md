# Logon & Session Lifecycle Performance — Architecture

## Purpose

This Azure Data Explorer dashboard provides observability for user logon and
session lifecycle behavior using uberAgent data stored in ADX.

## Dashboard structure

- Logon Overview
- Group Policy
- Session Lifecycle
- Logoff

## Parameters

- Time range
- User
- Host
- Session

## Data source

The public dashboard uses the portable data source name ADX_Observability.

Update the data source after import:

- Cluster: your Azure Data Explorer cluster
- Database: your database containing the required uberAgent tables

## Schema

Azure Data Explorer Dashboard Schema 78.
