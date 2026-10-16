---
description: >-
  Mifinity on Hyperswitch: a Mifinity wallet payment connector. Declared as a
  payout processor, with no payout flow implemented.
---

# Mifinity

Mifinity is not a payout connector. Hyperswitch declares it as one, but no payout flow is implemented, so a Mifinity payout cannot be executed, and the control center does not offer it in the payout processor list. Mifinity does work as a payment connector for Mifinity wallet payments, which the rest of this page describes.

### Authentication

Mifinity uses `HeaderKey` authentication; the key is sent as the `key` header on every request ([`get_auth_header`](https://github.com/juspay/hyperswitch/blob/04ac0042fc99a2d305540a7c7ed9167279ce7052/crates/hyperswitch_connectors/src/connectors/mifinity.rs#L133-L145)).

| Credential | Description |
| --- | --- |
| **key** | Your Mifinity API key. Required. |
| **Merchant Brand ID** | Connector metadata `brand_id`. Required on the payments form ([`[mifinity]`](https://github.com/juspay/hyperswitch/blob/04ac0042fc99a2d305540a7c7ed9167279ce7052/crates/connector_configs/toml/sandbox.toml#L3155-L3170)). |
| **Destination Account Number** | Connector metadata `destination_account_number`. Required on the payments form; the payout form asks for the same value as **Source Account Number** ([`[mifinity_payout]`](https://github.com/juspay/hyperswitch/blob/04ac0042fc99a2d305540a7c7ed9167279ce7052/crates/connector_configs/toml/sandbox.toml#L9678-L9690)). |

### Supported Payout Methods

| Method | Rails / Networks | Notes |
| --- | --- | --- |
| Mifinity wallet | Mifinity network | Declared only, not implemented: no payout flow exists. |
| SEPA bank transfer | SEPA | Declared only, not implemented: no payout flow exists. |

### Payout Flows

| Flow | Description |
| --- | --- |
| All payout flows | Not implemented. The connector has no payout code and falls under the blanket default, which builds no request ([blanket payout default](https://github.com/juspay/hyperswitch/blob/04ac0042fc99a2d305540a7c7ed9167279ce7052/crates/hyperswitch_connectors/src/default_implementations.rs#L5182-L5186), [Mifinity in that list](https://github.com/juspay/hyperswitch/blob/04ac0042fc99a2d305540a7c7ed9167279ce7052/crates/hyperswitch_connectors/src/default_implementations.rs#L5265)); the Unified Connector Service answers every payout flow with a not-implemented error ([stub declaration](https://github.com/juspay/hyperswitch-prism/blob/3a5ce8960f59009151a05f47f0e5ce1e88852294/crates/integrations/connector-integration/src/connectors/mifinity.rs#L42-L46)). |

### Payments

Mifinity accepts one payment method, the `mifinity` wallet, with automatic capture only; mandates and refunds are not supported ([declaration](https://github.com/juspay/hyperswitch/blob/04ac0042fc99a2d305540a7c7ed9167279ce7052/crates/hyperswitch_connectors/src/connectors/mifinity.rs#L527-L549), [`pm_filters.mifinity`](https://github.com/juspay/hyperswitch/blob/04ac0042fc99a2d305540a7c7ed9167279ce7052/config/development.toml#L990-L991)).

Authorize posts the payment to Mifinity's `init-iframe` endpoint ([`get_url`](https://github.com/juspay/hyperswitch/blob/04ac0042fc99a2d305540a7c7ed9167279ce7052/crates/hyperswitch_connectors/src/connectors/mifinity.rs#L246-L256)). Mifinity returns a trace id and an initialization token; Hyperswitch stores the trace id as the connector transaction id and returns the payment as `requires_customer_action` with a Mifinity redirect form carrying the token, so the customer completes the payment in Mifinity's hosted wallet flow ([authorize response](https://github.com/juspay/hyperswitch/blob/04ac0042fc99a2d305540a7c7ed9167279ce7052/crates/hyperswitch_connectors/src/connectors/mifinity/transformers.rs#L265-L300), [`RedirectForm::Mifinity`](https://github.com/juspay/hyperswitch/blob/04ac0042fc99a2d305540a7c7ed9167279ce7052/crates/hyperswitch_domain_models/src/router_response_types.rs#L451-L454)).

Payment sync reads Mifinity's payment-status endpoint, keyed on your merchant id and the payment id ([`PSync` URL](https://github.com/juspay/hyperswitch/blob/04ac0042fc99a2d305540a7c7ed9167279ce7052/crates/hyperswitch_connectors/src/connectors/mifinity.rs#L348-L358)). Mifinity's `SUCCESSFUL` maps to charged, `PENDING` to pending, `NOT_COMPLETED` to requires customer action, and `FAILED` to failed ([`MifinityPaymentStatus`](https://github.com/juspay/hyperswitch/blob/04ac0042fc99a2d305540a7c7ed9167279ce7052/crates/hyperswitch_connectors/src/connectors/mifinity/transformers.rs#L335-L346), [status mapping](https://github.com/juspay/hyperswitch/blob/04ac0042fc99a2d305540a7c7ed9167279ce7052/crates/hyperswitch_connectors/src/connectors/mifinity/transformers.rs#L423-L430)).

Capture, void, refund and refund sync are not implemented ([`Capture`](https://github.com/juspay/hyperswitch/blob/04ac0042fc99a2d305540a7c7ed9167279ce7052/crates/hyperswitch_connectors/src/connectors/mifinity.rs#L403-L479), [`Void`](https://github.com/juspay/hyperswitch/blob/04ac0042fc99a2d305540a7c7ed9167279ce7052/crates/hyperswitch_connectors/src/connectors/mifinity.rs#L481-L495), [`RSync`](https://github.com/juspay/hyperswitch/blob/04ac0042fc99a2d305540a7c7ed9167279ce7052/crates/hyperswitch_connectors/src/connectors/mifinity.rs#L497-L523)).

### Webhooks

Mifinity webhooks are not supported. The webhook handler returns `WebhooksNotImplemented` for every method ([`IncomingWebhook for Mifinity`](https://github.com/juspay/hyperswitch/blob/04ac0042fc99a2d305540a7c7ed9167279ce7052/crates/hyperswitch_connectors/src/connectors/mifinity.rs#L500-L523)), so a configured Mifinity callback has no effect. Use payment sync for status.

### Common Failure Modes

**Payout created against Mifinity**
The payout is accepted by the API but cannot be executed: no request reaches Mifinity. Use another payout connector for Mifinity recipients.

**Manual capture requested**
Only automatic capture is declared; manual capture is filtered out for this connector.

**Payment left in `requires_customer_action`**
The customer has not completed the hosted Mifinity flow. Sync the payment; `NOT_COMPLETED` keeps it in that state, `SUCCESSFUL` moves it to charged.

---

### Activating Mifinity via Hyperswitch

#### Prerequisites

1. Create or sign in to your [Mifinity account](https://mifinity.com/) and obtain your API key, Merchant Brand ID and Destination Account Number.
2. A registered Hyperswitch account, accessible from the [Hyperswitch control center](https://app.hyperswitch.io/).

Mifinity appears in the control center's payment processor list only; it is not in the payout processor list, so there is no dashboard form for a Mifinity payout account. Configure it as a payment processor for wallet payments.

[Steps to activate a connector on the Hyperswitch control center](../../activate-connector-on-hyperswitch/README.md)

---

Connector implementation: [`crates/hyperswitch_connectors/src/connectors/mifinity.rs`](https://github.com/juspay/hyperswitch/blob/04ac0042fc99a2d305540a7c7ed9167279ce7052/crates/hyperswitch_connectors/src/connectors/mifinity.rs) at Hyperswitch `04ac0042fc99a2d305540a7c7ed9167279ce7052`; Unified Connector Service payment flows at hyperswitch-prism `3a5ce8960f59009151a05f47f0e5ce1e88852294`.
