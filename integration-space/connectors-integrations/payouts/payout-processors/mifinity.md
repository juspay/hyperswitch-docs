---
description: >-
  Mifinity on Hyperswitch: a wallet payment connector, not a payout connector.
---

# Mifinity

Mifinity is not a payout connector. It is declared as one in Hyperswitch and appears in the control center's payout processor list, but no payout flow is implemented, so a Mifinity payout cannot be executed.

Mifinity works as a payment connector for Mifinity wallet payments: authorize and payment sync are implemented ([`Authorize`](https://github.com/juspay/hyperswitch/blob/04ac0042fc99a2d305540a7c7ed9167279ce7052/crates/hyperswitch_connectors/src/connectors/mifinity.rs#L232-L328), [`PSync`](https://github.com/juspay/hyperswitch/blob/04ac0042fc99a2d305540a7c7ed9167279ce7052/crates/hyperswitch_connectors/src/connectors/mifinity.rs#L330-L401)). Capture, void, refunds and webhooks are not ([`Capture`](https://github.com/juspay/hyperswitch/blob/04ac0042fc99a2d305540a7c7ed9167279ce7052/crates/hyperswitch_connectors/src/connectors/mifinity.rs#L403-L479), [`IncomingWebhook`](https://github.com/juspay/hyperswitch/blob/04ac0042fc99a2d305540a7c7ed9167279ce7052/crates/hyperswitch_connectors/src/connectors/mifinity.rs#L500-L513)). Capture is automatic, and mandates are not supported ([declaration](https://github.com/juspay/hyperswitch/blob/04ac0042fc99a2d305540a7c7ed9167279ce7052/crates/hyperswitch_connectors/src/connectors/mifinity.rs#L527-L549)).

### Authentication

For wallet payments, the connector form asks for the **key** (`HeaderKey`), a **Merchant Brand ID** and a **Destination Account Number**, all required ([`[mifinity]`](https://github.com/juspay/hyperswitch/blob/04ac0042fc99a2d305540a7c7ed9167279ce7052/crates/connector_configs/toml/sandbox.toml#L3155-L3170)).

[Steps to activate a connector on the Hyperswitch control center](../../activate-connector-on-hyperswitch/README.md)

---

Connector implementation: [`crates/hyperswitch_connectors/src/connectors/mifinity.rs`](https://github.com/juspay/hyperswitch/blob/04ac0042fc99a2d305540a7c7ed9167279ce7052/crates/hyperswitch_connectors/src/connectors/mifinity.rs) at Hyperswitch `04ac0042fc99a2d305540a7c7ed9167279ce7052`.
