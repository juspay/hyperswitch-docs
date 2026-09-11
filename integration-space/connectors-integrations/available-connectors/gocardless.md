---
description: Configure GoCardless bank debit payments with Hyperswitch.
metaLinks:
  alternates:
    - gocardless.md
---

# GoCardless

ACH, BECS, and SEPA Direct Debit define the GoCardless payment gateway route. Mandates and refunds apply to every bank debit method. Capture stays automatic or sequential automatic throughout.

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch a17a23c4c4c907d2314043a32a9f505f7f2bd4f9; host http://localhost:8080; fetched 2026-09-10; matrix canonical-json-v1 sha256 36360b019f2761dd; 138 connectors.
     Do not edit by hand. This block regenerates from the connector's
     SupportedPaymentMethods declaration in code; edit that instead. -->

**Integration status:** sandbox

**Category:** payment gateway

**Webhook flows:** mandates, payments, refunds

| Payment method | Type | Mandates | Refunds | Capture methods | Countries | Currencies |
|---|---|---|---|---|---|---|
| bank debit | ACH Direct Debit | supported | supported | automatic, sequential automatic | USA | USD |
| bank debit | BECS Direct Debit | supported | supported | automatic, sequential automatic | AUS | AUD |
| bank debit | SEPA Direct Debit | supported | supported | automatic, sequential automatic | 30 ([full list](https://hyperswitch.io/pm-list)) | 7 ([full list](https://hyperswitch.io/pm-list)) |

### Before you start

1. Create a GoCardless sandbox account.
2. Sign in to the [Hyperswitch control center](https://app.hyperswitch.io/) or create your Hyperswitch account.
3. In the GoCardless dashboard, go to **Developers > Create > Access Token** and create or copy your Access Token.
4. Enable the same payment methods in GoCardless and in your Hyperswitch connector configuration.

To connect GoCardless to your Hyperswitch account, follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for what GoCardless supports.

### Connector-Specific Notes

Hyperswitch sends `GoCardless-Version: 2015-07-06` on connector requests. This pins the API version used by the implementation. See [`GOCARDLESS_VERSION`](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/gocardless.rs#L85-L110).

### Authentication

Provide an `<access token>`. The `HeaderKey` mapping assigns `api_key` to the access token, and every connector request sends `Authorization: Bearer <access token>`. See [`GocardlessAuthType::try_from()`](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/gocardless/transformers.rs#L635-L649) and [`get_auth_header()`](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/gocardless.rs#L131-L142).

### Webhooks

Configure a `<webhook signing secret>` for source verification. Hyperswitch reads a hex-encoded signature from `Webhook-Signature` and verifies HMAC-SHA256 over the raw request body using the configured `merchant_secret`. See [`get_webhook_source_verification_signature()`](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/gocardless.rs#L719-L753) and [`verify_webhook_source()`](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_interfaces/src/webhooks.rs#L265-L301).

The connector maps 30 webhook action values:

| Resource | Wire action value | Effect |
|---|---|---|
| Payments | `created` | Payment is processing |
| Payments | `customer_approval_granted` | Payment is processing |
| Payments | `customer_approval_denied` | Payment fails |
| Payments | `submitted` | Payment is processing |
| Payments | `confirmed` | Payment succeeds |
| Payments | `paid_out` | Payment succeeds |
| Payments | `late_failure_settled` | Payment fails |
| Payments | `surcharge_fee_debited` | No status update |
| Payments | `failed` | Payment fails |
| Payments | `cancelled` | Payment fails |
| Payments | `resubmission_required` | No status update |
| Refunds | `created` | No status update |
| Refunds | `failed` | Refund fails |
| Refunds | `paid` | Refund succeeds |
| Refunds | `refund_settled` | No status update |
| Refunds | `funds_returned` | No status update |
| Mandates | `created` | No status update |
| Mandates | `customer_approval_granted` | No status update |
| Mandates | `customer_approval_skipped` | No status update |
| Mandates | `active` | Mandate becomes active |
| Mandates | `cancelled` | Mandate is revoked |
| Mandates | `failed` | Mandate is revoked |
| Mandates | `transferred` | No status update |
| Mandates | `expired` | Mandate is revoked |
| Mandates | `submitted` | No status update |
| Mandates | `resubmission_requested` | No status update |
| Mandates | `reinstated` | Mandate becomes active |
| Mandates | `replaced` | No status update |
| Mandates | `consumed` | Mandate is revoked |
| Mandates | `blocked` | No status update |

The wire values use `snake_case` in [`PaymentsAction`, `RefundsAction`, and `MandatesAction`](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/gocardless/transformers.rs#L839-L905). Their effects come from [`get_webhook_event_type()`](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/gocardless.rs#L790-L849).

### Source reference

The connector implementation is [`gocardless.rs`](https://github.com/juspay/hyperswitch/blob/a17a23c4c4c907d2314043a32a9f505f7f2bd4f9/crates/hyperswitch_connectors/src/connectors/gocardless.rs).
