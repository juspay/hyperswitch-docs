---
description: >-
  Accept and manage digital payments through ACI Worldwide via Hyperswitch —
  supports omni-commerce, bill payments, and fraud management.
metaLinks:
  alternates:
    - aci.md
---

# ACI

![](https://hyperswitch.io/icons/homePageIcons/logos/ACILogo.svg)

ACI connects to Hyperswitch as a `PaymentGateway` connector using `BodyKey` authentication — the API Key and Entity ID are embedded in the request body (using `application/x-www-form-urlencoded`), not in HTTP headers. The Entity ID identifies the specific merchant entity within ACI's platform and is required on every payment request alongside the API key.

### Connector-Specific Notes

- **BodyKey auth with Entity ID:** ACI's auth embeds both the API Key and Entity ID in the form-encoded request body. The Entity ID scopes requests to a specific merchant entity in ACI's multi-tenant platform — it is not a secondary credential, it is a routing identifier. Both values are found in your ACI dashboard.
- **Form-encoded requests:** All ACI payment requests use `application/x-www-form-urlencoded`, not JSON. This is distinct from most other connectors in Hyperswitch.
- **Capture methods supported:** Automatic and Manual.
- **SetupMandate:** Supported for applicable payment methods.
- ACI Worldwide supports omni-commerce (online, in-store, mobile), bill payments, and has built-in fraud management capabilities.
- For a full list of supported payment methods, visit [hyperswitch.io/pm-list](https://hyperswitch.io/pm-list).

---

### Activating ACI via Hyperswitch

#### Prerequisites

1. You need to be registered with ACI. Sign up at [aciworldwide.com](https://www.aciworldwide.com/).
2. You should have a registered Hyperswitch account, accessible from the [Hyperswitch control center](https://app.hyperswitch.io/).
3. ACI **API Key** and **Entity ID** are found in your ACI dashboard.

[Steps to activate ACI on the Hyperswitch control center](https://docs.hyperswitch.io/hyperswitch-cloud/connectors/activate-connector-on-hyperswitch)

---

### Responsibility Boundaries

**Hyperswitch owns:** routing decisions, retry scheduling, mandate record storage, and constructing the form-encoded request body with both credentials. **ACI owns:** payment execution, fraud evaluation, and entity-level routing within its platform. The Entity ID determines which ACI merchant entity processes the payment — Hyperswitch passes it on every request but does not validate ACI's internal entity configuration.

**Hyperswitch owns:** embedding credentials in each request body. **ACI owns:** validating the API Key and Entity ID combination. If the Entity ID is incorrect or the API Key is mismatched, ACI returns an authentication error in the response body.

---

### Common Failure Modes

**Entity ID mismatch**
Symptom: Payments fail with an ACI authentication or entity error. Fix: Verify both the API Key and Entity ID in Hyperswitch match the ones in your ACI dashboard. The Entity ID must correspond to the correct merchant entity in your ACI account.

**Payment method not configured for entity**
Symptom: A payment method fails with an availability error. Fix: Confirm the payment method is enabled for the specific Entity ID configured in Hyperswitch — ACI's method availability is scoped to each entity.

---

Connector implementation: `crates/hyperswitch_connectors/src/connectors/aci.rs`.
