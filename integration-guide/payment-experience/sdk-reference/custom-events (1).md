---
icon: trowel
---

# Custom Events

### Listen to Expiry Date event

This event is triggered when the expiry date changes. Merchants can listen to this event and implement checks and validations based on the received value.\\

```javascript
// CheckoutForm.js
window.addEventListener("message", (ev) => {
    // Collecting Expiry Date
    if (ev.data.expiryDate) {
      console.log("Expiry date => ", ev.data.expiryDate);
    }
  });
```

### Listen to Payment Method event

Merchants can listen to the Payment Method Info event to receive real-time updates when a customer selects or changes their payment method. This event provides essential details about the selected payment method, allowing merchants to implement custom checks, validations, or UI updates based on the received data.

For card payments, the event will include additional details such as:

* **Card Brand**: The card network, e.g., **Visa, Mastercard,** etc.

```javascript
// CheckoutForm.js
window.addEventListener("message", (ev) => {
    // Collecting Expiry Date
    if (ev.data.expiryDate) {
      console.log("Expiry date => ", ev.data.expiryDate);
    }
  });
```

## Subscription Events

Subscription events provide real-time updates from the SDK about the state of the selected payment method and checkout experience. Merchants can subscribe to specific events and react to changes during the checkout flow.

### surchargeInfo

The `surchargeInfo` event is emitted whenever surcharge information is calculated or updated for a card payment method, including both saved cards and newly entered card details.

#### Event Output

```
{
  "eventName": "surchargeInfo",
  "payload": {
    "surcharge": {
      "type": "fixed",
      "value": 162
    },
    "taxOnSurcharge": null,
    "displaySurchargeAmount": 1.62,
    "displayTaxOnSurchargeAmount": 0,
    "displayTotalSurchargeAmount": 1.62
  }
}
```

The surcharge details are available under the payload property.

#### Payload Fields

| **Field**                   | **Description**                                |
| --------------------------- | ---------------------------------------------- |
| surcharge.type              | Type of surcharge applied (`fixed` or `rate`). |
| surcharge.value             | Surcharge value in the lowest currency unit.   |
| taxOnSurcharge              | Tax applied on the surcharge, if applicable.   |
| displaySurchargeAmount      | Formatted surcharge amount.                    |
| displayTaxOnSurchargeAmount | Formatted tax amount on surcharge.             |
| displayTotalSurchargeAmount | Total surcharge amount including tax.          |

#### JavaScript & React Integration

To receive surcharge updates, include `"surchargeInfo"` in the `subscriptionEvents` configuration when creating the payment element. Refer to [React](../pay-then-vault/web/react-with-rest-api-integration.md) and [Js](../pay-then-vault/web/js-with-rest-api-integration.md) integration documentation for implementation details.<br>

Js Integration

```js
const unifiedCheckoutOptions = {
    ...
    subscriptionEvents: ["surchargeInfo"],
    ...
  };

const unifiedCheckout = widgets.create("payment", unifiedCheckoutOptions);

unifiedCheckout.mount("#unified-checkout");

unifiedCheckout.on("surchargeInfo", (event) => {
    console.log("surchargeInfo is", event);
  });
```

\
React Integration

```js
// react integration
export const paymentElementOptions = {
  ...
  subscriptionEvents: [
     "surchargeInfo",
   ],
  
  ...
};

...


<PaymentElement
  id="payment-element"
  onChange={(event) => {
    if (event?.eventName === "surchargeInfo") {
      console.log("PaymentElement changed:", event);
    }
  }}
  options={paymentElementOptions}
/>      

```

### paymentMethodFlowCancel

The `paymentMethodFlowCancel` event is emitted when the customer starts a payment method's flow and then cancels it before the payment completes. Use it to restore your checkout UI, show a message, or let the customer try again. It is emitted when the customer:

* Closes the Apple Pay payment sheet.
* Closes the Google Pay payment sheet.
* Closes the PayPal popup, including closing it before it has finished loading.
* Closes the 3D Secure authentication window.

#### Event Output

```
{
  "eventName": "paymentMethodFlowCancel",
  "payload": {
    "paymentMethod": "wallet",
    "paymentMethodType": "apple_pay",
    "canRetryPayment": true
  }
}
```

The details of the cancelled flow are available under the payload property.

#### Payload Fields

| **Field**         | **Description**                                                                                                                                                                              |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| paymentMethod     | The payment method whose flow was cancelled, for example `wallet` or `card`.                                                                                                                 |
| paymentMethodType | The payment method type whose flow was cancelled, for example `apple_pay`, `google_pay` or `paypal`.                                                                                         |
| canRetryPayment   | Whether the customer can retry the payment with the same payment intent. Always `true` for wallet cancellations. For 3D Secure it is `true` only if manual retry is allowed for the payment. |

