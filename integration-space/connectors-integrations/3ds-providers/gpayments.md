---
description: >-
  Authenticate payments through GPayments 3DS MPI/ACS services integrated via
  Juspay Hyperswitch as an external 3DS authentication provider.
---

# GPayments

GPayments connects to Hyperswitch as an external `AuthenticationProvider` using `CertificateAuth` — a TLS client certificate and private key are required to establish authenticated connections with GPayments' ActiveServer. GPayments supports Visa Secure, Mastercard SecureCode, and global card authentication standards. GPayments is not a payment gateway; it handles only the EMV 3DS 2.X authentication phase.

### Authentication

GPayments uses `CertificateAuth` — mutual TLS with a client certificate and private key. There is no API key or Bearer token.

| Credential | Description |
| --- | --- |
| **Certificate** | Base64-encoded PEM certificate provisioned by GPayments |
| **Private Key** | Base64-encoded PEM private key corresponding to the certificate |

### 3DS Flows

GPayments handles the following flows within Hyperswitch's external 3DS authentication:

| Flow | Description |
| --- | --- |
| **Pre-Authenticate** | Initiates 3DS authentication — sends card and order details to GPayments' 3DS server |
| **Post-Authenticate** | Completes the flow — retrieves CAVV, ECI, and DS Transaction ID for use in payment authorization |

### Common Failure Modes

**TLS certificate rejected**
Symptom: All authentication requests fail at the connection level. Fix: Verify the Certificate and Private Key stored in Hyperswitch match those provisioned by GPayments. If the certificate has expired, renew it through GPayments and update Hyperswitch.

**Authentication result not available**
Symptom: Post-Authenticate returns missing or incomplete authentication values. Fix: Confirm Pre-Authenticate completed successfully and that GPayments' ACS communication was uninterrupted. Check GPayments logs for the 3DS server transaction ID.

---

### Activating GPayments via Hyperswitch

#### Prerequisites

1. A registered GPayments merchant account. Contact [gpayments.com](https://www.gpayments.com/) for onboarding.
2. A registered Hyperswitch account, accessible from the [Hyperswitch control center](https://app.hyperswitch.io/).
3. Certificate and Private Key provisioned by GPayments during onboarding.

[Steps to activate a connector on the Hyperswitch control center](../activate-connector-on-hyperswitch/README.md)

---

Connector implementation: `crates/hyperswitch_connectors/src/connectors/gpayments.rs`.
