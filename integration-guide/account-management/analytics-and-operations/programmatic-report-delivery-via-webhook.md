---
icon: database
---

# Programmatic Report Delivery via Webhook

### Overview

Hyperswitch supports asynchronous report generation for automated workflows. You can trigger a report using an API key and receive the completed report through a webhook.

The webhook payload contains a pre-signed URL to download the CSV file. The CSV file is not included in the webhook payload.

Programmatic report delivery is supported only at the Merchant and Profile levels. Organization-level reports are not supported.

### How It Works

1. Send a report request with a time range, email address and `returnUrl`.
2. Hyperswitch accepts the request and starts report generation.
3. Hyperswitch uploads the completed CSV file to secure storage.
4. Hyperswitch sends a signed webhook to your `returnUrl`.
5. Verify the signature and download the report using `data.download_url`.

Report generation can take a few seconds or several minutes, depending on the amount of data.

### Prerequisites

Before you begin, ensure that you have the following:

* a Hyperswitch sandbox/production API key
* at least one valid email address for the \`emails\` field
* a public HTTPS endpoint that can receive `POST` requests
* your Profile ID or when requesting a Profile-level report

Note: You do not need to provide a Merchant ID for Merchant-level reports. Hyperswitch identifies the Merchant from the API key.

### Supported Report Types

You can generate the following reports:

| Report Type     | URL Suffix        |
| --------------- | ----------------- |
| Payments        | `payments`        |
| Refunds         | `refunds`         |
| Disputes        | `dispute`         |
| Payouts         | `payouts`         |
| Authentications | `authentications` |

> Note: Use `dispute` in the endpoint URL, not `disputes`. Authentications is only supported in sandbox

### Sandbox Endpoints

#### Merchant-Level Endpoints

Use these endpoints to generate a report for the Merchant associated with your API key.

| Report Type     | Endpoint                                                                      |
| --------------- | ----------------------------------------------------------------------------- |
| Payments        | `https://app.hyperswitch.io/api/analytics/v1/merchant/report/payments`        |
| Refunds         | `https://app.hyperswitch.io/api/analytics/v1/merchant/report/refunds`         |
| Disputes        | `https://app.hyperswitch.io/api/analytics/v1/merchant/report/dispute`         |
| Payouts         | `https://app.hyperswitch.io/api/analytics/v1/merchant/report/payouts`         |
| Authentications | `https://app.hyperswitch.io/api/analytics/v1/merchant/report/authentications` |

The API key identifies the Merchant. You do not need to pass a Merchant ID in the endpoint or request body.

#### Profile-Level Endpoints

Use these endpoints with the `X-Profile-Id` header to generate a report for a specific Profile.

| Report Type     | Endpoint                                                                     |
| --------------- | ---------------------------------------------------------------------------- |
| Payments        | `https://app.hyperswitch.io/api/analytics/v1/profile/report/payments`        |
| Refunds         | `https://app.hyperswitch.io/api/analytics/v1/profile/report/refunds`         |
| Disputes        | `https://app.hyperswitch.io/api/analytics/v1/profile/report/dispute`         |
| Payouts         | `https://app.hyperswitch.io/api/analytics/v1/profile/report/payouts`         |
| Authentications | `https://app.hyperswitch.io/api/analytics/v1/profile/report/authentications` |

#### Production Endpoints

Contact the Hyperswitch team to get the production report endpoints for your account. Use your production API key and allowlist the production webhook URL before going live.

### Request Parameters

#### Headers

| Header                           | Merchant Request | Profile Request | Description                           |
| -------------------------------- | ---------------- | --------------- | ------------------------------------- |
| `api-key`                        | Required         | Required        | Your secret Hyperswitch API key       |
| `Content-Type: application/json` | Required         | Required        | Identifies the request body as JSON   |
| `X-Profile-Id`                   | Not required     | Required        | Identifies the Profile for the report |

#### Request Body

| Field                 | Required | Description                                                               |
| --------------------- | -------- | ------------------------------------------------------------------------- |
| `timeRange`           | Yes      | Contains the report start and end times                                   |
| `timeRange.startTime` | Yes      | Start time in ISO 8601 format                                             |
| `timeRange.endTime`   | No       | End time in ISO 8601 format. Defaults to the current time                 |
| `emails`              | Yes      | A non-empty array containing at least one valid email address             |
| `returnUrl`           | Yes      | The allowlisted HTTPS endpoint that receives the completed report webhook |

