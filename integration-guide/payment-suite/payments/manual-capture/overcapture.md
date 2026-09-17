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
     symbols: is_overcapture_enabled is taken from the connector authorize response, falling back to the effective enable_overcapture when the connector reports none = crates/router/src/core/payments/operations/payment_response.rs:2794-2804, 2912
     symbols: always_enable_overcapture applies only when capture_method is manual and the connector declares support, otherwise the effective value is cleared = crates/hyperswitch_domain_models/src/payments.rs:285-300
     symbols: the payments update route is POST /payments/{payment_id} = crates/router/src/routes/app.rs:1041-1043
     symbols: always_enable_overcapture profile field = crates/api_models/src/admin.rs:2488-2490; crates/diesel_models/src/business_profile.rs:91
     symbols: enable_overcapture accepted only with capture_method manual = crates/router/src/core/payments/helpers.rs:1244-1262
     symbols: connectors declared to support overcapture, Stripe and Adyen = crates/common_enums/src/connector_enums.rs:497-499
     symbols: only the Stripe connector implementation carries overcapture, as request_overcapture = crates/hyperswitch_connectors/src/connectors/stripe/transformers.rs:375-376; crates/hyperswitch_connectors/src/connectors/adyen/transformers.rs has zero occurrences
     symbols: the Unified Connector Service maps an overcapture result, and Adyen is not ucs-only so it can route either way = crates/hyperswitch_interfaces/src/unified_connector_service/transformers.rs:739-745; crates/router/src/core/unified_connector_service.rs:889-904; config/development.toml:1610
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

Go to Developer, then Payment Settings, then Always Enable Over Capture, and toggle it. This is the `always_enable_overcapture` setting on the profile.

It does not reach every payment on the profile. Hyperswitch applies it only when the payment's `capture_method` is `manual` and the connector routing the payment is one of the connectors declared to support overcapture. On any other payment the effective value is cleared, and the profile setting has no effect.

#### Per payment, from the API

Send the boolean `enable_overcapture` on [`POST /payments`](https://api-reference.hyperswitch.io/v1/payments/payments--create) or [`POST /payments/{payment_id}`](https://api-reference.hyperswitch.io/v1/payments/payments--update), the update call. The request value overrides the profile setting.

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

`is_overcapture_enabled` is the answer, when the connector gives one. Hyperswitch fills it from the connector's authorization response. If that response carries no overcapture result, Hyperswitch falls back to the effective request value, so `true` can mean the connector accepted overcapture, or only that it was requested and the connector said nothing. Treat it as confirmation only for a connector you already know reports the result.

| Field                    | Set by       | `true` means                                            |
| ------------------------ | ------------ | --------------------------------------------------------- |
| `enable_overcapture`     | You, or the profile setting | Overcapture was requested for this payment.  |
| `is_overcapture_enabled` | The connector, or the requested value as a fallback | The connector accepted overcapture, or it did not report a result and this repeats the request. |

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

Stripe and Adyen are the connectors declared to support overcapture. On any other connector the requested value is cleared, so `is_overcapture_enabled` comes back empty rather than `false`, and overcapture does not apply whatever you send. If you need overcapture on a different connector, contact the Hyperswitch support team.

Of those two, only Stripe carries overcapture in its own connector implementation today, which is why the example above uses it. The Adyen connector implementation sends no overcapture field and reads no overcapture result, so on that path an Adyen payment can report `is_overcapture_enabled: true` from the fallback described above. Adyen can also be routed through the Unified Connector Service, which does map an overcapture result, so what you get back depends on how your Adyen traffic is routed. Confirm overcapture with Adyen and with your Hyperswitch contact before relying on it; the tracking issue is [juspay/hyperswitch#14275](https://github.com/juspay/hyperswitch/issues/14275).

### Before you go live

* Set the capture method to `manual` at payment creation. Overcapture cannot be added to a `manual_multiple` payment.
* Confirm with your connector that it supports overcapture and reports the result, rather than reading `is_overcapture_enabled: true` as proof on its own. On a connector that reports nothing, that field repeats what you asked for.
* Refunds are bounded by `amount_captured`, so an overcaptured payment is refundable up to the larger captured figure. See [Refunds](../../refunds.md).

### Questions this page does not answer

* Partial capture, the uncaptured remainder, and capture statuses: [Manual Capture](./).
* Raising the authorized amount instead of capturing above it: [Incremental Authorization](../authorizations/incremental-authorization.md).
* Per-connector overcapture headroom: the connector's own documentation.
