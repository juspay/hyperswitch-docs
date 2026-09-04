---
description: >-
  Accept UPI Collect payments in India through Razorpay on Hyperswitch.
---

# Razorpay

Razorpay brings UPI Collect payments to Hyperswitch for merchants in India, with INR settlement and refund support. The integration is in sandbox; mandates are not supported.

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

Razorpay webhooks are not currently supported; Hyperswitch does not process incoming Razorpay webhook notifications, so payment and refund status updates rely on syncing with the API; configuring a Razorpay webhook endpoint has no effect.

The capability block lists payments and refunds webhook flows for this connector, but the webhook handler is not implemented, keeping this page aligned with the code in [`IncomingWebhook for Razorpay`](https://github.com/juspay/hyperswitch/blob/d3c487e91c4f492e8839838966cce47ff12dc648/crates/hyperswitch_connectors/src/connectors/razorpay.rs#L772-L795).

### Source reference

Connector implementation: [`crates/hyperswitch_connectors/src/connectors/razorpay.rs`](https://github.com/juspay/hyperswitch/blob/d3c487e91c4f492e8839838966cce47ff12dc648/crates/hyperswitch_connectors/src/connectors/razorpay.rs).
