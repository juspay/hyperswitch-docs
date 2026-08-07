---
description: >-
  Accept payments globally through Adyen via Hyperswitch, supporting cards,
  wallets, and local payment methods.
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/kf7BGdsPkCw9nalhAIlE/other-features/connectors/available-connectors/adyen
---

# Adyen

{% hint style="info" %}
This section gives you an overview of how to make payments via Adyen through Hyperswitch.
{% endhint %}

\
<img src="https://hyperswitch.io/icons/homePageIcons/logos/adyenLogo.svg" alt="" data-size="original">

Adyen is a global payments company allowing businesses to accept payments on a global scale. It offers a variety of local and international payment methods. To know more about payment methods supported by Adyen via Juspay Hyperswitch, visit [here](https://hyperswitch.io/pm-list).

### Activating Adyen via Hyperswitch

#### I. Prerequisites

1. You need to be registered with Adyen in order to proceed. In case you aren't, you can quickly set up your Adyen account [here](https://www.adyen.com/signup).
2. You should have a registered Hyperswitch account. You can access your account from the [Hyperswitch control center](https://app.hyperswitch.io/register).
3. Request the Adyen support team to enable handling raw card data for your Adyen account via email (support@adyen.com). This will enable Hyperswitch to securely handle your customer's payment details.
4. The Adyen API key and Account ID are available in your Adyen dashboard under: Home page -> Developers -> API credentials.
5. Select all the payment methods you wish to use Adyen for. Ensure that these are the same as the ones configured on your Adyen dashboard under Settings -> Payment methods.
6. To set webhooks, navigate to the webhooks section of your Adyen dashboard (Developers -> Webhooks) and create a new standard webhook. Know more about the webhook source verification key [here](https://docs.adyen.com/development-resources/webhooks/verify-hmac-signatures/#enable-hmac-signatures).

[Steps](https://docs.hyperswitch.io/hyperswitch-cloud/connectors/activate-connector-on-hyperswitch) to activate Adyen on Hyperswitch control center.

#### II. Points to remember

1. For Klarna, the following fields are mandatory or recommended to improve customer experience and conversion rates:
   * `email`
   * `billing.first_name`
   * `billing.last_name`
   * `billing.city`
   * `billing.country`
   * `billing.line1`
   * `billing.line2`
   * `billing.zip`
   * `order_details`
2. For Klarna, `customer_id` is also a required field for which you have to create a customer using [Hyperswitch - Create Customer](https://api-reference.hyperswitch.io/api-reference/customers/customers--create).
3.  Supported Country-Currency matrix:

    |   Payment Method   | Country                                                                                                                                     | Currency                                                                                      |
    | :----------------: | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
    | Credit/Debit Cards | All enabled on your Adyen account                                                                                                           | All enabled on your Adyen account                                                             |
    |      Apple Pay     | `AU,NZ,CN,JP,HK,SG,MY,BH,AE,KW,BR,ES,GB,SE,NO,AT,NL,DE,HU,CY,LU,CH,BE,FR,DK,FI,RO,HR,LI,UA,MT,SI,GR,PT,IE,CZ,EE,LT,LV,IT,PL,IS,CA,US`       | `AUD,CHF,CAD,EUR,GBP,HKD,SGD,USD`                                                             |
    |     Google Pay     | `AU,NZ,JP,HK,SG,MY,TH,VN,BH,AE,KW,BR,ES,GB,SE,NO,SK,AT,NL,DE,HU,CY,LU,CH,BE,FR,DK,RO,HR,LI,MT,SI,GR,PT,IE,CZ,EE,LT,LV,IT,PL,TR,IS,CA,US`    | All enabled on your Adyen account                                                             |
    |       PayPal       | `AU,NZ,CN,JP,HK,MY,TH,KR,PH,ID,AE,KW,BR,ES,GB,SE,NO,SK,AT,NL,DE,HU,CY,LU,CH,BE,FR,DK,FI,RO,HR,UA,MT,SI,GI,PT,IE,CZ,EE,LT,LV,IT,PL,IS,CA,US` | `AUD,BRL,CAD,CZK,DKK,EUR,HKD,HUF,INR,JPY,MYR,MXN,NZD,NOK,PHP,PLN,RUB,GBP,SGD,SEK,CHF,THB,USD` |
    |        iDEAL       | `NL`                                                                                                                                        | `EUR`                                                                                         |
    |       Sofort       | `AT,BE,DE,ES,CH,NL`                                                                                                                         | `CHF,EUR`                                                                                     |
    |       Klarna       | `AU,AT,BE,CA,CZ,DK,FI,FR,DE,GR,IE,IT,NO,PL,PT,RO,ES,SE,CH,NL,GB,US`                                                                         | `AUD,EUR,CAD,CZK,DKK,NOK,PLN,RON,SEK,CHF,GBP,USD`                                             |

    * If your desired country-currency combination is not listed here, please reach out to Hyperswitch Support to get it enabled.
4. **(Special Note):** For Klarna and PayPal, in the Adyen Sandbox environment, Automatic Capture is not working as intended. All payments are required to be explicitly captured, and only then will refunds be processed. This might be an account configuration issue from Adyen; there are no detected bugs or issues from Hyperswitch's end. If the same behaviour persists in production, please reach out to your Adyen Support or Hyperswitch Support to stop Automatic Captures for the same.
5. **(Special Note):** For Sofort, Adyen has discontinued support for Sofort as a payment method. Hyperswitch provides the integration of Sofort via Adyen, but it is subject to availability by Adyen on your account. Some or all features might not work if Adyen has not enabled it for you. Please contact Adyen support to resolve this.
