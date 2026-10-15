---
description: >-
  Drive checkout from your own backend and fetch the payment, its payment
  methods and the wallet session tokens in a single call
icon: server
metaLinks:
  alternates:
    - server-to-server-payments.md
---

<!-- truth manifest; hyperswitch 01365da86035c7bb6ebe99126443248d811cbcaf; spec api-reference/v1/openapi_spec_v1.json@01365da86035c7bb6ebe99126443248d811cbcaf
     symbols: X-Integration-Type header name = crates/common_utils/src/consts.rs:234 (X_INTEGRATION_TYPE, "x-integration-type"); annotated on both routes at crates/openapi/src/routes/payments.rs:639,695
     symbols: an absent or unrecognised header reads as client, matched case-insensitively after trim = crates/api_models/src/payments.rs:11217-11225
     symbols: MerchantIntegrationType client, server, client_and_server, default client = crates/common_enums/src/enums/accounts.rs:66-76
     symbols: merchant integration type config key system.payment_integration_type_<merchant id> = crates/router/src/consts.rs:425; crates/router/src/core/configs/dimension_config.rs:1106-1126
     symbols: accept or reject matrix and IR_06 rejection = crates/router/src/core/payments/server_integration.rs:90-111; crates/hyperswitch_domain_models/src/errors/api_error_response.rs:197-198
     symbols: create enriches when header is server and confirm is not true = crates/router/src/routes/payments.rs:137-142,204-221
     symbols: update enriches only for merchant API key auth = crates/router/src/routes/payments.rs:1001-1003,1061-1078
     symbols: sections built after the write, concurrently, 30 s each, failures inline = crates/router/src/core/payments/server_integration.rs:37-38,143-242
     symbols: vault session is per payment and shared with /session_tokens = crates/router/src/core/payments/server_integration.rs:283-286
     symbols: vault_details variants hyperswitch { sdk_authorization } and vgs { vault_id, environment } = crates/api_models/src/payments.rs:11338-11367
     symbols: CustomerPaymentMethodForClient.requires_cvv = crates/api_models/src/payment_methods.rs:3273
     symbols: confirm resolves a raw payment method id in payment_token only when modular payment methods are allowed; otherwise it is a redis token lookup = crates/router/src/core/payments/operations/payment_confirm.rs:1362-1418; crates/router/src/core/payments/helpers.rs:3588-3603
     checked: 2026-10-15 -->

# Server-to-Server Payments

Server-to-Server (S2S) Payments allow merchants to manage the checkout flow through their backend while using Hyperswitch for payment processing.

With `X-Integration-Type: server`, a single create call returns the payment together with the available payment methods, the customer's saved payment methods, and the wallet session tokens. Without it, checkout needs three separate calls to gather the same information. This integration suits custom checkout experiences across web, mobile, and other platforms.

## How it works

1. Your backend creates a payment with `X-Integration-Type: server`. The response includes the payment methods and session tokens.
2. If the amount or other payment details change, your backend updates the payment with the same header and gets refreshed payment methods and session tokens.
3. Your application displays the available methods and securely collects payment information.
4. Your backend confirms the payment.

For card payments, the Hyperswitch Payment Methods SDK tokenizes card details so your backend never handles raw card information.

## Prerequisites

Before integrating, ensure you have:

* An active Hyperswitch merchant account with payment processors configured.
* A merchant API key and publishable key.
* Server-side integration enabled for your merchant account.
* A customer identifier, if you intend to support saved payment methods.

### Enable server-side integration

Each merchant account has an integration type: `client` (the default), `server`, or `client_and_server`. Contact the Hyperswitch team to set your account to `server` or `client_and_server`.

If you self-host Hyperswitch, set it yourself with the admin API key:

```bash
curl --location 'https://your-hyperswitch-host/configs/' \
  --header 'api-key: YOUR_ADMIN_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '{
    "key": "system.payment_integration_type_YOUR_MERCHANT_ID",
    "value": "client_and_server"
  }'
```

### Integration type

Specify the integration type with the `X-Integration-Type` header when creating or updating payments.

