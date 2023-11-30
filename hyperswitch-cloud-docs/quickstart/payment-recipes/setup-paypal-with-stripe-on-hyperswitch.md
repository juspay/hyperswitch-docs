# Setup Paypal with Stripe on Hyperswitch

![logo\_paypalstripe](https://hyperswitch.io/img/site/paypalstripe.png)

**Activate your Hyperswitch account**

Creating your HyperSwitch account is the first step toward using the service. With Hyperswitch you can process upto 10,000 transactions every month, and the free tier gets automatically activated for your account.

Navigate to the web dashboard to register a sandbox account with the HyperSwitch.

<figure><img src="https://hyperswitch.io/img/site/dasboardRegister.png" alt=""><figcaption></figcaption></figure>

After your account is registered, you will be redirected to the HyperSwitch control center in test sandbox mode.

### Build Hyperswitch



{% hint style="info" %}
Note: Your account is automatically configured with a Stripe Test and Paypal Test Processor. These configurations will act like mock payment processors and you can easily complete your Hyperswitch integration using this setup.
{% endhint %}

Proceed to build your app to process payments through Hyperswitch. To make the job easier Hyperswitch offers various two flavors of integration. Feel free to choose the most appropriate option and complete the integration.

* **Migrate from Stripe** - for those already integrated with Stripe UI Elements
* **Integrate from Scratch** - for those planning to start afresh with Hyperswitch integration

Before you choose the appropriate option, get your API key and Publishable key from the [Developers](https://app.hyperswitch.io/developers) page of Hyperswitch dashboard.

## Migrate from Stripe

**Estimated time to complete:** Less than 15 minutes

If you are already integrated with the leading payment processor Stripe, Hyperswitch makes your integration fast, fun and easy.

Below are the products and features of Stripe support for Hyperswitch quick migration. And once you migrate, get immediate access to 40+ payment processors and features of Hyperswitch.

```
<td>Cards</td>
<td>Supported</td>
```

| Stripe Products                          | Stripe UI elements                | Supported for Payment sheet, Card element and wallet element |
| ---------------------------------------- | --------------------------------- | ------------------------------------------------------------ |
| Stripe Payment links                     | Coming soon                       |                                                              |
| Stripe Checkout                          | Coming soon                       |                                                              |
| Functionalities                          | Payments (One-time and recurring) | Supported                                                    |
| Customers                                | Supported                         |                                                              |
| Refunds                                  | Supported                         |                                                              |
| Payment methods                          | Supported                         |                                                              |
| Payment Methods                          |                                   |                                                              |
| Digital wallets - Paypal, Applepay, Gpay | Supported                         |                                                              |
| Bank Transfers - Giropay, Sofort etc.,   | Supported                         |                                                              |
| BNPL - Klarna, Affirm, Afterpay          | Supported                         |                                                              |
| Backend platforms                        | Node                              | Supported                                                    |
| Python                                   | Coming soon                       |                                                              |
| PHP                                      | Coming soon                       |                                                              |
| Ruby                                     | Coming soon                       |                                                              |
| Frontend platforms                       | HTML                              | Supported                                                    |
| React                                    | Supported                         |                                                              |
| Java                                     | Supported                         |                                                              |
| Swift                                    | Supported                         |                                                              |
| React Native                             | Supported                         |                                                              |
| Woocommerce                              | Supported                         |                                                              |
| Bigcommerce                              | Coming soon                       |                                                              |
| Shopify                                  | Not supported                     |                                                              |

**Checkout the migration steps here:**

* [Web](../migrate-from-stripe/web.md)
* [Android](../migrate-from-stripe/android.md)
* [iOS](../migrate-from-stripe/ios.md)
* [React Native](../migrate-from-stripe/react-native.md)

## Integrate from Scratch

**Estimated time to complete:** 30 to 60 minutes

Hyperswitch provides ready-to-use code snippets for all platforms. You can choose to follow either of the approaches:

* Clone the [sample apps from Github](https://github.com/orgs/juspay/repositories?q=Hyperswitch+a+simple+integration+app\&type=public\&language=\&sort=) and run them on your local.
* Replicate the code snippets on your backend and frontend application to get you Hyperswitch integration up and running

Here is a quick primer on the [Integration Architecture](https://hyperswitch.io/docs/quickstart#3-integrate-hyperswitch).

{% hint style="info" %}
Note: This step is fully optional. Because, your account is automatically configured with a Stripe Test and Paypal Test Processor. These configurations will act like mock payment processors and you can easily complete your Hyperswitch integration using this setup.
{% endhint %}

### \[Optional step] Configure Payment Processors

As an optional step, if you have ready access to the API credentials of Stripe and Paypal, you can configure them on the Hyperswitch Dashboard. If you are registering yourself for the first time on Stripe or Paypal, you will need more information like Business Name, SSN, Registered address of business etc., and the process will take around 2 to 10 minutes.

So, let's proceed to configure two payment processors — one for Paypal and the other for the Stripe service.

Enabling a processor on HyperSwitch requires that you provide the API credentials generated in your account with the service. HyperSwitch will encrypt these credentials and only use them to authenticate the connections with the payment services.

Navigate to the **Processors** page under **Connectors** within the control center to view the list of processors supported on HyperSwitch.

<figure><img src="https://hyperswitch.io/img/site/dashboardProcessors.png" alt=""><figcaption></figcaption></figure>

#### Enabling Paypal Processor

Paypal provides a sandbox environment for developers to safely test out the service. You will need to provide a Paypal Client ID and Secret to use the Paypal processor through HyperSwitch.

Fetch the Client ID and Secret from [Paypal Dashboard](https://developer.paypal.com/dashboard/applications/sandbox)

<figure><img src="https://hyperswitch.io/img/site/paypalDashboard.png" alt=""><figcaption></figcaption></figure>

Navigate back to the **Processors** page and click on Paypal to connect with Hyperswitch

<figure><img src="https://hyperswitch.io/img/site/paypalprocessors.png" alt=""><figcaption></figcaption></figure>

Next, you need to verify the supported payment methods through which you want to receive payments with Paypal service.

<figure><img src="https://hyperswitch.io/img/site/paypalPaymentMethods.png" alt=""><figcaption></figcaption></figure>

Click the **Proceed** button to save the payment methods and complete the connection:

<figure><img src="https://hyperswitch.io/img/site/paypalSummary.png" alt=""><figcaption></figcaption></figure>

#### Enabling Stripe Processor

[Stripe is one of the world's leading payment companies](https://blog.logrocket.com/react-stripe-payment-system-tutorial/) that focuses on providing payment APIs. Similar to Paypal, Stripe also provides a sandbox environment for developers to safely test out the service. You will need to provide a Stripe key to use the Stripe processor for Hyperswitch.

Navigate to the [Developers](https://dashboard.stripe.com/test/apikeys) section of your Stripe dashboard and then select the “API keys” tab to view your secret key credential:

<figure><img src="https://hyperswitch.io/img/site/paypalApiKey.png" alt=""><figcaption></figcaption></figure>

Next, you need to adjust your integration settings on Stripe to enable you to handle card information through a third-party service such as HyperSwitch. HyperSwitch abides by its PCI compliance agreement within the Terms of Use to handle credit card information in the best way possible.

Navigate to the **Integration** page within your Stripe settings and toggle the “Handle Card information directly” switch:

<figure><img src="../../../.gitbook/assets/image (73).png" alt=""><figcaption></figcaption></figure>

Navigate back to the **Processors** page and click on Stripe to begin the second processor connection.

<figure><img src="../../../.gitbook/assets/image (77).png" alt=""><figcaption></figcaption></figure>

Select the Mastercard and Visa methods for debit and credit payments within the “Payment Methods” step.

<figure><img src="../../../.gitbook/assets/image (75).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (78).png" alt=""><figcaption></figcaption></figure>

Now, you will find the processors you have configured within the “Previously Connected” section of the **Processors** page. You can always edit the details for the connected processors wherever they change at a later time.

### Go live with Hyperswitch

From the **Home** page of Hyperswitch dashboard you can request for production access, by filling a short form. The Hyperswitch support team will verify your account and send you production access credentials on your registered email address within 8 hours.

<figure><img src="../../../.gitbook/assets/image (79).png" alt=""><figcaption></figcaption></figure>

Once you have access to the production credentials, please follow the instructions on the [go-live checklist](https://hyperswitch.io/docs/goLiveChecklist).
