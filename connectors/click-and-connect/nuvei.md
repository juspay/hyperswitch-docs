# Nuvei

![logo\_discord](https://hyperswitch.io/icons/homePageIcons/logos/nuveiLogo.svg)

### About

Nuvei is a payment technology company that provides payment processing and acquiring services to merchants worldwide, with a focus on e-commerce and high-growth industries.

| Payment Methods  | Features supported                                                               | Payment Flows     |
| ---------------- | -------------------------------------------------------------------------------- | ----------------- |
| `Cards`          | All major card networks like Mastercard, Visa, Diners, American Express and more | One-time payments |
| `Wallets`        | Google Pay, Apple pay, Paypal                                                    | One-time payments |
| `Bank redirects` | Ideal, Giropay, Sofort, EPS                                                      | One-time payments |

#### Additional features

* Support for Refunds and webhooks
* Support for 3DS 2.0 and non-3DS transactions

### Activating Nuvei via Hyperswitch

#### I. Prerequisites

1. You need to be registered with Nuvei in order to proceed. In case you aren't, you can quickly setup your Nuvei account [here](https://nuvei.com/)
2. You should have a registered Hyperswitch account. You can access your account from the [Hyperswitch dashboard](https://app.hyperswitch.io/)

#### II. Steps to activate Nuvei with Hyperswitch

1. Ensure that you are on the Test Mode of the Hyperswitch Dashboard. You would be able to toggle between the Live and Test modes from the top right corner of the Dashboard
2. Navigate to the [Connectors](https://app.hyperswitch.io/connectors) section on the Hyperswitch Dashboard and select Nuvei using the '+ Connect' button
3. Enter your Country, Business Label and Nuvei **Merchant ID**, **Mechant Secret** and **Merchant Site ID**. The Nuvei API key can be found in your Nuvei dashboard under Settings -> My Account -> Account Details
4. Select all the payment methods you wish to use Nuvei for. Ensure that this is the same as the ones configured on your Nuvei dashboard
5. Click Done and you will see a successful message that the configuration is complete

_Congratulations! You have successfully configured with Nuvei via Hyperswitch. Now in order to test the integration you can follow one of the following steps Test via Hyperswitch dashboard_

#### III. Test the Configuration using Dashboard

1. Upon configuration of the Connector, navigate to the dashboard [home page](https://app.hyperswitch.io/home)
2. Proceed with the "Try out Unified Checkout" option on the home page of the dashboard

<figure><img src="../../.gitbook/assets/connector_unifiedcheckout.png" alt="" width="358"><figcaption></figcaption></figure>

3. Use the test payment details provided by Nuvei to test a transaction and click on Pay Now

```
Card Number: 4444 3333 2222 1111
Expiry: 09/26
CVC: 123
```

4. Click on Pay Now and you will get a Success message
5. Validate transaction on Hyperswitch dashboard \
   \- Goto the left pane on the Hyperswitch dashboard \
   \- Click on Operations -> Orders \
   \- Your transactions should be visible under the order management tab
6. Open your Nuvei dashboard and validate the transaction under the Payments Tab

_Congratulations! You have successfully tested the payment via Hyperswitch and processed by Nuvei_

### Need support?

In case you continue to face issues reach us at [Hyperswitch support](https://hyperswitch.io/docs/support)
