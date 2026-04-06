---
title: reverse (Java SDK)
description: Reverse captured payments before settlement to recover funds from same-day cancellations or errors
tags:
  - java
  - payments
  - reverse
---

# reverse Method

## Overview

The `reverse` method cancels a captured payment before settlement.

## Request Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `merchantReverseId` | String | Yes | Reverse operation ID |
| `connectorTransactionId` | String | Yes | Transaction ID |
| `cancellationReason` | String | No | Reason |

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `status` | PaymentStatus | VOIDED, REVERSED |

## Example

```java
Map<String, Object> request = new HashMap<>();
request.put("merchantReverseId", "reverse_001");
request.put("connectorTransactionId", "pi_xxx");
request.put("cancellationReason", "Duplicate charge");

Map<String, Object> response = paymentClient.reverse(request);
```
