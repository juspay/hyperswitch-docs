---
description: Dwolla connector for payment gateway.
metaLinks:
  alternates:
    - dwolla.md
---

# Dwolla

Dwolla supports ACH direct debit in the sandbox, with refunds and automatic capture. Payment and refund webhook flows are declared.

To connect Dwolla to your Hyperswitch account, follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for what Dwolla supports.

### Status and capabilities

<!-- generated from GET /feature_matrix; host http://localhost:8080; hyperswitch 502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5; fetched 2026-09-22; matrix canonical-json-v1 sha256 873f2bbfe94dc9fd; 146 connectors.
     Do not edit by hand. Payment method rows regenerate from the connector's SupportedPaymentMethods declaration; countries and
     currencies come from pm_filters in config/development.toml. Webhook flows and capture methods print as declared; the
     declaration-gap check reconciles them in prose. Edit those sources instead. -->

**Integration status:** sandbox

**Category:** payment gateway

**Webhook flows:** payments, refunds

| Payment method | Type | Mandates | Refunds | Capture methods | Countries | Currencies |
|---|---|---|---|---|---|---|
| bank debit | ACH Direct Debit | not supported | supported | automatic, sequential automatic | USA | USD |


### Authentication

Supply Client ID and Client Secret. The dashboard labels come from the connector configuration; implementation details are defined in the connector source.

### Before you start

Dwolla is available in the control center connector list. Have the credentials shown in the Authentication section ready before configuring the connector.

### Webhooks

Dwolla webhook events are converted from the connector event type enum, including CustomerCreated, CustomerVerified, CustomerFundingSourceAdded, CustomerFundingSourceRemoved, CustomerFundingSourceUnverified, CustomerFundingSourceVerified, CustomerMicrodepositsAdded, CustomerMicrodepositsFailed, CustomerMicrodepositsCompleted, CustomerMicrodepositsMaxAttempts, CustomerTransferCreated, CustomerBankTransferCreationFailed, CustomerBankTransferCreated, CustomerBankTransferCompleted, CustomerBankTransferFailed, CustomerTransferCompleted, CustomerTransferFailed, TransferCreated, TransferPending, TransferCompleted, and TransferFailed. Source verification uses HMAC-SHA256. See [`get_webhook_event_type()`](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/dwolla.rs#L947-L959) and the webhook verification implementation (https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/dwolla.rs#L900-L912).

### Source reference

Authentication and webhook behavior on this page is tied to Hyperswitch `502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5`. See [Dwolla connector source](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/dwolla.rs) and [Dwolla transformers](https://github.com/juspay/hyperswitch/blob/502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5/crates/hyperswitch_connectors/src/connectors/transformers.rs).
