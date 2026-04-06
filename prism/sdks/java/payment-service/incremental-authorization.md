---
title: incrementalAuthorization (Java SDK)
description: Increase authorized amounts to add charges for hotel incidentals, tips, or add-on services
tags:
  - java
  - payments
  - authorization
---

# incrementalAuthorization Method

## Overview

The `incrementalAuthorization` method increases the authorized amount.

## Request Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `merchantAuthorizationId` | String | Yes | Incremental auth ID |
| `connectorTransactionId` | String | Yes | Original auth ID |
| `amount` | Money | Yes | New total amount |
| `reason` | String | No | Reason |

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `status` | AuthorizationStatus | AUTHORIZED |

## Example

```java
Map<String, Object> request = new HashMap<>();
request.put("merchantAuthorizationId", "incr_auth_001");
request.put("connectorTransactionId", "pi_xxx");
request.put("amount", Map.of("minorAmount", 1500, "currency", "USD"));
request.put("reason", "Room service");

Map<String, Object> response = paymentClient.incrementalAuthorization(request);
```
