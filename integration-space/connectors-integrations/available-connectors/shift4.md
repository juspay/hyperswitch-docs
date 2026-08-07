---
description: Accept payments through Shift4 via Juspay Hyperswitch
metaLinks:
  alternates:
    - shift4.md
---

# Shift4

Shift4 connects to Hyperswitch as a `PaymentGateway` connector using `HeaderKey` authentication with a Base64-encoded API key. Unlike connectors that use a plain Bearer token, Shift4 uses HTTP Basic auth format: the API key is Base64-encoded as `{api_key}:` (with a trailing colon and empty password field) and sent as `Authorization: Basic {base64_encoded_key}`. All requests use `application/json`.

### Connector-Specific Notes

- **HTTP Basic auth format:** Shift4's API key is Base64-encoded in HTTP Basic format (`{api_key}:`) — the empty string after the colon is intentional. This is functionally an API key auth, but the encoding and header format follow the HTTP Basic auth convention. The API key is found in your Shift4 dashboard on the Home page.
- **Capture methods supported:** Automatic, Manual, SequentialAutomatic.
- **SetupMandate:** Supported for applicable payment methods.
- Shift4 provides payment processing with a focus on hospitality, retail, and restaurant verticals, in addition to e-commerce.
- Payment methods must be enabled in both Hyperswitch and your Shift4 dashboard to function correctly.
- For a full list of supported payment methods, visit [hyperswitch.io/pm-list](https://hyperswitch.io/pm-list).

---

### Activating Shift4 via Hyperswitch

#### Prerequisites

1. You need to be registered with Shift4. Sign up at [shift4.com](https://www.shift4.com/).
2. You should have a registered Hyperswitch account, accessible from the [Hyperswitch control center](https://app.hyperswitch.io/).
3. The Shift4 API key is found on the Home page of your Shift4 dashboard.
4. Select all payment methods you wish to use Shift4 for. Ensure these match the ones configured in your Shift4 dashboard.

[Steps to activate Shift4 on the Hyperswitch control center](https://docs.hyperswitch.io/hyperswitch-cloud/connectors/activate-connector-on-hyperswitch)

---

### Responsibility Boundaries

**Hyperswitch owns:** routing decisions, retry scheduling, mandate record storage, Base64-encoding the API key into HTTP Basic format on every request, and unified error mapping. **Shift4 owns:** payment execution, fraud decisioning, and terminal/POS routing for in-person payment scenarios. Shift4's POS routing logic is entirely within Shift4's system — Hyperswitch only interacts with Shift4's online payment API.

**Hyperswitch owns:** constructing the correct Base64-encoded Authorization header. **Shift4 owns:** validating the decoded API key. If the API key changes in Shift4 and is not updated in Hyperswitch, all requests will fail authentication.

---

### Common Failure Modes

**Authentication failure due to encoding error**
Symptom: All requests return an authentication error from Shift4. Fix: Verify the API key in Hyperswitch is the raw key from your Shift4 dashboard — Hyperswitch handles the Base64 encoding automatically. Do not manually Base64-encode the key before entering it in the control center.

**Payment method not configured in Shift4**
Symptom: A payment method fails with an availability error. Fix: Verify the method is enabled in your Shift4 account and matches the selection in the Hyperswitch connector configuration.

---

Connector implementation: `crates/hyperswitch_connectors/src/connectors/shift4.rs`.
