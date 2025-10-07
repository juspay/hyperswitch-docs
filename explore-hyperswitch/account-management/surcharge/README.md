---
description: Configure advanced rules with various payment parameters
icon: clipboard-list-check
---

# Surcharge

Hyperswitch Surcharge feature allows the merchant to configure advanced rules using various payment parameters such as amount, currency etc., to apply surcharges to payments.

## What is Surcharge?

A surcharge, sometimes called a checkout fee or service fee, is an additional fee that merchants can impose onto a customer’s bill to cover the costs of credit card or other payment method processing. Each time a business accepts a credit card or online payment, they pay a small fee (either a percentage or a fixed rate) to various entities, including the card brand (Visa, Mastercard, American Express, etc.), issuers (Klarna, Paypal, Affirm, etc) and the payment processor. Usually, merchants absorb this expense. But with a surcharge program, customers pay for the convenience of using their credit card or other payment methods.

## How does it work?



<figure><img src="../../../.gitbook/assets/Surcharge.drawio (1).svg" alt=""><figcaption></figcaption></figure>

Hyperswitch supports surcharge for most payment processors and you can configure surcharge through two ways:

**i) Sending the Surcharge details during payments/create request**

Surcharge can be applied to a payment using `surcharge_details` field in [payments/create API request](https://api-reference.hyperswitch.io/api-reference/payments/payments--create)

**ii) Configuring Surcharge rules using Hyperswitch Control Center**&#x20;

* The Surcharge Manager on the Hyperswitch Control Center allows you to configure advanced rules based on payment parameters to decide when and how much surcharge to apply to the payment
* Surcharge Decision Manager supports rules based on various payment parameters like payment\_amount, payment\_method, card\_network etc. Follow this [setup guide](surcharge-setup-guide.md) to configure rules using the Surcharge Decision Manager
* For example, if you want to apply 5% surcharge for all payments of value greater than $100 then you could setup the following rule on the Surcharge Manager and all the payment requests conforming to that rule would have sucharge of 5% of the original amount being applied to it. ie, If payment amount is 1000$, 1050$ will be sent as authorization amount to the payment processor.&#x20;

<figure><img src="../../../.gitbook/assets/Screenshot 2024-07-01 at 11.52.18 AM.png" alt=""><figcaption></figcaption></figure>

## Next step&#x20;

To test the Surcharge Manager, after activating the rule, we can make a Test Payment using the [Hyperswitch Dashboard ](https://app.hyperswitch.io/sdk)

{% content-ref url="../../../hyperswitch-open-source/account-setup/test-a-payment.md" %}
[test-a-payment.md](../../../hyperswitch-open-source/account-setup/test-a-payment.md)
{% endcontent-ref %}
