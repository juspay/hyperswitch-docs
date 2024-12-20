---
description: Create Payment Links
---

Payment links are created using [Payments Create](https://api-reference.hyperswitch.io/api-reference/payments/payments--create) API. `payment_link` field should be sent as true in the request. Payment links cannot be confirmed during creation, hence `confirm` cannot be true.

Each field in the request uses a fallback logic. Preference is always given to the config sent in the payment create request, next to the business profile config and default config is used as a fallback. Refer to [this](explore-hyperswitch/payment-flows-and-management/quickstart/payment-link/configurations.md) section for a default UI for payment links.

# Create default Payment links

Creating a payment link uses the configured UI config for the given profile in the request.

{% code %}
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
{% endcode %}

# Configure UI during Payment link creation

Payment link's UI can be configured on-demand during payment link creation as well.

{% code %}
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
{% endcode %}

# For using a specific style ID

{% code %}
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
{% endcode %}

## Next step:

{% content-ref url="./secure-payment-links.md" %}
[Secure Payment links](./secure-payment-links.md)
{% endcontent-ref %}
