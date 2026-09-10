---
description: >-
  Accept card and wallet payments.
metaLinks:
  alternates:
    - authorizedotnet.md
---

# Authorize.net

Authorize.net is an online payment provider. Its card and selected wallet methods can be used for recurring charges, while PayPal mandates are not declared. Payments can be captured automatically, manually, or through sequential automatic capture, with payment and refund webhook flows available.

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch 2ef1f9ee5bdf65356c3169f4f5db67fa1d4de7bc; host http://localhost:8080; fetched 2026-09-10; matrix canonical-json-v1 sha256 36360b019f2761dd; 138 connectors.
     Do not edit by hand. This block regenerates from the connector's
     SupportedPaymentMethods declaration in code; edit that instead. -->

**Integration status:** live

**Category:** payment gateway

**Webhook flows:** payments, refunds

| Payment method | Type | Mandates | Refunds | Capture methods | 3DS | Card networks | Countries | Currencies |
|---|---|---|---|---|---|---|---|---|
| card | Credit Card | supported | supported | automatic, manual, sequential automatic | not supported | American Express, Discover, JCB, Mastercard, Visa | - | CAD, USD |
| card | Debit Card | supported | supported | automatic, manual, sequential automatic | not supported | American Express, Discover, JCB, Mastercard, Visa | - | CAD, USD |
| wallet | Apple Pay | supported | supported | automatic, manual, sequential automatic | not applicable | - | - | 44 ([full list](https://hyperswitch.io/pm-list)) |
| wallet | Google Pay | supported | supported | automatic, manual, sequential automatic | not applicable | - | - | 11 ([full list](https://hyperswitch.io/pm-list)) |
| wallet | PayPal | not supported | supported | automatic, manual, sequential automatic | not applicable | - | - | 24 ([full list](https://hyperswitch.io/pm-list)) |

### Authentication

Supply the API Login ID and Transaction Key in the connector configuration. Hyperswitch maps them to the connector's body-based authentication fields. See [`AuthorizedotnetAuthType::try_from()`](https://github.com/juspay/hyperswitch/blob/2ef1f9ee5bdf65356c3169f4f5db67fa1d4de7bc/crates/hyperswitch_connectors/src/connectors/authorizedotnet/transformers.rs#L96-L108).

### Webhooks

Authorize.net webhooks are verified with HMAC-SHA512. Hyperswitch reads the signature from `X-ANET-Signature` and verifies the raw request body. See [`get_webhook_source_verification_algorithm()`](https://github.com/juspay/hyperswitch/blob/2ef1f9ee5bdf65356c3169f4f5db67fa1d4de7bc/crates/hyperswitch_connectors/src/connectors/authorizedotnet.rs#L1024-L1059).

The connector recognizes six webhook event names:

| Event | Effect in Hyperswitch |
|---|---|
| `net.authorize.payment.authorization.created` | Payment is marked successful |
| `net.authorize.payment.priorAuthCapture.created` | Payment is marked successful |
| `net.authorize.payment.authcapture.created` | Payment is marked successful |
| `net.authorize.payment.capture.created` | Payment is marked successful |
| `net.authorize.payment.void.created` | Payment is marked successful |
| `net.authorize.payment.refund.created` | Refund is marked successful |

The event names and mappings are defined by [`AuthorizedotnetIncomingWebhookEventType`](https://github.com/juspay/hyperswitch/blob/2ef1f9ee5bdf65356c3169f4f5db67fa1d4de7bc/crates/hyperswitch_connectors/src/connectors/authorizedotnet/transformers.rs#L2340-L2368).

### Activate Authorize.net with Hyperswitch

#### Before you start

1. You need to be registered with Authorize.net. Sign up at [authorize.net](https://www.authorize.net/).
2. You should have a registered Hyperswitch account, accessible from the [Hyperswitch control center](https://hyperswitch.io/contact-sales).
3. Have the credentials listed in [Authentication](#authentication) ready.

To connect Authorize.net to your Hyperswitch account, follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for what Authorize.net supports.

---

### Source reference

[Authorize.net connector implementation](https://github.com/juspay/hyperswitch/blob/2ef1f9ee5bdf65356c3169f4f5db67fa1d4de7bc/crates/hyperswitch_connectors/src/connectors/authorizedotnet.rs)
