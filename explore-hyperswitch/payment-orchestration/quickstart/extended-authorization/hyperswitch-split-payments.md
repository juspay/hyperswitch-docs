---
description: Get started with Split Payments via Hyperswitch
icon: split
---

# Split Payments

Hyperswitch enables split payments, allowing a single transaction to be completed using more than one payment method. This is commonly used for gift card + card scenarios, where a customer pays partially with a gift card and covers the remaining balance with another method.

This capability helps merchants:

* Increase conversion when gift card balances are insufficient
* Improve customer flexibility at checkout
* Support common retail and digital wallet experiences

Hyperswitch manages the orchestration, balance checks, and sequential processing behind the scenes.

### Supported Scenarios

Currently, Hyperswitch supports:

* One or more gift cards combined with **at most one credit/debit card**
* Non-3DS card flows
* Gift Cards via Givex (through Adyen)

These configurations are designed to cover the most common real-world split payment use cases while maintaining predictable authorization behavior

### How Split Payment work at a high level

1. Customer applies a gift card in the Checkout SDK
2. Hyperswitch fetches and displays the gift card balance
3. If the balance is insufficient, the customer adds a card for the remaining amount
4. On payment confirmation:
   1. Payment methods are processed sequentially
   2. The remaining amount is charged to the card
   3. The gift card is charged for its applicable portion
5. If the gift card fully covers the amount, no secondary method is required

### Merchant Enablement

To activate split payments:

1. **Enable Split Payments** in the Hyperswitch Control Center for your business profile
2. Configure at least one connector that supports gift cards (e.g., Adyen)

No custom orchestration logic is required on the merchant side beyond standard SDK integration.



### Hyperswitch Split Payments Flow

<figure><img src="../../../../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

###







