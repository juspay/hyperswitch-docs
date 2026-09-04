---
description: >-
  Connect NMI to Hyperswitch as a live payment gateway.
---

# NMI

NMI connects to Hyperswitch as a live payment gateway. Payment methods, card networks, countries, currencies, capture methods, refunds, mandates, 3DS support and webhook flow classes are listed below.

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch d3c487e91c4f492e8839838966cce47ff12dc648; host http://localhost:8080; fetched 2026-09-04; matrix canonical-json-v1 sha256 27951de892af028b; 138 connectors.
     Do not edit by hand. This block regenerates from the connector's
     SupportedPaymentMethods declaration in code; edit that instead. -->

**Integration status:** live  
**Category:** payment gateway  
**Webhook flows:** payments, refunds

| Payment method | Type | Mandates | Refunds | Capture methods | 3DS | Card networks | Countries | Currencies |
|---|---|---|---|---|---|---|---|---|
| card | Credit Card | supported | supported | automatic, manual, sequential automatic | supported, optional | American Express, Cartes Bancaires, Diners Club, Discover, Interac, JCB, Maestro, Mastercard, UnionPay, Visa | 98 ([full list](https://hyperswitch.io/pm-list)) | 160 ([full list](https://hyperswitch.io/pm-list)) |
| card | Debit Card | supported | supported | automatic, manual, sequential automatic | supported, optional | American Express, Cartes Bancaires, Diners Club, Discover, Interac, JCB, Maestro, Mastercard, UnionPay, Visa | 98 ([full list](https://hyperswitch.io/pm-list)) | 160 ([full list](https://hyperswitch.io/pm-list)) |
| wallet | Apple Pay | supported | supported | automatic, manual, sequential automatic | not applicable | - | 96 ([full list](https://hyperswitch.io/pm-list)) | 160 ([full list](https://hyperswitch.io/pm-list)) |
| wallet | Google Pay | supported | supported | automatic, manual, sequential automatic | not applicable | - | 96 ([full list](https://hyperswitch.io/pm-list)) | 160 ([full list](https://hyperswitch.io/pm-list)) |

### Webhooks

NMI declares payments and refunds webhook flows. The connector handles these 10 webhook event names from `NmiWebhookEventType` at this SHA:

- `transaction.auth.failure`
- `transaction.auth.success`
- `transaction.capture.failure`
- `transaction.capture.success`
- `transaction.refund.failure`
- `transaction.refund.success`
- `transaction.sale.failure`
- `transaction.sale.success`
- `transaction.void.failure`
- `transaction.void.success`

`transaction.auth.unknown`, `transaction.capture.unknown`, `transaction.refund.unknown`, `transaction.sale.unknown` and `transaction.void.unknown` are acknowledged as `EventNotSupported`. Unknown events are also acknowledged as `EventNotSupported`. Event names are defined in [`NmiWebhookEventType`](https://github.com/juspay/hyperswitch/blob/d3c487e91c4f492e8839838966cce47ff12dc648/crates/hyperswitch_connectors/src/connectors/nmi/transformers.rs#L1791-L1825), and mapped by [`get_nmi_webhook_event`](https://github.com/juspay/hyperswitch/blob/d3c487e91c4f492e8839838966cce47ff12dc648/crates/hyperswitch_connectors/src/connectors/nmi/transformers.rs#L1827-L1851). Source verification uses `HmacSha256`, reads `webhook-signature`, extracts `t` and `s`, hex-decodes `s`, and verifies the message as `t.body` in [`IncomingWebhook for Nmi`](https://github.com/juspay/hyperswitch/blob/d3c487e91c4f492e8839838966cce47ff12dc648/crates/hyperswitch_connectors/src/connectors/nmi.rs#L943-L1001).

### Source reference

Connector implementation: [`crates/hyperswitch_connectors/src/connectors/nmi.rs`](https://github.com/juspay/hyperswitch/blob/d3c487e91c4f492e8839838966cce47ff12dc648/crates/hyperswitch_connectors/src/connectors/nmi.rs).
