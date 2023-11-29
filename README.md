---
description: The complete guide to setting up and managing your own payments switch
cover: .gitbook/assets/Frame.png
coverY: -1.5791666666666666
layout:
  cover:
    visible: true
    size: full
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
---

# 👋 Intro to Hyperswitch

{% hint style="info" %}
Note that we are still moving things around and adding new sections to this document, please expect changes as you navigate and integrate Hyperswitch
{% endhint %}

## Hyperswitch and the payments ecosystem

Hyperswitch is a unified API to connect with dozens of different payment processors, each with very different internal APIs and SDKs. In other words, our payment switch is a set of payments domain abstractions, built over the capabilities of leading payment processors, wallets, Buy Now Pay Later (BNPL) providers and banks.

Hyperswitch can simplify your payment integrations and allow you to take full control of your payments.

Using Hyperswitch, you can:

* ⬇️ **Reduce dependency** on a single processor like Stripe or Braintree
* 🧑‍💻 **Reduce Dev effort** to add & maintain integrations by 90%&#x20;
* 🚀 **Improve success rates** with seamless failover and auto-retries
* 💸 **Reduce processing fees** with smart routing
* 🎨 **Customize payment flows** with full visibility and control
* 🌐 **Increase business reach** with local/alternate payment methods

The current payment landscape is extremely diverse, with 500+ payment processors, 200+ wallets, 130+ bank transfer options, local payment solutions and so on. Over the years, this has increased the number of fintech layers, resulting in more latency and cost associated with each transaction. In addition to this, connecting and maintaining multiple payment integrations requires a lot of development effort.

The payment ecosystem is:

* Dominated by closed systems and walled gardens
* Ever increasing diversity
* Becoming expensive for businesses

These problems can only be solved by open systems and this is what Hyperswitch is all about:

> A community led, open payments switch to enable access to the best payments infrastructure for every digital business.

## What to expect

### An infrastructure solution that's super lightweight and scalable

Hyperswitch is optimized for sub 30 ms application overhead (and getting better) and falls within 5% of the payment processor's latency. The application can absorb any shock resulting from unusual traffic spikes and uses a distributed key-value store for high frequency write operations

<figure><img src=".gitbook/assets/latency.png" alt="" width="563"><figcaption></figcaption></figure>

### One click cloud deployment

Hyperswitch supports one-click kubernetes deployment through CDK scripts. The deployment includes an app server, a control center and a web client

<figure><img src=".gitbook/assets/oss.png" alt="" width="563"><figcaption></figcaption></figure>

### Full visibility and control

You can monitor system health by exporting your AWS Cloudwatch metrics to Grafana and stream application logs from Hyperswitch to Loki/Kibana for storing and viewing logs

<figure><img src=".gitbook/assets/logs.gif" alt="" width="563"><figcaption></figcaption></figure>

### Simplified payment operations

Hyperswitch provides a control center to handle all your payment operations like adding payment processors, managing payment routing and viewing analytics

<figure><img src=".gitbook/assets/dashboard.gif" alt="" width="563"><figcaption></figcaption></figure>

### Mobile responsive & PCI Compliant Web Checkout

Finally, you can self-host your own PCI compliant web checkout and integrate it with your web app. Our web client is highly customizable and blends right in with your web app\


<figure><img src=".gitbook/assets/sdk.png" alt="" width="563"><figcaption></figcaption></figure>

## Join the movement

It doesn’t matter if you don’t come from a technical or a payments background (though it’s okay if you do too!) We made this guide to make Payments Infrastructure accessible to as many people as possible. The only prerequisite is that you know how to use a few dev tools and know some basic coding.

A Payments Switch allows you to connect with any Payment processing entity and enable any payment method without having to repeat the development or design effort multiple times. This can be achieved by a single integration with Hyperswitch. A lot of people have a misconception that you need to master all kinds of hard-to-get stuff to drive payment or even understand it.  But as you’ll see, those people are wrong. Here are a few things you _absolutely don’t need_ to run your own payments stack:

| Myth                     | Truth                                                                                                                            |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------- |
| Lots of Compliance needs | Just a self assessment for PCI compliance if you process less than 6 million transactions a year. 1-month long process otherwise |
| Lots of complexity       | A single dashboard to view and review all your payment metrics                                                                   |
| Lots of Expense          | Flexibility to work with any payment processor to get best prices and cut down of multiple layers in between                     |

We are a small community of payment infrastructure enthusiasts that believe that payments should be a basic utility like water or electricity. We launched in Jan '2023 and we have released successive versions of the product, offering a feature-rich payments solution.

Our Parent entity, Juspay, is South-Asia's largest payment experience and Orchestration provider, processing more than 70 Million transactions every day. Launched in 2012, Juspay works with some of the largest enterprises and banks like Amazon, Google, Flipkart, HDFC to name a few.

<figure><img src=".gitbook/assets/Screenshot 2023-10-26 at 4.30.06 PM.png" alt=""><figcaption></figcaption></figure>
