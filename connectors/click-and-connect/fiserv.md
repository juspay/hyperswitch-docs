# Fiserv

![logo\_discord](https://hyperswitch.io/icons/homePageIcons/logos/fiservLogo.svg)

### About

Fiserv is a global fintech and payments company with solutions for banking, global commerce, merchant acquiring, billing and payments, and point-of-sale.

### Features supported by Hyperswitch

| Payment Methods | Features supported                                                               | Payment Flows     |
| --------------- | -------------------------------------------------------------------------------- | ----------------- |
| `Cards`         | All major card networks like Mastercard, Visa, Diners, American Express and more | One-time payments |

#### Additional features

* Support for non-3DS transactions

### Activating Fiserv via Hyperswitch

#### I. Prerequisites

1. You need to be registered with Fiserv in order to proceed. In case you aren't, you can quickly setup your Fiserv account [here](https://www.fiserv.com/en.html)
2. You should have a registered Hyperswitch account. You can access your account from the [Hyperswitch dashboard](https://app.hyperswitch.io/register)

#### II. Steps to activate Fiserv with Hyperswitch

1. Ensure that you are on the Test Mode of the Hyperswitch Dashboard. You would be able to toggle between the Live and Test modes from the top right corner of the Dashboard
2. Navigate to the [Connectors](https://app.hyperswitch.io/connectors) section on the Hyperswitch Dashboard and select Fiserv using the '+ Connect' button
3. Enter your Country, Business Label and Fiserv **API Key**, **API Secret**, **Merchant ID** and **Terminal ID**. The Fiserv API key can be found in your Fiserv dashboard under Credentials
4. Select all the payment methods you wish to use Fiserv for. Ensure that this is the same as the ones configured on your Fiserv dashboard
5. Click Done and you will see a successful message that the configuration is complete

_Congratulations! You have successfully configured with Fiserv via Hyperswitch. Now in order to test the integration you can follow one of the following steps Test via Hyperswitch dashboard_

#### III. Test the Configuration using Dashboard

1. Upon configuration of the Connector, navigate to the dashboard [home page](https://app.hyperswitch.io/home)
2. Proceed with the "Try out Unified Checkout" option on the home page of the dashboard

<figure><img src="../../.gitbook/assets/connector_unifiedcheckout.png" alt="" width="358"><figcaption></figcaption></figure>

3. Use the test payment details provided by Fiserv to test a transaction and click on Pay Now

```
Card Number: 5413 3300 8901 0640
Expiry: 12/30
CVC: 123
```

4. Click on Pay Now and you will get a Success message
5. Validate transaction on Hyperswitch dashboard \
   \- Goto the left pane on the Hyperswitch dashboard \
   \- Click on Operations -> Orders \
   \- Your transactions should be visible under the order management tab
6. Open your Fiserv dashboard and validate the transaction under the Payments Tab

_Congratulations! You have successfully tested the payment via Hyperswitch and processed by Fiserv_

### Need support?

In case you continue to face issues reach us at [Hyperswitch support](https://hyperswitch.io/docs/support)
