---
description: >-
  Juspay Hyperswitch is designed to facilitate the integration and management of
  payment-related functionalities in a decoupled or headless architecture with
  flexibility to customize your checkout UI.
icon: grip
---

# Headless SDK

#### Customize the payment experience using Headless functions

**1. Initialize the Hyperswitch SDK**

Initialize Juspay Hyperswitch Headless SDK onto your app with your publishable key. To get a Publishable Key please find it [here](https://app.hyperswitch.io/developers).

```dart
// dependencies: flutter_hyperswitch: ^version_number
// run the following command to fetch and install the dependencies flutter pub get
import 'package:flutter_hyperswitch/flutter_hyperswitch.dart';
_hyper.init(HyperConfig(publishableKey: 'YOUR_PUBLISHABLE_KEY'));
```

**2. Create a Payment Intent**

Make a request to the endpoint on your server to create a new Payment. The `clientSecret` returned by your endpoint is used to initialize the payment session.

{% hint style="danger" %}
**Important**: Make sure to never share your API key with your client application as this could potentially compromise your security
{% endhint %}

**3. Initialize your Payment Session**

Initialize a Payment Session by passing the clientSecret to the `initPaymentSession`

```dart
final params = PaymentMethodParams(clientSecret: 'YOUR_PAYMENT_INTENT_CLIENT_SECRET')
Session _sessionId = await hyper.initPaymentSession(params);
```

| options (Required)                   | Description                                                     |
| ------------------------------------ | --------------------------------------------------------------- |
| `paymentIntentClientSecret (string)` | **Required.** Required to use as the identifier of the payment. |

**4. Craft a customized payments experience**

Call `getCustomerSavedPaymentMethods` with your session id and keep the `SavedSession` it returns. On Flutter the confirm functions are on the `Hyper` instance and take that saved session, as the example below shows, rather than hanging off a session object.

```dart
SavedSession? _savedSessionId = await _hyper.getCustomerSavedPaymentMethods(_sessionId!);

// use the customer_default_saved_payment_method_data to fulfill your usecases
final customer_last_used_saved_payment_method_data = await _hyper.getCustomerLastUsedSavedPaymentMethodData(_savedSessionId!);
if (customer_last_used_saved_payment_method_data != null) {
    final paymentMethod = customer_last_used_saved_payment_method_data.left;
    if (paymentMethod != null) {
       final card = paymentMethod.left;
    }
  }
}

// use the confirmWithCustomerDefaultPaymentMethod function to confirm and handle the payment session response
Future<void> _confirmPayment() async {
  final confirmWithLastUsedPaymentMethodResponse = 
    await _hyper.confirmWithLastUsedPaymentMethod(_savedSessionId!);
  if (confirmWithLastUsedPaymentMethodResponse != null) {
    final message = confirmWithLastUsedPaymentMethodResponse.message;
    if (message.isLeft) {
      _confirmStatusText = "${confirmWithLastUsedPaymentMethodResponse.status.name}\n${message.left!.name}";
    } else {
      _confirmStatusText = "${confirmWithLastUsedPaymentMethodResponse.status.name}\n${message.right}";
    }
  }
}
```

**Payload for** `confirmWithCustomerLastUsedPaymentMethod(callback)`

<table><thead><tr><th width="296">options (Required)</th><th>Description</th></tr></thead><tbody><tr><td><code>callback (function)</code></td><td>Callback to get confirm response.</td></tr></tbody></table>

***
