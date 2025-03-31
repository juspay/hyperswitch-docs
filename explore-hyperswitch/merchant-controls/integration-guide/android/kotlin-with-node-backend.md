---
description: Integrate hyper SDK to your Kotlin App using hyperswitch-node
---

# Kotlin with Node Backend

## [Demo App](https://github.com/aashu331998/Hyperswitch-Android-Demo-App/archive/refs/heads/main.zip)

## Requirements

* Android 6.0 (API level 23) and above
* [Android Gradle Plugin](https://developer.android.com/studio/releases/gradle-plugin) 8.5+
* [Gradle](https://gradle.org/releases/) 8.8+
* [AndroidX](https://developer.android.com/jetpack/androidx/)

## 1. Setup the server

```js
$ npm install @juspay-tech/hyperswitch-node
```

Follow the [Server Setup](../web/server-setup.md) section.

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

{% hint style="danger" %}
Please retrieve the payment status from the Hyperswitch backend to get the terminal status of the payment. Do not rely solely on the status returned by the SDK, as it may not always reflect the final state of the transaction.
{% endhint %}

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
