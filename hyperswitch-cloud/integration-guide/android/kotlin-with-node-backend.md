---
description: Integrate hyper SDK to your Kotlin App using hyperswitch-node
---

# Kotlin with Node Backend

Use this guide to integrate hyper SDK to your Android app. You can use this as a reference with your Hyperswitch credentials to test the setup. You can also checkout the [App on Google Play Store](https://play.google.com/store/apps/details?id=io.hyperswitch.hyperecom) to test the payment flow.

## [Demo App](https://github.com/aashu331998/Hyperswitch-Android-Demo-App/archive/refs/heads/main.zip)

## Requirements

* Android 5.0 (API level 21) and above
* [Android Gradle Plugin](https://developer.android.com/studio/releases/gradle-plugin) 7.3.1
* [Gradle](https://gradle.org/releases/) 7.5.1+
* [AndroidX](https://developer.android.com/jetpack/androidx/)

## 1. Setup the server

### 1.1 Install the `hyperswitch-node` library

Install the package and import it in your code

```js
$ npm install @juspay-tech/hyperswitch-node
```

### 1.2 Create a payment

Before creating a payment, import the `hyperswitch-node` dependencies and initialize it with your API key.

```js
const hyper = require("@juspay-tech/hyperwitch-node")(‘YOUR_API_KEY’);
```

Add an endpoint on your server that creates a Payment. Creating a Payment helps to establish the intent of the customer to start a payment. It also helps to track the customer’s payment lifecycle, keeping track of failed payment attempts and ensuring the customer is only charged once. Return the `client_secret` obtained in the response to securely complete the payment on the client.

```js
// Create a Payment with the order amount and currency
app.post("/create-payment", async (req, res) => {
  try {
    const paymentIntent = await hyper.paymentIntents.create({
      currency: "USD",
      amount: 100,
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

## 2. Build checkout page on your app

### 2.1 Configure your repository with Hyperswitch dependency

Add the following maven repository to the settings.gradle file

```js
dependencyResolutionManagement {
    repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
    repositories {
        google()
        mavenCentral()
           maven {
            url "https://maven.hyperswitch.io/release/production"
        }
    }
}
```

### 2.2 Add the Hyperswitch dependency

Add hyperswitch-android to the dependencies block of your build.gradle file to install the SDK

```js
dependencies {

    // Hyperswitch Android SDK
    implementation 'io.hyperswitch:hyperswitch-android:+'
}
```

### 2.3 Implement the HyperInterface

Implement the HyperInterface to your CheckoutActivity

```js
class CheckoutActivity : AppCompatActivity(), HyperInterface {

    // ...
}

```

### 2.4 Setup the SDK and fetch a Payment

Setup the SDK with your publishable key

```js
PaymentConfiguration.init(applicationContext, "YOUR_PUBLISHABLE_KEY");
```

Fetch a payment by requesting your server for a payment as soon as your view is loaded. Store a reference to the `client_secret` returned by the server; the Payment Sheet will use this secret to complete the payment later.

## 3. Complete the payment on your app

Create a PaymentSheet instance using the `client_secret` retrieved from the previous step. Present the payment page from your view controller and use the PaymentSheet.Configuration struct for customising your payment page.

```js
val configuration = PaymentSheet.Configuration("Your_app, Inc.")

// Present Payment Page
paymentSheet.presentWithPaymentIntent(paymentIntentClientSecret, configuration)
```

Handle the payment result in the completion block and display appropriate messages to your customer based on whether the payment fails with an error or succeeds.

```js
private fun onPaymentSheetResult(paymentResult: PaymentSheetResult) {
        when (paymentResult) {
            is PaymentSheetResult.Completed -> {
                showToast("Payment complete!")
            }
            is PaymentSheetResult.Canceled -> {
                Log.i(TAG, "Payment canceled!")
            }
            is PaymentSheetResult.Failed -> {
                showAlert("Payment failed", paymentResult.error.localizedMessage)
            }
        }
    }
```
