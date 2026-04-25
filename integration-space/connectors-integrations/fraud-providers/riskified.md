---
description: >-
  Integrate Riskified fraud prevention with Juspay Hyperswitch for guaranteed
  real-time fraud decisions powered by machine learning.
---

# Riskified

Riskified connects to Hyperswitch as a `FraudAndRiskManagementProvider`. It provides machine-learning-powered ecommerce fraud prevention with guaranteed real-time decisions. Like Signifyd, Riskified takes on chargeback liability for approved orders. Riskified is not a payment processor; it evaluates orders independently.

### Authentication

Riskified uses `BodyKey` authentication — two credentials are required: a secret token for HMAC request signing, and a domain name that identifies your Riskified merchant account.

| Credential | Description |
| --- | --- |
| **Secret Token (API Key)** | Used to generate HMAC-SHA256 signatures on request bodies. Found in your Riskified merchant portal. |
| **Domain Name (Key1)** | Your shop's domain as registered with Riskified (e.g. `yourshop.com`). Sent as the `X-RISKIFIED-SHOP-DOMAIN` header. |

### FRM Flows

Riskified participates in the following Hyperswitch FRM flows:

| Flow | Description |
| --- | --- |
| **Checkout** | Fraud evaluation at checkout, before payment is submitted |
| **Transaction** | Post-authorization evaluation of a completed transaction |
| **Fulfillment** | Signal to Riskified that an order has been fulfilled (triggers liability shift) |
| **RecordReturn** | Notify Riskified of a return or refund on a previously approved order |

### Request Signing

Every request to Riskified is signed with HMAC-SHA256 using the secret token. The signature is sent in the `X-RISKIFIED-HMAC-SHA256` header. Hyperswitch handles this signing automatically.

### Common Failure Modes

**HMAC signature mismatch**
Symptom: Riskified rejects requests with a 401 or signature error. Fix: Verify the Secret Token stored in Hyperswitch exactly matches the token in your Riskified merchant portal. Trailing whitespace or encoding differences will cause failures.

**Domain not recognized**
Symptom: Riskified returns a merchant not found error. Fix: Ensure the Domain Name (Key1) matches the domain registered in your Riskified account exactly, including subdomain and TLD.

**Liability shift not applied**
Symptom: Order approved but chargeback liability not shifted. Fix: Confirm the Fulfillment flow is triggered after shipment. Riskified requires a fulfillment notification to complete the liability transfer.

---

### Activating Riskified via Hyperswitch

#### Prerequisites

1. A registered Riskified merchant account. Contact [riskified.com](https://www.riskified.com/) for onboarding.
2. A registered Hyperswitch account, accessible from the [Hyperswitch control center](https://app.hyperswitch.io/).
3. Secret Token and registered Domain Name from the Riskified merchant portal.

[Steps to activate a connector on the Hyperswitch control center](../activate-connector-on-hyperswitch/README.md)

---

Connector implementation: `crates/hyperswitch_connectors/src/connectors/riskified.rs`.
