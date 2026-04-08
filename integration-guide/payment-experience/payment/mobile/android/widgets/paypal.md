---
description: >-
  Learn how to integrate the PayPal widget for accepting PayPal payments in your
  Android app using Juspay Hyperswitch SDK.
icon: paypal
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/kf7BGdsPkCw9nalhAIlE/integration-guide/payment-experience/payment/mobile/android/widgets/paypal
---

# PayPal

PayPal payments with Juspay Hyperswitch.

### Add PayPal Widget to Layout

```xml
<io.hyperswitch.view.BasePaymentWidget
    android:id="@+id/payPalButton"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    app:paymentMethod="paypal" />
```

### Initialize PayPal Launcher

```kotlin
private lateinit var payPalButton: BasePaymentWidget
private lateinit var payPalLauncherInstance: UnifiedPaymentLauncher

private fun setupPayPalLauncher() {
    payPalButton = findViewById(R.id.payPalButton)
    payPalButton.isEnabled = false
    
    payPalLauncherInstance = UnifiedPaymentLauncher.createPayPalLauncher(
        activity = this,
        clientSecret = paymentIntentClientSecret,
        readyCallback = ::onPayPalReady,
        resultCallback = ::onPayPalResult
    )

    payPalButton.setOnClickListener {
        if (::payPalLauncherInstance.isInitialized) {
            payPalLauncherInstance.presentForPayment(paymentIntentClientSecret)
        } else {
            Toast.makeText(this, "PayPal Launcher not initialized", Toast.LENGTH_SHORT).show()
        }
    }
}
```

### Handle PayPal Callbacks

```kotlin
private fun onPayPalReady(isReady: Boolean) {
    payPalButton.isEnabled = isReady
}

private fun onPayPalResult(result: PayPalPaymentMethodLauncher.Result) {
    when (result) {
        is PayPalPaymentMethodLauncher.Result.Completed -> {
            val paymentMethodId = result.paymentMethod.id
            Toast.makeText(this, "PayPal payment successful: $paymentMethodId", Toast.LENGTH_LONG).show()
        }
        is PayPalPaymentMethodLauncher.Result.Canceled -> {
            Toast.makeText(this, "PayPal payment canceled: ${result.data}", Toast.LENGTH_LONG).show()
        }
        is PayPalPaymentMethodLauncher.Result.Failed -> {
            Toast.makeText(this, "PayPal payment failed: ${result.error.message}", Toast.LENGTH_LONG).show()
        }
    }
}
```
