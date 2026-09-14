---
icon: database
---

<!-- truth manifest; hyperswitch e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0
     symbols: POST /analytics/v1/merchant/report/{dispute,refunds,payments,payouts,authentications} = crates/router/src/analytics.rs:236-321
     symbols: POST /analytics/v1/org/report/{dispute,refunds,payments,payouts,authentications} = crates/router/src/analytics.rs:323-395
     symbols: POST /analytics/v1/profile/report/{dispute,refunds,payments,payouts,authentications} = crates/router/src/analytics.rs:397-506
     symbols: ReportRequest, timeRange, emails, returnUrl, columns, reportType (v2 only) = crates/api_models/src/analytics.rs:148-159
     symbols: TimeRange, startTime, endTime = crates/common_utils/src/types.rs:774-787
     symbols: HTTPS returnUrl validation = crates/router/src/analytics_validator.rs:26-32
     symbols: payment_response_hash_key fetch and handoff for merchant reports = crates/router/src/analytics.rs:3062-3081
     symbols: payment_response_hash_key fetch and handoff for profile reports = crates/router/src/analytics.rs:3262-3281
     symbols: HMAC-SHA512, X-Webhook-Signature-512 = crates/router/src/core/webhooks/types.rs:44-75; crates/router/src/lib.rs:153
     symbols: organization report signing key is None = crates/router/src/analytics.rs:3164-3172
     external: report_generation.completed, status, org_id, merchant_id, data.report_type, data.start_date_utc, data.end_date_utc, data.download_url, data.expires_in_hours = report component contract; checked against in-repo boundary ReportRequest.return_url at crates/api_models/src/analytics.rs:150-158 and signing-key fetch at crates/router/src/analytics.rs:3062-3081,3262-3281
     checked: 2026-09-14 -->

# Programmatic report delivery via webhook

### Overview

Hyperswitch can generate reports asynchronously. Submit a report request with `returnUrl` to receive the completed report through a webhook instead of waiting for the file in the API response.

Report routes exist at the Merchant, Organization, and Profile levels. Merchant and Profile handlers fetch `payment_response_hash_key` when `returnUrl` is present and pass it to the report component. Organization handlers exist, but pass no signing key. Confirm the required authentication and webhook-signing behavior before using an Organization-level route for webhook delivery.

### How it works

1. Send a report request with `timeRange`, a non-empty `emails` array, and `returnUrl`.
2. The router validates an API-key request and passes it to the report component.
3. The report component generates the file and sends its completion payload to `returnUrl`.
4. Verify the webhook signature before using `data.download_url`.

The router owns the route, request validation, and signing-key handoff. The completion payload documented below is owned and emitted by the external report component.

### Supported report types

Each of the 3 route scopes exposes the same 5 report suffixes, for 15 routes in total:

| Report type | URL suffix |
| --- | --- |
| Payments | `payments` |
| Refunds | `refunds` |
| Disputes | `dispute` |
| Payouts | `payouts` |
| Authentications | `authentications` |

Use `dispute`, not `disputes`.

### Endpoints

#### Merchant-level endpoints

| Report type | Endpoint |
| --- | --- |
| Payments | `POST /analytics/v1/merchant/report/payments` |
| Refunds | `POST /analytics/v1/merchant/report/refunds` |
| Disputes | `POST /analytics/v1/merchant/report/dispute` |
| Payouts | `POST /analytics/v1/merchant/report/payouts` |
| Authentications | `POST /analytics/v1/merchant/report/authentications` |

Merchant routes accept API-key or JWT authentication.

#### Organization-level endpoints

| Report type | Endpoint |
| --- | --- |
| Payments | `POST /analytics/v1/org/report/payments` |
| Refunds | `POST /analytics/v1/org/report/refunds` |
| Disputes | `POST /analytics/v1/org/report/dispute` |
| Payouts | `POST /analytics/v1/org/report/payouts` |
| Authentications | `POST /analytics/v1/org/report/authentications` |

Organization routes use JWT authentication with `OrganizationReportRead`. Their handlers pass no `payment_response_hash_key` to the report component.

