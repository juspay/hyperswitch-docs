---
icon: database
---

<!-- truth manifest; hyperswitch e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0; spec api-reference/v1/openapi_spec_v1.json@e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0
     symbols: report endpoint paths = verified zero in api-reference/v1/openapi_spec_v1.json paths
     symbols: report request, response, and webhook schemas = verified zero in api-reference/v1/openapi_spec_v1.json components.schemas
     checked: 2026-09-14 -->

# Programmatic report delivery via webhook

### Overview

Hyperswitch supports asynchronous report generation. You can trigger a report with an API key and receive a webhook on the configured `returnUrl`.

This page documents the request endpoints and the verified failure webhook event. A completed-report webhook was previously documented, but its payload fields are not part of the public v1 API contract, so only the failure event is listed here.

### How it works

1. Send a report request with a time range, email address, and `returnUrl`.
2. Hyperswitch accepts the request and starts report generation.
3. If report generation fails, Hyperswitch sends a signed `report_generation.failed` webhook to your `returnUrl`.

Report generation can take a few seconds or several minutes, depending on the amount of data.

### Prerequisites

Before you begin, ensure that you have the following:

* a Hyperswitch sandbox/production API key
* at least one valid email address for the `emails` field
* a public HTTPS endpoint that can receive `POST` requests
* your Profile ID when requesting a Profile-level report

Note: You do not need to provide a Merchant ID for Merchant-level reports. Hyperswitch identifies the Merchant from the API key.

### Supported report types

You can generate the following reports:

| Report Type     | URL Suffix        |
| --------------- | ----------------- |
| Payments        | `payments`        |
| Refunds         | `refunds`         |
| Disputes        | `dispute`         |
| Payouts         | `payouts`         |
| Authentications | `authentications` |

> Note: Use `dispute` in the endpoint URL, not `disputes`. Authentications is only supported in sandbox.

### Sandbox endpoints

#### Merchant-level endpoints

Use these endpoints to generate a report for the Merchant associated with your API key.

| Report Type     | Endpoint                                                                      |
| --------------- | ----------------------------------------------------------------------------- |
| Payments        | `https://app.hyperswitch.io/api/analytics/v1/merchant/report/payments`        |
| Refunds         | `https://app.hyperswitch.io/api/analytics/v1/merchant/report/refunds`         |
| Disputes        | `https://app.hyperswitch.io/api/analytics/v1/merchant/report/dispute`         |
| Payouts         | `https://app.hyperswitch.io/api/analytics/v1/merchant/report/payouts`         |
| Authentications | `https://app.hyperswitch.io/api/analytics/v1/merchant/report/authentications` |

The API key identifies the Merchant. You do not need to pass a Merchant ID in the endpoint or request body.

#### Profile-level endpoints

Use these endpoints with the `X-Profile-Id` header to generate a report for a specific Profile.

| Report Type     | Endpoint                                                                     |
| --------------- | ---------------------------------------------------------------------------- |
| Payments        | `https://app.hyperswitch.io/api/analytics/v1/profile/report/payments`        |
| Refunds         | `https://app.hyperswitch.io/api/analytics/v1/profile/report/refunds`         |
| Disputes        | `https://app.hyperswitch.io/api/analytics/v1/profile/report/dispute`         |
| Payouts         | `https://app.hyperswitch.io/api/analytics/v1/profile/report/payouts`         |
| Authentications | `https://app.hyperswitch.io/api/analytics/v1/profile/report/authentications` |

#### Production endpoints

Contact the Hyperswitch team to get the production report endpoints for your account. Use your production API key and allowlist the production webhook URL before going live.

### Request parameters

#### Headers

| Header                           | Merchant Request | Profile Request | Description                           |
| -------------------------------- | ---------------- | --------------- | ------------------------------------- |
| `api-key`                        | Required         | Required        | Your secret Hyperswitch API key       |
| `Content-Type: application/json` | Required         | Required        | Identifies the request body as JSON   |
| `X-Profile-Id`                   | Not required     | Required        | Identifies the Profile for the report |

#### Request body

| Field                 | Required | Description                                                               |
| --------------------- | -------- | ------------------------------------------------------------------------- |
| `timeRange`           | Yes      | Contains the report start and end times                                   |
| `timeRange.startTime` | Yes      | Start time in ISO 8601 format                                             |
| `timeRange.endTime`   | No       | End time in ISO 8601 format. Defaults to the current time                 |
| `emails`              | Yes      | A non-empty array containing at least one valid email address             |
| `returnUrl`           | Yes      | The allowlisted HTTPS endpoint that receives the report webhook           |

Use UTC timestamps with millisecond precision, such as `2026-06-15T00:00:00.000Z`.

