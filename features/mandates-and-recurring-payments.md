---
description: Setting up and managing recurring payments
---

# 🔁 Mandates & recurring payments

{% hint style="info" %}
With this section, let's setup and execute recurring payments with hyperswitch.
{% endhint %}

Hyperswitch supports recurring payments by creating mandates - a record of the permission that your customer provides to debit their payment method such as cards, wallets, etc later for the specified amount and period.

## Setting up a Recurring payment

You can set up a recurring payment by creating a mandate by passing the **mandate\_type** details under the **`mandate_data`** object and the **`setup_future_usage`** field with value as ‘off\_session’ during payments/create API request.

Our Unified checkout takes care of the remaining mandate creation process by showing the customers a mandate acceptance form during payment that explicitly gathers their permission to store and charge their payment method later. The required data for the **customer\_acceptance** object under the **mandate\_data** object in payments API is also automatically gathered by our Unified checkout and passed to the Hyperswitch backend.

On successful mandate creation, a **`mandate_id`** is generated against the payment and this can be found in your dashboard.

## Executing Recurring Transactions

Once you have the **mandate\_id**, you can pass the **mandate\_id** in payments/create API requests along with the **`off_session`** field as ‘true’ and ‘**`confirm`**’ as ‘true’ from your server when you want to charge your customer later when they are not present in your checkout flow.

Your customers’ payment method would be charged automatically in most cases without any Strong Customer Authentication (SCA) prompts. In case your customers are required to perform a SCA authentication by the processor, Hyperswitch will transition the payment’s status to ‘requires\_customer\_action’ state and you would need to notify your customer to come to the checkout flow to complete the authentication and payment.

## Try a Mandate/Recurring payment on Hyperswitch

* To setup a mandate, make a request to the [payments](https://api-reference.hyperswitch.io/api-reference/payments/payments--create) endpoint with **`mandate_data`** object along with other necessary fields  (**`amount, currency, payment_method, payment_method_type, payment_method_data`**) and **`confirm=true`**
* Make a recurring payment by making another request to  [payments](https://api-reference.hyperswitch.io/api-reference/payments/payments--create) endpoint by passing the **`mandate_id`** received in the previous step along with **`off_session`** field

## Troubleshooting: Common errors and workarounds
