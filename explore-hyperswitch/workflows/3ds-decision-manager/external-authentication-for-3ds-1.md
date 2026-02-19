---
description: >-
  Use any Standalone 3DS server to run 3D Secure (3DS) authentication and
  authorize the payment with any payment provider (PSP).
hidden: true
icon: up-right-from-square
---

# Copy of Standalone 3D Secure (via Hyperswitch)

Standalone 3DS separates authentication from authorization, giving you the flexibility to work with multiple payment processors or support specialized payment workflows.

Enterprise teams often adopt Standalone 3DS to enhance payment performance by enabling:

* Fine grained API control over 3DS requests and the checkout experience
* Greater visibility into issuer authentication responses
* Transaction level customization based on business priorities such as fraud reduction, conversion optimization, or cost management

When a Standalone 3DS authentication completes successfully, it generates a 3DS cryptogram. This cryptogram can then be submitted as part of the payment authorization. This helps is effective [Smart Retry](../smart-retries/) workflows where the same authentication can be succesfully used with multiple authorization attempts across different payment providers (PSP)

Supported [external 3DS authenticators](https://juspay.io/integrations?categories=3DS+PROVIDER) are - Juspay 3DS server, Netcetera, Cardinal and 3dsecure.io

### Setup External 3DS authentication via Hyperswitch

1. Log into the [Hyperswitch dashboard](https://app.hyperswitch.io/)&#x20;
2. Under Connectors > setup 3DS Authenticator. You can select Juspay 3DS server or any other external 3DS server

<figure><img src="../../../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/Screenshot 2024-05-09 at 3.28.59 PM.png" alt=""><figcaption><p>Add credentials for 3DS authenticator</p></figcaption></figure>

3. Under Connectors > setup the payment provders (PSP) that you wish to use for payment processing&#x20;

<figure><img src="../../../.gitbook/assets/Screenshot 2024-05-09 at 3.31.16 PM.png" alt=""><figcaption><p>Add new payment processors</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/Screenshot 2024-05-09 at 3.33.02 PM.png" alt=""><figcaption><p>Add credentials for payment processor</p></figcaption></figure>

4. Under Developers -> Payment Settings -> Add Authentication Connector and its relevant details

<figure><img src="../../../.gitbook/assets/image (112).png" alt=""><figcaption></figcaption></figure>

### Perform external authentication

Initiate a Payments Create API from your server with [external authentication](https://api-reference.hyperswitch.io/v1/payments/payments--create#body-request-external-three-ds-authentication-one-of-0) as true&#x20;

```javascript
// Set external authentication type in the Payments call
 "request_external_three_ds_authentication": "true"
```

This flows follows the same steps as highlighted in authenticate with 3D secure via PSP&#x20;

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

{% hint style="warning" %}
**Visit** [**this**](../../payment-orchestration/3ds-decision-manager/broken-reference/) **page to complete few additional steps to enable this feature for Mobile SDK.**
{% endhint %}

{% hint style="success" %}
Being a payments product, Hyperswitch is always up to date with the latest regulations globally. On that front, the merchants need not worry about compliance. For merchants who want to integrate the latest authentication products to offer a frictionless payment flow to their customers, but also enjoy the liability shift, Hyperswitch has got you covered. Products like Digital Authentication Framework (DAF), Delegated Authentication (DA), Secure Payment Confirmation (SPC), Click to Pay (CTP), etc. are in our roadmap. Check out the product on sandbox or get in touch with us for more information.
{% endhint %}