Use UTC timestamps with millisecond precision, such as `2026-06-15T00:00:00.000Z`.

> Note: The `emails` array is currently required for API-key requests, even when the report is delivered through a webhook. If the field is missing or empty, the API returns HTTP `400` with error code `IR_06`.

> Note: `timeRange.endTime` is optional. We recommend sending it when you need a fixed and repeatable reporting period.

### Step 1: Configure Your Webhook Endpoint

Set up a dedicated endpoint on your server to receive the completed report webhook.

Your `returnUrl` must:

* use HTTPS
* be accessible from the public internet
* be allowlisted by the Hyperswitch team(for production)
* accept `POST` requests with a JSON body

Share the exact sandbox and production URLs with the Hyperswitch team if you use different endpoints for each environment.

### Step 2: Trigger Report Generation

#### Merchant-Level Request

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

#### Profile-Level Request

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

### API Response

Hyperswitch returns HTTP `200` after accepting the report request. The response body can be JSON `null`.

```http
HTTP/1.1 200 OK
Content-Type: application/json

null
```

This response is only an acknowledgement. The report is generated asynchronously and is not included in the API response.

### Step 3: Receive the Webhook

When the report is ready, Hyperswitch sends a `POST` request to your `returnUrl`.

The request includes the following signature header:

```http
X-Webhook-Signature-512: <hex-encoded-signature>
```

The webhook payload has the following structure:

```json
{
  "event_type": "report_generation.completed",
  "status": "success",
  "org_id": "org_example",
  "merchant_id": "merchant_example",
  "data": {
    "report_type": "payment_report",
    "start_date_utc": "2026-06-15",
    "end_date_utc": "2026-07-15",
    "download_url": "https://example-bucket.s3.amazonaws.com/report.csv?...",
    "expires_in_hours": 48
  }
}
```

The report is available at `data.download_url`. The webhook does not contain the CSV file itself.

#### Field reference

<table data-search="false"><thead><tr><th>Field</th><th>Description</th></tr></thead><tbody><tr><td><code>event_type</code></td><td>Event type. This is always <code>report_generation.completed</code>.</td></tr><tr><td><code>status</code></td><td>Report generation status. <code>success</code> means the report was generated and uploaded successfully.</td></tr><tr><td><code>org_id</code></td><td>Organization ID associated with the report.</td></tr><tr><td><code>merchant_id</code></td><td>Merchant ID associated with the report.</td></tr><tr><td><code>data.report_type</code></td><td>Report type. Possible values are <code>payment_report</code>, <code>refund_report</code>, <code>dispute_report</code>, <code>payout_report</code>, and <code>authentication_report</code>.</td></tr><tr><td><code>data.start_date_utc</code></td><td>Start date of the reporting period in <code>YYYY-MM-DD</code> UTC format.</td></tr><tr><td><code>data.end_date_utc</code></td><td>End date of the reporting period in <code>YYYY-MM-DD</code> UTC format.</td></tr><tr><td><code>data.download_url</code></td><td>Pre-signed AWS S3 URL for downloading the generated CSV report. The webhook payload does not contain the report itself.</td></tr><tr><td><code>data.expires_in_hours</code></td><td>Number of hours before the download URL expires, typically <code>48</code>. Generate a new report if the URL has expired.</td></tr></tbody></table>

### Step 4: Verify the Webhook Signature(Optional)

Hyperswitch signs the exact request body using HMAC-SHA512 and the `payment_response_hash_key` associated with the Merchant or Profile.

To validate the webhook:

1. Read the exact raw request body.
2. Read the `X-Webhook-Signature-512` header.
3. Generate an HMAC-SHA512 signature using the raw body and `payment_response_hash_key`.
4. Fetch `payment_response_hash_key`  from payment settings in hyperwitch control center.
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

### Step 5: Download the Report

After verifying the signature, download the CSV file from `data.download_url`.

The pre-signed URL usually expires after 48 hours. Download and store the report before the value in `data.expires_in_hours` is reached.

> Security Warning: Do not expose or log the complete `download_url`. Anyone with access to the URL may be able to download the report until it expires.

### Report Limit

Each generated report can contain up to 50,000 rows.

If your report may exceed this limit:

1. Split the reporting period into smaller, non-overlapping time ranges.
2. Generate one report for each time range.
3. Combine the downloaded CSV files in your system.

Reports that exceed the limit are not automatically paginated.

For endpoint allowlisting and integration support, contact the Hyperswitch team through your usual support channel.
