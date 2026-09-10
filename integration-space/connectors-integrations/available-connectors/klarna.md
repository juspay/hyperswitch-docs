---
description: Accept pay later payments through Klarna.
metaLinks:
  alternates:
    - klarna.md
---

# Klarna

<div align="left"><img src="https://hyperswitch.io/icons/homePageIcons/logos/klarnaLogo.svg" alt=""></div>

Klarna provides pay later payments through a payment gateway integration. The declared method supports refunds and automatic, manual, or sequential automatic capture, but not mandates. Incoming webhooks are not supported by the connector, so status updates rely on API synchronization.

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch a17a23c4c4c907d2314043a32a9f505f7f2bd4f9; host http://localhost:8080; fetched 2026-09-10; matrix canonical-json-v1 sha256 36360b019f2761dd; 138 connectors.
     Do not edit by hand. This block regenerates from the connector's
     SupportedPaymentMethods declaration in code; edit that instead. -->

**Integration status:** live

**Category:** payment gateway

**Webhook flows:** None declared in code

| Payment method | Type | Mandates | Refunds | Capture methods | Countries | Currencies |
|---|---|---|---|---|---|---|
| pay later | Klarna | not supported | supported | automatic, manual, sequential automatic | 22 ([full list](https://hyperswitch.io/pm-list)) | 12 ([full list](https://hyperswitch.io/pm-list)) |

### Authentication

Supply an API Username and API Password in the connector configuration. Hyperswitch combines them as `<API username>:<API password>`, Base64-encodes the result, and sends it as `Authorization: Basic <base64(username:password)>` on connector requests. See [`KlarnaAuthType::try_from()`](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/klarna/transformers.rs#L454-L470) and [`get_auth_header()`](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/klarna.rs#L93-L106).

### Webhooks

Klarna webhooks are not currently processed by this connector. Do not configure Klarna webhooks as the source of status updates in Hyperswitch. The incoming webhook implementation returns `EventNotSupported` and `WebhooksNotImplemented`; see [`get_webhook_event_type()`](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/klarna.rs#L1450-L1474).

### Activate Klarna with Hyperswitch

#### Before you start

1. Register with Klarna.
2. Create a Hyperswitch account.
3. Have the credentials listed in [Authentication](#authentication) ready.

To connect Klarna to your Hyperswitch account, follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for what Klarna supports.

### Source reference

[Klarna connector implementation](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/klarna.rs) and [Klarna data mappings](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/klarna/transformers.rs)
