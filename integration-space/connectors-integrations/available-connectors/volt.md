---
description: Accept bank redirect payments through Volt.
metaLinks:
  alternates:
    - volt.md
---

# Volt

<img src="../../.gitbook/assets/Volt-Logo (1).png" alt="logo_volt" data-size="original">

Volt is a payment gateway for open banking payments through bank redirects. The declared methods support refunds and automatic capture, but not mandates. Webhooks cover payment and refund updates.

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch a17a23c4c4c907d2314043a32a9f505f7f2bd4f9; host http://localhost:8080; fetched 2026-09-10; matrix canonical-json-v1 sha256 36360b019f2761dd; 138 connectors.
     Do not edit by hand. This block regenerates from the connector's
     SupportedPaymentMethods declaration in code; edit that instead. -->

**Integration status:** live

**Category:** payment gateway

**Webhook flows:** payments, refunds

| Payment method | Type | Mandates | Refunds | Capture methods | Countries | Currencies |
|---|---|---|---|---|---|---|
| bank redirect | Open Banking | not supported | supported | automatic | 31 ([full list](https://hyperswitch.io/pm-list)) | DKK, EUR, GBP, NOK, PLN, SEK |
| bank redirect | Open Banking UK | not supported | supported | automatic | 31 ([full list](https://hyperswitch.io/pm-list)) | GBP |

### Connector-Specific Notes

* **Request headers:** Hyperswitch generates an idempotency key and sends the API version and hosted initiation channel on payment requests. You do not need to supply these headers. See [`build_headers()`](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/volt.rs#L95-L130).

### Authentication

Supply a Username, Password, Client ID, and Client Secret in the connector configuration. Hyperswitch exchanges all four credentials for an access token, then sends `Authorization: Bearer <access token>` on payment requests. See [`VoltAuthType::try_from()`](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/volt/transformers.rs#L293-L317), [`VoltAuthUpdateRequest::try_from()`](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/volt/transformers.rs#L242-L270), and [`build_headers()`](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/volt.rs#L95-L130).

### Webhooks

Configure a webhook merchant secret in Hyperswitch; the shared webhook verifier uses that value as the signature key. See [`verify_webhook_source()`](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_interfaces/src/webhooks.rs#L266-L301). Volt webhooks use HMAC-SHA256 verification: Hyperswitch reads the hex signature from `X-Volt-Signed` and verifies the request body, `X-Volt-Timed`, and the version from the user-agent value. See [`webhook_headers`](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/volt/transformers.rs#L39-L44) and [`get_webhook_source_verification_algorithm()`](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/volt.rs#L668-L708).

The connector recognizes seven webhook status values. An empty body is treated as endpoint verification.

| Resource | Status | Effect in Hyperswitch |
|---|---|---|
| Payment | `RECEIVED` | Payment is marked successful |
| Payment | `FAILED` | Payment is marked failed |
| Payment | `NOT_RECEIVED` | Payment is marked failed |
| Payment | `COMPLETED` | Payment remains processing |
| Payment | `PENDING` | Payment remains processing |
| Refund | `REFUND_CONFIRMED` | Refund is marked successful |
| Refund | `REFUND_FAILED` | Refund is marked failed |

The wire values and mappings are defined by [`VoltWebhookPaymentStatus`](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/volt/transformers.rs#L730-L780).

### Activate Volt with Hyperswitch

#### Before you start

1. Register with Volt.
2. Create a Hyperswitch account.
3. Have the credentials listed in [Authentication](#authentication) ready.

To connect Volt to your Hyperswitch account, follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for what Volt supports.

### Source reference

[Volt connector implementation](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/volt.rs) and [Volt data mappings](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/volt/transformers.rs)
