---
description: Accept card and wallet payments through Archipel.
metaLinks:
  alternates:
    - archipel.md
---

# Archipel

Accept cards and Apple Pay through Archipel. Card transactions can use mandates, optional 3DS, refunds, and immediate or delayed capture. Apple Pay supports refunds and the same capture methods, but not mandates.

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch 184ffd4c015fd3fea2f3868549f1a86ffa5f40da; host http://localhost:8080; fetched 2026-09-16; matrix canonical-json-v1 sha256 02ce435bc7059143; 140 connectors.
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

Supply a **CA Certificate PEM** in the connector API Key field. Hyperswitch maps that field to `ca_certificate` and attaches the PEM certificate to connector requests instead of sending an authorization header. See [`ArchipelAuthType::try_from()`](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/archipel/transformers.rs#L69-L82), [`get_auth_header()`](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/archipel.rs#L123-L128), and the certificate attachment in [`build_request()`](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/archipel.rs#L249-L263).

The connector also requires two metadata fields. Requests fail with an invalid connector configuration error if either is missing. See [`ArchipelConfigData`](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/archipel/transformers.rs#L85-L99).

| Field | Metadata key | Format |
|---|---|---|
| **Tenant ID** | `tenant_id` | Your Archipel tenant ID |
| **Platform Endpoint Prefix** | `platform_url` | Host and port only, for example `192.0.0.1:8080`. Do not include `https://` or a path |

Hyperswitch builds the request URL as `https://<Platform Endpoint Prefix>/ArchiPEL/Transaction/v1`, so a value that already includes `https://` produces an invalid URL. See [`build_env_specific_endpoint()`](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/archipel.rs#L85-L93) and the [production base URL](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/config/deployments/production.toml#L44).

### Before you start

1. Sign in to the [Hyperswitch control center](https://app.hyperswitch.io/).
2. Have the **CA Certificate PEM**, **Tenant ID**, and **Platform Endpoint Prefix** ready.
3. To accept Apple Pay, set up Apple Pay with [Hyperswitch decryption](../../wallets/apple-pay/in-app-and-web-transactions-processed-using-hyperswitch-decryption.md) first. Archipel accepts only Apple Pay tokens that Hyperswitch has decrypted, and the connector requires these Apple Pay fields: merchant certificate, merchant private key, Apple merchant identifier, display name, domain (`web` or `ios`), domain name, merchant business country, and payment processing location (`Hyperswitch`). See the [Apple Pay token handling](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/archipel/transformers.rs#L254-L275) and the [connector metadata fields](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/connector_configs/toml/production.toml#L6243-L6305).

To connect Archipel to your Hyperswitch account, follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for what Archipel supports.

### Webhooks

Archipel webhooks are not supported. Use payment sync for payment status updates. The connector's webhook handlers all return `WebhooksNotImplemented`; see [`IncomingWebhook for Archipel`](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/archipel.rs#L1028-L1052).

### Source reference

Authentication, setup, and webhook behavior on this page is tied to Hyperswitch `d8b6ebe773690aa37cf249b2992c2358dbd7f438`. See [Archipel connector source](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/archipel.rs) and [Archipel transformers](https://github.com/juspay/hyperswitch/blob/d8b6ebe773690aa37cf249b2992c2358dbd7f438/crates/hyperswitch_connectors/src/connectors/archipel/transformers.rs).
