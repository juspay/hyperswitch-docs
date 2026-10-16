---
description: >-
  Mifinity as a payout processor on Hyperswitch: declared for wallet and SEPA
  payouts, with no payout flow implemented yet.
---

# Mifinity

Mifinity is declared as a Hyperswitch payout processor for Mifinity wallet payouts and SEPA bank transfers, and it is listed as both a payment and a payout processor in the control center. No payout flow is implemented, so a Mifinity payout cannot be executed today. This page records what is declared and what the code does, so you can plan against it.

{% hint style="warning" %}
**Mifinity payouts do not execute.** The declaration, dashboard form and required fields exist, but neither path that could carry a payout has an implementation: the in-process connector has no payout flow and builds no request ([blanket payout default](https://github.com/juspay/hyperswitch/blob/04ac0042fc99a2d305540a7c7ed9167279ce7052/crates/hyperswitch_connectors/src/default_implementations.rs#L5182-L5186), [Mifinity in that list](https://github.com/juspay/hyperswitch/blob/04ac0042fc99a2d305540a7c7ed9167279ce7052/crates/hyperswitch_connectors/src/default_implementations.rs#L5265), [default request builder returns none](https://github.com/juspay/hyperswitch/blob/04ac0042fc99a2d305540a7c7ed9167279ce7052/crates/hyperswitch_interfaces/src/api.rs#L242-L252)), and the Unified Connector Service answers every payout flow with a not-implemented error ([stub declaration](https://github.com/juspay/hyperswitch-prism/blob/3a5ce8960f59009151a05f47f0e5ce1e88852294/crates/integrations/connector-integration/src/connectors/mifinity.rs#L42-L46), [what it expands to](https://github.com/juspay/hyperswitch-prism/blob/3a5ce8960f59009151a05f47f0e5ce1e88852294/crates/integrations/connector-integration/src/connectors/macros.rs#L1570-L1600)). What Mifinity does run is wallet payments: authorize and payment sync ([`Authorize`](https://github.com/juspay/hyperswitch/blob/04ac0042fc99a2d305540a7c7ed9167279ce7052/crates/hyperswitch_connectors/src/connectors/mifinity.rs#L232-L328), [`PSync`](https://github.com/juspay/hyperswitch/blob/04ac0042fc99a2d305540a7c7ed9167279ce7052/crates/hyperswitch_connectors/src/connectors/mifinity.rs#L330-L401)); capture, void, refunds and webhooks are not implemented either ([`Capture`](https://github.com/juspay/hyperswitch/blob/04ac0042fc99a2d305540a7c7ed9167279ce7052/crates/hyperswitch_connectors/src/connectors/mifinity.rs#L403-L479), [`Void`](https://github.com/juspay/hyperswitch/blob/04ac0042fc99a2d305540a7c7ed9167279ce7052/crates/hyperswitch_connectors/src/connectors/mifinity.rs#L481-L495), [`IncomingWebhook`](https://github.com/juspay/hyperswitch/blob/04ac0042fc99a2d305540a7c7ed9167279ce7052/crates/hyperswitch_connectors/src/connectors/mifinity.rs#L500-L513)).
{% endhint %}

### What is declared

* Mifinity is a payout connector: `mifinity` is a variant of [`PayoutConnectors`](https://github.com/juspay/hyperswitch/blob/04ac0042fc99a2d305540a7c7ed9167279ce7052/crates/api_models/src/enums.rs#L46-L71), and it is marked as supporting instant payouts for wallet and bank payout types ([`supports_instant_payout`](https://github.com/juspay/hyperswitch/blob/04ac0042fc99a2d305540a7c7ed9167279ce7052/crates/common_enums/src/connector_enums.rs#L235-L253)).
* Two payout methods are declared: the Mifinity wallet, identified by the recipient's email address or Mifinity account number in `payout_method_data.wallet.mifinity.destination_account` ([`Mifinity`](https://github.com/juspay/hyperswitch/blob/04ac0042fc99a2d305540a7c7ed9167279ce7052/crates/api_models/src/payouts.rs#L686-L691), [required field](https://github.com/juspay/hyperswitch/blob/04ac0042fc99a2d305540a7c7ed9167279ce7052/crates/router/src/configs/defaults/payout_required_fields.rs#L379-L389)), and SEPA bank transfer with `payout_method_type: sepa` ([SEPA connector list](https://github.com/juspay/hyperswitch/blob/04ac0042fc99a2d305540a7c7ed9167279ce7052/crates/router/src/configs/defaults/payout_required_fields.rs#L66-L72)).
* The service-side credential shape accepts the API key with optional `brand_id` and `destination_account_number` metadata ([`MifinityMetadata`](https://github.com/juspay/hyperswitch/blob/04ac0042fc99a2d305540a7c7ed9167279ce7052/crates/router/src/core/unified_connector_service/connector_config.rs#L2121-L2138)).

### Authentication

The payout connector form asks for the **key**, a `HeaderKey` credential, and a required **Source Account Number** stored as the `destination_account_number` metadata ([`[mifinity_payout]`](https://github.com/juspay/hyperswitch/blob/04ac0042fc99a2d305540a7c7ed9167279ce7052/crates/connector_configs/toml/sandbox.toml#L9678-L9690)). The payments form for the same connector additionally requires a **Merchant Brand ID** ([`[mifinity]`](https://github.com/juspay/hyperswitch/blob/04ac0042fc99a2d305540a7c7ed9167279ce7052/crates/connector_configs/toml/sandbox.toml#L3155-L3170)). Hyperswitch rejects any auth type other than `HeaderKey` for Mifinity.

### Activating Mifinity Payouts via Hyperswitch

Mifinity appears in the control center as a payout processor, so the form can be filled in, but a payout created against it fails as described above. Until a payout flow lands, use another payout connector for Mifinity recipients.

[Steps to activate a connector on the Hyperswitch control center](../../activate-connector-on-hyperswitch/README.md)

---

Connector implementation: payment connector at [`crates/hyperswitch_connectors/src/connectors/mifinity.rs`](https://github.com/juspay/hyperswitch/blob/04ac0042fc99a2d305540a7c7ed9167279ce7052/crates/hyperswitch_connectors/src/connectors/mifinity.rs); Unified Connector Service implementation at [hyperswitch-prism `mifinity.rs`](https://github.com/juspay/hyperswitch-prism/blob/3a5ce8960f59009151a05f47f0e5ce1e88852294/crates/integrations/connector-integration/src/connectors/mifinity.rs) (payment flows only: [prerequisites](https://github.com/juspay/hyperswitch-prism/blob/3a5ce8960f59009151a05f47f0e5ce1e88852294/crates/integrations/connector-integration/src/connectors/mifinity.rs#L82-L127)). Hyperswitch `04ac0042fc99a2d305540a7c7ed9167279ce7052`, hyperswitch-prism `3a5ce8960f59009151a05f47f0e5ce1e88852294`.
