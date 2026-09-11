---
description: >-
  Accept card and wallet payments through Braintree with Hyperswitch.
metaLinks:
  alternates:
    - braintree.md
---

# Braintree

Braintree is a PayPal service for accepting payments in apps and websites. Merchants can accept cards with mandates, refunds, manual capture, and optional 3DS. Apple Pay, Google Pay, and PayPal are also available, with mandates supported for Apple Pay. Webhooks cover payment and refund updates, and the webhook mapper also recognizes several dispute events (see below).

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

### Authentication

Supply the Public Key and Private Key in the connector configuration. Hyperswitch uses the Public Key as the HTTP Basic username and the Private Key as the password, then Base64-encodes `public_key:private_key`. The shared third credential field is not used for Braintree authentication. See [`BraintreeAuthType::try_from()`](https://github.com/juspay/hyperswitch/blob/740e642eabb5b54094f589d4ebc08aa9e796fab1/crates/hyperswitch_connectors/src/connectors/braintree/transformers.rs#L215-L237) and [`get_auth_header()`](https://github.com/juspay/hyperswitch/blob/740e642eabb5b54094f589d4ebc08aa9e796fab1/crates/hyperswitch_connectors/src/connectors/braintree.rs#L136-L149).

### Before you start

1. Register with Braintree.
2. Create or sign in to your account in the [Hyperswitch control center](https://app.hyperswitch.io/).
3. In the Braintree dashboard, go to **Home → Settings → API** to find the Public Key and Private Key.
4. Under **Home → Settings → API → Webhooks**, register the Hyperswitch webhook endpoint.
5. Have the credentials listed in [Authentication](#authentication) ready.

To connect Braintree to your Hyperswitch account, follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for what Braintree supports.

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
