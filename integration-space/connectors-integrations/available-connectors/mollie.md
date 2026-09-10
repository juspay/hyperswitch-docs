---
description: Configure Mollie card, wallet, bank debit, bank redirect, and pay later payments with Hyperswitch.
metaLinks:
  alternates:
    - mollie.md
---

# Mollie

<div align="left"><img src="https://hyperswitch.io/icons/homePageIcons/logos/mollieLogo.svg" alt=""></div>

Mollie is a payment gateway for card, wallet, bank debit, bank redirect, and pay later payments through Hyperswitch. Its connector covers Apple Pay and PayPal alongside several European bank payment methods. Card payments can use mandates, while the other declared methods do not. Refunds and delayed capture are available across the declared methods.

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch a17a23c4c4c907d2314043a32a9f505f7f2bd4f9; host http://localhost:8080; fetched 2026-09-10; matrix canonical-json-v1 sha256 36360b019f2761dd; 138 connectors.
     Do not edit by hand. This block regenerates from the connector's
     SupportedPaymentMethods declaration in code; edit that instead. -->

**Integration status:** sandbox

**Category:** payment gateway

**Webhook flows:** None declared in code

| Payment method | Type | Mandates | Refunds | Capture methods | 3DS | Card networks | Countries | Currencies |
|---|---|---|---|---|---|---|---|---|
| bank debit | SEPA Direct Debit | not supported | supported | automatic, sequential automatic, manual | not applicable | - | - | - |
| bank redirect | Bancontact Card | not supported | supported | automatic, sequential automatic, manual | not applicable | - | - | - |
| bank redirect | EPS | not supported | supported | automatic, sequential automatic, manual | not applicable | - | AUT | EUR |
| bank redirect | Giropay | not supported | supported | automatic, sequential automatic, manual | not applicable | - | - | - |
| bank redirect | iDEAL | not supported | supported | automatic, sequential automatic, manual | not applicable | - | NLD | EUR |
| bank redirect | Przelewy24 | not supported | supported | automatic, sequential automatic, manual | not applicable | - | POL | EUR, PLN |
| bank redirect | Sofort | not supported | supported | automatic, sequential automatic, manual | not applicable | - | - | - |
| card | Credit Card | supported | supported | automatic, sequential automatic, manual | supported, optional | American Express, Cartes Bancaires, Diners Club, Discover, Interac, JCB, Mastercard, UnionPay, Visa | - | - |
| card | Debit Card | supported | supported | automatic, sequential automatic, manual | supported, optional | American Express, Cartes Bancaires, Diners Club, Discover, Interac, JCB, Mastercard, UnionPay, Visa | - | - |
| pay later | Klarna | not supported | supported | automatic, sequential automatic, manual | not applicable | - | 19 ([full list](https://hyperswitch.io/pm-list)) | 8 ([full list](https://hyperswitch.io/pm-list)) |
| wallet | Apple Pay | not supported | supported | automatic, sequential automatic, manual | not applicable | - | - | - |
| wallet | PayPal | not supported | supported | automatic, sequential automatic, manual | not applicable | - | - | - |

To connect Mollie to your Hyperswitch account, follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for what Mollie supports.

### Connector-Specific Notes

Card tokenization requires the profile token in addition to the API key. Hyperswitch places the profile token in the tokenization request body. See [`MollieCardTokenRequest::try_from()`](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/mollie/transformers.rs#L623-L665).

### Authentication

Mollie accepts two credential paths. Provide an `<API key>` for the `HeaderKey` path. For card tokenization, provide an `<API key>` and `<profile token>` through the `BodyKey` path, where `key1` maps to the profile token. Both paths send `Authorization: Bearer <API key>`; the profile token is carried in the tokenization body rather than the authorization header. See [`MollieAuthType::try_from()`](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/mollie/transformers.rs#L828-L848), [`get_auth_header()`](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/mollie.rs#L108-L119), and [`MollieCardTokenRequest::try_from()`](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/mollie/transformers.rs#L623-L665).

### Webhooks

The feature matrix declares no webhook flows, but the connector processes a payment resource callback. The callback body has an `id` field and no event-name field, so there is no separate wire event value to configure. Source verification currently returns `false`, so the callback is not accepted as verified by this implementation. See [`MollieWebhookBody`](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/mollie/transformers.rs#L1073-L1076) and [`verify_webhook_source()`](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/mollie.rs#L837-L849).

The connector maps 1 callback shape:

| Wire field | Effect |
|---|---|
| `id` | Payment is marked processing |

The mapping is defined by [`get_webhook_event_type()`](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/mollie.rs#L850-L867).

### Source reference

The connector implementation is [`mollie.rs`](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/mollie.rs).
