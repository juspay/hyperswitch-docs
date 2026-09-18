---
description: Accept card and wallet payments through BarclayCard SmartPay Fuse.
metaLinks:
  alternates:
    - barclaycard.md
---

# BarclayCard SmartPay Fuse

BarclayCard SmartPay Fuse accepts card payments alongside Apple Pay and Google Pay. Cards support refunds, optional 3DS, and automatic, manual, or sequential automatic capture. Mandates are not supported on any route, so this connector cannot store a payment method for later reuse.

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch 9e5dd70d1cb4011bbcca3114862406008a0b61f8; host http://localhost:8080; fetched 2026-09-17; matrix canonical-json-v1 sha256 25db1ecc45c5b9c7; 140 connectors.
     Do not edit by hand. Payment method rows regenerate from the
     connector's SupportedPaymentMethods declaration; countries and
     currencies come from pm_filters in config/development.toml.
     Webhook flows and capture methods print as declared; the
     declaration-gap check reconciles them in prose. Edit those
     sources instead. -->

**Integration status:** sandbox

**Category:** bank acquirer

**Webhook flows:** None declared in code

| Payment method | Type | Mandates | Refunds | Capture methods | 3DS | Card networks | Countries | Currencies |
|---|---|---|---|---|---|---|---|---|
| card | Credit Card | not supported | supported | automatic, manual, sequential automatic | supported, optional | American Express, Cartes Bancaires, Diners Club, Discover, Interac, JCB, Maestro, Mastercard, UnionPay, Visa | - | EUR, GBP, PLN, SEK, USD |
| card | Debit Card | not supported | supported | automatic, manual, sequential automatic | supported, optional | American Express, Cartes Bancaires, Diners Club, Discover, Interac, JCB, Maestro, Mastercard, UnionPay, Visa | - | EUR, GBP, PLN, SEK, USD |
| wallet | Apple Pay | not supported | supported | automatic, manual, sequential automatic | not applicable | - | - | 22 |
| wallet | Google Pay | not supported | supported | automatic, manual, sequential automatic | not applicable | - | - | 23 |

