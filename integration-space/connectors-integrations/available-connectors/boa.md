---
description: >-
  Accept card and wallet payments through Bank of America with signed API requests.
metaLinks:
  alternates:
    - boa.md
---

# Bank of America

Bank of America covers card payments and several wallet paths. Most declared methods can be reused with mandates, while one wallet remains limited to one-time use. Refunds and delayed capture options are available across the declared checkout paths.

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch 184ffd4c015fd3fea2f3868549f1a86ffa5f40da; host http://localhost:8080; fetched 2026-09-16; matrix canonical-json-v1 sha256 02ce435bc7059143; 140 connectors.
     Do not edit by hand. Payment method rows regenerate from the
     connector's SupportedPaymentMethods declaration; countries and
     currencies come from pm_filters in config/development.toml.
     Webhook flows and capture methods are reconciled against
     implemented flows. Edit those sources instead. -->

**Integration status:** live

**Category:** bank acquirer

**Webhook flows:** None declared in code

| Payment method | Type | Mandates | Refunds | Capture methods | 3DS | Card networks | Countries | Currencies |
|---|---|---|---|---|---|---|---|---|
| card | Credit Card | supported | supported | automatic, manual, sequential automatic | not supported | American Express, Cartes Bancaires, Diners Club, Discover, Interac, JCB, Maestro, Mastercard, UnionPay, Visa | 216 ([full list](https://hyperswitch.io/pm-list)) | USD |
| card | Debit Card | supported | supported | automatic, manual, sequential automatic | not supported | American Express, Cartes Bancaires, Diners Club, Discover, Interac, JCB, Maestro, Mastercard, UnionPay, Visa | 216 ([full list](https://hyperswitch.io/pm-list)) | USD |
| wallet | Apple Pay | supported | supported | automatic, manual, sequential automatic | not applicable | - | 72 ([full list](https://hyperswitch.io/pm-list)) | USD |
| wallet | Google Pay | supported | supported | automatic, manual, sequential automatic | not applicable | - | 66 ([full list](https://hyperswitch.io/pm-list)) | USD |
| wallet | Samsung Pay | not supported | supported | automatic, manual, sequential automatic | not applicable | - | 31 ([full list](https://hyperswitch.io/pm-list)) | USD |

### Authentication

Bank of America requires **API Key**, **Merchant ID**, and **Shared Secret**. Hyperswitch builds a newline-delimited signing string from the host, date, request target, an optional body digest, and Merchant ID; it signs that string with HMAC-SHA256 using the Base64-decoded Shared Secret. The API Key becomes `keyid` in the `Signature` header, while Merchant ID is also sent in `v-c-merchant-id`. See [`BankOfAmericaAuthType::try_from()`](https://github.com/juspay/hyperswitch/blob/d4e93b6e6dd39e45a8d5d8647b362f1bb8543946/crates/hyperswitch_connectors/src/connectors/bankofamerica/transformers.rs#L47-L65) and [`generate_signature()`](https://github.com/juspay/hyperswitch/blob/d4e93b6e6dd39e45a8d5d8647b362f1bb8543946/crates/hyperswitch_connectors/src/connectors/bankofamerica.rs#L97-L137).

### Before you start

1. Register through the [Bank of America developer portal](https://developer.cybersource.com/hello-world/sandbox.html).
2. Sign in to the [Hyperswitch control center](https://app.hyperswitch.io/).
3. Obtain the **Merchant ID** from the dashboard and generate the **API Key** and **Shared Secret** under **Payment Configuration → Key Management**.
4. If the activation flow asks you to select payment methods, choose only the methods enabled in the connector dashboard.

Follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for Bank of America-specific behavior.

### Webhooks

Handled event wire values: **0**. Webhooks are not currently supported, so status updates rely on syncing through the API. The incoming webhook implementation is not implemented: object reference and resource object lookups return `WebhooksNotImplemented`, and event typing returns `EventNotSupported`; see [`IncomingWebhook for Bankofamerica`](https://github.com/juspay/hyperswitch/blob/d4e93b6e6dd39e45a8d5d8647b362f1bb8543946/crates/hyperswitch_connectors/src/connectors/bankofamerica.rs#L1054-L1077).

### Source reference

Authentication and webhook behavior on this page is tied to Hyperswitch `d4e93b6e6dd39e45a8d5d8647b362f1bb8543946`. See [Bank of America connector source](https://github.com/juspay/hyperswitch/blob/d4e93b6e6dd39e45a8d5d8647b362f1bb8543946/crates/hyperswitch_connectors/src/connectors/bankofamerica.rs) and [Bank of America transformers](https://github.com/juspay/hyperswitch/blob/d4e93b6e6dd39e45a8d5d8647b362f1bb8543946/crates/hyperswitch_connectors/src/connectors/bankofamerica/transformers.rs).
