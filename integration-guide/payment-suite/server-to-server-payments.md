---
description: >-
  Drive checkout from your own backend and fetch the payment, its payment
  methods and the wallet session tokens in a single call
icon: server
---

# Server to Server Payments

In a server-to-server integration your backend orchestrates checkout. It holds the merchant API key, calls Hyperswitch, and hands the result to whatever renders the payment screen: your own UI, a mobile app, or a partner surface.

The difficulty is that a checkout screen needs three things before it can render anything.

1. The payment itself
2. The payment methods available for it, including the customer's saved cards
3. The wallet session tokens

Fetched separately, that is three sequential round trips, with the client secret threaded through two of them. Sending `X-Integration-Type: server` on the payments update call collapses it into one.

## How it compares

<table><thead><tr><th width="220">Client integration</th><th>Server integration</th></tr></thead><tbody><tr><td>The SDK runs in the browser or app and fetches what it needs</td><td>Your backend fetches everything and renders checkout itself</td></tr><tr><td>Three calls before rendering</td><td>One call before rendering</td></tr><tr><td>Publishable key and client secret reach the client</td><td>Merchant API key stays on your server</td></tr><tr><td>Header is <code>client</code>, or absent</td><td>Header is <code>server</code></td></tr></tbody></table>

Reach for a client integration when the Hyperswitch SDK drives checkout, because it already fetches what it needs. Reach for a server integration when your backend is in charge and you would rather make one call than three.

## The header

| Value               | What comes back                                                    |
| ------------------- | ------------------------------------------------------------------ |
| `server`            | The payment, plus `payment_method_list` and `session_tokens`        |
| `client`, or absent | The payment response, unchanged                                     |

{% hint style="info" %}
The header is honoured only with merchant API key authentication. This route also accepts a publishable key with a client secret, and a caller authenticated that way gets the ordinary response even if it sends `server`. An unrecognised value reads as `client`, so a typo gives you the ordinary response rather than an error.
{% endhint %}

## Step 1: Create the payment

Create the intent without confirming it.

```bash
curl --location 'https://sandbox.hyperswitch.io/payments' \
  --header 'api-key: YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '{
    "amount": 6540,
    "currency": "USD",
    "confirm": false,
    "capture_method": "automatic",
    "customer_id": "cus_abcdefgh",
    "email": "guest@example.com"
  }'
```

Keep the `payment_id` and `client_secret` from the response.

```json
{
  "payment_id": "pay_mbabizu24mvu3mela5njyhpit4",
  "status": "requires_payment_method",
  "amount": 6540,
  "currency": "USD",
  "client_secret": "pay_mbabizu24mvu3mela5njyhpit4_secret_el9ksDkiB8hi6j9N78yo",
  "customer_id": "cus_abcdefgh",
  "profile_id": "pro_abcdefghijklmnop"
}
```

## Step 2: Fetch everything your checkout needs

Update the intent with the header set. You can change real fields in the same call, or send only what you want to change. The sections are attached either way.

```bash
curl --location 'https://sandbox.hyperswitch.io/payments/pay_mbabizu24mvu3mela5njyhpit4' \
  --header 'api-key: YOUR_API_KEY' \
  --header 'X-Integration-Type: server' \
  --header 'Content-Type: application/json' \
  --data '{
    "amount": 7654
  }'
```

The response is the payment you already know, with two sections added.

```json
{
  "payment_id": "pay_mbabizu24mvu3mela5njyhpit4",
  "status": "requires_payment_method",
  "amount": 7654,
  "currency": "USD",
  "client_secret": "pay_mbabizu24mvu3mela5njyhpit4_secret_el9ksDkiB8hi6j9N78yo",
  "customer_id": "cus_abcdefgh",

  "payment_method_list": {
    "payment_methods_enabled": [
      {
        "payment_method": "card",
        "payment_method_type": "credit",
        "card_networks": ["Visa", "Mastercard"],
        "customer_acceptance_support": "supported"
      }
    ],
    "customer_payment_methods": [
      {
        "payment_token": "token_7ebf443fa0504067",
        "payment_method": "card",
        "payment_method_type": "credit",
        "requires_cvv": true,
        "payment_method_data": {
          "card": {
            "last4_digits": "4242",
            "card_network": "Visa",
            "expiry_month": "12",
            "expiry_year": "2030"
          }
        }
      }
    ],
    "sdk_next_action": { "next_action": "confirm" },
    "intent_data": {
      "payment_id": "pay_mbabizu24mvu3mela5njyhpit4",
      "status": "requires_payment_method",
      "amount": 7654,
      "currency": "USD"
    }
  },

  "session_tokens": {
    "payment_id": "pay_mbabizu24mvu3mela5njyhpit4",
    "client_secret": "pay_mbabizu24mvu3mela5njyhpit4_secret_el9ksDkiB8hi6j9N78yo",
    "session_token": [],
    "vault_details": {
      "vault_type": "hyperswitch",
      "vault_data": {
        "sdk_authorization": "cHJvZmlsZV9pZD1wcm9mXzEyMyxwdWJsaXNoYWJsZV9rZXk9cGtfbGl2ZV8xMjM="
      }
    }
  }
}
```

`payment_method_list` is the same object [List payment methods for a payment](https://api-reference.hyperswitch.io/v1/payment-methods/list-payment-methods-for-a-payment-via-client-sdk) returns, and `session_tokens` is the same object [Create session tokens](https://api-reference.hyperswitch.io/v1/payments/payments--session-token) returns. Anything already parsing those responses works unchanged.

## Step 3: Confirm

Render your checkout from those two sections, then confirm. A saved card is confirmed with the `payment_token` that came back in `customer_payment_methods`.

```bash
curl --location 'https://sandbox.hyperswitch.io/payments/pay_mbabizu24mvu3mela5njyhpit4/confirm' \
  --header 'api-key: YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '{
    "payment_method": "card",
    "payment_method_type": "credit",
    "payment_token": "token_7ebf443fa0504067"
  }'
```

## When a section cannot be built

The payment write has already committed by the time these sections are built. A section that fails therefore reports its own error inline rather than failing the whole request, so a committed state change is never hidden from you by a problem in a read that came after it.

```json
{
  "payment_id": "pay_mbabizu24mvu3mela5njyhpit4",
  "status": "requires_payment_method",
  "amount": 7654,

  "payment_method_list": {
    "payment_methods_enabled": [],
    "customer_payment_methods": [],
    "sdk_next_action": { "next_action": "confirm" },
    "intent_data": { "payment_id": "pay_mbabizu24mvu3mela5njyhpit4" }
  },

  "session_tokens": {
    "error": {
      "type": "api",
      "message": "Something went wrong",
      "code": "HE_00"
    }
  }
}
```

Check each section for an `error` key before using it. The payment is unaffected, so you can proceed with the section that arrived and either retry the other or fall back to its standalone endpoint.

{% hint style="success" %}
Adding the header never changes the payment itself. The same update sent with `client`, or with no header at all, does exactly the same thing to the payment; only the response shape differs. An existing integration that has never heard of this header is unaffected.
{% endhint %}

## Related

* [Payments - Update API reference](https://api-reference.hyperswitch.io/v1/payments/payments--update)
* [Server to Server payments in the API reference](https://api-reference.hyperswitch.io/v1/payments/payments--server-to-server)
* [Token Led Payment](payment-method-card/payments.md)
