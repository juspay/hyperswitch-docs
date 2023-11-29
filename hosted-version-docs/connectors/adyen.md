# Adyen

<img src="https://hyperswitch.io/icons/homePageIcons/logos/adyenLogo.svg" alt="" data-size="original">

### About

Adyen is a global payments company allowing businesses to accept payments on a global scale. It offers a variety of local and international payment methods.

### Features supported by Hyperswitch

| Payment Methods     | Features supported                                                               | Payment Flows                   |
| ------------------- | -------------------------------------------------------------------------------- | ------------------------------- |
| `Cards`             | All major card networks like Mastercard, Visa, Diners, American Express and more | One-time and recurring payments |
| `Wallets`           | Google pay, Apple pay, Paypal                                                    | One-time payments               |
| `BNPLs`             | Klarna, Affirm, Afterpay                                                         | One-time payments               |
| `Banking Redirects` | Ideal, Giropay, Sofort, EPS                                                      | One-time payments               |

### Additional features

* Refunds, Subscriptions and Asynchronous updates via webhooks
* Support for 3DS 2.0 and non-3DS transactions

### Activating Adyen via Hyperswitch

#### I. Prerequisites

1. You need to be registered with Adyen in order to proceed. In case you aren't, you can quickly setup your Adyen account [here](https://www.adyen.com/signup)
2. You should have a registered Hyperswitch account. You can access your account from the [Hyperswitch dashboard](https://app.hyperswitch.io/register)
3. Request the Adyen support team to enable handling raw card data for your Adyen account via email (support@adyen.com). This will enable Hyperswitch to securely handle your customer's payment details

#### II. Steps to activate Adyen on the Hyperswitch Dashboard

1. Ensure that you are on the Test Mode of the Hyperswitch Dashboard. You would be able to toggle between the Live and Test modes from the top right corner of the Dashboard
2. Navigate to the [Connectors](https://app.hyperswitch.io/connectors) section on the Hyperswitch Dashboard and select Adyen using the '+ Connect' button
3. Enter your Country, Adyen API key and Account ID. The Adyen API key and Account ID are available in your Adyen dashboard under - Home page -> Developers -> API credentials
4. Select all the payment methods you wish to use Adyen for. Ensure that this is the same as the ones configured on your Adyen dashboard under Settings -> Payment methods
5. Click Done and you will see a successful message that the configuration is complete
6. Webhooks: Navigate to the webhooks section of your Adyen dashboard (Developers -> Webhooks) and create a new standard webhook.
7. Enter the hyperswitch url under the server configuration section: `{{hyperswitch_base_url}}`/webhooks/Hyperswitch\_Merchant\_ID/adyen. Note that Hyperswitch currently does not support source verification.

_Congratulations! You have **successfully integrated with Adyen via Hyperswitch**. Now in order to test the integration you can follow one of the following steps Test via Hyperswitch dashboard_

#### III. Test the Configuration using Dashboard

1. Upon configuration of the Connector, navigate to the dashboard [home page](https://app.hyperswitch.io/home)
2. Proceed with the "Try out Unified Checkout" option on the home page of the dashboard

<figure><img src="../../.gitbook/assets/connector_unifiedcheckout.png" alt="" width="358"><figcaption></figcaption></figure>

3. Use the test payment details provided by Adyen to test a transaction and click on Pay Now

```
Card Number: 4000020000000000
Expiry: 03/30
CVC: 737
Country: United States
```

4. Click on Pay Now and you will get a Success message&#x20;
5. Validate transaction on Hyperswitch dashboard. \
   \- Goto the left pane on the Hyperswitch dashboard \
   \- Click on Operations -> Orders \
   \- Your transactions should be visible under the order management tab&#x20;
6. Open your Adyen dashboard and validate the transaction under the Payments Tab

_Congratulations! You have **successfully tested the payment via Hyperswitch** and processed by Adyen_

### Need support?

In case you continue to face issues reach us at [Hyperswitch support](https://hyperswitch.io/docs/support)
