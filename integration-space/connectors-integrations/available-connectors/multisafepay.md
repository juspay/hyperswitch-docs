---
description: >-
  Accept card, bank redirect, pay-later, and wallet payments through MultiSafepay.
metaLinks:
  alternates:
    - multisafepay.md
---

# MultiSafepay

MultiSafepay brings several checkout families into one connector, including cards, bank redirects, wallets, and pay-later payments. Some paths can be reused with mandates, while others remain one-time checkout options. Refund handling is available across the declared methods.

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch d4e93b6e6dd39e45a8d5d8647b362f1bb8543946; host http://localhost:8080; fetched 2026-09-14; matrix canonical-json-v1 sha256 1beab3d720a6bcc5; 138 connectors.
     Do not edit by hand. This block regenerates from the connector's
     SupportedPaymentMethods declaration in code; edit that instead. -->

**Integration status:** sandbox

**Category:** payment gateway

**Webhook flows:** None declared in code

| Payment method | Type | Mandates | Refunds | Capture methods | 3DS | Card networks | Countries | Currencies |
|---|---|---|---|---|---|---|---|---|
| bank redirect | EPS | not supported | supported | automatic, sequential automatic | not applicable | - | AUT | EUR |
| bank redirect | Giropay | not supported | supported | automatic, sequential automatic | not applicable | - | DEU | EUR |
| bank redirect | iDEAL | not supported | supported | automatic, sequential automatic | not applicable | - | NLD | EUR |
| bank redirect | Sofort | not supported | supported | automatic, sequential automatic | not applicable | - | 9 ([full list](https://hyperswitch.io/pm-list)) | EUR |
| bank redirect | Trustly | not supported | supported | automatic, sequential automatic | not applicable | - | 15 ([full list](https://hyperswitch.io/pm-list)) | EUR, GBP, SEK |
| card | Credit Card | supported | supported | automatic, sequential automatic | required | American Express, Cartes Bancaires, Maestro, Mastercard, Visa | 249 ([full list](https://hyperswitch.io/pm-list)) | 34 ([full list](https://hyperswitch.io/pm-list)) |
| card | Debit Card | supported | supported | automatic, sequential automatic | required | American Express, Cartes Bancaires, Maestro, Mastercard, Visa | 249 ([full list](https://hyperswitch.io/pm-list)) | 34 ([full list](https://hyperswitch.io/pm-list)) |
| pay later | Klarna | not supported | supported | automatic, sequential automatic | not applicable | - | 13 ([full list](https://hyperswitch.io/pm-list)) | DKK, EUR, GBP, NOK, SEK |
| wallet | Alipay | not supported | supported | automatic, sequential automatic | not applicable | - | - | EUR, USD |
| wallet | Google Pay | supported | supported | automatic, sequential automatic | not applicable | - | 75 ([full list](https://hyperswitch.io/pm-list)) | 34 ([full list](https://hyperswitch.io/pm-list)) |
| wallet | MB WAY | not supported | supported | automatic, sequential automatic | not applicable | - | PRT | EUR |
| wallet | PayPal | not supported | supported | automatic, sequential automatic | not applicable | - | 249 ([full list](https://hyperswitch.io/pm-list)) | 25 ([full list](https://hyperswitch.io/pm-list)) |
| wallet | WeChat Pay | not supported | supported | automatic, sequential automatic | not applicable | - | - | EUR |


### Authentication

MultiSafepay requires an **API Key**. Hyperswitch sends it as an `api_key` query parameter in every request URL rather than as a header. See [`MultisafepayAuthType::try_from()`](https://github.com/juspay/hyperswitch/blob/d4e93b6e6dd39e45a8d5d8647b362f1bb8543946/crates/hyperswitch_connectors/src/connectors/multisafepay/transformers.rs#L821-L832), [`build_headers()`](https://github.com/juspay/hyperswitch/blob/d4e93b6e6dd39e45a8d5d8647b362f1bb8543946/crates/hyperswitch_connectors/src/connectors/multisafepay.rs#L68-L77), and the URL construction in [`payments_sync()`](https://github.com/juspay/hyperswitch/blob/d4e93b6e6dd39e45a8d5d8647b362f1bb8543946/crates/hyperswitch_connectors/src/connectors/multisafepay.rs#L196).

### Before you start

1. Register with MultiSafepay at [multisafepay.com](https://www.multisafepay.com/).
2. Sign in to the [Hyperswitch control center](https://app.hyperswitch.io/).
3. Obtain the **API Key** under **Integrations → Site** in the MultiSafepay dashboard.
4. Enable the same payment methods in MultiSafepay and in your Hyperswitch connector configuration.

Follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for MultiSafepay-specific behavior.

### Webhooks

Handled event wire values: **0**. Webhooks are not currently supported, so status updates rely on syncing through the API. Object-reference and resource-object lookups return `WebhooksNotImplemented`, while event typing returns `EventNotSupported`; see [`IncomingWebhook for Multisafepay`](https://github.com/juspay/hyperswitch/blob/d4e93b6e6dd39e45a8d5d8647b362f1bb8543946/crates/hyperswitch_connectors/src/connectors/multisafepay.rs#L525-L548).

### Source reference

Authentication and webhook behavior on this page is tied to Hyperswitch `d4e93b6e6dd39e45a8d5d8647b362f1bb8543946`. See [MultiSafepay connector source](https://github.com/juspay/hyperswitch/blob/d4e93b6e6dd39e45a8d5d8647b362f1bb8543946/crates/hyperswitch_connectors/src/connectors/multisafepay.rs) and [MultiSafepay transformers](https://github.com/juspay/hyperswitch/blob/d4e93b6e6dd39e45a8d5d8647b362f1bb8543946/crates/hyperswitch_connectors/src/connectors/multisafepay/transformers.rs).
