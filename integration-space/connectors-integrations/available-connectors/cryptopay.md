---
description: Connect Cryptopay through Hyperswitch.
metaLinks:
  alternates:
    - cryptopay.md
---

# Cryptopay

Cryptopay lets merchants send cryptocurrency payments through a payment gateway integration. Cryptopay signs API requests with the Secret Key and signs webhook payloads with the `X-Cryptopay-Signature` header. The pinned connector does not implement capture requests, so review the capture limitation before enabling the flow.

To connect Cryptopay to your Hyperswitch account, follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for connector-specific behavior.

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7; host http://localhost:8080; fetched 2026-09-21; matrix canonical-json-v1 sha256 873f2bbfe94dc9fda3279d10e6c077a8fe4a10d38f97f3aba64d57093c5245c4; 146 connectors.
     Do not edit by hand. Payment method rows regenerate from the
     connector's SupportedPaymentMethods declaration; countries and
     currencies come from pm_filters in config/development.toml.
     Webhook flows and capture methods print as declared; the
     declaration-gap check reconciles them in prose. Edit those
     sources instead. -->

**Integration status:** live

**Category:** payment gateway

**Webhook flows:** payments

| Payment method | Type | Mandates | Refunds | Capture methods | Countries | Currencies |
|---|---|---|---|---|---|---|
| crypto | Crypto | not supported | not supported | automatic, sequential automatic | - | - |

The capability block declares automatic and sequential automatic capture, but the pinned connector has an empty Capture integration with no `build_request`. Capture requests are not implemented; treat the capture declaration as an upstream gap and do not rely on post-authorisation capture. See [`ConnectorIntegration<Capture, ...>`](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/cryptopay.rs#L419-L425).

### Authentication

Enter **API Key** and **Secret Key**. The connector labels are defined in [`[cryptopay.connector_auth.BodyKey]`](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/connector_configs/toml/sandbox.toml); the accepted fields are mapped by [`CryptopayAuthType`](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/cryptopay/transformers.rs#L107-L126). Each API request gets an HMAC-SHA1 `Authorization` value built from the Secret Key in [`build_headers()`](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/cryptopay.rs#L91-L147). **Source verification key** is the webhook signing secret, not a connector-auth field. These credentials are not currency-scoped.

### Before you start

1. Obtain the **API Key**, **Secret Key**, and webhook signing secret from Cryptopay.
2. Sign in to the [Hyperswitch control center](https://app.hyperswitch.io/) and open Cryptopay.
3. Enter the two connector-auth fields and configure the webhook signing secret separately.

No provider dashboard path beyond these credential names was verified for this page.

### Webhooks

Cryptopay verifies callbacks with HMAC-SHA256 over the raw request body, using the hex signature in `X-Cryptopay-Signature`. It maps the wire statuses `completed` to success, `unresolved` to action required, and `cancelled` to failure; other statuses are unsupported. See [`get_webhook_source_verification_algorithm()`](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/cryptopay.rs#L429-L456) and [`get_webhook_event_type()`](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/cryptopay.rs#L477-L499).

### Source reference

Authentication, capture, and webhook behavior on this page is tied to Hyperswitch `ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7`. See [Cryptopay connector source](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/cryptopay.rs) and [Cryptopay transformers](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/cryptopay/transformers.rs).
