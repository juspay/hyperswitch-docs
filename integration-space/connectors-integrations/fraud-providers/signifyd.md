---
description: >-
  Integrate Signifyd fraud and risk management with Juspay Hyperswitch to
  automate fraud decisions and protect against chargeback liability.
---

# Signifyd

Signifyd connects to Hyperswitch as a `FraudAndRiskManagementProvider`. It provides AI-driven commerce protection with guaranteed fraud liability coverage — Signifyd takes on chargeback liability for orders it approves. Signifyd is not a payment processor; it evaluates orders independently of payment authorization.

### Authentication

Signifyd uses `HeaderKey` authentication — a single API key sent as a Bearer token on every request.

| Credential | Description |
| --- | --- |
| **API Key** | Bearer token issued by Signifyd. Found in your Signifyd merchant portal under API settings. |

### FRM Flows

Signifyd participates in the following Hyperswitch FRM flows:

| Flow | Description |
| --- | --- |
| **Sale** | Pre-authorization fraud check on the payment attempt |
| **Checkout** | Fraud evaluation at checkout, before payment is submitted |
| **Transaction** | Post-authorization evaluation of a completed transaction |
| **Fulfillment** | Signal to Signifyd that an order has been fulfilled (triggers liability shift) |
| **RecordReturn** | Notify Signifyd of a return or refund on a previously approved order |

### Webhook Events

Signifyd sends decision updates via webhook. Hyperswitch handles HMAC-SHA256 signature verification using the API key.

### Common Failure Modes

**Decision not returned**
Symptom: FRM evaluation times out or returns no decision. Fix: Check Signifyd's merchant portal for order status. Ensure the order details (email, address, line items) are complete — incomplete orders are often held or declined by Signifyd.

**Liability shift not applied**
Symptom: Signifyd approves the order but chargeback liability is not shifted. Fix: Verify the Fulfillment flow is being called after shipment. Liability shift typically requires a fulfillment signal.

---

### Activating Signifyd via Hyperswitch

#### Prerequisites

1. A registered Signifyd merchant account. Contact [signifyd.com](https://www.signifyd.com/) for onboarding.
2. A registered Hyperswitch account, accessible from the [Hyperswitch control center](https://app.hyperswitch.io/).
3. API Key from the Signifyd merchant portal.

[Steps to activate a connector on the Hyperswitch control center](../activate-connector-on-hyperswitch/README.md)

---

Connector implementation: `crates/hyperswitch_connectors/src/connectors/signifyd.rs`.