BarclayCard SmartPay Fuse is a UCS-only connector. While the Unified Connector Service is enabled, Hyperswitch routes every BarclayCard payment through it, and the UCS kill switch never diverts this connector to a direct path the way it can for others. If UCS is switched off or its client is unavailable, the router falls back to the direct implementation instead. Treat that fallback with care: the direct path behind a UCS-only connector has never carried production traffic. See the `ucs_only_connectors` list in [`config/deployments/production.toml`](https://github.com/juspay/hyperswitch/blob/9e5dd70d1cb4011bbcca3114862406008a0b61f8/config/deployments/production.toml#L1064), [`determine_connector_integration_type()`](https://github.com/juspay/hyperswitch/blob/9e5dd70d1cb4011bbcca3114862406008a0b61f8/crates/router/src/core/unified_connector_service.rs#L883-L913), the disabled-UCS arm in [`should_call_unified_connector_service()`](https://github.com/juspay/hyperswitch/blob/9e5dd70d1cb4011bbcca3114862406008a0b61f8/crates/router/src/core/unified_connector_service.rs#L971-L987), and [`is_kill_switch_applicable()`](https://github.com/juspay/hyperswitch/blob/9e5dd70d1cb4011bbcca3114862406008a0b61f8/crates/router/src/core/unified_connector_service.rs#L1130-L1152).

### Authentication

Supply **Key**, **Merchant ID**, and **Shared Secret**, the labels shown in the Hyperswitch control center. You do not need to build the request signature yourself; Hyperswitch signs every request for you.

Behind the scenes, Hyperswitch Base64-decodes the Shared Secret and uses it as an HMAC-SHA256 key over the `host`, `date`, request-target, and Merchant ID lines. The result goes out Base64-encoded in a `Signature` header that carries your Key as `keyid`, and the Merchant ID travels separately in `v-c-merchant-id`. Payment requests are POSTs: they also sign a SHA-256 digest of the body and send it in a `Digest` header. The sync flows are GETs, which have no body, so they carry neither. See [`BarclaycardAuthType::try_from()`](https://github.com/juspay/hyperswitch/blob/9e5dd70d1cb4011bbcca3114862406008a0b61f8/crates/hyperswitch_connectors/src/connectors/barclaycard/transformers.rs#L51-L75), [`generate_signature()`](https://github.com/juspay/hyperswitch/blob/9e5dd70d1cb4011bbcca3114862406008a0b61f8/crates/hyperswitch_connectors/src/connectors/barclaycard.rs#L92-L132), and [`build_headers()`](https://github.com/juspay/hyperswitch/blob/9e5dd70d1cb4011bbcca3114862406008a0b61f8/crates/hyperswitch_connectors/src/connectors/barclaycard.rs#L159-L215).

### Before you start

1. Register for BarclayCard SmartPay Fuse and obtain your **Key**, **Merchant ID**, and **Shared Secret**.
2. Sign in to the [Hyperswitch control center](https://app.hyperswitch.io/).
3. Enter **Key**, **Merchant ID**, and **Shared Secret** during connector activation.
4. Enable only the card and wallet methods available on your connector account.
5. Make sure your payment requests carry an email address and a full billing address. BarclayCard needs a first name, last name, address line 1, city, state, postal code and country on every card and wallet payment, and Hyperswitch rejects the request before sending it if any of them is missing.
6. To accept Apple Pay, work through [Apple Pay setup](../../wallets/apple-pay/README.md) first. Activation then asks for the merchant certificate and merchant private key, **both Base64-encoded**, plus the Apple merchant identifier, display name, domain (`web` or `ios`), domain name, merchant business country, and where payments are processed (`Connector` or `Hyperswitch`). All of them are required.
7. To accept Google Pay, work through [Google Pay setup](../../wallets/google-pay/README.md) first. Google Pay asks for more than the other wallets, and all seven fields are required: merchant name, merchant ID, merchant key, public key, private key, recipient ID, and allowed authentication methods (`PAN_ONLY`, `CRYPTOGRAM_3DS`).

The billing requirement comes from [`build_bill_to()`](https://github.com/juspay/hyperswitch/blob/9e5dd70d1cb4011bbcca3114862406008a0b61f8/crates/hyperswitch_connectors/src/connectors/barclaycard/transformers.rs#L284-L310), and the wallet field labels from the [connector wallet configuration](https://github.com/juspay/hyperswitch/blob/9e5dd70d1cb4011bbcca3114862406008a0b61f8/crates/connector_configs/toml/production.toml#L1336-L1456).

To connect BarclayCard SmartPay Fuse to your Hyperswitch account, follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for connector-specific behavior.

### Webhooks

BarclayCard SmartPay Fuse webhooks are not supported. Use payment sync and refund sync for status updates. [`get_webhook_object_reference_id()`](https://github.com/juspay/hyperswitch/blob/9e5dd70d1cb4011bbcca3114862406008a0b61f8/crates/hyperswitch_connectors/src/connectors/barclaycard.rs#L1520-L1525), [`get_webhook_event_type()`](https://github.com/juspay/hyperswitch/blob/9e5dd70d1cb4011bbcca3114862406008a0b61f8/crates/hyperswitch_connectors/src/connectors/barclaycard.rs#L1527-L1533), and [`get_webhook_resource_object()`](https://github.com/juspay/hyperswitch/blob/9e5dd70d1cb4011bbcca3114862406008a0b61f8/crates/hyperswitch_connectors/src/connectors/barclaycard.rs#L1535-L1541) each return `WebhooksNotImplemented`.

### Source reference

Authentication and webhook behavior on this page is tied to Hyperswitch `9e5dd70d1cb4011bbcca3114862406008a0b61f8`. See [BarclayCard connector source](https://github.com/juspay/hyperswitch/blob/9e5dd70d1cb4011bbcca3114862406008a0b61f8/crates/hyperswitch_connectors/src/connectors/barclaycard.rs) and [BarclayCard transformers](https://github.com/juspay/hyperswitch/blob/9e5dd70d1cb4011bbcca3114862406008a0b61f8/crates/hyperswitch_connectors/src/connectors/barclaycard/transformers.rs).
