---
description: >-
  Integrate Mollie as a payment connector on Juspay Hyperswitch to accept
  multiple payment methods with seamless checkout and robust security.
metaLinks:
  alternates:
    - mollie.md
---

# Mollie

![logo\_mollie](https://hyperswitch.io/icons/homePageIcons/logos/mollieLogo.svg)

Mollie connects to Hyperswitch as a `PaymentGateway` connector using `HeaderKey` authentication — the API key is passed as `Authorization: Bearer {api_key}` on every request. All requests use `application/json`. Mollie is a European payment service provider with strong coverage of local European payment methods including iDEAL, Bancontact, SOFORT, and Klarna — making it a natural choice for European-first merchants.

### Connector-Specific Notes

- **Bearer token auth:** Single API key passed as a Bearer token. The API key and Password are found in your Mollie dashboard.
- **European payment method coverage:** Mollie natively supports iDEAL (Netherlands), Bancontact (Belgium), SOFORT (DACH), Klarna, and a range of local European methods. The specific methods available depend on your Mollie account's configuration.
- **Capture methods supported:** Automatic, Manual, SequentialAutomatic.
- **SetupMandate:** Supported for applicable payment methods.
- Payment methods must be enabled both in Hyperswitch and in your Mollie dashboard — a mismatch between the two is the most common source of payment failures.
- For a full list of supported payment methods, visit [hyperswitch.io/pm-list](https://hyperswitch.io/pm-list).

---

### Activating Mollie via Hyperswitch

#### Prerequisites

1. You need to be registered with Mollie. Sign up at [mollie.com](https://www.mollie.com/).
2. You should have a registered Hyperswitch account, accessible from the [Hyperswitch control center](https://app.hyperswitch.io/register).
3. Mollie **API Key** and **Password** are found in your Mollie dashboard.
4. Select all payment methods you wish to use Mollie for. Ensure these match the ones configured in your Mollie dashboard.

[Steps to activate Mollie on the Hyperswitch control center](https://docs.hyperswitch.io/hyperswitch-cloud/connectors/activate-connector-on-hyperswitch)

---

### Responsibility Boundaries

**Hyperswitch owns:** routing decisions, retry scheduling, mandate record storage, and unified error code mapping. **Mollie owns:** payment execution, local payment method availability per country, and webhook delivery to Hyperswitch's endpoint. Mollie determines which local methods are available based on your account's approved methods and the customer's country — Hyperswitch routes to Mollie but cannot override Mollie's method availability rules.

**Hyperswitch owns:** forwarding Mollie webhook events to your configured endpoint. **Mollie owns:** delivering webhook events to Hyperswitch's registered endpoint. Payment status will not update automatically if Mollie's webhook delivery fails.

---

### Common Failure Modes

**Payment method not enabled in Mollie dashboard**
Symptom: A payment method selected in Hyperswitch fails with a method availability error from Mollie. Fix: Enable the method in your Mollie dashboard and ensure it matches what is selected in the Hyperswitch connector configuration.

**API key invalid or expired**
Symptom: All requests return an authentication error from Mollie. Fix: Verify the API key in Hyperswitch matches your Mollie dashboard. Mollie uses separate keys for test and live environments — ensure you are using the correct environment key.

**Webhook delivery failure**
Symptom: Payments complete at Mollie but Hyperswitch status is not updated. Fix: Verify the Hyperswitch webhook endpoint is correctly registered in your Mollie dashboard.

---

Connector implementation: `crates/hyperswitch_connectors/src/connectors/mollie.rs`.
