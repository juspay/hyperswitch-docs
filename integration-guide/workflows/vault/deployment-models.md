---
description: >-
  Choose the right Vault deployment model based on your hosting preference and
  PCI compliance posture
icon: layer-group
metaLinks:
  alternates:
    - deployment-models.md
---

# Vault Deployment Models

Juspay Hyperswitch supports multiple vault deployment models to match your PCI profile and infrastructure preferences. The table below summarizes each option; click a row to read the full integration guide.

**Deployment Model: Standalone Vaulting Service**

<table><thead><tr><th width="200">Vault Options</th><th width="200">PCI Ownership / Scope</th><th>Example Use Case</th></tr></thead><tbody><tr><td><a href="vault-standalone-saas-vault-pci.md">SaaS Hyperswitch Vault</a></td><td>Merchant PCI Environment</td><td>Financial institutions requiring full data sovereignty and PCI control with raw payment method responses</td></tr><tr><td><a href="vault-standalone-saas-vault-non-pci.md">SaaS Hyperswitch Vault</a></td><td>Non PCI Scope</td><td>Merchants wanting to avoid PCI scope while maintaining existing PSP relationships via Proxy API</td></tr><tr><td><a href="connect-external-vaults-to-hyperswitch-orchestration.md">Third-Party Vault</a></td><td>Merchant PCI Environment</td><td>Merchants already using third-party vault providers like VGS, TokenEx, or similar services</td></tr></tbody></table>

**Deployment Model: Self-Hosted Payments Orchestrator with Vaulting Service**

|                                                                                          |                 |                                                                                   |
| ---------------------------------------------------------------------------------------- | --------------- | --------------------------------------------------------------------------------- |
| [Self-Hosted Hyperswitch Vault](self-hosted-and-in-house-pci.md)                         | PCI Environment | Large enterprises requiring full control over both orchestration and payment data |
| [SaaS Hyperswitch Vault](self-hosted-orchestration-with-saas-vault.md)                   | Non-PCI         | Mid-size merchants needing orchestration flexibility without PCI burden           |
| [Third-Party Vault](self-hosted-orchestration-with-external-or-third-party-pci-vault.md) | Non-PCI         | Businesses with existing vault investments (VGS, TokenEx) adding orchestration    |

**Deployment Model: SaaS Payments Orchestrator with Vaulting Service**

|                                                                   |                                      |                                                                          |
| ----------------------------------------------------------------- | ------------------------------------ | ------------------------------------------------------------------------ |
| [SaaS Hyperswitch Vault](saas-orchestration-with-juspay-vault.md) | Managed by Hyperswitch               | Growing businesses seeking fully managed payment infrastructure          |
| [Third-Party Vault](saas-orchestration-with-third-party-vault.md) | Shared / External PCI Responsibility | SaaS companies with compliance requirements for specific vault providers |

<div align="center"><img src="../../../.gitbook/assets/vault-external-vaults.png" alt=""></div>

All deployment models share the same `payment_method_id` token standard and are compatible with the [Vault-Then-Pay](../../payment-suite/payment-method-card/) payment flow.
