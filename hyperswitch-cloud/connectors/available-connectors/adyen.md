---
description: Accept payments through Adyen via Hyperswitch
---

# Adyen

{% hint style="info" %}
This section gives you an overview of how to make payments via Adyen through Hyperswitch
{% endhint %}

\
<img src="https://hyperswitch.io/icons/homePageIcons/logos/adyenLogo.svg" alt="" data-size="original">



Adyen is a global payments company allowing businesses to accept payments on a global scale. It offers a variety of local and international payment methods. To know about more about payment methods supported by adyen via hyperswitch visit [here](https://hyperswitch.io/pm-list).

### Activating Adyen via Hyperswitch

#### I. Prerequisites

1. You need to be registered with Adyen in order to proceed. In case you aren't, you can quickly setup your Adyen account [here](https://www.adyen.com/signup)
2. You should have a registered Hyperswitch account. You can access your account from the [Hyperswitch control center](https://app.hyperswitch.io/register).
3. Request the Adyen support team to enable handling raw card data for your Adyen account via email (support@adyen.com). This will enable Hyperswitch to securely handle your customer's payment details.
4. The Adyen API key and Account ID are available in your Adyen dashboard under - Home page -> Developers -> API credentials.
5. Select all the payment methods you wish to use Adyen for. Ensure that this is the same as the ones configured on your Adyen dashboard under Settings -> Payment methods
6. To set webhooks, Navigate to the webhooks section of your Adyen dashboard (Developers -> Webhooks) and create a new standard webhook. Know more about webhook source verification key [here](https://docs.adyen.com/development-resources/webhooks/verify-hmac-signatures/#enable-hmac-signatures).

[Steps](https://docs.hyperswitch.io/hyperswitch-cloud/connectors/activate-connector-on-hyperswitch) to activate Adyen on Hyperswitch control center.
