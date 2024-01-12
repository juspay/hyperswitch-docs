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

### 3.1 Add package to your Flutter app

In the checkout of your app, import the below package

```dart
import 'package:flutter_hyperswitch/flutter_hyperswitch.dart';
```

### 3.2 Fetch the PaymentIntent client Secret

Make a network request to the backend endpoint you created in the [previous step](react-native-with-node-backend.md#id-1.2-create-a-payment). The clientSecret returned by your endpoint is used to complete the payment.

```dart
Future<String> fetchPaymentParams() async {
    try {
      var response = await http.post(Uri.parse("$API_URL/create-payment"),
          headers: <String, String>{
            'Accept': 'application/json',
            'Content-Type': 'application/json; charset=UTF-8',
          },
          body: jsonEncode(
              {'paymentFlow': 'ZeroAuth', 'customer_id': customerId}));

      return jsonDecode(response.body)["clientSecret"];
    } catch (error) {
      throw Exception("Create Payment API call failed");
    }
  }
```

### 3.3 Collect Payment details

Create an instance of `FlutterHyperswitch` class, now use this object to initialize paymentsheet.  You can call the methods `initPaymentSheet` and `presentPaymentSheet` through this object.

```dart
 final _flutterHyperswitchPlugin = FlutterHyperswitch();
```

Call `initPaymentSheet` through the object created above to customise paymentsheet, billing or shipping addresses and initialize paymentsheet.

```dart
 void initialisePaymentSheet() async {
    var clientSecret = await fetchPaymentParams();
    PaymentSheetParams params = PaymentSheetParams(
      publishableKey: "YOUR_PUBLISHABLE_KEY",
      clientSecret: clientSecret,
    );
    Map<String, dynamic> initPaymentSheetResponse =
        await _flutterHyperswitchPlugin.initPaymentSheet(params) ?? {};
    if (initPaymentSheetResponse["type"] == "success") {
      // you may handle your side effects when payment sheet is initialised
    }
  }
```

### 3.4 Handle Payment Response

To display the Payment Sheet, integrate a "**Pay Now**" button within the checkout page, which, when clicked, invokes the `presentPaymentSheet()`method and handles the payment response.

Consider the below function, it invokes and `presentPaymentSheet` and handles various payment results.

```dart
void openPaymentSheet() async {
    Map<String, dynamic> presentPaymentSheetResponse =
        await _flutterHyperswitchPlugin.presentPaymentSheet() ?? {};

    var paymentSheetResponseType = presentPaymentSheetResponse["type"];
    var paymentSheetResponseMessage = presentPaymentSheetResponse["message"];

    print(
        "presentPaymentSheetResponseType:${paymentSheetResponseType}, presentPaymentSheetMessage:${paymentSheetResponseMessage}");

    switch (paymentSheetResponseType) {
      case "cancelled":
        showDialog(
          context: _scaffoldKey.currentContext!,
          builder: (BuildContext context) {
            return const AlertDialog(
                title: Text("cancelled"), content: Text("cancelled"));
          },
        );
        break;
      case "failed":
        showDialog(
          context: _scaffoldKey.currentContext!,
          builder: (BuildContext context) {
            return const AlertDialog(
                title: Text("failed"), content: Text("Payment failed"));
          },
        );
        break;
      case "completed":
        switch (paymentSheetResponseMessage) {
          case "succeeded":
            showDialog(
              context: _scaffoldKey.currentContext!,
              builder: (BuildContext context) {
                return const AlertDialog(
                    title: Text("succeeded"),
                    content: Text("Your order is succeeded"));
              },
            );
            break;
          case "requires_capture":
            showDialog(
              context: _scaffoldKey.currentContext!,
              builder: (BuildContext context) {
                return const AlertDialog(
                    title: Text("requires_capture"),
                    content: Text("Your order is requires_capture"));
              },
            );
            break;
          default:
            showDialog(
              context: _scaffoldKey.currentContext!,
              builder: (BuildContext context) {
                return const AlertDialog(
                    title: Text("status not captured"),
                    content: Text("Please check the integration"));
              },
            );
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
