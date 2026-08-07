---
description: >-
  Authenticate payments through 3dsecure.io's JSON API integrated via Juspay
  Hyperswitch as an external 3DS authentication provider.
---

# 3dsecure.io

3dsecure.io connects to Hyperswitch as an external `AuthenticationProvider`. It facilitates 3-D Secure verification for online credit and debit card transactions via a JSON API. 3dsecure.io is currently available in Sandbox status on Hyperswitch — it is not yet available for live production traffic.

### Authentication

3dsecure.io uses `HeaderKey` authentication — a single API key sent as a Bearer token on every request.

| Credential | Description |
| --- | --- |
| **API Key** | Bearer token issued by 3dsecure.io. Obtained during 3dsecure.io onboarding. |

### 3DS Flows

3dsecure.io handles the following flows within Hyperswitch's external 3DS authentication:

| Flow | Description |
| --- | --- |
| **Pre-Authenticate** | Initiates 3DS authentication — sends card and order details to 3dsecure.io's 3DS server |
| **Post-Authenticate** | Completes the flow — retrieves CAVV, ECI, and DS Transaction ID for use in payment authorization |

### Sandbox Status

3dsecure.io is available for sandbox/testing use on Hyperswitch. Use this connector to test external 3DS authentication flows before enabling a production 3DS provider.

### Common Failure Modes

**API key rejected**
Symptom: Authentication requests return 401 Unauthorized. Fix: Verify the API key stored in Hyperswitch matches the one issued by 3dsecure.io. Keys are environment-specific — sandbox keys do not work in production.

**Authentication not completed**
Symptom: Post-Authenticate returns no result. Fix: Confirm Pre-Authenticate was called first and returned a valid transaction ID. The 3DS flow must follow the pre/post sequence.

---

### Activating 3dsecure.io via Hyperswitch

#### Prerequisites

1. A registered 3dsecure.io account. Contact [3dsecure.io](https://3dsecure.io/) for onboarding.
2. A registered Hyperswitch account, accessible from the [Hyperswitch control center](https://app.hyperswitch.io/).
3. API Key provided during 3dsecure.io onboarding.

[Steps to activate a connector on the Hyperswitch control center](../activate-connector-on-hyperswitch/README.md)

---

Connector implementation: `crates/hyperswitch_connectors/src/connectors/threedsecureio.rs`.
