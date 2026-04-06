---
title: accept (PHP SDK)
description: Concede chargeback disputes to accept liability when evidence is insufficient or defense costs exceed dispute amount
tags:
  - php
  - disputes
  - chargebacks
---

# accept Method

## Overview

The `accept` method concedes a dispute and accepts the loss.

## Request Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `disputeId` | string | Yes | The dispute ID |
| `reason` | string | No | Internal reason |

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `disputeId` | string | The dispute ID |
| `status` | DisputeStatus | LOST |
| `amountDebited` | Money | Amount charged back |

## Example

```php
$request = [
    'disputeId' => 'dp_xxx',
    'reason' => 'Insufficient evidence'
];
$response = $disputeClient->accept($request);
```
