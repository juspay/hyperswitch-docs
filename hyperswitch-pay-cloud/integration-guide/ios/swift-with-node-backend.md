---
description: Integrate hyper SDK to your Swift App using hyperswitch-node
---

# Swift with Node Backend

{% hint style="info" %}
Use this guide to integrate Hyperswitch SDK to your iOS app. You can use the following [app](https://github.com/aashu331998/Hyperswitch-iOS-Demo-App/archive/refs/heads/main.zip) as a reference with your Hyperswitch credentials to test the setup. You can also checkout the [app on Apple Testflight](https://testflight.apple.com/join/WhPLmrT6) to test the payment flow.
{% endhint %}

## Requirements

* iOS 12.4 and above
* CocoaPods
* npm

## 1. Setup the server

### 1.1 Install the `hyperswitch-node` library

Install the package and import it in your code

```js
$ npm install @juspay-tech/hyperswitch-node
```

### 1.2 Create a payment

Before creating a payment, import the `hyperswitch-node` dependencies and initialize it with your API key.

```js
const hyper = require("@juspay-tech/hyperwitch-node")(‘YOUR_API_KEY’);
```

Add an endpoint on your server that creates a Payment. Creating a Payment helps to establish the intent of the customer to start a payment. It also helps to track the customer’s payment lifecycle, keeping track of failed payment attempts and ensuring the customer is only charged once. Return the `client_secret` obtained in the response to securely complete the payment on the client.

```js
// Create a Payment with the order amount and currency
app.post("/create-payment", async (req, res) => {
  try {
    const paymentIntent = await hyper.paymentIntents.create({
      currency: "USD",
      amount: 100,
    });
    // Send publishable key and PaymentIntent details to client
    res.send({
      clientSecret: paymentIntent.client_secret,
    });
  } catch (err) {
    return res.status(400).send({
      error: {
        message: err.message,
      },
    });
  }
});
```

## 2. Build checkout page on your app

### 2.1 Configure your repository with Hyperswitch dependency

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
  pod 'HyperswitchCore'
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

### 2.2 Setup the SDK and fetch a Payment

Fetch a payment by requesting your server for a payment as soon as your view is loaded. Store a reference to the `client_secret` returned by the server, the Payment Sheet will use this secret to complete the payment later. Setup the SDK with your publishable key.

```swift
STPAPIClient.shared.publishableKey = <YOUR_PUBLISHABLE_KEY>
```

{% hint style="warning" %}
Note: For Open Source Setup, initialise your custom Backend app URL as:

<pre class="language-bash"><code class="lang-bash"><strong>STPAPIClient.shared.customBackendUrl = &#x3C;YOUR_SERVER_URL>
</strong></code></pre>
{% endhint %}

## 3. Complete the payment on your app

## 3.1 Swift

Create a PaymentSheet instance using the `client_secret` retrieved from the previous step. Present the payment page from your view controller and use the PaymentSheet.Configuration struct for customising your payment page.



{% tabs %}
{% tab title="Swift" %}
```swift
var paymentSheet: PaymentSheet?
var paymentResult: PaymentSheetResult?

var configuration = PaymentSheet.Configuration()
configuration.merchantDisplayName = "Example, Inc."

// Present Payment Page
paymentSheet = PaymentSheet(paymentIntentClientSecret: paymentIntentClientSecret, configuration: configuration)
```
{% endtab %}

{% tab title="SwiftUI" %}
```swift
@ObservedObject var model = BackendModel()
@Published var paymentSheet: HyperPaymentSheet?
@Published var paymentResult: HyperPaymentSheetResult?


// Present Payment Page
paymentSheet = PaymentSheet(paymentIntentClientSecret: paymentIntentClientSecret, configuration: configuration)
```
{% endtab %}
{% endtabs %}

Handle the payment result in the completion block and display appropriate messages to your customer based on whether the payment fails with an error or succeeds.

{% tabs %}
{% tab title="Swift" %}
```swift
@objc
func openPaymentSheet(_ sender: Any) { //present payment sheet
    self.paymentSheet?.present(from: self, completion: { result in
        switch result {
        case .completed:
            print("Payment complete")
        case .failed(let error):
            print("Payment failed: \(error.localizedDescription)")
        case .canceled:
            print("Payment canceled.")
        }
    })
}
```
{% endtab %}

{% tab title="SwiftUI" %}
```swift
VStack {
  if let paymentSheet = model.paymentSheet {
    HyperPaymentSheet.PaymentButton(paymentSheet: paymentSheet,
    onCompletion: model.onPaymentCompletion)
    { Text("Hyper Payment Sheet")
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
```
{% endtab %}
{% endtabs %}

## 4. Card Element

## 4.1 Swift

Create a card element view and pay button and handle the payment result in the completion block and display appropriate messages to your customer based on whether the payment fails with an error or succeeds.

{% tabs %}
{% tab title="Swift" %}
<pre class="language-swift"><code class="lang-swift"><strong>//Create a card element view and pay button.
</strong><strong>lazy var hyperCardTextField: STPPaymentCardTextField = {
</strong>    let cardTextField = STPPaymentCardTextField()
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
  let paymentIntentParams = STPPaymentIntentParams(clientSecret: paymentIntentClientSecret)
  let paymentHandler = STPPaymentHandler.shared()

  paymentHandler.confirmPayment(paymentIntentParams, with: self)
  { (status, paymentIntent, error) in
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
@State var paymentMethodParams: STPPaymentMethodParams?

VStack {
  STPPaymentCardTextField.Representable(paymentMethodParams: $paymentMethodParams)
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

Congratulations! Now that you have integrated the iOS SDK, you can customize the payment sheet to blend with the rest of your app.&#x20;

## Next step:

{% content-ref url="../../payment-methods-setup/" %}
[payment-methods-setup](../../payment-methods-setup/)
{% endcontent-ref %}
