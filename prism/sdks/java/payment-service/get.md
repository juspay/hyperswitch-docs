---
title: get (Java SDK)
description: Retrieve payment status from processors to synchronize payment states and enable accurate order tracking
tags:
  - java
  - payments
  - status
---

# get Method

## Overview

The `get` method retrieves payment status from the processor.

## Request Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `merchantTransactionId` | String | Yes | Your reference |
| `connectorTransactionId` | String | Yes | Connector's ID |

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `status` | PaymentStatus | Current status |
| `amount` | Money | Payment amount |

## Example

```java
Map<String, Object> request = new HashMap<>();
request.put("merchantTransactionId", "txn_001");
request.put("connectorTransactionId", "pi_xxx");

Map<String, Object> response = paymentClient.get(request);
```
