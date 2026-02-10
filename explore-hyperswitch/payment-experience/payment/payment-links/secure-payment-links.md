---
description: Secure payment links
---

# Secure Payment Links

Secure payment links are those embedded within the iframe of a trusted domain. These links cannot be directly opened in a browser tab and are designed to provide a safe environment for users to view and save their payment methods.

## Using secure Payment links

To use secure payment links, you need to configure a list of trusted domains in the business profile under the `allowed_domains` field. Once set up, any payment link you create will include two URLs:

1. An open link for direct browser access.
2. A secure link intended for embedding in an iframe.

The domain of the parent webpage embedding the secure link must match one of the domains listed in `allowed_domains`.

**Steps for using secure payment links**

**1. Configure `allowed_domains` in business profile**

Set up a trusted domain, such as `localhost:5500`, by updating the business profile configuration.

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

**2. Create payment links**

Use the following API request to create payment links, which will return both the open and secure links.

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

The response includes the following fields:

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

**3. Embedding secure payment links in an iframe**

To embed a secure payment link, include it in an iframe within your HTML:

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

### Next step:

{% content-ref url="setup-custom-domain.md" %}
[setup-custom-domain.md](setup-custom-domain.md)
{% endcontent-ref %}
