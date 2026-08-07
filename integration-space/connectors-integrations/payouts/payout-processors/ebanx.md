---
description: >-
  Configure EBANX as a payout processor on Juspay Hyperswitch for local
  currency payouts across Latin America via Pix and other local rails.
---

# EBANX

EBANX connects to Hyperswitch as a `PayoutProcessor` for cross-border disbursements and local currency payouts across Latin America. It specializes in LATAM markets where global card rails and SWIFT are not the preferred disbursement method. Pix (Brazil's instant payment rail) support is currently in beta.

### Authentication

EBANX uses `HeaderKey` authentication — a single integration key sent on every request.

| Credential | Description |
| --- | --- |
| **Integration Key (API Key)** | EBANX integration key. Found in your EBANX merchant portal under API settings. |

### Supported Payout Methods

| Method | Rails / Networks | Regions | Notes |
| --- | --- | --- | --- |
| Bank transfers | Pix | Brazil | Instant bank transfer via Brazil's Pix rail. Currently in beta. |

### Payout Flows

EBANX implements the following Hyperswitch payout flows:

| Flow | Description |
| --- | --- |
| **PoCreate** | Creates the payout disbursement in EBANX |
| **PoFulfill** | Executes and submits the payout for processing |
| **PoCancel** | Cancels a pending payout |

### Common Failure Modes

**Integration key rejected**
Symptom: EBANX returns 401 Unauthorized. Fix: Verify the Integration Key stored in Hyperswitch matches the key from your EBANX merchant portal. Keys are environment-specific — test keys do not work in production.

**Pix key not found**
Symptom: Payout fails with recipient validation error. Fix: Confirm the recipient's Pix key (CPF, CNPJ, email, phone, or random key) is registered in Brazil's Pix directory. Invalid or unregistered Pix keys will be rejected.

**Country not supported**
Symptom: Payout fails for a non-LATAM destination. Fix: EBANX payouts are limited to supported LATAM countries. Check EBANX's supported country list for payout availability.

---

### Activating EBANX Payouts via Hyperswitch

#### Prerequisites

1. An EBANX merchant account with payout capabilities. Contact [ebanx.com](https://www.ebanx.com/) for onboarding.
2. A registered Hyperswitch account, accessible from the [Hyperswitch control center](https://app.hyperswitch.io/).
3. Integration Key from your EBANX merchant portal.

[Steps to activate a connector on the Hyperswitch control center](../../activate-connector-on-hyperswitch/README.md)

---

Connector implementation: `crates/hyperswitch_connectors/src/connectors/ebanx.rs`.
