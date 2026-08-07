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

To receive surcharge updates, include `"surchargeInfo"` in the `subscriptionEvents` configuration when creating the payment element. Refer to  [React](../pay-then-vault/web/react-with-rest-api-integration.md) and [Js](../pay-then-vault/web/js-with-rest-api-integration.md) integration documentation for implementation details.<br>

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

