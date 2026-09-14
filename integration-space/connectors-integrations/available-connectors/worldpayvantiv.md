---
description: >-
  Accept card and wallet payments through Worldpay Vantiv using merchant-scoped Basic authentication.
metaLinks:
  alternates:
    - worldpayvantiv.md
---

# Worldpay Vantiv

Worldpay Vantiv is implemented separately from the Worldpay connector and uses its own routes and configuration. Its declared checkout paths cover cards and selected wallets with refunds and mandate reuse. Immediate and delayed capture patterns are available across those methods.

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch d4e93b6e6dd39e45a8d5d8647b362f1bb8543946; host http://localhost:8080; fetched 2026-09-14; matrix canonical-json-v1 sha256 1beab3d720a6bcc5; 138 connectors.
     Do not edit by hand. This block regenerates from the connector's
     SupportedPaymentMethods declaration in code; edit that instead. -->

**Integration status:** sandbox

**Category:** payment gateway

**Webhook flows:** None declared in code

| Payment method | Type | Mandates | Refunds | Capture methods | 3DS | Card networks | Countries | Currencies |
|---|---|---|---|---|---|---|---|---|
| card | Credit Card | supported | supported | automatic, manual, sequential automatic | not supported | American Express, Diners Club, Discover, JCB, Mastercard, Visa | 133 ([full list](https://hyperswitch.io/pm-list)) | 147 ([full list](https://hyperswitch.io/pm-list)) |
| card | Debit Card | supported | supported | automatic, manual, sequential automatic | not supported | American Express, Diners Club, Discover, JCB, Mastercard, Visa | 133 ([full list](https://hyperswitch.io/pm-list)) | 147 ([full list](https://hyperswitch.io/pm-list)) |
| wallet | Apple Pay | supported | supported | automatic, manual, sequential automatic | not applicable | - | 133 ([full list](https://hyperswitch.io/pm-list)) | 147 ([full list](https://hyperswitch.io/pm-list)) |
| wallet | Google Pay | supported | supported | automatic, manual, sequential automatic | not applicable | - | 133 ([full list](https://hyperswitch.io/pm-list)) | 147 ([full list](https://hyperswitch.io/pm-list)) |


### Authentication

Worldpay Vantiv requires **Username**, **Password**, and **Merchant ID**. Hyperswitch constructs `<Username>:<Password>`, Base64-encodes it, and sends `Authorization: Basic <encoded value>` across payment, refund, dispute, and file request paths. Merchant ID is placed in the XML request data. See [`WorldpayvantivAuthType::try_from()`](https://github.com/juspay/hyperswitch/blob/d4e93b6e6dd39e45a8d5d8647b362f1bb8543946/crates/hyperswitch_connectors/src/connectors/worldpayvantiv/transformers.rs#L83-L99) and [`get_auth_header()`](https://github.com/juspay/hyperswitch/blob/d4e93b6e6dd39e45a8d5d8647b362f1bb8543946/crates/hyperswitch_connectors/src/connectors/worldpayvantiv.rs#L141-L154). The connector ID and configuration paths are independent from Worldpay; see [`ConnectorCommon for Worldpayvantiv`](https://github.com/juspay/hyperswitch/blob/d4e93b6e6dd39e45a8d5d8647b362f1bb8543946/crates/hyperswitch_connectors/src/connectors/worldpayvantiv.rs#L124-L139).

### Webhooks

Handled event wire values: **0**. Webhooks are not currently supported, so status updates rely on syncing through the API. The incoming webhook implementation returns `WebhooksNotImplemented`; see [`IncomingWebhook for Worldpayvantiv`](https://github.com/juspay/hyperswitch/blob/d4e93b6e6dd39e45a8d5d8647b362f1bb8543946/crates/hyperswitch_connectors/src/connectors/worldpayvantiv.rs#L1542-L1565).

### Activate Worldpay Vantiv with Hyperswitch

#### Before you start

1. Register with Worldpay Vantiv at [worldpayvantiv.com](https://www.worldpayvantiv.com/).
2. Sign in to the [Hyperswitch control center](https://app.hyperswitch.io/).
3. Obtain **Username**, **Password**, and **Merchant ID** from the Worldpay Vantiv dashboard.
4. If the activation flow asks you to select payment methods, choose only the methods enabled in the connector dashboard.

Follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for Worldpay Vantiv-specific behavior.

### Source reference

Authentication and webhook behavior on this page is tied to Hyperswitch `d4e93b6e6dd39e45a8d5d8647b362f1bb8543946`. See [Worldpay Vantiv connector source](https://github.com/juspay/hyperswitch/blob/d4e93b6e6dd39e45a8d5d8647b362f1bb8543946/crates/hyperswitch_connectors/src/connectors/worldpayvantiv.rs) and [Worldpay Vantiv transformers](https://github.com/juspay/hyperswitch/blob/d4e93b6e6dd39e45a8d5d8647b362f1bb8543946/crates/hyperswitch_connectors/src/connectors/worldpayvantiv/transformers.rs).
