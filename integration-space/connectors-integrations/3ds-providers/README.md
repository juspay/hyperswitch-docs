---
description: >-
  Connect external 3DS authentication providers to Juspay Hyperswitch for
  EMV 3DS 2.X cardholder verification independent of the payment processor.
icon: lock
---

# 3DS Providers

Juspay Hyperswitch supports external 3DS authentication providers as a distinct connector category — classified as `AuthenticationProvider`. These connectors handle only the EMV 3DS 2.X authentication phase. The resulting authentication values (CAVV, ECI, DS Transaction ID) are then passed to the payment processor for authorization.

### Native PSP 3DS vs External 3DS Provider

| | Native PSP 3DS | External 3DS Provider |
| --- | --- | --- |
| **How it works** | The payment processor runs its own 3DS server | Hyperswitch calls an external 3DS server before the payment processor |
| **When to use** | Default — supported by most PSPs | When you need 3DS independently of the PSP, or when the PSP doesn't support native 3DS (e.g. Authorize.net) |
| **Control** | Managed by the PSP | Full control over 3DS server, ACS routing, and authentication data |

### Supported 3DS Providers

| Provider | Integration Status | Description |
| --- | --- | --- |
| **Netcetera** | Live | EMV 3DS 2.X processing via TLS client certificate authentication. Handles Pre-Authenticate and Post-Authenticate flows. |
| **GPayments** | Live | 3DS MPI/ACS services supporting Visa Secure, Mastercard SecureCode, and global card authentication standards |
| **Juspay 3DS Server** | Live | Juspay's own 3DS Server for comprehensive 3-Domain Secure authentication, cardholder verification, and fraud prevention across card networks |
| **3dsecure.io** | Sandbox | 3-D Secure verification for online card transactions via a JSON API |

### Activating a 3DS Provider

3DS providers are activated through the same connector onboarding flow as payment processors. For Netcetera specifically, activation requires a TLS client certificate and private key provisioned by Netcetera — not an API key.

[Steps to activate a connector on the Hyperswitch control center](../activate-connector-on-hyperswitch/README.md)

[Netcetera configuration details](netcetera.md)
