---
description: >-
  Hyperswitch App Clip is a lightweight version of your iOS app that launches
  instantly (via QR code, NFC, or link) to let users complete payments quickly
  without installing the full app.
icon: app-store
---

# App Clips

* A **lightweight, instant-launch** version of your iOS app.
* Lets users complete **fast Hyperswitch payments** without installing the full app.
* Can be triggered via **QR code, NFC tag, Safari link, or Maps**.
* Ideal for quick checkout use cases (parking, food ordering, event tickets, etc.)

### Requirements

* **iOS 14+**
* **Xcode 12+**
* Apple Developer Account
* Hyperswitch SDK already integrated in main iOS app

## Quick Steps

#### 1. Create App Clip Target

* Xcode → **File → New Target → App Clip**
* Bundle ID: `your.main.app.bundle.id.Clip`
* Same Team as main app.

#### 2. Share Payment Logic

* Make `HyperViewModel` target membership include **both** the main app and App Clip.
* Or move shared code into a framework.

#### 3. Minimal UI in App Clip

```swift
@objc func openPaymentSheet(_ sender: Any) {
    var config = PaymentSheet.Configuration()
    config.primaryButtonLabel = "Purchase ($2.00)"
    config.appearance = PaymentSheet.Appearance()

    hyperViewModel.paymentSession?.presentPaymentSheetLite(
        viewController: self,
        configuration: config
    ) { result in
        switch result {
        case .completed:
            self.statusLabel.text = "Payment complete"
        case .failed(let error):
            self.statusLabel.text = "Payment failed: \(error)"
        case .canceled:
            self.statusLabel.text = "Payment canceled."
        }
    }
}
```

***

### Flow Summary

1. **User triggers App Clip** (QR/NFC/web link).
2. **App Clip requests payment intent** from your backend.
3. **Backend creates payment session** with Hyperswitch.
4. **SDK presents PaymentSheetLite** for checkout.
5. **User pays → Hyperswitch processes**.
6. **Result shown instantly** (success/fail).

## Related Pages

To use this feature add Lite SDK in your AppClips

{% content-ref url="../integration-guide/mobile/ios/lite-sdk.md" %}
[lite-sdk.md](../integration-guide/mobile/ios/lite-sdk.md)
{% endcontent-ref %}
