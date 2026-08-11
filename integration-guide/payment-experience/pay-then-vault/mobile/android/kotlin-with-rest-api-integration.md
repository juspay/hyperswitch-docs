---
description: Integrate hyper SDK to your Kotlin App using hyperswitch-node
icon: k
---

# Kotlin with REST API Integration

<details>

<summary><a href="https://github.com/aashu331998/Hyperswitch-Android-Demo-App/archive/refs/heads/main.zip"><strong>Demo App</strong></a></summary>

You can use this demo app as a reference with your Juspay Hyperswitch credentials to test the setup.

</details>

#### Requirements

* Android 7.0 (API level 24) and above
* [Android Gradle Plugin](https://developer.android.com/studio/releases/gradle-plugin) 8.13+
* [Gradle](https://gradle.org/releases/) 8.13+
* [AndroidX](https://developer.android.com/jetpack/androidx/)

#### 1. Setup the server

Follow the [Server Setup](../../server-setup.md) section.&#x20;

#### 2. Build checkout page on your app

**2.1 Add the Buildscript Classpath**

To start integrating the Juspay Hyperswitch SDK, add the following classpath to the `buildscript` block of your project-level `build.gradle` file:

<pre class="language-gradle"><code class="lang-gradle">buildscript {
    repositories {
        mavenCentral()
    }
    dependencies {
        classpath "io.hyperswitch:hyperswitch-gradle-plugin:<a data-footnote-ref href="#user-content-fn-1">$latest_version</a>"
    }
}
</code></pre>

**2.2 Add the Plugin**

Add the following plugin to the `plugins` block of your app-level `build.gradle` file:

```gradle
plugins {
    // Apply Hyperswitch Plugin
    id 'io.hyperswitch.plugin'
}
```

**2.3 Configure the SDK**

Configure the Hyperswitch SDK in your app-level `build.gradle` file. You can specify the main SDK version and enable optional features:

<pre class="language-gradle"><code class="lang-gradle">hyperswitch {
    // Optional: Specify main SDK version (defaults to latest if not specified)
    sdkVersion = "<a data-footnote-ref href="#user-content-fn-2">latest_version</a>"
    
    // Optional features - only add what you need
    features = [HyperFeature.SCANCARD, HyperFeature.NETCETERA]
}
</code></pre>

{% hint style="warning" %}
Note:

* If you don't specify `sdkVersion`, the plugin will automatically use the latest available version
* You only need to enable the features you plan to use
* Individual feature versions are optional - the plugin will use recommended compatible versions
{% endhint %}

**2.4 Implement the HyperInterface**

Next, implement the `HyperInterface` in your `CheckoutActivity`. This involves extending `FragmentActivity` or a subclass such as `AppCompatActivity`, and implementing the `HyperInterface`:

```kotlin
class CheckoutActivity : AppCompatActivity(), HyperInterface {
    // ...
}
```

{% hint style="warning" %}
**Note**:

`PaymentSession` is designed to work with AndroidX activities. Ensure that your `CheckoutActivity` extends `FragmentActivity` or its subclass from the AndroidX library
{% endhint %}

**2.5 Setup the SDK and fetch a Payment**

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



**Fetch a Payment**

Request your server to fetch a payment as soon as your view is loaded. Store the `sdk_authorization` returned by your server. The `PaymentSession` will use this to complete the payment process.

#### 3. Complete the payment on your app

**Initialize Payment Session**

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

**Handle Payment Result**

Handle the payment result in the completion block. Display appropriate messages to your customer based on the outcome of the payment:

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

{% hint style="danger" %}
Please retrieve the payment status from the Hyperswitch backend to get the terminal status of the payment. Do not rely solely on the status returned by the SDK, as it may not always reflect the final state of the transaction.
{% endhint %}

**Present the Payment Page**

Create a configuration object to customize the payment sheet and present the payment page:

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

**Final Step**

Congratulations! You have successfully integrated the Hyperswitch Android SDK into your app. You can now customize the payment sheet to match the look and feel of your app.

#### Next Step:

[^1]: [Get Latest Version](https://central.sonatype.com/artifact/io.hyperswitch/hyperswitch-gradle-plugin/versions)

[^2]: [https://central.sonatype.com/artifact/io.hyperswitch/hyperswitch-sdk-android/versions](https://central.sonatype.com/artifact/io.hyperswitch/hyperswitch-sdk-android/versions)
