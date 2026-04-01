---
description: >-
  Test a payment with your configured connector using the Hyperswitch dashboard,
  including test credentials for popular connectors and payment methods like
  Klarna, Google Pay, and Apple Pay.
icon: vial-circle-check
---

# Try a Payment

### Test the Configuration using Dashboard

1. Upon configuration of the Connector, navigate to the dashboard [home page](https://app.hyperswitch.io/home)
2. Proceed with the "Try a test payment" option on the home page of the dashboard.
3. Set up your demo checkout page by providing Business profile, Profile Id, Currency and Amount.
4. Click on **Show Preview**. Your demo checkout page will be visible in the preview section.
5. Choose the desired payment method in the demo page, Please find the test payment instrument data [here](test-a-payment-with-connector.md#test-credentials)
6. Click on Pay and you will get a Success message
7. Validate the transaction on the Juspay Hyperswitch dashboard:
   * Go to the left pane on the Hyperswitch dashboard.
   * Click on **Operations > Payments**.
   * Your transactions should be visible under the order management tab.

<figure><img src="../../../.gitbook/assets/Screenshot 2024-12-10 at 11.55.19 AM.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/Screenshot 2024-12-10 at 11.55.03 AM.png" alt=""><figcaption></figcaption></figure>

### Test Credentials

#### Test Cards for popular connectors <a href="#test-cards-for-popular-connectors" id="test-cards-for-popular-connectors"></a>

| Connector       | Card Number      | Expiry MM/YY | CVV | Reference - More Test Credentials                                                                           |
| --------------- | ---------------- | ------------ | --- | ----------------------------------------------------------------------------------------------------------- |
| Adyen           | 4000020000000000 | 03/30        | 737 | [Click here](https://docs.adyen.com/development-resources/testing/test-card-numbers)                        |
| Bluesnap        | 6011000180331112 | 02/26        | 123 | [Click here](https://developers.bluesnap.com/reference/test-credit-cards)                                   |
| Authorize.net   | 4242424242424242 | 12/25        | 100 | [Click here](https://developer.authorize.net/hello_world/testing_guide.html)                                |
| Braintree       | 4111111111111111 | 12/25        | 100 | [Click here](https://developer.paypal.com/braintree/docs/reference/general/testing/php#credit-card-numbers) |
| Checkout        | 4242424242424242 | 12/25        | 100 | [Click here](https://www.checkout.com/docs/testing/test-cards)                                              |
| Fiserv          | 4005550000000019 | 02/35        | 123 | -                                                                                                           |
| Global Payments | 4263970000005262 | 12/25        | 100 | [Click here](https://developer.globalpay.com/resources/test-card-numbers)                                   |
| Nuvei           | 4444333322221111 | 12/25        | 123 | [Click here](https://helpdesk.nuvei.com/doku.php?id=developer:integration_docs:testing-guide)               |
| Stripe          | 4242424242424242 | 12/25        | 100 | [Click here](https://stripe.com/docs/testing#cards)                                                         |
| Worldline       | 4012000033330026 | 12/25        | 123 | [Click here](https://epayments.developer-ingenico.com/documentation/testcases/detail/visa)                  |

**Dummy Connector test cards**

* Different flows are available for dummy connector transactions, determined by the card number.
* For dummy connector cards, both the expiration date and CVV can be any future date and three-digit number, respectively.
* Dummy connectors only support payments and refunds.
* Payments made with dummy connectors expire after 2 days. Refunds will not be possible for expired payments.

**Non 3DS flows**

* Success
  * 4111111111111111
  * 4242424242424242
  * 5555555555554444
  * 38000000000006
  * 378282246310005
  * 6011111111111117
* Card declined
  * 5105105105105100
  * 4000000000000002
* Insufficient funds
  * 4000000000009995
* Lost card
  * 4000000000009987
* Stolen card
  * 4000000000009979

**3DS flows**

* Success
  * 4000003800000446

#### Klarna - Direct integration test credentials <a href="#klarna---direct-integration-test-credentials" id="klarna---direct-integration-test-credentials"></a>

Simulate a successful payment with the following credentials

1. **United States**
   * Phone number: +1310668331
   * OTP: 123456 (Random 6-digit different from 999999)
2. **United Kingdom**
   * Phone number: +4408082580300
   * OTP: 123456 (Random 6-digit different from 999999)

For testing more scenarios, please refer [Klarna - Sample customer data](https://docs.klarna.com/resources/test-environment/sample-customer-data/)

#### Google Pay - Test credentials <a href="#googlepay---test-credentials" id="googlepay---test-credentials"></a>

In order to test Google Pay, you will have to use your Gmail account and join [Google’s test user group](https://groups.google.com/g/googlepay-test-mode-stub-data).

You will land on Google’s page which says “Congratulations! You now have access to our test suite! No further action is required.”

Ensure that you are logged in to your Gmail account, hit the Google Pay option. You will automatically get all test cards on your user journey.

#### Apple Pay - Test credentials <a href="#applepay---test-credentials" id="applepay---test-credentials"></a>

In order to test Apple Pay, you will need to follow these steps written in [Apple Pay sandbox testing docs](https://developer.apple.com/apple-pay/sandbox-testing/).

Apple Pay provides test cards from various card companies and supported regions as well. To pay you can use Touch ID on the MacBook or your iPhone. These devices should be configured in your Apple account.

#### Unable to Test Apple Pay Successfully?

1. Apple Pay sandbox testing is supported only if you are located in any of these [15 countries](https://developer.apple.com/apple-pay/sandbox-testing/).
2. Your Safari browser automatically detects your location from your System Preferences.
3. If you are not located in the supported countries, but still wish to test Apple Pay, please change your Region using **Mac System Preferences > Language & Region** and choose any of the 15 supported countries.

<figure><img src="../../../.gitbook/assets/languageRegion (1).png" alt=""><figcaption></figcaption></figure>
