---
description: >-
  Accept card payments through Billwerk using private and public API credentials.
metaLinks:
  alternates:
    - billwerk.md
---

# Billwerk

Billwerk connects subscription commerce to card payment processing. Both credit and debit card paths support refunds. Merchants can choose between immediate and delayed capture patterns for those transactions.

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch d4e93b6e6dd39e45a8d5d8647b362f1bb8543946; host http://localhost:8080; fetched 2026-09-14; matrix canonical-json-v1 sha256 1beab3d720a6bcc5; 138 connectors.
     Do not edit by hand. This block regenerates from the connector's
     SupportedPaymentMethods declaration in code; edit that instead. -->

**Integration status:** sandbox

**Category:** payment gateway

**Webhook flows:** None declared in code

| Payment method | Type | Mandates | Refunds | Capture methods | 3DS | Card networks | Countries | Currencies |
|---|---|---|---|---|---|---|---|---|
| card | Credit Card | not supported | supported | automatic, manual, sequential automatic | not supported | American Express, Cartes Bancaires, Diners Club, Discover, Interac, JCB, Mastercard, UnionPay, Visa | DEU, DNK, FRA, SWE | DKK, NOK |
| card | Debit Card | not supported | supported | automatic, manual, sequential automatic | not supported | American Express, Cartes Bancaires, Diners Club, Discover, Interac, JCB, Mastercard, UnionPay, Visa | DEU, DNK, FRA, SWE | DKK, NOK |


### Authentication

Billwerk requires **Private API Key** and **Public API Key**. For authenticated API requests, Hyperswitch constructs `<Private API Key>:` with an empty value after the colon, Base64-encodes it, and sends `Authorization: Basic <encoded value>`. The Public API Key is placed in the tokenization request as `pkey`. See [`BillwerkAuthType::try_from()`](https://github.com/juspay/hyperswitch/blob/d4e93b6e6dd39e45a8d5d8647b362f1bb8543946/crates/hyperswitch_connectors/src/connectors/billwerk/transformers.rs#L50-L61), [`get_auth_header()`](https://github.com/juspay/hyperswitch/blob/d4e93b6e6dd39e45a8d5d8647b362f1bb8543946/crates/hyperswitch_connectors/src/connectors/billwerk.rs#L124-L136), and [`BillwerkTokenRequest::try_from()`](https://github.com/juspay/hyperswitch/blob/d4e93b6e6dd39e45a8d5d8647b362f1bb8543946/crates/hyperswitch_connectors/src/connectors/billwerk/transformers.rs#L90-L104).

### Webhooks

Handled event wire values: **0**. Webhooks are not currently supported, so status updates rely on syncing through the API. The incoming webhook implementation returns `WebhooksNotImplemented`; see [`IncomingWebhook for Billwerk`](https://github.com/juspay/hyperswitch/blob/d4e93b6e6dd39e45a8d5d8647b362f1bb8543946/crates/hyperswitch_connectors/src/connectors/billwerk.rs#L799-L822).

### Activate Billwerk with Hyperswitch

#### Before you start

1. Register with Billwerk+ Pay at [signup.billwerk.plus](https://signup.billwerk.plus/).
2. Sign in to the [Hyperswitch control center](https://app.hyperswitch.io/).
3. Obtain the **Private API Key** and **Public API Key** under **Developers → API Credentials** in the Billwerk+ Pay dashboard.
4. If the activation flow asks you to select payment methods, choose only the methods enabled in the connector dashboard.

Follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for Billwerk-specific behavior.

### Source reference

Authentication and webhook behavior on this page is tied to Hyperswitch `d4e93b6e6dd39e45a8d5d8647b362f1bb8543946`. See [Billwerk connector source](https://github.com/juspay/hyperswitch/blob/d4e93b6e6dd39e45a8d5d8647b362f1bb8543946/crates/hyperswitch_connectors/src/connectors/billwerk.rs) and [Billwerk transformers](https://github.com/juspay/hyperswitch/blob/d4e93b6e6dd39e45a8d5d8647b362f1bb8543946/crates/hyperswitch_connectors/src/connectors/billwerk/transformers.rs).
