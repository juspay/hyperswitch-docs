---
description: >-
  Store and retrieve sensitive payment credentials through vault providers
  integrated with Juspay Hyperswitch.
icon: vault
---

# Vault Providers

Juspay Hyperswitch supports external vault providers for storing sensitive payment credentials — card numbers, bank account details — independently of any payment processor. This allows you to retain ownership of tokenized data and route payments across processors without re-collecting credentials from customers.

### Hyperswitch built-in vault vs external vault providers

Hyperswitch ships with its own PCI-compliant built-in vault (`HyperswitchVault`) that handles card tokenization automatically when using the Unified Checkout SDK. External vault providers offer an alternative if you have an existing vault relationship or require vendor-specific tokenization formats.

### Supported Vault Providers

| Provider | Vault Type | Description |
| --- | --- | --- |
| **Hyperswitch Vault** | Built-in | Hyperswitch's own PCI-compliant vault. Used automatically by the Unified Checkout SDK. No separate activation required. |
| **VGS (Very Good Security)** | External | External vault with tokenization and proxy capabilities. Integrates via Hyperswitch's ExternalVault interface for insert and retrieve operations. |

### When to use an external vault provider

- You already have card data tokenized in an external vault and want to use Hyperswitch for payment orchestration without re-collecting card details
- Your compliance posture requires a specific vault vendor
- You need proxy-based tokenization (VGS transparent proxy model)

### Activating an external vault provider

External vault providers are configured as connectors in Hyperswitch.

[Steps to activate a connector on the Hyperswitch control center](../activate-connector-on-hyperswitch/README.md)
