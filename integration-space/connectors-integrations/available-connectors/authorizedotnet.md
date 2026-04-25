---
description: Accept payments through Authorize.net via Hyperswitch
metaLinks:
  alternates:
    - authorizedotnet.md
---

# Authorize.net

Authorize.net connects to Hyperswitch as a `PaymentGateway` connector using `BodyKey` authentication — the API Login ID and Transaction Key are embedded inside the JSON request body under `merchantAuthentication`, not in HTTP headers. All requests use `application/json`. This body-embedded credential pattern is specific to Authorize.net and means the credentials are part of the payload structure, not transport-layer auth.

### Connector-Specific Notes

- **Body-embedded credentials:** Authorize.net's `BodyKey` auth places credentials inside every request payload as `{"merchantAuthentication": {"name": "{api_login_id}", "transactionKey": "{transaction_key}"}}`. There is no `Authorization` header on payment requests — auth is validated by Authorize.net when it parses the request body.
- **Credentials location:** API Login ID and Transaction Key are found in your Authorize.net dashboard under **Account → Security Settings**.
- **Payment method configuration:** Configure accepted payment methods in your Authorize.net dashboard under **Account → Digital Payment Solutions**.
- **Capture methods supported:** Automatic, Manual, SequentialAutomatic.
- **SetupMandate:** Supported for applicable payment methods.
- Authorize.net is a Visa solution focused on the US market — it is a widely-used payment gateway for US merchants accepting credit cards and ACH payments.
- For a full list of supported payment methods, visit [hyperswitch.io/pm-list](https://hyperswitch.io/pm-list).

---

### Activating Authorize.net via Hyperswitch

#### Prerequisites

1. You need to be registered with Authorize.net. Sign up at [authorize.net](https://www.authorize.net/).
2. You should have a registered Hyperswitch account, accessible from the [Hyperswitch control center](https://hyperswitch.io/contact-sales).
3. The **API Login ID** and **Transaction Key** are found in your Authorize.net dashboard under **Account → Security Settings**.
4. Configure accepted payment methods in your Authorize.net dashboard under **Account → Digital Payment Solutions**.

[Steps to activate Authorize.net on the Hyperswitch control center](https://docs.hyperswitch.io/hyperswitch-cloud/connectors/activate-connector-on-hyperswitch)

---

### Responsibility Boundaries

**Hyperswitch owns:** routing decisions, retry scheduling, mandate record storage, and unified error code mapping. **Authorize.net owns:** payment execution, fraud filtering (Advanced Fraud Detection Suite), and ACH processing. Authorize.net's fraud filters run before authorization — a payment rejected by fraud rules is a pre-authorization rejection, not an authorization failure.

**Hyperswitch owns:** embedding credentials correctly in each request body. **Authorize.net owns:** validating those credentials on receipt. Auth errors from Authorize.net are returned inside the response body with code `E00007` (not as HTTP 401) — Hyperswitch maps these to its unified error format.

---

### Common Failure Modes

**Authentication error inside response body**
Symptom: Requests return HTTP 200 but contain error code `E00007` (User Authentication Failed). Fix: Verify the API Login ID and Transaction Key in Hyperswitch match your Authorize.net dashboard exactly. Auth errors are returned in the body, not as HTTP error codes.

**Payment method not enabled**
Symptom: Specific payment methods (e.g. ACH, PayPal) fail with a feature not enabled error. Fix: Enable the required methods in your Authorize.net dashboard under **Account → Digital Payment Solutions**.

**Fraud filter rejection**
Symptom: Payments are declined before authorization with a fraud-related reason code. Fix: Review and adjust your Authorize.net Advanced Fraud Detection Suite settings — these are configured entirely in Authorize.net, not in Hyperswitch.

---

Connector implementation: `crates/hyperswitch_connectors/src/connectors/authorizedotnet.rs`.
