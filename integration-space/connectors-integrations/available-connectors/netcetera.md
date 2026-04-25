---
description: >-
  Authenticate payments through Netcetera's EMV 3DS 2.X processing ecosystem
  integrated via Juspay Hyperswitch as an external 3DS authentication provider.
metaLinks:
  alternates:
    - netcetera.md
---

# Netcetera

Netcetera connects to Hyperswitch as an external 3DS authentication provider using `CertificateAuth` — a TLS client certificate and private key are required to establish authenticated connections with Netcetera's 3DS server. Unlike API key or Bearer token connectors, Netcetera authenticates at the TLS transport layer using a client certificate. Netcetera is not a payment gateway; it performs EMV 3DS 2.X authentication only — payment execution is handled by the acquirer/gateway after authentication.

### Connector-Specific Notes

- **TLS client certificate authentication:** Netcetera uses `CertificateAuth` — a certificate (PEM format) and corresponding private key are required. These are used to establish mutual TLS with Netcetera's 3DS server. There is no API key or Bearer token header; authentication happens at the connection layer.
- **External 3DS server, not a payment gateway:** Netcetera handles only the 3DS authentication phase (Pre-Authenticate and Post-Authenticate flows). The resulting authentication values (CAVV, ECI, DS Transaction ID) are then passed to the acquirer for authorization. Netcetera does not process payments, captures, or refunds.
- **Credentials location:** Certificate and Private Key are provisioned by Netcetera and provided during onboarding.
- Netcetera offers EMV® 3DS 2.X transaction processing and is incorporated into the merchant environment to process in-app and web payments based on the 3DS 2.X standard.

---

### Activating Netcetera via Hyperswitch

#### Prerequisites

1. You need to be registered with Netcetera for 3DS server access. Contact [netcetera.com](https://www.netcetera.com/) for onboarding.
2. You should have a registered Hyperswitch account, accessible from the [Hyperswitch control center](https://app.hyperswitch.io/).
3. Netcetera **Certificate** and **Private Key** are provided during the Netcetera onboarding process.

[Steps to activate Netcetera on the Hyperswitch control center](../../../integration-guide/workflows/3ds-decision-manager/external-authentication-for-3ds.md)

[Steps to integrate Netcetera in Hyperswitch Payments SDK](../../merchant-controls/payment-features/3d-secure-3ds/netcetera.md)

---

### Responsibility Boundaries

**Hyperswitch owns:** initiating the 3DS authentication flow (Pre-Authenticate), completing it (Post-Authenticate), and passing the resulting authentication values to the payment connector for authorization. **Netcetera owns:** 3DS server processing, ACS communication, and authentication result delivery.

**Hyperswitch owns:** presenting the correct client certificate on every TLS connection to Netcetera. **Netcetera owns:** validating the certificate and rejecting unauthorized connections. If the certificate expires or is revoked and not renewed in Hyperswitch, all 3DS authentication requests will fail.

---

### Common Failure Modes

**TLS certificate rejected**
Symptom: All 3DS authentication requests fail at the connection level. Fix: Verify the Certificate and Private Key stored in Hyperswitch match the ones provisioned by Netcetera. If the certificate has expired, renew it through Netcetera and update Hyperswitch.

**Authentication result not available**
Symptom: Post-Authenticate flow fails or returns missing authentication values. Fix: Confirm the Pre-Authenticate step completed successfully and that Netcetera's ACS communication was uninterrupted. Check Netcetera's logs for the 3DS server transaction ID.

---

Connector implementation: `crates/hyperswitch_connectors/src/connectors/netcetera.rs`.
