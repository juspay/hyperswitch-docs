---
name: hyperswitch-docs-mobile-sdk
description: Use this skill when the user asks about "Hyperswitch Android SDK", "Hyperswitch iOS SDK", "mobile payment integration", "Kotlin Hyperswitch", "Swift Hyperswitch", "React Native Hyperswitch", "Flutter Hyperswitch", "HyperCheckout mobile", "mobile SDK setup", "Android payment element", "iOS payment sheet", or needs to integrate Hyperswitch payments into a native mobile app.
version: 1.0.0
tags: [hyperswitch, docs, mobile, android, ios, kotlin, swift, react-native, flutter]
---

# Mobile SDK Integration

## Overview

Hyperswitch provides native SDKs for Android (Kotlin) and iOS (Swift), plus cross-platform support via React Native and Flutter. All mobile integrations follow the same pattern: server creates a payment → returns `client_secret` → mobile SDK completes checkout.

## Doc References

| Platform | Doc Path |
|----------|----------|
| Android (Kotlin) | `explore-hyperswitch/payment-experience/payment/mobile/android/kotlin-with-rest-api-integration.md` |
| iOS (Swift) | `explore-hyperswitch/payment-experience/payment/mobile/ios/` |
| React Native | `explore-hyperswitch/payment-experience/payment/mobile/react-native/` |
| Flutter | `explore-hyperswitch/payment-experience/payment/mobile/flutter/` |
| Android Lite SDK | `explore-hyperswitch/payment-experience/payment/mobile/android/lite-sdk.md` |

---

## Android (Kotlin)

### Install

```kotlin
// build.gradle (app)
dependencies {
    implementation("io.hyperswitch:hyperswitch-sdk-android:<latest_version>")
}
```

### Usage

```kotlin
// 1. Fetch client_secret from your server
val clientSecret = fetchClientSecretFromServer()

// 2. Initialise HyperCheckout
val paymentSheet = PaymentSheet(this, ::onPaymentResult)

// 3. Present the payment sheet
paymentSheet.presentWithPaymentIntent(
    clientSecret,
    PaymentSheet.Configuration(
        merchantDisplayName = "Your Store",
        appearance = PaymentSheet.Appearance(/* custom theme */)
    )
)

// 4. Handle result
private fun onPaymentResult(result: PaymentSheetResult) {
    when (result) {
        is PaymentSheetResult.Completed -> { /* fulfill order */ }
        is PaymentSheetResult.Canceled  -> { /* user dismissed */ }
        is PaymentSheetResult.Failed    -> { /* show error */ }
    }
}
```

### Android Widgets

For custom UI (individual elements rather than the full sheet):

- **Card Element** — `explore-hyperswitch/payment-experience/payment/mobile/android/widgets/card-element.md`
- **Google Pay** — `explore-hyperswitch/payment-experience/payment/mobile/android/widgets/google-pay.md`
- **PayPal** — `explore-hyperswitch/payment-experience/payment/mobile/android/widgets/paypal.md`
- **Express Checkout** — `explore-hyperswitch/payment-experience/payment/mobile/android/widgets/express-checkout.md`

---

## Server Setup (Common to All Mobile Platforms)

Your server endpoint is the same regardless of mobile platform:

```javascript
// POST /create-payment
const payment = await fetch('https://sandbox.hyperswitch.io/payments', {
  method: 'POST',
  headers: { 'api-key': process.env.HYPERSWITCH_SECRET_KEY, 'Content-Type': 'application/json' },
  body: JSON.stringify({
    amount: 1000,
    currency: 'USD',
    confirm: false,
    return_url: 'yourapp://payment/complete',  // deep link for mobile
  }),
}).then(r => r.json());

return { clientSecret: payment.client_secret };
```

Note: `return_url` should be a deep link (custom URL scheme) for mobile apps. Configure it in your app's URL scheme settings.

---

## React Native

```bash
npm install @juspay-tech/hyper-sdk-react
```

```jsx
import HyperSdk from '@juspay-tech/hyper-sdk-react';

const clientSecret = await fetchFromServer();

await HyperSdk.initPaymentSession({ clientSecret });
const result = await HyperSdk.presentPaymentSheet();

if (result.status === 'success') {
  // order fulfilled
}
```

---

## Key Differences vs Web SDK

| Aspect | Web | Mobile |
|--------|-----|--------|
| `return_url` | HTTPS URL | Deep link (`yourapp://...`) |
| 3DS | Browser redirect | In-app WebView (handled by SDK) |
| Apple Pay | Safari only | Native iOS (requires entitlement) |
| Google Pay | Chrome/Android | Native Android |
| Customization | CSS variables | `PaymentSheet.Appearance` API |

---

## Production Tips

- Register your deep link URL scheme in the app manifest before testing 3DS — without it, the post-3DS redirect fails silently.
- Test on real devices, not just emulators — Apple Pay and NFC-based methods don't work in simulators.
- Use the Lite SDK (`android/lite-sdk.md`) if you want a minimal footprint with just card input; it omits wallets and APMs.
- For Android: add `<uses-permission android:name="android.permission.INTERNET"/>` to your manifest.
