---
description: Infinite control over managing your payments
---

# 🛣️ Smart Router

{% hint style="info" %}
With this section, understand how the Hyperswitch Smart Router works to improve your conversion rates and reduces processing costs by intelligently routing payments across various processors
{% endhint %}

{% embed url="https://hyperswitch.io/video/edit_conf.mp4" %}

## Prerequisites

To get started with Smart Router, ensure to have one or more payment processors integrated. You can integrate the payment processor of your choice on the Control Center by following the [Connector Integration](../hyperswitch-cloud/connectors/) guide.

## What is smart payment routing?

Selling globally or otherwise invariably brings in a requirement to adopt multiple payment processors to cater to a wide range of payment method needs of the customers and gives you the flexibility to switch between processors to manage down-time and , it could be vital to optimising your payment processing costs as your business can choose the most optimal payment processors for every payment based on the cost, region and customer.

Hence, Hyperswitch’s smart router is designed as a no-code tool to provide complete control and transparency in creating and modifying payment routing rules. Hyperswitch supports below formats of Smart Routing.

**Volume Based Configuration:** Define volume distribution among multiple payment processors using percentages.

**Rule Based Configuration:** More granular control which allows to define custom routing logics based on different parameters of payment.

**Default Fallback Routing :** If the active routing rules are not applicable, the priority order of all configured payment processors is used to route payments. This priority order is configurable from the Dashboard.

**Cost Based Configuration** (submit a feature request [here](https://github.com/juspay/hyperswitch/discussions/new?category=ideas-feature-requests))**:** Automatically routes transaction to the payment processor charging the least MDR (merchant discount rate) for the opted payment method.

## How does the Smart Router work?

Hyperswitch Smart Router Engine evaluates every payment request against your predefined routing logic and makes a decision on the best payment processor for the payment, and executes the transaction. If the payment fails or if the payment processor is down, the payment is automatically retried through a different processor.

<figure><img src="../.gitbook/assets/Smart Routing Flow.drawio.png" alt=""><figcaption><p>Hyperswitch Smart Router Flow</p></figcaption></figure>

## How to configure the Smart Router?

[Hyperswitch dashboard](https://app.hyperswitch.io/routing) provides a simple, intuitive UI to configure multiple Routing rules on your dashboard under the **Routing** tab. There are three routing rule formats that Hyperswitch currently supports.\
\


<table data-view="cards"><thead><tr><th></th><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th><th data-hidden data-card-cover data-type="files"></th></tr></thead><tbody><tr><td><strong>Rule Based Routing</strong></td><td></td><td></td><td><a href="merchant-controls/smart-router/rule-based-routing.md">rule-based-routing.md</a></td><td><a href="../.gitbook/assets/rule-based.png">rule-based.png</a></td></tr><tr><td><strong>Volume Based Routing</strong></td><td></td><td></td><td><a href="merchant-controls/smart-router/volume-based-routing.md">volume-based-routing.md</a></td><td><a href="../.gitbook/assets/volume-based.png">volume-based.png</a></td></tr><tr><td><strong>Default Fallback Routing</strong></td><td></td><td></td><td><a href="merchant-controls/smart-router/default-fallback-routing.md">default-fallback-routing.md</a></td><td><a href="../.gitbook/assets/default.png">default.png</a></td></tr></tbody></table>

## Next step&#x20;

To test the Smart Router, after activating one rule, we can make a Test Payment using the [Hyperswitch Dashboard ](https://app.hyperswitch.io/sdk)

{% content-ref url="../hyperswitch-open-source/testing/test-a-payment.md" %}
[test-a-payment.md](../hyperswitch-open-source/testing/test-a-payment.md)
{% endcontent-ref %}

<details>

<summary>FAQs</summary>

### 1. What parameters can I use to configure routing rules?

The rule-based routing supports setting up advanced rule configuration based on all critical /payments parameters such as Payment Method, Payment Method Type, Country, Currency, Amount etc.

### 2. Why did my payment go through 'Y' connector even though I have specified 'X' in my routing configuration? OR Why is it showing me 'Abc' payment method in SDK checkout even though I have not enabled it for the 'X' connector that I'm routing my payments through?

There can be multiple reasons why this happened but all of them can be boiled down to a "connector eligibility failure" for a given payment. We'll walk through a common scenario to examine what this really means.

* Imagine that you configured two connectors for your account. Say `Stripe`, then `Adyen`, in that order. Since you configured them in that order, your default fallback looks like this: `[Stripe, Adyen]` (connectors are appended to the end of your default fallback list when configured for the first time)
* In your connectors dashboard, you enable Cards for Stripe, and ApplePay for Adyen.
* Now you create a new Volume-based routing configuration, and you configure it to route 100% of your traffic through Stripe for now.
* Now you go ahead and open up the Hyperswitch SDK to make a test payment. In the payment method selection area, you can see two buttons, one for `Cards` and one for `ApplePay`.&#x20;
  * This is where you run into your first question. "Why is it showing me ApplePay even though I have configured 100% of my payments to go through Stripe, and ApplePay is not enabled for Stripe?"
  * The answer to this is, the payment methods that are shown to the customer in the SDK aren't conscious of your routing configuration. We prioritize giving your customers the complete spread of all enabled payment methods across all of your enabled connectors. Therefore, if you specifically do not wish for ApplePay to appear on your checkout screen, you need to disable it in `Adyen` here, even though your routing configuration makes no mention of Adyen.
* Now you select `ApplePay`, go through the required steps, confirm the payment, and it succeeds. You go to your payments dashboard and see that the payment went through `Adyen`.
  * This is where you run into the second question. "Why is the payment going through `Adyen` even though I have set my routing configuration to route 100% of my payments through `Stripe`?
  * The answer to this carries over from the previous point. Since we displayed `ApplePay` on the checkout screen even though it wasn't enabled for your preferred connector `Stripe`, we need to adhere to your connector payment method configuration and ensure the payment goes through the right connector, here, `Adyen` since `ApplePay` is only enabled for Adyen. To briefly explain how Hyperswitch reaches this conclusion :-
    * Hyperswitch runs your configured routing algorithm. Since this is `100% Stripe`, Hyperswitch receives `Stripe` as the outuput.
    * Hyperswitch then runs an Eligibility Analysis on the output (`Stripe`) to gauge its eligibility for the current payment. The Eligibility Analysis fails once Hyperswitch realizes that the payment is made through `ApplePay` which is not enabled for `Stripe`
    * The application then goes into fallback mode and loads your `default fallback`, which is `[Stripe, Adyen]` as seen earlier.
    * The application looks through the list in order. It ignores `Stripe` since it has already failed the Eligibility Analysis. It instead subjects `Adyen` (the next connector in the list) to the same Eligibility Analysis.
    * This time the analysis passes since `ApplePay` is enabled for `Adyen`.
    * Hyperswitch takes `Adyen` as the final connector to make the payment through even though your configuration says `100% Stripe`.
  * This fallback flow is taken when none of the connectors in the output of routing are eligible for the payment. This is done in an effort to maximize the success rate of the payment even if it means deviating from the currently active routing configuration.

</details>
