---
description: Enable Apple pay on your iOS app
---

# iOS Application

## **Prerequisites**

Before beginning to integrate Apple Pay with Hyperswitch, below prerequisites need to be fulfilled. _Please feel free to reach out to Hyperswitch support if you are stuck at any stage when integrating and testing Apple Pay._

1. Apple Pay requires an Apple Developer Account. You can [Sign Up](https://developer.apple.com/programs/enroll/) for one here.
2. You must have a valid SSL certificate on your domain _(meaning it begins with **https**)_

Apple Pay requires additional steps, and requires macOS 10.12.1+ or iOS 10.1+. Follow the steps given below to setting up Apple Pay -

## **Creating an Apple MerchantID**

You can create an Apple MerchantID referencing the video or following the steps mentioned below&#x20;

* Log in to your [Apple Developer account](https://developer.apple.com/account/resources/certificates/list)
* Go to the [add MerchantIDs section](https://developer.apple.com/account/resources/identifiers/add/merchant), select Merchant IDs and click Continue
* Add a useful description _(like merchant id for test environment)_
* Enter a unique descriptive identifier _(like merchant.com.testdomain.sandbox)_ and click Continue
* Verify the description and identifier and click on Register

## **Validating Merchant Domain**

You can validate the merchant domain by following the steps mentioned below -

* Log in to your [Apple Developer account](https://developer.apple.com/account/resources/certificates/list), go to Identifiers and select the Merchant ID you created previously
* Under the Merchant Domains section, click on **Add Domain**
* Enter your _merchant\_domain_ as domain and click on Save
* Click on Download and a **.txt** file will be downloaded
* Host this file on _merchant\_domain_/.well-known/apple-developer-merchantid-domain-association.txt
* Once you host the .txt file in the path mentioned above, click on Verify
* Make sure the status is verified as shown in the following image

## **Creating Apple MerchantID Certificate and Private Key**

You can create an Apple MerchantID certificate and private key referencing the video below or following the steps mentioned below -

\
Your browser does not support the video tag.

**Note:** It is recommended that you keep all the generated files in the same workspace for the sake of simplicity

* Open a terminal and create **.csr** and **.key** file using the following command -

```cmd
openssl req -out uploadMe.csr -new -newkey rsa:2048 -nodes -keyout certificate_sandbox.key
```

* Enter your details asked in the prompt and when asked to enter a challenge password, you can leave it as blank. You will get a **.csr** and **.key** file
* Log in to your [Apple Developer account](https://developer.apple.com/account/resources/certificates/list), go to Identifiers and select the Merchant ID you created previously
* Under the **Apple Pay Merchant Identity Certificate** section _(make sure you are not in the Apple Pay Payment Processing Certificate section)_, click on Create Certificate
* Upload the **.csr** file you just created by running the command _(it would be called **uploadMe.csr** if you copy-pasted the command)_ and click on Continue
* You will get a **.cer** file on clicking on Download _(it will probably be named **merchant\_id.cer**)_
* You will need to convert this **.cer** file into a **.pem** file using the following command -

```cmd
openssl x509 -inform der -in merchant_id.cer -out certificate_sandbox.pem
```

## **Creating Apple Pay Payment Processing Certificate**

* You will need to get a **.csr** file from your processor's dashboard, _(like Adyen)_
* Upload the **.cer** file you received while creating Apple MerchantID Certificate on the processor's dashboard
* Log in to your [Apple Developer account](https://developer.apple.com/account/resources/certificates/list), go to Identifiers and select the Merchant ID you created previously
* Under the **Apple Pay Payment Processing Certificate** section, click on Create Certificate
* After answering whether the Merchant ID will be processed exclusively in China mainland, click on Continue
* Upload the **.csr** you received from your processor and click Continue

## **Configuring Apple Pay on Hyperswitch**

You can configure Apple Pay on Hyperswitch by following the steps mentioned below -

* Login to [Hyperswitch dashboard](https://app.hyperswitch.io/)
* In the Connectors tab, select your processor
* While selecting Payment Methods, click on Apple Pay in the Wallet section
* Select the iOS Certificate option

<figure><img src="../../../../.gitbook/assets/Screenshot 2023-12-07 at 7.40.48 PM.png" alt="" width="563"><figcaption></figcaption></figure>

* In Apple Merchant Identifier, add your identifier which you added while creating Apple MerchantID
* In Merchant Certificate, copy the text of your **.pem** file _(it will be certificate\_sandbox.pem, if you copy-pasted the terminal command)_, and base64 encode it
* Display Name should be Apple Pay
* In Domain Name, add the verified domain name you configured in Merchant Domains in Apple Developer Account
* In Merchant Private Key, copy the text of your **.key** file _(it will be certificate\_sandbox.key, if you copy-pasted the terminal command)_, and base64 encode it

<figure><img src="../../../../.gitbook/assets/Screenshot 2023-12-07 at 7.42.00 PM.png" alt="" width="563"><figcaption></figcaption></figure>

**Note:** It is mandatory for you to pass the customer's billing details for Apple Pay. You can pass these details while creating payment intent as mentioned in the code snippet below -

```javascript
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
