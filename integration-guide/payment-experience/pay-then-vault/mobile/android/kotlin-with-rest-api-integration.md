---
description: Integrate hyper SDK to your Kotlin App using hyperswitch-node
icon: k
---

# Kotlin with REST API Integration

Follow the [Server Setup](../../server-setup.md) section.&#x20;

<pre class="language-gradle"><code class="lang-gradle">hyperswitch {
    // Optional: Specify main SDK version (defaults to latest if not specified)
    sdkVersion = "<a data-footnote-ref href="#user-content-fn-1">latest_version</a>"
    
    // Optional features - only add what you need
    features = [HyperFeature.SCANCARD, HyperFeature.NETCETERA]
}
</code></pre>

Next, implement the `HyperInterface` in your `CheckoutActivity`. This involves extending `FragmentActivity` or a subclass such as `AppCompatActivity`, and implementing the `HyperInterface`:

Create a HyperswitchInstance using the publishable key and optional profile ID returned by your server:

```kotlin
hyperswitchInstance = Hyperswitch.init(
          activity = this,
          config = HyperswitchConfiguration(
              publishableKey = response.publishableKey,
              profileId = response.profileId,
          ),
      )
```

{% hint style="warning" %}
**Note**:

For an open-source setup, use the following parameters:

```kotlin
val config = HyperswitchConfiguration(
      publishableKey = response.publishableKey,
      profileId = response.profileId,
      customConfig = CustomEndpointConfiguration(
          commonEndpoint = "https://your-hyperswitch-host.example.com",
      ),
  )
```



The SDK derives the backend, logging, and asset paths from commonEndpoint. Provide the base URL without a trailing slash.

Individual endpoints can be overridden when required:

```kotlin
val config = HyperswitchConfiguration(
      publishableKey = response.publishableKey,
      profileId = response.profileId,
      customConfig = CustomEndpointConfiguration(
          overrideEndpoints = OverrideEndpoints(
              customBackendEndpoint =
                  "https://your-hyperswitch-host.example.com/api",
              customLoggingEndpoint =
                  "https://your-hyperswitch-host.example.com/api/logs/sdk",
              customAssetEndpoint =
                  "https://your-hyperswitch-host.example.com/assets/v2",
          ),
      ),
  )
```
{% endhint %}



Request your server to fetch a payment as soon as your view is loaded. Store the `sdk_authorization` returned by your server. The `PaymentSession` will use this to complete the payment process.

Initialize the payment session with the `sdk_authorization`:

```kotlin
 private fun initializePaymentSession(sdkAuthorization: String) {
      val instance = hyperswitchInstance ?: return

      lifecycleScope.launch {
          paymentSession = instance.initPaymentSession(
              PaymentSessionConfiguration(
                  sdkAuthorization = sdkAuthorization,
              ),
          )

          // The payment sheet can now be presented.
          enablePayButton()
      }
  }
```

```kotlin
private fun handlePaymentResult(result: PaymentResult) {
      when (result) {
          is PaymentResult.Completed -> {
              showMessage("Payment completed")
          }
          is PaymentResult.Canceled -> {
              showMessage("Payment cancelled")
          }
          is PaymentResult.Failed -> {
              showMessage(
                  result.throwable.message ?: "Payment failed",
              )
          }
      }
  }
```

```kotlin
private fun buildPaymentSheetConfiguration(): PaymentSheet.Configuration =
      PaymentSheet.Configuration.Builder(
          merchantDisplayName = "Example, Inc.",
      )
          .primaryButtonLabel("Pay Now")
          .allowsDelayedPaymentMethods(false)
          .allowsPaymentMethodsRequiringShippingAddress(false)
          .build()

// Present Payment Page
private fun presentPaymentSheet() {
      val session = paymentSession ?: return

      lifecycleScope.launch {
          val result = session.presentPaymentSheet(
              buildPaymentSheetConfiguration(),
          )

          handlePaymentResult(result)
      }
  }
```

## Before you begin

{% columns %}
{% column width="60%" %}
### Requirements

