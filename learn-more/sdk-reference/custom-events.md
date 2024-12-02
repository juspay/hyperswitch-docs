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