| Header value | Behavior |
| --- | --- |
| `server` | The response also includes `payment_method_list` and `session_tokens`. |
| `client` | The standard payment response. |
| Not provided | Treated as `client`. |

The value is case-insensitive, and any value other than `server` or `client` is treated as `client`.

For server-side integrations, include:

```http
X-Integration-Type: server
```

Every create and update request checks the header against the account's integration type, and rejects a mismatch with HTTP `422`:

| Account integration type | `server` | `client` or not provided |
| --- | --- | --- |
| `client` (default) | Rejected | Accepted |
| `server` | Accepted | Rejected |
| `client_and_server` | Accepted | Accepted |

```json
{
  "error": {
    "type": "invalid_request",
    "message": "`x-integration-type` header value `server` does not match the merchant integration type `client`",
    "code": "IR_06"
  }
}
```

{% hint style="info" %}
Switching an account to `server` means requests without the header are rejected. Use `client_and_server` while you migrate existing callers.
{% endhint %}

### When the extra fields are returned

| API | Returned when |
| --- | --- |
| Payment Create | The header is `server` and the request does not set `"confirm": true` |
| Payment Update | The header is `server` and the request is authenticated with the merchant API key |

A create-and-confirm request returns the standard response, since a confirmed payment has no further use for payment methods or session tokens. Payment Update also accepts a publishable key with a client secret; those requests always get the standard response.

## Integration steps

### Step 1: Create or identify a customer

Create a customer using the Customers API to associate payments and saved payment methods with the customer. If the customer already exists, reuse their identifier.

**Endpoint:** `POST /customers`

```bash
curl --location 'https://sandbox.hyperswitch.io/customers' \
  --header 'api-key: YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '{
    "customer_id": "cus_abcdefgh",
    "name": "John Doe",
    "email": "guest@example.com"
  }'
```

Use the returned `customer_id` when creating the payment.

### Step 2: Create a payment

Create the payment with `X-Integration-Type: server`, without confirming it.

**Endpoint:** `POST /payments`

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
    "customer_id": "cus_abcdefgh"
  }'
