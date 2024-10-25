---
icon: arrow-up-right-dots
---

# Incremental Authorization

## What is Incremental Authorization?

Generally for any payment transaction, the payable amount from the payment request is authorized and then captured. But in some situations like hotel bookings, car rentals, or services where the final cost is uncertain, we might need to increase the authorized amount.&#x20;

Incremental authorization in Hyperswitch allows merchants to request additional funds after the initial authorization, giving them the flexibility to handle changing costs without disrupting the customer’s payment experience.

## Why is it important?

Incremental authorization extends the ability to request more funds beyond the original authorized amount, which is perfect for aforementioned situations like hotel bookings, car rentals, or services where the final cost is uncertain. Hyperswitch enables merchants to easily add charges during the checkout process without affecting the user journey for re-authorization.

### How Incremental Authorization Helps Businesses?

Incremental authorization can help businesses to fulfill the following use-cases:&#x20;

* **Adjust Payments in Real-Time**: Handle unexpected increases in charges, such as additional services or extended stays without redirecting customers for re-authorization.
* **Improve Customer Experience**: Avoid disruptions in the payment process, as customers do not need to reauthorize or re-enter their payment information.
* **Streamline Settlements**: Hyperswitch combines the initial charge and all incremental authorizations into a single settlement, simplifying reconciliation.

## Pre-requisites-&#x20;

1. Ensure that your business operates in a region without Strong Customer Authentication (SCA) requirements, as incremental authorizations are only possible in such environments.
2. This feature is limited to card payments and specific networks, with rules that vary depending on the payment connector used.

### How to use Incremental Authorization through Hyperswitch?

**Step 1:** To use Incremental authorization you can set the value of the [request\_incremental\_authorization](https://api-reference.hyperswitch.io/api-reference/payments/payments--create) field to true in the payments/create API call.

```
curl --request POST \
  --url https://sandbox.hyperswitch.io/payments \
  --header 'Content-Type: application/json' \
  --header 'api-key: <api-key>' \
  --data '{
  "amount": 6540,
  "authentication_type": "three_ds",
  "currency": "USD",
  “request_incremental_authorization”: “true”
}'
```

**Step 2:** In the response, you can find whether the connector allows the Incremental authorization for that particular payment intent or not, refer to [incremental\_authorization\_allowed](https://api-reference.hyperswitch.io/api-reference/payments/payments--create) field in API response.

**Step 3:** Use the below curl to make the Incremental authorization requests.

```
curl --request POST \
  --url https://sandbox.hyperswitch.io/payments/{payment_id}/incremental_authorization \
  --header 'Content-Type: application/json' \
  --header 'api-key: <api-key>' \
  --data '{
  "amount": 6540,
  "reason": "<string>"
}'
```

\


\
