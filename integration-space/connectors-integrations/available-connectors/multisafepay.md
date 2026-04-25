---
description: >-
  Accept payments through MultiSafepay — a Dutch fintech providing online
  payment processing, digital wallets, and fraud prevention — via Juspay
  Hyperswitch.
metaLinks:
  alternates:
    - multisafepay.md
---

# MultiSafepay

![logo\_multisafepay](https://hyperswitch.io/icons/homePageIcons/logos/multisafepayLogo.svg)

MultiSafepay connects to Hyperswitch as a `PaymentGateway` connector using `HeaderKey` authentication — the API Key is embedded directly in the request URL as a query parameter (`?api_key={api_key}`), not in an HTTP header. All requests use `application/json`. MultiSafepay is a Dutch payment service provider with strong European payment method coverage.

### Connector-Specific Notes

- **API key in URL query parameter:** MultiSafepay does not use an `Authorization` header. The API Key is appended to the request URL as `?api_key={api_key}` on every request (orders, sync, captures, refunds). Do not place the key in a header field — only the URL parameter is validated.
- **Credentials location:** API Key is found in your MultiSafepay dashboard under **Integrations → Site**.
- **Capture methods supported:** Automatic and SequentialAutomatic. Manual capture is not supported.
- **SetupMandate:** Not supported.
- **Webhook support:** Webhooks are not implemented for MultiSafepay in Hyperswitch — payment status relies on sync polling.
- MultiSafepay is a Dutch fintech company providing online payment processing, digital wallets, and fraud prevention for European merchants.
- For a full list of supported payment methods, visit [hyperswitch.io/pm-list](https://hyperswitch.io/pm-list).

---

### Activating MultiSafepay via Hyperswitch

#### Prerequisites

1. You need to be registered with MultiSafepay. Sign up at [multisafepay.com](https://www.multisafepay.com/).
2. You should have a registered Hyperswitch account, accessible from the [Hyperswitch control center](https://app.hyperswitch.io/).
3. MultiSafepay **API Key** is found in your MultiSafepay dashboard under **Integrations → Site**.
4. Select all payment methods you wish to use MultiSafepay for. Ensure these match the ones configured in your MultiSafepay dashboard.

[Steps to activate MultiSafepay on the Hyperswitch control center](https://docs.hyperswitch.io/hyperswitch-cloud/connectors/activate-connector-on-hyperswitch)

---

### Responsibility Boundaries

**Hyperswitch owns:** routing decisions, retry scheduling, appending the API Key to every request URL, and unified error mapping. **MultiSafepay owns:** payment execution, fraud decisioning, and payment method routing. Since the API Key is in the URL, it must be kept confidential — HTTPS is required for all requests.

**Hyperswitch owns:** polling for payment status (no webhook delivery). **MultiSafepay owns:** making payment status available via the sync endpoint. All status updates rely on Hyperswitch's sync polling.

---

### Common Failure Modes

**Authentication failure**
Symptom: All requests fail with a MultiSafepay authentication error. Fix: Verify the API Key in Hyperswitch matches the one found in your MultiSafepay dashboard under **Integrations → Site**. The key is appended to the URL as `?api_key={value}`.

**Payment status not updating**
Symptom: Payments remain pending in Hyperswitch. Fix: Since MultiSafepay does not push webhooks in this integration, status is updated via sync polling. Ensure Hyperswitch's sync polling is running and the MultiSafepay endpoint is reachable.

**Payment method not configured**
Symptom: A payment method fails with an availability error. Fix: Verify the method is enabled for your MultiSafepay merchant account and matches the selection in the Hyperswitch connector configuration.

---

Connector implementation: `crates/hyperswitch_connectors/src/connectors/multisafepay.rs`.
