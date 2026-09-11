---
description: Configure PayU card and wallet payments with Hyperswitch.
metaLinks:
  alternates:
    - payu-1.md
---

# PayU

<div align="left"><img src="https://hyperswitch.io/icons/homePageIcons/logos/payuLogo.svg" alt=""></div>

PayU is a payment gateway for card and wallet payments through Hyperswitch. Its connector covers Apple Pay and Google Pay alongside credit and debit cards. Refunds and delayed capture use the same integration, while mandates are not declared for these methods.

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch a17a23c4c4c907d2314043a32a9f505f7f2bd4f9; host http://localhost:8080; fetched 2026-09-10; matrix canonical-json-v1 sha256 36360b019f2761dd; 138 connectors.
     Do not edit by hand. This block regenerates from the connector's
     SupportedPaymentMethods declaration in code; edit that instead. -->

**Integration status:** sandbox

**Category:** payment gateway

**Webhook flows:** None declared in code

| Payment method | Type | Mandates | Refunds | Capture methods | 3DS | Card networks | Countries | Currencies |
|---|---|---|---|---|---|---|---|---|
| card | Credit Card | not supported | supported | automatic, manual, sequential automatic | required | American Express, Cartes Bancaires, Diners Club, Discover, Interac, JCB, Mastercard, UnionPay, Visa | 134 ([full list](https://hyperswitch.io/pm-list)) | 134 ([full list](https://hyperswitch.io/pm-list)) |
| card | Debit Card | not supported | supported | automatic, manual, sequential automatic | required | American Express, Cartes Bancaires, Diners Club, Discover, Interac, JCB, Mastercard, UnionPay, Visa | 134 ([full list](https://hyperswitch.io/pm-list)) | 134 ([full list](https://hyperswitch.io/pm-list)) |
| wallet | Apple Pay | not supported | supported | automatic, manual, sequential automatic | not applicable | - | - | - |
| wallet | Google Pay | not supported | supported | automatic, manual, sequential automatic | not applicable | - | 46 ([full list](https://hyperswitch.io/pm-list)) | 53 ([full list](https://hyperswitch.io/pm-list)) |

To connect PayU to your Hyperswitch account, follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for what PayU supports.

### Connector-Specific Notes

PayU obtains an access token with a form-encoded client credentials request before it sends transaction requests. Hyperswitch manages this exchange, so configure the connector credentials rather than supplying an access token directly. See [`PayuAuthUpdateRequest`](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/payu/transformers.rs#L323-L336).

### Before you start

1. You need to be registered with PayU. Sign up at [corporate.payu.com](https://corporate.payu.com/).
2. You should have a registered Hyperswitch account, accessible from the [Hyperswitch control center](https://app.hyperswitch.io/).
3. Your PayU API Key and Merchant POS ID are in your PayU dashboard under My Shops.
4. Select all payment methods you wish to use PayU for, and make sure they match the ones configured in your PayU dashboard.

To connect PayU to your Hyperswitch account, follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for what PayU supports.

### Authentication

Provide an **API key** and **merchant POS ID**. The `BodyKey` auth mapping assigns `api_key` to the API key and `key1` to the merchant POS ID; the token request sends the merchant POS ID as `client_id` and the API key as `client_secret`. See [`PayuAuthType::try_from()`](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/payu/transformers.rs#L188-L203) and [`PayuAuthUpdateRequest::try_from()`](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/payu/transformers.rs#L323-L336).

Transaction requests use `Authorization: Bearer <access token>`. The connector's common auth path can also return `Authorization: <API key>`, while the transaction header builder requires the exchanged token. See [`build_headers()`](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/payu.rs#L70-L96) and [`get_auth_header()`](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/payu.rs#L112-L123).

### Webhooks

Webhooks are not currently supported. Payment status updates rely on syncing with the API. The webhook implementation returns `EventNotSupported` and does not provide a resource object. See [`get_webhook_event_type()`](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/payu.rs#L785-L808).

### Source reference

The connector implementation is [`payu.rs`](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/payu.rs).
