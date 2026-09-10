---
description: Configure dLocal card and voucher payments with Hyperswitch.
metaLinks:
  alternates:
    - dlocal.md
---

# dLocal

<div align="left"><img src="https://hyperswitch.io/icons/homePageIcons/logos/dlocalLogo.svg" alt=""></div>

dLocal is a payment gateway for card and voucher payments through Hyperswitch. Its connector covers credit and debit cards alongside OXXO vouchers. Card payments support delayed capture, while the voucher path uses automatic capture. Refunds are declared for each method, and mandates are not declared.

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch a17a23c4c4c907d2314043a32a9f505f7f2bd4f9; host http://localhost:8080; fetched 2026-09-10; matrix canonical-json-v1 sha256 36360b019f2761dd; 138 connectors.
     Do not edit by hand. This block regenerates from the connector's
     SupportedPaymentMethods declaration in code; edit that instead. -->

**Integration status:** sandbox

**Category:** payment gateway

**Webhook flows:** None declared in code

| Payment method | Type | Mandates | Refunds | Capture methods | 3DS | Card networks | Countries | Currencies |
|---|---|---|---|---|---|---|---|---|
| card | Credit Card | not supported | supported | automatic, manual, sequential automatic | supported, optional | American Express, Cartes Bancaires, Diners Club, Discover, Interac, JCB, Mastercard, UnionPay, Visa | - | - |
| card | Debit Card | not supported | supported | automatic, manual, sequential automatic | supported, optional | American Express, Cartes Bancaires, Diners Club, Discover, Interac, JCB, Mastercard, UnionPay, Visa | - | - |
| voucher | OXXO | not supported | supported | automatic | not applicable | - | - | MXN |

To connect dLocal to your Hyperswitch account, follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for what dLocal supports.

### Connector-Specific Notes

Each API request is signed with HMAC-SHA256. For an empty body, Hyperswitch concatenates the login and request date with no delimiter. Otherwise it concatenates the login, request date, and request body in that order with no delimiter. It hex-encodes the signature and sends `Authorization: V2-HMAC-SHA256, Signature: <hex signature>`. See [`build_headers()`](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/dlocal.rs#L82-L133).

### Authentication

Provide a `<login>`, `<transaction key>`, and `<secret key>`. The `SignatureKey` mapping assigns `api_key` to the login, `key1` to the transaction key, and `api_secret` to the secret key. The login and transaction key are also sent separately as `X-Login: <login>` and `X-Trans-Key: <transaction key>`; the secret key is the HMAC key and is not sent as a header value. See [`DlocalAuthType::try_from()`](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/dlocal/transformers.rs#L225-L249) and [`build_headers()`](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/dlocal.rs#L82-L133).

### Webhooks

Webhooks are not currently supported. Payment status updates rely on syncing with the API. The webhook implementation returns `EventNotSupported` and does not provide a resource object. See [`get_webhook_event_type()`](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/dlocal.rs#L692-L715).

### Source reference

The connector implementation is [`dlocal.rs`](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/dlocal.rs).
