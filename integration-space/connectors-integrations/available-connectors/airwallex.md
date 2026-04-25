---
description: >-
  Accept payments globally through Airwallex via Hyperswitch, with support for
  cross-border payments, foreign exchange, and multiple payment methods.
metaLinks:
  alternates:
    - airwallex.md
---

# Airwallex

![Airwallex logo](https://hyperswitch.io/icons/homePageIcons/logos/airwallexLogo.svg)

Airwallex connects to Hyperswitch as a `PaymentGateway` connector using a two-step authentication model: the API Key and Client ID are exchanged for a short-lived Bearer access token via Airwallex's `/authentication/login` endpoint, and this token is then used on all subsequent payment requests. All requests use `application/json`. Airwallex is primarily used for cross-border payment scenarios where multi-currency support and FX handling are requirements.

### Connector-Specific Notes

- **OAuth-style token exchange:** Unlike connectors with static Bearer tokens, Airwallex requires fetching an access token before each session using the API Key and Client ID. Hyperswitch handles this token exchange internally — the credentials configured in the control center are the API Key and Client ID, not the access token.
- **Credentials location:** API Key and Client ID are found in your Airwallex dashboard under **Developer → API Keys**.
- **Cross-border and FX:** Airwallex's primary differentiator is multi-currency settlement and FX conversion. Payment methods and currencies available depend on your Airwallex account's approved corridors.
- **Capture methods supported:** Automatic, Manual, SequentialAutomatic.
- **SetupMandate:** Supported for applicable payment methods.
- For a full list of supported payment methods, visit [hyperswitch.io/pm-list](https://hyperswitch.io/pm-list).

---

### Activating Airwallex via Hyperswitch

#### Prerequisites

1. You need to be registered with Airwallex. Sign up at [airwallex.com](https://www.airwallex.com/).
2. You should have a registered Hyperswitch account, accessible from the [Hyperswitch control center](https://app.hyperswitch.io/).
3. The Airwallex API Key and Client ID are found in your Airwallex dashboard under **Developer → API Keys**.
4. Select all payment methods you wish to use Airwallex for. Ensure these match the ones configured in your Airwallex dashboard.

[Steps to activate Airwallex on the Hyperswitch control center](https://docs.hyperswitch.io/hyperswitch-cloud/connectors/activate-connector-on-hyperswitch)

---

### Responsibility Boundaries

**Hyperswitch owns:** routing decisions, token lifecycle management (fetching and refreshing the Airwallex access token), retry scheduling, and mandate record storage. **Airwallex owns:** payment execution, FX conversion, corridor availability, and settlement. The specific payment methods and currencies available for a given transaction are determined by your Airwallex account's approved corridors — Hyperswitch has no visibility into corridor restrictions at runtime.

**Hyperswitch owns:** initiating the token exchange before payment requests. **Airwallex owns:** issuing and expiring access tokens. If Airwallex's token endpoint is unavailable, payment requests cannot be initiated.

---

### Common Failure Modes

**Token exchange failure**
Symptom: Payment requests fail before reaching Airwallex's payment API. Fix: Verify the API Key and Client ID in Hyperswitch are correct and that your Airwallex account is active. An inactive account will cause token exchange to fail.

**Payment method not available for corridor**
Symptom: A payment method works in test but fails in production for a specific country or currency. Fix: Confirm with Airwallex that the specific country-currency corridor is approved for your account.

**FX rate unavailable**
Symptom: Cross-currency payments fail with a rate or corridor error. Fix: Airwallex's FX rates are real-time — if a rate is temporarily unavailable, retry or use a fallback currency.

---

Connector implementation: `crates/hyperswitch_connectors/src/connectors/airwallex.rs`.
