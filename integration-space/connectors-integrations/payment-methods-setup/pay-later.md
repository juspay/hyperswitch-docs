---
description: Accept pay later options through Juspay Hyperswitch
icon: calendar-day
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/kf7BGdsPkCw9nalhAIlE/other-features/payment-orchestration/quickstart/payment-methods-setup/pay-later
---

# Pay Later

### Klarna, Affirm, Afterpay/Clearpay - Redirection flow

Juspay Hyperswitch supports multiple buy now pay later options:

* Klarna is a global buy now pay later payment method available in 23+ countries and supports 15+ currencies.
* Affirm is a buy now pay later payment method available to US customers and supports USD.
* Afterpay/Clearpay is a buy now pay later payment method available as Afterpay to customers in US, Canada, Australia, New Zealand while available as Clearpay to customers in the United Kingdom, Spain, France and Italy. It currently supports USD, CAD, AUD, NZD, EUR and GBP.

### How to configure pay later options (Redirection flow) on Juspay Hyperswitch?

1. Make sure that the pay later options are enabled on your connector's dashboard
2. Enable pay later options on Hyperswitch dashboard under "payment methods" tab while configuring your connector
3. Ensure that you add the additional mandatory parameters when you create a payment (using node SDK or /payments API) from your server-side.

```js
"email": "guest@example.com",
"shipping": {
        "address": {
            "line1": "1467",
            "line2": "Harrison Street",
            "line3": "Harrison Street",
            "city": "San Francisco",
            "state": "California",
            "zip": "94122",
            "country": "US",
            "first_name": "John",
            "last_name": "Doe"
        },
            "phone": {
            "number": "123456789",
            "country_code": "+1"
        }
    },
"billing": {
      "address": {
          "line1": "1467",
          "line2": "Harrison Street",
          "line3": "Harrison Street",
          "city": "San Francisco",
          "state": "California",
          "zip": "94122",
          "country": "US",
          "first_name": "John",
          "last_name": "Doe"
      },
          "phone": {
          "number": "123456789",
          "country_code": "+1"
      }
  }
```

### Klarna - In app flow

![Klarna Logo](https://hyperswitch.io/icons/homePageIcons/logos/klarnaLogo.svg)

Klarna In app flow in Juspay Hyperswitch is available if you configure Klarna as a payment processor. It provides a superior checkout flow for the customers compared to redirection flow.

To configure Klarna SDK flow, follow these steps. As a prerequisite, you would need to have a merchant account with Klarna. For Klarna SDK, you need to add a mandatory metaData object while creating a payment (/payments) from your server-side. The metaData object will look something like below.

```js
"metadata": {
      "order_details": {
        "product_name": "Apple iPhone 15",
        "quantity": 1
      }
    }
```

---

### Connector Capability Matrix

Sourced from each connector's `SupportedPaymentMethods` implementation in `crates/hyperswitch_connectors`.

| BNPL Method | Supported Connectors | Mandates | Refunds | Integration Mode |
| --- | --- | --- | --- | --- |
| **Klarna** | Adyen, Stripe, Mollie, Klarna (direct) | Adyen: ✓ · Others: ✗ | ✓ | Redirect or in-app SDK (Klarna direct only) |
| **Affirm** | Adyen, Stripe | ✗ | ✓ | Redirect |
| **Afterpay / Clearpay** | Adyen, Stripe | ✗ | ✓ | Redirect |
| **PayBright** | Adyen | ✗ | ✓ | Redirect (Canada) |
| **Walley** | Adyen | ✗ | ✓ | Redirect (Nordics) |
| **Alma** | Adyen | ✗ | ✓ | Redirect (France) |
| **Atome** | Adyen | ✗ | ✓ | Redirect (Southeast Asia) |

{% hint style="info" %}
**Mandates via Klarna on Adyen:** Adyen's Klarna integration supports mandate creation, allowing subsequent charges without customer interaction. All other connectors treat Klarna as a one-time payment — no mandate setup.
{% endhint %}

---

### Integration Modes

**Redirection flow (all BNPL methods)**
The customer is redirected to the BNPL provider's hosted page to complete identity verification and approval. After approval, they return to your site. Hyperswitch handles the redirect lifecycle automatically.

Required fields on payment create:
- `email` (mandatory for all BNPL providers)
- `billing.address` with `first_name`, `last_name`, `line1`, `city`, `state`, `zip`, `country`
- `shipping.address` (same fields as billing)
- `shipping.phone.number` and `country_code`

**Klarna in-app SDK flow (Klarna connector only)**
Klarna renders its own UI within your app — no redirect. Requires the Klarna connector (not Stripe or Adyen) and an additional `metadata.order_details` object on payment create:

```json
{
  "metadata": {
    "order_details": {
      "product_name": "Product Name",
      "quantity": 1
    }
  }
}
```

---

### Common Failure Modes

**Missing required fields**
Symptom: BNPL payment rejected before reaching the provider. Fix: All BNPL providers require `email`, full billing address, and full shipping address on the payment request. A missing `country` or `zip` field is the most common cause of pre-authorization rejection.

**BNPL method not available for customer's country**
Symptom: Payment method not shown at checkout or rejected at provider. Fix: Each BNPL method is country-scoped (e.g., Affirm is US-only, Walley is Nordics-only, Alma is France-focused). Ensure the customer's billing country matches the method's supported region and that the method is enabled in your connector dashboard for that market.

**Klarna in-app flow not rendering**
Symptom: Klarna SDK UI does not appear. Fix: Verify you are using the Klarna connector (not Stripe or Adyen) and that `metadata.order_details` with `product_name` and `quantity` is present on the payment create call.
