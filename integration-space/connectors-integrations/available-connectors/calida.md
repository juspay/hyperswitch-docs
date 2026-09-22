---
description: Connect Calida through Hyperswitch.
metaLinks:
  alternates:
    - calida.md
---

# Calida

Calida gives merchants an alternative payment method integration in Hyperswitch. It declares wallet support in the capability block below, with method-specific capture, refund, mandate, region, and currency details there. Use the status and webhook declaration in that block when deciding whether to enable it.

To connect Calida to your Hyperswitch account, follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for connector-specific behavior.

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7; host http://localhost:8080; fetched 2026-09-21; matrix canonical-json-v1 sha256 873f2bbfe94dc9fda3279d10e6c077a8fe4a10d38f97f3aba64d57093c5245c4; 146 connectors.
     Do not edit by hand. Payment method rows regenerate from the
     connector's SupportedPaymentMethods declaration; countries and
     currencies come from pm_filters in config/development.toml.
     Webhook flows and capture methods print as declared; the
     declaration-gap check reconciles them in prose. Edit those
     sources instead. -->

**Integration status:** live

**Category:** alternative payment method

**Webhook flows:** payments

| Payment method | Type | Mandates | Refunds | Capture methods | Countries | Currencies |
|---|---|---|---|---|---|---|
| wallet | Bluecode | not supported | not supported | automatic | 30 | EUR |

### Authentication

Calida provides three values when you set up your account with them — contact Calida or visit [https://www.calida.com](https://www.calida.com) to get started:

| Field | Hyperswitch configuration | Description |
|---|---|---|
| **E-Order Token** | Connector API key | API token issued by Calida, sent as an `Authorization: token <E-Order Token>` header on every API request |
| **Shop Name** | Connector metadata | Your Calida shop identifier, sent as `shop_name` in each payment creation request |
| **Source verification key** | Webhook secret | Secret used to verify incoming Calida webhooks (see [Webhooks](#webhooks)) |

Enter these through the connector configuration form in the control center. The E-Order Token uses Hyperswitch's header-key authentication — see [`CalidaAuthType`](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/calida/transformers.rs#L158-L172) and the [auth header construction](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/calida.rs#L123-L134) in the connector source.

### Before you start

1. Set up a Calida account at [https://www.calida.com/](https://www.calida.com/) to obtain the E-Order Token, Shop Name, and Source verification key.
2. Sign in to the [Hyperswitch control center](https://app.hyperswitch.io/).
3. Open the connector configuration form and provide the fields named in Authentication.
4. Use the configured base URL for the environment you are enabling.

### Webhooks

Calida sends payment webhooks. Hyperswitch verifies each webhook using **HMAC-SHA512**: the signature arrives in the `x-eorder-webhook-signature` header (hex-encoded) and is computed over the **sorted, minified JSON** of the webhook body — not the raw request body. The HMAC secret is the **Source verification key** you configured in the connector webhook details.

Webhook statuses map to Hyperswitch payment states as follows:

| Calida status | Hyperswitch state |
|---|---|
| `COMPLETED` | Charged (payment succeeded) |
| `FAILED` | Failure |
| `MANUAL_PROCESSING` | Pending |
| `PENDING` | Authentication pending |
| `PAYMENT_INITIATED` | Authentication pending |

See [webhook verification](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/calida.rs#L621-L682) and [status mapping](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/calida/transformers.rs#L174-L185) in the connector source.

### Source reference

Authentication and webhook behavior on this page is tied to Hyperswitch `ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7`. See [Calida connector source](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/calida.rs) and [Calida transformers](https://github.com/juspay/hyperswitch/blob/ec9d1d22bf0257b7de4d4d8bbba4e27fd520bdf7/crates/hyperswitch_connectors/src/connectors/calida/transformers.rs).
