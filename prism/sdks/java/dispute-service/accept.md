---
title: accept (Java SDK)
description: Concede chargeback disputes to accept liability when evidence is insufficient or defense costs exceed dispute amount
tags:
  - java
  - disputes
  - chargebacks
---

# accept Method

## Overview

The `accept` method concedes a dispute and accepts the loss.

## Request Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `disputeId` | String | Yes | Dispute ID |
| `reason` | String | No | Internal reason |

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `status` | DisputeStatus | LOST |

## Example

```java
Map<String, Object> request = new HashMap<>();
request.put("disputeId", "dp_xxx");

Map<String, Object> response = disputeClient.accept(request);
```
