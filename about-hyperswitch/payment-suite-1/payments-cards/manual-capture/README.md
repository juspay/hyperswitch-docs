---
description: >-
  Understand how to place a hold on your customers' funds and capture them later
  either fully or partially and either in one-go or multiple times
icon: transmission
---

# Manual Capture

{% embed url="https://youtu.be/XtOMZVhvLwQ" %}

In most online payments use-cases, a merchant would want to capture the funds from their customers' accounts in one-step after the issuer authorizes the payment. This is called 'one-step' payments flow and at Hyperswitch we term this the 'Automatic Capture' flow.

But in some cases, merchants would like to place a hold on the customer's funds post authorization so that they can capture the funds at a later time once they deliver the goods and services. This is called the 'two-step' flow or 'Auth and Capture' flow in general payments parlance. Here at Hyperswitch, we call this the 'Manual Capture' flow.

### Benefits of Manual Capture

1. Improved Control: Funds are captured only after goods or services are delivered.
2. Flexibility: You can capture the full amount or a partial amount as per the delivery.
3. Customer Satisfaction: Builds trust by charging customers only after fulfilling the order.

### How to do Manual Capture?

#### Step 1 — Create [Payment](https://api-reference.hyperswitch.io/v1/payments/payments--create) with Deferred Capture

The 'capture\_method' field determines the type of capture for a particular payment and it defaults to 'automatic' if not passed. So, to do manual capture, set `"capture_method" = "manual"` when creating a payment from your server

**Sample curl:**

```bash
curl --location 'https://sandbox.hyperswitch.io/payments' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'api-key: <your_api_key>' \
--data '{
    "amount": 6540,
    "currency": "USD",
    "confirm": false,
    "capture_method": "manual",
    "authentication_type": "no_three_ds",
    "return_url": "https://duck.com",
    "billing": {
        "address": {
            "line1": "1467",
            "line2": "Harrison Street",
            "line3": "Harrison Street",
            "city": "San Fransico",
            "state": "California",
            "zip": "94122",
            "country": "US",
            "first_name": "John"
        }
    }
}'
```

#### Step 2 — Confirm (Authorization Phase)

[Confirm](https://api-reference.hyperswitch.io/v1/payments/payments--confirm) the payment after collecting the payment\_method details from your customer and informing them that the funds in their account would be blocked and charged later once the goods and services are delivered. Unified checkout handles this for automatically. On successful authorization, the payment would transition to `'requires_capture'` status.

Note - You can mark `"confirm" = "true"` in the previous step and directly move to the capture flow.&#x20;

**Sample curl:**

```bash
curl --location 'https://sandbox.hyperswitch.io/payments/<original_payment_id>/confirm' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'api-key: <your_publishable_key>' \
--data '{
    "payment_method": "card",
    "client_secret": "<client_secret_of_the_original_payment>",
    "payment_method_data": {
        "card": {
            "card_number": "4242424242424242",
            "card_exp_month": "10",
            "card_exp_year": "25",
            "card_holder_name": "joseph Doe",
            "card_cvc": "123"
        }
    }
}'
```

#### Step 3 — Capture Funds via [Capture API](https://api-reference.hyperswitch.io/v1/payments/payments--capture#payments-capture)

After delivering the goods and services, capture the payment by passing the `payment_id` from above step to `payments/capture` API endpoint. On successful capture, the payment would transition from `'requires_capture'` to `'succeeded'` status.

**Sample curl:**

```bash
curl --location 'https://sandbox.hyperswitch.io/payments/pay_At7O43TJJZyP7OmrcdQD/capture' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'api-key: <your_api_key>' \
--data '{
    "amount_to_capture": 6540,
    "statement_descriptor_name": "Joseph",
    "statement_descriptor_suffix": "JS"
}'
```

### Capture types available :

#### **Full capture**

Capture the full amount that was authorized - Here the payments status transitions to 'SUCCEEDED' as soon the  `payments/capture` API endpoint is executed for the `payment_id` .

#### **Partial Capture**&#x20;

Capture only a partial amount from the total amount that was authorized. Once the transaction is executed, the status goes to either `partially_captured` or `partially_captured_and_capturable` &#x20;

1. When capture method is manual & single capture is supported - `partially_captured`
2. When capture method is manual & multiple captures are supported - `partially_captured_and_capturable`  <br>

Possible states:

| Connector Capability       | Resulting Status                    |
| -------------------------- | ----------------------------------- |
| Single capture only        | `partially_captured`                |
| Multiple capture supported | `partially_captured_and_capturable` |

#### Over Capture &#x20;

Over Capture occurs when a merchant captures (settles) an amount greater than the originally authorized amount. You can find detailed docs [here](https://docs.hyperswitch.io/~/revisions/KHifKaZGv4c5XEloMvlu/about-hyperswitch/payment-suite-1/payments-cards/manual-capture/overcapture)&#x20;

