# ⏭️ External Authentication for 3DS

Simplify 3DS authentication, stay compliant, offer latest authentication methods to the customers, improve customer experience with Native Challenge and improve conversion rates - All with the Hyperswitch 3DS authentication module

## Why do we need external authentication?

3DS authentication for cards is a crucial step before authorization. Designed to enhance security, reduce fraud, and improve customer experience, the 3DS authentication is mandatory in many markets. Up until now, merchants relied on the payment processors to complete the authentication and authorization. But it comes with its own challenges.

* **Poor data availability** - In the processor authentication flow, the merchant has no visibility on authentication metrics independently. They cannot distinguish failures that happen in the authentication leg from those that happen in the authorization leg. Therefore, it becomes difficult to take corrective actions.
* **Poor customer experience** - No matter the flow, challenge or frictionless, the customer has to be redirected at least once when the authentication is done via the payment processor. Redirections in the payment journey lead to customer drop offs.&#x20;
* **Compliance management** - With continuously evolving security standards and payment regulations, merchants have to stay on top of the 3DS compliance guide to make sure that they fulfill all the regulatory requirements.&#x20;
* **New innovative products in the authentication space** - To cope up with the regulations and at the same time enhance security and customer experience, there are multiple innovative products out there in the authentication space. To focus on these innovations, instead of the core business, is a real distraction for the merchants.

## How to get started?

We will be using HyperSwitch's hosted dashboard and Postman API collection for configuring connectors and processing payouts. You can find API reference [here](https://api-reference.hyperswitch.io/api-reference/payments/payments--external-3ds-authentication).

Backend API endpoint - https://sandbox.hyperswitch.io

Dashboard - [https://app.hyperswitch.io](https://app.hyperswitch.io)

### Pre-requisites

* Setup 3DS Authenticator&#x20;

<figure><img src="../../../.gitbook/assets/Screenshot 2024-05-09 at 3.27.58 PM.png" alt=""><figcaption><p>Add new 3DS authenticator</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/Screenshot 2024-05-09 at 3.28.59 PM.png" alt=""><figcaption><p>Add credentials for 3DS authenticator</p></figcaption></figure>

* Setup payment processor

<figure><img src="../../../.gitbook/assets/Screenshot 2024-05-09 at 3.31.16 PM.png" alt=""><figcaption><p>Add new payment processors</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/Screenshot 2024-05-09 at 3.33.02 PM.png" alt=""><figcaption><p>Add credentials for payment processor</p></figcaption></figure>

* Go to Developers -> Payment Settings -> Choose default setting and add Authentication Connectors

<figure><img src="../../../.gitbook/assets/Screenshot 2024-05-09 at 3.36.36 PM.png" alt=""><figcaption><p>Add required urls and set the authentication connector</p></figcaption></figure>

* Create/Collect your API key and Publishable key

You are done with the setup!

### How to do external authentication?

### 1. Create a payment from your server with request\_external\_three\_ds\_authentication as true

Do a create payment call to initiate the transaction. The status of the response should be 'requres\_customer\_action" and should contain the "next\_action" object.

```
curl --location 'https://sandbox.hyperswitch.io/payments' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'api-key: {{api_key}}' \
--data-raw '{
    "amount": 2540,
    "currency": "USD",
    "confirm": true,
    "amount_to_capture": 2540,
    "capture_method": "automatic",
    "capture_on": "2022-09-10T10:11:12Z",
    "customer_id": "StripeCustomer",
    "email": "abcdef123@gmail.com",
    "name": "John Doe",
    "phone": "999999999",
    "request_external_three_ds_authentication": true,
    "phone_country_code": "+65",
    "description": "Its my first payment request",
    "authentication_type": "three_ds",
    "return_url": "https://google.com",
    "setup_future_usage": "on_session",
    "browser_info": {
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
        "accept_header": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "language": "nl-NL",
        "color_depth": 24,
        "screen_height": 723,
        "screen_width": 1536,
        "time_zone": 0,
        "java_enabled": true,
        "java_script_enabled": true,
        "ip_address": "127.0.0.1"
    },
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
        }
    },
    "routing": {
        "type": "single",
        "data": "nmi"
    },
    "statement_descriptor_name": "joseph",
    "statement_descriptor_suffix": "JS",
    "metadata": {
        "udf1": "value1",
        "new_customer": "true",
        "login_date": "2019-09-10T10:11:12Z"
    },
    "payment_method": "card",
    "payment_method_type": "credit",
    "payment_method_data": {
        "card": {
            "card_number": "4000000000002370",
            "card_exp_month": "08",
            "card_exp_year": "25",
            "card_holder_name": "joseph Doe",
            "card_cvc": "999"
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
        }
    }
}'
```

### 2. Do authentication

Initiate the authentication with the client\_secret generated

```
curl --location 'https://sandbox.hyperswitch.io/payments/pay_xXr8btC2depRWfVYKmNt/3ds/authentication' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'api-key: {{api_key}}' \
--data '{
    "client_secret": "{{client_secret}}",
    "device_channel": "BRW",
    "threeds_method_comp_ind": "Y"
}'
```

After the challenge is completed, the status should go to 'succeeded' status

{% hint style="info" %}
Visit [this](../../../hyperswitch-cloud/connectors/available-connectors/zen-1/authenticating-payments-via-netcetera-through-hyperswitch-sdk.md) page to know more about enabling this feature steps in SDK
{% endhint %}

{% hint style="success" %}
Being a payments product, Hyperswitch is always up to date with the latest regulations globally. On that front, the merchants need not worry about compliance. For merchants who want to integrate the latest authentication products to offer a frictionless payment flow to their customers, but also enjoy the liability shift, Hyperswitch has got you covered. Products like Digital Authentication Framework (DAF), Delegated Authentication (DA), Secure Payment Confirmation (SPC), Click to Pay (CTP), etc. are in our roadmap. Check out the product on sandbox or get in touch with us for more information.
{% endhint %}

