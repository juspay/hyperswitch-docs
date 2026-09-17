---
description: Accept cryptocurrency payments through Bitpay.
---

# Bitpay

Bitpay provides a cryptocurrency checkout route with automatic capture. Payment webhooks can move an invoice through processing, success, or failure outcomes. Review the refund caveat below before enabling this connector.

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch 9e5dd70d1cb4011bbcca3114862406008a0b61f8; host http://localhost:8080; fetched 2026-09-17; matrix canonical-json-v1 sha256 25db1ecc45c5b9c7; 140 connectors.
     Do not edit by hand. Payment method rows regenerate from the
     connector's SupportedPaymentMethods declaration; countries and
     currencies come from pm_filters in config/development.toml.
     Webhook flows and capture methods print as declared; the
     declaration-gap check reconciles them in prose. Edit those
     sources instead. -->

**Integration status:** sandbox

**Category:** alternative payment method

**Webhook flows:** payments

| Payment method | Type | Mandates | Refunds | Capture methods | Countries | Currencies |
|---|---|---|---|---|---|---|
| crypto | Crypto | not supported | supported | automatic | 30 | 8 |

The feature matrix declares refunds, but the refund execute request returns `NotImplemented`. Do not rely on refunds until [the declaration gap is resolved](https://github.com/juspay/hyperswitch/issues/14296).

### Authentication

Supply **API Key**, the label shown in the Hyperswitch control center. The current [`build_headers()`](https://github.com/juspay/hyperswitch/blob/9e5dd70d1cb4011bbcca3114862406008a0b61f8/crates/hyperswitch_connectors/src/connectors/bitpay.rs#L83-L107) override sends content type and `X-Accept-Version: 2.0.0`; it does not call [`get_auth_header()`](https://github.com/juspay/hyperswitch/blob/9e5dd70d1cb4011bbcca3114862406008a0b61f8/crates/hyperswitch_connectors/src/connectors/bitpay.rs#L126-L137), so the API Key is not added to connector requests. [`BitpayAuthType::try_from()`](https://github.com/juspay/hyperswitch/blob/9e5dd70d1cb4011bbcca3114862406008a0b61f8/crates/hyperswitch_connectors/src/connectors/bitpay/transformers.rs#L67-L80) maps the dashboard field.

### Before you start

1. Sign in to the [Hyperswitch control center](https://app.hyperswitch.io/).
2. Enter **API Key** during connector activation.
3. Leave **Source verification key** blank. Bitpay uses the default no-op verification algorithm, so this field does not add signature verification.

To connect Bitpay to your Hyperswitch account, follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for Bitpay-specific behavior.

### Webhooks

Bitpay does not verify callback signatures. The default [`get_webhook_source_verification_algorithm()`](https://github.com/juspay/hyperswitch/blob/9e5dd70d1cb4011bbcca3114862406008a0b61f8/crates/hyperswitch_interfaces/src/webhooks.rs#L194-L200) selects `NoAlgorithm`, whose [`verify_signature()`](https://github.com/juspay/hyperswitch/blob/9e5dd70d1cb4011bbcca3114862406008a0b61f8/crates/common_utils/src/crypto.rs#L177-L185) always returns true.

The connector handles 8 event wire values.

| Wire value | Effect |
|---|---|
| `invoice_paidInFull` | Payment is processing |
| `invoice_confirmed` | Payment succeeds |
| `invoice_completed` | Payment succeeds |
| `invoice_expired` | No payment update is applied |
| `invoice_failedToConfirm` | No payment update is applied |
| `invoice_declined` | Payment fails |
| `invoice_refundComplete` | No payment update is applied |
| `invoice_manuallyNotified` | No payment update is applied |

Any other event value uses the unknown fallback and applies no payment update. The 8 wire values and fallback come from [`WebhookEventType`](https://github.com/juspay/hyperswitch/blob/9e5dd70d1cb4011bbcca3114862406008a0b61f8/crates/hyperswitch_connectors/src/connectors/bitpay/transformers.rs#L306-L325); their effects come from [`get_webhook_event_type()`](https://github.com/juspay/hyperswitch/blob/9e5dd70d1cb4011bbcca3114862406008a0b61f8/crates/hyperswitch_connectors/src/connectors/bitpay.rs#L399-L420).

### Source reference

Authentication and webhook behavior on this page follows [Bitpay connector source](https://github.com/juspay/hyperswitch/blob/9e5dd70d1cb4011bbcca3114862406008a0b61f8/crates/hyperswitch_connectors/src/connectors/bitpay.rs) and [Bitpay transformers](https://github.com/juspay/hyperswitch/blob/9e5dd70d1cb4011bbcca3114862406008a0b61f8/crates/hyperswitch_connectors/src/connectors/bitpay/transformers.rs).
