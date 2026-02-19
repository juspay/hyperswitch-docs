---
icon: rotate-exclamation
---

# Authenticate with 3D Secure via PSP

You can integrate 3D Secure (3DS) authentication into your checkout flow on multiple platforms, including Web, iOS, Android, and React Native. The most basic form of invoking a 3DS is via the payment provider (PSP) through which the transaction is being processed. This ties the transaction to that PSP and any subsequent retries of transaction with a different payment provider would need to re-invoke 3DS

#### Control the 3DS flows

In a typical [Payments Create API](https://api-reference.hyperswitch.io/v1/payments/payments--create#body-authentication-type) flow that triggers 3DS:

1. The user enters their payment information, which confirms a Payment, or attaches a Payment Method to a Customer.
2. Hyperswitch assesses if the transaction supports and requires 3DS intelligence engine, and other criteria.

To invoke 3DS through the underlying PSP pass the below parameter in the [Payments Create API ](https://api-reference.hyperswitch.io/v1/payments/payments--create#body-authentication-type)call&#x20;

```javascript
// Set authentication type in the Payments call
 "authentication_type": "three_ds"
```

Note - Certain PSPs do not support 3DS and require the merchant to perform authentication independently before sending the transaction.&#x20;
