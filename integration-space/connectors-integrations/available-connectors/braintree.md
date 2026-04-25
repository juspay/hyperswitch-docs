---
description: >-
  Accept payments through Braintree via Hyperswitch — covers prerequisites, API
  credentials, and webhook configuration.
metaLinks:
  alternates:
    - braintree.md
---

# Braintree

Braintree connects to Hyperswitch as a `PaymentGateway` connector using `MultiAuthKey` authentication — three credentials (Merchant ID, Public Key, Private Key) are required. Unlike most connectors that use a single API key, Braintree authenticates requests using HTTP Basic auth where the username is the Public Key and the password is the Private Key, base64-encoded. All payment operations use Braintree's GraphQL API (not REST), which Hyperswitch handles transparently via its connector implementation.

### Connector-Specific Notes

- **Authentication model:** Three-credential `MultiAuthKey` — Merchant ID, Public Key, and Private Key. The Public Key and Private Key together form HTTP Basic auth credentials (`Authorization: Basic base64(public_key:private_key)`). The Merchant ID is used to scope all requests to your Braintree merchant account.
- **GraphQL-based API:** Braintree uses GraphQL mutations for payment operations, not REST endpoints. Hyperswitch constructs the appropriate GraphQL queries internally — this is invisible to the caller but means error responses from Braintree are structured differently from REST connectors.
- **Webhook verification:** Braintree uses HMAC-SHA1 for webhook signature verification. Configure the webhook endpoint in Braintree and store the webhook notification signing key in Hyperswitch.
- **PayPal parent account requirement:** Braintree is owned by PayPal, and a PayPal Business account is required to activate Braintree. Ensure your PayPal Business account is in good standing before setting up Braintree credentials.
- **Google Pay and Apple Pay via Braintree:** Both wallets are supported via Braintree's SDK-based integration. Google Pay uses Braintree's Google Pay SDK flow; Apple Pay uses the Braintree Apple Pay SDK flow. These differ from PSP-decryption and Hyperswitch-decryption wallet flows.
- **Capture methods supported:** Automatic, Manual, SequentialAutomatic.
- For a full list of supported payment methods, visit [hyperswitch.io/pm-list](https://hyperswitch.io/pm-list).

---

### Activating Braintree via Hyperswitch

#### Prerequisites

1. You need to be registered with Braintree. Sign up at [braintreepayments.com/sandbox](https://www.braintreepayments.com/sandbox).
2. You should have a registered Hyperswitch account, accessible from the [Hyperswitch control center](https://app.hyperswitch.io/register).
3. The Braintree Merchant ID, Public Key, and Private Key are available in your Braintree dashboard under **Home → Settings → API**.
4. To set webhooks, navigate to **Home → Settings → API → Webhooks** and create a new webhook.

[Steps to activate Braintree on the Hyperswitch control center](https://docs.hyperswitch.io/hyperswitch-cloud/connectors/activate-connector-on-hyperswitch)

---

### Responsibility Boundaries

**Hyperswitch owns:** routing decisions, mandate record storage, retry scheduling, and unified error mapping. **Braintree owns:** payment execution via its GraphQL API, fraud evaluation (Kount integration), and vault storage for payment methods. Braintree's vault is separate from Hyperswitch's vault — payment methods stored in Braintree are referenced by Braintree's nonce/token system, not Hyperswitch's token IDs.

**Hyperswitch owns:** translating its unified payment model into Braintree's GraphQL mutation structure. **Braintree owns:** execution and response. If a GraphQL mutation is rejected (e.g. missing required field for a payment method), the error surfaces as a Braintree-level validation error in Hyperswitch's error response — not a network or authentication error.

---

### Common Failure Modes

**Wrong credential type used**
Symptom: All API calls return authentication errors. Fix: Confirm you are using the Public Key (not the API key or Private Key alone) as the HTTP Basic username, and the Private Key as the password. The Merchant ID is a separate field, not part of the Basic auth credentials.

**PayPal Business account not active**
Symptom: Braintree account activation fails or payments cannot be processed. Fix: Ensure the PayPal Business account linked to your Braintree account is verified and in good standing.

**Webhook signature verification failure**
Symptom: Braintree webhook events are received but rejected by Hyperswitch — payment statuses do not update. Fix: Verify the webhook signing key configured in Hyperswitch matches the one in your Braintree dashboard under **Settings → API → Webhooks**.

**Google Pay or Apple Pay SDK flow not initialising**
Symptom: Wallet payment buttons do not appear or fail at initialisation. Fix: Both wallets require Braintree's SDK-based integration. Ensure the correct SDK session token is being generated via Hyperswitch before rendering the wallet button.

---

Connector implementation: `crates/hyperswitch_connectors/src/connectors/braintree.rs`.
