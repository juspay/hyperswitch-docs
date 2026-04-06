---
title: void (Java SDK)
description: Cancel authorized payments before capture to release held funds back to customer payment methods
tags:
  - java
  - payments
  - void
---

# void Method

## Overview

The `void` method cancels an authorized payment before capture.

## Request Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `merchantTransactionId` | String | Yes | Your reference |
| `connectorTransactionId` | String | Yes | Connector's ID |
| `voidReason` | String | No | Reason for voiding |

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `status` | PaymentStatus | VOIDED |

## Example

```java
Map<String, Object> request = new HashMap<>();
request.put("merchantTransactionId", "txn_001");
request.put("connectorTransactionId", "pi_xxx");

Map<String, Object> response = paymentClient.void(request);
```

## Next Steps

- [authorize](./authorize.md) - Create authorization
