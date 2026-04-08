# Payment Method Authentication Service Overview

## Overview

The Payment Method Authentication Service manages 3D Secure (3DS) authentication flows using the Node.js SDK. 3DS adds an extra layer of security for online card payments by verifying the cardholder's identity with their bank.

**Business Use Cases:**

* **Fraud prevention** - Shift liability to issuers for authenticated transactions
* **Regulatory compliance** - Meet Strong Customer Authentication (SCA) requirements
* **Risk-based** - Request 3DS for high-risk transactions
* **Global payments** - Required for many European and international transactions

## Operations

| Operation                                    | Description                                                                       | Use When                                     |
| -------------------------------------------- | --------------------------------------------------------------------------------- | -------------------------------------------- |
| [`preAuthenticate`](pre-authenticate-1.md)   | Initiate 3DS flow before payment. Collects device data for authentication.        | Starting 3D Secure flow                      |
| [`authenticate`](authenticate-1.md)          | Execute 3DS challenge or frictionless verification. Performs bank authentication. | After preAuthenticate, complete the 3DS flow |
| [`postAuthenticate`](post-authenticate-1.md) | Validate authentication results with issuer. Confirms authentication decision.    | After customer completes 3DS challenge       |

## SDK Setup

```javascript
const { PaymentMethodAuthenticationClient } = require('hyperswitch-prism');

const authClient = new PaymentMethodAuthenticationClient({
    connector: 'stripe',
    apiKey: 'YOUR_API_KEY',
    environment: 'SANDBOX'
});
```

## 3DS Flow

| Flow             | User Experience      | When It Happens                                 |
| ---------------- | -------------------- | ----------------------------------------------- |
| **Frictionless** | No interruption      | Low risk, returning customer, device recognized |
| **Challenge**    | Customer enters code | High risk, new device, large amount             |

## Next Steps

* [Payment Service](payment-service-1.md) - Complete payment after 3DS
* [authorize](authorize-1.md) - Use 3DS result for authorization
