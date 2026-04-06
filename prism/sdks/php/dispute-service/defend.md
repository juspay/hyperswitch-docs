---
title: defend (PHP SDK)
description: Submit formal defense against chargebacks to contest fraudulent transaction claims and recover revenue
tags:
  - php
  - disputes
  - chargebacks
---

# defend Method

## Overview

The `defend` method submits your formal argument against a chargeback claim.

## Request Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `disputeId` | string | Yes | The dispute ID |
| `reasonCode` | string | Yes | Defense reason code |
| `explanation` | string | Yes | Detailed explanation |

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `disputeId` | string | The dispute ID |
| `defenseSubmitted` | bool | Success status |
| `status` | DisputeStatus | UNDER_REVIEW |

## Example

```php
$request = [
    'disputeId' => 'dp_xxx',
    'reasonCode' => 'product_or_service_provided',
    'explanation' => 'Product was delivered successfully'
];
$response = $disputeClient->defend($request);
```