#### JavaScript & React Integration

To receive this event, include `"paymentMethodFlowCancel"` in the `subscriptionEvents` configuration when creating the payment element. The event is delivered to your `change` handler (`onChange` in React), so check `eventName` to identify it. Refer to [React](../pay-then-vault/web/react-with-rest-api-integration.md) and [Js](../pay-then-vault/web/js-with-rest-api-integration.md) integration documentation for implementation details.

{% hint style="info" %}
Unlike `surchargeInfo`, this event has no dedicated `on("paymentMethodFlowCancel", ...)` listener. Listen with `on("change", ...)` in JS or `onChange` in React.
{% endhint %}

Js Integration

```js
const unifiedCheckoutOptions = {
    ...
    subscriptionEvents: ["paymentMethodFlowCancel"],
    ...
  };

const unifiedCheckout = widgets.create("payment", unifiedCheckoutOptions);

unifiedCheckout.mount("#unified-checkout");

unifiedCheckout.on("change", (event) => {
    if (event?.eventName === "paymentMethodFlowCancel") {
      const { paymentMethodType, canRetryPayment } = event.payload;
      console.log(`${paymentMethodType} flow was cancelled`, canRetryPayment);
    }
  });
```

\
React Integration

```js
// react integration
export const paymentElementOptions = {
  ...
  subscriptionEvents: [
     "paymentMethodFlowCancel",
   ],
  
  ...
};

...


<PaymentElement
  id="payment-element"
  onChange={(event) => {
    if (event?.eventName === "paymentMethodFlowCancel") {
      const { paymentMethodType, canRetryPayment } = event.payload;
      console.log(`${paymentMethodType} flow was cancelled`, canRetryPayment);
    }
  }}
  options={paymentElementOptions}
/>
```

## Lifecycle Events

Lifecycle events tell you about the state of the payment element itself, such as when it has loaded or changed size. They do not need to be added to `subscriptionEvents`.

### ready

The `ready` event is emitted when the payment element has loaded. When it fires depends on the `enableProgressiveLoading` option passed when creating the payment element.

| **enableProgressiveLoading** | **When `ready` fires**                                                                                                                                                                                                                                                                                                                                                                                   |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `true` (default)             | Each section (saved payment methods, wallet buttons, payment methods) is shown as soon as it has loaded. `ready` fires once the first section is on screen.                                                                                                                                                                                                                                              |
| `false`                      | A single loading skeleton is shown until every section on the first screen has loaded, and the whole payment element is then revealed at once. `ready` fires at that moment. Wallets still checking whether they can be shown (for example Apple Pay, Google Pay or Klarna) are waited on for up to 3 seconds. Only the first screen is held back; screens the customer opens later render as they load. |

#### JavaScript & React Integration

Js Integration

```js
const unifiedCheckoutOptions = {
    ...
    enableProgressiveLoading: false,
    ...
  };

const unifiedCheckout = widgets.create("payment", unifiedCheckoutOptions);

unifiedCheckout.mount("#unified-checkout");

unifiedCheckout.on("ready", () => {
    console.log("Payment element is fully loaded");
  });
```

\
React Integration

```js
// react integration
export const paymentElementOptions = {
  ...
  enableProgressiveLoading: false,
  ...
};

...


<PaymentElement
  id="payment-element"
  onReady={() => {
    console.log("Payment element is fully loaded");
  }}
  options={paymentElementOptions}
/>
```

### resize

The `resize` event is emitted when the height of the payment element changes, for example when a payment method is expanded, an error message appears, or the element finishes loading. Use it to adjust the layout around the payment element, such as a modal, a bottom sheet or a fixed container.

* The event is emitted after the height has settled (about 100 ms after the last change), so you get one event per change rather than one per frame.
* It is also emitted once right after the payment element becomes ready, even when the height has not changed, so you always receive the final loaded height.
* A height of `0` (for example while the element is hidden) is never reported.

#### Event Output

```
{
  "height": 512,
  "isReady": true
}
```

#### Fields

| **Field** | **Description**                                                                                                                                   |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| height    | The new height of the payment element, in pixels.                                                                                                 |
| isReady   | `true` once the payment element has emitted its `ready` event. Events with `false` describe the loading state (for example the loading skeleton). |

#### JavaScript & React Integration

Js Integration

```js
const unifiedCheckout = widgets.create("payment", unifiedCheckoutOptions);

unifiedCheckout.mount("#unified-checkout");

unifiedCheckout.on("resize", (event) => {
    console.log("Payment element height:", event.height, "ready:", event.isReady);
  });
```

\
React Integration

```js
// react integration
<PaymentElement
  id="payment-element"
  onResize={(event) => {
    console.log("Payment element height:", event.height, "ready:", event.isReady);
  }}
  options={paymentElementOptions}
/>
```
