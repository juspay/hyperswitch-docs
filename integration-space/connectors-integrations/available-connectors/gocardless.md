---
description: >-
  Accept bank payments, Direct Debit, and Open Banking via GoCardless through
  Juspay Hyperswitch.
metaLinks:
  alternates:
    - gocardless.md
---

# GoCardless

GoCardless connects to Hyperswitch as a `PaymentGateway` connector using `HeaderKey` authentication — the Access Token is sent as `Authorization: Bearer {access_token}` on every request. All requests also include a `GoCardless-Version: 2015-07-06` header that pins the API version. All requests use `application/json`. GoCardless specialises in bank-pull payments: Direct Debit, recurring bank debits, and Open Banking.

### Connector-Specific Notes

- **Bearer token auth with version header:** GoCardless uses a static Access Token (not a rotating OAuth token) as the Bearer credential. Every request also sends `GoCardless-Version: 2015-07-06` to pin the API version. This version is fixed in the Hyperswitch implementation.
- **Credentials location:** Access Token is found in your GoCardless dashboard under **Developers → Create → Access Token**.
- **Webhook verification:** GoCardless signs webhook events with HMAC-SHA256. Configure the Hyperswitch webhook endpoint in your GoCardless dashboard and store the webhook signing secret.
- **Capture methods supported:** Automatic, SequentialAutomatic. Manual capture is not supported.
- **SetupMandate:** Supported for applicable payment methods (Direct Debit mandates).
- GoCardless specialises in bank payments (Direct Debit, ACH, SEPA, BACS) and recurring payment collection. It is widely used in Europe, US, and ANZ for subscription billing and invoice collection.
- For a full list of supported payment methods, visit [hyperswitch.io/pm-list](https://hyperswitch.io/pm-list).

---

### Activating GoCardless via Hyperswitch

#### Prerequisites

1. You need to be registered with GoCardless. Sign up at [manage-sandbox.gocardless.com](https://manage-sandbox.gocardless.com/sign-up).
2. You should have a registered Hyperswitch account, accessible from the [Hyperswitch control center](https://app.hyperswitch.io/).
3. GoCardless **Access Token** is found in your GoCardless dashboard under **Developers → Create → Access Token**.
4. Select all payment methods you wish to use GoCardless for. Ensure these match the ones configured in your GoCardless dashboard.

[Steps to activate GoCardless on the Hyperswitch control center](https://docs.hyperswitch.io/hyperswitch-cloud/connectors/activate-connector-on-hyperswitch)

---

### Responsibility Boundaries

**Hyperswitch owns:** routing decisions, retry scheduling, Direct Debit mandate reference storage, sending the Access Token as the Bearer credential and pinning the API version on every request, and unified error mapping. **GoCardless owns:** payment execution, bank debit collection, mandate management, and webhook delivery.

**Hyperswitch owns:** presenting the correct Access Token on every request. **GoCardless owns:** validating it. If the Access Token is revoked in GoCardless and not replaced in Hyperswitch, all requests will fail authentication immediately.

---

### Common Failure Modes

**Authentication failure**
Symptom: All requests fail with a GoCardless 401 or authentication error. Fix: Verify the Access Token in Hyperswitch matches the one generated in your GoCardless dashboard under **Developers → Access Tokens**. If the token was revoked or rotated, generate a new one and update Hyperswitch.

**Mandate setup failure**
Symptom: Direct Debit mandate setup fails or mandate reference is rejected on subsequent charges. Fix: Verify the payment method type and customer bank details are correctly provided in the SetupMandate request. GoCardless mandates require valid bank account details specific to each payment scheme (BACS, SEPA, ACH).

**Webhook verification failure**
Symptom: GoCardless webhooks arrive at Hyperswitch but events are not processed. Fix: Verify the webhook signing secret stored in Hyperswitch matches the one GoCardless uses to sign events. Mismatched secrets cause HMAC-SHA256 verification to fail.

---

Connector implementation: `crates/hyperswitch_connectors/src/connectors/gocardless.rs`.
