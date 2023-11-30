# Bambora

![logo\_bambora](https://hyperswitch.io/icons/homePageIcons/logos/bamboraLogo.svg)

### About

Bambora, a Worldline solution, design and operate leading digital payment and transactional solutions that enable sustainable economic growth and reinforce trust and security.

| Payment Methods | Features supported                                                               | Payment Flows     |
| --------------- | -------------------------------------------------------------------------------- | ----------------- |
| `Cards`         | All major card networks like Mastercard, Visa, Diners, American Express and more | One-time payments |
| `Wallets`       | Google Pay, Apple pay                                                            | One-time payments |

#### Additional features

* Support for Refunds and webhooks
* Support for 3DS 2.0 and non-3DS transactions

### Activating Bambora via Hyperswitch

#### I. Prerequisites

1. You need to be registered with Bambora in order to proceed. In case you aren't, you can quickly setup your Bambora account [here](https://www.bambora.com)
2. You should have a registered Hyperswitch account. You can access your account from the [Hyperswitch dashboard](https://app.hyperswitch.io/register)

#### II. Steps to activate Bambora with Hyperswitch

1. Ensure that you are on the Test Mode of the Hyperswitch Dashboard. You would be able to toggle between the Live and Test modes from the top right corner of the Dashboard
2. Navigate to the [Connectors](https://app.hyperswitch.io/connectors) section on the Hyperswitch Dashboard and select Bambora using the '+ Connect' button

<figure><img src="../../.gitbook/assets/connector_unifiedcheckout.png" alt="" width="358"><figcaption></figcaption></figure>

3. Enter your Country, Business Label and Bambora **Passcode** and **Merchant ID**. The Bambora keys can be found in your Bambora dashboard
4. Select all the payment methods you wish to use Bambora for. Ensure that this is the same as the ones configured on your Bambora dashboard
5. Click Done and you will see a successful message that the configuration is complete

_Congratulations! You have successfully configured with Bambora via Hyperswitch. Now in order to test the integration you can follow one of the following steps Test via Hyperswitch dashboard_

#### III. Test the Configuration using Dashboard

1. Upon configuration of the Connector, navigate to the dashboard [home page](https://app.hyperswitch.io/home)
2. Proceed with the "Try out Unified Checkout" option on the home page of the dashboard
3. Use the test payment details provided by Bambora to test a transaction and click on Pay Now

```
Card Number: 4005 5500 0000 0001
Expiry: 09/26
CVC: 123
```

4. Click on Pay Now and you will get a Success message&#x20;
5. Validate transaction on Hyperswitch dashboard \
   \- Goto the left pane on the Hyperswitch dashboard \
   \- Click on Operations -> Orders \
   \- Your transactions should be visible under the order management tab&#x20;
6. Open your Bambora dashboard and validate the transaction under the Payments Tab

_Congratulations! You have successfully tested the payment via Hyperswitch and processed by Bambora_

### Need support?

In case you continue to face issues reach us at [Hyperswitch support](https://hyperswitch.io/docs/support)
