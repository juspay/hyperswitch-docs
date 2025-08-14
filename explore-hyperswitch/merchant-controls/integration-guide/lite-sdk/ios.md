---
description: Integrate Hyperswitch Lite SDK to your IOS App
---

# IOS

## Key Features of Lite SDK

#### Lightweight Integration

* **Smaller bundle size**: 282.84 KB
* **Faster initialization**: Streamlined setup process
* **Web-based UI**: Uses web components for payment forms
* **Reduced dependencies**: Minimal impact on app size
* **Shared Configuration: The Lite SDK  uses the same `PaymentSession` options as the main SDK, including:**
  * Appearance customization
  * Billing details
  * Shipping information
  * Payment method preferences
  * Branding options

## Requirements

* IOS 13.4+
* Cocoa Pods​

## 1. Setup the server

Follow the [Server Setup](../web/server-setup.md) section.

### 2. Build Checkout in Your App

#### 2.1 Add the Dependency

In your **`Podfile`**:

**Lite SDK only**

```ruby
pod 'hyperswitch-sdk-ios/lite', 'Latest_version'
```

**Lite SDK with Scan Card functionality**

```ruby
pod 'hyperswitch-sdk-ios/lite+scancard', 'Latest_version'
```

> **Note:** The Lite SDK and the regular SDK share a codebase. Their versions **must** match at all times.\
> Replace `Latest_version` with the actual version number.

#### 2.2 Setup the Lite SDK and Fetch a Payment

**Initialize PaymentSession:**

```swift
let paymentSession = PaymentSession()

// Initialize with client secret
paymentSession.initPaymentSession(paymentIntentClientSecret: "your_client_secret_here")
```

**Complete Payment**

```swift
// Present the PaymentSheet Lite
paymentSession.presentPaymentSheetLite(
    viewController: self,
    configuration: configuration
) { result in
    switch result {
    case .completed(let data):
        print("Payment completed: \(data)")
        // Handle successful payment

    case .canceled(let data):
        print("Payment canceled: \(data)")
        // Handle cancellation

    case .failed(let error):
        print("Payment failed: \(error)")
        // Handle error
    }
}
```

**Final Step**

You have successfully integrated the **Hyperswitch Lite SDK** into your iOS app.\
The Lite SDK delivers **full payment processing** capabilities with a **smaller footprint**, perfect for apps where bundle size matters.
