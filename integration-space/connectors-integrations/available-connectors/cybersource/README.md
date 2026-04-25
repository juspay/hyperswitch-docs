---
description: >-
  Accept payments globally through CyberSource via Juspay Hyperswitch with
  support for multiple payment methods and geographies.
metaLinks:
  alternates:
    - ./
---

# Cybersource

![CyberSource Logo](https://hyperswitch.io/icons/homePageIcons/logos/CybersourceLogo.svg)

CyberSource connects to Hyperswitch as a `PaymentGateway` connector using `SignatureKey` authentication — API Key, Merchant ID, and Secret Key. Unlike connectors that use a simple Bearer token, CyberSource authenticates requests using an HTTP Signature scheme: Hyperswitch computes an HMAC-SHA256 digest of the request headers and body, then sends it as `Authorization: Signature keyId="{merchant_id}",algorithm="HmacSHA256",...`. All requests use `application/json;charset=utf-8`. CyberSource also supports incremental authorization and payouts — two capabilities not universally available across connectors.

### Connector-Specific Notes

- **HTTP Signature authentication:** CyberSource does not use Bearer tokens. Every request carries a computed HMAC-SHA256 signature over the request headers and body. The API Key, Merchant ID, and Secret Key are all required to construct this signature. Missing or incorrect credentials produce authentication errors, not 401s — the error format is specific to CyberSource's API response structure.
- **Incremental authorization:** CyberSource supports incrementally increasing an authorized amount before capture. This is available via Hyperswitch's `IncrementalAuthorization` flow, and requires `capture_method: manual` on the original payment.
- **Payouts:** CyberSource supports payout fulfillment through Hyperswitch's unified payouts interface.
- **Apple Pay and Google Pay:** Both wallets have specific setup steps for CyberSource due to its certificate-based payment processing model. See the dedicated subpages:
  - [Apple Pay via CyberSource](apple-pay.md)
  - [Google Pay via CyberSource](google-pay.md)
- **Required fields for Apple Pay and Google Pay:** Both wallets require `email` and full billing address (First Name, Last Name, Address Line 1, Zip/Postal Code, City, State, Country) to be present on the payment request. Pass these when creating the Payment Intent — if not provided, the Hyperswitch SDK will collect them from the customer at checkout.
- **Capture methods supported:** Automatic, Manual, SequentialAutomatic.
- For a full list of supported payment methods, visit [hyperswitch.io/pm-list](https://hyperswitch.io/pm-list).

---

### Activating CyberSource via Hyperswitch

#### Prerequisites

1. You need to be registered with CyberSource. Sign up at [cybersource.com](https://www.cybersource.com/en-gb.html).
2. You should have a registered Hyperswitch account, accessible from the [Hyperswitch control center](https://app.hyperswitch.io/register).
3. CyberSource API credentials — **API Key**, **Secret Key**, and **Merchant ID** — are found in your CyberSource dashboard.
4. Select all payment methods you wish to use CyberSource for. Ensure these match the ones configured in your CyberSource dashboard.

[Steps to activate CyberSource on the Hyperswitch control center](https://docs.hyperswitch.io/hyperswitch-cloud/connectors/activate-connector-on-hyperswitch)

---

### Responsibility Boundaries

**Hyperswitch owns:** routing decisions, mandate record storage, incremental authorization orchestration, retry scheduling, and webhook fan-out. **CyberSource owns:** payment execution, fraud scoring (Decision Manager), and payout disbursement. CyberSource's Decision Manager runs independently of Hyperswitch — fraud decisions are made by CyberSource before the authorization response is returned, not after.

**Hyperswitch owns:** constructing and signing the HTTP Signature on every request. **CyberSource owns:** validating that signature against the stored API credentials. If the Merchant ID, API Key, or Secret Key changes on the CyberSource side and is not updated in Hyperswitch, all subsequent requests will fail signature validation.

---

### Common Failure Modes

**HTTP Signature validation failure**
Symptom: All requests return a CyberSource authentication error. Fix: Verify that all three credentials (API Key, Merchant ID, Secret Key) in Hyperswitch match exactly what is configured in your CyberSource Business Center. Any mismatch in any of the three fields causes signature validation to fail.

**Apple Pay or Google Pay payment failure**
Symptom: Wallet payments fail with a CyberSource validation error. Fix: Ensure `email` and full billing address fields are present on the payment request. See [Apple Pay via CyberSource](apple-pay.md) and [Google Pay via CyberSource](google-pay.md) for the specific certificate and credential setup steps.

**Incremental authorization rejected**
Symptom: Incremental authorization call fails. Fix: Incremental authorization requires `capture_method: manual` on the original payment. CyberSource does not support incremental authorization on automatically-captured payments.

**Payout failure due to missing recipient details**
Symptom: Payout fulfillment fails with a recipient validation error. Fix: CyberSource payouts require complete recipient information. Ensure all required recipient fields are populated before initiating the payout.

---

Connector implementation: `crates/hyperswitch_connectors/src/connectors/cybersource.rs`. For wallet-specific setup, see [Apple Pay](apple-pay.md) and [Google Pay](google-pay.md) subpages.
