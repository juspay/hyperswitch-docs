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

3. If 3DS is:
   1. Not required: For example, because of an [exemption](3ds-intelligence-engine/), Hyperswitch attempts the payment as a non-3DS transaction. The Payment transitions to a status of `succeeded`. If requested by the issuer with a soft decline, we automatically reattempt and continue as if required.
   2. Not supported: The Payment is tried as a non-3DS transaction by default. However, if the merchant explicitly specifies the above authentication\_type flag as three\_ds then the payment would fail.&#x20;
   3. Required: Hyperswitch starts the 3DS authentication flow by contacting the card issuer’s 3DS Access Control Server (ACS) and starting the 3DS flow
4. When 3DS flow information is received from the issuer the status of transaction moves to `requires_customer_action`
   1. Issuers may initiate multiple 3DS flow types, and these do not always surface a customer challenge. For example, authentication may complete via a frictionless flow.
   2. Most data required for a 3DS authentication request is typically collected from the customer during the transaction. To minimize friction and reduce the likelihood of authentication failures, we may enrich the request using additional signals. These can include information gathered during the payment flow.
   3. When Hyperswitch already has sufficient data to attempt authentication, we may automatically initiate the authentication process while confirming the Payment. If authentication succeeds, the Payment can move directly to a `succeeded` state. If further customer interaction or additional data is required, the Payment transitions to `requires_customer_action` to complete the 3DS flow. \
      \
      Inspect the  `next_action`. If it contains `redirect_to_url`, that means 3DS is required. In the browser, redirect the customer to the `redirect_to_url` to complete authentication.

```javascript
// Redirect customer to redirect url to complete authentication in case of a challenge flow
 "next_action": {
        "type": "redirect_to_url",
        "redirect_to_url": "https://sandbox.hyperswitch.io/api/payments/redirect/pay_l45HmzZ4mVgP3B4lBz1x/juspay222/pay_l45HmzZ4mVgP3B4lBz1x"
    },
```

When the customer finishes the authentication process, the redirect sends them back to the `return_url` you specified when you [created](https://api-reference.hyperswitch.io/v1/payments/payments--create#body-return-url-one-of-0) or [confirmed](https://api-reference.hyperswitch.io/v1/payments/payments--confirm#body-return-url-one-of-0) the Payment.

5. Depending on the 3DS authentication result:
   1. Authenticated: The Payment transitions to a status of `succeeded`.
   2. Failure: The Payment transitions to a status of `requires_payment_method`, indicating that you need to try a different payment method, or you can retry 3DS by reconfirming.
