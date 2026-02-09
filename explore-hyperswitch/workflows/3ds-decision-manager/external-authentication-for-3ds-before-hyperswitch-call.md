---
icon: shield-slash
---

# External Authentication for 3DS (before Hyperswitch call)

Multiple business invoke 3DS before calling Hyperswitch. They use Juspay 3DS server or any other independent 3DS server to authenticate the transaction before the /payments via Hyperswitch

#### Passing 3DS via payments&#x20;

```javascript
// Set authentication type in the Payments call
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

Refer to the API payload [here](https://api-reference.hyperswitch.io/v1/payments/payments--create#body-three-ds-data)
