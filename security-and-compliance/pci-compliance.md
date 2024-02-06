---
description: A brief summary of PCI compliance for Hyperswitch Cloud users
---

# 💳 PCI Compliance

Hyperswitch Cloud offers out-of-the-box PCI compliance, so that you do not have to worry about securing and storing customers's cards.

## PCI DSS Level 1 compliance <a href="#docs-internal-guid-959e0903-7fff-fc13-1542-001b2640a715" id="docs-internal-guid-959e0903-7fff-fc13-1542-001b2640a715"></a>

Hyperswitch is Level 1 PCI DSS 3.2.1 certified which is the strictest level of compliance to handle card data securely.

The infrastructure and application are annually audited with a PCI approved scanning vendor to keep the PCI compliance up to date.

## Enabling raw card acceptance with payment processors <a href="#docs-internal-guid-959e0903-7fff-fc13-1542-001b2640a715" id="docs-internal-guid-959e0903-7fff-fc13-1542-001b2640a715"></a>

While you are using Hyperswitch, your customers' cards will be securely tokenized and stored on Hyperswitch Cloud vault.&#x20;

However this will require the payment processors to enable raw card acceptance at their end (which most payment processor do not offer as default setting). You will have to send Hyperswitch PCI AOC to your payment processor's support team and request to enable the setting against your merchant account.

{% hint style="info" %}
Please drop a note to `biz@hyperswitch.io` to get access to the Hyperswitch PCI AOC (applicable only for Hyperswitch Cloud users)
{% endhint %}

If you are planning to use Hyperswitch Open Source, please [refer here](../hyperswitch-open-source/going-live/pci-compliance/) for more notes about ensuring PCI compliance when you self deploy Hyperswitch
