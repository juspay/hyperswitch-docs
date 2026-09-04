---
description: >-
  Connect RAZORPAY to Hyperswitch as a sandbox payment gateway.
---

# RAZORPAY

RAZORPAY connects to Hyperswitch as a sandbox payment gateway. Payment methods, card networks, countries, currencies, capture methods, refunds, mandates, 3DS support and webhook flow classes are listed below.

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch d3c487e91c4f492e8839838966cce47ff12dc648; host http://localhost:8080; fetched 2026-09-04; matrix canonical-json-v1 sha256 27951de892af028b; 138 connectors.
     Do not edit by hand. This block regenerates from the connector's
     SupportedPaymentMethods declaration in code; edit that instead. -->

**Integration status:** sandbox  
**Category:** payment gateway  
**Webhook flows:** payments, refunds

| Payment method | Type | Mandates | Refunds | Capture methods | Countries | Currencies |
|---|---|---|---|---|---|---|
| upi | UPI Collect | not supported | supported | automatic | IND | INR |

### Webhooks

Razorpay declares payments and refunds webhook flows, but the active webhook handler does not process event names at this SHA. `get_webhook_event_type()` returns `EventNotSupported`, and the object and resource methods return `WebhooksNotImplemented` in [`IncomingWebhook for Razorpay`](https://github.com/juspay/hyperswitch/blob/d3c487e91c4f492e8839838966cce47ff12dc648/crates/hyperswitch_connectors/src/connectors/razorpay.rs#L772-L795).

### Source reference

Connector implementation: [`crates/hyperswitch_connectors/src/connectors/razorpay.rs`](https://github.com/juspay/hyperswitch/blob/d3c487e91c4f492e8839838966cce47ff12dc648/crates/hyperswitch_connectors/src/connectors/razorpay.rs).
