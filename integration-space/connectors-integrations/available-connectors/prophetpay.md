---
description: >-
  Connect Prophetpay with Juspay Hyperswitch to accept and process payments
  through Prophetpay's integrated payment methods on your platform.
metaLinks:
  alternates:
    - prophetpay.md
---

# Prophetpay

Prophetpay connects to Hyperswitch as a `PaymentGateway` connector using `SignatureKey` authentication with three credentials. The Username and Password are combined as `{username}:{password}`, Base64-encoded, and sent as `Authorization: Basic {encoded}` on every request. The Profile ID (api_secret) is used in request bodies to scope payments to the correct merchant profile. All requests use `application/json`.

### Connector-Specific Notes

- **HTTP Basic auth with Profile ID:** Prophetpay uses `SignatureKey` auth with three credentials. The Username (api_key) and Password (key1) form the HTTP Basic auth credentials: `Authorization: Basic base64(username:password)`. The Profile ID (api_secret) is embedded in payment request bodies to identify the merchant profile — it is not sent in the Authorization header.
- **Credentials location:** Username and Password are obtained from the Prophetpay team during onboarding (register at [clubprophet.com](https://www.clubprophet.com/products---prophetpay)). Profile ID is obtained from the Prophetpay dashboard after registration.
- **Capture methods supported:** Automatic and SequentialAutomatic. Manual capture is not supported.
- **Webhook support:** Webhooks are not implemented for Prophetpay in Hyperswitch.
- Prophetpay is a payment service provider focused on the golf and hospitality industry, with integrated payment methods for club and venue management platforms.
- For a full list of supported payment methods, visit [hyperswitch.io/pm-list](https://hyperswitch.io/pm-list).

---

### Activating Prophetpay via Hyperswitch

#### Prerequisites

1. You need to be registered with Prophetpay. Register at [clubprophet.com/products---prophetpay](https://www.clubprophet.com/products---prophetpay).
2. You should have a registered Hyperswitch account, accessible from the [Hyperswitch control center](https://app.hyperswitch.io/).
3. Prophetpay **Username** and **Password** are provided by the Prophetpay team during onboarding. **Profile ID** is obtained from your Prophetpay dashboard.
4. Select all payment methods you wish to use Prophetpay for. Ensure these match the ones configured in your Prophetpay dashboard.

[Steps to activate Prophetpay on the Hyperswitch control center](https://docs.hyperswitch.io/hyperswitch-cloud/connectors/activate-connector-on-hyperswitch)

---

### Responsibility Boundaries

**Hyperswitch owns:** routing decisions, retry scheduling, constructing the HTTP Basic authorization header on every request, embedding the Profile ID in payment request bodies, and unified error mapping. **Prophetpay owns:** payment execution, merchant profile validation, and payment method routing.

**Hyperswitch owns:** sending the correct credentials on every request. **Prophetpay owns:** validating the Username, Password, and Profile ID combination. If any credential changes and is not updated in Hyperswitch, requests will fail authentication or profile validation.

---

### Common Failure Modes

**Authentication failure**
Symptom: All requests fail with a Prophetpay authentication error. Fix: Verify the Username and Password in Hyperswitch match exactly what was provided during Prophetpay onboarding. Do not manually Base64-encode them before entering in the control center.

**Profile ID mismatch**
Symptom: Payments fail with a merchant profile or configuration error. Fix: Verify the Profile ID in Hyperswitch matches the one shown in your Prophetpay dashboard. The Profile ID is embedded in every payment request body.

---

Connector implementation: `crates/hyperswitch_connectors/src/connectors/prophetpay.rs`.
