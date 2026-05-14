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

| Deployment Model | Vault Options | PCI Ownership / Scope | Example Use Case |
|---|---|---|---|
| | [SaaS Hyperswitch Vault](self-hosted-and-in-house-pci.md) | Merchant PCI Environment | Financial institutions requiring full data sovereignty and PCI control with raw payment method responses |
| **Vault Standalone** | [SaaS Hyperswitch Vault](hyperswitch-vault-pass-through-proxy-payments.md) | Non PCI Scope | Merchants wanting to avoid PCI scope while maintaining existing PSP relationships via Proxy API |
| | [Third-Party Vault](connect-external-vaults-to-hyperswitch-orchestration.md) | Merchant PCI Environment | Merchants already using third-party vault providers like VGS, TokenEx, or similar services |
| | [Self-Hosted Hyperswitch Vault](self-hosted-and-in-house-pci.md) | PCI Environment | Large enterprises requiring full control over both orchestration and payment data |
| **Self-Hosted Pay Orchestrator** | [SaaS Hyperswitch Vault](self-hosted-orchestration-with-external-or-third-party-pci-vault.md) | Non-PCI | Mid-size merchants needing orchestration flexibility without PCI burden |
| | [Third-Party Vault](self-hosted-orchestration-with-external-or-third-party-pci-vault.md) | Non-PCI | Businesses with existing vault investments (VGS, TokenEx) adding orchestration |
| **SaaS Pay Orchestrator** | [SaaS Hyperswitch Vault](saas-orchestration-with-juspay-vault.md) | Managed by Hyperswitch | Growing businesses seeking fully managed payment infrastructure |
| | [Third-Party Vault](saas-orchestration-with-third-party-vault.md) | Shared / External PCI Responsibility | SaaS companies with compliance requirements for specific vault providers |

<div align="center"><img src="../../../.gitbook/assets/vault-external-vaults.png" alt=""></div>

All deployment models share the same `payment_method_id` token standard and are compatible with the [Vault-Then-Pay](../../payment-suite/payment-method-card/README.md) payment flow.
