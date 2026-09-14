---
description: >-
  Accept card payments through Bambora with refunds and immediate or delayed capture options.
metaLinks:
  alternates:
    - bambora.md
---

# Bambora

<div align="left"><img src="https://hyperswitch.io/icons/homePageIcons/logos/bamboraLogo.svg" alt=""></div>

Bambora is a Worldline payment solution for merchants accepting card payments. Its card path supports refunds and gives merchants a choice between immediate and delayed capture patterns. Mandate-based reuse is not part of this integration.

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch d4e93b6e6dd39e45a8d5d8647b362f1bb8543946; host http://localhost:8080; fetched 2026-09-14; matrix canonical-json-v1 sha256 1beab3d720a6bcc5; 138 connectors.
     Do not edit by hand. This block regenerates from ConnectorSpecifications
     and pm_filters in code; edit those sources instead. -->

**Integration status:** sandbox

**Category:** payment gateway

**Webhook flows:** None declared in code

| Payment method | Type | Mandates | Refunds | Capture methods | 3DS | Card networks | Countries | Currencies |
|---|---|---|---|---|---|---|---|---|
| card | Credit Card | not supported | supported | automatic, manual, sequential automatic | supported, optional | American Express, Diners Club, Discover, JCB, Mastercard, Visa | CAN, USA | USD |


### Authentication

Bambora requires **Merchant ID** and **Passcode**. Hyperswitch constructs `<Merchant ID>:<Passcode>`, Base64-encodes that value, and sends `Authorization: Passcode <encoded value>` on every implemented request path. See [`BamboraAuthType::try_from()`](https://github.com/juspay/hyperswitch/blob/d4e93b6e6dd39e45a8d5d8647b362f1bb8543946/crates/hyperswitch_connectors/src/connectors/bambora/transformers.rs#L257-L272) and [`get_auth_header()`](https://github.com/juspay/hyperswitch/blob/d4e93b6e6dd39e45a8d5d8647b362f1bb8543946/crates/hyperswitch_connectors/src/connectors/bambora.rs#L125-L136).

### Before you start

1. Register with Bambora at [bambora.com](https://www.bambora.com/).
2. Sign in to the [Hyperswitch control center](https://app.hyperswitch.io/).
3. Obtain the **Merchant ID** and **Passcode** from the Bambora dashboard.
4. If the activation flow asks you to select payment methods, choose only the methods enabled in the connector dashboard.

Follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for Bambora-specific behavior.

### Webhooks

Handled event wire values: **0**. Webhooks are not currently supported, so status updates rely on syncing through the API. The incoming webhook implementation is not implemented: object reference and resource object lookups return `WebhooksNotImplemented`, and event typing returns `EventNotSupported`; see [`IncomingWebhook for Bambora`](https://github.com/juspay/hyperswitch/blob/d4e93b6e6dd39e45a8d5d8647b362f1bb8543946/crates/hyperswitch_connectors/src/connectors/bambora.rs#L821-L844).

### Source reference

Authentication and webhook behavior on this page is tied to Hyperswitch `d4e93b6e6dd39e45a8d5d8647b362f1bb8543946`. See [Bambora connector source](https://github.com/juspay/hyperswitch/blob/d4e93b6e6dd39e45a8d5d8647b362f1bb8543946/crates/hyperswitch_connectors/src/connectors/bambora.rs) and [Bambora transformers](https://github.com/juspay/hyperswitch/blob/d4e93b6e6dd39e45a8d5d8647b362f1bb8543946/crates/hyperswitch_connectors/src/connectors/bambora/transformers.rs).
