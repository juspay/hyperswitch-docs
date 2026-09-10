---
description: Accept card, bank transfer, wallet, and voucher payments through Zen.
metaLinks:
  alternates:
    - zen.md
---

# Zen

<div align="left"><img src="https://hyperswitch.io/img/site/zenLogo.svg" alt=""></div>

Zen is a payment gateway for cards, bank transfers, digital wallets, and voucher payments. Every declared method supports refunds and automatic, manual, or sequential automatic capture, but not mandates. Card payments run without 3DS, and webhooks cover payment and refund updates.

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch a17a23c4c4c907d2314043a32a9f505f7f2bd4f9; host http://localhost:8080; fetched 2026-09-10; matrix canonical-json-v1 sha256 36360b019f2761dd; 138 connectors.
     Do not edit by hand. This block regenerates from the connector's
     SupportedPaymentMethods declaration in code; edit that instead. -->

**Integration status:** live

**Category:** payment gateway

**Webhook flows:** payments, refunds

| Payment method | Type | Mandates | Refunds | Capture methods | 3DS | Card networks | Countries | Currencies |
|---|---|---|---|---|---|---|---|---|
| bank transfer | Multibanco | not supported | supported | automatic, manual, sequential automatic | not applicable | - | PRT | EUR |
| bank transfer | Pix | not supported | supported | automatic, manual, sequential automatic | not applicable | - | BRA | BRL |
| bank transfer | PSE | not supported | supported | automatic, manual, sequential automatic | not applicable | - | COL | COP |
| card | Credit Card | not supported | supported | automatic, manual, sequential automatic | not supported | American Express, Cartes Bancaires, Diners Club, Discover, Interac, JCB, Mastercard, UnionPay, Visa | - | - |
| card | Debit Card | not supported | supported | automatic, manual, sequential automatic | not supported | American Express, Cartes Bancaires, Diners Club, Discover, Interac, JCB, Mastercard, UnionPay, Visa | - | - |
| voucher | Boleto Bancário | not supported | supported | automatic, manual, sequential automatic | not applicable | - | BRA | BRL |
| voucher | Efecty | not supported | supported | automatic, manual, sequential automatic | not applicable | - | COL | COP |
| voucher | PagoEfectivo | not supported | supported | automatic, manual, sequential automatic | not applicable | - | PER | PEN |
| voucher | RedCompra | not supported | supported | automatic, manual, sequential automatic | not applicable | - | CHL | CLP |
| voucher | RedPagos | not supported | supported | automatic, manual, sequential automatic | not applicable | - | URY | UYU |
| wallet | Apple Pay | not supported | supported | automatic, manual, sequential automatic | not applicable | - | - | - |
| wallet | Google Pay | not supported | supported | automatic, manual, sequential automatic | not applicable | - | - | - |

### Authentication

Supply an API Key in the connector configuration. Hyperswitch sends `Authorization: Bearer <API key>` on connector requests. See [`ZenAuthType::try_from()`](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/zen/transformers.rs#L58-L73) and [`get_auth_header()`](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/zen.rs#L117-L127).

### Webhooks

Configure a webhook merchant secret in Hyperswitch; the shared webhook verifier uses that value as the signature key. See [`verify_webhook_source()`](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_interfaces/src/webhooks.rs#L266-L301). Zen webhooks carry a hex `hash` in the request body. Hyperswitch verifies a SHA-256 digest built from the merchant transaction ID, currency, amount, uppercased status, and the configured secret. See [`get_webhook_source_verification_algorithm()`](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/zen.rs#L561-L629).

The connector handles four transaction-type and status combinations:

| `type` | `status` | Effect in Hyperswitch |
|---|---|---|
| `TRT_PURCHASE` | `ACCEPTED` | Payment is marked successful |
| `TRT_PURCHASE` | `REJECTED` | Payment is marked failed |
| `TRT_REFUND` | `ACCEPTED` | Refund is marked successful |
| `TRT_REFUND` | `REJECTED` | Refund is marked failed |

The wire values and mappings are defined by [`get_webhook_event_type()`](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/zen.rs#L654-L676), [`ZenPaymentStatus`](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/zen/transformers.rs#L837-L847), and [`ZenWebhookTxnType`](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/zen/transformers.rs#L1186-L1202).

### Activate Zen with Hyperswitch

#### Before you start

1. Register with Zen.
2. Create a Hyperswitch account.
3. Have the credential listed in [Authentication](#authentication) ready.

To connect Zen to your Hyperswitch account, follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for what Zen supports.

### Source reference

[Zen connector implementation](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/zen.rs) and [Zen data mappings](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/zen/transformers.rs)
