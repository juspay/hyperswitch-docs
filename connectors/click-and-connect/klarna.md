# Klarna

![logo\_discord](https://hyperswitch.io/icons/homePageIcons/logos/klarnaLogo.svg)

### About

It allows businesses to provide direct payments, pay later options, and installment plans in a one-click purchase experience.

### Features supported by Hyperswitch

| Payment Methods | Features supported | Payment Flows     |
| --------------- | ------------------ | ----------------- |
| `BNPL`          | Klarna             | One-time payments |

### Activating Klarna via Hyperswitch

#### I. Prerequisites

1. You need to be registered with Klarna in order to proceed. In case you aren't, you can quickly setup your Klarna account [here](https://www.klarna.com/us/business/)
2. You should have a registered Hyperswitch account. You can access your account from the [Hyperswitch dashboard](https://app.hyperswitch.io/register)

#### II. Steps to activate Klarna with Hyperswitch

1. Ensure that you are on the Test Mode of the Hyperswitch Dashboard. You would be able to toggle between the Live and Test modes from the top right corner of the Dashboard
2. Navigate to the [Connectors](https://app.hyperswitch.io/connectors) section on the Klarna Dashboard and select Klarna using the '+ Connect' button
3. Enter your Country, Business Label and Klarna **API Key**. The Klarna API key can be found in your Klarna dashboard under settings
4. Select all the payment methods you wish to use Klarna for. Ensure that this is the same as the ones configured on your Klarna dashboard
5. Click Done and you will see a successful message that the configuration is complete

_Congratulations! You have successfully configured with Klarna via Hyperswitch. Now in order to test the integration you can follow one of the following steps Test via Hyperswitch dashboard_

#### III. Test the Configuration using Dashboard

1. Upon configuration of the Connector, navigate to the dashboard [home page](https://app.hyperswitch.io/home)
2. Proceed with the "Try out Unified Checkout" option on the home page of the dashboard

<figure><img src="../../.gitbook/assets/connector_unifiedcheckout.png" alt="" width="358"><figcaption></figcaption></figure>

3. Use the test payment details provided by Klarna to test a transaction and click on Pay Now

```
Card Number: 4111 1111 1111 1111
Expiry: 12/28
CVC: 123
```

4. Click on Pay Now and you will get a Success message&#x20;
5. Validate transaction on Hyperswitch dashboard \
   \- Goto the left pane on the Hyperswitch dashboard \
   \- Click on Operations -> Orders \
   \- Your transactions should be visible under the order management tab
6. Open your Klarna dashboard and validate the transaction under the Payments Tab

_Congratulations! You have successfully tested the payment via Hyperswitch and processed by Klarna_

### Need support?

In case you continue to face issues reach us at [Hyperswitch support](https://hyperswitch.io/docs/support)
