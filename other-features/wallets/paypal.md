---
description: Setup PayPal on your application
icon: paypal
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/kf7BGdsPkCw9nalhAIlE/other-features/wallets/paypal
---

# PayPal

PayPal is a digital wallet that lets customers load balance onto the wallet and as well as save their cards for quicker one-touch checkout. PayPal currently supports 200+ markets and 25+ currencies.

### **How to configure PayPal on Juspay Hyperswitch?**

Since PayPal is both a payment method (wallet) as well as a payment processor, Hyperswitch gives you the flexibility to configure PayPal through multiple avenues.

### **PayPal native SDK experience:**

1. Before testing the PayPal SDK integration, ensure that you have enabled PayPal on your Braintree account. Go to [https://sandbox.braintreegateway.com/](https://sandbox.braintreegateway.com/).
2. Select the settings icon on the top right.
3. Select Processing and enable the PayPal option.

Currently, Hyperswitch supports Braintree's [Vault](https://developer.paypal.com/braintree/docs/guides/paypal/overview) flow for PayPal as it offers seamless storing of payment methods for later use across Web, iOS and Android devices. The returning customers will be able to pay through PayPal with one-touch experience without logging in again after saving their card the first time.

### **PayPal Redirection experience**

Configuring PayPal through other payment processors like Adyen, Checkout, etc on Hyperswitch will redirect the customers to PayPal's website to complete the payment. For this approach, you just have to make sure that you enable PayPal on your respective processors' dashboards and also, enable PayPal while configuring these processors on your Hyperswitch dashboard.
