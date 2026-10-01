---
description: >-
  Activate the Juspay 3DS Server connector in Hyperswitch and provide the
  merchant metadata required for standalone 3DS authentication.
metaLinks:
  alternates:
    - juspaythreedsserver.md
---

# Juspay 3DS Server

Juspay 3DS Server handles standalone 3DS authentication for card payments. Enable it in the Hyperswitch Control Center, enter the merchant authentication metadata, then follow the external 3DS workflow guide.

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch c934d28c22cb7dbf3e6fcf58e39305556cc177ea; host http://localhost:8080; fetched 2026-10-01; matrix canonical-json-v1 sha256 8b92b42f08eb323a31ea974c99ac67dc4972774ab49bda767a79da9d2992fd5b; 147 connectors.
     Do not edit by hand. Payment method rows regenerate from the
     connector's SupportedPaymentMethods declaration; countries and
     currencies come from pm_filters in config/development.toml.
     Webhook flows and capture methods print as declared; the
     declaration-gap check reconciles them in prose. Edit those
     sources instead. -->

**Integration status:** alpha

**Category:** authentication provider

**Webhook flows:** None declared in code

_This connector declares no payment methods. It is a authentication provider rather than a payment processor._

### Activation fields

The connector configuration declares `NoKey`. The Control Center does not ask for an API key or bearer token when you activate this connector.

Have these merchant-specific values ready:

- **ThreeDS requestor name:** Optional text.
- **ThreeDS request id:** Required text.
- **merchant_category_code:** Required text.
- **merchant_country_code:** Required text.
- **merchant_name:** Required text.
- **Pull Mechanism Enabled:** Required toggle.

### Activate the connector

1. Sign in to the [Hyperswitch Control Center](https://app.hyperswitch.io/).
2. Follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md).
3. Select **Juspay 3DS Server** and complete the activation fields above.
4. Follow [External 3DS with the Juspay 3DS Server](../../../integration-guide/workflows/3ds-decision-manager/external-3ds-with-the-juspay-3ds-server.md) to integrate the payment and browser steps.

### Webhooks

Handled webhook event wire values: **0**. The feature matrix declares no webhook flows. The connector's incoming-webhook methods return `WebhooksNotImplemented`.

### Troubleshooting

**The activation form asks for an API key**

The current connector configuration does not define an API key field. Confirm that you selected **Juspay 3DS Server**. Do not put an API key into a metadata field.

**The connector cannot be saved because metadata is missing**

Complete every required activation field above. Only **ThreeDS requestor name** is optional in the current configuration.

### Source reference

The activation fields and webhook behavior on this page are tied to Hyperswitch `c934d28c22cb7dbf3e6fcf58e39305556cc177ea`. See the [production connector configuration](https://github.com/juspay/hyperswitch/blob/c934d28c22cb7dbf3e6fcf58e39305556cc177ea/crates/connector_configs/toml/production.toml#L7043-L7079), [connector specification](https://github.com/juspay/hyperswitch/blob/c934d28c22cb7dbf3e6fcf58e39305556cc177ea/crates/hyperswitch_connectors/src/connectors/juspaythreedsserver.rs#L631-L674), and [connector validation](https://github.com/juspay/hyperswitch/blob/c934d28c22cb7dbf3e6fcf58e39305556cc177ea/crates/router/src/core/connector_validation.rs#L371-L379).
