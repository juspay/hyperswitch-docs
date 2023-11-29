# ⚡ Quickstart

## Getting Started with Hyperswitch

> Hyperswitch is an Open Source Payment orchestrator intended to simplify payments for the merchants. With Hyperswitch, you can connect to multiple Payment processors, aggregators, banks, wallets, BNPLs and future payment methods with a few clicks on our dashboard.

### Use API keys to authenticate API requests.

> Hyperswitch authenticates your API requests using your account’s API keys. Hyperswitch raises an invalid request error if you don’t include a key, and an authentication error if the key is incorrect or outdated.

You can use the Hyperswitch Dashboard to reveal, revoke, and create secret API keys. If you’re setting up Hyperswitch through a third-party platform (3PP), reveal your API keys in live mode to begin processing payments.

#### 1. Get your Hyperswitch API key

If you have not created a sandbox account, please create one

[Sign Up for Hyperswitch](https://app.hyperswitch.io/register)

If you have already created a sandbox account, your api key could be fetched from [settings section](https://app.hyperswitch.io/developers).

#### 2. Configure your payment processor

Configure the payment processor of your choice using [Connectors](https://app.hyperswitch.io/connectors) tab on our dashboard. You will need to have the API credentials of the payment processor readily available.

If you do not have access to the API credentials of your payment processor, do not worry. Hyperswitch has a demo payment processor automatically configured to your sandbox account. It will assist you to simulate various payment flows and assist you in completing the integration.

#### 3. Integrate Hyperswitch

Don't want to write code? Check out the [Hyperswitch Postman Collection](https://www.postman.com/hyperswitch/workspace/hyperswitch/request/25176183-9b4ad6a8-fbdd-4919-8505-c75c83bdf9d6) for a no-code way to get started with Hyperswitch's API.

You will be using both a server and a client-side component of Hyperswitch to complete the integration.

The payment flow begins once your user has added products to a shopping cart and now wishes to make a payment.

**Step 1:** Your server will create a payment with Hyperswitch server, to get a client\_secret.

**Step 2:** Your website loads and initiates the [Hyperswitch SDK](https://hyperswitch.io/docs/sdkIntegrations/unifiedCheckoutWeb/) to render a payment widget to the customer. Depending on the customer's currency and country, the list of payment methods are displayed to the customer.

**Step 3:** The customer chooses a payment method, enters additional information (say card details) and hits the pay button.

**Step 4:** Hyperswitch SDK securely transmits the payment information to Hyperswitch Server. The Hyperswitch server processes the payment with the most suitable payment processor, as per the your smart routing algorithm.

**Step 5:** Upon successful payment, the customer is automatically redirected to your payment status confirmation page.

<figure><img src=".gitbook/assets/image (69).png" alt=""><figcaption></figcaption></figure>

#### 4. Configure and manage payment methods on hyperswitch Dashboard

The [Hyperswitch dashboard](https://app.hyperswitch.io/register) provides complete control on your payment operations.

* **Enable and manage payment processors:** Easily onboard multiple payment processors and manage payment methods with a few clicks.
* **Track payment and refund information:** The unified dashboard allows you to query upon a particular payment or refund. You may also initiate refunds from the dashboard.
* **Smart payment routing:** You will have the complete capability to dynamically set the payment routing logic based on 20+ variables. Use this to optimize your payment processing goals.

Learn how to enable all payment methods [here](https://hyperswitch.io/docs/paymentMethods/cards) starting with Cards.

