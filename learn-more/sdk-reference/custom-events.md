# Custom Events

## Listen to Expiry Date event

This event is triggered when the expiry date changes. Merchants can listen to this event and implement checks and validations based on the received value.\


```javascript
// CheckoutForm.js
window.addEventListener("message", (ev) => {
    // Collecting Expiry Date
    if (ev.data.expiryDate) {
      console.log("Expiry date => ", ev.data.expiryDate);
    }
  });
```

## Listen to Payment Methods Info event

Merchants can listen to the Payment Method Info event to receive real-time updates when a customer selects or changes their payment method. This event provides essential details about the selected payment method, allowing merchants to implement custom checks, validations, or UI updates based on the received data.

For card payments, the event will include additional details such as:

* **Card Brand**: The card network, e.g., **Visa, Mastercard,** etc.

```javascript
// CheckoutForm.js
window.addEventListener("message", (ev) => {
    // Collecting Payment Method Info
    if (ev.data.paymentMethodInfo) {
      console.log("Payment method info => ", ev.data.paymentMethodInfo);
    }
  });
```
