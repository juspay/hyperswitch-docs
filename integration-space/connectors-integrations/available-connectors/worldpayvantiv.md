---
description: >-
  Accept card and wallet payments through Worldpay Vantiv using merchant-scoped XML credentials.
metaLinks:
  alternates:
    - worldpayvantiv.md
---

# Worldpay Vantiv

Worldpay Vantiv is implemented separately from the Worldpay connector and uses its own routes and configuration. It supports cards and selected wallets, with refunds and mandate reuse, and both immediate and delayed capture. Disputes are supported end-to-end: fetching, syncing, acceptance, and evidence submission, with file upload and retrieval.

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch 184ffd4c015fd3fea2f3868549f1a86ffa5f40da; host http://localhost:8080; fetched 2026-09-16; matrix canonical-json-v1 sha256 02ce435bc7059143; 140 connectors.
     Do not edit by hand. Payment method rows regenerate from the
     connector's SupportedPaymentMethods declaration; countries and
     currencies come from pm_filters in config/development.toml.
     Webhook flows and capture methods are reconciled against
     implemented flows. Edit those sources instead. -->

**Integration status:** sandbox

**Category:** payment gateway

**Webhook flows:** None declared in code

| Payment method | Type | Mandates | Refunds | Capture methods | 3DS | Card networks | Countries | Currencies |
|---|---|---|---|---|---|---|---|---|
| card | Credit Card | supported | supported | automatic, manual, sequential automatic | not supported | American Express, Diners Club, Discover, JCB, Mastercard, Visa | 133 | 147 |
| card | Debit Card | supported | supported | automatic, manual, sequential automatic | not supported | American Express, Diners Club, Discover, JCB, Mastercard, Visa | 133 | 147 |
| wallet | Apple Pay | supported | supported | automatic, manual, sequential automatic | not applicable | - | 133 | 147 |
| wallet | Google Pay | supported | supported | automatic, manual, sequential automatic | not applicable | - | 133 | 147 |

### Authentication

Worldpay Vantiv requires **Username**, **Password**, and **Merchant ID**. Its shared [`build_headers()`](https://github.com/juspay/hyperswitch/blob/e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0/crates/hyperswitch_connectors/src/connectors/worldpayvantiv.rs#L106-L121) override sends `Content-Type` only, so core payment and refund requests do not use the connector's Basic authorization helper. Instead, the XML request contains Username and Password in `authentication` and Merchant ID in the `merchantId` attribute; see [`CnpOnlineRequest and Authentication`](https://github.com/juspay/hyperswitch/blob/e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0/crates/hyperswitch_connectors/src/connectors/worldpayvantiv/transformers.rs#L140-L168) and [`TryFrom<&WorldpayvantivRouterData<&PaymentsAuthorizeRouterData>> for CnpOnlineRequest`](https://github.com/juspay/hyperswitch/blob/e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0/crates/hyperswitch_connectors/src/connectors/worldpayvantiv/transformers.rs#L779-L836).

Sync, dispute, and file paths use flow-specific headers. Those paths call [`get_auth_header()`](https://github.com/juspay/hyperswitch/blob/e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0/crates/hyperswitch_connectors/src/connectors/worldpayvantiv.rs#L141-L154), which constructs `<Username>:<Password>`, Base64-encodes it, and sends `Authorization: Basic <encoded value>`; see the [`payment-sync get_headers()`](https://github.com/juspay/hyperswitch/blob/e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0/crates/hyperswitch_connectors/src/connectors/worldpayvantiv.rs#L383-L391), [`refund-sync get_headers()`](https://github.com/juspay/hyperswitch/blob/e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0/crates/hyperswitch_connectors/src/connectors/worldpayvantiv.rs#L900-L910), [`dispute get_headers()`](https://github.com/juspay/hyperswitch/blob/e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0/crates/hyperswitch_connectors/src/connectors/worldpayvantiv.rs#L1067-L1090), and [`file-upload get_headers()`](https://github.com/juspay/hyperswitch/blob/e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0/crates/hyperswitch_connectors/src/connectors/worldpayvantiv.rs#L1354-L1367) overrides. [`WorldpayvantivAuthType::try_from()`](https://github.com/juspay/hyperswitch/blob/e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0/crates/hyperswitch_connectors/src/connectors/worldpayvantiv/transformers.rs#L83-L99) maps all three credentials. The connector remains independent from Worldpay through [`ConnectorCommon for Worldpayvantiv`](https://github.com/juspay/hyperswitch/blob/e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0/crates/hyperswitch_connectors/src/connectors/worldpayvantiv.rs#L124-L139).

### Before you start

1. Register with Worldpay Vantiv at [worldpay.com](https://www.worldpay.com/en).
2. Sign in to the [Hyperswitch control center](https://app.hyperswitch.io/).
3. Obtain **Username**, **Password**, and **Merchant ID** from the Worldpay Vantiv dashboard.
4. Set the **Report Group** and **Merchant Config Currency** metadata fields on the connector account. Authorization checks the configured currency, so it must be correct.
5. If the activation flow asks you to select payment methods, choose only the methods enabled in the connector dashboard.

Follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for Worldpay Vantiv-specific behavior.

### Webhooks

Handled event wire values: **0**. Webhooks are not currently supported, so status updates rely on syncing through the API. Sync requests go to a separate reporting endpoint, `{secondary_base_url}/reports/dtrPaymentStatus/{transaction_id}`, rather than the main transaction URL; see the [`payment-sync get_url()`](https://github.com/juspay/hyperswitch/blob/e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0/crates/hyperswitch_connectors/src/connectors/worldpayvantiv.rs#L398-L409) construction. [`get_webhook_object_reference_id()`](https://github.com/juspay/hyperswitch/blob/e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0/crates/hyperswitch_connectors/src/connectors/worldpayvantiv.rs#L1544-L1549), [`get_webhook_event_type()`](https://github.com/juspay/hyperswitch/blob/e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0/crates/hyperswitch_connectors/src/connectors/worldpayvantiv.rs#L1551-L1557), and [`get_webhook_resource_object()`](https://github.com/juspay/hyperswitch/blob/e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0/crates/hyperswitch_connectors/src/connectors/worldpayvantiv.rs#L1559-L1565) each return `WebhooksNotImplemented`.

### Source reference

Authentication and webhook behavior on this page is tied to Hyperswitch `e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0`. See [Worldpay Vantiv connector source](https://github.com/juspay/hyperswitch/blob/e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0/crates/hyperswitch_connectors/src/connectors/worldpayvantiv.rs) and [Worldpay Vantiv transformers](https://github.com/juspay/hyperswitch/blob/e8e30d1018b1ab5aecada04cf1b3ab63a39a68d0/crates/hyperswitch_connectors/src/connectors/worldpayvantiv/transformers.rs).
