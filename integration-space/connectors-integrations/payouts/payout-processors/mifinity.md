---
description: >-
  Configure Mifinity as a payout processor on Juspay Hyperswitch to distribute
  funds to Mifinity wallets and SEPA bank accounts.
---

# Mifinity

Mifinity connects to Hyperswitch as a `PayoutProcessor` for wallet payouts and SEPA bank transfers. Payout flows for Mifinity are served by the Hyperswitch unified connector service. Mifinity also works as a payment connector for wallet collections.

### Authentication

Mifinity uses `HeaderKey` authentication. Hyperswitch rejects any other auth type for Mifinity.

| Credential | Description |
| --- | --- |
| **API Key** | Mifinity API key, passed as the header key. Required. |
| **Brand ID** | Optional connector metadata (`brand_id`), passed when your Mifinity account uses it. |
| **Destination account number** | Optional connector metadata (`destination_account_number`). |

### Supported Payout Methods

| Method | Rails / Networks | Notes |
| --- | --- | --- |
| Mifinity wallet | Mifinity network | Payout to the recipient's Mifinity wallet identifier, an email address or Mifinity account number, sent as `payout_method_data.wallet.mifinity.destination_account` |
| SEPA bank transfer | SEPA | Bank transfer payouts with `payout_method_data.bank_transfer` and `payout_method_type: sepa` |

### Payout fields

* Mifinity wallet: `destination_account` is the required field under `payout_method_data.wallet.mifinity`.
* SEPA bank transfer: the standard SEPA fields apply under `payout_method_data.bank_transfer` with `payout_method_type: sepa`.

### Activating Mifinity Payouts via Hyperswitch

#### Prerequisites

1. A Mifinity business account with API access.
2. A registered Hyperswitch account, accessible from the [Hyperswitch control center](https://app.hyperswitch.io/).
3. A Mifinity API key, and your brand ID if your account uses one.

[Steps to activate a connector on the Hyperswitch control center](../../activate-connector-on-hyperswitch/README.md)

---

Connector implementation: payment connector at `crates/hyperswitch_connectors/src/connectors/mifinity.rs`; payout flows run through the unified connector service in `crates/router/src/core/unified_connector_service/`.
