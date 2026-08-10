# Validation

DASH-004 v0.1.0 was functionally validated in Azure Data Explorer before the
canonical dashboard export was prepared for public sanitization.

Validated structure:

- Schema version: 78
- Pages: 5
- Tiles: 26
- Parameters: 6
- Query definitions: 31

Functional validation covered:

- Site Overview
- Registration & Capacity
- Catalogs & Delivery Groups
- VDA Diagnostics
- Published Resources

Specific validated changes include:

- unique query IDs for every query reference;
- Machine Catalog Registration % visualization;
- Delivery Group Registration % visualization;
- Maintenance mode displayed as Off / On;
- VDA Power State Distribution using time on the X-axis and VDA quantity on
  the Y-axis.

Public releases must still be validated against the target environment because
table population and Citrix configuration differ between deployments.