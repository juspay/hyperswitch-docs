---
description: >-
  Drive checkout from your own backend and fetch the payment, its payment
  methods and the wallet session tokens in a single call
icon: server
metaLinks:
  alternates:
    - server-to-server-payments.md
---

# Server to Server Payments

In a server-to-server integration your backend orchestrates checkout. It holds the merchant API key, calls Hyperswitch, and hands the result to whatever renders the payment screen: your own UI, a mobile app, or a partner surface.

The difficulty is that a checkout screen needs three things before it can render anything.

1. The payment itself
2. The payment methods available for it, including the customer's saved cards
3. The wallet session tokens

Fetched separately, that is three sequential round trips, with the client secret threaded through two of them. Sending `X-Integration-Type: server` collapses them into one.

## How it compares

<table><thead><tr><th width="220">Client integration</th><th>Server integration</th></tr></thead><tbody><tr><td>The SDK runs in the browser or app and fetches what it needs</td><td>Your backend fetches everything and renders checkout itself</td></tr><tr><td>Three calls to gather what checkout needs</td><td>One call to gather what checkout needs</td></tr><tr><td>Publishable key and client secret reach the client</td><td>Merchant API key stays on your server</td></tr><tr><td>Header is <code>client</code>, or absent</td><td>Header is <code>server</code></td></tr></tbody></table>

Reach for a client integration when the Hyperswitch SDK drives checkout, because it already fetches what it needs. Reach for a server integration when your backend is in charge and you would rather gather everything in one call than three.

## The header

`X-Integration-Type` is accepted on both the create and the update call.

| Value               | What comes back                                                    |
| ------------------- | ------------------------------------------------------------------ |
| `server`            | The payment, plus `payment_method_list` and `session_tokens`        |
| `client`, or absent | The payment response, unchanged                                     |

{% hint style="info" %}
The header is honoured only with merchant API key authentication. The update call also accepts a publishable key with a client secret, and a caller authenticated that way gets the ordinary response even if it sends `server`. An unrecognised value reads as `client`, so a typo gives you the ordinary response rather than an error.
{% endhint %}

{% hint style="info" %}
On create, the header applies to an unconfirmed intent. A create-and-confirm request, meaning one that sends `"confirm": true`, returns the ordinary response, because a payment that has already been confirmed has no use for a payment-method list or wallet session tokens.
{% endhint %}

## Step 1: Create the customer

Create the customer first so the payment can be attached to it. This is what lets the payment-method list come back with the customer's saved cards, and what lets a card tokenized during this checkout be reused later.

```bash
curl --location 'https://sandbox.hyperswitch.io/customers' \
  --header 'api-key: YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '{
    "customer_id": "cus_abcdefgh",
    "name": "John Doe",
    "email": "guest@example.com",
    "phone": "9123456789",
    "phone_country_code": "+1",
    "description": "First time shopper"
  }'
```

```json
{
  "customer_id": "cus_abcdefgh",
  "name": "John Doe",
  "email": "guest@example.com",
  "phone": "9123456789",
  "phone_country_code": "+1",
  "description": "First time shopper",
  "address": null,
  "created_at": "2026-09-16T10:12:33.456Z",
  "metadata": null,
  "default_payment_method_id": null
}
```

Keep the `customer_id`. If you already have one, skip this step and reuse it.

{% hint style="info" %}
Omit `customer_id` from the request and Hyperswitch generates one for you. Reuse the same `customer_id` across visits so saved cards follow the customer.
{% endhint %}

## Step 2: Create the payment and fetch everything

Create the intent against that customer, without confirming it, with the header set.

