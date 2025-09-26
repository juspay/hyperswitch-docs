---
description: Swift and streamlined payout automation
icon: file-invoice-dollar
---

# Process Payouts

Effortlessly facilitate swift payouts to your global network of sellers, merchants, and service providers using Hyperswitch's advanced automated system. Whether you're managing payments received through Hyperswitch or from other sources, leverage this infrastructure to streamline and orchestrate your payout processes efficiently.

<figure><img src="../../../.gitbook/assets/payouts.png" alt=""><figcaption></figcaption></figure>

The payouts feature enables businesses to transfer funds to third parties, such as sellers, service providers, or affiliates, using a wide range of payment methods, including bank accounts, cards, and wallets. Hyperswitch integrates seamlessly with global payment processors to facilitate these transactions. It helps:&#x20;

* Streamline and automate recurring and bulk payouts.
* Centralize payout tracking and improve operational efficiency.
* Reduce payout failures with smart retries tailored to specific errors.
* Ensure PCI-compliance and secure handling of sensitive payment information.

### How it helps your business?

**Supercharge Conversions**

* **Effortless Transfers**: Send funds to bank accounts or cards through your preferred payout method.
* **Smart Retries**: Enhance payout success rates with retries intelligently configured based on error types and connectors available.
* [List](https://hyperswitch.io/pm-list) of supported connectors.

**Simplify Operations**

* **Unified Dashboard**: Monitor all payouts across processors and partners from a single view.
* **Bulk Payouts**: Upload .xlsx or .csv files to manage large-scale payouts with ease.
* **Recurring Payouts**: Automate fixed-value payouts on a scheduled basis.

**Stay Secure**

* **Secure Card Handling**: PCI-compliant methods ensure safe acceptance, authentication, and storage of card details.
* **Independent Tokenization**: Tokenize card and bank data securely, independent of payment processors.
* **Bank Account Verification**: Enable verification for accounts with Stripe or other supported processors.

Business continuity with compatibility ensured for your Stripe connect onboarded sellers, merchants and service providers.

## Supported Processors and Payment Methods

#### Adyen

<table><thead><tr><th>Regions</th><th>Cards</th><th width="160">Banks</th><th>Wallets</th></tr></thead><tbody><tr><td>Europe</td><td>Major Networks </td><td>SEPA, SWIFT</td><td>Paypal, Neteller*, Skrill*</td></tr><tr><td>North America</td><td>Major Networks</td><td>ACH</td><td>Paypal</td></tr><tr><td>Others</td><td>Major Networks</td><td>SWIFT</td><td>Paypal</td></tr></tbody></table>

#### Cybersource

| Regions       | Cards           | Banks | Wallets |
| ------------- | --------------- | ----- | ------- |
| Europe        | Major Networks  | -     | -       |
| North America | Major Networks  | -     | -       |
| Others        | Major Networks  | -     | -       |

#### Ebanx

| Regions       | Cards | Banks   | Wallets |
| ------------- | ----- | ------- | ------- |
| Europe        | -     | -       | -       |
| North America | -     | -       | -       |
| Others        | -     | Pix\*\* | -       |

#### Paypal

| Regions       | Cards | Banks | Wallets       |
| ------------- | ----- | ----- | ------------- |
| Europe        | -     | -     | Paypal        |
| North America | -     | -     | Paypal, Venmo |
| Others        | -     | -     | Paypal        |

#### Stripe

| Regions       | Cards           | Banks | Wallets |
| ------------- | --------------- | ----- | ------- |
| Europe        | Major Networks  | SEPA  | -       |
| North America | Major Networks  | -     | -       |
| Others        | Major Networks  | -     | -       |

#### Wise

<table><thead><tr><th width="200">Regions</th><th>Cards</th><th>Banks</th><th>Wallets</th></tr></thead><tbody><tr><td>Europe</td><td>Major Networks</td><td>SEPA, SWIFT</td><td>-</td></tr><tr><td>North America</td><td>Major Networks</td><td>ACH</td><td>-</td></tr><tr><td>Others</td><td>Major Networks</td><td>SWIFT</td><td>-</td></tr></tbody></table>

{% hint style="info" %}
Methods marked with `*` are supported but not enabled by default.

Methods marked with `**` are in beta.
{% endhint %}

<table data-view="cards"><thead><tr><th></th><th data-hidden></th><th data-hidden></th></tr></thead><tbody><tr><td><mark style="color:blue;">Getting started with payouts</mark> </td><td></td><td></td></tr><tr><td><mark style="color:blue;">Payouts using saved payment methods</mark></td><td></td><td></td></tr><tr><td><mark style="color:blue;">Smart router for payout</mark></td><td></td><td></td></tr><tr><td><mark style="color:blue;">Smart retries for payouts</mark></td><td></td><td></td></tr><tr><td><mark style="color:blue;">Payout links</mark></td><td></td><td></td></tr></tbody></table>

## FAQs?

* **Can I use Hyperswitch solely for payouts without payments?** \
  Yes, Hyperswitch allows you to handle payouts independently. You can process payouts either through embedded payments or directly to a third party by providing direct payment information or using a token ID​​.
* **What does "independent tokenization" mean?** \
  Independent tokenization refers to the secure conversion of sensitive card and bank data into a token without dependency on any specific payment processor. \
  With Hyperswitch, this is possible when users permit saving their card or bank information. This ensures flexibility, allowing tokens to be used across various payment processors while maintaining data security and compliance​​.
