---
description: >-
  Integrate with more than 200+ Connectors enabling 150+ payment methods with
  zero development effort.
icon: plug
---

# Connectors Integration

### Overview

Connectors are integrations that allow Hyperswitch to talk to external payment services such as PSPs, Acquirers, APMs, Card vaults, 3DS authentications, Fraud management, Subscription, Payouts and more. They act as bridges between your Hyperswitch setup and the third-party services that move or manage money for your business.

Every provider has its own APIs, authentication methods, and feature sets. Hyperswitch standardizes these differences through connectors, exposing a single unified Payments API.\
This means you can add, switch, or remove processors without rewriting your code, just plug in credentials and start transacting.

Connectors form the foundation of Hyperswitch's **payment orchestration layer**, enabling you to manage payments, routing, 3DS authentication, fraud checks, and payouts through a single interface.

> Browse the complete list of live integrations here: [**Hyperswitch Integrations Directory →**](https://integrations.hyperswitch.io/)

### Why multiple processors?

As your business grows faster, there would be a need to expand payment offerings with more payment processors. This need might arise due to multiple reasons:

* Reducing dependency on a single processor and reducing vendor lock-in
* Introducing a challenger processor for better cost and auth rates
* Launching a business in new geography with a local payment processor
* Offering local or new payment methods for your customers
* Reducing technical downtimes and improving success rates with a fallback&#x20;

Integrating and maintaining multiple payment processors and their different versions is a time and resource intensive process. Hyperswitch can add a new PSP in [2-4 weeks](https://hyperswitch.io/blog/part-1-5-payment-challenges-for-vertical-saas-businesses)  allowing you to focus on you  core business activities.

### Adding a connector

Most connector integrations follow a simple click-and-connect flow on Hyperswitch using your connector credentials. However, some connectors may require additional setup details as required on the control center. The standard setup steps are as follows :&#x20;

1. You need to be registered with PSP in order to proceed. In case you aren't, you can quickly setup your  account by signing up on their dashboard.
2. You should have registered on [Hyperswitch Control center](https://hyperswitch.io/contact-sales).
3. Add the PSP authentication credentials from their dashboard into the Hyperswitch Control center. These authentication credentials vary across different PSPs. Few samples authentication combinations are shared below :
   1. Authorizedotnet -  API Login ID and Transaction Key
   2. Adyen - API key and Account ID
   3. Braintree - Merchant ID, Public key and Private key
   4. Airwallex API key and Client ID&#x20;
   5. Fiserv - API Key, API Secret, Merchant ID and Terminal ID
   6. Paypal - Client Secret and Client ID&#x20;

* Choose the payment methods you want to utilize with Authorize.net by navigating to the next screen on Hyperswitch.&#x20;
* Enable the PSP once you're done.
* Complete list of Hyperswitch integrations can be found here - [https://integrations.hyperswitch.io/](https://integrations.hyperswitch.io/)

### Connector types

Hyperswitch supports a wide variety of connectors like - PSPs, Acquirers, APMs, Card vaults, 3DS authentications, Fraud management, Subscription, Payouts and more. In the below sections we'll primarily cover payment connectors - PSPs and Acquirers and the related flows.

Hyperswitch supports a wide range of parameters through the **Payments Create API** for the underlying payment connectors it integrates with. The diagram below illustrates the various parameters and flows supported as part of a typical payment connector integration



1. **Parameters flows supported for cards -** Hyperswitch enables multiple card payment flow configurations, designed to support a wide range of industry-specific use cases.

<figure><img src="../../.gitbook/assets/Juspay hyperswitch - Architecture deepdive (6).png" alt=""><figcaption></figcaption></figure>

2. **Parameters supported for cards -** Hyperswitch supports an extensive set of card-specific parameters through the Payments API. These parameters ensure flexibility across multiple regions, issuers, and use cases, from retail to subscription billing. Merchants can easily configure and pass these parameters to optimize for conversion, compliance, and cost efficiency.

<figure><img src="../../.gitbook/assets/Juspay hyperswitch - Architecture deepdive (5).png" alt=""><figcaption></figcaption></figure>

3. **Parameters supported for wallets -** Hyperswitch provides comprehensive wallet integration parameters that streamline setup and transaction management across leading digital wallets.\
   It supports key attributes such as tokenization, wallet identifiers, and more. This ensures a seamless checkout experience while allowing merchant to maintaining the right control.

<figure><img src="../../.gitbook/assets/Juspay hyperswitch - Architecture deepdive (4).png" alt=""><figcaption></figcaption></figure>

4. **Parameters supported for Refunds, Disputes and Errors -** Hyperswitch offers structured support for **refunds, disputes, and error handling**, ensuring transparency and control throughout the payment lifecycle. Merchants can track, respond, and reconcile outcomes across multiple PSPs from a unified interface. Detailed error codes and dispute attributes enable faster resolution and automated workflow orchestration.

<figure><img src="../../.gitbook/assets/Juspay hyperswitch - Architecture deepdive (8).png" alt=""><figcaption></figcaption></figure>

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden></th><th data-hidden data-card-target data-type="content-ref"></th><th data-hidden data-card-cover data-type="files"></th></tr></thead><tbody><tr><td><mark style="color:blue;"><strong>Activate connector on Hyperswitch</strong></mark></td><td><p></p><p>A detailed guide on how to configure a connector along with payment methods in a few steps </p></td><td></td><td><a href="activate-connector-on-hyperswitch.md">activate-connector-on-hyperswitch.md</a></td><td></td></tr><tr><td><mark style="color:blue;"><strong>List of available connectors and payment methods</strong></mark></td><td>Learn more about all the available connectors and payments methods on Hyperswitch</td><td></td><td><a href="https://integrations.hyperswitch.io/">https://integrations.hyperswitch.io/</a></td><td></td></tr><tr><td><mark style="color:blue;"><strong>Raise a request for a new connector or payment method integration</strong></mark></td><td>Don't see payment processor of your choice? Raise a integration request, we will be happy to help!</td><td></td><td><a href="https://hyperswitch-io.slack.com/ssb/redirect">https://hyperswitch-io.slack.com/ssb/redirect</a></td><td></td></tr></tbody></table>

{% content-ref url="activate-connector-on-hyperswitch.md" %}
[activate-connector-on-hyperswitch.md](activate-connector-on-hyperswitch.md)
{% endcontent-ref %}

{% hint style="info" %}
**Have Questions?**\
Join our [Slack Community](https://join.slack.com/t/hyperswitch-io/shared_invite/zt-2jqxmpsbm-WXUENx022HjNEy~Ark7Orw) to ask questions, share feedback, and collaborate.\
Prefer direct support? Use our [Contact Us](https://hyperswitch.io/contact-us) page to reach out.
{% endhint %}
