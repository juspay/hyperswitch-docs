---
description: >-
  Accept card-redirect payments through Prophetpay using profile-scoped credentials.
metaLinks:
  alternates:
    - prophetpay.md
---

# Prophetpay

Prophetpay uses a hosted card-entry path for one-time payments. Refunds are supported for that path, while mandate reuse is not declared. The connector supports immediate and follow-up automatic capture behavior.

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch d4e93b6e6dd39e45a8d5d8647b362f1bb8543946; host http://localhost:8080; fetched 2026-09-14; matrix canonical-json-v1 sha256 1beab3d720a6bcc5; 138 connectors.
     Do not edit by hand. This block regenerates from the connector's
     SupportedPaymentMethods declaration in code; edit that instead. -->

**Integration status:** alpha

**Category:** payment gateway

**Webhook flows:** None declared in code

| Payment method | Type | Mandates | Refunds | Capture methods | Countries | Currencies |
|---|---|---|---|---|---|---|
| card redirect | Card Redirect | not supported | supported | automatic, sequential automatic | USA | USD |


### Authentication

Prophetpay requires **Username**, **Password**, and **Profile ID**. Hyperswitch constructs `<Username>:<Password>`, Base64-encodes it, and sends `Authorization: Basic <encoded value>` for each implemented request path. Profile ID is placed in request bodies to select the merchant profile. See [`ProphetpayAuthType::try_from()`](https://github.com/juspay/hyperswitch/blob/d4e93b6e6dd39e45a8d5d8647b362f1bb8543946/crates/hyperswitch_connectors/src/connectors/prophetpay/transformers.rs#L52-L68), [`get_auth_header()`](https://github.com/juspay/hyperswitch/blob/d4e93b6e6dd39e45a8d5d8647b362f1bb8543946/crates/hyperswitch_connectors/src/connectors/prophetpay.rs#L112-L127), and [`ProphetpayPaymentsRequest::try_from()`](https://github.com/juspay/hyperswitch/blob/d4e93b6e6dd39e45a8d5d8647b362f1bb8543946/crates/hyperswitch_connectors/src/connectors/prophetpay/transformers.rs#L132-L150).

### Webhooks

Handled event wire values: **0**. Webhooks are not currently supported, so status updates rely on syncing through the API. The incoming webhook implementation returns `WebhooksNotImplemented`; see [`IncomingWebhook for Prophetpay`](https://github.com/juspay/hyperswitch/blob/d4e93b6e6dd39e45a8d5d8647b362f1bb8543946/crates/hyperswitch_connectors/src/connectors/prophetpay.rs#L708-L731).

### Activate Prophetpay with Hyperswitch

#### Before you start

1. Register for Prophetpay at [clubprophet.com](https://www.clubprophet.com/products---prophetpay).
2. Sign in to the [Hyperswitch control center](https://app.hyperswitch.io/).
3. Obtain **Username** and **Password** during onboarding and obtain **Profile ID** from the Prophetpay dashboard.
4. If the activation flow asks you to select payment methods, choose only the methods enabled in the connector dashboard.

Follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for Prophetpay-specific behavior.

### Source reference

Authentication and webhook behavior on this page is tied to Hyperswitch `d4e93b6e6dd39e45a8d5d8647b362f1bb8543946`. See [Prophetpay connector source](https://github.com/juspay/hyperswitch/blob/d4e93b6e6dd39e45a8d5d8647b362f1bb8543946/crates/hyperswitch_connectors/src/connectors/prophetpay.rs) and [Prophetpay transformers](https://github.com/juspay/hyperswitch/blob/d4e93b6e6dd39e45a8d5d8647b362f1bb8543946/crates/hyperswitch_connectors/src/connectors/prophetpay/transformers.rs).
