# GlobalPayments

![logo\_globalPayment](https://hyperswitch.io/icons/homePageIcons/logos/GlobalPaymentsLogo.svg)

### About

Global Payments allows businesses to accept over 140 payment types across several channels with industry-specific solutions. Merchants can use it to set up subscriptions and recurring automatic payments, along with multiple customizable options for checkout.

### Features supported by Hyperswitch

| Payment Methods | Features supported                                                               | Payment Flows     |
| --------------- | -------------------------------------------------------------------------------- | ----------------- |
| `Cards`         | All major card networks like Mastercard, Visa, Diners, American Express and more | One-time payments |

#### Additional features

* Refunds
* Support for non-3DS transactions

### Activating GlobalPayments via Hyperswitch

#### I. Prerequisites

1. You need to be registered with GlobalPayments in order to proceed. In case you aren't, you can quickly setup your GlobalPayments account [here](https://www.globalpayments.com/en-ap)
2. You should have a registered Hyperswitch account. You can access your account from the [Hyperswitch dashboard](https://app.hyperswitch.io/register)

#### II. Steps to activate GlobalPayments with Hyperswitch

1. Ensure that you are on the Test Mode of the Hyperswitch Dashboard. You would be able to toggle between the Live and Test modes from the top right corner of the Dashboard
2. Navigate to the [Connectors](https://app.hyperswitch.io/connectors) section on the Hyperswitch Dashboard and select GlobalPayments using the '+ Connect' button
3. Enter your Country, Business Label and GlobalPayments **App Key**, **App ID** and **Account Name**. The GlobalPayments key and other details can be found in your GlobalPayments dashboard under My Account -> My Apps & Keys
4. Select all the payment methods you wish to use GlobalPayments for. Ensure that this is the same as the ones configured on your GlobalPayments dashboard
5. Click Done and you will see a successful message that the configuration is complete

_Congratulations! You have successfully configured with GlobalPayments via Hyperswitch. Now in order to test the integration you can follow one of the following steps Test via Hyperswitch dashboard_

#### III. Test the Configuration using Dashboard

1. Upon configuration of the Connector, navigate to the dashboard [home page](https://app.hyperswitch.io/home)
2. Proceed with the "Try out Unified Checkout" option on the home page of the dashboard

<figure><img src="../../.gitbook/assets/connector_unifiedcheckout.png" alt="" width="358"><figcaption></figcaption></figure>

3. Use the test payment details provided by GlobalPayments to test a transaction and click on Pay Now

```
Card Number: 4263 9700 0000 5262
Expiry: 12/25
CVC: 100
```

4. Click on Pay Now and you will get a Success message
5. Validate transaction on Hyperswitch dashboard \
   \- Goto the left pane on the Hyperswitch dashboard \
   \- Click on Operations -> Orders \
   \- Your transactions should be visible under the order management tab
6. Open your GlobalPayments dashboard and validate the transaction under the Payments Tab

_Congratulations! You have successfully tested the payment via Hyperswitch and processed by GlobalPayments_

### Need support?

In case you continue to face issues reach us at [Hyperswitch support](https://hyperswitch.io/docs/support)
