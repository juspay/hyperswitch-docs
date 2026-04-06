---
title: createSessionToken (PHP SDK)
description: Create session tokens for payment processing to maintain state across multi-step payment flows
tags:
  - php
  - session
  - tokens
---

# createSessionToken Method

## Overview

The `createSessionToken` method creates a session token for payment processing.

## Request Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `merchantSessionId` | string | Yes | Your session reference |
| `amount` | Money | Yes | Payment amount |

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `sessionToken` | string | Token for operations |

## Example

```php
$request = [
    'merchantSessionId' => 'session_001',
    'amount' => ['minorAmount' => 10000, 'currency' => 'USD']
];
$response = $authClient->createSessionToken($request);
```
