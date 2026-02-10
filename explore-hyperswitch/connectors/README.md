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

> Browse the complete list of live integrations here: [**Hyperswitch Integrations Directory →**](https://juspay.io/integrations)

### Why multiple processors?

As your business grows faster, there would be a need to expand payment offerings with more payment processors. This need might arise due to multiple reasons:

* Reducing dependency on a single processor and reducing vendor lock-in
* Introducing a challenger processor for better cost and auth rates
* Launching a business in new geography with a local payment processor
* Offering local or new payment methods for your customers
* Reducing technical downtimes and improving success rates with a fallback

Integrating and maintaining multiple payment processors and their different versions is a time and resource intensive process. Hyperswitch can add a new PSP in [2 weeks](https://hyperswitch.io/blog/part-1-5-payment-challenges-for-vertical-saas-businesses) allowing you to focus on you core business activities.

### Adding a connector

Most connector integrations follow a simple click-and-connect flow on Hyperswitch using your connector credentials. However, some connectors may require additional setup details as required on the control center. The standard setup steps are as follows :

1. You need to be registered with PSP in order to proceed. In case you aren't, you can quickly setup your account by signing up on their dashboard.
2. You should have registered on [Hyperswitch Control center](https://hyperswitch.io/contact-sales).
3. Add the PSP authentication credentials from their dashboard into the Hyperswitch Control center. These authentication credentials vary across different PSPs. Few samples authentication combinations are shared below :
   1. Authorizedotnet - API Login ID and Transaction Key
   2. Adyen - API key and Account ID
   3. Braintree - Merchant ID, Public key and Private key
   4. Airwallex API key and Client ID
   5. Fiserv - API Key, API Secret, Merchant ID and Terminal ID
   6. Paypal - Client Secret and Client ID

* Choose the payment methods you want to utilize with Authorize.net by navigating to the next screen on Hyperswitch.
* Enable the PSP once you're done.
* Complete list of Hyperswitch integrations can be found here - [https://juspay.io/integrations](https://juspay.io/integrations)

### Connector types

Hyperswitch supports a wide variety of connectors like -&#x20;

* Payment Processors, Acquirers & APMs&#x20;
* Payment platforms
* Payouts Processors
* Subscription Providers
* Card vaults ([read more](https://docs.hyperswitch.io/~/revisions/X2JziUYSPA0p9yrv2keP/explore-hyperswitch/workflows/vault))
* 3DS authentications ([read more](https://docs.hyperswitch.io/~/revisions/X2JziUYSPA0p9yrv2keP/explore-hyperswitch/workflows/3ds-decision-manager))
* Fraud management ([read more](https://docs.hyperswitch.io/~/revisions/X2JziUYSPA0p9yrv2keP/explore-hyperswitch/workflows/fraud-and-risk-management))

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden></th><th data-hidden data-card-target data-type="content-ref"></th><th data-hidden data-card-cover data-type="files"></th></tr></thead><tbody><tr><td><mark style="color:blue;"><strong>Activate connector on Hyperswitch</strong></mark></td><td>A detailed guide on how to configure a connector along with payment methods in a few steps</td><td></td><td><a href="activate-connector-on-hyperswitch/">activate-connector-on-hyperswitch</a></td><td></td></tr><tr><td><mark style="color:blue;"><strong>List of available connectors and payment methods</strong></mark></td><td>Learn more about all the available connectors and payments methods on Hyperswitch</td><td></td><td><a href="https://integrations.hyperswitch.io/">https://integrations.hyperswitch.io/</a></td><td></td></tr><tr><td><mark style="color:blue;"><strong>Raise a request for a new connector or payment method integration</strong></mark></td><td>Don't see payment processor of your choice? Raise a integration request, we will be happy to help!</td><td></td><td><a href="https://hyperswitch-io.slack.com/ssb/redirect">https://hyperswitch-io.slack.com/ssb/redirect</a></td><td></td></tr></tbody></table>

{% content-ref url="activate-connector-on-hyperswitch/" %}
[activate-connector-on-hyperswitch](activate-connector-on-hyperswitch/)
{% endcontent-ref %}

{% hint style="info" %}
**Have Questions?**\
Join our [Slack Community](https://join.slack.com/t/hyperswitch-io/shared_invite/zt-2jqxmpsbm-WXUENx022HjNEy~Ark7Orw) to ask questions, share feedback, and collaborate.\
Prefer direct support? Use our [Contact Us](https://hyperswitch.io/contact-us) page to reach out.
{% endhint %}
