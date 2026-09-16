---
description: >-
  Capture more than the originally authorized amount on a manual capture payment
icon: chart-diagram
metaLinks:
  alternates:
    - overcapture.md
---

<!-- truth manifest; hyperswitch 184ffd4c015fd3fea2f3868549f1a86ffa5f40da; spec api-reference/v1/openapi_spec_v1.json@184ffd4c015fd3fea2f3868549f1a86ffa5f40da
     symbols: enable_overcapture = crates/api_models/src/payments.rs:1611, 8008
     symbols: is_overcapture_enabled = crates/api_models/src/payments.rs:8013
     symbols: is_overcapture_enabled is taken from the connector authorize response = crates/router/src/core/payments/operations/payment_response.rs:2794-2798, 2912
     symbols: always_enable_overcapture profile field = crates/api_models/src/admin.rs:2488-2490; crates/diesel_models/src/business_profile.rs:91
     symbols: enable_overcapture accepted only with capture_method manual = crates/router/src/core/payments/helpers.rs:1244-1262
     symbols: connectors declared to support overcapture, Stripe and Adyen = crates/common_enums/src/connector_enums.rs:497-499
     symbols: amount_to_capture ceiling check skipped when the attempt has overcapture enabled = crates/router/src/core/payments/operations/payment_capture.rs:101-111
     symbols: amount_capturable, amount_received = crates/api_models/src/payments.rs:7490
     symbols: capture_method wire values = crates/common_enums/src/enums.rs:814-830
     symbols: refundable ceiling is amount_captured = crates/router/src/core/refunds.rs:1665-1674
     checked: 2026-09-16 -->

# Overcapture

### Overview

Overcapture is capturing more than the amount the issuer originally authorized. It is useful when the final order value is only known after authorization:

* Shipping, handling, or gratuities added later.
* Price adjustments after the customer checked out.
* Orders where you would otherwise authorize high to be safe.

### It only works with single manual capture

Overcapture is accepted only when `capture_method` is `manual`. A request with `enable_overcapture: true` and any other capture method, `manual_multiple` included, is rejected with a precondition error saying overcapture is supported only with manual capture. If you need several captures, you cannot also have overcapture; pick one at payment creation.

### Turn it on

#### Profile level, from the dashboard

Go to Developer, then Payment Settings, then Always Enable Over Capture, and toggle it. This is the `always_enable_overcapture` setting on the profile, and it applies to every payment on that profile.

#### Per payment, from the API

Send the boolean `enable_overcapture` on [`POST /payments`](https://api-reference.hyperswitch.io/v1/payments/payments--create) or [`POST /payments/{payment_id}/update`](https://api-reference.hyperswitch.io/v1/payments/payments--update). The request value overrides the profile setting.

**Sample curl:**

```bash
curl --location 'https://sandbox.hyperswitch.io/payments' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'api-key: <api key>' \
--data '{
  "amount": 100,
  "currency": "USD",
  "confirm": true,
  "capture_method": "manual",
  "enable_overcapture": true
}'
```

### Asking is not the same as getting

Two fields, and they do not mean the same thing.

`enable_overcapture` is what you asked for. You set it; it is echoed back.

`is_overcapture_enabled` is the answer. Hyperswitch fills it from the connector's authorization response, so it tells you whether the processor actually accepted overcapture for this payment. Read it after authorization, before you plan a capture above the authorized amount.

| Field                    | Set by       | `true` means                                            |
| ------------------------ | ------------ | --------------------------------------------------------- |
| `enable_overcapture`     | You          | You requested overcapture for this payment.               |
| `is_overcapture_enabled` | The connector | The connector accepted overcapture for this payment.       |

**Sample response after authorization:**

```json
{
  "payment_id": "<payment_id>",
  "status": "requires_capture",
  "amount": 100,
  "amount_capturable": 100,
  "connector": "stripe",
  "enable_overcapture": true,
  "is_overcapture_enabled": true,
  "capture_method": "manual",
  "payment_method": "card",
  "payment_method_type": "debit",
  "created": "2025-09-24T11:29:55.629Z",
  "expires_on": "2025-09-24T11:44:55.629Z"
}
```

### What changes at capture time

Normally `amount_to_capture` may not exceed `amount_capturable`, and a capture above it is rejected. When the payment attempt has overcapture enabled, that ceiling check is skipped and a larger `amount_to_capture` goes through to the connector. How much above the authorized amount the connector will accept is the connector's rule, not Hyperswitch's, and it is usually a percentage of the authorization. Confirm the headroom with your connector before you rely on it.

`amount_capturable` after authorization still shows the authorized amount, so it is not the overcapture limit. Use `amount_received` after capture to see what was actually settled.

### Connector support

Stripe and Adyen are the connectors declared to support overcapture. Any other connector will leave `is_overcapture_enabled` false, whatever you send. If you need overcapture on a different connector, contact the Hyperswitch support team.

### Before you go live

* Set the capture method to `manual` at payment creation. Overcapture cannot be added to a `manual_multiple` payment.
* Check `is_overcapture_enabled` after authorization rather than assuming your request was honoured.
* Refunds are bounded by `amount_captured`, so an overcaptured payment is refundable up to the larger captured figure. See [Refunds](../../refunds.md).

### Questions this page does not answer

* Partial capture, the uncaptured remainder, and capture statuses: [Manual Capture](./).
* Raising the authorized amount instead of capturing above it: [Incremental Authorization](../authorizations/incremental-authorization.md).
* Per-connector overcapture headroom: the connector's own documentation.
