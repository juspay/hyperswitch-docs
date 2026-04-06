---
title: postAuthenticate (PHP SDK)
description: Validate 3DS authentication results with the issuing bank to confirm successful verification
tags:
  - php
  - 3ds
  - authentication
---

# postAuthenticate Method

## Overview

The `postAuthenticate` method validates 3D Secure results with the bank.

## Request Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `merchantOrderId` | string | Yes | Your order reference |
| `amount` | Money | Yes | Transaction amount |
| `paymentMethod` | PaymentMethod | Yes | Card details |
| `authenticationData` | array | No | 3DS result data |

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `status` | string | AUTHENTICATED, FAILED |
| `authenticationData` | array | Validated 3DS data |

## Example

```php
$request = [
    'merchantOrderId' => 'order_001',
    'amount' => ['minorAmount' => 10000, 'currency' => 'USD'],
    'authenticationData' => ['eci' => '05', 'cavv' => 'AAAB...']
];
$response = $authClient->postAuthenticate($request);
```
