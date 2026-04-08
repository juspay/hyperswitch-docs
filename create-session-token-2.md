# Create Session Token

## Overview

The `create_session_token` method creates a session token for payment processing. This maintains state across multiple operations.

**Business Use Case:** Multi-step payment flows like 3DS authentication require session state.

## Purpose

| Scenario           | Benefit          |
| ------------------ | ---------------- |
| 3DS authentication | Maintain context |
| Redirect payments  | Preserve state   |

## Request Fields

| Field                 | Type  | Required | Description                   |
| --------------------- | ----- | -------- | ----------------------------- |
| `merchant_session_id` | str   | Yes      | Your unique session reference |
| `amount`              | Money | Yes      | Payment amount                |
| `test_mode`           | bool  | No       | Use test environment          |

## Response Fields

| Field           | Type | Description          |
| --------------- | ---- | -------------------- |
| `session_token` | str  | Token for operations |
| `status_code`   | int  | HTTP status code     |

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
    "merchant_session_id": "session_001",
    "amount": {
        "minor_amount": 10000,
        "currency": "USD"
    },
    "test_mode": True
}

response = await auth_client.create_session_token(request)
```

### Response

```python
{
    "session_token": "sess_1234567890abcdef",
    "status_code": 200
}
```

## Next Steps

* [create\_sdk\_session\_token](create-sdk-session-token-2.md) - Wallet sessions
