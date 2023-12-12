---
description: Accept debit and credit card payments on your application
---

# 💳 Cards

{% hint style="info" %}
This section gives you an overview of how to enable debit and credit cards on Hyperswitch along with how to configure the web client to securely save your customers' card details for future payments
{% endhint %}

![logo\_discord](https://hyperswitch.io/logos/logo\_diners.svg)![logo\_discord](https://hyperswitch.io/logos/logo\_visa.svg)![logo\_discord](https://hyperswitch.io/logos/logo\_mastercard.svg)![logo\_discord](https://hyperswitch.io/logos/logo\_amex.svg)

Hyperswitch supports credit and debit card payments through all our payment processor connectors**.** \
We accept cards from all major global and local card networks, such as Visa, Mastercard, American Express, Diners, Discover, JCB, Union Pay, etc. While Hyperswitch supports card payments in 135+ currencies and 150+ countries, each of these connectors and networks has limitations in terms of the number of countries and currencies they support.

Apart from regular one-time payments, Hyperswitch supports saving a card, recurring payments, and placing a hold for later capture.

## Integration Steps

1. Go to Hyperswitch dashboard and to connectors tab [here](https://app.hyperswitch.io/) and enable card.

## Saved Cards

You could use Hyperswitch’s PCI Compliant secure vault to safely store your customers’ card data and retrieve them when they return to pay on your website/app. In addition, our hyper SDK has a checkbox on the payment page that you can use to take customers’ consent to store their card data. To try out the save cards feature through API, include either of the values for the `setup_future_usage` field in your Payments API request body. This feature comes with [Unified Checkout](../integration-guide/web/).

The Saved cards feature comes out of the box without any additional integration steps. The Unified Checkout SDK will fetch the saved cards details and show them to your users. All you need to do is create a customer or send a customer id when you call the Payments API. The cards belonging to that customer ID are securely stored and retrived from the card vault.

Follow the below guide to learn how to make a saved card payment using Hyperswitch

{% content-ref url="../../features/payment-flows/tokenization-and-saved-cards.md" %}
[tokenization-and-saved-cards.md](../../features/payment-flows/tokenization-and-saved-cards.md)
{% endcontent-ref %}

## Recurring Payments - Mandate through cards

Hyperswitch supports the creation of mandates for card transactions through various payment processors to collect card information from the customer and authorize a mandate. The mandate can then be charged against at specific intervals and specific amounts based on the mandate setup.&#x20;

Follow the below guide to learn how to make a recurring payment with Hyperswitch

{% content-ref url="../../features/payment-flows/mandates-and-recurring-payments.md" %}
[mandates-and-recurring-payments.md](../../features/payment-flows/mandates-and-recurring-payments.md)
{% endcontent-ref %}

## Auth and Capture

By default, all payments are auto-captured during authorization in Hyperswitch, but you can choose to separate capture from authorization by manually capturing an authorized payment later. Setting the `capture` field in payments/confirm API to `manual` will block the stated amount on the customer’s card without charging them. To charge the customer an amount equal to or lesser than the blocked amount, use the payments/capture endpoint with the relevant details.
