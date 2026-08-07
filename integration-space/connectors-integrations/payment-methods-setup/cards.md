---
description: Accept debit and credit card payments on your application
icon: credit-card
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/kf7BGdsPkCw9nalhAIlE/other-features/payment-orchestration/quickstart/payment-methods-setup/cards
---

# Cards

![logo\_discord](https://hyperswitch.io/logos/logo_diners.svg) ![logo\_discord](https://hyperswitch.io/logos/logo_visa.svg) ![logo\_discord](https://hyperswitch.io/logos/logo_mastercard.svg) ![logo\_discord](https://hyperswitch.io/logos/logo_amex.svg)

Juspay Hyperswitch supports credit and debit card payments through all our payment processor connectors. We accept cards from all major global and local card networks, such as Visa, Mastercard, American Express, Diners, Discover, JCB, Union Pay, etc. While Hyperswitch supports card payments in 135+ currencies and 150+ countries, each of these connectors and networks has limitations in terms of the number of countries and currencies they support.

Apart from regular one-time payments, Hyperswitch supports saving a card, recurring payments, and placing a hold for later capture.

### Integration Steps

1. Go to Hyperswitch dashboard and to connectors tab [here](https://app.hyperswitch.io/dashboard/connectors) and enable card.

### Saved Cards

You could use Hyperswitch's PCI Compliant secure vault to safely store your customers' card data and retrieve them when they return to pay on your website/app. In addition, our hyper SDK has a checkbox on the payment page that you can use to take customers' consent to store their card data. To try out the save cards feature through API, include either of the values for the `setup_future_usage` field in your Payments API request body. This feature comes with [Unified Checkout](../../../integration-guide/payment-experience/payment/web/).

The Saved cards feature comes out of the box without any additional integration steps. The Unified Checkout SDK will fetch the saved cards details and show them to your users. All you need to do is create a customer or send a customer id when you call the Payments API. The cards belonging to that customer ID are securely stored and retrived from the card vault.

Follow the below guide to learn how to make a saved card payment using Hyperswitch

{% content-ref url="../../tokenization-and-saved-cards/" %}
[tokenization-and-saved-cards](../../tokenization-and-saved-cards/)
{% endcontent-ref %}

### Recurring Payments - Mandate through cards

Hyperswitch supports the creation of mandates for card transactions through various payment processors to collect card information from the customer and authorize a mandate. The mandate can then be charged against at specific intervals and specific amounts based on the mandate setup.

Follow the below guide to learn how to make a recurring payment with Hyperswitch

{% content-ref url="../../../integration-guide/payment-suite/payments/save-a-payment-method/" %}
[save-a-payment-method](../../../integration-guide/payment-suite/payments/save-a-payment-method/)
{% endcontent-ref %}

### Auth and Capture

By default, all payments are auto-captured during authorization in Hyperswitch, but you can choose to separate capture from authorization by manually capturing an authorized payment later. Setting the `capture` field in payments/confirm API to `manual` will block the stated amount on the customer's card without charging them. To charge the customer an amount equal to or lesser than the blocked amount, use the payments/capture endpoint with the relevant details.

---

### Supported Payment Flows

| Flow | Description | Key API fields |
| --- | --- | --- |
| **One-time (CIT)** | Customer-initiated single charge | `payment_method: card`, `payment_method_data.card.*` |
| **3DS authentication** | Cardholder challenged via issuer — reduces fraud liability | `authentication_type: three_ds` |
| **No-3DS** | Skip authentication — higher approval rate, merchant bears fraud liability | `authentication_type: no_three_ds` |
| **Saved card (on-session)** | Charge a previously vaulted card with customer present | `payment_token` or `recurring_details.type: payment_method_id` |
| **MIT / off-session mandate** | Merchant-initiated charge against a stored mandate | `mandate_id`, `off_session: true` |
| **Auth + manual capture** | Block funds now, capture later (up to connector's hold window) | `capture_method: manual`, then `POST /payments/:id/capture` |
| **$0 verification** | Verify card validity without charging | `amount: 0`, `confirm: true` |

---

### Required API Fields per Flow

**One-time card payment**
```json
{
  "payment_method": "card",
  "payment_method_data": {
    "card": {
      "card_number": "4242424242424242",
      "card_exp_month": "12",
      "card_exp_year": "2030",
      "card_holder_name": "John Doe",
      "card_cvc": "100"
    }
  }
}
```

**Creating a mandate (CIT — first charge)**
```json
{
  "setup_future_usage": "off_session",
  "customer_id": "cus_xyz"
}
```

**Charging against a mandate (MIT — subsequent charge)**
```json
{
  "mandate_id": "man_xyz",
  "off_session": true,
  "customer_id": "cus_xyz"
}
```

**Manual auth then capture**
```json
// POST /payments  (authorize only)
{ "capture_method": "manual" }

// POST /payments/:id/capture
{ "amount_to_capture": 1000 }
```

---

### Common Failure Modes

**Card declined**
Symptom: Payment returns `payment_failed` with a decline code. Fix: Check the issuer decline code in `error_code` — common values are `insufficient_funds`, `do_not_honor`, `card_velocity_exceeded`. Retry with a different card or ask the customer to contact their bank. Do not retry declined cards automatically without changing something (e.g., reduced amount, different card).

**3DS not triggered when expected**
Symptom: Payment skips authentication and fails at authorization. Fix: Ensure `authentication_type: three_ds` is set on the payment. Also verify the connector has 3DS enabled on its dashboard and the card BIN is enrolled in 3DS. Authorize.net does not support native 3DS — route 3DS-required payments to a different connector.

**Mandate charge fails after setup**
Symptom: MIT charge returns `mandate_invalid` or `customer_not_found`. Fix: Verify `mandate_id` and `customer_id` are from the original CIT that set up the mandate. MIT charges must use `off_session: true` and the same customer ID as the mandate creation.

**Card network not accepted**
Symptom: Payment fails with `card_network_not_supported`. Fix: Verify the card network (e.g., UnionPay, Discover) is enabled on your connector dashboard. Some connectors require explicit network enablement per region.
