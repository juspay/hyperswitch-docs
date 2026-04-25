---
description: >-
  Configure Cybersource as a payout processor on Juspay Hyperswitch for
  global card-based payouts.
---

# Cybersource

Cybersource connects to Hyperswitch as a `PayoutProcessor` for card-based payouts globally. It supports payouts to major card networks. Cybersource is also a payment gateway on Hyperswitch — the same connector handles both inbound payments and outbound payouts.

### Authentication

Cybersource uses `SignatureKey` authentication — three credentials are required. Requests are signed using HTTP Signature authentication (HMAC-SHA256 over request headers and body).

| Credential | Description |
| --- | --- |
| **API Key** | Cybersource shared secret key for HTTP Signature generation. Found in the Cybersource Business Center under Payment Configuration → Key Management. |
| **Merchant Account (Key1)** | Your Cybersource merchant ID. Found in the Cybersource Business Center. Used in request signing and routing. |
| **API Secret** | Cybersource secret key used as the HMAC signing key for request authentication. |

### Supported Payout Methods

| Method | Rails / Networks | Notes |
| --- | --- | --- |
| Cards | Major card networks | Push-to-card payouts to debit and prepaid cards |

### Payout Flows

Cybersource implements the following Hyperswitch payout flows:

| Flow | Description |
| --- | --- |
| **PoFulfill** | Submits the push-to-card payout directly for execution |

Cybersource's payout integration uses a direct fulfill model — there is no separate create or eligibility step.

### Common Failure Modes

**HTTP Signature mismatch**
Symptom: Cybersource returns a 401 with a signature validation error. Fix: Verify all three credentials (API Key, Merchant Account, API Secret) stored in Hyperswitch exactly match those in the Cybersource Business Center. Signature errors often indicate a key mismatch or an incorrect merchant ID.

**Card network not enabled for push payments**
Symptom: Payout fails with a card type or network restriction error. Fix: Confirm push-to-card payouts are enabled for the target card network on your Cybersource merchant account. Some networks require explicit enablement with Cybersource.

**Declined by issuer**
Symptom: Payout returns a decline reason code. Fix: The card issuer declined the push-to-card payment. This is not a Cybersource or Hyperswitch configuration issue — the recipient's issuing bank rejected the credit.

---

### Activating Cybersource Payouts via Hyperswitch

#### Prerequisites

1. A Cybersource merchant account with push-to-card payouts enabled. Contact your Cybersource account manager to enable payout capabilities.
2. A registered Hyperswitch account, accessible from the [Hyperswitch control center](https://app.hyperswitch.io/).
3. API Key, Merchant ID, and API Secret from the Cybersource Business Center under Key Management.

[Steps to activate a connector on the Hyperswitch control center](../../activate-connector-on-hyperswitch/README.md)

---

Connector implementation: `crates/hyperswitch_connectors/src/connectors/cybersource.rs`.
