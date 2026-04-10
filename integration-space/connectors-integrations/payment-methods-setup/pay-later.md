---
description: Configure buy now pay later options including Klarna Affirm and Afterpay for customer flexibility
icon: calendar-day
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/kf7BGdsPkCw9nalhAIlE/other-features/payment-orchestration/quickstart/payment-methods-setup/pay-later
---

# Pay Later

### Klarna, Affirm, Afterpay/Clearpay - Redirection flow

Juspay Hyperswitch supports multiple buy now pay later options:

* Klarna is a global buy now pay later payment method available in 23+ countries and supports 15+ currencies.
* Affirm is a buy now pay later payment method available to US customers and supports USD.
* Afterpay/Clearpay is a buy now pay later payment method available as Afterpay to customers in US, Canada, Australia, New Zealand while available as Clearpay to customers in the United Kingdom, Spain, France and Italy. It currently supports USD, CAD, AUD, NZD, EUR and GBP.

### How to configure pay later options (Redirection flow) on Juspay Hyperswitch?

1. Make sure that the pay later options are enabled on your connector's dashboard
2. Enable pay later options on Hyperswitch dashboard under "payment methods" tab while configuring your connector
3. Ensure that you add the additional mandatory parameters when you create a payment (using node SDK or /payments API) from your server-side.

```js
"email": "guest@example.com",
"shipping": {
        "address": {
            "line1": "1467",
            "line2": "Harrison Street",
            "line3": "Harrison Street",
            "city": "San Francisco",
            "state": "California",
            "zip": "94122",
            "country": "US",
            "first_name": "John",
            "last_name": "Doe"
        },
            "phone": {
            "number": "123456789",
            "country_code": "+1"
        }
    },
"billing": {
      "address": {
          "line1": "1467",
          "line2": "Harrison Street",
          "line3": "Harrison Street",
          "city": "San Francisco",
          "state": "California",
          "zip": "94122",
          "country": "US",
          "first_name": "John",
          "last_name": "Doe"
      },
          "phone": {
          "number": "123456789",
          "country_code": "+1"
      }
  }
```

### Klarna - In app flow

![Klarna Logo](https://hyperswitch.io/icons/homePageIcons/logos/klarnaLogo.svg)

Klarna In app flow in Juspay Hyperswitch is available if you configure Klarna as a payment processor. It provides a superior checkout flow for the customers compared to redirection flow.

To configure Klarna SDK flow, follow these steps. As a prerequisite, you would need to have a merchant account with Klarna. For Klarna SDK, you need to add a mandatory metaData object while creating a payment (/payments) from your server-side. The metaData object will look something like below.

```js
"metadata": {
      "order_details": {
        "product_name": "Apple iPhone 15",
        "quantity": 1
      }
    }
```
