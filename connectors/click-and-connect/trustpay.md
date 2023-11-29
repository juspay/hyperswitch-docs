# TrustPay

![logo\_discord](https://hyperswitch.io/icons/homePageIcons/logos/trustpayLogo.svg)

### About

TrustPay belongs to the first financial institutions within the region to provide secure e-commerce payments across the EEA area. They provide innovative payment services for online businesses with cross-border reach offering a variety of payment solutions.

| Payment Methods | Features supported                                                               | Payment Flows     |
| --------------- | -------------------------------------------------------------------------------- | ----------------- |
| `Cards`         | All major card networks like Mastercard, Visa, Diners, American Express and more | One-time payments |
| `Wallets`       | Google Pay, Apple pay                                                            | One-time payments |

#### Additional features

* Support for Refunds
* Support for 3DS 2.0 and non-3DS transactions

### Activating TrustPay via Hyperswitch

#### I. Prerequisites

1. You need to be registered with TrustPay in order to proceed. In case you aren't, you can quickly setup your TrustPay account [here](https://www.trustpay.eu/)
2. You should have a registered Hyperswitch account. You can access your account from the [Hyperswitch dashboard](https://app.hyperswitch.io/)

#### II. Steps to activate TrustPay with Hyperswitch

1. Ensure that you are on the Test Mode of the Hyperswitch Dashboard. You would be able to toggle between the Live and Test modes from the top right corner of the Dashboard
2. Navigate to the [Connectors](https://app.hyperswitch.io/connectors) section on the Hyperswitch Dashboard and select TrustPay using the '+ Connect' button
3. Enter your Country, Business Label and TrustPay **API Key**, **Project ID** and **Secret Key**. The TrustPay keys can be found in your TrustPay dashboard
4. Select all the payment methods you wish to use TrustPay for. Ensure that this is the same as the ones configured on your TrustPay dashboard
5. Click Done and you will see a successful message that the configuration is complete

_Congratulations! You have successfully configured with TrustPay via Hyperswitch. Now in order to test the integration you can follow one of the following steps Test via Hyperswitch dashboard_

#### III. Test the Configuration using Dashboard

1. Upon configuration of the Connector, navigate to the dashboard [home page](https://app.hyperswitch.io/home)
2. Proceed with the "Try out Unified Checkout" option on the home page of the dashboard

<figure><img src="../../.gitbook/assets/connector_unifiedcheckout.png" alt="" width="358"><figcaption></figcaption></figure>

3. Use the test payment details provided by TrustPay to test a transaction and click on Pay Now

```
Card Number: 4111 1111 1111 1111
Expiry: 09/26
CVC: 123
```

4. Click on Pay Now and you will get a Success message
5. Validate transaction on Hyperswitch dashboard \
   \- Goto the left pane on the Hyperswitch dashboard \
   \- Click on Operations -> Orders \
   \- Your transactions should be visible under the order management tab
6. Open your TrustPay dashboard and validate the transaction under the Payments Tab

_Congratulations! You have successfully tested the payment via Hyperswitch and processed by TrustPay_

### Need support?

In case you continue to face issues reach us at [Hyperswitch support](https://hyperswitch.io/docs/support)
