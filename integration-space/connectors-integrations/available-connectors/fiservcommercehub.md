---
description: Configure Fiserv Commerce Hub card payments with Hyperswitch.
metaLinks:
  alternates:
    - fiservcommercehub.md
---

# Fiserv Commerce Hub

Fiserv Commerce Hub processes credit and debit card payments through Hyperswitch. Both routes support mandates, refunds, and manual capture alongside automatic capture. Cardholders can complete payments with or without 3DS across the declared card networks.

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

**Webhook flows:** None declared in code

| Payment method | Type | Mandates | Refunds | Capture methods | 3DS | Card networks | Countries | Currencies |
|---|---|---|---|---|---|---|---|---|
| card | Credit Card | supported | supported | automatic, manual | supported, optional | American Express, Cartes Bancaires, Diners Club, Discover, Interac, JCB, Maestro, Mastercard, UnionPay, Visa | - | - |
| card | Debit Card | supported | supported | automatic, manual | supported, optional | American Express, Cartes Bancaires, Diners Club, Discover, Interac, JCB, Maestro, Mastercard, UnionPay, Visa | - | - |

Fiserv Commerce Hub runs through the Unified Connector Service.

The table matches what is implemented: authorize, capture, void, payment sync, refund, refund sync, mandate setup and repeat payments are all implemented ([flow status](https://github.com/juspay/hyperswitch-prism/blob/882997b7447232b53a28d09676ff9f8d2797c3b0/crates/integrations/connector-integration/src/connectors/fiservcommercehub.rs#L948-L970)).

3DS is supported in the sense that Fiserv Commerce Hub accepts the result of a 3DS authentication performed elsewhere: it forwards the `ds_trans_id` and `cavv` from the payment's authentication data ([`build_additional_data_3ds`](https://github.com/juspay/hyperswitch-prism/blob/882997b7447232b53a28d09676ff9f8d2797c3b0/crates/integrations/connector-integration/src/connectors/fiservcommercehub/transformers.rs#L962-L982)). It does not run the challenge itself and never returns a redirect.

Mandate setup is a zero-amount tokenization. A setup request with an amount above zero is rejected as not supported ([`SetupMandate`](https://github.com/juspay/hyperswitch-prism/blob/882997b7447232b53a28d09676ff9f8d2797c3b0/crates/integrations/connector-integration/src/connectors/fiservcommercehub/transformers.rs#L2451-L2460)); charge the card through a normal payment instead, and use the stored token for repeat payments.

### Authentication

Provide the **API Key**, **Merchant ID**, **API Secret**, and **Terminal ID** shown in the connector form. The labels and accepted multi-auth fields are defined by the [`fiservcommercehub.connector_auth.MultiAuthKey` configuration](https://github.com/juspay/hyperswitch/blob/d03f8547d6367fab56690e4f5043590be4935dcd/crates/connector_configs/toml/sandbox.toml#L2716-L2720) and carried as [`FiservcommercehubAuthType`](https://github.com/juspay/hyperswitch-prism/blob/882997b7447232b53a28d09676ff9f8d2797c3b0/crates/integrations/connector-integration/src/connectors/fiservcommercehub/transformers.rs#L523-L528).

They are not used the same way. Every request is signed: the **API Key** is sent in the `Api-Key` header, and the `Authorization` header carries an HMAC-SHA256 signature keyed on the **API Secret** over the API key, a request id, a timestamp and the request body, with `Auth-Token-Type: HMAC` ([`build_hmac_headers`](https://github.com/juspay/hyperswitch-prism/blob/882997b7447232b53a28d09676ff9f8d2797c3b0/crates/integrations/connector-integration/src/connectors/fiservcommercehub/transformers.rs#L561-L608), [`generate_hmac_signature`](https://github.com/juspay/hyperswitch-prism/blob/882997b7447232b53a28d09676ff9f8d2797c3b0/crates/integrations/connector-integration/src/connectors/fiservcommercehub/transformers.rs#L531-L552)). The **Merchant ID** and **Terminal ID** are not authentication values; they travel in the request body ([merchant details](https://github.com/juspay/hyperswitch-prism/blob/882997b7447232b53a28d09676ff9f8d2797c3b0/crates/integrations/connector-integration/src/connectors/fiservcommercehub/transformers.rs#L619-L626)). A wrong API Key or API Secret fails the signature check; a wrong Merchant ID or Terminal ID fails the payment.

### Before you start

Request the API Key, Merchant ID, API Secret, and Terminal ID from [Fiserv](https://www.fiserv.com/en/who-we-serve/enterprise/contact-us.html?cid=%7Ccommerce-hub-for-platforms%7C). Once you have them, follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md) to connect Fiserv Commerce Hub to your account.

### Webhooks

Fiserv Commerce Hub webhooks are not supported; the incoming-webhook handler for this connector is empty ([`IncomingWebhook for Fiservcommercehub`](https://github.com/juspay/hyperswitch-prism/blob/882997b7447232b53a28d09676ff9f8d2797c3b0/crates/integrations/connector-integration/src/connectors/fiservcommercehub.rs#L556-L558)). Use Hyperswitch payment sync and refund sync to check status; both are implemented and run through the Unified Connector Service ([`PSync`](https://github.com/juspay/hyperswitch-prism/blob/882997b7447232b53a28d09676ff9f8d2797c3b0/crates/integrations/connector-integration/src/connectors/fiservcommercehub.rs#L691-L721), [`RSync`](https://github.com/juspay/hyperswitch-prism/blob/882997b7447232b53a28d09676ff9f8d2797c3b0/crates/integrations/connector-integration/src/connectors/fiservcommercehub.rs#L753-L786)) and [Connector Service routing](https://github.com/juspay/hyperswitch/blob/d03f8547d6367fab56690e4f5043590be4935dcd/config/development.toml#L1684).

### Source reference

The capability declaration and credential labels on this page are tied to Hyperswitch `d03f8547d6367fab56690e4f5043590be4935dcd`. Flow, authentication and webhook behavior is tied to the Unified Connector Service implementation at hyperswitch-prism `882997b7447232b53a28d09676ff9f8d2797c3b0`: see [Fiserv Commerce Hub service source](https://github.com/juspay/hyperswitch-prism/blob/882997b7447232b53a28d09676ff9f8d2797c3b0/crates/integrations/connector-integration/src/connectors/fiservcommercehub.rs) and [Fiserv Commerce Hub service transformers](https://github.com/juspay/hyperswitch-prism/blob/882997b7447232b53a28d09676ff9f8d2797c3b0/crates/integrations/connector-integration/src/connectors/fiservcommercehub/transformers.rs).
