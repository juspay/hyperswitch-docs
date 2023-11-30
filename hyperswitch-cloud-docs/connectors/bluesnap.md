# Bluesnap

![BlueSnap Logos](https://cdn2.hubspot.net/hubfs/454819/blog-files/Logo\_color.png)

### About

BlueSnap is a payment platform that allows businesses to easily accept online and mobile payments across the world. BlueSnap payment gateway integration can accept payments for e-commerce transactions, subscription billing models, and other online payment businesses need.

| Payment Methods | Features supported                                                               | Payment Flows     |
| --------------- | -------------------------------------------------------------------------------- | ----------------- |
| `Cards`         | All major card networks like Mastercard, Visa, Diners, American Express and more | One-time payments |
| `Wallets`       | Google Pay, Apple pay                                                            | One-time payments |

#### Additional features

* Support for Refunds
* Support for 3DS 2.0 and non-3DS transactions

### Activating Bluesnap via Hyperswitch

#### I. Prerequisites

1. You need to be registered with Bluesnap in order to proceed. In case you aren't, you can quickly setup your Bluesnap account [here](https://home.bluesnap.com/)
2. You should have a registered Hyperswitch account. You can access your account from the [Hyperswitch dashboard](https://app.hyperswitch.io/register)

#### II. Steps to activate Bluesnap with Hyperswitch

1. Ensure that you are on the Test Mode of the Hyperswitch Dashboard. You would be able to toggle between the Live and Test modes from the top right corner of the Dashboard
2. Navigate to the [Connectors](https://app.hyperswitch.io/connectors) section on the Hyperswitch Dashboard and select BlueSnap using the '+ Connect' button
3. Enter your Country, Business Label and Bluesnap **Username** and **Password**. The Bluesnap API key can be found in your Bluesnap dashboard under API settings
4. Select all the payment methods you wish to use Bluesnap for. Ensure that this is the same as the ones configured on your Bluesnap dashboard under Checkout Page -> Payment methods
5. Click Done and you will see a successful message that the configuration is complete

_Congratulations! You have successfully configured with Bluesnap via Hyperswitch. Now in order to test the integration you can follow one of the following steps Test via Hyperswitch dashboard_

#### III. Test the Configuration using Dashboard

1. Upon configuration of the Connector, navigate to the dashboard [home page](https://app.hyperswitch.io/home)
2. Proceed with the "Try out Unified Checkout" option on the home page of the dashboard

<figure><img src="../../.gitbook/assets/connector_unifiedcheckout.png" alt="" width="358"><figcaption></figcaption></figure>

3. Use the test payment details provided by Bluesnap to test a transaction and click on Pay Now

```
Card Number: 5425 2334 3010 9903
Expiry: 04/26
CVC: 123
```

4. Click on Pay Now and you will get a Success message&#x20;
5. Validate transaction on Hyperswitch dashboard \
   \- Goto the left pane on the Hyperswitch dashboard \
   \- Click on Operations -> Orders \
   \- Your transactions should be visible under the order management tab&#x20;
6. Open your Bluesnap dashboard and validate the transaction under the Payments Tab

_Congratulations! You have successfully tested the payment via Hyperswitch and processed by Bluesnap_

### Need support?

In case you continue to face issues reach us at [Hyperswitch support](https://hyperswitch.io/docs/support)
