---
description: Accept card and wallet payments through Archipel.
---

# Archipel

Archipel brings card processing and Apple Pay into one payment gateway connection. Card transactions can use mandates, optional 3DS, refunds, and immediate or delayed capture. Apple Pay follows a narrower path without mandate support.

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch d8b6ebe773690aa37cf249b2992c2358dbd7f438; host http://localhost:8080; fetched 2026-09-15; matrix canonical-json-v1 sha256 571f94742339b80b; 139 connectors.
     Do not edit by hand. Payment method rows regenerate from the
     connector's SupportedPaymentMethods declaration; countries and
     currencies come from pm_filters in config/development.toml.
     Webhook flows and capture methods are reconciled against
     implemented flows. Edit those sources instead. -->

**Integration status:** live

**Category:** payment gateway

**Webhook flows:** None declared in code

| Payment method | Type | Mandates | Refunds | Capture methods | 3DS | Card networks | Countries | Currencies |
|---|---|---|---|---|---|---|---|---|
| card | Credit Card | supported | supported | automatic, manual, sequential automatic | supported, optional | American Express, Cartes Bancaires, Diners Club, Discover, Mastercard, Visa | - | - |
| card | Debit Card | supported | supported | automatic, manual, sequential automatic | supported, optional | American Express, Cartes Bancaires, Diners Club, Discover, Mastercard, Visa | - | - |
| wallet | Apple Pay | not supported | supported | automatic, manual, sequential automatic | not applicable | - | - | - |

### Authentication

Supply a **CA Certificate PEM** in the connector API Key field. Hyperswitch maps that field to `ca_certificate` and attaches the PEM certificate to connector requests instead of sending an authorization header. The connector also reads **Tenant ID** and **Platform URL** metadata. See [`ArchipelAuthType::try_from()`](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/archipel/transformers.rs#L69-L82), [`ArchipelConfigData`](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/archipel/transformers.rs#L85-L99), [`get_auth_header()`](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/archipel.rs#L123-L128), and the certificate attachment in [`build_request()`](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/archipel.rs#L249-L263).

### Before you start

1. Sign in to the [Hyperswitch control center](https://app.hyperswitch.io/).
2. Have the **CA Certificate PEM**, **Tenant ID**, and **Platform URL** ready.
3. If the activation flow produces or requests connector metadata, provide the Tenant ID and Platform URL there.
4. If payment methods are offered during activation, select only those enabled for your connector account.

To connect Archipel to your Hyperswitch account, follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for what Archipel supports.

### Webhooks

Handled event wire values: **0**. Webhooks are not currently supported, so status updates rely on syncing through the API. Object lookup, event classification, and resource parsing each return `WebhooksNotImplemented`; see [`IncomingWebhook for Archipel`](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/archipel.rs#L1028-L1052).

### Source reference

Authentication and webhook behavior on this page is tied to Hyperswitch `d8b6ebe773690aa37cf249b2992c2358dbd7f438`. See [Archipel connector source](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/archipel.rs) and [Archipel transformers](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/archipel/transformers.rs).
