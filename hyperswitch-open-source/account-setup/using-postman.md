---
description: >-
  Create your Hyperswitch account and add a payment provider using Hyperswitch
  APIs through postman
icon: rocket-launch
---

# Using postman

## Create a Hyperswitch account <a href="#user-content-create-a-payment" id="user-content-create-a-payment"></a>

​Hyperswitch operates on a multi-tenant architecture, enabling a single application server to support multiple merchants. To create a new merchant account, follow these steps:​

1. **Locate the Admin API Key**:
   * Find the `config/docker_compose.toml` file in your Hyperswitch setup.​
   * Search for the `api_key` entry within this file to retrieve your admin API key.​
2. **Execute the cURL Command**:
   * Use the following cURL command to create a merchant account:​
   * Replace `<admin-api-key>` with your actual admin API key.

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

3. **Receive the Response**:

* Upon executing the command, you should receive a response containing the `merchant_id` and `publishable_key`.​

## Create an API key <a href="#user-content-create-an-api-key" id="user-content-create-an-api-key"></a>

To generate an API key for your merchant account in Hyperswitch, follow these steps:​

1. **Prepare the cURL Command**:
   * Replace `<your_merchant_id>` with the `merchant_id` obtained from the previous step.​
   * Replace `<admin-api-key>` with your admin API key.​

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

2. **Secure the API Key**:

* The response will include the plaintext API key. Store this key securely, as it is essential for authenticating API requests from your merchant server.​

## Set up a payment processor <a href="#user-content-set-up-a-payment-processor-account" id="user-content-set-up-a-payment-processor-account"></a>

​To integrate your preferred payment processor with Hyperswitch, follow these steps:​

**1. Obtain API Credentials from Your Payment Processor:**

* Sign up with your chosen payment processor (e.g., Stripe, Adyen) and acquire the necessary API credentials.​

2. **Set Up the Payment Processor in Hyperswitch:**
   * Use the following cURL command to configure the payment processor
     * Replace `<your_merchant_id>` with your merchant ID obtained earlier.
     * Replace `<admin-api-key>` with your admin API key.
     * Replace `<connector_name>` with the name of your payment processor (e.g., "stripe").
     * Replace `<connector_api_key>` with the API key provided by your payment processor.

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

**3. Customize Connector Account Details:**

* The `connector_account_details` field requires specific authentication details for your chosen payment processor. For payment processors, the required fields may vary. You can find payment provider-specific details to be included in this [spreadsheet](https://docs.google.com/spreadsheets/d/e/2PACX-1vQWHLza9m5iO4Ol-tEBx22_Nnq8Mb3ISCWI53nrinIGLK8eHYmHGnvXFXUXEut8AFyGyI9DipsYaBLG/pubhtml?gid=748960791\&single=true).

**4. Enable Payment Methods:**

* In the `payment_methods_enabled` section, specify the payment methods and types you wish to enable. For example, to enable credit card payments via Visa and Mastercard, include them as shown in the cURL command above.

## **Resources**

* To explore more of our APIs, please check the remaining folders in the [Postman collection](https://www.postman.com/hyperswitch/workspace/hyperswitch-development/collection/25176162-630b5353-7002-44d1-8ba1-ead6c230f2e3)

## Next step

{% content-ref url="test-a-payment.md" %}
[test-a-payment.md](test-a-payment.md)
{% endcontent-ref %}
