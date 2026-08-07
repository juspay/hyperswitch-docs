---
description: >-
  Accept payments through Billwerk+ via Juspay Hyperswitch — configure API
  credentials for the subscription and payment platform.
metaLinks:
  alternates:
    - billwerk.md
---

# Billwerk

Billwerk connects to Hyperswitch as a `PaymentGateway` connector using `BodyKey` authentication. The Private API Key is sent as `Authorization: Basic {base64(api_key:)}` — HTTP Basic auth format with the API key as the username and an intentionally empty password field (trailing colon). All requests use `application/json`. Billwerk+ Pay is an acquirer-independent payment gateway.

### Connector-Specific Notes

- **HTTP Basic auth with empty password:** Billwerk uses HTTP Basic auth where only the Private API Key is provided as the username, with no password: `Authorization: Basic base64(api_key:)`. The trailing colon is intentional. The Public API Key (key1) is stored as a second credential but is not sent in the Authorization header — it is used separately for client-side tokenization flows.
- **Credentials location:** Private API Key and Public API Key are found in your Billwerk+ Pay dashboard under **Developers → API Credentials**.
- **Capture methods supported:** Automatic, Manual, SequentialAutomatic.
- **SetupMandate:** Not supported.
- **Webhook support:** Webhooks are not implemented for Billwerk.
- Billwerk+ Pay is an acquirer-independent payment gateway with broad payment method support and European market focus.
- For a full list of supported payment methods, visit [hyperswitch.io/pm-list](https://hyperswitch.io/pm-list).

---

### Activating Billwerk via Hyperswitch

#### Prerequisites

1. You need to be registered with Billwerk+ Pay. Sign up at [signup.billwerk.plus](https://signup.billwerk.plus/).
2. You should have a registered Hyperswitch account, accessible from the [Hyperswitch control center](https://app.hyperswitch.io/).
3. Billwerk+ Pay **Private API Key** and **Public API Key** are found in your Billwerk+ Pay dashboard under **Developers → API Credentials**.
4. Select all payment methods you wish to use Billwerk for. Ensure these match the ones configured in your Billwerk+ Pay dashboard under the **Configurations** tab.

[Steps to activate Billwerk on the Hyperswitch control center](https://docs.hyperswitch.io/hyperswitch-cloud/connectors/activate-connector-on-hyperswitch)

---

### Responsibility Boundaries

**Hyperswitch owns:** routing decisions, retry scheduling, constructing the HTTP Basic authorization header with an empty password field on every request, and unified error mapping. **Billwerk owns:** payment execution, acquirer routing, and credential validation.

**Hyperswitch owns:** embedding the Private API Key in every request header. **Billwerk owns:** validating it. If the Private API Key changes in Billwerk and is not updated in Hyperswitch, all requests will fail authentication immediately.

---

### Common Failure Modes

**Authentication failure**
Symptom: All requests fail with a Billwerk authentication error. Fix: Verify the Private API Key in Hyperswitch matches your Billwerk+ Pay dashboard. The key is sent as the HTTP Basic username with an empty password — do not manually Base64-encode it before entering in the control center.

**Payment method not configured**
Symptom: A payment method fails with an availability error. Fix: Verify the method is enabled for your Billwerk+ Pay account and matches the selection in the Hyperswitch connector configuration. Confirm the method appears under **Configurations** in the Billwerk+ Pay dashboard.

---

Connector implementation: `crates/hyperswitch_connectors/src/connectors/billwerk.rs`.
