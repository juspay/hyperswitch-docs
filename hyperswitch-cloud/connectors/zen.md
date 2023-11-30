# Zen

![logo\_zen](https://hyperswitch.io/img/site/zenLogo.svg)&#x20;

### About

Zen is a modern and responsive payments portal with low fees for conversion boost and increased revenue

### Features supported by Hyperswitch

| Payment Methods | Features supported                                                               | Payment Flows                   |
| --------------- | -------------------------------------------------------------------------------- | ------------------------------- |
| `Cards`         | All major card networks like Mastercard, Visa, Diners, American Express and more | One-time and recurring payments |
| `Wallets`       | Google pay, Apple pay                                                            | One-time payments               |

### Additional features

* Refunds, Subscriptions and Asynchronous updates via webhooks
* Support for 3DS 2.0 and non-3DS transactions

### Activating Zen via Hyperswitch

#### I. Prerequisites

1. You need to be registered with Zen and obtained the API Key from your Zen Account manager.
2. You should have a registered Hyperswitch account. You can access your account from the [Hyperswitch dashboard](https://app.hyperswitch.io/)
3. Request the Zen support team to enable handling raw card data for your account. This will enable Hyperswitch to securely handle your customer's payment details

#### II. Steps to activate Zen on the Hyperswitch Dashboard

1. Ensure that you are on the Test Mode of the Hyperswitch Dashboard. You would be able to toggle between the Live and Test modes from the top right corner of the Dashboard
2. Navigate to the [Connectors](https://app.hyperswitch.io/connectors) section on the Hyperswitch Dashboard and select Adyen using the '+ Connect' button

3\. Enter your Country of operation and Zen API key.

4\. Select all the payment methods you wish to use Zen for.

5. Click Done and you will see a successful message that the configuration is complete.

_Congratulations! You have successfully integrated with Zen via Hyperswitch. Now in order to test the integration you can follow one of the following steps Test via Hyperswitch dashboard_

#### III. Test the Configuration using Dashboard

1. Upon configuration of the Connector, navigate to the dashboard [home page](https://app.hyperswitch.io/home)
2. Proceed with the "Try out Unified Checkout" option on the home page of the dashboard

<figure><img src="../../.gitbook/assets/connector_unifiedcheckout.png" alt="" width="358"><figcaption></figcaption></figure>

3. Use the test payment details provided by Zen to test a transaction and click on Pay Now

```
Card Number: 4242424242424242
Expiry: 03/30
CVC: 100
```

4. Click on Pay Now and you will get a Success message&#x20;
5. Validate transaction on Hyperswitch dashboard. \
   \- Goto the left pane on the Hyperswitch dashboard \
   \- Click on Operations -> Orders \
   \- Your transactions should be visible under the order management tab
6. Open your Zen dashboard and validate the transaction under the Payments Tab

_Congratulations! You have successfully tested the a payment via Hyperswitch and processed by Zen_

### Need support?

In case you continue to face issues, Reach us on [Hyperswitch support](https://hyperswitch.io/docs/support)
