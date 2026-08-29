---
name: hyperswitch-docs-activate-connector
description: Use this skill when the user asks "how do I add a connector in the Hyperswitch dashboard", "activate connector on Hyperswitch", "configure payment processor", "test a connector", "connector setup steps", "where do I enter my Stripe API key", "where do I find available connectors", "how do I enable payment methods for a connector", or needs step-by-step guidance for onboarding a new connector from the docs.
version: 1.0.0
tags: [hyperswitch, docs, connectors, setup, activation, payment-processor]
---

# Activate a Connector on Hyperswitch

## Overview

This skill walks through the connector activation workflow documented in the Hyperswitch docs — from selecting a connector to testing your first payment through it.

**Doc reference:** `explore-hyperswitch/connectors/activate-connector-on-hyperswitch/README.md`

---

## Step 1: Navigate to Connectors

1. Log in to [app.hyperswitch.io](https://app.hyperswitch.io)
2. Navigate to **Connectors → Payment Processors**
3. Browse the list of 143+ supported connectors
4. Click **Connect** next to your target connector

**Doc reference for available connectors:** `explore-hyperswitch/connectors/available-connectors/README.md`

---

## Step 2: Enter Credentials

Each connector requires specific credentials. Common patterns:

| Credential Type | Example Connectors |
|----------------|-------------------|
| Single API key | Stripe, most modern PSPs |
| API key + Merchant Account | Adyen |
| Key + Secret pair | Checkout.com, Braintree |
| Client ID + Secret | PayPal |

Enter credentials in **Test Mode** for sandbox. All test transactions are free.

---

## Step 3: Enable Payment Methods

After entering credentials:
1. Click **Payment Methods** tab
2. Toggle on the methods your checkout supports: Cards, Wallets, Bank Redirects, BNPL
3. For cards: select Visa, Mastercard, Amex, Discover as needed
4. Click **Save**

Only enabled payment methods are presented to customers.

---

## Step 4: Test a Payment

Run a test payment through the newly configured connector:

**Doc reference:** `explore-hyperswitch/connectors/activate-connector-on-hyperswitch/test-a-payment-with-connector.md`

```bash
curl --request POST \
  --url https://sandbox.hyperswitch.io/payments \
  --header 'api-key: YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '{
    "amount": 1000,
    "currency": "USD",
    "confirm": true,
    "capture_method": "automatic",
    "routing": { "type": "single", "data": { "connector": "stripe" } },
    "payment_method": "card",
    "payment_method_data": {
      "card": {
        "card_number": "4242424242424242",
        "card_exp_month": "03",
        "card_exp_year": "2030",
        "card_cvc": "737"
      }
    },
    "return_url": "https://example.com"
  }'
```

Verify `status: "succeeded"` and check the connector's dashboard to confirm the transaction appears.

---

## Available Connector Docs

The `explore-hyperswitch/connectors/available-connectors/` directory contains individual setup guides for every supported connector. Notable ones:

| Connector | Guide Path |
|-----------|-----------|
| Adyen | `available-connectors/adyen.md` |
| Braintree | `available-connectors/braintree.md` |
| Checkout.com | `available-connectors/checkout.md` |
| Cybersource | `available-connectors/cybersource/README.md` |
| GoCardless | `available-connectors/gocardless.md` |
| Klarna | `available-connectors/klarna.md` |
| Mollie | `available-connectors/mollie.md` |
| Stripe | (configured via standard API key) |

Each connector doc lists: required credentials, supported payment methods, test card numbers, and known quirks.

---

## Split Payments / Marketplace Connectors

For platform/marketplace payment splitting:

**Doc reference:** `explore-hyperswitch/connectors/split-payments/`

---

## Production Tips

- Add **at least two connectors** before going live. Single-connector setups have no fallback if the connector experiences downtime.
- Rotate API keys in the connector's dashboard and update in Hyperswitch simultaneously — there is a brief window where transactions may fail if keys are out of sync.
- Use **Business Profiles** to assign different connector sets to different product lines or geographies (Dashboard → Account Management → Profiles).
- Enable **Test Mode** / **Live Mode** toggle carefully — live mode processes real money. Verify your integration is fully tested before switching.
