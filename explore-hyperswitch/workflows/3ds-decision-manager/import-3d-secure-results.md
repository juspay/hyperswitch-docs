---
description: Process payments when 3D Secure runs outside Hyperswitch
icon: shield-slash
---

# Import 3D Secure results

Importing 3DS results is an advanced payment flow that enables you to use external 3DS authentication with your Hyperswitch payments. Instead of running authentication within Hyperswitch, you can pass the completed authentication outcome directly into the payment flow.

This approach is required when you use a third party provider to perform 3DS. In such cases, you can submit the card details and authentication cryptogram directly through the [Payment Create API](https://api-reference.hyperswitch.io/v1/payments/payments--create#body-three-ds-data), rather than relying on Hyperswitch SDK to collect payment information and execute 3DS.

#### Process a payment&#x20;

1. Make a [Payments Create API](https://api-reference.hyperswitch.io/v1/payments/payments--create#body-three-ds-data) call with the external 3d Secure (3DS) data

```javascript
// Pass the authentication data in the Payments Create call
 "three_ds_data": {
        "authentication_cryptogram": {
            "cavv": {
                "authentication_cryptogram": "3q2+78r+ur7erb7vyv66vv////8="
            }
        },
        "ds_trans_id": "c4e59ceb-a382-4d6a-bc87-385d591fa09d",
        "version": "2.1.0",
        "eci": "05",
        "transaction_status": "Y",
        "exemption_indicator": "low_value"
    }
```

2. All [standard payment flows](../../../about-hyperswitch/payment-suite-1/payments/) are supported even when you import external 3DS results
