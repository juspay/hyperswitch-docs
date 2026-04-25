---
description: >-
  Configure PayPal as a payout processor on Juspay Hyperswitch to distribute
  funds to PayPal and Venmo accounts globally.
---

# PayPal

PayPal connects to Hyperswitch as a `PayoutProcessor` for digital wallet payouts. It supports payouts to PayPal accounts globally and Venmo accounts within the US. PayPal is also a payment gateway on Hyperswitch — the same connector handles both payments and payouts.

### Authentication

PayPal uses `BodyKey` authentication with OAuth2 client credentials. Two credentials are required.

| Credential | Description |
| --- | --- |
| **Client Secret (API Key)** | PayPal app client secret. Found in the PayPal Developer Dashboard under Apps & Credentials. |
| **Client ID (Key1)** | PayPal app client ID. Found in the PayPal Developer Dashboard under Apps & Credentials. |

Hyperswitch uses these credentials to obtain a Bearer access token from PayPal's OAuth2 token endpoint before each API call.

### Supported Payout Methods

| Method | Rails / Networks | Notes |
| --- | --- | --- |
| Wallets | PayPal | Payouts to any PayPal account email address globally |
| Wallets | Venmo | Payouts to Venmo accounts (US only) |

### Payout Flows

PayPal implements the following Hyperswitch payout flows:

| Flow | Description |
| --- | --- |
| **PoCreate** | Creates the payout batch in PayPal's Payouts API |
| **PoFulfill** | Executes the payout — processes the created batch |
| **PoSync** | Retrieves the status of a payout item |

### Common Failure Modes

**Access token fetch fails**
Symptom: PayPal returns 401 on all requests. Fix: Verify the Client ID and Client Secret stored in Hyperswitch match your PayPal app credentials. Credentials are environment-specific — sandbox credentials do not work in production.

**Receiver account not found**
Symptom: Payout fails with `RECEIVER_UNREGISTERED` or similar error. Fix: The recipient email must be a registered PayPal account. PayPal payouts cannot be sent to unregistered email addresses.

**Payout blocked by compliance**
Symptom: Payout returns a `COMPLIANCE_VIOLATION` error. Fix: This occurs when the recipient country or payout amount triggers PayPal's compliance checks. Review PayPal's payout restrictions for the target country.

---

### Activating PayPal Payouts via Hyperswitch

#### Prerequisites

1. A PayPal Business account with Payouts API access enabled. Enable the Payouts API in the PayPal Developer Dashboard.
2. A registered Hyperswitch account, accessible from the [Hyperswitch control center](https://app.hyperswitch.io/).
3. Client ID and Client Secret from the PayPal Developer Dashboard under Apps & Credentials.

[Steps to activate a connector on the Hyperswitch control center](../../activate-connector-on-hyperswitch/README.md)

---

Connector implementation: `crates/hyperswitch_connectors/src/connectors/paypal.rs`.
