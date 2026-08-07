---
description: >-
  Configure Adyen as a payout processor on Juspay Hyperswitch to distribute
  funds globally via cards, SEPA, SWIFT, ACH, and digital wallets.
---

# Adyen

Adyen connects to Hyperswitch as a `PayoutProcessor`. It supports card payouts, bank rail transfers (SEPA, SWIFT, ACH), and digital wallet payouts (PayPal, Neteller, Skrill) across global markets. Adyen is also a payment gateway on Hyperswitch — the same connector handles both inbound payments and outbound payouts.

### Authentication

Adyen uses `BodyKey` authentication for payouts — two credentials are required.

| Credential | Description |
| --- | --- |
| **API Key** | Adyen API key from the Adyen Customer Area. Used in the `X-API-Key` header. |
| **Merchant Account (Key1)** | Your Adyen merchant account code. Sent in the request body to identify the account initiating payouts. |

### Supported Payout Methods

| Method | Rails / Networks | Notes |
| --- | --- | --- |
| Cards | Major card networks | Card payouts to debit and credit cards |
| Bank transfers | SEPA, SWIFT, ACH | Local and international bank account payouts |
| Wallets | PayPal, Neteller, Skrill | Neteller and Skrill require explicit enablement |

### Payout Flows

Adyen implements the following Hyperswitch payout flows:

| Flow | Description |
| --- | --- |
| **PoCreate** | Creates the payout record in Adyen |
| **PoEligibility** | Checks whether a payment method is eligible for payouts |
| **PoFulfill** | Submits the payout for execution |
| **PoCancel** | Cancels a payout before it is processed |

### Common Failure Modes

**Invalid merchant account**
Symptom: Adyen returns a `700 Invalid merchant account` error. Fix: Verify the Merchant Account (Key1) stored in Hyperswitch matches the merchant account code in your Adyen Customer Area exactly (case-sensitive).

**Payout not enabled**
Symptom: Adyen rejects the payout with a permissions error. Fix: Ensure the Adyen account has the `PAYOUT` permission enabled. Payouts require explicit enablement in the Adyen Customer Area and may require a separate Adyen Payout contract.

**Unsupported payout method**
Symptom: Eligibility check fails for a specific payment method. Fix: Confirm the payment method is supported for payouts in the target country. Not all card networks or bank rails are available in all regions.

---

### Activating Adyen Payouts via Hyperswitch

#### Prerequisites

1. An Adyen merchant account with payout permissions enabled. Contact your Adyen account manager to enable the payout contract.
2. A registered Hyperswitch account, accessible from the [Hyperswitch control center](https://app.hyperswitch.io/).
3. API Key and Merchant Account code from the Adyen Customer Area.

[Steps to activate a connector on the Hyperswitch control center](../../activate-connector-on-hyperswitch/README.md)

---

Connector implementation: `crates/hyperswitch_connectors/src/connectors/adyen.rs`.
