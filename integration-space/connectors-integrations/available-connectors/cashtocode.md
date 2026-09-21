---
description: Connect CashToCode through Hyperswitch.
metaLinks:
  alternates:
    - cashtocode.md
---

# CashToCode

CashToCode settles payments as rewards rather than card or bank transactions, in two forms: Classic Reward and Evoucher. A payment either completes or it does not. There are no refunds, no cancellations, and no stored method to charge again later.

To connect CashToCode to your Hyperswitch account, follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for connector-specific behavior.

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7; host http://localhost:8080; fetched 2026-09-21; matrix canonical-json-v1 sha256 873f2bbfe94dc9fda3279d10e6c077a8fe4a10d38f97f3aba64d57093c5245c4; 146 connectors.
     Do not edit by hand. Payment method rows regenerate from the
     connector's SupportedPaymentMethods declaration; countries and
     currencies come from pm_filters in config/development.toml.
     Webhook flows and capture methods print as declared; the
     declaration-gap check reconciles them in prose. Edit those
     sources instead. -->

**Integration status:** live

**Category:** payment gateway

**Webhook flows:** payments

| Payment method | Type | Mandates | Refunds | Capture methods | Countries | Currencies |
|---|---|---|---|---|---|---|
| reward | Classic Reward | not supported | not supported | automatic, manual, sequential automatic | 249 | 160 |
| reward | Evoucher | not supported | not supported | automatic, manual, sequential automatic | 249 | 160 |

The table's currency count comes from the payment-method filters, not from CashToCode's credentials. Credentials exist for eleven currencies only, listed under Authentication, and a payment in any other currency has no credential set to authenticate with. Treat those eleven as the real list.

The matrix declares manual capture, but the capture flow is not implemented: [`build_request()`](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/cashtocode.rs#L347-L359) returns `FlowNotSupported`. Use automatic capture. Cancellation is unavailable for the same reason, at [`Void`](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/cashtocode.rs#L361-L373).

### Authentication

CashToCode credentials are scoped per currency, not per connector account. For each currency you accept, you supply two sets of three:

| Field | Classic Reward | Evoucher |
| --- | --- | --- |
| Username | **Username Classic** | **Username Evoucher** |
| Password | **Password Classic** | **Password Evoucher** |
| Merchant ID | **MerchantId Classic** | **MerchantId Evoucher** |

Eleven currencies are configured, each carrying its own set: AUD, CAD, CHF, CNY, EUR, GBP, INR, JPY, NZD, USD and ZAR. So a merchant accepting two currencies and both reward types fills in twelve values. The shape comes from [`cashtocode.connector_auth.CurrencyAuthKey`](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/connector_configs/toml/sandbox.toml), and the connector selects the set matching the payment's currency and reward type.

### Before you start

1. Register with CashToCode at [cashtocode.com](https://cashtocode.com/).
2. Obtain a username, password and merchant ID for each currency you plan to accept, and for each reward type you plan to offer. Both reward types in one currency means six values.
3. Sign in to the [Hyperswitch control center](https://app.hyperswitch.io/).
4. Enter those credentials during connector activation, and select automatic capture.
5. Enter your CashToCode webhook secret in **Source verification key**. Callbacks are rejected without it, and it is the only thing authenticating them. See [Webhooks](#webhooks).

### Webhooks

CashToCode posts a payment webhook, and two things about how Hyperswitch handles it are worth knowing before you rely on it.

**There is no event list.** Every callback that Hyperswitch accepts is treated as a successful payment. [`get_webhook_event_type()`](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/cashtocode.rs#L431-L441) returns `PaymentIntentSuccess` for any non-empty body and `EventNotSupported` only for an empty one. It never reads a status field, so there is no failure or pending event to handle.

Classification is not the whole check. A callback must also parse as the expected object and carry a `transactionId` naming a payment, at [`get_webhook_object_reference_id()`](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/cashtocode.rs#L417-L429); a malformed body or one with no usable reference is rejected before any payment is touched. So a callback has to be well formed and name a real payment, but if it is, it means success and nothing else.

**Verification is a shared secret in a header, not a signature.** CashToCode sends the secret in the `Authorization` header, and [`verify_webhook_source()`](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/cashtocode.rs#L387-L415) compares that header to your configured **Source verification key** as plain text. Nothing is computed over the body, so the check confirms the sender knows the secret and says nothing about what the body contains.

Two consequences follow. The secret travels in the clear on every callback, so anyone who can read one request, from a log or a proxy, holds it. And because a well-formed callback naming a real payment then counts as success, that secret is most of what it takes to drive a payment to succeeded. Treat the source verification key as a live credential and rotate it if a callback may have been logged.

There is no second opinion to fall back on. CashToCode does not implement payment sync: its [`PSync`](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/cashtocode.rs#L317-L336) leaves `build_request` at the interface default, which builds no request and returns `Ok(None)`, so Hyperswitch cannot re-check a payment after the fact. The callback is the only status signal, which is why the secret matters. Reconcile against CashToCode's own records rather than against Hyperswitch.

### Source reference

Authentication and webhook behavior on this page is tied to Hyperswitch `ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7`. See [CashToCode connector source](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/cashtocode.rs) and [CashToCode transformers](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/cashtocode/transformers.rs).
