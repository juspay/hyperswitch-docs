---
description: Accept card and wallet payments through Worldpay on Hyperswitch.
metaLinks:
  alternates:
    - worldpay.md
---

# Worldpay

<div align="left"><img src="https://hyperswitch.io/icons/homePageIcons/logos/worldpayLogo.svg" alt=""></div>

Worldpay connects merchants to payment processing through Hyperswitch.

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch d8f9262a968f392d6ad75747c38ed7aece123fe9; host http://localhost:8080; fetched 2026-09-09; matrix canonical-json-v1 sha256 36360b019f2761dd; 138 connectors.
     Do not edit by hand. This block regenerates from the connector's
     SupportedPaymentMethods declaration in code; edit that instead. -->

**Integration status:** live

**Category:** payment gateway

**Webhook flows:** payments

| Payment method | Type | Mandates | Refunds | Capture methods | 3DS | Card networks | Countries | Currencies |
|---|---|---|---|---|---|---|---|---|
| card | Credit Card | supported | supported | automatic, manual, sequential automatic | supported, optional | American Express, Cartes Bancaires, Diners Club, JCB, Maestro, Mastercard, Visa | 133 ([full list](https://hyperswitch.io/pm-list)) | 147 ([full list](https://hyperswitch.io/pm-list)) |
| card | Debit Card | supported | supported | automatic, manual, sequential automatic | supported, optional | American Express, Cartes Bancaires, Diners Club, JCB, Maestro, Mastercard, Visa | 133 ([full list](https://hyperswitch.io/pm-list)) | 147 ([full list](https://hyperswitch.io/pm-list)) |
| wallet | Apple Pay | not supported | supported | automatic, manual, sequential automatic | not applicable | - | 90 ([full list](https://hyperswitch.io/pm-list)) | 58 ([full list](https://hyperswitch.io/pm-list)) |
| wallet | Google Pay | not supported | supported | automatic, manual, sequential automatic | not applicable | - | 75 ([full list](https://hyperswitch.io/pm-list)) | 57 ([full list](https://hyperswitch.io/pm-list)) |

### Connector-Specific Notes

* **Authentication:** Configure the API key, username, and entity ID. In the `SignatureKey` mapping, `key1` carries the username, `api_key` carries the API key, and `api_secret` carries the entity ID. Hyperswitch joins `key1` and `api_key`, Base64-encodes the pair, and sends it as an HTTP Basic credential in the `Authorization` header on every request. The backward-compatible `BodyKey` path uses `key1` and `api_key` for the same credential and sets the entity ID to `default` ([auth mapping](https://github.com/juspay/hyperswitch/blob/d8f9262a968f392d6ad75747c38ed7aece123fe9/crates/hyperswitch_connectors/src/connectors/worldpay/transformers.rs#L715-L748), [request header](https://github.com/juspay/hyperswitch/blob/d8f9262a968f392d6ad75747c38ed7aece123fe9/crates/hyperswitch_connectors/src/connectors/worldpay.rs#L149-L160)).
* **Mandate setup:** The connector implements `MandateSetup` ([flow implementation](https://github.com/juspay/hyperswitch/blob/d8f9262a968f392d6ad75747c38ed7aece123fe9/crates/hyperswitch_connectors/src/connectors/worldpay.rs#L215-L224)).
* **Payout fulfillment:** When Hyperswitch is built with the `payouts` feature, the connector implements payout fulfillment ([feature-gated flow implementation](https://github.com/juspay/hyperswitch/blob/d8f9262a968f392d6ad75747c38ed7aece123fe9/crates/hyperswitch_connectors/src/connectors/worldpay.rs#L1146-L1151)).
* For the full payment-method list behind the generated table, visit [hyperswitch.io/pm-list](https://hyperswitch.io/pm-list).

### Webhooks

Worldpay can send the 12 named events below. Seven update payment state; five are unsupported. Unrecognized event names use the `Unknown` fallback and are unsupported ([event names](https://github.com/juspay/hyperswitch/blob/d8f9262a968f392d6ad75747c38ed7aece123fe9/crates/hyperswitch_connectors/src/connectors/worldpay/response.rs#L235-L253), [event effects](https://github.com/juspay/hyperswitch/blob/d8f9262a968f392d6ad75747c38ed7aece123fe9/crates/hyperswitch_connectors/src/connectors/worldpay.rs#L1350-L1374)).

| Worldpay event | Effect in Hyperswitch |
|---|---|
| `Authorized` | Payment authorization succeeds |
| `Settled` | Payment succeeds |
| `SentForSettlement` | Payment is processing |
| `SentForAuthorization` | Payment is processing |
| `Error` | Payment fails |
| `Expired` | Payment fails |
| `SettlementFailed` | Payment fails |
| `Cancelled` | Event is not supported |
| `Refused` | Event is not supported |
| `Refunded` | Event is not supported |
| `SentForRefund` | Event is not supported |
| `RefundFailed` | Event is not supported |
| `Unknown` | Event is not supported |

Webhook source verification is implemented. Hyperswitch reads the final signature value from `Event-Signature`, verifies the raw request body with HMAC-SHA256 using the hex-decoded webhook `secret`, and compares the computed and received hex values ([verification implementation](https://github.com/juspay/hyperswitch/blob/d8f9262a968f392d6ad75747c38ed7aece123fe9/crates/hyperswitch_connectors/src/connectors/worldpay.rs#L1266-L1335)).

***

### Activating Worldpay via Hyperswitch

#### Prerequisites

1. You need to be registered with Worldpay. Sign up at [worldpay.com](https://online.worldpay.com/).
2. You should have a registered Hyperswitch account, accessible from the [Hyperswitch control center](https://app.hyperswitch.io/).
3. Have the connector credentials listed in [Connector-Specific Notes](#connector-specific-notes) ready.
4. Select all payment methods you wish to use Worldpay for. Ensure these match the ones configured in your Worldpay dashboard.

[Steps to activate Worldpay on the Hyperswitch control center](https://docs.hyperswitch.io/hyperswitch-cloud/connectors/activate-connector-on-hyperswitch)

***

### Responsibility Boundaries

**Hyperswitch owns:** routing decisions, retry scheduling, mandate reference storage (ConnectorMandateId from SetupMandate used in RepeatPayment), routing captures to `/settlements` or `/partialSettlements` based on capture type, and unified error mapping. **Worldpay owns:** payment execution, fraud scoring, settlement routing, and token issuance for mandate flows.

**Hyperswitch owns:** sending the correct payment instrument reference in RepeatPayment requests. **Worldpay owns:** validating that the reference is active and matches the original SetupMandate. If a mandate reference expires or is revoked in Worldpay and is not updated in Hyperswitch, RepeatPayment requests will fail.

***

### Common Failure Modes

**Authentication failure** Symptom: All requests fail with a Worldpay 401 or authentication error. Fix: Verify the username, API key, and entity ID in Hyperswitch match your Worldpay configuration. Enter the values exactly as provided.

**Partial capture fails** Symptom: A multiple capture request fails after the first capture. Fix: Ensure the original payment was authorized with `capture_method: manual` and that the sum of partial captures does not exceed the authorized amount.

**RepeatPayment fails: invalid mandate reference** Symptom: MIT payment fails with a Worldpay token or reference error. Fix: Verify the mandate reference from the original SetupMandate is stored correctly in Hyperswitch and has not been revoked in Worldpay.

**Payment method not configured** Symptom: A payment method fails with an availability error. Fix: Verify the method is enabled for your Worldpay merchant account and matches the selection in the Hyperswitch connector configuration.

***

Connector implementation: `crates/hyperswitch_connectors/src/connectors/worldpay.rs`.
