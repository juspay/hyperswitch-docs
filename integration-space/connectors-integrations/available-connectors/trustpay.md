---
description: >-
  Accept card, network token, bank redirect, bank transfer, and wallet payments
  through TrustPay.
metaLinks:
  alternates:
    - trustpay.md
---

# TrustPay

<div align="left"><img src="https://hyperswitch.io/icons/homePageIcons/logos/trustpayLogo.svg" alt=""></div>

TrustPay is a payment gateway for cards, network tokens, bank redirects, bank transfers, and digital wallets. Every declared method supports refunds and does not support mandates. Cards run without 3DS, while network tokens support optional 3DS. Webhooks cover payment, refund, and dispute updates.

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch a17a23c4c4c907d2314043a32a9f505f7f2bd4f9; host http://localhost:8080; fetched 2026-09-10; matrix canonical-json-v1 sha256 36360b019f2761dd; 138 connectors.
     Do not edit by hand. This block regenerates from the connector's
     SupportedPaymentMethods declaration in code; edit that instead. -->

**Integration status:** live

**Category:** payment gateway

**Webhook flows:** disputes, payments, refunds

| Payment method | Type | Mandates | Refunds | Capture methods | 3DS | Card networks | Countries | Currencies |
|---|---|---|---|---|---|---|---|---|
| bank redirect | BLIK | not supported | supported | automatic, sequential automatic | not applicable | - | - | - |
| bank redirect | EPS | not supported | supported | automatic, sequential automatic | not applicable | - | - | - |
| bank redirect | Giropay | not supported | supported | automatic, sequential automatic | not applicable | - | - | - |
| bank redirect | iDEAL | not supported | supported | automatic, sequential automatic | not applicable | - | - | - |
| bank redirect | Sofort | not supported | supported | automatic, sequential automatic | not applicable | - | - | - |
| bank transfer | Instant Bank Transfer | not supported | supported | automatic, sequential automatic | not applicable | - | AUT, CZE, DEU, GBR, ITA, SVK | CZK, EUR, GBP |
| bank transfer | Instant Bank Transfer Finland | not supported | supported | automatic, sequential automatic | not applicable | - | FIN | EUR |
| bank transfer | Instant Bank Transfer Poland | not supported | supported | automatic, sequential automatic | not applicable | - | POL | PLN |
| bank transfer | SEPA Bank Transfer | not supported | supported | automatic, sequential automatic | not applicable | - | - | - |
| card | Credit Card | not supported | supported | automatic, sequential automatic | not supported | American Express, Cartes Bancaires, Diners Club, Discover, Interac, JCB, Mastercard, UnionPay, Visa | - | - |
| card | Debit Card | not supported | supported | automatic, sequential automatic | not supported | American Express, Cartes Bancaires, Diners Club, Discover, Interac, JCB, Mastercard, UnionPay, Visa | - | - |
| network token | Network Token | not supported | supported | automatic, sequential automatic | supported, optional | American Express, Cartes Bancaires, Diners Club, Discover, Interac, JCB, Mastercard, UnionPay, Visa | - | - |
| wallet | Apple Pay | not supported | supported | automatic, sequential automatic | not applicable | - | - | - |
| wallet | Google Pay | not supported | supported | automatic, sequential automatic | not applicable | - | - | - |

### Authentication

Supply an API Key, Project ID, and Secret Key in the connector configuration. Card and wallet requests send `X-API-Key: <API key>`. Bank redirect and bank transfer flows first send `Authorization: Basic <base64 project ID and secret key>` to obtain an access token, then send `Authorization: Bearer <access token>` on payment requests. See [`TrustpayAuthType::try_from()`](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/trustpay/transformers.rs#L64-L87), [`build_headers()`](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/trustpay.rs#L84-L121), and [`RefreshTokenType::get_headers()`](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/trustpay.rs#L276-L302).

### Webhooks

Configure a webhook merchant secret in Hyperswitch; the shared webhook verifier uses that value as the signature key. See [`verify_webhook_source()`](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_interfaces/src/webhooks.rs#L266-L301). TrustPay webhooks use HMAC-SHA256 verification: Hyperswitch decodes the hex `signature` in the webhook body, removes that field, sorts the remaining values, and joins them with `/` before verification. See [`get_webhook_source_verification_algorithm()`](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/trustpay.rs#L1181-L1218).

The connector handles six status and credit/debit-indicator combinations. An empty body is treated as endpoint verification.

| `creditDebitIndicator` | `status` | Effect in Hyperswitch |
|---|---|---|
| `CRDT` | `Paid` | Payment is marked successful |
| `CRDT` | `Rejected` | Payment is marked failed |
| `DBIT` | `Paid` | Refund is marked successful |
| `DBIT` | `Refunded` | Refund is marked successful |
| `DBIT` | `Rejected` | Refund is marked failed |
| `DBIT` | `Chargebacked` | Dispute is marked lost |

The wire values and mappings are defined by [`get_webhook_event_type()`](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/trustpay.rs#L1111-L1167) and [`CreditDebitIndicator`](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/trustpay/transformers.rs#L2074-L2091).

### Activate TrustPay with Hyperswitch

#### Before you start

1. Register with TrustPay.
2. Create a Hyperswitch account.
3. Have the credentials listed in [Authentication](#authentication) ready.

To connect TrustPay to your Hyperswitch account, follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for what TrustPay supports.

### Source reference

[TrustPay connector implementation](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/trustpay.rs) and [TrustPay data mappings](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/trustpay/transformers.rs)
