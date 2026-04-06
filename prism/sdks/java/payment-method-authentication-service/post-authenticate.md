---
title: postAuthenticate (Java SDK)
description: Validate 3DS authentication results with the issuing bank to confirm successful verification
tags:
  - java
  - 3ds
  - authentication
---

# postAuthenticate Method

## Overview

The `postAuthenticate` method validates 3D Secure authentication results.

## Request Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `merchantOrderId` | String | Yes | Order reference |
| `amount` | Money | Yes | Transaction amount |
| `paymentMethod` | PaymentMethod | Yes | Card details |
| `authenticationData` | Map | No | 3DS data |

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `status` | String | AUTHENTICATED, FAILED |
| `authenticationData` | Map | Validated 3DS data |

## Example

```java
Map<String, Object> request = new HashMap<>();
request.put("merchantOrderId", "order_001");
request.put("amount", Map.of("minorAmount", 10000, "currency", "USD"));
request.put("authenticationData", Map.of("eci", "05", "cavv", "AAAB..."));

Map<String, Object> response = authClient.postAuthenticate(request);
```
