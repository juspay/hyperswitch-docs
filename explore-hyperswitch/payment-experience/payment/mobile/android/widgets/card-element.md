---
icon: credit-card
---

# Card Element

**Purpose:** Card payments

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
        Toast.makeText(this, "SDK is not initialised", Toast.LENGTH_SHORT).show()
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

## 5. Best Practices

### 5.1 Error Handling

Always check if launchers are initialized before using them:

```kotlin
if (::cardPaymentLauncher.isInitialized) {
    cardPaymentLauncher.confirmCardPayment(confirmParams)
} else {
    Toast.makeText(this, "SDK is not initialised", Toast.LENGTH_SHORT).show()
}
```

