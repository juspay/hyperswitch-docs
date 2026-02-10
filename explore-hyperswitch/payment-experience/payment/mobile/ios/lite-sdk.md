---
icon: mobile-screen
---

# Lite SDK

## Key Features of Lite SDK

#### Lightweight Integration

* **Smaller artifact size**: <300 KB
* **Faster initialization**: Streamlined setup process
* **Web-based UI**: Uses web components for payment forms
* **Reduced dependencies**: Minimal impact on app size
* **Shared Configuration: The Lite SDK uses the same `PaymentSession` options as the main SDK, including:**
  * Appearance customization
  * Billing details
  * Shipping information
  * Payment method preferences
  * Branding options

## Requirements

* IOS 15.1+
* Cocoapods​

## 1. Setup the server

Follow the [Server Setup](../../server-setup.md) section.

### 2. Build Checkout in Your App

#### 2.1 Add the Dependency

In your **`Podfile`**:

**Lite SDK only**

```ruby
pod 'hyperswitch-sdk-ios-lite'
```

**Lite SDK with Scan Card functionality**

```ruby
pod 'hyperswitch-sdk-ios-lite/scancard'
```

> **Note:** The Lite SDK and the regular SDK share a codebase. Their versions **must** match at all times.\
> Replace `Latest_version` with the actual version number.

#### 2.2 Setup the Lite SDK and Fetch a Payment

**Initialize PaymentSession:**

```swift
import HyperswitchLite
paymentSession = PaymentSession(publishableKey: <YOUR_PUBLISHABLE_KEY>)

// Initialize with client secret
paymentSession.initPaymentSession(paymentIntentClientSecret: paymentIntentClientSecret)
```

**Complete Payment**

```swift
// Present the PaymentSheet Lite
paymentSession.presentPaymentSheetLite(
    viewController: self, 
    configuration: configuration, 
    completion: { 
        result in
            DispatchQueue.main.async {
                switch result {
                case .completed:
                    self.statusLabel.text = "Payment complete"
                case .failed(let error):
                    self.statusLabel.text =  "Payment failed: \(error)"
                case .canceled:
                    self.statusLabel.text = "Payment canceled."
            }
    }
})
```

**Final Step**

You have successfully integrated the **Hyperswitch Lite SDK** into your iOS app.\
The Lite SDK delivers **full payment processing** capabilities with a **smaller footprint**, perfect for apps where bundle size matters.
