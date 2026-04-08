# Customer Service Overview

## Overview

The Customer Service enables you to create and manage customer profiles at payment processors using the Python SDK. Storing customer details with connectors streamlines future transactions and improves authorization rates.

**Business Use Cases:**

* **E-commerce accounts** - Save customer profiles for faster checkout on return visits
* **SaaS platforms** - Associate customers with subscription payments and billing histories
* **Recurring billing** - Link customers to stored payment methods for automated billing
* **Fraud prevention** - Consistent customer identity improves risk scoring accuracy

## Operations

| Operation               | Description                                                                                                    | Use When                                                                |
| ----------------------- | -------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| [`create`](create-2.md) | Create customer record in the payment processor system. Stores customer details for future payment operations. | First-time customer checkout, account registration, subscription signup |

## SDK Setup

```python
from hyperswitch_prism import CustomerClient

customer_client = CustomerClient(
    connector='stripe',
    api_key='YOUR_API_KEY',
    environment='SANDBOX'
)
```

## Next Steps

* [Payment Service](payment-service-2.md) - Process payments linked to customers
* [Payment Method Service](payment-method-service-2.md) - Store and manage customer payment methods
* [Recurring Payment Service](recurring-payment-service-2.md) - Set up recurring billing for customers
