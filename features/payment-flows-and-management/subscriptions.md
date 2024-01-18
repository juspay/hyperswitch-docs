---
description: >-
  Augments payment processing capabilities with your preferred Subscription
  Solution provider
---

# 🔁 Subscriptions

{% hint style="info" %}
In this section we will cover how you can leverage the benefits of Hyperswitch for payments processing while managing subscriptions with your preferred Subscription Solution Provider
{% endhint %}

### Benefits

Hyperswitch allows you to work with your preferred subscription provider while having the flexibility to connect with multiple payment processors and payment methods. The benefits you get with using Hyperswitch integration as a supplement with your Subscription Solution Provider are as follows:

* Flexibility to work with any payment processor of your choice based on better costs or auth rates
* Expand to local payment methods across global markets
* Smart route recurring payments across multiple payment processors to improve the success rate ([part of Q1 roadmap](https://docs.hyperswitch.io/about-hyperswitch/roadmap))
* Unified solution to manage one-time payments use cases (e-commerce use case) and recurring payments use cases (subscription payments)

### What subscription providers do we support?

All major Subscription Solution Providers offer integration points to manage payments with external payment processors. And the integration solution proposed below should work universal across any subscription provider.

In case of queries, or if you need a specific payment method of payment processor integration - please drop an email to biz@hyperswitch.io

### Use cases supported

* User flow 1 - User selects a plan followed by selecting the payment method and adding the payment method details to make the payment and start subscription.&#x20;
* User flow 2 -  User selects a payment method and adds the payment method details which are saved. User finally selects the plan to start the subscription
* Use cases common to both user flows
  * Subscription management portal
  * Subscription payment retries&#x20;
  * Subscription reminder emails

#### User flow-1&#x20;

User selects a plan followed by selecting the payment method and adding the payment method details to start subscription. This flow can be broken into 5 parts

* Integration and set up - Merchants will setup their account and generate API keys with the subscription provider and Hyperswitch as well as integrate with both of them. Merchants will set up their plans with the subscription provider and set up their payment providers with Hyperswitch.
* Retrieve plans and create subscription - Merchants will retrieve the eligible plans and display them on their website. The customer will select one of the plans shown to them. Merchant will use the selected plan to create a customer and a subscription with the subscription provider. &#x20;
* Collect payment method details - Once the subscription is created and the key fields are received by the merchant, they'll initiate a Payments create call with Hyperswitch and load the payment SDK on their website ([more on SDK integration](https://docs.hyperswitch.io/hyperswitch-cloud/integration-guide)) to collect payment details from the customer&#x20;
* Make payment and return invoice - Using the payment details entered by the user the merchant will make a payment with Hyperswitch and create a mandate ([more details](https://docs.hyperswitch.io/features/payment-flows-and-management/mandates-and-recurring-payments)). The subscription is marked as active upon successful payment and the invoice with the customer.
  * In case the subscription start date is in future and the customer need not be charged immediately then the merchant should initiate a $0 mandate with Hyperswitch ([more details](https://docs.hyperswitch.io/features/payment-flows-and-management/zero-amount-authorization)).  &#x20;
* Make MIT transactions - The subscription provider will trigger a webhook to the merchant on the date of the scheduled payment for subscription. Upon receiving the webhook, the merchant should initiate a payment with Hyperswitch using the customer ID and mandate ID. The merchant will share the invoice with the customer upon successful payment

<figure><img src="../../.gitbook/assets/image (110).png" alt=""><figcaption></figcaption></figure>

#### User flow-2

User selects a payment method and adds the payment method details which are saved. User finally selects the plan to start the subscription. This flow can be broken into 5 parts

* Integration and set up - Merchants will setup their account and generate API keys with the subscription provider and Hyperswitch as well as integrate with both of them. Merchants will set up their plans with the subscription provider and set up their payment providers with Hyperswitch. &#x20;
* Collect and store payment method details - Merchant will initiate a Payments create call with Hyperswitch and load the payment SDK on their website ([more on SDK integration](https://docs.hyperswitch.io/hyperswitch-cloud/integration-guide)) to collect payment details from the customer.
  * Merchant will create a customer with the subscription provider
  * Merchant will initiate a $0 mandate with Hyperswitch ([more details](https://docs.hyperswitch.io/features/payment-flows-and-management/zero-amount-authorization)) to validate and store the payment details and create a mandate with Hyperswitch (using the same customer ID).  &#x20;
* Retrieve plans and create subscription - Merchants will retrieve the eligible plans and display them on their website. The customer will select one of the plans shown to them. Merchant will use the selected plan to create a subscription with the subscription provider.
* Make payment and return invoice - Using the mandate ID created earlier the merchant will make a payment with Hyperswitch. The subscription is marked as active upon successful payment and the invoice with the customer.
  * In case the subscription start date is in future and the customer need not be charged immediately then no payment is inittaed with Hyperswitch
* Make MIT transactions - The subscription provider will trigger a webhook to the merchant on the date of the scheduled payment for subscription. Upon receiving the webhook, the merchant should initiate a payment with Hyperswitch using the customer ID and mandate ID. The merchant will share the invoice with the customer upon successful payment

<figure><img src="../../.gitbook/assets/image (113).png" alt=""><figcaption></figcaption></figure>

#### Subscription management portal

The customer-facing subscription management interface allows the customers to modify their billing address, add new payment method details for subscripotion payments and cancel subscription. If a merchant offers a subscription management portal then here's how Hyperswitch can support:

* User updates billing address  - The merchant will update the new billing address with both Hyperswitch and the subscription provider using the customer ID.
* User updates payment method details -  The merchant will load Hyperswitch SDK to allow the user to select the payment method and add the relevant payment method details. Merchant will validate and add this payment method with Hyperswitch using $0 mandate and create a new mandate.
* User cancels subscriptions - The merchant will revoke the mandate with Hyperswitch post which they will cancel the subscription with the subscription provider.

<figure><img src="../../.gitbook/assets/image (111).png" alt=""><figcaption></figcaption></figure>

#### Subscription payment retries&#x20;

The payment made for subscriptions can fail&#x20;

* When customer is present in the flow - The user will retry the payment using same or different payment method
* When customer is not present in the flow - Once the merchant receives payment failed notification from Hyperswitch, they need to update the same with their subscription provider. All subscription providers have their own retry logics (default or configured by the merchant). Their retry logic will then send retry payment webhooks to the merchant. The merchant needs to consume the webhook and retrigger the payment with Hyperswitch ([more details](subscriptions.md#what-subscription-use-cases-do-we-support))&#x20;

#### Subscription reminder emails

The merchant can use the Hyperswitch Payment links when sending email reminders to customers who failed to make their subscription payments. Here's how it'll work:

* The send email notification is a functionality offered by most subscription providers. They also allow customising the message and payment links shared inside the email
* &#x20;The merchant needs to host a standard page and share the link to that page on the email
* When the customer click on that link requesting to pay, the merchant will call Hyperswitch with the customer ID to create and share the Payment link
* The customer is redirected to the payment link hosted page (with a validity of 15-mins) which allows them to make the payment using any payment option
* Once the payment is successful, the merchant should mark the invoice as paid with their subscription provider and return the invoice to the customer

<figure><img src="../../.gitbook/assets/image (112).png" alt=""><figcaption></figcaption></figure>

### FAQ

<details>

<summary>Can I bring in my own subscription provider ? </summary>

Yes, we support any subscription provider using the above framework.

</details>

<details>

<summary>Can I process both one-time payments and recurring payments via the same setup?</summary>

Yes, once you're integrated with Hyperswitch, you'll be able to process both one-time payments and recurring payments.

</details>

