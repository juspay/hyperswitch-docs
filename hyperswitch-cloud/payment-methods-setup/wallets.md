---
description: International wallets supported by Hyperswitch
---

# 📱 Wallets

{% hint style="info" %}
Steps to integrate PayPal, Google Pay, Apple Pay
{% endhint %}

## Wallets

Hyperswitch supports leading international wallets which include:

* Digital wallets such as Paypal which enable customers to pay through wallet balance that they could load
* Card container wallets such as Google Pay and Apple Pay which enable customers to save their cards for quick one-click payments in supported websites

### Paypal

![Paypal Logo](https://hyperswitch.io/icons/homePageIcons/logos/paypalLogo.png)

Paypal is a digital wallet that lets customers load balance onto the wallet and as well as save their cards for quicker one-touch checkout. Paypal currently supports 200+ countries and 25 currencies.

**How to configure Paypal on Hyperswitch?**

Since Paypal is both a payment method (wallet) as well as a payment processor, Hyperswitch gives you the flexibility to configure Paypal through multiple avenues.

**Paypal native SDK experience:**

1. Before testing the PayPal SDK integration, ensure that you have enabled PayPal on your Braintree account. Go to [https://sandbox.braintreegateway.com/](https://sandbox.braintreegateway.com/).
2. Select the settings icon on the top right.
3. Select Processing and enable the PayPal option.

Currently, Hyperswitch supports Braintree’s [Vault](https://developer.paypal.com/braintree/docs/guides/paypal/overview) flow for Paypal as it offers seamless storing of payment methods for later use across Web, iOS and Android devices. The returning customers will be able to pay through Paypal with one-touch experience without logging in again after saving their card the first time.

**Paypal Redirection experience:**

1. Configuring Paypal through other payment processors like Adyen, Checkout, etc on Hyperswitch will redirect the customers to Paypal’s website to complete the payment. For this approach, you just have to make sure that you enable Paypal on your respective processors’ dashboards and also, enable Paypal while configuring these processors on your Hyperswitch dashboard.

### Google Pay

![Google Pay Logo PNG Vector](https://seeklogo.com/images/G/google-pay-logo-AA826E728D-seeklogo.com.png)

&#x20;Google Pay is a simple and secure way for customers to pay by adding their cards and bank account to their Google wallet. Currently, Google Pay is available through Web and Android devices in [70+ countries](https://support.google.com/googlepay/answer/12429287?hl=en#zippy=%2Cpay-in-store%2Cpay-online-or-in-apps) while iOS devices are supported only in the US and India.



Google Pay has additional layers of security embedded in its payment flow and hence Google Pay integration is bound to be elaborate by nature.

**Prerequisites**



There are few prerequisites that need to be fulfilled before integrating Google Pay on Hyperswitch -

1. Configure Google Pay on your processor's dashboard
2. In order to test Google Pay integration you will need to add test cards to your google account. You can go to [Google Pay API Test Cards Allowlist](https://groups.google.com/g/googlepay-test-mode-stub-data?pli=1) and click on Join Group to automatically add test cards in your Google Developer Account

**Configuring Google Pay on Hyperswitch**

To configure Google Pay on Hyperswitch follow the steps given below -

1. Login to [Hyperswitch dashboard](https://app.hyperswitch.io/)
2. In the Connectors tab, select your processor
3. While selecting Payment Methods, click on Google Pay in the Wallet section
4. Use this [link](https://developers.google.com/pay/api/web/guides/tutorial#tokenization) to search for your processor's input parameters. Get those parameters from the processor dashboard and configure them in Google Pay Merchant Key
5. In Google Pay Merchant Name, provide a user-visible merchant name

**Go-Live Checklist**

Your app requires an approval from Google Pay before you go live. Please follow [Google's instructions](https://developers.google.com/pay/api/android/guides/test-and-deploy/request-prod-access) and request production access.

1. Choose integration type **Gateway** when prompted.
2. Submit your app screenshots for review.
3. Set the Google Pay Environment to Production.
4. Once the app is reviewed and approved, launch GooglePay from a signed, released build your app.

**Google Pay Compatibility**

Google Pay is available only in certain countries or regions and on certain devices. Take a look at the [exhaustive list of countries](https://support.google.com/googlepay/answer/12429287?visit\_id=638320942600397737-977605919\&rd=1#zippy=%2Cpay-online-or-in-apps) where Google Pay is available. For security reasons, Google Pay is not supported in some browsers. Please check the list below to know the supported browsers:

| Browser                                         | Google Pay Support |
| ----------------------------------------------- | ------------------ |
| `Firefox`                                       | Yes                |
| `Chrome`                                        | Yes                |
| `Safari`                                        | Yes                |
| `Opera`                                         | Yes                |
| `Mobile-web: Firefox`                           | Yes                |
| `Mobile-web: Chrome`                            | Yes                |
| `Mobile-web: Safari`                            | Yes                |
| `iOS in-app browser - Instagram`                | No                 |
| `Android in-app browser - Instagram`            | No                 |
| `iOS in-app browser - X (Formerly Twitter)`     | Yes                |
| `Android in-app browser - X (Formerly Twitter)` | Yes                |

### Apple Pay

![Apple Pay Logo PNG Vector](https://seeklogo.com/images/A/apple-pay-logo-F68C9AC252-seeklogo.com.png)

Apple Pay allows customers to securely pay from their saved cards in their Apple Pay account in macOS (Safari) or iOS using Touch ID and Face ID and thereby eliminating the need for them to manually type in their card and shipping details. Apple Pay is currently supported by [participating banks and card issuers in 75+ countries](https://support.apple.com/en-us/HT207957).

Since Apple Pay also boasts additional layers of security, the payments flow and integration for Apple Pay are elaborate too.

**Prerequisites**

Before beginning to integrate Apple Pay with Hyperswitch, below prerequisites need to be fulfilled. _Please feel free to reach out to Hyperswitch support if you are stuck at any stage when integrating and testing Apple Pay._

1. Apple Pay requires an Apple Developer Account. You can [Sign Up](https://developer.apple.com/programs/enroll/) for one here.
2. You must have a valid SSL certificate on your domain _(meaning it begins with **https**)_

Apple Pay requires additional steps, and requires macOS 10.12.1+ or iOS 10.1+. Follow the steps given below to setting up Apple Pay -

**Step 1: Creating an Apple MerchantID**

You can create an Apple MerchantID referencing the video or following the steps mentioned below -



1. Log in to your [Apple Developer account](https://developer.apple.com/account/resources/certificates/list)
2. Go to the [add MerchantIDs section](https://developer.apple.com/account/resources/identifiers/add/merchant), select Merchant IDs and click Continue
3. Add a useful description _(like merchant id for test environment)_
4. Enter a unique descriptive identifier _(like merchant.com.testdomain.sandbox)_ and click Continue
5. Verify the description and identifier and click on Register

**Step 2: Validating Merchant Domain**

You can validate the merchant domain by following the steps mentioned below -

1. Log in to your [Apple Developer account](https://developer.apple.com/account/resources/certificates/list), go to Identifiers and select the Merchant ID you created previously
2. Under the Merchant Domains section, click on **Add Domain**
3. Enter your _merchant\_domain_ as domain and click on Save
4. Click on Download and a **.txt** file will be downloaded
5. Host this file on _merchant\_domain_/.well-known/apple-developer-merchantid-domain-association.txt
6. Once you host the .txt file in the path mentioned above, click on Verify
7. Make sure the status is verified as shown in the following image\
   \


**Step 3: Creating Apple MerchantID Certificate and Private Key**

You can create an Apple MerchantID certificate and private key referencing the video below or following the steps mentioned below -

\
Your browser does not support the video tag.

**Note:** It is recommended that you keep all the generated files in the same workspace for the sake of simplicity

1. Open a terminal and create **.csr** and **.key** file using the following command -

```cmd
openssl req -out uploadMe.csr -new -newkey rsa:2048 -nodes -keyout certificate_sandbox.key
```

2. Enter your details asked in the prompt and when asked to enter a challenge password, you can leave it as blank. You will get a **.csr** and **.key** file
3. Log in to your [Apple Developer account](https://developer.apple.com/account/resources/certificates/list), go to Identifiers and select the Merchant ID you created previously
4. Under the **Apple Pay Merchant Identity Certificate** section _(make sure you are not in the Apple Pay Payment Processing Certificate section)_, click on Create Certificate
5. Upload the **.csr** file you just created by running the command _(it would be called **uploadMe.csr** if you copy-pasted the command)_ and click on Continue
6. You will get a **.cer** file on clicking on Download _(it will probably be named **merchant\_id.cer**)_
7. You will need to convert this **.cer** file into a **.pem** file using the following command -

```cmd
openssl x509 -inform der -in merchant_id.cer -out certificate_sandbox.pem
```

**Step 4: Creating Apple Pay Payment Processing Certificate**

1. You will need to get a **.csr** file from your processor's dashboard, _(like Adyen)_
2. Upload the **.cer** file you received while creating Apple MerchantID Certificate on the processor's dashboard
3. Log in to your [Apple Developer account](https://developer.apple.com/account/resources/certificates/list), go to Identifiers and select the Merchant ID you created previously
4. Under the **Apple Pay Payment Processing Certificate** section, click on Create Certificate
5. After answering whether the Merchant ID will be processed exclusively in China mainland, click on Continue
6. Upload the **.csr** you received from your processor and click Continue

**Step 5: Configuring Apple Pay on Hyperswitch**

You can configure Apple Pay on Hyperswitch by following the steps mentioned below -

1. Login to [Hyperswitch dashboard](https://app.hyperswitch.io/)
2. In the Connectors tab, select your processor
3. While selecting Payment Methods, click on Apple Pay in the Wallet section
4. In Apple Merchant Identifier, add your identifier which you added while creating Apple MerchantID
5. In Merchant Certificate, copy the text of your **.pem** file _(it will be certificate\_sandbox.pem, if you copy-pasted the terminal command)_, and base64 encode it
6. Display Name should be Apple Pay
7. In Domain Name, add the verified domain name you configured in Merchant Domains in Apple Developer Account
8. In Merchant Private Key, copy the text of your **.key** file _(it will be certificate\_sandbox.key, if you copy-pasted the terminal command)_, and base64 encode it

**Note:** It is mandatory for you to pass the customer's billing details for Apple Pay. You can pass these details while creating payment intent as mentioned in the code snippet below -

```js
app.post("/create-payment", async (req, res) => {
  try {
    const paymentIntent = await hyper.paymentIntents.create({
      amount: 100,
      currency: "USD",
      billing_details: {
        address: {
          country: "US",
        },
      },
    });
    // Send publishable key and PaymentIntent details to client
    res.send({
      clientSecret: paymentIntent.client_secret,
    });
  } catch (err) {
    return res.status(400).send({
      error: {
        message: err.message,
      },
    });
  }
});
```

Previous{"<<"} Cards NextPay Later >>
