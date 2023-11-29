# GooglePay

With Google Pay, customers can conveniently make payments within your app or website using credit or debit cards saved in their Google Account. This includes cards from various sources, such as Google Play, YouTube, Chrome, or any Android device. By utilizing the Google Pay API, you can request access to any credit or debit card stored in your customer's Google account.

Google Pay seamlessly integrates with Hyperswitch, providing you with the flexibility to replace conventional payment forms whenever it is feasible and appropriate.

**Accept a payment using Google Pay in your React Native app**

To begin accepting Google Pay in your React Native apps, utilize Hyperswitch's React Native SDK, which offers the swiftest and most straightforward approach.

## Enable Google Pay

In your PaymentScreen.js file call initPaymentSheet from the useHyper hook pass the Google Pay Parameter to enable it in your app

```js
const { error } = await initPaymentSheet({
  merchantDisplayName: "Hyperswitch",
  paymentIntentClientSecret: clientSecret,
  googlePay: {
    testEnv: true,
    merchantCountryCode: "US",
    currencyCode: "USD",
  },
});
```

Once your app receives approval, proceed to test your integration in the production environment by setting testEnv to false. Launch Google Pay from a signed, release build of your app to ensure a smooth and accurate testing process.
