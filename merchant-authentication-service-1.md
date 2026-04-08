# Merchant Authentication Service Overview

## Overview

The Merchant Authentication Service generates secure credentials for accessing payment processor APIs using the Node.js SDK. These short-lived tokens provide secure access without storing secrets client-side.

**Business Use Cases:**

* **Frontend SDKs** - Generate tokens for client-side payment flows
* **Wallet payments** - Initialize Apple Pay, Google Pay sessions
* **Session management** - Maintain secure state across payment operations
* **Multi-party payments** - Secure delegated access

## Operations

| Operation                                                | Description                                                                                  | Use When                           |
| -------------------------------------------------------- | -------------------------------------------------------------------------------------------- | ---------------------------------- |
| [`createAccessToken`](create-access-token-1.md)          | Generate short-lived connector authentication token. Provides secure API access credentials. | Need temporary API access token    |
| [`createSessionToken`](create-session-token-1.md)        | Create session token for payment processing. Maintains session state across operations.      | Starting a multi-step payment flow |
| [`createSdkSessionToken`](create-sdk-session-token-1.md) | Initialize wallet payment sessions. Sets up Apple Pay, Google Pay context.                   | Enabling wallet payments           |

## SDK Setup

```javascript
const { MerchantAuthenticationClient } = require('hyperswitch-prism');

const authClient = new MerchantAuthenticationClient({
    connector: 'stripe',
    apiKey: 'YOUR_API_KEY',
    environment: 'SANDBOX'
});
```

## Security Best Practices

* Never store tokens long-term
* Use tokens immediately after creation
* Handle token expiration gracefully
* Use HTTPS for all token transmissions

## Next Steps

* [Payment Service](payment-service-1.md) - Use tokens for payment operations
* [Payment Method Authentication Service](payment-method-authentication-service-1.md) - 3D Secure authentication