> Note: The `emails` array is currently required for API-key requests, even when the report is delivered through a webhook. If the field is missing or empty, the API returns HTTP `400` with error code `IR_06`.

> Note: `timeRange.endTime` is optional. We recommend sending it when you need a fixed and repeatable reporting period.

### Step 1: Configure your webhook endpoint

Set up a dedicated endpoint on your server to receive the report webhook.

Your `returnUrl` must:

* use HTTPS
* be accessible from the public internet
* be allowlisted by the Hyperswitch team (for production)
* accept `POST` requests with a JSON body

Share the exact sandbox and production URLs with the Hyperswitch team if you use different endpoints for each environment.

### Step 2: Trigger report generation

#### Merchant-level request

The following example generates a Merchant-level Payments report in sandbox:

```bash
curl --request POST \
  --url https://app.hyperswitch.io/api/analytics/v1/merchant/report/payments \
  --header 'Content-Type: application/json' \
  --header 'api-key: <api-key>' \
  --data '{
    "timeRange": {
      "startTime": "2026-06-15T00:00:00.000Z",
      "endTime": "2026-07-15T23:59:59.000Z"
    },
    "emails": [
      "reports@example.com"
    ],
    "returnUrl": "https://example.com/webhooks/hyperswitch-reports"
  }'
```

Change the endpoint suffix to generate another supported report type.

#### Profile-level request

For a Profile-level report, use the Profile endpoint and include `X-Profile-Id`:

```bash
curl --request POST \
  --url https://app.hyperswitch.io/api/analytics/v1/profile/report/payments \
  --header 'Content-Type: application/json' \
  --header 'X-Profile-Id: <profile-id>' \
  --header 'api-key: <api-key>' \
  --data '{
    "timeRange": {
      "startTime": "2026-06-15T00:00:00.000Z",
      "endTime": "2026-07-15T23:59:59.000Z"
    },
    "emails": [
      "reports@example.com"
    ],
    "returnUrl": "https://example.com/webhooks/hyperswitch-reports"
  }'
```

### API response

Hyperswitch returns HTTP `200` after accepting the report request. The response body can be JSON `null`.

```http
HTTP/1.1 200 OK
Content-Type: application/json

null
```

This response is only an acknowledgement. The report is generated asynchronously and is not included in the API response.

### Step 3: Receive the webhook

If report generation fails, Hyperswitch sends a `POST` request to your `returnUrl`.

The request includes the following signature header:

```http
X-Webhook-Signature-512: <hex-encoded-signature>
```

The failure payload has the following structure:

```json
{
  "org_id": "org_example",
  "merchant_id": "merchant_example",
  "data": {
    "code": "internal_server_error",
    "message": "We could not generate the report due to an internal server error. Please request the report again."
  },
  "event": "report_generation.failed"
}
```

#### Field reference

| Field          | Description                                                                           |
| -------------- | ------------------------------------------------------------------------------------- |
| `event`        | Event type. This is always `report_generation.failed` for report generation failures. |
| `org_id`       | Organization ID associated with the report request.                                   |
| `merchant_id`  | Merchant ID associated with the report request.                                       |
| `data.code`    | Machine-readable error code that identifies the failure.                              |
| `data.message` | Description of the failure and the recommended action.                                |

#### Handling a failure event

When you receive a failure event:

1. Record the error code and message for monitoring.
2. Submit a new report request.
3. Contact the Hyperswitch team if the failure continues.

### Step 4: Verify the webhook signature (optional)

Hyperswitch signs the exact request body using HMAC-SHA512 and the `payment_response_hash_key` associated with the Merchant or Profile.

To validate the webhook:

1. Read the exact raw request body.
2. Read the `X-Webhook-Signature-512` header.
3. Fetch `payment_response_hash_key` from payment settings in the Hyperswitch Control Center.
4. Generate an HMAC-SHA512 signature using the raw body and `payment_response_hash_key`.
5. Compare the generated and received signatures in constant time.
6. Reject the webhook if the signatures do not match.

Python example:

```python
import hashlib
import hmac


def verify_signature(raw_body: bytes, signature: str, hash_key: str) -> bool:
    expected = hmac.new(
        hash_key.encode("utf-8"),
        raw_body,
        hashlib.sha512,
    ).hexdigest()

    return hmac.compare_digest(expected, signature)
```

> Important: Do not parse and recreate the JSON before signature verification. Any change to the original request body can produce a different signature.

### Report limit

Each generated report can contain up to 50,000 rows.

If your report may exceed this limit:

1. Split the reporting period into smaller, non-overlapping time ranges.
2. Generate one report for each time range.
3. Combine the downloaded CSV files in your system.

Reports that exceed the limit are not automatically paginated.

For endpoint allowlisting and integration support, contact the Hyperswitch team through your usual support channel.
