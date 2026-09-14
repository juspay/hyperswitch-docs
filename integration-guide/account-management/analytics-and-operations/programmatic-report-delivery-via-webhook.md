---
icon: database
---

<!-- truth manifest; hyperswitch e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0; spec api-reference/v1/openapi_spec_v1.json@e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0
     symbols: report endpoint paths = verified zero in api-reference/v1/openapi_spec_v1.json paths
     symbols: report request, response, and webhook schemas = verified zero in api-reference/v1/openapi_spec_v1.json components.schemas
     checked: 2026-09-14 -->

# Programmatic report delivery via webhook

### Overview

The public v1 API specification does not currently define a programmatic report endpoint, its request fields, or its webhook payload. This page therefore does not publish an integration contract or sample payload.

Do not build against examples that previously appeared here. They included endpoint paths and payload fields that cannot be checked against the public API contract at the pinned source version.

### Before you integrate

Ask the Hyperswitch team for the published report API and webhook contract. Confirm that the contract defines all of the following before implementation:

* endpoint path and authentication
* request and response schemas
* completion and failure event wire values
* webhook payload fields and report-type values
* download URL lifetime
* signature header and signing procedure
