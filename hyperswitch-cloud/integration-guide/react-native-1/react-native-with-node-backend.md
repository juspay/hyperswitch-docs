---
description: Integrate hyper SDK to your Flutter App using hyperswitch-node
---

# Flutter with Node Backend



{% hint style="info" %}
Use this guide to integrate `hyper` SDK to your Flutter app.&#x20;
{% endhint %}

**Before following these steps, please configure your payment methods** [here](../../payment-methods-setup/cards.md).

## Requirements

* Android 5.0 (API level 21) and above
* [Android Gradle Plugin](https://developer.android.com/studio/releases/gradle-plugin) 7.3.1
* [Gradle](https://gradle.org/releases/) 7.5.1+
* [AndroidX](https://developer.android.com/jetpack/androidx/)
* iOS 13.0 and above
* CocoaPods
* npm

## 1. Setup the server

### 1.1 Install the `hyperswitch-node` library

Install the package and import it in your code

```js
$ npm install @juspay-tech/hyperswitch-node
```

### 1.2 Create a payment

Before creating a payment, import the hyper dependencies and initialize it with your API key. Get your API key from [Hyperswitch dashboard](https://app.hyperswitch.io/developers?tabIndex=1).

```js
const hyper = require("@juspay-tech/hyperswitch-node")(‘YOUR_API_KEY’);
```

Add an endpoint on your server that creates a Payment. Creating a Payment helps to establish the intent of the customer to start a payment. It also helps to track the customer’s payment lifecycle, keeping track of failed payment attempts and ensuring the customer is only charged once. Return the client\_secret obtained in the response to securely complete the payment on the client.

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

## 2. Build checkout page on the client

### 2.1 Install the `flutter_hyperswitch` library

Add `flutter_hyperswitch` to your `pubspec.yaml` file

```js
dependencies:
  flutter_hyperswitch: ^version_number
```

Run the following command to fetch and install the dependencies.

```sh
flutter pub get
```

## 3. Complete the checkout on the client

### 3.1 Initialize the Hyperswitch SDK

Initialize `Hyper` onto your app with your publishable key with the `Hyper` constructor. To get a PublishableKey please find it [here](https://app.hyperswitch.io/developers).

```dart
import 'package:flutter_hyperswitch/flutter_hyperswitch.dart';
final _hyper = FlutterHyperswitch();
_hyper.init(HyperConfig(publishableKey: 'YOUR_PUBLISHABLE_KEY', customBackendUrl: 'YOUR_CUSTOM_BACKEND_URL'));
```

{% hint style="info" %}
When utilizing a custom backend or logging system, you can add the customBackendUrl to HyperConfig
{% endhint %}

### 3.2  Create a Payment Intent

Make a network request to the backend endpoint you created in the [previous step](react-native-with-node-backend.md#id-1.2-create-a-payment). The clientSecret returned by your endpoint is used to complete the payment.

```dart
Future<String> fetchPaymentParams() async {
    try {
      var response = await http.get(Uri.parse("$API_URL/create-payment"),
      return jsonDecode(response.body)["clientSecret"];
    } catch (error) {
      throw Exception("Create Payment API call failed");
    }
  }
```

### 3.3 Initialize your Payment Session

Initialize a Payment Session by passing the clientSecret to the `initPaymentSession`

```dart
 Session paymentSession = await hyper.initPaymentSession(PaymentMethodParams(clientSecret: 'YOUR_PAYMENT_INTENT_CLIENT_SECRET'));
```

### 3.4 Present payment sheet and handle response

To display the Payment Sheet, integrate a "**Pay Now**" button within the checkout page, which, when clicked, invokes the `presentPaymentSheet()`method and handles the payment response.

Consider the below function, it invokes and `presentPaymentSheet` and handles various payment results.

```dart
void openPaymentSheet() async {
    PaymentResult presentPaymentSheetResponse = await paymentSession.presentPaymentSheet();

    var status = confirmWithCustomerDefaultPaymentMethodResponse.status;
    var message = confirmWithCustomerDefaultPaymentMethodResponse.message;
    
    // use paymentSheetResponseType, paymentSheetResponseMessage to complete the payment journey
    switch (status) {
      case "cancelled":
        // handle cancelled case
        break;
      case "failed":
        // handle failed case
        break;
      case "completed":
          switch (message) {
              case "succeeded":
                // handle succeeded case
                break;
              case "processing":
                // handle requires_capture case
                break;
              default:
                // handle the default case
                break;
        }
        break;
    }
  }
```

Congratulations! Now that you have integrated the  Flutter SDK, you can [**customize**](customization.md) the payment sheet to blend with the rest of your app.&#x20;

## Next step:

{% content-ref url="../../payment-methods-setup/" %}
[payment-methods-setup](../../payment-methods-setup/)
{% endcontent-ref %}
