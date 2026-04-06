---
title: createSdkSessionToken (Java SDK)
description: Initialize wallet payment sessions for Apple Pay and Google Pay to enable secure tokenized payments
tags:
  - java
  - wallet
  - session
---

# createSdkSessionToken Method

## Overview

The `createSdkSessionToken` method initializes wallet payment sessions.

## Request Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `merchantSdkSessionId` | String | Yes | SDK session reference |
| `amount` | Money | Yes | Payment amount |
| `paymentMethodType` | String | No | APPLE_PAY, GOOGLE_PAY |

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `sessionToken` | Map | Wallet session data |

## Example

```java
Map<String, Object> request = new HashMap<>();
request.put("merchantSdkSessionId", "sdk_session_001");
request.put("amount", Map.of("minorAmount", 10000, "currency", "USD"));
request.put("paymentMethodType", "APPLE_PAY");

Map<String, Object> response = authClient.createSdkSessionToken(request);
```
