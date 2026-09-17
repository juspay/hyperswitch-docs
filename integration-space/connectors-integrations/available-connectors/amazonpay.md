---
description: Accept Amazon Pay wallet payments.
---

# Amazon Pay

Amazon Pay provides a wallet checkout route for customers using their Amazon account. The wallet route uses automatic capture and supports refunds. It does not declare mandate reuse or webhook handling.

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch 9e5dd70d1cb4011bbcca3114862406008a0b61f8; host http://localhost:8080; fetched 2026-09-17; matrix canonical-json-v1 sha256 25db1ecc45c5b9c7; 140 connectors.
     Do not edit by hand. Payment method rows regenerate from the
     connector's SupportedPaymentMethods declaration; countries and
     currencies come from pm_filters in config/development.toml.
     Webhook flows and capture methods print as declared; the
     declaration-gap check reconciles them in prose. Edit those
     sources instead. -->

**Integration status:** beta

**Category:** alternative payment method

**Webhook flows:** None declared in code

| Payment method | Type | Mandates | Refunds | Capture methods | Countries | Currencies |
|---|---|---|---|---|---|---|
| wallet | Amazon Pay | not supported | supported | automatic | USA | USD |

### Authentication

Supply **Public Key** and **Private Key**, the labels shown in the Hyperswitch control center. Hyperswitch hashes the canonical request with SHA-256, signs the algorithm line and request hash with RSA-PSS-SHA256 using the Private Key, Base64-encodes the signature, and places the Public Key with the signature in the `Authorization` header. See [`AmazonpayAuthType::try_from()`](https://github.com/juspay/hyperswitch/blob/9e5dd70d1cb4011bbcca3114862406008a0b61f8/crates/hyperswitch_connectors/src/connectors/amazonpay/transformers.rs#L323-L339), [`create_authorization_header()`](https://github.com/juspay/hyperswitch/blob/9e5dd70d1cb4011bbcca3114862406008a0b61f8/crates/hyperswitch_connectors/src/connectors/amazonpay.rs#L92-L130), [`create_signature()`](https://github.com/juspay/hyperswitch/blob/9e5dd70d1cb4011bbcca3114862406008a0b61f8/crates/hyperswitch_connectors/src/connectors/amazonpay.rs#L132-L184), and [`build_headers()`](https://github.com/juspay/hyperswitch/blob/9e5dd70d1cb4011bbcca3114862406008a0b61f8/crates/hyperswitch_connectors/src/connectors/amazonpay.rs#L209-L278).

### Before you start

1. Sign in to the [Hyperswitch control center](https://app.hyperswitch.io/).
2. Enter **Public Key** and **Private Key** during connector activation.
3. Enable Amazon Pay only after the wallet is available on your connector account.

To connect Amazon Pay to your Hyperswitch account, follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for Amazon Pay-specific behavior.

### Webhooks

Amazon Pay webhooks are not supported. Use payment sync for status updates. [`get_webhook_object_reference_id()`](https://github.com/juspay/hyperswitch/blob/9e5dd70d1cb4011bbcca3114862406008a0b61f8/crates/hyperswitch_connectors/src/connectors/amazonpay.rs#L727-L732), [`get_webhook_event_type()`](https://github.com/juspay/hyperswitch/blob/9e5dd70d1cb4011bbcca3114862406008a0b61f8/crates/hyperswitch_connectors/src/connectors/amazonpay.rs#L734-L740), and [`get_webhook_resource_object()`](https://github.com/juspay/hyperswitch/blob/9e5dd70d1cb4011bbcca3114862406008a0b61f8/crates/hyperswitch_connectors/src/connectors/amazonpay.rs#L742-L748) each return `WebhooksNotImplemented`.

### Source reference

Authentication and webhook behavior on this page follows [Amazon Pay connector source](https://github.com/juspay/hyperswitch/blob/9e5dd70d1cb4011bbcca3114862406008a0b61f8/crates/hyperswitch_connectors/src/connectors/amazonpay.rs) and [Amazon Pay transformers](https://github.com/juspay/hyperswitch/blob/9e5dd70d1cb4011bbcca3114862406008a0b61f8/crates/hyperswitch_connectors/src/connectors/amazonpay/transformers.rs).
