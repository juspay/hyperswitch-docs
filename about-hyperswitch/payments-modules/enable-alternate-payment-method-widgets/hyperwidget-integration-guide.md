---
icon: plug-circle-bolt
---

# Hyperwidget Integration Guide

Once the merchant signs up onto the unified dashboard, they’ll get their API keys and can enable the APMs <> PSP combinations that they would like to provide on their checkout.&#x20;

Hyperswitch provides a code transformer that allows the merchant to leverage their existing integration (with PSP or middle layer) and make a call to Hyperswitch server with minimal changes. Hyperwidget acts as a Unified wrapper on top of all major APMs and simplifies up-scaling or down-scaling of these APMs across one or multiple PSPs.&#x20;

The unified dashboard offers the merchants ability to enable or disable APMs via any PSP. The dashboard also offers capabilities like - Analytics, Operations, Refunds, Chargebacks, and Reconciliation.

<figure><img src="../../../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

### Supported APM features:

| Payment Method | Region  | Type         | Supported flow          | Shipping Address availability | Billing address availability |
| -------------- | ------- | ------------ | ----------------------- | ----------------------------- | ---------------------------- |
| Paypal         | US + EU | Wallet       | SDK flow, Redirect flow | Yes\*                         | Yes                          |
| Apple Pay      | US + EU | Wallet       | SDK flow                | Yes\*                         | Yes                          |
| Google Pay     | US + EU | Wallet       | SDK flow                | Yes\*                         | Yes                          |
| Paze           | US + EU | Wallet       | SDK flow                | No                            | Yes                          |
| Samsung Pay    | US + EU | Wallet       | SDK flow                | No                            | No                           |
| Ali Pay        | US + EU | Wallet       | Redirect flow           | Yes                           | Yes                          |
| WeChat Pay     | US + EU | Wallet       | Redirect flow           | Yes                           | Yes                          |
| Affirm         | US + EU | BNPL         | Redirect flow           | Yes                           | Yes                          |
| Klarna         | US + EU | BNPL         | SDK flow, Redirect flow | Yes\*                         | Yes                          |
| Afterpay       | US + EU | BNPL         | Redirect flow           | Yes                           | Yes                          |
| iDEAL          | EU      | Bank-to-bank | Redirect flow           | Yes                           | Yes                          |
| SEPA           | EU      | Bank-to-bank | Redirect flow           | Yes                           | Yes                          |

\*only in the SDK flow

### Steps to integrate Hyperwidgets:&#x20;

To start collecting payments via the APM of your choice, follow these simple steps: ​

* [Install the Hyperwidgets SDK following these steps.](https://docs.hyperswitch.io/hyperswitch-cloud/integration-guide/web/node-and-react)
  * As we have a single SDK to manage all APMs, thus the integration steps are similar to the ones for integrating Unified Checkout.
* [For customizations on the Checkout Page follow this guide.](https://docs.hyperswitch.io/explore-hyperswitch/merchant-controls/integration-guide/web)&#x20;

{% content-ref url="../../../explore-hyperswitch/merchant-controls/payment-features/click-to-pay/" %}
[click-to-pay](../../../explore-hyperswitch/merchant-controls/payment-features/click-to-pay/)
{% endcontent-ref %}
