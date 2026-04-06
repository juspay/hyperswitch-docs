---
title: authenticate (Java SDK)
description: Execute 3DS challenge or frictionless verification to complete customer authentication with their bank
tags:
  - java
  - 3ds
  - authentication
---

# authenticate Method

## Overview

The `authenticate` method executes 3D Secure authentication.

## Request Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `merchantOrderId` | String | Yes | Order reference |
| `amount` | Money | Yes | Transaction amount |
| `paymentMethod` | PaymentMethod | Yes | Card details |

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `status` | String | AUTHENTICATED, FAILED |
| `authenticationData` | Map | 3DS results |

## Example

```java
Map<String, Object> request = new HashMap<>();
request.put("merchantOrderId", "order_001");
request.put("amount", Map.of("minorAmount", 10000, "currency", "USD"));

Map<String, Object> response = authClient.authenticate(request);
```
