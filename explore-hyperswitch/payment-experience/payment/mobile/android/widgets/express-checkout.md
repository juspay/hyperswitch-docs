---
icon: cart-shopping-fast
---

# Express Checkout

**Purpose:** One click solution for last used saved payment method

**Add Express Checkout Widget to Layout**

```xml
<io.hyperswitch.view.BasePaymentWidget
    android:id="@+id/expressCheckoutWidget"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    app:paymentMethod="expressCheckout" />

<Button
    android:id="@+id/confirmEC"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:text="Confirm EC" />
```

**Initialize Express Checkout Launcher**

```kotlin
private lateinit var ecLauncherInstance: UnifiedPaymentLauncher

private fun setupECLauncher() {
    ecLauncherInstance = UnifiedPaymentLauncher.createExpressCheckoutLauncher(
        activity = this,
        clientSecret = paymentIntentClientSecret,
        readyCallback = ::onExpressCheckoutReady,
        resultCallback = ::onExpressCheckoutResult
    )

    findViewById<View>(R.id.confirmEC).setOnClickListener {
        if (::ecLauncherInstance.isInitialized) {
            ecLauncherInstance.presentForPayment(paymentIntentClientSecret)
        } else {
            Toast.makeText(this, "Express Checkout Launcher not initialized", Toast.LENGTH_SHORT).show()
        }
    }
}
```

**Handle Express Checkout Callbacks**

```kotlin
private fun onExpressCheckoutReady(isReady: Boolean) {
    findViewById<View>(R.id.confirmEC).isEnabled = isReady
}

private fun onExpressCheckoutResult(result: ExpressCheckoutPaymentMethodLauncher.Result) {
    when (result) {
        is ExpressCheckoutPaymentMethodLauncher.Result.Completed -> {
            Toast.makeText(this, "Express checkout successful: ${result.paymentMethod}", Toast.LENGTH_LONG).show()
        }
        is ExpressCheckoutPaymentMethodLauncher.Result.Canceled -> {
            Toast.makeText(this, "Express checkout canceled: ${result.data}", Toast.LENGTH_LONG).show()
        }
        is ExpressCheckoutPaymentMethodLauncher.Result.Failed -> {
            Toast.makeText(this, "Express checkout failed: ${result.error.message}", Toast.LENGTH_LONG).show()
        }
    }
}
```

