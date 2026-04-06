---
title: Payment Method Service (PHP SDK)
description: Tokenize and securely store payment methods to enable one-click checkout and recurring billing
tags:
  - php
  - payment-methods
  - tokenization
---

# Payment Method Service

## Overview

The Payment Method Service enables you to securely store payment methods at payment processors using the PHP SDK. Tokenization replaces sensitive card data with secure tokens, enabling one-click payments and recurring billing without PCI compliance exposure.

**Business Use Cases:**
- **One-click checkout** - Returning customers pay without re-entering card details
- **Subscription billing** - Stored payment methods for recurring charges
- **Vault migration** - Move existing tokens between processors
- **PCI compliance** - Reduce compliance scope by avoiding raw card storage

## Operations

| Operation | Description | Use When |
|-----------|-------------|----------|
| [`tokenize`](./tokenize.md) | Store payment method for future use. Replaces raw card details with secure token. | Customer wants to save card for future purchases |

## SDK Setup

```php
use HyperswitchPrism\PaymentMethodClient;

$paymentMethodClient = new PaymentMethodClient([
    'connector' => 'stripe',
    'apiKey' => 'YOUR_API_KEY',
    'environment' => 'SANDBOX'
]);
```

## Next Steps

- [Payment Service](../payment-service/README.md) - Use tokenized payment methods for charges
- [Customer Service](../customer-service/README.md) - Associate payment methods with customers
- [Recurring Payment Service](../recurring-payment-service/README.md) - Set up recurring billing with stored methods