```bash
curl --location 'https://sandbox.hyperswitch.io/payments' \
  --header 'api-key: YOUR_API_KEY' \
  --header 'X-Integration-Type: server' \
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

The response is the payment you already know, with two sections added. Keep the `payment_id`, and keep `session_tokens.vault_details` for Step 4.

```json
{
  "payment_id": "pay_mbabizu24mvu3mela5njyhpit4",
  "status": "requires_payment_method",
  "amount": 6540,
  "currency": "USD",
  "client_secret": "pay_mbabizu24mvu3mela5njyhpit4_secret_el9ksDkiB8hi6j9N78yo",
  "customer_id": "cus_abcdefgh",
  "profile_id": "pro_abcdefghijklmnop",

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
      "amount": 6540,
      "currency": "USD",
      "client_secret": "pay_mbabizu24mvu3mela5njyhpit4_secret_el9ksDkiB8hi6j9N78yo",
      "customer_id": "cus_abcdefgh",
      "email": "guest@example.com",
      "setup_future_usage": null,
      "return_url": null
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

`payment_method_list` is the object [List payment methods for a payment](https://api-reference.hyperswitch.io/v1/payment-methods/list-payment-methods-for-a-payment-via-client-sdk) returns, including `intent_data`, which repeats the intent fields the checkout screen needs so you do not have to thread them through yourself. `session_tokens` is the same object [Create session tokens](https://api-reference.hyperswitch.io/v1/payments/payments--session-token) returns. Anything already parsing those responses works unchanged.

A returning customer's saved cards arrive in `customer_payment_methods`, each with a `payment_token`. If the customer picks one of those, skip Step 4 and confirm with that token. Check `requires_cvv` first: when it is `true`, collect the CVV and send it alongside the token, as the [saved card](#confirming-a-saved-card) example shows.

## Step 3: Update the payment, only if something changed

Skip this step unless a field on the intent actually changes, for example the basket total or the currency. Send the same header and both sections come back refreshed against the new values. If you do run it, use this response for the rest of the flow: its `session_tokens` and `payment_method_list` supersede the ones from Step 2.

```bash
curl --location 'https://sandbox.hyperswitch.io/payments/pay_mbabizu24mvu3mela5njyhpit4' \
  --header 'api-key: YOUR_API_KEY' \
  --header 'X-Integration-Type: server' \
  --header 'Content-Type: application/json' \
  --data '{
    "amount": 7654,
    "currency": "USD"
  }'
```

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
      "currency": "USD",
      "client_secret": "pay_mbabizu24mvu3mela5njyhpit4_secret_el9ksDkiB8hi6j9N78yo",
      "customer_id": "cus_abcdefgh",
      "email": "guest@example.com",
      "setup_future_usage": null,
      "return_url": null
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

## Step 4: Collect the card with the Payment Methods SDK

Card details never touch your server. The `sdk_authorization` inside `vault_details` is the vault session the Payment Methods SDK needs, so you do not have to call `/payment-method-sessions` separately — the call you just made already handed it to you. Take it from the most recent response: Step 3's if you ran it, otherwise Step 2's.

Pass it to your frontend, add a placeholder for the widget, and mount it.

```html
<form id="payment-methods-management-form">
  <div id="payment-methods-management-elements">
    <!--HyperLoader injects the Payment Methods Management SDK-->
  </div>
</form>
```

```javascript
// sdkAuthorization comes from your server, lifted out of the latest response:
//   session_tokens.vault_details.vault_data.sdk_authorization
let hyper;
let paymentMethodsManagementElements;

function initialize(sdkAuthorization) {
  const script = document.createElement("script");
  script.type = "text/javascript";
  script.src = "https://beta.hyperswitch.io/v1/HyperLoader.js";

  script.onload = () => {
    hyper = window.Hyper({
      publishableKey: "YOUR_PUBLISHABLE_KEY",
      profileId: "YOUR_PROFILE_ID",
    });

    paymentMethodsManagementElements = hyper.paymentMethodsManagementElements({
      appearance: { theme: "default" },
      sdkAuthorization: sdkAuthorization,
    });

    const paymentMethodsManagement = paymentMethodsManagementElements.create(
      "paymentMethodsManagement"
    );
    paymentMethodsManagement.mount("#payment-methods-management-elements");
  };

  document.body.appendChild(script);
}

// Call it with the value your server passed to the page.
initialize(sdkAuthorization);
```

When the customer submits, call `confirmTokenization()`. The card is tokenized inside the Hyperswitch-hosted iframe and you get a token back.

```javascript
const response = await hyper.confirmTokenization({
  paymentMethodsManagementElements,
  confirmParams: {
    return_url: "https://example.com/complete",
  },
  redirect: "if_required",
});

if (response?.id) {
  // Send this to your server; it is what Step 5 confirms with.
  await fetch("/complete-payment", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ token: response.id }),
  });
} else {
  showError(response?.error?.message ?? "An unexpected error occurred.");
}
```

`YOUR_PUBLISHABLE_KEY` comes from the dashboard under Developers, and `YOUR_PROFILE_ID` is the `profile_id` on the Step 2 response. Never send your API key to the browser.

{% hint style="info" %}
For the full SDK walkthrough, including appearance customization and error handling, see [Vault SDK Integration](../workflows/vault/sdk-integration.md).
{% endhint %}

## Step 5: Confirm

Confirm from your server with the merchant API key and the token your frontend sent back from Step 4, the `response.id` of `confirmTokenization()`.

```bash
curl --location 'https://sandbox.hyperswitch.io/payments/pay_mbabizu24mvu3mela5njyhpit4/confirm' \
  --header 'api-key: YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '{
    "payment_method": "card",
    "payment_method_type": "credit",
    "payment_token": "<token from confirmTokenization()>"
  }'
```

### Confirming a saved card

A returning customer who picked a saved card never goes through Step 4. Confirm with that card's `payment_token` from `customer_payment_methods` instead. When the card came back with `"requires_cvv": true`, collect the CVV and send it in `payment_method_data.card_token`.

```bash
curl --location 'https://sandbox.hyperswitch.io/payments/pay_mbabizu24mvu3mela5njyhpit4/confirm' \
  --header 'api-key: YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '{
    "payment_method": "card",
    "payment_method_type": "credit",
    "payment_token": "token_7ebf443fa0504067",
    "payment_method_data": {
      "card_token": {
        "card_cvc": "123"
      }
    }
  }'
```

Collect that CVV through the SDK rather than your own form, so the value never reaches your server. Cards that come back with `"requires_cvv": false` confirm with the token alone.

```json
{
  "payment_id": "pay_mbabizu24mvu3mela5njyhpit4",
  "status": "succeeded",
  "amount": 6540,
  "amount_received": 6540,
  "currency": "USD",
  "customer_id": "cus_abcdefgh",
  "connector": "stripe",
  "payment_method": "card",
  "payment_method_type": "credit",
  "payment_method_id": "pm_9Xn4KkTgVqLmZpRsWbYc",
  "connector_transaction_id": "pi_3PqR4s2eZvKYlo2C1gFJbEwX",
  "profile_id": "pro_abcdefghijklmnop",
  "error_code": null,
  "error_message": null,
  "next_action": null,
  "created": "2026-09-16T10:12:41.882Z"
}
```

A `status` of `succeeded` means the payment is done. If the card needs 3DS, `status` comes back as `requires_customer_action` with a `next_action` telling you where to send the customer.

## When a section cannot be built

The payment write has already committed by the time these sections are built. A section that fails therefore reports its own error inline rather than failing the whole request, so a committed state change is never hidden from you by a problem in a read that came after it.

```json
{
  "payment_id": "pay_mbabizu24mvu3mela5njyhpit4",
  "status": "requires_payment_method",
  "amount": 6540,

  "payment_method_list": {
    "payment_methods_enabled": [],
    "customer_payment_methods": [],
    "sdk_next_action": { "next_action": "confirm" }
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
Adding the header never changes the payment itself. The same request sent with `client`, or with no header at all, does exactly the same thing to the payment; only the response shape differs. An existing integration that has never heard of this header is unaffected.
{% endhint %}

## Related

* [Customers - Create API reference](https://api-reference.hyperswitch.io/v1/customers/customers--create)
* [Payments - Create API reference](https://api-reference.hyperswitch.io/v1/payments/payments--create)
* [Payments - Update API reference](https://api-reference.hyperswitch.io/v1/payments/payments--update)
* [Payments - Confirm API reference](https://api-reference.hyperswitch.io/v1/payments/payments--confirm)
* [Vault SDK Integration](../workflows/vault/sdk-integration.md)
* [Server to Server payments in the API reference](https://api-reference.hyperswitch.io/v1/payments/payments--server-to-server)
