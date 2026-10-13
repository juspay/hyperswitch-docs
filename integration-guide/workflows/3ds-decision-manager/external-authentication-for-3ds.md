---
description: >-
  Use a standalone 3DS server to authenticate a cardholder before authorizing
  the payment with a payment processor.
icon: up-right-from-square
metaLinks:
  alternates:
    - external-authentication-for-3ds.md
---

<!-- truth manifest; hyperswitch cfbeb2bedf523da301d7d7b0a8dcbeaf2263c696; spec api-reference/v1/openapi_spec_v1.json@cfbeb2bedf523da301d7d7b0a8dcbeaf2263c696
     symbols: request_external_three_ds_authentication = api-reference/v1/openapi_spec_v1.json:34256-34262
     symbols: NextActionData::ThreeDsInvoke = crates/api_models/src/payments.rs:6900-6903,6995-6999
     checked: 2026-10-01 -->

# Standalone 3D Secure (via Hyperswitch)

Standalone 3DS separates cardholder authentication from payment authorization. Use it when a dedicated 3DS provider should authenticate the cardholder before your payment processor authorizes the payment.

Set `request_external_three_ds_authentication` on the payment to request this path. When browser work is required, the payment can return a `three_ds_invoke` next action.

## Choose the provider guide

Provider setup and browser handling differ. Use the guide for the 3DS provider you configured:

* [Juspay 3DS Server browser walkthrough](external-3ds-with-the-juspay-3ds-server.md)
* [3DS provider setup pages](../../../integration-space/connectors-integrations/3ds-providers/README.md)

For processor-managed 3DS, use [Authenticate with 3D Secure via PSP](authenticate-with-3d-secure-via-psp.md) instead.
