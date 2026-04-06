---
title: authenticate (PHP SDK)
description: Execute 3DS challenge or frictionless verification to complete customer authentication with their bank
tags:
  - php
  - 3ds
  - authentication
---

# authenticate Method

## Overview

The `authenticate` method executes the 3D Secure authentication step.

## Request Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `merchantOrderId` | string | Yes | Your order reference |
| `amount` | Money | Yes | Transaction amount |
| `paymentMethod` | PaymentMethod | Yes | Card details |

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `status` | string | AUTHENTICATED, FAILED |
| `authenticationData` | array | 3DS results |

## Example

```php
$request = [
    'merchantOrderId' => 'order_001',
    'amount' => ['minorAmount' => 10000, 'currency' => 'USD'],
    'paymentMethod' => ['card' => [...]]
];
$response = $authClient->authenticate($request);
```
