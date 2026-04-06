---
title: refund (Java SDK)
description: Issue refunds to customer payment methods for returns, cancellations, or service adjustments
tags:
  - java
  - payments
  - refunds
---

# refund Method

## Overview

The `refund` method returns funds to a customer's payment method.

## Request Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `merchantRefundId` | String | Yes | Your refund reference |
| `connectorTransactionId` | String | Yes | Transaction ID |
| `refundAmount` | Money | No | Amount to refund |
| `reason` | String | No | Refund reason |

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `status` | RefundStatus | PENDING, SUCCEEDED |
| `connectorRefundId` | String | Refund ID |

## Example

```java
Map<String, Object> request = new HashMap<>();
request.put("merchantRefundId", "refund_001");
request.put("connectorTransactionId", "pi_xxx");
request.put("refundAmount", Map.of("minorAmount", 1000, "currency", "USD"));

Map<String, Object> response = paymentClient.refund(request);
```
