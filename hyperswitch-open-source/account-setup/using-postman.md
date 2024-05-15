---
description: Create your Hyperswitch account and add a payment provider through postman
---

# 🚀 Using postman

## Account setup using Postman <a href="#user-content-create-a-payment" id="user-content-create-a-payment"></a>

***

## Create a Hyperswitch account <a href="#user-content-create-a-payment" id="user-content-create-a-payment"></a>

In Hyperswitch, payments are processed for a merchant. Hyperswitch is multi-tenant, i.e. a single hyperswitch app server can support multiple merchants.

Use the below cURL command to create a new merchant account. Set the admin API key you configured in the application configuration for `admin_api_key` variable in the cURL request. You can find the configuration file at `config/docker_compose.toml`, search for `api_key` to find the admin API key.  Trigger the request to create a merchant account. You should obtain a response containing the merchant ID and publishable key.

<details>

<summary>Merchant Account - Create</summary>

```json
curl --location 'http://localhost:8080/accounts' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--header 'api-key: <admin-api-key>' \
--data-raw '{
  "merchant_id": "Test_merchant",
  "locker_id": "m0010",
  "merchant_name": "NewAge Retailer",
  "merchant_details": {
    "primary_contact_person": "John Test",
    "primary_email": "JohnTest@test.com",
    "primary_phone": "sunt laborum",
    "secondary_contact_person": "John Test2",
    "secondary_email": "JohnTest2@test.com",
    "secondary_phone": "cillum do dolor id",
    "website": "www.example.com",
    "about_business": "Online Retail with a wide selection of organic products for North America",
    "address": {
      "line1": "1467",
      "line2": "Harrison Street",
      "line3": "Harrison Street",
      "city": "San Fransico",
      "state": "California",
      "zip": "94122",
      "country": "US"
    }
  },
  "return_url": "https://google.com",
  "sub_merchants_enabled": false
}'
```

</details>

## Create an API key <a href="#user-content-create-an-api-key" id="user-content-create-an-api-key"></a>

Use the below cURL command to create an API key. Update URL of the below cURL request with the `merchant_id` obtained in the previous step. Once you trigger the request, you will obtain a response containing the plaintext API key. Store the API key returned in the response securely.

<details>

<summary>API Key - Create</summary>

```json
curl --location 'http://localhost:8080/api_keys/<your_merchant_id>' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'api-key: <admin-api-key>' \
--data '{
  "name": "API Key 1",
  "description": null,
  "expiration": "2023-09-23T01:02:03.000Z"
}'
```

</details>

## Set up a payment processor <a href="#user-content-set-up-a-payment-processor-account" id="user-content-set-up-a-payment-processor-account"></a>

Run the below cURL to set up your preferred payment processor an API key. You'll need the  API keys of payment processor. In case you don't have an account with a payment provider, you can sign-up on any payment processor (say Stripe, Adyen, etc.) and get the necessary credentials.&#x20;

In the below cURL update the following details&#x20;

* Under  `connector_name` and `connector_account_details` fields. `Connector_name`is the name of the Payment provider you want to process payment through&#x20;
* `Connector_account_details`are the respective details of the payment provider in order to complete the authentication succesfully. You can find payment provider-specific details to be included in this [spreadsheet](https://docs.google.com/spreadsheets/d/e/2PACX-1vQWHLza9m5iO4Ol-tEBx22\_Nnq8Mb3ISCWI53nrinIGLK8eHYmHGnvXFXUXEut8AFyGyI9DipsYaBLG/pubhtml?gid=748960791\&single=true).
* Update URL of the below cURL request with the `merchant_id` obtained in the previous step

<details>

<summary>Payment Connector - Create</summary>

```json
curl --location 'http://localhost:8080/account/<your merchant id>/connectors' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'api-key: <admin-api-key>' \
--data '{
  "connector_type": "fiz_operations",
  "connector_name": "stripe",
  "connector_account_details": {
    "auth_type": "HeaderKey",
    "api_key": "<stripe-api-key>"
  },
  "test_mode": false,
  "disabled": false,
  "payment_methods_enabled": [
    {
      "payment_method": "card",
      "payment_method_types": [
        {
          "payment_method_type": "credit",
          "card_networks": [
            "Visa",
            "Mastercard"
          ],
          "minimum_amount": 1,
          "maximum_amount": 68607706,
          "recurring_enabled": true,
          "installment_payment_enabled": true
        },
        {
          "payment_method_type": "debit",
          "card_networks": [
            "Visa",
            "Mastercard"
          ],
          "minimum_amount": 1,
          "maximum_amount": 68607706,
          "recurring_enabled": true,
          "installment_payment_enabled": true
        }
      ]
    },
    {
      "payment_method": "pay_later",
      "payment_method_types": [
        {
          "payment_method_type": "klarna",
          "payment_experience": "redirect_to_url",
          "minimum_amount": 1,
          "maximum_amount": 68607706,
          "recurring_enabled": true,
          "installment_payment_enabled": true
        },
        {
          "payment_method_type": "affirm",
          "payment_experience": "redirect_to_url",
          "minimum_amount": 1,
          "maximum_amount": 68607706,
          "recurring_enabled": true,
          "installment_payment_enabled": true
        }
  }
}'
```

</details>

## **Resources**

* To explore more of our APIs, please check the remaining folders in the [Postman collection](https://www.postman.com/hyperswitch/workspace/hyperswitch-development/collection/25176162-630b5353-7002-44d1-8ba1-ead6c230f2e3)

## Next step:

{% content-ref url="../testing/test-a-payment.md" %}
[test-a-payment.md](../testing/test-a-payment.md)
{% endcontent-ref %}
