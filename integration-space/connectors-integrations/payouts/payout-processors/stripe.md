---
description: >-
  Configure Stripe as a payout processor on Juspay Hyperswitch to distribute
  funds via cards and SEPA bank transfers using Stripe Connect.
---

# Stripe

Stripe connects to Hyperswitch as a `PayoutProcessor` via Stripe Connect. It supports card payouts and SEPA bank transfers globally. Stripe is also a payment gateway on Hyperswitch — the same connector handles both inbound payments and outbound payouts.

### Authentication

Stripe uses `HeaderKey` authentication — a single API key sent as a Bearer token on every request.

| Credential | Description |
| --- | --- |
| **API Key** | Stripe secret key (starts with `sk_live_` for production, `sk_test_` for test mode). Found in the Stripe Dashboard under Developers → API keys. |

### Supported Payout Methods

| Method | Rails / Networks | Notes |
| --- | --- | --- |
| Cards | Major card networks | Card payouts to debit cards via Stripe Connect |
| Bank transfers | SEPA | Bank account payouts within the SEPA zone |

### Payout Flows

Stripe implements the following Hyperswitch payout flows:

| Flow | Description |
| --- | --- |
| **PoCreate** | Creates the payout recipient in Stripe Connect |
| **PoFulfill** | Initiates the payout transfer |
| **PoCancel** | Cancels a pending payout |
| **PoRecipient** | Creates or updates the connected account recipient |
| **PoRecipientAccount** | Sets up or links a bank account to the connected account |

### Common Failure Modes

**Insufficient funds**
Symptom: Stripe returns `insufficient_funds` error. Fix: Ensure the Stripe Connect platform account has sufficient available balance before initiating payouts.

**Connected account not ready**
Symptom: Payout fails with `account_invalid` or `account_incomplete`. Fix: Verify the connected account has completed Stripe's identity verification and onboarding requirements. Stripe requires KYC completion before payouts can be disbursed.

**SEPA payout rejected**
Symptom: Bank transfer fails with an IBAN validation error. Fix: Confirm the IBAN is valid and belongs to a SEPA-zone bank account. Stripe validates IBAN format before initiating the transfer.

---

### Activating Stripe Payouts via Hyperswitch

#### Prerequisites

1. A Stripe account with Connect enabled. Set up Stripe Connect in the Stripe Dashboard.
2. A registered Hyperswitch account, accessible from the [Hyperswitch control center](https://app.hyperswitch.io/).
3. Stripe secret key from the Stripe Dashboard under Developers → API keys.

[Steps to activate a connector on the Hyperswitch control center](../../activate-connector-on-hyperswitch/README.md)

---

Connector implementation: `crates/hyperswitch_connectors/src/connectors/stripe.rs`.
