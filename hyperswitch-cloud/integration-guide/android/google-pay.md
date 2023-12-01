---
description: Accept a payment using Google Pay in your Android app
---

# Google Pay

With Google Pay, customers can conveniently make payments within your app or website using credit or debit cards saved in their Google Account. This includes cards from various sources, such as Google Play, YouTube, Chrome, or any Android device. By utilizing the Google Pay API, you can request access to any credit or debit card stored in your customer's Google account.

Google Pay seamlessly integrates with Hyperswitch, providing you with the flexibility to replace conventional payment forms whenever it is feasible and appropriate.

**Accept a payment using Google Pay in your Android app**

The Hyperswitch Android SDK includes GooglePay, which offers the quickest and most straightforward method to initiate Google Pay acceptance in your Android applications.

## Enable Google Pay in CheckoutActivity.kt

Enable Google Pay by passing a PaymentSheet.GooglePayConfiguration object with the Google Pay environment (production or test) along with the country code of your business and currency code when initializing PaymentSheet.Configuration.

```java
val configuration = PaymentSheet.Configuration.Builder("Hyperswitch, Inc.")
.appearance(appearance)
.googlePay(PaymentSheet.GooglePayConfiguration(
    PaymentSheet.GooglePayConfiguration.Environment.Test, "US", "USD"))
.build()
```
