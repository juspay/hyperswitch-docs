---
description: >-
  Leverage the integrated vault that comes with Hyperswitch Orchestration
  account to store cards
icon: box-circle-check
---

# SaaS Orchestration with Juspay Vault

This is the fully managed Hyperswitch SaaS model, where Juspay handles both orchestration and PCI responsibilities.\
Merchants can tokenize, vault, and process without any PCI exposure.

Key Highlights:

* No PCI compliance overhead.
* Automatic network tokenization and lifecycle management.
* Simplified setup — single integration for orchestration + vault.

### SaaS orchestration - Payments and vaulting flow

<figure><img src="../../../.gitbook/assets/image (114).png" alt=""><figcaption></figcaption></figure>

The sequence diagram above outlines how a SaaS merchant performs payments and vaulting

**New user payments flow**

1. For self-hosting the Hyperswitch orchestration stack including vault follow the [self-hosting guide](../../../hyperswitch-open-source/deploy-on-kubernetes-using-helm/)
2. Load the Hyperswitch SDK. The end-user enters their payment credentials for the selected payment option
3. The [Payments Create API request ](https://api-reference.hyperswitch.io/v1/payments/payments--create)containing the payment method is sent to the PSP from Hyperswitch
4. Once the PSP responds with the outcome `approved` or `declined` along with the PSP token, Hyperswitch then proceeds to store and tokenize the card.
5. The card is stored in Hyperswitch vault and a `payment_method_id` is generated. A `payment_method_id` is a versatile token and connects a lot of entities together&#x20;

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

6. This `Payment_method_id` is returned to the merchant via webhooks

**Repeat user payments flow**

1. In a repeat-user the payment, the Hyperswitch SDK will load the stored payment methods of the customer based the `customer_id` sent as part of the [Payments Create API request ](https://api-reference.hyperswitch.io/v1/payments/payments--create).&#x20;
2. The end-user can select the desired payment option and add their `CVV`&#x20;
3. The SDK sends the [Payment Confirm API request](https://api-reference.hyperswitch.io/v1/payments/payments--confirm) when the user hits `Pay`&#x20;
4. The Hyperswitch backend resolves the `payment_method_id` to identify available payment credentials - card, PSP token, network token and more
5. It sends payload with appropriate credential to the payment provider or PSP downstream based on the merchant configurations

**Merchant Initiated Transaction (MIT) flow**

1. The merchant can perform the [MIT or Recurring transactions](../../../about-hyperswitch/payment-suite-1/payments-cards/recurring-payments.md) using `payment_method_id`
