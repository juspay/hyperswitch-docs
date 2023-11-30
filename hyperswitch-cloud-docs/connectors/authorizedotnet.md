# Authorizedotnet

## Authorize.net

### About

Authorizedotnet, a Visa solution, is a US-based payment gateway service provider, allowing merchants to accept credit card and electronic check payments through their website and online.

### Features supported by Hyperswitch

| Payment Methods | Features supported                                                               | Payment Flows                   |
| --------------- | -------------------------------------------------------------------------------- | ------------------------------- |
| `Cards`         | All major card networks like Mastercard, Visa, Diners, American Express and more | One-time and recurring payments |
| `Wallets`       | Google pay, Apple pay                                                            | One-time payments               |

### Additional features

* Refunds and Subscriptions
* Support for non-3DS transactions

### Activating Authorizedotnet via Hyperswitch

### I. Prerequisites

1. You need to be registered with Authorizedotnet in order to proceed. In case you aren't, you can quickly setup your Authorizedotnet account [here](https://www.authorize.net/)
2. You should have registered and completed settings on [Hyperswitch dashboard](https://hyperswitch.io/contact-sales)

### II. Steps to activate Authorizedotnet with Hyperswitch

1. Ensure that you are on the Test Mode of the Hyperswitch Dashboard. You would be able to toggle between the Live and Test modes from the top right corner of the Dashboard
2. Navigate to the [Connectors](https://app.hyperswitch.io/connectors) section on the Hyperswitch Dashboard and select Authorizedotnet using the '+ Connect' button
3. Enter your Country, Business Label and Authorizedotnet **API Login ID** and **Transaction Key**. The Authorizedotnet API key can be found in your Authorizedotnet dashboard under the Account section (Security settings)
4. Select all the payment methods you wish to use Authorizedotnet for. Ensure that this is the same as the ones configured on your Authorizedotnet dashboard
5. Click Done and you will see a successful message that the configuration is complete

_Congratulations! You have successfully integrated with Authorizedotnet via Hyperswitch. Now in order to test the integration you can follow one of the following steps Test via Hyperswitch dashboard_

### III. Test the Configuration using Dashboard

1. Upon configuration of the Connector, navigate to the dashboard [home page](https://app.hyperswitch.io/home)
2. Proceed with the "Try out Unified Checkout" option on the home page of the dashboard

<figure><img src="../../.gitbook/assets/connector_unifiedcheckout.png" alt="" width="358"><figcaption></figcaption></figure>

3. Use the test payment details provided by Authorizedotnet to test a transaction and click on Pay Now

```
Card Number: 3700 0000 0000 002
Expiry: 09/26
CVC: 737
```

4. Click on Pay Now and you will get a Success message
5. Validate transaction on Hyperswitch dashboard\
   \- Goto the left pane on the Hyperswitch dashboard - Click on Operations -> Orders - Your transactions should be visible under the order management tab
6. Open your Authorizedotnet dashboard and validate the transaction under the Payments Tab

_Congratulations! You have successfully tested the payment via Hyperswitch and processed by Authorizedotnet_

### Need support?

In case you continue to face issues reach us at [Hyperswitch support](https://hyperswitch.io/docs/support)
