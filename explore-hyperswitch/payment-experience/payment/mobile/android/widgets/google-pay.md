---
description: Learn how to integrate the Google Pay widget for accepting Google Pay payments in your Android app using Juspay Hyperswitch SDK.
icon: google
---

# Google Pay

**Purpose:** Google Pay payments with Juspay Hyperswitch

**Add Google Pay Widget to Layout**

```xml
<io.hyperswitch.view.BasePaymentWidget
    android:id="@+id/googlePayButton"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    app:paymentMethod="google_pay" />
```

**Initialize Google Pay Launcher**

```kotlin
private lateinit var googlePayButton: BasePaymentWidget
private lateinit var googlePayLauncherInstance: UnifiedPaymentLauncher

private fun setupGooglePayLauncher() {
    googlePayButton = findViewById(R.id.googlePayButton)
    googlePayButton.isEnabled = false
    
    googlePayLauncherInstance = UnifiedPaymentLauncher.createGooglePayLauncher(
        activity = this,
        clientSecret = paymentIntentClientSecret,
        config = GooglePayConfig(
            environment = GooglePayEnvironment.Test, // Use GooglePayEnvironment.Production for live
            merchantCountryCode = "US",
            merchantName = "Your Store Name"
        ),
        readyCallback = ::onGooglePayReady,
        resultCallback = ::onGooglePayResult
    )

    googlePayButton.setOnClickListener {
        if (::googlePayLauncherInstance.isInitialized) {
            googlePayLauncherInstance.presentForPayment(paymentIntentClientSecret)
        } else {
            Toast.makeText(this, "Google Pay Launcher not initialized", Toast.LENGTH_SHORT).show()
        }
    }
}
```

**Handle Google Pay Callbacks**

```kotlin
private fun onGooglePayReady(isReady: Boolean) {
    googlePayButton.isEnabled = isReady
}

private fun onGooglePayResult(result: GooglePayPaymentMethodLauncher.Result) {
    when (result) {
        is GooglePayPaymentMethodLauncher.Result.Completed -> {
            val paymentMethodId = result.paymentMethod.id
            Toast.makeText(this, "Payment successful: $paymentMethodId", Toast.LENGTH_LONG).show()
        }
        is GooglePayPaymentMethodLauncher.Result.Canceled -> {
            Toast.makeText(this, "Payment canceled: ${result.data}", Toast.LENGTH_LONG).show()
        }
        is GooglePayPaymentMethodLauncher.Result.Failed -> {
            Toast.makeText(this, "Payment failed: ${result.error.message}", Toast.LENGTH_LONG).show()
        }
    }
}
```

## Best Practices

### UI State Management

Disable payment buttons until launchers are ready:

```kotlin
private fun onGooglePayReady(isReady: Boolean) {
    googlePayButton.isEnabled = isReady
}
```
