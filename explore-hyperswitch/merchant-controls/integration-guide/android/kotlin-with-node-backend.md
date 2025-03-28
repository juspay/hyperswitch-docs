---
description: Integrate hyper SDK to your Kotlin App using hyperswitch-node
---

# Kotlin with Node Backend

{% hint style="info" %}
In this section, you will get detailed instructions for integrating the Hyperswitch native Android SDK for your Android app
{% endhint %}

{% hint style="info" %}
Use this guide to integrate hyper SDK to your Android app. You can use this as a reference with your Hyperswitch credentials to test the setup. You can also checkout the [App on Google Play Store](https://play.google.com/store/apps/details?id=io.hyperswitch.hyperecom) to test the payment flow.
{% endhint %}

## [Demo App](https://github.com/aashu331998/Hyperswitch-Android-Demo-App/archive/refs/heads/main.zip)

## Requirements

* Android 6.0 (API level 23) and above
* [Android Gradle Plugin](https://developer.android.com/studio/releases/gradle-plugin) 8.5+
* [Gradle](https://gradle.org/releases/) 8.8+
* [AndroidX](https://developer.android.com/jetpack/androidx/)

## 1. Setup the server

### 1.1 Install the `hyperswitch-node` library

Install the package and import it in your code

```sh
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

### 2.1 Add the Buildscript Classpath

To start integrating the Hyperswitch SDK, add the following classpath to the `buildscript` block of your project-level `build.gradle` file:

<pre class="language-gradle"><code class="lang-gradle">buildscript {
    repositories {
        mavenCentral()
    }
    dependencies {
        classpath "io.hyperswitch:hyperswitch-gradle-plugin:<a data-footnote-ref href="#user-content-fn-1">$latest_version</a>"
    }
}
</code></pre>

### 2.1 Add the Buildscript Classpath

Add the following plugin to the `plugins` block of your app-level `build.gradle` file:

```gradle
plugins {
    // Apply Hyperswitch Plugin
    id 'io.hyperswitch.plugin'
}
```

### 2.3 Implement the HyperInterface

Next, implement the `HyperInterface` in your `CheckoutActivity`. This involves extending `FragmentActivity` and implementing the `HyperInterface`:

```kotlin
class CheckoutActivity : AppCompatActivity(), HyperInterface {
    // ...
}
```

{% hint style="warning" %}
**Note**:&#x20;

`PaymentSession` is designed to work with AndroidX activities. Ensure that your `CheckoutActivity` extends `FragmentActivity` or its subclass from the AndroidX library
{% endhint %}

### 2.4 Setup the SDK and fetch a Payment

Set up the SDK using your publishable key. This is essential for initializing a `PaymentSession`:

```java
val paymentSession = PaymentSession(applicationContext, "YOUR_PUBLISHABLE_KEY");
```

{% hint style="warning" %}
**Note**:&#x20;

PaymentSession needs to be initialised in onCreate method of your `FragmentActivity`
{% endhint %}

{% hint style="warning" %}
**Note**:&#x20;

For an open-source setup, use the following parameters:

```kotlin
val paymentSession = PaymentSession(applicationContext, "YOUR_PUBLISHABLE_KEY", "YOUR_CUSTOM_BACKEND_URL", "YOUR_CUSTOM_LOG_URL")
```
{% endhint %}

**Fetch a Payment**

Request your server to fetch a payment as soon as your view is loaded. Store the `client_secret` returned by your server. The `PaymentSession` will use this secret to complete the payment process.

## 3. Complete the payment on your app

**Initialise Payment Session**

Initialise the payment session with the `client_secret`:

```kotlin
paymentSession.initPaymentSession(paymentIntentClientSecret)
```

**Handle Payment Result**

Handle the payment result in the completion block. Display appropriate messages to your customer based on the outcome of the payment:

```kotlin
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

**Present the Payment Page**

Create a configuration object to customize the payment sheet and present the payment page:

```kotlin
val configuration = PaymentSheet.Configuration("Your_app, Inc.")

// Present Payment Page
paymentSession.presentPaymentSheet(configuration, ::onPaymentSheetResult)
```

#### Final Step

Congratulations! You have successfully integrated the Hyperswitch Android SDK into your app. You can now customize the payment sheet to match the look and feel of your app.

## Next step:

{% content-ref url="../../../payment-flows-and-management/quickstart/payment-methods-setup/" %}
[payment-methods-setup](../../../payment-flows-and-management/quickstart/payment-methods-setup/)
{% endcontent-ref %}

[^1]: &#x20;[Get Latest Version](https://central.sonatype.com/artifact/io.hyperswitch/hyperswitch-gradle-plugin/versions)
