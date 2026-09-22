---
description: >-
  Configure network tokenisation, understand saved-card execution, and check the
  repository defaults for supported networks and connectors.
icon: shield-check
metaLinks:
  alternates:
    - network-tokenisation.md
---

# Network Tokenisation

Network tokenisation replaces a stored card number with a token issued through a card network. A payment can use that token only when the profile is enabled, the token service is configured, and the selected payment connector supports the flow.

For example, the Checkout connector identifies a Visa network token as `vts` and a Mastercard network token as `mdes`. Other connector-specific formats and decryption behavior belong on the connector page.

## Prerequisites

Complete these checks before testing a tokenised payment:

1. **Enable network tokenisation for the profile.** The `is_network_tokenization_enabled` database default is `false`.
2. **Configure the network tokenisation service.** The service configuration is optional at application startup. A tokenisation call made without it is rejected with `NetworkTokenizationServiceNotConfigured`, whose source message is `Network token service not configured`.
3. **Allow the card network and connector in deployment configuration.** The lists below are repository example defaults. Operators can change them for a deployment.
4. **Keep a card available in the vault for fallback.** The saved-card payment path can use the card when the token cannot be fetched or the selected connector is not enabled for network tokens.

## Repository example defaults

These values come from `config/config.example.toml`. They describe the repository example configuration, not every deployment.

| Configuration      | Example default                              | Count |
| ------------------ | -------------------------------------------- | ----: |
| Card networks      | Visa, American Express, Mastercard           |     3 |
| Payment connectors | Adyen, Cybersource, Peach Payments, TrustPay |     4 |

A connector can support cards without supporting Hyperswitch-managed network-token execution. Check the active deployment configuration before routing live traffic.

## How the lifecycle works

The saved-card sequence below describes the v1 path. Token fetching has separate v1 and v2 implementations, but the selection and deletion behavior cited here is v1-specific.

1. **Provision.** When an eligible card is saved and network tokenisation is enabled, Hyperswitch requests a network token. The payment method stores a network-token request reference, a network-token locker reference, and encrypted network-token metadata.
2. **Use.** A later payment supplies the saved `payment_method_id`. For the v1 saved-card path, Hyperswitch checks the profile flag, the selected connector against the configured allowlist, and the saved network-token request reference.
3. **Fetch fresh payment data.** When all checks pass, Hyperswitch fetches network-token payment data from the token service. The payment data can carry a cryptogram and ECI for connector authorization.
4. **Fall back to the card.** If the connector is not allowed, the request reference is absent, or the token fetch fails, Hyperswitch retrieves card details from the vault instead.
5. **Read status and maintain metadata.** Status checks read token state and expiration. Network-token webhooks can update stored expiration metadata. In v1, deleting the saved method invokes deletion from the token service and its locker record.

## Reuse across payment connectors

A saved network token is reusable across payment connectors only when each selected connector is in the deployment's `network_tokenization_supported_connectors` list. It is not automatically portable to every connector.

The saved-card network-token decision does not read `connector_tokens`. If `connector_tokens` is `null`, Hyperswitch can still select the network-token path when the profile is enabled, the selected connector is allowed, and the payment method has a network-token request reference. If any of those checks fail, the path uses the vaulted card.

## Vault and `payment_method_id`

`payment_method_id` is the stable reference used by a later payment. It identifies the saved payment method, while the card and network-token material remain behind the vault and token-service references.

Network tokenisation does not change payment-method ownership or sharing rules. For cross-merchant reuse and on-behalf-of operations, see [Platform organization concepts](../integration-guide/account-management/multiple-accounts-and-profiles/platform-organization-concepts.md).

For card storage and retrieval choices, see [Vault workflows](../integration-guide/workflows/vault/). For general card enablement and 3DS setup, see [Cards](payment-orchestration/quickstart/payment-methods-setup/cards.md).

## 3DS and cryptographic data

Network-token payment data carries a token cryptogram and ECI when the token service returns them. The network-token flow does not declare a separate data-only 3DS mode in the relevant payment, token, or vault-selection code.

Treat 3DS configuration and network tokenisation as separate checks. A connector may require its own authentication setup even when it accepts network-token fields.

## Payment Account Reference

The network-token data model carries an optional Payment Account Reference (PAR) in both v1 and v2. Token-service responses map PAR into that model when present.

A connector can also return `payment_account_reference` on a payment. Hyperswitch stores that value on the payment attempt and returns it in the payment response. Because both values are optional, do not assume that every token or connector response includes PAR.

## Connector and analytics details

* **Checkout:** Its adapter maps Visa network tokens to `vts` and Mastercard network tokens to `mdes`. See the [Checkout connector page](https://docs.hyperswitch.io/integrations/connectors-integrations/payment-processor-capabilities/available-connectors/checkout) for connector-owned setup and capability details.
* **Peach Payments:** The current connector directory has no dedicated Peach Payments page. Use [Connector configurations](https://docs.hyperswitch.io/integrations/connectors-integrations/payment-processor-capabilities/available-connectors) to check the published connector pages, and verify the active deployment configuration before relying on decryption behavior.
* **Control Center analytics:** Token execution and connector capability are not analytics definitions. See [Analytics](/broken/pages/BwHg28C74KoY3JgRzksn) for the available Control Center views and filters.
