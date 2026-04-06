---
title: preAuthenticate (PHP SDK)
description: Initiate 3D Secure authentication flows to reduce fraud liability and comply with SCA requirements
tags:
  - php
  - 3ds
  - authentication
---

# preAuthenticate Method

## Overview

The `preAuthenticate` method initiates the 3D Secure authentication flow.

## Request Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `merchantOrderId` | string | Yes | Your order reference |
| `amount` | Money | Yes | Transaction amount |
| `paymentMethod` | PaymentMethod | Yes | Card details |
| `returnUrl` | string | Yes | URL to redirect |

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `status` | string | FRICTIONLESS, AUTHENTICATION_REQUIRED |
| `authenticationData` | array | 3DS data |

## Example

```php
$request = [
    'merchantOrderId' => 'order_001',
    'amount' => ['minorAmount' => 10000, 'currency' => 'USD'],
    'paymentMethod' => ['card' => [...]],
    'returnUrl' => 'https://your-app.com/3ds/return'
];
$response = $authClient->preAuthenticate($request);
```
