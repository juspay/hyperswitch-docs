---
description: Secure payment links
---

Payment links which are embedded in an iframe of a trusted domain are secure payment links. These links can only be embedded in an iframe and cannot be directly opened in a browser tab. Customers can view their saved payment methods and also save new payment methods in this link.

# Using secure Payment links

A list of trusted allowed domains must be configured in business profile for provisioning secure payment links. Once `allowed_domains` are configured, creating payment links will give back two URLs - one for open payment links which can be opened in a browser tab, and a secure link which can only be embedded in an iframe of a parent HTML. Domain name of the parent webpage should be configured in the `allowed_domains` field in business profile.

#### Steps for using secure payment links

**1. Configure `allowed_domains` in business profile**

Below configuration sets up `localhost:5500` as trusted domain.

{% code fullWidth="true" %}
```
curl --location '{{BASE_URL}}/account/{{MERCHANT_ID}}/business_profile/{{PROFILE_ID}}' \
    --header 'Content-Type: application/json' \
    --header 'api-key: {{ADMIN_API_KEY}}' \
    '{
        "payment_link_config": {
            "allowed_domains": [
                "localhost:5500"
            ]
        }
    }'
```
{% endcode %}

**2. Create payment links**

{% code fullWidth="true" %}
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

This returns back two links in the response

{% code fullWidth="true" %}
```
{
  ...

  "payment_link": {
    "link": "http://localhost:8080/payment_link/merchant_1734676749/pay_Dw4CBoUWGGkvSXcfz1Mu?locale=en",
    "secure_link": "http://localhost:8080/payment_link/s/merchant_1734676749/pay_Dw4CBoUWGGkvSXcfz1Mu?locale=en",
    "payment_link_id": "plink_lF9deXMRrdIEs1drMVhF"
  },

  ...
}
```
{% endcode %}

**3. Embedding secure payment links in an iframe**

{% code fullWidth="true" %}
```
<html>
  <head>
    <style>
      html,
      body {
        margin: 0;
        height: 100vh;
        width: 100vw;
        display: flex;
        justify-content: center;
        align-items: center;
        background-color: bisque;
      }
      iframe {
        border-radius: 4px;
        height: 80vh;
        width: 80vw;
      }
    </style>
  </head>
  <body>
    <iframe
      src="http://localhost:8080/payment_link/s/merchant_1734676749/pay_Dw4CBoUWGGkvSXcfz1Mu?locale=en"
      frameborder="0"
    ></iframe>
  </body>
</html>
```
{% endcode %}

## Next step:

{% content-ref url="./setup-custom-domain.md" %}
[Setup Custom Domain](./setup-custom-domain.md)
{% endcontent-ref %}
