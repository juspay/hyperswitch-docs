# Create Access Token

## Overview

The `create_access_token` method generates a short-lived authentication token for accessing payment processor APIs.

**Business Use Case:** Your frontend needs to initialize a payment widget. Generate a temporary token for client-side use.

## Purpose

| Scenario         | Benefit                           |
| ---------------- | --------------------------------- |
| Frontend SDKs    | Secure client-side initialization |
| Delegated access | Scoped tokens for third parties   |

## Request Fields

| Field        | Type | Required | Description               |
| ------------ | ---- | -------- | ------------------------- |
| `scope`      | str  | No       | Token scope               |
| `expires_in` | int  | No       | Token lifetime in seconds |

## Response Fields

| Field          | Type | Description          |
| -------------- | ---- | -------------------- |
| `access_token` | str  | The token string     |
| `token_type`   | str  | Bearer               |
| `expires_in`   | int  | Seconds until expiry |
| `status_code`  | int  | HTTP status code     |

## Example

### SDK Setup

```python
from hyperswitch_prism import MerchantAuthenticationClient

auth_client = MerchantAuthenticationClient(
    connector='stripe',
    api_key='YOUR_API_KEY',
    environment='SANDBOX'
)
```

### Request

```python
request = {
    "scope": "payment:write",
    "expires_in": 3600
}

response = await auth_client.create_access_token(request)
```

### Response

```python
{
    "access_token": "sk_test_xxx",
    "token_type": "Bearer",
    "expires_in": 3600,
    "status_code": 200
}
```

## Next Steps

* [create\_session\_token](create-session-token-2.md) - Create session tokens
