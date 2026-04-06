---
title: createSessionToken (Node.js SDK)
description: Create session tokens for payment processing to maintain state across multi-step payment flows
tags:
  - node
  - session
  - tokens
---

# createSessionToken Method

## Overview

The `createSessionToken` method creates a session token for payment processing. This token maintains state across multiple payment operations, enabling secure tracking for multi-step payment flows.

**Business Use Case:** When processing payments that require multiple steps (3DS authentication, redirect flows), you need to maintain session state between requests.

## Purpose

| Scenario | Benefit |
|----------|---------|
| 3DS authentication | Maintain context through challenge flow |
| Redirect payments | Preserve state during bank redirects |
| Multi-step checkout | Track progress across pages |

## Request Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `merchantSessionId` | string | Yes | Your unique session reference |
| `amount` | Money | Yes | Payment amount for this session |
| `metadata` | object | No | Additional metadata |
| `testMode` | boolean | No | Use test environment |

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `sessionToken` | string | Token for subsequent operations |
| `statusCode` | number | HTTP status code |

## Example

### SDK Setup

```javascript
const { MerchantAuthenticationClient } = require('hyperswitch-prism');

const authClient = new MerchantAuthenticationClient({
    connector: 'stripe',
    apiKey: 'YOUR_API_KEY',
    environment: 'SANDBOX'
});
```

### Request

```javascript
const request = {
    merchantSessionId: "session_001",
    amount: {
        minorAmount: 10000,
        currency: "USD"
    },
    testMode: true
};

const response = await authClient.createSessionToken(request);
```

### Response

```javascript
{
    sessionToken: "sess_1234567890abcdef",
    statusCode: 200
}
```

## Next Steps

- [createSdkSessionToken](./create-sdk-session-token.md) - Initialize wallet sessions
- [Payment Service](../payment-service/README.md) - Process payments using session
