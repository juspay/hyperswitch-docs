---
description: >-
  Authenticate payments through Juspay's own 3DS Server integrated via Juspay
  Hyperswitch for comprehensive cardholder verification across card networks.
---

# Juspay 3DS Server

Juspay 3DS Server connects to Hyperswitch as an external `AuthenticationProvider`. It is Juspay's own 3DS Server providing comprehensive 3-Domain Secure authentication, cardholder verification, and fraud prevention across card networks. Because it is operated by Juspay, it shares the same trust boundary as Hyperswitch itself.

### Authentication

Juspay 3DS Server uses `HeaderKey` authentication — a single API key sent as a Bearer token on every request.

| Credential | Description |
| --- | --- |
| **API Key** | Bearer token issued during Juspay 3DS Server provisioning |

### 3DS Flows

Juspay 3DS Server handles the following flows within Hyperswitch's external 3DS authentication:

| Flow | Description |
| --- | --- |
| **Pre-Authenticate** | Initiates 3DS authentication — sends card and order details to Juspay's 3DS server |
| **Post-Authenticate** | Completes the flow — retrieves CAVV, ECI, and DS Transaction ID for use in payment authorization |

### Common Failure Modes

**API key rejected**
Symptom: Authentication requests return 401 Unauthorized. Fix: Verify the API key stored in Hyperswitch matches the one provisioned for your Juspay 3DS Server instance.

**Authentication result missing**
Symptom: Post-Authenticate returns empty or incomplete authentication values. Fix: Confirm Pre-Authenticate completed successfully. Check that the card BIN is enrolled in 3DS on the relevant card network.

---

### Activating Juspay 3DS Server via Hyperswitch

#### Prerequisites

1. Juspay 3DS Server provisioned for your account. Contact your Juspay account manager for access.
2. A registered Hyperswitch account, accessible from the [Hyperswitch control center](https://app.hyperswitch.io/).
3. API Key provided during Juspay 3DS Server provisioning.

[Steps to activate a connector on the Hyperswitch control center](../activate-connector-on-hyperswitch/README.md)

---

Connector implementation: `crates/hyperswitch_connectors/src/connectors/juspaythreedsserver.rs`.
