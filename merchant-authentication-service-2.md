# Merchant Authentication Service Overview

## Overview

The Merchant Authentication Service generates secure credentials for accessing payment processor APIs using the Python SDK. These short-lived tokens provide secure access without storing secrets client-side.

**Business Use Cases:**

* **Frontend SDKs** - Generate tokens for client-side payment flows
* **Wallet payments** - Initialize Apple Pay, Google Pay sessions
* **Session management** - Maintain secure state across payment operations
* **Multi-party payments** - Secure delegated access

## Operations

| Operation                                                   | Description                                                                                  | Use When                           |
| ----------------------------------------------------------- | -------------------------------------------------------------------------------------------- | ---------------------------------- |
| [`create_access_token`](create-access-token-2.md)           | Generate short-lived connector authentication token. Provides secure API access credentials. | Need temporary API access token    |
| [`create_session_token`](create-session-token-2.md)         | Create session token for payment processing. Maintains session state across operations.      | Starting a multi-step payment flow |
| [`create_sdk_session_token`](create-sdk-session-token-2.md) | Initialize wallet payment sessions. Sets up Apple Pay, Google Pay context.                   | Enabling wallet payments           |

## SDK Setup

```python
from hyperswitch_prism import MerchantAuthenticationClient

auth_client = MerchantAuthenticationClient(
    connector='stripe',
    api_key='YOUR_API_KEY',
    environment='SANDBOX'
)
```

## Common Patterns

### Token Lifecycle

```mermaid
sequenceDiagram
    participant App as Your App
    participant CS as Prism
    participant PP as Payment Provider

    Note over App: Need temporary access
    App->>CS: create_access_token
    CS->>PP: Request token
    PP-->>CS: Return short-lived token
    CS-->>App: Return access_token
    Note over App: Use token for API calls
    App->>PP: API call with token
    PP-->>App: API response
    Note over App: Token expires
```

**Flow Explanation:**

1. **Request token** - Call `create_access_token` when you need temporary access.
2. **Use token** - Include the token in API calls to the connector.
3. **Token expires** - Tokens are short-lived; request new ones as needed.

## Security Best Practices

* Never store tokens long-term
* Use tokens immediately after creation
* Handle token expiration gracefully
* Use HTTPS for all token transmissions

## Next Steps

* [Payment Service](payment-service-2.md) - Use tokens for payment operations
* [Payment Method Authentication Service](payment-method-authentication-service-2.md) - 3D Secure authentication
