---
description: >-
  Authenticate payments through Netcetera using client-certificate authentication.
metaLinks:
  alternates:
    - netcetera.md
---

# Netcetera

Netcetera handles external 3DS authentication rather than payment execution. It does not declare payment methods because its role ends when authentication data is returned for the payment connector. Merchants use it to add a dedicated authentication step to supported payment flows.

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch d4e93b6e6dd39e45a8d5d8647b362f1bb8543946; host http://localhost:8080; fetched 2026-09-14; matrix canonical-json-v1 sha256 1beab3d720a6bcc5; 138 connectors.
     Do not edit by hand. This block regenerates from the connector's
     SupportedPaymentMethods declaration in code; edit that instead. -->

**Integration status:** sandbox

**Category:** authentication provider

**Webhook flows:** None declared in code

_This connector declares no payment methods. It is an authentication provider rather than a payment processor._


### Authentication

Netcetera requires a PEM **Certificate** and matching **Private Key**. Hyperswitch maps them through `CertificateAuth` for mutual TLS and sends no HTTP authorization header. See [`NetceteraAuthType::try_from()`](https://github.com/juspay/hyperswitch/blob/d4e93b6e6dd39e45a8d5d8647b362f1bb8543946/crates/hyperswitch_connectors/src/connectors/netcetera/transformers.rs#L232-L246) and [`get_auth_header()`](https://github.com/juspay/hyperswitch/blob/d4e93b6e6dd39e45a8d5d8647b362f1bb8543946/crates/hyperswitch_connectors/src/connectors/netcetera.rs#L120-L125).

### Before you start

1. Contact [netcetera.com](https://www.netcetera.com/) to register for 3DS server access.
2. Sign in to the [Hyperswitch control center](https://app.hyperswitch.io/).
3. Obtain the PEM **Certificate** and matching **Private Key** during Netcetera onboarding.

Follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for Netcetera-specific behavior.

If your activation uses the external authentication flow, follow [External authentication for 3DS](../../../integration-guide/workflows/3ds-decision-manager/external-authentication-for-3ds.md) after the connector is enabled.

### Webhooks

Handled event wire values: **0** — Netcetera does not dispatch on individual event wire values. The incoming webhook implementation parses result callbacks for their external authentication reference (the 3DS server transaction ID) and resource object, and maps every callback to a single fixed event, `ExternalAuthenticationARes`. See [`IncomingWebhook for Netcetera`](https://github.com/juspay/hyperswitch/blob/d4e93b6e6dd39e45a8d5d8647b362f1bb8543946/crates/hyperswitch_connectors/src/connectors/netcetera.rs#L179-L211).

### Source reference

Authentication and webhook behavior on this page is tied to Hyperswitch `d4e93b6e6dd39e45a8d5d8647b362f1bb8543946`. See [Netcetera connector source](https://github.com/juspay/hyperswitch/blob/d4e93b6e6dd39e45a8d5d8647b362f1bb8543946/crates/hyperswitch_connectors/src/connectors/netcetera.rs) and [Netcetera transformers](https://github.com/juspay/hyperswitch/blob/d4e93b6e6dd39e45a8d5d8647b362f1bb8543946/crates/hyperswitch_connectors/src/connectors/netcetera/transformers.rs).
