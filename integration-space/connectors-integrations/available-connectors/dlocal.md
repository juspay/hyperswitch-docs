---
description: Accept payments through dLocal via Hyperswitch
metaLinks:
  alternates:
    - dlocal.md
---

# dLocal

<div align="left"><img src="https://hyperswitch.io/icons/homePageIcons/logos/dlocalLogo.svg" alt=""></div>

dLocal connects to Hyperswitch as a `PaymentGateway` connector using `SignatureKey` authentication with HMAC-SHA256 request signing. Unlike Bearer token connectors, dLocal authenticates each request by computing an HMAC-SHA256 signature of the request body using the Secret Key, then sending it alongside the Login key and Trans Key in a custom `Authorization` header. All requests use `application/json`. dLocal specializes in emerging market payments — it provides a single API to access local payment methods across Latin America, Africa, and Asia.

### Connector-Specific Notes

* **HMAC-SHA256 request signing:** Every request carries a computed signature in the `Authorization` header, formatted as `V2-HMAC-SHA256, Signature: {hex_encoded_hmac_sha256}`. The HMAC input is `{x_login}{date}` for empty-body requests, or `{x_login}{date}{request_body}` when a body is present, signed with the Secret Key using HMAC-SHA256 and hex-encoded. The Login and Trans Key are sent as separate `X-Login` and `X-Trans-Key` headers respectively — they are not embedded in the `Authorization` value. All three credentials (Login, Secret Key, Trans Key) are required.
* **Credentials location:** Login, Secret Key, and Trans Key are found in your dLocal dashboard.
* **Emerging market focus:** dLocal's value is enabling local payment methods (Boleto, PIX, OXXO, local card schemes) across LatAm, Africa, and Asia through a single integration. The specific methods available depend on your dLocal account's approved countries.
* **Capture methods supported:** Automatic, Manual, SequentialAutomatic (and Automatic for some methods).
* **SetupMandate:** Supported for applicable payment methods.
* For a full list of supported payment methods, visit [hyperswitch.io/pm-list](https://hyperswitch.io/pm-list).

***

### Activating dLocal via Hyperswitch

#### Prerequisites

1. You need to be registered with dLocal. Sign up at [dlocal.com](https://dlocal.com/).
2. You should have a registered Hyperswitch account, accessible from the [Hyperswitch control center](https://app.hyperswitch.io/register).
3. dLocal API keys — **Login**, **Secret Key**, and **Trans Key** — are found in your dLocal dashboard.

[Steps to activate dLocal on the Hyperswitch control center](https://docs.hyperswitch.io/hyperswitch-cloud/connectors/activate-connector-on-hyperswitch)

***

### Responsibility Boundaries

**Hyperswitch owns:** routing decisions, retry scheduling, mandate record storage, HMAC signature construction on each request, and unified error mapping. **dLocal owns:** payment execution, local payment method routing in each market, and country-level compliance. dLocal determines which local payment methods are available based on your merchant account's approved markets — Hyperswitch cannot enable a local method that dLocal has not approved for your account.

**Hyperswitch owns:** computing and sending the HMAC-SHA256 signature on every request. **dLocal owns:** validating that signature. If the Secret Key changes in dLocal and is not updated in Hyperswitch, all requests will fail authentication.

***

### Common Failure Modes

**HMAC signature mismatch** Symptom: All requests fail with a dLocal authentication error. Fix: Verify that all three credentials (Login, Secret Key, Trans Key) in Hyperswitch match the ones in your dLocal dashboard exactly. Any mismatch causes the computed signature to fail dLocal's validation.

**Local payment method unavailable** Symptom: A specific local payment method (e.g. Boleto, PIX) fails with an availability error. Fix: Confirm with dLocal that the specific method and country combination is approved for your merchant account.

**Currency not supported for target market** Symptom: A payment fails with a currency or market error. Fix: dLocal processes payments in local currencies for each market. Verify the currency-country combination is supported by your dLocal account configuration.

***

Connector implementation: `crates/hyperswitch_connectors/src/connectors/dlocal.rs`.
