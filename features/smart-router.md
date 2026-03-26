---
description: Configure intelligent payment routing rules to optimize authorization rates and processing costs
---

# Smart Router

{% hint style="info" %}
With this section, understand how the Hyperswitch Smart Router works to improve your conversion rates and reduce processing costs by intelligently routing payments across various processors.
{% endhint %}

{% embed url="https://hyperswitch.io/video/edit_conf.mp4" %}

## Prerequisites

To get started with Smart Router, ensure to have one or more payment processors integrated. You can integrate the payment processor of your choice on the Control Center by following the [Connector Integration](../hyperswitch-cloud/connectors/) guide.

## What is Smart Payment Routing?

Selling globally or otherwise invariably brings in a requirement to adopt multiple payment processors to cater to a wide range of payment method needs of the customers and gives you the flexibility to switch between processors to manage down-time and optimize your payment processing costs. Your business can choose the most optimal payment processors for every payment based on the cost, region, and customer.

Hence, Hyperswitch's Smart Router is designed as a no-code tool to provide complete control and transparency in creating and modifying payment routing rules. Hyperswitch supports the following formats of Smart Routing:

**Volume Based Configuration:** Define volume distribution among multiple payment processors using percentages.

**Rule Based Configuration:** More granular control which allows defining custom routing logic based on different parameters of payment.

**Default Fallback Routing:** If the active routing rules are not applicable, the priority order of all configured payment processors is used to route payments. This priority order is configurable from the Dashboard.

**Cost Based Configuration** (submit a feature request [here](https://github.com/juspay/hyperswitch/discussions/new?category=ideas-feature-requests))**:** Automatically routes transactions to the payment processor charging the lowest merchant discount rate (MDR) for the opted payment method.

## How Does the Smart Router Work?

Hyperswitch Smart Router Engine evaluates every payment request against your predefined routing logic and makes a decision on the best payment processor for the payment, and executes the transaction. If the payment fails or if the payment processor is down, the payment is automatically retried through a different processor.

<figure><img src="../.gitbook/assets/Smart Routing Flow.drawio.png" alt=""><figcaption><p>Hyperswitch Smart Router Flow</p></figcaption></figure>

## How to Configure the Smart Router?

[Hyperswitch dashboard](https://app.hyperswitch.io/routing) provides a simple, intuitive UI to configure multiple routing rules on your dashboard under the **Routing** tab. There are three routing rule formats that Hyperswitch currently supports.



<table data-view="cards"><thead><tr><th></th><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th><th data-hidden data-card-cover data-type="files"></th></tr></thead><tbody><tr><td><strong>Rule Based Routing</strong></td><td></td><td></td><td><a href="merchant-controls/smart-router/rule-based-routing.md">rule-based-routing.md</a></td><td><a href="../.gitbook/assets/rule-based.png">rule-based.png</a></td></tr><tr><td><strong>Volume Based Routing</strong></td><td></td><td></td><td><a href="merchant-controls/smart-router/volume-based-routing.md">volume-based-routing.md</a></td><td><a href="../.gitbook/assets/volume-based.png">volume-based.png</a></td></tr><tr><td><strong>Default Fallback Routing</strong></td><td></td><td></td><td><a href="merchant-controls/smart-router/default-fallback-routing.md">default-fallback-routing.md</a></td><td><a href="../.gitbook/assets/default.png">default.png</a></td></tr></tbody></table>

## Next Step

To test the Smart Router, after activating one rule, you can make a test payment using the [Hyperswitch Dashboard](https://app.hyperswitch.io/sdk).

{% content-ref url="../hyperswitch-open-source/testing/test-a-payment.md" %}
[test-a-payment.md](../hyperswitch-open-source/testing/test-a-payment.md)
{% endcontent-ref %}

<details>

<summary>FAQs</summary>

### What Parameters Can I Use to Configure Routing Rules?

The rule-based routing supports setting up advanced rule configuration based on all critical payments parameters such as Payment Method, Payment Method Type, Country, Currency, Amount, and more.

### Why Did My Payment Go Through One Connector Even Though I Specified Another?

There can be multiple reasons why this happened, but all of them can be boiled down to a "connector eligibility failure" for a given payment. We will walk through a common scenario to examine what this really means.

* Imagine that you configured two connectors for your account. Say Stripe, then Adyen, in that order. Since you configured them in that order, your default fallback looks like this: `[Stripe, Adyen]` (connectors are appended to the end of your default fallback list when configured for the first time)
* In your connectors dashboard, you enable Cards for Stripe, and Apple Pay for Adyen.
* Now you create a new Volume-based routing configuration, and you configure it to route 100% of your traffic through Stripe for now.
* Now you go ahead and open up the Hyperswitch SDK to make a test payment. In the payment method selection area, you can see two buttons, one for Cards and one for Apple Pay.
  * This is where you run into your first question: "Why is it showing me Apple Pay even though I have configured 100% of my payments to go through Stripe, and Apple Pay is not enabled for Stripe?"
  * The answer to this is: the payment methods that are shown to the customer in the SDK are not conscious of your routing configuration. We prioritize giving your customers the complete spread of all enabled payment methods across all of your enabled connectors. Therefore, if you specifically do not wish for Apple Pay to appear on your checkout screen, you need to disable it in Adyen here, even though your routing configuration makes no mention of Adyen.
* Now you select Apple Pay, go through the required steps, confirm the payment, and it succeeds. You go to your payments dashboard and see that the payment went through Adyen.
  * This is where you run into the second question: "Why is the payment going through Adyen even though I have set my routing configuration to route 100% of my payments through Stripe?"
  * The answer to this carries over from the previous point. Since we displayed Apple Pay on the checkout screen even though it was not enabled for your preferred connector Stripe, we need to adhere to your connector payment method configuration and ensure the payment goes through the right connector, here, Adyen since Apple Pay is only enabled for Adyen. To briefly explain how Hyperswitch reaches this conclusion:
    * Hyperswitch runs your configured routing algorithm. Since this is 100% Stripe, Hyperswitch receives Stripe as the output.
    * Hyperswitch then runs an eligibility analysis on the output (Stripe) to gauge its eligibility for the current payment. The eligibility analysis fails once Hyperswitch realizes that the payment is made through Apple Pay which is not enabled for Stripe.
    * The application then goes into fallback mode and loads your default fallback, which is `[Stripe, Adyen]` as seen earlier.
    * The application looks through the list in order. It ignores Stripe since it has already failed the eligibility analysis. It instead subjects Adyen (the next connector in the list) to the same eligibility analysis.
    * This time the analysis passes since Apple Pay is enabled for Adyen.
    * Hyperswitch takes Adyen as the final connector to make the payment through even though your configuration says 100% Stripe.
  * This fallback flow is taken when none of the connectors in the output of routing are eligible for the payment. This is done in an effort to maximize the success rate of the payment even if it means deviating from the currently active routing configuration.

</details>
