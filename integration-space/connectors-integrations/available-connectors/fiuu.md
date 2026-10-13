---
description: Configure Fiuu bank redirect, card, real-time payment, and wallet payments with Hyperswitch.
metaLinks:
  alternates:
    - fiuu.md
---

# Fiuu

Fiuu combines Malaysian bank redirects and DuitNow with card and wallet payments. Its card routes support mandates, while every declared payment route supports refunds and multiple capture modes. Apple Pay and Google Pay require additional wallet metadata before they can be used.

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch d03f8547d6367fab56690e4f5043590be4935dcd; host http://127.0.0.1:8080; fetched 2026-10-02; matrix canonical-json-v1 sha256 8b92b42f08eb323a31ea974c99ac67dc4972774ab49bda767a79da9d2992fd5b; 147 connectors.
     Do not edit by hand. Payment method rows regenerate from the
     connector's SupportedPaymentMethods declaration; countries and
     currencies come from pm_filters in config/development.toml.
     Webhook flows and capture methods print as declared; the
     declaration-gap check reconciles them in prose. Edit those
     sources instead. -->

**Integration status:** live

**Category:** payment gateway

**Webhook flows:** payments, refunds

| Payment method | Type | Mandates | Refunds | Capture methods | 3DS | Card networks | Countries | Currencies |
|---|---|---|---|---|---|---|---|---|
| bank redirect | Online Banking FPX | not supported | supported | automatic, manual, sequential automatic | not applicable | - | MYS | MYR |
| card | Credit Card | supported | supported | automatic, manual, sequential automatic | supported, optional | Diners Club, Discover, JCB, Mastercard, UnionPay, Visa | 9 | 9 |
| card | Debit Card | supported | supported | automatic, manual, sequential automatic | supported, optional | Diners Club, Discover, JCB, Mastercard, UnionPay, Visa | 9 | 9 |
| real time payment | DuitNow | not supported | supported | automatic, manual, sequential automatic | not applicable | - | MYS | MYR |
| wallet | Apple Pay | not supported | supported | automatic, manual, sequential automatic | not applicable | - | MYS | MYR |
| wallet | Google Pay | not supported | supported | automatic, manual, sequential automatic | not applicable | - | MYS | MYR |

### Authentication

Provide the **Verify Key**, **Merchant ID**, and **Secret Key** shown in the connector form. The labels and accepted signature-key fields are defined by the [`fiuu.connector_auth.SignatureKey` configuration](https://github.com/juspay/hyperswitch/blob/d03f8547d6367fab56690e4f5043590be4935dcd/crates/connector_configs/toml/sandbox.toml#L6581-L6584) and [`FiuuAuthType::try_from()`](https://github.com/juspay/hyperswitch/blob/d03f8547d6367fab56690e4f5043590be4935dcd/crates/hyperswitch_connectors/src/connectors/fiuu/transformers.rs#L73-L89).

Wallet setup requires these fields from the [`fiuu.metadata` configuration](https://github.com/juspay/hyperswitch/blob/d03f8547d6367fab56690e4f5043590be4935dcd/crates/connector_configs/toml/sandbox.toml#L6586-L6708):

| Wallet | Required fields |
|---|---|
| Google Pay | Google Pay Merchant Name, Google Pay Merchant Id, Google Pay Merchant Key, Allowed Auth Methods |
| Apple Pay | Merchant Certificate (Base64 Encoded), Merchant PrivateKey (Base64 Encoded), Apple Merchant Identifier, Display Name, Domain, Domain Name, Merchant Business Country, Payment Processing Details At |

For Google Pay, Allowed Auth Methods accepts `PAN_ONLY` and `CRYPTOGRAM_3DS`. For Apple Pay, Domain accepts `web` or `ios`, and Payment Processing Details At is set to `Hyperswitch`.

### Before you start

Have the Verify Key, Merchant ID, and Secret Key ready. Add the required wallet metadata when you enable Apple Pay or Google Pay. To connect Fiuu to your Hyperswitch account, follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for what Fiuu supports.

### Webhooks

Configure the **Source verification key** shown in the connector form. Fiuu verifies payment and refund callbacks with MD5, using a different ordered message for each payload type. See [`fiuu.connector_webhook_details`](https://github.com/juspay/hyperswitch/blob/d03f8547d6367fab56690e4f5043590be4935dcd/crates/connector_configs/toml/sandbox.toml#L6709-L6710), [`get_webhook_source_verification_algorithm()`](https://github.com/juspay/hyperswitch/blob/d03f8547d6367fab56690e4f5043590be4935dcd/crates/hyperswitch_connectors/src/connectors/fiuu.rs#L798-L803), and [`get_webhook_source_verification_message()`](https://github.com/juspay/hyperswitch/blob/d03f8547d6367fab56690e4f5043590be4935dcd/crates/hyperswitch_connectors/src/connectors/fiuu.rs#L834-L894).

The payment and refund status enums each define three named wire values and one fallback, for eight outcomes total:

| Payload | Wire value | Effect |
|---|---|---|
| Payment | `00` | Payment succeeds |
| Payment | `11` | Payment fails |
| Payment | `22` | Payment remains in processing |
| Payment | Any other value | Callback is acknowledged without a payment update |
| Refund | `00` | Refund succeeds |
| Refund | `11` | Refund fails |
| Refund | `22` | Callback is acknowledged without a refund update |
| Refund | Any other value | Callback is acknowledged without a refund update |

The wire values and fallbacks are defined by [`FiuuRefundsWebhookStatus`](https://github.com/juspay/hyperswitch/blob/d03f8547d6367fab56690e4f5043590be4935dcd/crates/hyperswitch_connectors/src/connectors/fiuu/transformers.rs#L2107-L2120) and [`FiuuPaymentWebhookStatus`](https://github.com/juspay/hyperswitch/blob/d03f8547d6367fab56690e4f5043590be4935dcd/crates/hyperswitch_connectors/src/connectors/fiuu/transformers.rs#L2142-L2155). Their merchant-facing effects come from the two [`IncomingWebhookEvent` mappings](https://github.com/juspay/hyperswitch/blob/d03f8547d6367fab56690e4f5043590be4935dcd/crates/hyperswitch_connectors/src/connectors/fiuu/transformers.rs#L2168-L2198).

### Source reference

Authentication and webhook behavior on this page is tied to Hyperswitch `d03f8547d6367fab56690e4f5043590be4935dcd`. See [Fiuu connector source](https://github.com/juspay/hyperswitch/blob/d03f8547d6367fab56690e4f5043590be4935dcd/crates/hyperswitch_connectors/src/connectors/fiuu.rs) and [Fiuu transformers](https://github.com/juspay/hyperswitch/blob/d03f8547d6367fab56690e4f5043590be4935dcd/crates/hyperswitch_connectors/src/connectors/fiuu/transformers.rs).