#### Profile-level endpoints

| Report type | Endpoint |
| --- | --- |
| Payments | `POST /analytics/v1/profile/report/payments` |
| Refunds | `POST /analytics/v1/profile/report/refunds` |
| Disputes | `POST /analytics/v1/profile/report/dispute` |
| Payouts | `POST /analytics/v1/profile/report/payouts` |
| Authentications | `POST /analytics/v1/profile/report/authentications` |

Profile routes accept API-key or JWT authentication. Include the profile context required by your authentication method.

### Request parameters

`ReportRequest` uses camel-case JSON field names:

| Field | Required for webhook delivery | Description |
| --- | --- | --- |
| `timeRange` | Yes | Report time range. |
| `timeRange.startTime` | Yes | ISO 8601 start time. The Rust field is `start_time` and accepts the `startTime` alias. |
| `timeRange.endTime` | No | ISO 8601 end time. The Rust field is optional and accepts the `endTime` alias. |
| `emails` | Yes for API-key requests | Non-empty array. The first address is used as the primary report address. |
| `returnUrl` | Yes | HTTPS endpoint that receives the report-component webhook. |
| `columns` | No | Optional report-column selection. |

The shared Rust type also contains `reportType`, but that field is compiled only for v2. The v1 endpoint suffix selects the report type.

For API-key requests, `validate_report_request` rejects a non-HTTPS `returnUrl`. A missing or empty `emails` array returns HTTP `400` with error code `IR_06`.

### Trigger report generation

This request generates a Merchant-level payment report. Set `HYPERSWITCH_BASE_URL` to the base URL for your environment.

```bash
curl --request POST \
  --url "${HYPERSWITCH_BASE_URL}/analytics/v1/merchant/report/payments" \
  --header 'Content-Type: application/json' \
  --header 'api-key: <api-key>' \
  --data '{
    "timeRange": {
      "startTime": "2026-06-15T00:00:00.000Z",
      "endTime": "2026-07-15T23:59:59.000Z"
    },
    "emails": ["reports@example.com"],
    "returnUrl": "https://example.com/webhooks/reports"
  }'
```

Change the scope and suffix only to a route listed above. Profile and Organization routes have different authentication context.

### Receive the completion webhook

The completion shape below comes from the external report component, not from the router's OpenAPI specification or an in-repo router response struct. The in-repo boundary confirms that the router passes `returnUrl` and, for Merchant and Profile routes, the signing key to that component.

```json
{
  "event_type": "report_generation.completed",
  "status": "success",
  "org_id": "<organization-id>",
  "merchant_id": "<merchant-id>",
  "data": {
    "report_type": "payment_report",
    "start_date_utc": "2026-06-15",
    "end_date_utc": "2026-07-15",
    "download_url": "https://example.com/reports/report.csv",
    "expires_in_hours": 48
  }
}
```

The 9 documented completion symbols are `event_type`, `status`, `org_id`, `merchant_id`, `data.report_type`, `data.start_date_utc`, `data.end_date_utc`, `data.download_url`, and `data.expires_in_hours`. Their payload contract is external to the router repository.

`data.report_type` has 5 external contract values: `payment_report`, `refund_report`, `dispute_report`, `payout_report`, and `authentication_report`.

### Verify the webhook signature

For Merchant and Profile reports, setting `returnUrl` makes the handler fetch `payment_response_hash_key` and pass it to the report component. The component uses that key for the HMAC-SHA512 signature sent in `X-Webhook-Signature-512`.

1. Read the raw request body before parsing it.
2. Read `X-Webhook-Signature-512`.
3. Generate an HMAC-SHA512 digest from the raw body with `payment_response_hash_key`.
4. Hex-encode the digest.
5. Compare the generated and received values in constant time.
6. Reject the delivery if they do not match.

Do not apply this signing procedure to an Organization-level completion webhook without confirmation. The Organization handlers pass no signing key to the report component.

### Download the report

After signature verification, download the file from `data.download_url`. The report-component payload states the lifetime in `data.expires_in_hours`. Do not log or expose the full download URL.
