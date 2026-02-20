---
icon: hand-holding-circle-dollar
---

# Payment Method (Card)

Hyperswitch provides flexible payment processing with multiple flow patterns to accommodate different business needs. The system supports one-time payments, saved payment methods, and recurring billing through a comprehensive API design.

{% hint style="info" %}
### Integration Path

#### Server-to-Server (S2S) Payments (Tokenize followed by Payment)

Refer to this section if you intend to use the SDK exclusively for vaulting/storing card details. In this scenario, the actual payment execution is handled via S2S API calls from your backend to Hyperswitch, offering you more granular control over the transaction lifecycle.
{% endhint %}

Payment method flows leverages all the capabilities available in [Payments](https://docs.hyperswitch.io/~/revisions/Moc8cqgBbfb8T8KrBi8V/about-hyperswitch/payment-suite-1/payments-cards). The primary goal here is to allow the business to control the payment journey via S2S APIs and a token or `payment_method_id`&#x20;

The business can use the Payment Method SDK or `/payment-methods` API to first capture the card details and create a `payment_method_id` &#x20;

The business can then use the `payment_method_id` in `/payments` API to perform all functionalities supported by the [Payments](https://docs.hyperswitch.io/~/revisions/Moc8cqgBbfb8T8KrBi8V/about-hyperswitch/payment-suite-1/payments-cards) flow.&#x20;



**Payment Method Lifecycle**

The Payment Method flow leverages the full suite of Hyperswitch [Payment](https://docs.hyperswitch.io/~/revisions/Moc8cqgBbfb8T8KrBi8V/about-hyperswitch/payment-suite-1/payments-cards) capabilities while granting businesses granular control over the user journey. By utilizing Server-to-Server (S2S) APIs and unique identifiers `payment_method_id`, businesses can separate the collection of payment credentials from the actual transaction logic.

**The Two-Step Integration Pattern**

1. **Credential Capture & Vaulting**

The business initiates the flow by capturing payment details (such as cards, wallets, or bank accounts) using either the Payment Method SDK or the `/payment-methods` API. This process securely vaults the payment instrument and generates a unique `payment_method_id`.

2. **Transaction Execution**

Once the `payment_method_id` is generated, it serves as a reusable token. The business can pass this ID into the /payments API to execute any supported [Payment](https://docs.hyperswitch.io/~/revisions/Moc8cqgBbfb8T8KrBi8V/about-hyperswitch/payment-suite-1/payments-cards) functionality without re-collecting sensitive data.

The `payment_method_id` serves as a unique identifier mapped to a specific combination of a Customer ID and a unique Payment Instrument (e.g., a specific credit card, digital wallet, or bank account).

* Logic: A single customer can have multiple payment methods, each assigned a distinct ID. However, the same payment instrument used by the same customer will always resolve to the same `payment_method_id`.
* Scope: This uniqueness applies across all payment types, including cards, wallets, and bank details.

| **Customer ID** | **Payment Instrument**            | **Payment Method ID** |
| --------------- | --------------------------------- | --------------------- |
| 123             | Visa ending in 4242               | `PM1`                 |
| 123             | Mastercard ending in 1111         | `PM2`                 |
| 456             | Visa ending in 4242               | `PM3`                 |
| 123             | PayPal Account (`user@email.com`) | `PM4`                 |
