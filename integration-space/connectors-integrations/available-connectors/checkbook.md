---
description: Connect Checkbook through Hyperswitch.
metaLinks:
  alternates:
    - checkbook.md
---

# Checkbook

Checkbook lets merchants receive ACH payments through a bank-transfer integration. The connector is in beta, and payment callbacks use a signed `signature` header that Checkbook provides with the webhook request.

To connect Checkbook to your Hyperswitch account, follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for connector-specific behavior.

This connector is in beta status. Check with the Hyperswitch team before enabling it in production.


### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7; host http://localhost:8080; fetched 2026-09-21; matrix canonical-json-v1 sha256 873f2bbfe94dc9fda3279d10e6c077a8fe4a10d38f97f3aba64d57093c5245c4; 146 connectors.
     Do not edit by hand. Payment method rows regenerate from the
     connector's SupportedPaymentMethods declaration; countries and
     currencies come from pm_filters in config/development.toml.
     Webhook flows and capture methods print as declared; the
     declaration-gap check reconciles them in prose. Edit those
     sources instead. -->

**Integration status:** beta

**Category:** payment gateway

**Webhook flows:** payments

| Payment method | Type | Mandates | Refunds | Capture methods | Countries | Currencies |
|---|---|---|---|---|---|---|
| bank transfer | ACH Direct Debit | not supported | not supported | automatic | USA | USD |

### Authentication

Enter **Checkbook Publishable key** and **Checkbook API Secret key**. Checkbook combines them as `publishable_key:secret_key` for the `Authorization` header. The control-center labels are defined in [`[checkbook.connector_auth.BodyKey]`](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/connector_configs/toml/sandbox.toml#L1842-L1846); the accepted fields are mapped by [`CheckbookAuthType`](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/checkbook/transformers.rs#L53-L69) and sent by [`get_auth_header()`](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/checkbook.rs#L120-L136). The Source verification key is not a connector credential.

### Before you start

1. Create or sign in to your Checkbook account and obtain the **Checkbook Publishable key** and **Checkbook API Secret key**.
2. Sign in to the [Hyperswitch control center](https://app.hyperswitch.io/) and open Checkbook.
3. Enter those two credentials.

No provider dashboard path beyond account setup was verified for this page.

### Webhooks

Checkbook maps the webhook status in the request body to a payment event through [`get_webhook_event_type()`](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/checkbook.rs#L554-L567). It verifies the callback with HMAC-SHA256: the `signature` header carries `signature=<hex>` and `nonce=<value>`, and the signed message is the request body followed by the nonce. See [`get_webhook_source_verification_algorithm()`](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/checkbook.rs#L580-L628).

### Source reference

Authentication, capture, and webhook behavior on this page is tied to Hyperswitch `ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7`. See [Checkbook connector source](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/checkbook.rs) and [Checkbook transformers](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/checkbook/transformers.rs).
