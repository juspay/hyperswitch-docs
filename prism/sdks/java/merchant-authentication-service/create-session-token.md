---
title: createSessionToken (Java SDK)
description: Create session tokens for payment processing to maintain state across multi-step payment flows
tags:
  - java
  - session
  - tokens
---

# createSessionToken Method

## Overview

The `createSessionToken` method creates a session token for payment processing.

## Request Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `merchantSessionId` | String | Yes | Session reference |
| `amount` | Money | Yes | Payment amount |

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `sessionToken` | String | Token string |

## Example

```java
Map<String, Object> request = new HashMap<>();
request.put("merchantSessionId", "session_001");
request.put("amount", Map.of("minorAmount", 10000, "currency", "USD"));

Map<String, Object> response = authClient.createSessionToken(request);
```
