---
title: setupRecurring (Java SDK)
description: Set up recurring payment mandates to enable subscription billing and automated future charges
tags:
  - java
  - recurring
  - subscriptions
---

# setupRecurring Method

## Overview

The `setupRecurring` method establishes a payment mandate for future charges.

## Request Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `merchantRecurringPaymentId` | String | Yes | Recurring setup ID |
| `amount` | Money | Yes | Initial amount |
| `paymentMethod` | PaymentMethod | Yes | Card details |
| `address` | PaymentAddress | Yes | Billing address |
| `authType` | String | Yes | THREE_DS or NO_THREE_DS |

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `status` | PaymentStatus | ACTIVE, FAILED |
| `mandateReference` | Map | Mandate details |

## Example

```java
Map<String, Object> request = new HashMap<>();
request.put("merchantRecurringPaymentId", "recurring_001");
request.put("amount", Map.of("minorAmount", 2900, "currency", "USD"));
request.put("authType", "NO_THREE_DS");

Map<String, Object> response = paymentClient.setupRecurring(request);
```
