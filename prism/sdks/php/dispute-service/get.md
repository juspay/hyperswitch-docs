---
title: get (PHP SDK)
description: Retrieve dispute status to track chargeback progress and review evidence submission deadlines
tags:
  - php
  - disputes
  - status
---

# get Method

## Overview

The `get` method retrieves the current status of a dispute.

## Request Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `disputeId` | string | Yes | The connector's dispute ID |

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `disputeId` | string | Connector's dispute ID |
| `status` | DisputeStatus | NEEDS_RESPONSE, UNDER_REVIEW, WON, LOST |
| `amount` | Money | Disputed amount |
| `evidenceDueBy` | string | Deadline for evidence |
| `statusCode` | int | HTTP status code |

## Example

```php
$request = ['disputeId' => 'dp_xxx'];
$response = $disputeClient->get($request);
```
