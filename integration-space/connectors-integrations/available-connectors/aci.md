---
description: >-
  Accept and manage digital payments through ACI Worldwide via Hyperswitch —
  supports omni-commerce, bill payments, and fraud management.
metaLinks:
  alternates:
    - aci.md
---

# ACI

<div align="left"><img src="https://hyperswitch.io/icons/homePageIcons/logos/ACILogo.svg" alt=""></div>

ACI connects to Hyperswitch as a `PaymentGateway` connector using `BodyKey` authentication — the API Key is sent as `Authorization: Bearer {api_key}` in the HTTP header, while the Entity ID is embedded in the form-encoded request body as `TransactionDetails.entity_id` on every request. All requests use `application/x-www-form-urlencoded`. ACI also delivers encrypted webhook events using AES-256-GCM — the payload is sent hex-encoded in the body, with decryption metadata (IV and auth tag) in HTTP headers.

### Connector-Specific Notes

* **Bearer token header + Entity ID in body:** ACI uses `BodyKey` auth, but the two credentials serve different roles. The API Key is transmitted as `Authorization: Bearer {api_key}` in the HTTP header. The Entity ID is placed inside the form-encoded body (as part of `TransactionDetails`) on every payment and cancel request — it identifies the merchant entity in ACI's multi-tenant platform and is required on every request.
* **Form-encoded requests:** All ACI payment requests use `application/x-www-form-urlencoded`, not JSON. This is distinct from most other connectors in Hyperswitch.
* **AES-256-GCM webhook encryption:** ACI delivers webhook payloads as hex-encoded AES-256-GCM ciphertext in the request body. The IV is provided in the `X-Initialization-Vector` header (hex-encoded), and the GCM auth tag is in the `X-Authentication-Tag` header (hex-encoded). Hyperswitch decrypts the payload using the webhook secret (32-byte key) before processing the event. If either header is missing, webhook verification fails.
* **Capture methods supported:** Automatic and Manual.
* **SetupMandate:** Supported for applicable payment methods.
* ACI Worldwide supports omni-commerce (online, in-store, mobile), bill payments, and has built-in fraud management capabilities.
* For a full list of supported payment methods, visit [hyperswitch.io/pm-list](https://hyperswitch.io/pm-list).

***

### Activating ACI via Hyperswitch

#### Prerequisites

1. You need to be registered with ACI. Sign up at [aciworldwide.com](https://www.aciworldwide.com/).
2. You should have a registered Hyperswitch account, accessible from the [Hyperswitch control center](https://app.hyperswitch.io/).
3. ACI **API Key** and **Entity ID** are found in your ACI dashboard.

[Steps to activate ACI on the Hyperswitch control center](https://docs.hyperswitch.io/hyperswitch-cloud/connectors/activate-connector-on-hyperswitch)

***

### Responsibility Boundaries

**Hyperswitch owns:** routing decisions, retry scheduling, mandate record storage, and constructing the form-encoded request body with both credentials. **ACI owns:** payment execution, fraud evaluation, and entity-level routing within its platform. The Entity ID determines which ACI merchant entity processes the payment — Hyperswitch passes it on every request but does not validate ACI's internal entity configuration.

**Hyperswitch owns:** sending the API Key in the `Authorization: Bearer` header and embedding the Entity ID in every form-encoded request body. **ACI owns:** validating the API Key and Entity ID combination. If the Entity ID is incorrect or the API Key is mismatched, ACI returns an authentication error in the response body. If the webhook secret is incorrect or either `X-Initialization-Vector` / `X-Authentication-Tag` header is absent, webhook decryption fails and the event is not processed.

***

### Common Failure Modes

**Authentication failure (API Key)** Symptom: All requests fail with an ACI 401 or authentication error. Fix: Verify the API Key in Hyperswitch matches your ACI dashboard. The API Key is sent as `Authorization: Bearer {api_key}` — do not manually encode it before entering in the control center.

**Entity ID mismatch** Symptom: Payments fail with an ACI entity or merchant error. Fix: Verify the Entity ID in Hyperswitch matches the one in your ACI dashboard. The Entity ID is embedded in the form-encoded request body and must correspond to the correct merchant entity in your ACI account.

**Webhook decryption failure** Symptom: ACI webhooks arrive at Hyperswitch but events are not processed. Fix: ACI encrypts webhook payloads with AES-256-GCM. Verify the webhook secret in Hyperswitch matches the 32-byte key ACI uses. Also ensure the `X-Initialization-Vector` and `X-Authentication-Tag` headers are present in each webhook request — if either is missing, decryption fails.

**Payment method not configured for entity** Symptom: A payment method fails with an availability error. Fix: Confirm the payment method is enabled for the specific Entity ID configured in Hyperswitch — ACI's method availability is scoped to each entity.

***

Connector implementation: `crates/hyperswitch_connectors/src/connectors/aci.rs`.
