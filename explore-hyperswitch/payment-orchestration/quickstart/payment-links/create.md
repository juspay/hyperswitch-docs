---
description: Create Payment Links
---

# Create Payment Links

Payment links are created using [Payments Create](https://api-reference.hyperswitch.io/api-reference/payments/payments--create) API. `payment_link` field should be sent as true in the request. Payment links cannot be confirmed during creation, hence `confirm` cannot be true.

Each field in the request uses a fallback logic. Below is the order of preference -

* Config sent during payment link creation
* Config set for the business profile
* Default values for payment link config

Refer to [this](../../../payment-flows-and-management/quickstart/payment-links/configurations/#list-of-defaults-for-the-payment-link-ui-config) section for a default UI for payment links.

## Create Payment link using business profile config

Creating a payment link uses the UI config set for the given profile in the request.

```
curl --location '{{BASE_URL}}/payments' \
    --header 'Content-Type: application/json' \
    --header 'api-key: {{API_KEY}}' \
    '{
        "amount": 100,
        "currency": "USD",
        "payment_link": true,
        "profile_id": "pro_YXlbYtgiANENrZgxdL8Q"
    }'
```

## Configure UI during Payment link creation

You can set payment link's UI during payment link creation.

```
curl --location '{{BASE_URL}}/payments' \
    --header 'Content-Type: application/json' \
    --header 'api-key: {{API_KEY}}' \
    '{
        "amount": 100,
        "currency": "USD",
        "payment_link": true,
        "profile_id": "pro_YXlbYtgiANENrZgxdL8Q",
        "payment_link_config": {
            "theme": "#4E6ADD",
            "logo": "https://hyperswitch.io/favicon.ico",
            "seller_name": "HyperSwitch Inc.",
            "sdk_layout": "accordion",
            "display_sdk_only": true,
            "enabled_saved_payment_method": true,
            "hide_card_nickname_field": true,
            "show_card_form_by_default": true,
            "payment_button_text": "Proceed to Payment!",
            "transaction_details": [
                {
                    "key": "Policy Number",
                    "value": "297472368473924",
                    "ui_configuration": {
                        "position": 5,
                        "is_key_bold": true,
                        "is_value_bold": true
                    }
                }
            ]
        }
    }'
```

## For using a specific style ID

If you've set multiple payment link configs in the profile, the style ID can be sent in `payment_link_config_id` during payment link creation.

```
curl --location '{{BASE_URL}}/payments' \
    --header 'Content-Type: application/json' \
    --header 'api-key: {{API_KEY}}' \
    '{
        "amount": 100,
        "currency": "USD",
        "payment_link": true,
        "profile_id": "pro_YXlbYtgiANENrZgxdL8Q",
        "payment_link_config_id": "style1"
    }'
```

### Next step:

{% content-ref url="secure-payment-links.md" %}
[secure-payment-links.md](secure-payment-links.md)
{% endcontent-ref %}