* Android 7.0 (API level 24) and above
* [Android Gradle Plugin](https://developer.android.com/studio/releases/gradle-plugin) 8.13+
* [Gradle](https://gradle.org/releases/) 8.13+
* [AndroidX](https://developer.android.com/jetpack/androidx/)
{% endcolumn %}

{% column width="40%" %}
{% hint style="info" %}
[**Download the demo app**](https://github.com/aashu331998/Hyperswitch-Android-Demo-App/archive/refs/heads/main.zip)

You can use this demo app as a reference with your Juspay Hyperswitch credentials to test the setup.
{% endhint %}
{% endcolumn %}
{% endcolumns %}

{% stepper %}
{% step %}
### Setup the server

[Complete the Server Setup guide](../../server-setup.md) before building the checkout page.
{% endstep %}

{% step %}
### Build checkout page on your app

#### 2.1 Add the Buildscript Classpath

To start integrating the Juspay Hyperswitch SDK, add the following classpath to the `buildscript` block of your project-level `build.gradle` file:

```gradle
buildscript {
    repositories {
        mavenCentral()
    }
    dependencies {
        classpath "io.hyperswitch:hyperswitch-gradle-plugin:$latest_version"
    }
}
```

[Check the latest plugin version](https://central.sonatype.com/artifact/io.hyperswitch/hyperswitch-gradle-plugin/versions) before adding the dependency.

#### 2.2 Add the Plugin

Add the following plugin to the `plugins` block of your app-level `build.gradle` file:

```gradle
plugins {
    // Apply Hyperswitch Plugin
    id 'io.hyperswitch.plugin'
}
```

#### 2.3 Configure the SDK

Configure the Hyperswitch SDK in your app-level `build.gradle` file. You can specify the main SDK version and enable optional features:

```gradle
hyperswitch {
    // Optional: Specify main SDK version (defaults to latest if not specified)
    sdkVersion = "1.1.5"
    
    // Optional features - only add what you need
    features = [HyperFeature.SCANCARD, HyperFeature.NETCETERA]
}
```

#### 2.4 Implement the HyperInterface

Next, implement the `HyperInterface` in your `CheckoutActivity`. This involves extending `FragmentActivity` and implementing the `HyperInterface`:

```kotlin
class CheckoutActivity : AppCompatActivity(), HyperInterface {
    // ...
}
```

#### 2.5 Setup the SDK and fetch a Payment

Set up the SDK using your publishable key. This is essential for initializing a `PaymentSession`:

```java
val paymentSession = PaymentSession(applicationContext, "YOUR_PUBLISHABLE_KEY");
```

<details>

<summary><strong>Configuration notes</strong></summary>

* If you don't specify `sdkVersion`, the plugin will automatically use the latest available version.
* You only need to enable the features you plan to use.
* Individual feature versions are optional—the plugin will use recommended compatible versions.
* `PaymentSession` is designed to work with AndroidX activities. Ensure that your `CheckoutActivity` extends `FragmentActivity` or its subclass from the AndroidX library.
* Initialize `PaymentSession` in the `onCreate` method of your `FragmentActivity`.

For an open-source setup, use the following parameters:

```kotlin
val paymentSession = PaymentSession(applicationContext, "YOUR_PUBLISHABLE_KEY", "YOUR_CUSTOM_BACKEND_URL", "YOUR_CUSTOM_LOG_URL")
```

</details>

#### 2.6 Fetch a Payment

Request your server to fetch a payment as soon as your view is loaded. Store the `client_secret` returned by your server. The `PaymentSession` will use this secret to complete the payment process.
{% endstep %}

{% step %}
### Complete the payment on your app

#### 3.1 Initialize Payment Session

Initialize the payment session with the `client_secret`:

```kotlin
paymentSession.initPaymentSession(paymentIntentClientSecret)
```

#### 3.2 Handle Payment Result

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

#### 3.3 Present the Payment Page

Create a configuration object to customize the payment sheet and present the payment page:

```kotlin
val configuration = PaymentSheet.Configuration("Your_app, Inc.")

// Present Payment Page
paymentSession.presentPaymentSheet(configuration, ::onPaymentSheetResult)
```

#### 3.4 Final Step

{% hint style="success" %}
Congratulations! You have successfully integrated the Hyperswitch Android SDK into your app. You can now customize the payment sheet to match the look and feel of your app.
{% endhint %}
{% endstep %}
{% endstepper %}

## Next steps

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Customize checkout</strong></td><td>Match the payment sheet to your Android app and brand.</td><td><a href="customization.md">customization.md</a></td></tr><tr><td><strong>Explore Android widgets</strong></td><td>Build a modular payment experience with individual widgets.</td><td><a href="widgets/">widgets</a></td></tr><tr><td><strong>Return to Android</strong></td><td>Compare the available Android integration paths.</td><td><a href="./">.</a></td></tr></tbody></table>

[^1]: [https://central.sonatype.com/artifact/io.hyperswitch/hyperswitch-sdk-android/versions](https://central.sonatype.com/artifact/io.hyperswitch/hyperswitch-sdk-android/versions)
