---
description: Integrate Hyperswitch Lite SDK to your Kotlin App
icon: mobile-screen
---

# Lite SDK

## Key Features of Lite SDK

#### Lightweight Integration

* **Smaller artifact size**: <300 KB
* **Faster initialization**: Streamlined setup process
* **Web-based UI**: Uses web components for payment forms
* **Reduced dependencies**: Minimal impact on app size
* **Shared Configuration: The Lite SDK the same `PaymentSheet.Configuration` options as the main SDK, including:**
  * Appearance customization
  * Billing details
  * Shipping information
  * Payment method preferences
  * Branding options

## Requirements

* Android 6.0 (API level 23) and above
* [Android Gradle Plugin](https://developer.android.com/studio/releases/gradle-plugin) 8.5+
* [Gradle](https://gradle.org/releases/) 8.8+
* [AndroidX](https://developer.android.com/jetpack/androidx/)

## 1. Setup the server

Follow the [Server Setup](../../server-setup.md) section.

## 2. Build checkout page on your app

### 2.1 Add the Dependency

Add the Hyperswitch Lite SDK dependency to your app-level `build.gradle` file:

```gradle
dependencies {
    implementation 'io.hyperswitch:hyperswitch-sdk-android-lite:+'
}
```

### 2.2 Setup the Lite SDK and fetch a Payment

Set up the Lite SDK using your publishable key. This is essential for initializing a `PaymentSession`:

```kotlin
import io.hyperswitch.lite.PaymentSession

val paymentSession = PaymentSession(applicationContext, "YOUR_PUBLISHABLE_KEY")
```

{% hint style="warning" %}
**Note**:

PaymentSession needs to be initialized in onCreate method of your `FragmentActivity`
{% endhint %}

{% hint style="warning" %}
**Note**:

For an open-source setup, use the following parameters:

```kotlin
val paymentSession = PaymentSession(applicationContext, "YOUR_PUBLISHABLE_KEY", "YOUR_CUSTOM_BACKEND_URL", "YOUR_CUSTOM_LOG_URL")
```
{% endhint %}

**Fetch a Payment**

Request your server to fetch a payment as soon as your view is loaded. Store the `client_secret` returned by your server. The `PaymentSession` (Lite) will use this secret to complete the payment process.

## 3. Complete the payment on your app

**Initialize Payment Session**

Initialize the payment session with the `client_secret`:

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

// Present Payment Page (Lite SDK)
paymentSession.presentPaymentSheet(configuration, ::onPaymentSheetResult)
```

#### Final Step

Congratulations! You have successfully integrated the Hyperswitch Lite SDK into your app. The Lite SDK provides the same powerful payment processing capabilities with a smaller footprint, making it ideal for apps where bundle size is a concern.

## Next step:

{% content-ref url="../../../../payment-orchestration/quickstart/payment-methods-setup/" %}
[payment-methods-setup](../../../../payment-orchestration/quickstart/payment-methods-setup/)
{% endcontent-ref %}
