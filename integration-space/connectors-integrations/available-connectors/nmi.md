---
description: >-
  Accept card and wallet payments through NMI on Hyperswitch, with mandates, refunds, and manual capture.
---

# NMI

NMI handles card payments and Apple Pay and Google Pay wallets through Hyperswitch, with mandates, refunds, and manual capture across the board, and optional 3DS on cards. The integration is live.

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

Use NMI webhooks to keep payment and refund statuses updated in Hyperswitch after NMI sends transaction updates. Keep webhooks enabled for the Hyperswitch endpoint used by your account. See your NMI account settings for where to configure the endpoint.

NMI handles 10 event names that follow `transaction.<type>.<result>`, where `<type>` is `sale`, `auth`, `capture`, `void`, or `refund`, and `<result>` is `success` or `failure`.

| NMI event | Effect in Hyperswitch |
|---|---|
| `transaction.auth.failure` | Payment authorization fails |
| `transaction.auth.success` | Payment authorization succeeds |
| `transaction.capture.failure` | Payment capture fails |
| `transaction.capture.success` | Payment capture succeeds |
| `transaction.refund.failure` | Refund fails |
| `transaction.refund.success` | Refund succeeds |
| `transaction.sale.failure` | Payment fails |
| `transaction.sale.success` | Payment succeeds |
| `transaction.void.failure` | Payment cancellation fails |
| `transaction.void.success` | Payment is cancelled |

Any other event, including the `unknown` variants, is acknowledged without changing a status. Event names are defined in [`NmiWebhookEventType`](https://github.com/juspay/hyperswitch/blob/d3c487e91c4f492e8839838966cce47ff12dc648/crates/hyperswitch_connectors/src/connectors/nmi/transformers.rs#L1791-L1825), and mapped by [`get_nmi_webhook_event`](https://github.com/juspay/hyperswitch/blob/d3c487e91c4f492e8839838966cce47ff12dc648/crates/hyperswitch_connectors/src/connectors/nmi/transformers.rs#L1827-L1851).

Hyperswitch verifies the `webhook-signature` header before processing NMI webhooks in [`IncomingWebhook for Nmi`](https://github.com/juspay/hyperswitch/blob/d3c487e91c4f492e8839838966cce47ff12dc648/crates/hyperswitch_connectors/src/connectors/nmi.rs#L943-L1001).

### Source reference

Connector implementation: [`crates/hyperswitch_connectors/src/connectors/nmi.rs`](https://github.com/juspay/hyperswitch/blob/d3c487e91c4f492e8839838966cce47ff12dc648/crates/hyperswitch_connectors/src/connectors/nmi.rs).
