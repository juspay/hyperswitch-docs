# Payment Method Service Overview

## Overview

The Payment Method Service enables you to securely store payment methods at payment processors using the Python SDK. Tokenization replaces sensitive card data with secure tokens, enabling one-click payments and recurring billing without PCI compliance exposure.

**Business Use Cases:**

* **One-click checkout** - Returning customers pay without re-entering card details
* **Subscription billing** - Stored payment methods for recurring charges
* **Vault migration** - Move existing tokens between processors
* **PCI compliance** - Reduce compliance scope by avoiding raw card storage

## Operations

| Operation                   | Description                                                                       | Use When                                         |
| --------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------ |
| [`tokenize`](tokenize-2.md) | Store payment method for future use. Replaces raw card details with secure token. | Customer wants to save card for future purchases |

## SDK Setup

```python
from hyperswitch_prism import PaymentMethodClient

payment_method_client = PaymentMethodClient(
    connector='stripe',
    api_key='YOUR_API_KEY',
    environment='SANDBOX'
)
```

## Next Steps

* [Payment Service](payment-service-2.md) - Use tokenized payment methods for charges
* [Customer Service](customer-service-2.md) - Associate payment methods with customers
* [Recurring Payment Service](recurring-payment-service-2.md) - Set up recurring billing with stored methods
