---
description: Best way to offer postpaid payment services
---

# 0 Zero Auth flow on Hyperswitch

{% hint style="info" %}
In this section, we will understand zero-auth flow, it's usage, and webhook consumption
{% endhint %}

The zero-auth flow in Hyperswitch allows the merchant to offer postpaid payment services. On customer registration, the merchant can initiate a zero-auth flow transaction with Hyperswitch to authenticate the customer payment method (card, bank account etc.) and receive authorization from the customer to use the payment method for recurring payments. A mandate would be created and issued to the merchant. And in the future they can charge against this mandate.

The following API cURLs demonstrate the usage of the zero-auth flow. The example below uses the credit card payment method. But this can be extended to bank debits and other payment methods as well.

## How to use the zero-auth flow

1. Creating a 0 amount payment along with the mandate data to set up a mandate with customer’s payment details (Customer initiated transaction)\


```shell
curl --location 'http://sandbox.hyperswitch.io/payments' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'api-key: <enter your Hyperswitch API key here>' \
--data-raw '{
"amount": 0,
"currency": "USD",
"confirm": false,
"customer_id": "zero_auth_test_customer",
"email": "m.arjunkarthik@gmail.com",
"name": "John Doe",
"phone": "999999999",
"phone_country_code": "+1",
"description": "Its my first payment request",
"mandate_data": {
    "mandate_type": {
    "multi_use": {
    "amount": 100000,
    "currency": "USD"
                    }
            }
    },
"setup_future_usage": "off_session"
}'

```

2. Confirm the payment after collecting payment information from the user \[You can skip this step if you are using the Hyperswitch Unified Checkout]

```bash
curl --location 'http://http://sandbox.hyperswitch.io/payments/{{payment_id}}/confirm' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'api-key: <enter your Hyperswitch API key here>' \
--data-raw '{
    "confirm": true,
    "payment_method": "card",
    "payment_method_type": "credit",
    "payment_method_data": {
        "card": {
            "card_number": "4111111111111111",
            "card_exp_month": "01",
            "card_exp_year": "2035",
            "card_holder_name": "joseph Doe",
            "card_cvc": "100"
        }
    },
    "customer_id": "GC222",
    "setup_future_usage": "off_session",
    "payment_type": "setup_mandate",
    "mandate_data": {
        "customer_acceptance": {
            "acceptance_type": "online",
            "accepted_at": "1963-05-03T04:07:52.723Z",
            "online": {
                "ip_address": "127.0.0.1",
                "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
            }
        }
    },
    "browser_info": {
        "ip_address": "172.0.0.1"
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
            "first_name": "joseph",
            "last_name": "Doe"
        },
        "phone": {
            "number": "8056594427",
            "country_code": "+91"
        }
    }
}'
```

3.  Charging a customer against the mandate issued in the future (Merchant initiated Transaction)

    \


    You can use the List Mandates API to retrieve the list of mandates issued against a customer and their status.

```bash
curl --location 'https://sandbox.hyperswitch.io/customers/{{customer_id}}/mandates' \
--header 'Accept: application/json' \
--header 'api-key: <enter your Hyperswitch API key here>'
```

You’ll get the list of mandates in the response:

```bash
[
    {
        "mandate_id": "man_oBkxfbl29hAW3yJ5P4FX",
        "status": "active",
        "payment_method_id": "jkwS4P7oYC8Q1t82",
        "payment_method": "card",
        "card": {
            "last4_digits": "4242",
            "card_exp_month": "10",
            "card_exp_year": "25",
            "card_holder_name": "joseph Doe",
            "card_token": null,
            "scheme": null,
            "issuer_country": null,
            "card_fingerprint": null
        },
        "customer_acceptance": {
            "acceptance_type": "online",
            "accepted_at": "1963-05-03T04:07:52.723Z",
            "online": {
                "ip_address": "127.0.0.1",
                "user_agent": "amet irure esse"
            }
        }
    }
]


```

For any of the active mandates you can use the below request to make the recurring payment.

```bash
curl --location 'http://sandbox.hyperswitch.io/payments' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'api-key: use your Hyperswitch API key' \
--data-raw '{
    "amount": 1231,
    "currency": "USD",
    "confirm": true,
    "customer_id": "GC222",
    "email": "m.arjunkarthik@gmail.com",
    "name": "John Doe",
    "billing": {
        "address": {
            "line1": "1467",
            "line2": "Harrison Street",
            "line3": "Harrison Street",
            "city": "San Fransico",
            "state": "California",
            "zip": "94122",
            "country": "US",
            "first_name": "joseph",
            "last_name": "Doe"
        },
        "phone": {
            "number": "8056594427",
            "country_code": "+91"
        }
    },
    "description": "Its my first payment request",
    "mandate_id": "man_wvgqN9hdMawRaRzRpsXj",
    "off_session": true
}'
```

The same API request can be expanded to other payment methods as well by simply updating the parameters in the /payments/confirm request.&#x20;

The below example displays the schema for making a zero auth request for a bank direct debit payment method.

```bash
 "payment_method": "bank_debit",
    "payment_method_type": "ach",
    "payment_method_data": {
        "bank_debit": {
            "ach_bank_debit": {
                "account_number": "2715500356",
                "routing_number": "026073150",
                "bank_type": "checking",
                "billing_details": {
                    "address": {
                        "line1": "1467",
                        "line2": "Harrison Street",
                        "city": "San Fransico",
                        "state": "California",
                        "zip": "94122",
                        "country": "US",
                        "first_name": "Arjun",
                        "last_name": "Karthik"
                    },
                    "name": "Arjun AK AK AK",
                    "email": "arjun.karthik@juspay.in"
                },
                "bank_account_holder_name": "Arjun Karthik"
            }
        }
    }

```

## Webhook Consumption

To receive webhooks from Hyperswitch, configure your Server Webhook URL in the Hyperswitch dashboard [(Developer>Webhooks) ](https://app.hyperswitch.io/developers)

<figure><img src="https://lh7-us.googleusercontent.com/qBYvcG9TeKek6H4Q7mC_cJkHtzT-E94eQc_iVUVC1Uytls__O__mWHC0CZXf1m9pheHa4KUVmp95b8cbFkM3ccDa7J0vyuZ6IkiFYsnwT1xucRQsQ6z6BZxzUIPcWnT8JBYbLB4bNObJaZPiBu5akhk" alt=""><figcaption></figcaption></figure>

### Mandate Webhooks

Events to be handled - MandateActive and MandateRevoked

### Payment Webhooks

Events to be handled - PaymentSucceeded, PaymentFailed

Refer [Hyperswitch API docs](https://api-reference.hyperswitch.io/docs/hyperswitch-api-reference/?\_gl=1\*1omp6b9\*\_ga\*MTAxMjU4MDcyMS4xNjgzODI5OTAy\*\_ga\_1X38KQVJ1S\*MTY5NjU5NDk0MC43NC4xLjE2OTY1OTQ5NDguNTIuMC4w) for other webhook events (refunds, disputes etc.)&#x20;
