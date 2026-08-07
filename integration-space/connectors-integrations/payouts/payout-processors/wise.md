---
description: >-
  Configure Wise as a payout processor on Juspay Hyperswitch for cross-border
  money transfers via SEPA, SWIFT, and ACH.
---

# Wise

Wise connects to Hyperswitch as a `PayoutProcessor` for cross-border money transfers. It supports card payouts and bank rail transfers (SEPA, SWIFT, ACH) internationally. Wise is purpose-built for international payouts and handles currency conversion natively.

### Authentication

Wise uses `BodyKey` authentication — two credentials are required.

| Credential | Description |
| --- | --- |
| **API Key** | Wise API token. Found in the Wise Business account under Settings → API tokens. |
| **Profile ID (Key1)** | Wise profile ID identifying your business account. Found in the Wise Business account under Settings → Profile. |

### Supported Payout Methods

| Method | Rails / Networks | Notes |
| --- | --- | --- |
| Cards | Major card networks | Card payouts globally |
| Bank transfers | SEPA, SWIFT, ACH | Local and international bank account transfers with FX conversion |

### Payout Flows

Wise implements the following Hyperswitch payout flows:

| Flow | Description |
| --- | --- |
| **PoQuote** | Requests a transfer quote (exchange rate, fee, estimated delivery) |
| **PoRecipient** | Creates or verifies the transfer recipient's bank account |
| **PoCreate** | Creates the transfer using the quote and recipient |
| **PoFulfill** | Funds and executes the transfer |
| **PoEligibility** | Checks whether the payout method is eligible |
| **PoCancel** | Cancels a pending transfer |
| **PoSync** | Retrieves the current transfer status |

### Common Failure Modes

**Invalid profile ID**
Symptom: Wise returns a profile not found or unauthorized error. Fix: Verify the Profile ID (Key1) matches your Wise business profile ID. Personal and business profiles have separate IDs — use the business profile for payouts.

**Quote expired**
Symptom: Transfer creation fails after a delay. Fix: Wise quotes expire after a short window. Ensure PoCreate is called immediately after PoQuote. If the quote has expired, request a new quote.

**Recipient validation failed**
Symptom: Recipient creation fails with account validation error. Fix: Confirm the bank account details (IBAN, sort code, account number, routing number) are correct for the target country. Wise validates recipient accounts against local banking rules.

---

### Activating Wise Payouts via Hyperswitch

#### Prerequisites

1. A Wise Business account with API access enabled. Contact [wise.com/business](https://wise.com/business) for onboarding.
2. A registered Hyperswitch account, accessible from the [Hyperswitch control center](https://app.hyperswitch.io/).
3. API token and Profile ID from your Wise Business account settings.

[Steps to activate a connector on the Hyperswitch control center](../../activate-connector-on-hyperswitch/README.md)

---

Connector implementation: `crates/hyperswitch_connectors/src/connectors/wise.rs`.
