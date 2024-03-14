---
description: Swift and streamlined payout automation
---

# 💵 Payouts

{% hint style="info" %}
After reading this section, you will know about Payout features, supported processors, methods, working and how to get started with it.
{% endhint %}

Effortlessly facilitate swift payouts to your global network of sellers, merchants, and service providers using our automated system. Whether you're managing payments received through Hyperswitch or from other sources, leverage our infrastructure to streamline and orchestrate your payout processes efficiently.

<figure><img src="../../.gitbook/assets/payouts.png" alt=""><figcaption></figcaption></figure>

## Payouts combined with Payments

A way of paying out third parties combined with Hyperswitch's payments processing

*   **Supercharge Conversions**

    * Effortlessly send funds to bank accounts or cards using your preferred method
    * Boost success with smart retries.

    _Hyperswitch currently supports Adyen and Wise_
* **Simplify Operations**
  * All-in-One View: Monitor all payouts across partners in a single dashboard view
  * Bulk Payouts (submit a feature request [here](https://github.com/juspay/hyperswitch/discussions/new?category=ideas-feature-requests)): Manage large-scale payouts via simple file (.xlsx/.csv) uploads
  * Recurring Payouts (submit a feature request [here](https://github.com/juspay/hyperswitch/discussions/new?category=ideas-feature-requests)): Set up scheduled fixed-value payouts.
* **Stay Secure**
  * Secure Card Handling: PCI-compliant methods to accept, authenticate, and safely store card details. Plus, independent tokenization, irrespective of your payment processor.
  * Tokenize Bank Details (submit a feature request [here](https://github.com/juspay/hyperswitch/discussions/new?category=ideas-feature-requests)): Checkout page to accept and verify bank account verification for Stripe, along with processor-agnostic tokenization of bank details.

## Supported Processors and Payment Methods

#### Adyen

<table><thead><tr><th>Regions</th><th>Cards</th><th width="160">Banks</th><th>Wallets</th></tr></thead><tbody><tr><td>Europe</td><td>Major Networks</td><td>SEPA, SWIFT</td><td>Paypal, Neteller*, Skrill*</td></tr><tr><td>North America</td><td>Major Networks</td><td>ACH</td><td>Paypal</td></tr><tr><td>Others</td><td>Major Networks</td><td>SWIFT</td><td>Paypal</td></tr></tbody></table>

#### Wise

| Regions       | Cards          | Banks       | Wallets |
| ------------- | -------------- | ----------- | ------- |
| Europe        | Major Networks | SEPA, SWIFT | -       |
| North America | Major Networks | ACH         | -       |
| Others        | Major Networks | SWIFT       | -       |

**\*** _Payout methods supported by processor but not recommended (can be enabled upon request)_

**Payouts for Stripe Connect users (submit a feature request** [**here**](https://github.com/juspay/hyperswitch/discussions/new?category=ideas-feature-requests)**)**

* Business continuity with compatibility ensured for your Stripe connect onboarded sellers, merchants and service providers.

## FAQs?

* **Can I use Hyperswitch solely for payouts without payments?** Absolutely. You can payout with embedded payments or directly to a third party by providing direct payment info or token ID.
* **What does "independent tokenization" mean?** Independent tokenization means that your card and bank data are converted into a secure token, irrespective of which payment processor you use, with Hyperswitch. (We tokenize only when the user permits us to save their card/bank info)

