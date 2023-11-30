# Pay Later

## Pay Later

Hyperswitch supports the following global and local buy now pay later payment methods.

### Klarna, Affirm, Afterpay/Clearpay - Redirection flow

* Klarna is a global buy now pay later payment method that is available in more than 19 countries and supports 10 currencies.
* Affirm is a buy now pay later payment method available to US customers and supports USD.
* Afterpay/Clearpay is a buy now pay later payment method available as Afterpay to customers in US, Canada, Australia, New Zealand while available as Clearpay to customers in the United Kingdom, Spain, France and Italy. It currently supports USD, CAD, AUD, NZD, EUR and GBP.

**How to configure Paylater options (Redirection flow) on Hyperswitch?**

1. Make sure that the paylater options are enabled on your connector's dashboard
2. Enable paylater options on Hyperswitch dashboard under "payment methods" tab while configuring your connector
3. Ensure that you add the additional mandatory parameters when you create a payment (using node SDK or /payments API) from your server-side.

```js
"email": "guest@example.com",
"shipping": {
        "address": {
            "line1": "1467",
            "line2": "Harrison Street",
            "line3": "Harrison Street",
            "city": "San Fransico",
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
          "city": "San Fransico",
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

Klarna In app flow in Hyperswitch is available if you configure Klarna as a payment processor. It provides a superior checkout flow for the customers compared to redirection flow.

To configure Klarna SDK flow, follow these steps. As a prerequisite, you would need to have a merchant account with Klarna. For Klarna SDK, need to add mandatory metaData object while creating a payment (/payments) from your server-side. The metaData object will look something like below.

```js
"metadata": {
      "order_details": {
        "product_name": "Apple iphone 15",
        "quantity": 1
      }
    }
```
