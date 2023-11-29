# Stripe

![Stripe Logo](https://hyperswitch.io/icons/homePageIcons/logos/stripeLogo.svg)

### About

Stripe is a suite of APIs powering online payment processing and commerce solutions for internet businesses of all sizes. It allows businesses to accept payments and scale faster.

### Features supported by Hyperswitch

| Payment Methods     | Features supported                                                               | Payment Flows                   |
| ------------------- | -------------------------------------------------------------------------------- | ------------------------------- |
| `Cards`             | All major card networks like Mastercard, Visa, Diners, American Express and more | One-time and recurring payments |
| `Wallets`           | Google Pay, Apple pay                                                            | One-time payments               |
| `BNPL`              | Klarna, Affirm, AfterPay                                                         | One-time payments               |
| `Banking Redirects` | Ideal, Giropay, Sofort, EPS                                                      | One-time payments               |

#### Additional features

* Refunds, Subscriptions and Asynchronous updates via webhooks
* Support for 3DS 2.0 and non-3DS transactions

### Activating Stripe via Hyperswitch

#### I. Prerequisites

1. You need to be registered with Stripe in order to proceed. In case you aren't, you can quickly setup your Stripe account [here](https://dashboard.stripe.com/register)
2. You should have a registered Hyperswitch account. You can access your account from the [Hyperswitch dashboard](https://app.hyperswitch.io/)
3. Enable handling raw card data for your Stripe account by enabling the 'Handling card information directly' toggle from the [Settings > Integrations](https://dashboard.stripe.com/settings/integration) tab on your Stripe dashboard. This will enable Hyperswitch to securely handle your customer's payment details in a PCI compliant manner.

#### II. Steps to activate Stripe with Hyperswitch

1. Ensure that you are on the Test Mode of the Hyperswitch Dashboard. You would be able to toggle between the Live and Test modes from the top right corner of the Dashboard
2. Navigate to the [Connectors](https://app.hyperswitch.io/connectors) section on the Hyperswitch Dashboard and select Stripe using the '+ Connect' button

3\. Enter your Country, Business Label and Stripe API Key. The Stripe API key can be found in your Stripe dashboard under \[Developers -> API keys]\(https://dashboard.stripe.com/test/apikeys) as \*\*Secret Key\*\*

Note: Ensure to use the Secret Key -> Starts with \`sk\`\
\
4\. Select all the payment methods you wish to use Stripe for. Ensure that this is the same as the ones configured on your Stripe dashboard under Settings -> Payments -> Payment methods

5\. Click Done and you will see a successful message that the configuration is complete

6\. Webhooks: Navigate to the webhooks section of your Stripe dashboard (Developers -> Webhooks) and create a new webhook by clicking on \`Add an endpoint\`.

7. Enter the hyperswitch url under the Endpoint URL: `{{hyperswitch_base_url}}`/webhooks/Hyperswitch\_Merchant\_ID/stripe. Note that Hyperswitch currently does not support source verification.

_Congratulations! You have successfully configured with Stripe via Hyperswitch. Now in order to test the integration you can follow one of the following steps Test via Hyperswitch dashboard_

#### III. Test the Configuration using Dashboard

1. Upon configuration of the Connector, navigate to the dashboard [home page](https://app.hyperswitch.io/home)
2. Proceed with the "Try out Unified Checkout" option on the home page of the dashboard

<figure><img src="../../.gitbook/assets/connector_unifiedcheckout.png" alt="" width="358"><figcaption></figcaption></figure>

3. Use the test payment details provided by Stripe to test a transaction and click on Pay Now

```
Card Number: 4242 4242 4242 4242
Expiry: 03/30
CVC: 737
```

4. Click on Pay Now and you will get a Success message
5. Validate transaction on Hyperswitch dashboard. \
   \- Goto the left pane on the Hyperswitch dashboard \
   \- Click on Operations -> Orders \
   \- Your transactions should be visible under the order management tab
6. Open your Stripe dashboard and validate the transaction under the Payments Tab

_Congratulations! You have successfully tested the a payment via Hyperswitch and processed by Stripe_

### Need support?

In case you continue to face issues reach us at [Hyperswitch support](https://hyperswitch.io/docs/support)
