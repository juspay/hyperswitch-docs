---
description: Get started with Hyperswitch in 4 easy steps
---

# ⚡ Quickstart

## Get your Hyperswitch API key

If you have not created a sandbox account, please create one

[Sign Up for Hyperswitch](https://app.hyperswitch.io/register)

If you have already created a sandbox account, your api key could be fetched from [settings section](https://app.hyperswitch.io/developers).

## Configure your payment processor

Configure the payment processor of your choice using [Connectors](https://app.hyperswitch.io/connectors) tab on our control center. You will need to have the API credentials of the payment processor readily available.

If you do not have access to the API credentials of your payment processor, do not worry. Hyperswitch has a demo payment processor automatically configured to your sandbox account. It will assist you to simulate various payment flows and assist you in completing the integration.

## Integrate Hyperswitch

Don't want to write code? Check out the [Hyperswitch Postman Collection](https://www.postman.com/hyperswitch/workspace/hyperswitch/request/25176183-9b4ad6a8-fbdd-4919-8505-c75c83bdf9d6) for a no-code way to get started with Hyperswitch's API.

You will be using both a server and a client-side component of Hyperswitch to complete the integration.

The payment flow begins once your user has added products to a shopping cart and now wishes to make a payment.

**Step 1:** Your server will create a payment with Hyperswitch server, to get a client\_secret.

**Step 2:** Your website loads and initiates the [Hyperswitch SDK](integration-steps.md) to render a payment widget to the customer. Depending on the customer's currency and country, the list of payment methods are displayed to the customer.

**Step 3:** The customer chooses a payment method, enters additional information (say card details) and hits the pay button.

**Step 4:** Hyperswitch SDK securely transmits the payment information to Hyperswitch Server. The Hyperswitch server processes the payment with the most suitable payment processor, as per the your smart routing algorithm.

**Step 5:** Upon successful payment, the customer is automatically redirected to your payment status confirmation page.

<figure><img src="../.gitbook/assets/image (69).png" alt=""><figcaption></figcaption></figure>

## Configure and manage payment methods on the Hyperswitch Control Center

The control center provides complete control on your payment operations.

* **Enable and manage payment processors:** Easily onboard multiple payment processors and manage payment methods with a few clicks.
* **Track payment and refund information:** The unified control center allows you to query upon a particular payment or refund. You may also initiate refunds from the control center.
* **Smart payment routing:** You will have the complete capability to dynamically set the payment routing logic based on 20+ variables. Use this to optimize your payment processing goals.

Learn how to enable all payment methods [here](payment-methods-setup/cards.md) starting with Cards.

