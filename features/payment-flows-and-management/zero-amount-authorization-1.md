---
description: Best way to validate customer payment data and charge the customer later
---

# 0️ Zero Amount Authorization - Payment Method flow

{% hint style="info" %}
In this section, we will understand zero-auth flow, it's usage, and webhook consumption
{% endhint %}

The zero amount authorization flow in Hyperswitch allows the merchant to validate customer payment data and charge the customer later. On customer registration, the merchant can initiate a zero-auth flow transaction with Hyperswitch to authenticate the customer payment method (card, bank account etc.) and receive authorization from the customer to use the payment method to charge them at a later point (one-time or multi-use). A payment\_method\_id would be created and issued to the merchant. And in the future they can charge against this payment\_method\_id.

The following API cURLs demonstrate the usage of the zero-auth flow. The example below uses the credit card payment method. But this can be extended to bank debits and other payment methods as well.

## How to use the zero amount authorization flow?

1. Creating a 0 amount payment along with `setup_future_usage= off_session` to set up a mandate to store and charge the customer's payment method later **( Called as 'CIT' : Customer initiated transaction)**

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
"setup_future_usage": "off_session"
}'

```

2. Confirm the payment after collecting payment information from the user **\[You can skip this step if you are using the Hyperswitch Unified Checkout]**

<pre class="language-bash"><code class="lang-bash"><strong>curl --location 'http://http://sandbox.hyperswitch.io/payments/{{payment_id}}/confirm' \
</strong>--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
<strong>--header 'api-key: &#x3C;enter your Hyperswitch API key here>' \
</strong>--data-raw '{
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
    "customer_acceptance": {
        "acceptance_type": "online",
        "accepted_at": "1963-05-03T04:07:52.723Z",
        "online": {
            "ip_address": "127.0.0.1",
            "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
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
</code></pre>

3. Retrieve the `payment_method_id` that was created against the above payment by retrieving the payment. You will get the payment\_method\_id in the response

```bash
curl --location 'https://sandbox.hyperswitch.io/payments/<pass the payment_id>' \
--header 'Accept: application/json' \
--header 'api-key: <enter your Hyperswitch API key here>' \
```

4. Charge the customer later by passing the payment\_method\_id  **(Called as 'MIT': Merchant initiated Transaction)**\


Pass the above `payment_method_id` under the `recurring_details` object along with `off_session=true` in the payments request and confirm the payment

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
    "email": "abcd@gmail.com",
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
    "off_session": true,
    "recurring_details": {
        "type": "payment_method_id",
        "data": "pm_lmTnIO5EdCiiMgRPrV9x"
    },
}'
```
