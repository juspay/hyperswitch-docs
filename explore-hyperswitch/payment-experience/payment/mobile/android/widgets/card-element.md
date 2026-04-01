---
description: Learn how to integrate the Card Element widget for accepting card payments in your Android app using Juspay Hyperswitch SDK.
icon: credit-card
---

# Card Element

**Purpose:** Card payments with Juspay Hyperswitch

**Add Card Widget to Layout**

```xml
<io.hyperswitch.view.BasePaymentWidget
    android:id="@+id/cardElement"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    app:paymentMethod="card" />

<Button
    android:id="@+id/confirmButton"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:text="Pay with Card" />
```

**Initialize Card Launcher**

```kotlin
private lateinit var cardPaymentLauncher: UnifiedPaymentLauncher

private fun setupCardPayment() {
    cardPaymentLauncher = UnifiedPaymentLauncher.createCardLauncher(
        activity = this,
        resultCallback = ::onPaymentResult
    )
}
```

**Handle Card Payment**

```kotlin
private fun processCardPayment() {
    val cardInputWidget: BasePaymentWidget = findViewById(R.id.cardElement)
    val params: PaymentMethodCreateParams = cardInputWidget.paymentMethodCreateParams
    val confirmParams = ConfirmPaymentIntentParams.createWithPaymentMethodCreateParams(
        params,
        paymentIntentClientSecret
    )

    if (::cardPaymentLauncher.isInitialized) {
        cardPaymentLauncher.confirmCardPayment(confirmParams)
    } else {
        Toast.makeText(this, "SDK is not initialized", Toast.LENGTH_SHORT).show()
    }
}

// Handle card payment results
private fun onPaymentResult(paymentResult: PaymentResult) {
    when (paymentResult) {
        is PaymentResult.Completed -> {
            Toast.makeText(this, "Payment completed: ${paymentResult.data}", Toast.LENGTH_SHORT).show()
        }
        is PaymentResult.Canceled -> {
            Toast.makeText(this, "Payment canceled: ${paymentResult.data}", Toast.LENGTH_SHORT).show()
        }
        is PaymentResult.Failed -> {
            Toast.makeText(this, "Payment failed: ${paymentResult.throwable.message}", Toast.LENGTH_SHORT).show()
        }
    }
}
```

## Best Practices

### Error Handling

Always check if launchers are initialized before using them:

```kotlin
if (::cardPaymentLauncher.isInitialized) {
    cardPaymentLauncher.confirmCardPayment(confirmParams)
} else {
    Toast.makeText(this, "SDK is not initialized", Toast.LENGTH_SHORT).show()
}
```