```

In addition to standard payment details, the response includes:

| Field | Description |
| --- | --- |
| `payment_method_list` | Available payment methods and the customer's saved payment methods. Same object as [List Payment Methods](https://api-reference.hyperswitch.io/v1/payment-methods/list-payment-methods-for-a-payment-via-client-sdk). |
| `session_tokens` | Wallet session tokens and vault authorization details. Same object as [Create Session Tokens](https://api-reference.hyperswitch.io/v1/payments/payments--session-token). |

**Abbreviated example response:**

```json
{
  "payment_id": "pay_mbabizu24mvu3mela5njyhpit4",
  "status": "requires_payment_method",
  "amount": 6540,
  "currency": "USD",
  "customer_id": "cus_abcdefgh",
  "profile_id": "pro_abcdefghijklmnop",
  "payment_method_list": {
    "payment_methods_enabled": [
      {
        "payment_method": "card",
        "payment_method_type": "credit",
        "card_networks": ["Visa", "Mastercard"]
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
      "currency": "USD"
    }
  },
  "session_tokens": {
    "payment_id": "pay_mbabizu24mvu3mela5njyhpit4",
    "session_token": [],
    "vault_details": {
      "vault_type": "hyperswitch",
      "vault_data": {
        "sdk_authorization": "SDK_AUTHORIZATION_TOKEN"
      }
    }
  }
}
```

Store the returned `payment_id` for subsequent requests. Use `payment_method_list` to display available and saved payment methods, and `session_tokens` to initialize wallets and the Payment Methods SDK.

### Step 3: Update the payment if details change

Skip this step if nothing changes before confirmation. If the amount, currency, or other payment details change during checkout, update the payment with the same header. The response carries `payment_method_list` and `session_tokens` rebuilt for the new values; refresh what you display to the customer from it.

**Endpoint:** `POST /payments/{payment_id}`

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

The vault session is created once per payment, so `sdk_authorization` stays the same across create, update, and the standalone session tokens API. An SDK you already initialized keeps working after an update.

### Step 4: Collect payment details

For new card payments, use the [Hyperswitch Vault SDK](../workflows/vault/sdk-integration.md) to securely collect and tokenize card details.

The SDK authorization value is returned at:

```text
session_tokens.vault_details.vault_data.sdk_authorization
```

Pass the authorization value to the frontend and initialize the SDK. After tokenization, send the resulting payment method identifier to your backend for confirmation.

{% hint style="info" %}
`vault_type` is `hyperswitch` when cards are stored in the Hyperswitch vault. If your profile uses VGS as an external vault, `vault_details` is `{ "vault_type": "vgs", "vault_data": { "vault_id": "...", "environment": "..." } }` instead, and cards are collected with VGS.
{% endhint %}

**Saved payment methods:** For returning customers, `customer_payment_methods` contains previously saved methods, each with a `payment_token`. If `requires_cvv` is `true`, securely collect and tokenize the CVV through a supported SDK flow before confirmation. Do not send raw CVV to your backend unless your integration is explicitly designed and PCI DSS validated to handle it.

### Step 5: Confirm the payment

After the customer selects a payment method, confirm the payment through your backend.

**Endpoint:** `POST /payments/{payment_id}/confirm`

**Example — tokenized card:**

```bash
curl --location 'https://sandbox.hyperswitch.io/payments/pay_mbabizu24mvu3mela5njyhpit4/confirm' \
  --header 'api-key: YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '{
    "payment_method": "card",
    "payment_method_type": "credit",
    "payment_token": "PAYMENT_METHOD_IDENTIFIER"
  }'
```

{% hint style="warning" %}
Confirming with the payment method identifier returned by the Vault SDK requires the modular payment methods service to be enabled for your merchant account. Without it, `payment_token` only accepts the tokens returned in `customer_payment_methods`. Contact the Hyperswitch team to enable it.
{% endhint %}

For a saved payment method, send its `payment_token` from `customer_payment_methods` instead.

The response contains the payment status and applicable follow-up instructions.

| Status | Description |
| --- | --- |
| `succeeded` | Payment completed successfully. |
| `requires_customer_action` | Additional customer authentication is required. |
| `requires_payment_method` | A valid payment method is required. |
| `requires_capture` | Payment authorized and awaiting capture. |

If customer authentication is required, use the details in `next_action` to complete the flow.

## Error handling

`payment_method_list` and `session_tokens` are built after the payment is created or updated. If either cannot be built, it carries an `error` object instead of its data, and the request itself still succeeds:

```json
{
  "payment_id": "pay_mbabizu24mvu3mela5njyhpit4",
  "status": "requires_payment_method",
  "session_tokens": {
    "error": {
      "type": "api",
      "message": "Something went wrong",
      "code": "HE_00"
    }
  }
}
```

The two fields are built independently, each with a 30 second limit, so one failing does not affect the other. Check both fields for an `error` key before rendering payment options. If one fails, use the applicable standalone API to retrieve the missing information:

* [List Payment Methods](https://api-reference.hyperswitch.io/v1/payment-methods/list-payment-methods-for-a-payment-via-client-sdk)
* [Create Session Tokens](https://api-reference.hyperswitch.io/v1/payments/payments--session-token)

Keep your merchant API key on your backend. Use the SDK to collect sensitive card details and avoid handling raw card data on your servers unless required for your integration and supported by the appropriate PCI DSS controls.

## API references

* [Create Customer](https://api-reference.hyperswitch.io/v1/customers/customers--create)
* [Create Payment](https://api-reference.hyperswitch.io/v1/payments/payments--create)
* [Update Payment](https://api-reference.hyperswitch.io/v1/payments/payments--update)
* [Confirm Payment](https://api-reference.hyperswitch.io/v1/payments/payments--confirm)
* [Create Session Tokens](https://api-reference.hyperswitch.io/v1/payments/payments--session-token)
* [Vault SDK Integration](../workflows/vault/sdk-integration.md)
