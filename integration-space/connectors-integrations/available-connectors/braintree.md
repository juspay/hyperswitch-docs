---
description: >-
  Connect Braintree to Hyperswitch and review the connector setup.
metaLinks:
  alternates:
    - braintree.md
---

# Braintree

Use this guide to configure credentials and webhook behavior.

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch 93becbaee4ee3686e1a4d5750d2e547c56c27047; host http://localhost:8080; fetched 2026-09-10; matrix canonical-json-v1 sha256 27951de892af028b; 138 connectors.
     Do not edit by hand. This block regenerates from the connector's
     SupportedPaymentMethods declaration in code; edit that instead. -->

**Integration status:** live

**Category:** payment gateway

**Webhook flows:** payments, refunds

| Payment method | Type | Mandates | Refunds | Capture methods | 3DS | Card networks | Countries | Currencies |
|---|---|---|---|---|---|---|---|---|
| card | Credit Card | supported | supported | automatic, manual, sequential automatic | supported, optional | American Express, Discover, JCB, Mastercard, UnionPay, Visa | 45 ([full list](https://hyperswitch.io/pm-list)) | 134 ([full list](https://hyperswitch.io/pm-list)) |
| card | Debit Card | supported | supported | automatic, manual, sequential automatic | supported, optional | American Express, Discover, JCB, Mastercard, UnionPay, Visa | 45 ([full list](https://hyperswitch.io/pm-list)) | 134 ([full list](https://hyperswitch.io/pm-list)) |
| wallet | Apple Pay | supported | supported | automatic, manual, sequential automatic | not applicable | - | - | - |
| wallet | Google Pay | not supported | supported | automatic, manual, sequential automatic | not applicable | - | - | - |
| wallet | PayPal | not supported | supported | automatic, manual, sequential automatic | not applicable | - | - | - |

### Configure Braintree

Enter the Braintree public key in the API key field and the private key in the API secret field. Hyperswitch uses the public key as the HTTP Basic username and the private key as the HTTP Basic password. The shared third credential field is not used for Braintree authentication ([credential mapping](https://github.com/juspay/hyperswitch/blob/93becbaee4ee3686e1a4d5750d2e547c56c27047/crates/hyperswitch_connectors/src/connectors/braintree/transformers.rs#L215-L237), [request header](https://github.com/juspay/hyperswitch/blob/93becbaee4ee3686e1a4d5750d2e547c56c27047/crates/hyperswitch_connectors/src/connectors/braintree.rs#L136-L149)).

Follow the [connector activation guide](../activate-connector-on-hyperswitch/README.md) to add these credentials in Hyperswitch. Use Braintree's current dashboard guidance to find the credentials and register the webhook endpoint.

### Webhooks

Hyperswitch verifies Braintree webhook payloads with HMAC-SHA1. The handler reads the signature and encoded payload from the incoming form body ([source](https://github.com/juspay/hyperswitch/blob/93becbaee4ee3686e1a4d5750d2e547c56c27047/crates/hyperswitch_connectors/src/connectors/braintree.rs#L983-L1069)).

The implementation recognizes 7 dispute event names ([source](https://github.com/juspay/hyperswitch/blob/93becbaee4ee3686e1a4d5750d2e547c56c27047/crates/hyperswitch_connectors/src/connectors/braintree/transformers.rs#L2793-L2802)):

| Braintree event | Hyperswitch effect |
| --- | --- |
| `dispute_opened` | Dispute opened |
| `dispute_lost` | Dispute lost |
| `dispute_won` | Dispute won |
| `dispute_accepted` | Dispute accepted |
| `dispute_auto_accepted` | Dispute accepted |
| `dispute_expired` | Dispute expired |
| `dispute_disputed` | Dispute challenged |

Other event names are not supported.

### Page gaps

- The capability declaration lists payment and refund webhook flows, while the implemented event mapper recognizes dispute events. Confirm the intended declaration before relying on the generated webhook-flow list.
- The connector source does not declare the dashboard paths for finding credentials or registering the webhook endpoint. Use Braintree's current dashboard guidance when completing those steps.
