---
description: Integrate hyper SDK to your Flutter App using hyperswitch-node
---

# Flutter with Node Backend



{% hint style="info" %}
Use this guide to integrate `hyper` SDK to your Flutter app.&#x20;
{% endhint %}

**Before following these steps, please configure your payment methods** [here](../../../payment-flows-and-management/quickstart/payment-methods-setup/cards.md).

## Requirements

* Android 5.0 (API level 21) and above
* [Android Gradle Plugin](https://developer.android.com/studio/releases/gradle-plugin) 8.5+
* [Gradle](https://gradle.org/releases/) 8.8+
* [AndroidX](https://developer.android.com/jetpack/androidx/)
* iOS 13.0 and above
* CocoaPods
* npm

```js
$ npm install @juspay-tech/hyperswitch-node
```

## 1. Setup the server

Follow the [Server Setup](../web/server-setup.md) section.

## 2. Build checkout page on the client

### 2.1 Install the `flutter_hyperswitch` library

Add `flutter_hyperswitch` to your `pubspec.yaml` file

```yaml
dependencies:
  flutter_hyperswitch: ^version_number
```

Run the following command to fetch and install the dependencies.

```sh
flutter pub get
```

{% hint style="info" %}
To apply plugins using Flutter, run the following command:

```sh
dart run flutter_hyperswitch:apply_plugins
```

This command configures the necessary Flutter plugins for your project using the `flutter_hyperswitch` package. Ensure you have the package installed and configured correctly in your project. If you encounter any issues, check the package documentation for more details.
{% endhint %}

## 3. Complete the checkout on the client

### 3.1 Initialise the Hyperswitch SDK

Initialise `Hyper` onto your app with your publishable key with the `Hyper` constructor. To get a PublishableKey please find it [here](https://app.hyperswitch.io/developers).

```dart
import 'package:flutter_hyperswitch/flutter_hyperswitch.dart';
final _hyper = FlutterHyperswitch();
_hyper.init(HyperConfig(publishableKey: 'YOUR_PUBLISHABLE_KEY', customBackendUrl: 'YOUR_CUSTOM_BACKEND_URL'));
```

{% hint style="info" %}
When utilising a custom backend or logging system, you can add the customBackendUrl to HyperConfig
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
final params = PaymentMethodParams(clientSecret: 'YOUR_PAYMENT_INTENT_CLIENT_SECRET');
Session? _sessionId = await _hyper.initPaymentSession(params);
```

### 3.4 Present payment sheet and handle response

To display the Payment Sheet, integrate a "**Pay Now**" button within the checkout page, which, when clicked, invokes the `presentPaymentSheet()`method and handles the payment response.

Consider the below function, it invokes `presentPaymentSheet` and handles payment results.

{% code fullWidth="false" %}
```dart
Future<void> _presentPaymentSheet() async {
  final presentPaymentSheetResponse = await _hyper.presentPaymentSheet(_sessionId!);
  if (presentPaymentSheetResponse != null) {
    final message = presentPaymentSheetResponse.message;
    setState(() {
      if (message.isLeft) {
        _statusText =
            "${presentPaymentSheetResponse.status.name}\n${message.left!.name}";
      } else {
        _statusText =
            "${presentPaymentSheetResponse.status.name}\n${message.right}";
      }
    });
  }
}
```
{% endcode %}

Congratulations! Now that you have integrated the  Flutter SDK, you can [**customize**](customization.md) the payment sheet to blend with the rest of your app.&#x20;

{% hint style="danger" %}
Please retrieve the payment status from the Hyperswitch backend to get the terminal status of the payment. Do not rely solely on the status returned by the SDK, as it may not always reflect the final state of the transaction.
{% endhint %}

## Next step:

{% content-ref url="../../../payment-flows-and-management/quickstart/payment-methods-setup/" %}
[payment-methods-setup](../../../payment-flows-and-management/quickstart/payment-methods-setup/)
{% endcontent-ref %}
