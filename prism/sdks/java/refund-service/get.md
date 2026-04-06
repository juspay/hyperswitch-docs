---
title: get (Java SDK)
description: Retrieve refund status from payment processors to track refund progress and provide customer updates
tags:
  - java
  - refunds
  - get-refund
---

# get Method

## Overview

The `get` method retrieves refund status from the processor.

## Request Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `connectorRefundId` | String | Yes | Refund ID |

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `status` | RefundStatus | PENDING, SUCCEEDED |

## Example

```java
Map<String, Object> request = new HashMap<>();
request.put("connectorRefundId", "re_xxx");

Map<String, Object> response = paymentClient.getRefund(request);
```
