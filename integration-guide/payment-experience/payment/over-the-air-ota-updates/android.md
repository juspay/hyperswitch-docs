---
description: >-
  Configure over-the-air updates for Hyperswitch SDK on Android using
  HyperOTAReact for seamless app updates without store releases.
icon: android
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/kf7BGdsPkCw9nalhAIlE/integration-guide/payment-experience/payment/over-the-air-ota-updates/android
---

# Android

Juspay Hyperswitch provides over-the-air (OTA) updates for Android apps, enabling you to push updates without app store releases.

### Configuration

1. When initializing `HyperOTAReact`, ensure the **release config URL** (ending in `config.json`) is set for the correct **environment** (Sandbox or Production) and **version**. This is where HyperOTA will check for updates during app startup.

Example:

```kotlin
HyperOTAReact(
    context.applicationContext,
    "hyperswitch", // appId
    "hyperswitch.bundle", // bundle name
    BuildConfig.VERSION_NAME, // app version
    hyperOTAUrl, // release config URL
    headers,
    object : LazyDownloadCallback {
        override fun fileInstalled(filePath: String, success: Boolean) {}
        override fun lazySplitsInstalled(success: Boolean) {}
    },
    tracker
).also { hyperOTAServices = it }
```

{% hint style="info" %}
Replace `hyperOTAUrl` with your environment-specific endpoint.

`Example: $baseURL/mobile-ota/android/${BuildConfig.VERSION_NAME}/config.json`
{% endhint %}

2. In your `MainApplication` class, ensure `getJSBundleFile()` uses the bundle path from HyperOTA and falls back to the default asset if necessary

```kotlin
override fun getJSBundleFile(): String {
    return try {
        return hyperOTAServices?.getBundlePath() ?: "assets://hyperswitch.bundle"
    } catch (e: Exception) {
         return "assets://hyperswitch.bundle"
    }
}
```

For more information, see [Airborne](https://github.com/juspay/airborne).
