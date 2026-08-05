---
description: Integrate hyper SDK to your Swift App using hyperswitch-node
icon: swift
---

# Swift with REST API Integration

{% hint style="info" %}
Use this guide to integrate Juspay Hyperswitch SDK to your iOS app. You can use the following [app](https://github.com/aashu331998/Hyperswitch-iOS-Demo-App/archive/refs/heads/main.zip) as a reference with your Hyperswitch credentials to test the setup. You can also checkout the [app on Apple Testflight](https://testflight.apple.com/join/WhPLmrT6) to test the payment flow.
{% endhint %}

#### Requirements

* iOS 15.1 and above
* CocoaPods
* npm

#### 1. Setup the server

Follow the Server Setup section.

#### 2. Build checkout page on your app

**2.1 Configure your repository with Hyperswitch dependency**

CocoaPods Setup (only required if not already done)

1. Install the latest version of CocoaPods
2. To create a Podfile run the following command

```
pod init
```

SDK Setup

Add these lines to your Podfile:

```ruby
#use_frameworks!
#target 'YourAPP' do
  pod 'hyperswitch-sdk-ios'
#end
```

Run the following command:

```
pod install
```

**Remember that moving forward, you should open your project in Xcode using the .xcworkspace file rather than the .xcodeproj file.**

To update to the latest version of the SDK, run:

```
pod install --repo-update
```

**2.2 Setup the SDK and fetch a Payment**

Set up the SDK using your publishable key and profile id using `HyperswitchConfiguration`.  Use this to create a `Hyperswitch` instance.

To get a `publishableKey` and `profileId`, refer to your Hyperswitch dashboard [here](https://app.hyperswitch.io/developers).

<pre class="language-swift"><code class="lang-swift"><strong>import Hyperswitch
</strong>
let hyperswitchConfiguration = HyperswitchConfiguration(
    publishableKey: publishableKey,
    profileId: profileId
)
let hyperswitch = Hyperswitch(configuration: hyperswitchConfiguration)
</code></pre>

{% hint style="warning" %}
Note: For Open Source Setup, initialize your custom Backend app & log URL as:

```swift
hyperswitchConfiguration = HyperswitchConfiguration(
                                publishableKey: <YOUR_PUBLISHABLE_KEY>, 
                                profileId: <YOUR_PROFILE_ID>,
                                customEndpoints: .commonEndpoint(<YOUR_SERVER_URL>),
)

// For more granualar, per-service URLs
hyperswitchConfiguration = HyperswitchConfiguration(
                                publishableKey: <YOUR_PUBLISHABLE_KEY>,
                                profileId: <YOUR_PROFILE_ID>,
                                customEndpoints: .overrideEndpoints(
                                    OverrideEndpointConfiguration(
                                        customBackendEndpoint: <YOUR_BACKEND_URL>,
                                        customAssetEndpoint: <YOUR_ASSET_URL>,
                                        customSDKConfigEndpoint: <YOUR_SDK_CONFIG_URL>,
                                        customConfirmEndpoint: <YOUR_CONFIRM_URL>,
                                        customAirborneEndpoint: <YOUR_AIRBORNE_URL>,
                                        customLoggingEndpoint: <YOUR_LOGGING_URL>
                                    )
                                )
)
```
{% endhint %}

**2.3 Complete the payment on your app**

**Fetch a Payment**

Request your server to fetch a payment as soon as your view is loaded. Store the `sdkAuthorization` returned by your server. The `PaymentSession` will use this secret to complete the payment process.

{% hint style="danger" %}
**Important**: Make sure to never share your API key with your client application as this could potentially compromise your security.
{% endhint %}

{% tabs %}
{% tab title="Swift" %}
```swift
let paymentSessionConfiguration = PaymentSessionConfiguration(
    sdkAuthorization: sdkAuthorization
)

let paymentSession = hyperswitch.initPaymentSession(
    configuration: paymentSessionConfiguration
)
```
{% endtab %}
{% endtabs %}

**Handle Payment Result**

Handle the payment result in the completion block and display appropriate messages to your customer based on whether the payment fails with an error or succeeds.

{% tabs %}
{% tab title="Swift" %}
```swift
@objc
func openPaymentSheet(_ sender: Any) { //present payment shee
    var configuration = PaymentSheet.Configuration()
    configuration.merchantDisplayName = "Example, Inc."
    
    // Optional theming
    var appearance = PaymentSheet.Appearance()
    appearance.font.base = UIFont(name: "montserrat", size: UIFont.systemFontSize)
    appearance.shapes.shadow = .disabled
    appearance.colors.primary = UIColor(red: 0.55, green: 0.74, blue: 0.00, alpha: 1.00)
    appearance.primaryButton.shapes.borderRadius = 32
    configuration.appearance = appearance
    
    // Optional: enable native 3DS challenges inside the sheet
    configuration.netceteraSDKApiKey = netceteraApiKey
    
    paymentSession.presentPaymentSheet(
        viewController: self,
        configuration: configuration,
        subscribe: { builder in  // optional event subscription
            builder.on(.paymentMethodInfoCard) { event in
                if case .cardInfo(let info) = event.data {
                    print(info)
                }
            }
        },
        completion: { result in
            DispatchQueue.main.async {
                switch result {
                case .completed: print("Payment complete")
                case .failed(let error): print("Payment failed: \(error)")
                case .canceled: print("Payment canceled")
                }
            }
        }
    )
}
```

{% hint style="danger" %}
Please retrieve the payment status from the Hyperswitch backend to get the terminal status of the payment. Do not rely solely on the status returned by the SDK, as it may not always reflect the final state of the transaction.
{% endhint %}
{% endtab %}

{% tab title="SwiftUI" %}
```swift
VStack {
  if let paymentSession = model.paymentSession {
    PaymentSheet.PaymentButton(paymentSession: paymentSession, 
                                               configuration: configuration(),
                                               onCompletion: model.onPaymentCompletion)
    {
     Text("Hyper Payment Sheet")
        .padding()
        .background(.blue)
        .foregroundColor(.white)
        .cornerRadius(10.0)
    }

    if let result = model.paymentResult {
        switch result {
          case .completed:
            Text("Payment complete")
          case .failed(let error):
            Text("Payment failed: \(error.domain)")
          case .canceled:
            Text("Payment canceled.")
          }
      }
  }
}.onAppear { model.preparePaymentSheet() }

// handle result
func onPaymentCompletion(result: PaymentSheetResult) {
        DispatchQueue.main.async {
            self.paymentResult = result
        }
}

// setup configuration for payment sheet
func configuration() -> PaymentSheet.Configuration {
        var configuration = PaymentSheet.Configuration()
        configuration.merchantDisplayName = "Example, Inc."
        return configuration
}
```
{% endtab %}
{% endtabs %}

#### 3. Card Element (Beta)

Create a card element view and pay button and handle the payment result in the completion block and display appropriate messages to your customer based on whether the payment fails with an error or succeeds.

{% tabs %}
{% tab title="Swift" %}
<pre class="language-swift"><code class="lang-swift"><strong>//Create a card element view and pay button.
</strong><strong>lazy var hyperCardTextField: PaymentCardTextField = {
</strong>    let cardTextField = PaymentCardTextField()
    return cardTextField
}()

lazy var payButton: UIButton = {
    let button = UIButton(type: .custom)
    button.layer.cornerRadius = 5
    button.backgroundColor = .systemBlue
    button.setTitle("Pay", for: .normal)
    button.addTarget(self, action: #selector(pay), for: .touchUpInside)
    return button
}()


@objc
func pay() {
    guard let paymentIntentClientSecret = model.paymentIntentClientSecret else {
        return
    }
    let paymentIntentParams = PaymentIntentParams(clientSecret: paymentIntentClientSecret)
let paymentHandler = PaymentHandler.shared()

    paymentHandler.confirmPayment(paymentIntentParams, with: self) { 
        (status, paymentIntent, error) in
            switch (status) {
                case .failed:
                    break
                case .canceled:
                    break
                case .succeeded:
                    break
                @unknown default:
                    fatalError()
                    break
            }
    }
}
</code></pre>
{% endtab %}

{% tab title="SwiftUI" %}
```swift
@ObservedObject var model = BackendModel()
@State var paymentMethodParams: PaymentMethodParams?

VStack {
  PaymentCardTextField.Representable(paymentMethodParams: $paymentMethodParams)
    .padding()
  //Create a card element view and pay button.
  if let paymentIntent = model.paymentIntentParams {
    Button("Buy")
    {
      paymentIntent.paymentMethodParams = paymentMethodParams
      isConfirmingPayment = true
    }
    .disabled(isConfirmingPayment || paymentMethodParams == nil)
    .paymentConfirmationSheet(
        isConfirmingPayment: $isConfirmingPayment,
        paymentIntentParams: paymentIntent,
        onCompletion: model.onCompletion
        )
  }
  else {
    ProgressView()
  }
  if let paymentStatus = model.paymentStatus {
    PaymentHandlerStatusView(actionStatus: paymentStatus,
                             lastPaymentError: model.lastPaymentError)
  }
}.onAppear { model.preparePaymentIntent() }
```
{% endtab %}
{% endtabs %}

Congratulations! Now that you have integrated the iOS SDK, you can customize the payment sheet to blend with the rest of your app.

#### Next Step:
