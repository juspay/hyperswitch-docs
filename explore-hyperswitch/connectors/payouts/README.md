---
description: Swift and streamlined payout automation
icon: file-invoice-dollar
---

# Payouts Processors

### Overview

The Hyperswitch Payouts infrastructure allows you to programmatically distribute funds to third parties, including affiliates, contractors, and merchants, across a variety of payment methods. By integrating with global processors, Hyperswitch helps you manage the entire payout lifecycle from a single point of control.

* Automate at scale: Orchestrate high-volume bulk payouts or schedule recurring distributions.
* Optimize reliability: Use [smart retries](https://docs.hyperswitch.io/explore-hyperswitch/connectors/payouts/smart-retries-in-payout) and routing to minimize failed transfers.
* Maintain compliance: Reduce your PCI burden with secure, [processor-agnostic tokenization](https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/tokenization-and-saved-cards/network-tokenisation).
* Unified visibility: Track every payout across different regions and connectors in one dashboard.

<figure><img src="../../../.gitbook/assets/payouts.png" alt=""><figcaption></figcaption></figure>

### Key Features

#### High-velocity distribution

Move funds to bank accounts, cards, or digital wallets through your preferred connectors. Whether you are using funds collected through Hyperswitch or external sources, our API ensures a seamless transfer experience.

#### Intelligence and routing

Maximize payout success with [Smart Retries](https://docs.hyperswitch.io/explore-hyperswitch/connectors/payouts/smart-retries-in-payout). If a payout fails due to a temporary connector error, Hyperswitch automatically retries the transaction through the most viable path, ensuring your partners get paid on time without manual intervention.

#### Flexible data handling

* Independent Tokenization: Securely store card and bank data using our processor-independent vault. This gives you the flexibility to switch payout partners without losing your users' payment credentials.
* Bulk Operations: Effortlessly manage large-scale disbursements by uploading `.xlsx` or `.csv` files directly via the dashboard.
* Account Verification: Ensure the validity of recipient bank accounts through Stripe or other supported verification providers.

### Supported Connectors and Methods

Hyperswitch abstracts the complexity of regional payment rails. The table below outlines our currently supported payout combinations.

| Connector       | Regions | Cards          | Bank Rails       | Wallets                      |
| --------------- | ------- | -------------- | ---------------- | ---------------------------- |
| **Adyen**       | Global  | Major Networks | SEPA, SWIFT, ACH | PayPal, Neteller\*, Skrill\* |
| **Stripe**      | Global  | Major Networks | SEPA             | —                            |
| **Wise**        | Global  | Major Networks | SEPA, SWIFT, ACH | —                            |
| **PayPal**      | Global  | —              | —                | PayPal, Venmo (US)           |
| **Ebanx**       | LATAM   | —              | Pix\*\*          | —                            |
| **Cybersource** | Global  | Major Networks | —                | —                            |

{% hint style="info" %}
Methods marked with `*` are supported but not enabled by default.

Methods marked with `**` are in beta.
{% endhint %}

### FAQ

Can I use Hyperswitch solely for payouts without payments? \
Yes. Hyperswitch is modular. You can use our infrastructure to handle payouts independently of your payment collection. You can initiate payouts via direct payment info or by using an existing Token ID.

What is the benefit of independent tokenization?\
It prevents vendor lock-in. By tokenizing sensitive data independently of the underlying processor, you retain ownership of your data and can route payouts to any supported connector without asking your users to re-enter their information.
