# Braintree

## About

Braintree is a payment processor that allows online businesses to accept payments via app or website. It also provides merchant accounts and payment gateways. PayPal owns Braintree, and a PayPal Business account is required.

## Features supported by Hyperswitch

| Payment Methods | Features supported                                                               | Payment Flows                   |
| --------------- | -------------------------------------------------------------------------------- | ------------------------------- |
| `Cards`         | All major card networks like Mastercard, Visa, Diners, American Express and more | One-time and recurring payments |
| `Wallets`       | Paypal                                                                           | One-time payments               |

## Additional features

* Refunds
* Support for non-3DS transactions

## Activating via Hyperswitch

## I. Prerequisites

1. You need to be registered with Braintree in order to proceed. In case you dont, you can quickly signup by visiting the Braintree's Website.
2. You should have setup you account using Hyperswitch dashboard

## II. Steps to activate Braintree with Hyperswitch

1. Select Braintree from the options under Select a Payment Gateway
2. Add your Merchant ID, Public key and Private key available in Braintree. The Braintree Merchant ID, Public key and Private key are available in your Braintree dashboard under - Home page -> Settings (on the top right) -> API
3. Select the environment as Test under environment at the PG
4. Select the payment methods you wish to enable through Braintree
5. Click Finish and you will see a successful message after the configuration is complete

_Congratulations! You have successfully configured with Braintree via Hyperswitch. Now in order to test the integration you can follow one of the following steps Test via Hyperswitch dashboard_

## III. Test the Configuration using Dashboard

1. Upon configuration of the Connector you will get a "Test Payment" button.
2. Use the test payment details provided by Braintree to test a transaction and click on Pay Now

```
Card Number: 4242424242424242
Expiry: 10/25
CVC: 123
Country: United States
```

3. Click on Pay Now and you will get a Success message
4. Validate transaction on Hyperswitch dashboard.
   * Goto the left pane on the Hyperswitch dashboard
   * Click on Operations -> Orders
   * Your transactions should be visible under the order management tab
5. For verification purpose, open your Braintree's dashboard and validate the transaction under the Payments Tab

_Congratulations! You have successfully tested the a payment via Hyperswitch and processed by Braintree_

## Need support?

In case you continue to face issues reach us at Hyperswitch support
