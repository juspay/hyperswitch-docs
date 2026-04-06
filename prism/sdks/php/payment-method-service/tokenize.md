---
title: tokenize (PHP SDK)
description: Store payment methods securely to replace sensitive card data with tokens for safe storage
tags:
  - php
  - tokenization
  - payment-methods
---

# tokenize Method

## Overview

The `tokenize` method stores a payment method securely at the processor.

## Request Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `paymentMethod` | PaymentMethod | Yes | Card details |
| `customerId` | string | No | Customer association |

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `paymentMethodId` | string | Token ID |
| `status` | string | ACTIVE |

## Example

```php
$request = [
    'paymentMethod' => [
        'card' => [
            'cardNumber' => ['value' => '4242424242424242'],
            'cardExpMonth' => ['value' => '12'],
            'cardExpYear' => ['value' => '2027']
        ]
    ]
];
$response = $paymentMethodClient->tokenize($request);
```
