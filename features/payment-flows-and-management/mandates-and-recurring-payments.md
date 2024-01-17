---
description: Setting up and managing recurring payments
---

# 🔁 Mandates & recurring payments

{% hint style="info" %}
With this section, let's setup and execute recurring payments with Hyperswitch.
{% endhint %}

Hyperswitch supports recurring payments by creating mandates - a record of the permission that your customer provides to debit their payment method such as cards, wallets, etc for the specified amount and period, at a later point in time. You can also work with a subscription provider of your choice and use Hyperswitch for payments, both one-time and recurring ([more details](https://docs.hyperswitch.io/features/payment-flows-and-management/subscriptions))

## Setting up a Recurring payment

You can set up a recurring payment by creating a mandate by passing the **mandate\_type** details under the **`mandate_data`** object and the **`setup_future_usage`** field with value as ‘off\_session’ during payments-create API request.

Our Unified checkout takes care of the remaining mandate creation process by showing the customers a mandate acceptance form, during payment, that explicitly gathers their permission to store and charge their payment method later. The required data for the **customer\_acceptance** object under the **mandate\_data** object in payments API is also automatically gathered by our Unified checkout and passed to the Hyperswitch backend.

On successful mandate creation, a **`mandate_id`** is generated against the payment and this can be found in your dashboard.

## Executing Recurring Transactions

Once you have the **mandate\_id**, you can pass the **mandate\_id** in payments/create API requests along with the **`off_session`** field as ‘true’ and ‘**`confirm`**’ as ‘true’ from your server when you want to charge your customer later when they are not present in your checkout flow.

Your customers’ payment method would be charged automatically in most cases without any Strong Customer Authentication (SCA) prompts. In case your customers are required to perform a SCA authentication by the processor, Hyperswitch will transition the payment’s status to ‘requires\_customer\_action’ state and you would need to notify your customer to come to the checkout flow to complete the authentication and payment.

## Try creating a Mandate/Recurring payment on Hyperswitch

### **1.  Create a mandate payment from your server:**&#x20;

Make a request to the [payments](https://api-reference.hyperswitch.io/api-reference/payments/payments--create) endpoint with **`mandate_data`** object along with other necessary fields  (**`amount, currency, payment_method, payment_method_type, payment_method_data`**) and **`confirm=true`**

**Sample curl:**

```bash
curl --location 'https://sandbox.hyperswitch.io/payments' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'api-key: <your-hyperswitch-api-key>' \
--data '{
    "amount": 6540,
    "currency": "USD",
    "confirm": false,
    "customer_id":"StripeCustomer123",
    "authentication_type": "no_three_ds",
    "setup_future_usage": "off_session",
    "mandate_data": {
        "mandate_type": {
            "single_use": {
                "amount": 7000,
                "currency": "USD"
            }
        }
    }
}
```

### **2.  Confirm the mandate payment after collecting payment\_method\_data and customer\_acceptance from Unified checkout**

**Collect payment method information like card number or bank account number along with an acceptance from the customer stating that you would be storing their payment method details and charging them later even if they aren't in the flow. Pass these information in payments/confirm API. If you're using Unified checkout, this is taken care by it automatically.**

**Sample curl:**

````bash
curl --location 'https://sandbox.hyperswitch.io/payments/<original_payment_id>/confirm' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'api-key: <your_publishable_key>' \
--data '{
    "client_secret": "<client_secret_of_the_original_payment>",
    "payment_method": "card",
    "payment_method_data": {
        "card": {
            "card_number": "4242424242424242",
            "card_exp_month": "10",
            "card_exp_year": "25",
            "card_holder_name": "joseph Doe",
            "card_cvc": "123"
        }
    },
    "mandate_data": {
        "customer_acceptance": {
            "acceptance_type": "online",
            "accepted_at": "2023-11-03T04:07:52.723Z",
            "online": {
                "ip_address": "127.0.0.1",
                "user_agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
            }
        }
    }
}'
```
````

### 3. Make a recurring payment from your server by passing mandate\_id and off\_session fields:

Once you've created a mandate, store the `mandate_id` from the previous step. Whenever you want to make a recurring payment against the customer, pass the `mandate_id` in payments/create request along with:

* `off_session=true` to indicate that the customer is not in the flow&#x20;
* `confirm=true` to confirm the payment in one-step

````bash
curl --location 'https://sandbox.hyperswitch.io/payments' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'api-key: <your_api_key>' \
--data '{
    "amount": 6540,
    "currency": "USD",
    "confirm": true,
    "customer_id": "cus_abc_123",
    "authentication_type": "no_three_ds",
    "mandate_id": "<mandate_id>",
    "off_session": true
}'
```
````

## FAQ:

### **1. Does Hyperswitch support Automatic recurring payments/subscriptions at pre-defined intervals?**

No, Hyperswitch doesn't currently support automatic recurring payments at pre-defined intervals. This feature would be available soon under our Subscription module that is in development (Q1 2024). Until then, merchants can trigger recurring payments from their server by setting up the trigger schedules in their server.

