---
title: preAuthenticate (Java SDK)
description: Initiate 3D Secure authentication flows to reduce fraud liability and comply with SCA requirements
tags:
  - java
  - 3ds
  - authentication
---

# preAuthenticate Method

## Overview

The `preAuthenticate` method initiates the 3D Secure authentication flow.

## Request Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `merchantOrderId` | String | Yes | Order reference |
| `amount` | Money | Yes | Transaction amount |
| `paymentMethod` | PaymentMethod | Yes | Card details |
| `returnUrl` | String | Yes | Redirect URL |

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `status` | String | FRICTIONLESS, AUTHENTICATION_REQUIRED |
| `authenticationData` | Map | 3DS data |

## Example

```java
Map<String, Object> request = new HashMap<>();
request.put("merchantOrderId", "order_001");
request.put("amount", Map.of("minorAmount", 10000, "currency", "USD"));
request.put("returnUrl", "https://your-app.com/3ds/return");

Map<String, Object> response = authClient.preAuthenticate(request);
```
