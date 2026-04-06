---
title: get (Java SDK)
description: Retrieve dispute status to track chargeback progress and review evidence submission deadlines
tags:
  - java
  - disputes
  - status
---

# get Method

## Overview

The `get` method retrieves dispute status.

## Request Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `disputeId` | String | Yes | Dispute ID |

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `status` | DisputeStatus | NEEDS_RESPONSE, WON, LOST |

## Example

```java
Map<String, Object> request = new HashMap<>();
request.put("disputeId", "dp_xxx");

Map<String, Object> response = disputeClient.get(request);
```
