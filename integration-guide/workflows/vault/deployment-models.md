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

<table>
<thead>
<tr>
<th width="250">Deployment Model</th>
<th width="200">Vault Options</th>
<th width="200">PCI Ownership / Scope</th>
<th>Example Use Case</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="3" style="vertical-align: middle; background-color: rgba(100, 100, 100, 0.1);"><strong>Vault Standalone</strong></td>
<td style="background-color: rgba(100, 100, 100, 0.1);"><a href="self-hosted-and-in-house-pci.md">SaaS Hyperswitch Vault</a></td>
<td style="background-color: rgba(100, 100, 100, 0.1);">Merchant PCI Environment</td>
<td style="background-color: rgba(100, 100, 100, 0.1);">Financial institutions requiring full data sovereignty and PCI control with raw payment method responses</td>
</tr>
<tr>
<td style="background-color: rgba(100, 100, 100, 0.1);"><a href="hyperswitch-vault-pass-through-proxy-payments.md">SaaS Hyperswitch Vault</a></td>
<td style="background-color: rgba(100, 100, 100, 0.1);">Non PCI Scope</td>
<td style="background-color: rgba(100, 100, 100, 0.1);">Merchants wanting to avoid PCI scope while maintaining existing PSP relationships via Proxy API</td>
</tr>
<tr>
<td style="background-color: rgba(100, 100, 100, 0.1);"><a href="connect-external-vaults-to-hyperswitch-orchestration.md">Third-Party Vault</a></td>
<td style="background-color: rgba(100, 100, 100, 0.1);">Merchant PCI Environment</td>
<td style="background-color: rgba(100, 100, 100, 0.1);">Merchants already using third-party vault providers like VGS, TokenEx, or similar services</td>
</tr>
<tr style="height: 10px;"><td colspan="4"></td></tr>
<tr>
<td rowspan="3" style="vertical-align: middle; background-color: rgba(120, 120, 120, 0.1);"><strong>Self-Hosted Pay Orchestrator</strong></td>
<td style="background-color: rgba(120, 120, 120, 0.1);"><a href="self-hosted-and-in-house-pci.md">Self-Hosted Hyperswitch Vault</a></td>
<td style="background-color: rgba(120, 120, 120, 0.1);">PCI Environment</td>
<td style="background-color: rgba(120, 120, 120, 0.1);">Large enterprises requiring full control over both orchestration and payment data</td>
</tr>
<tr>
<td style="background-color: rgba(120, 120, 120, 0.1);"><a href="self-hosted-orchestration-with-external-or-third-party-pci-vault.md">SaaS Hyperswitch Vault</a></td>
<td style="background-color: rgba(120, 120, 120, 0.1);">Non-PCI</td>
<td style="background-color: rgba(120, 120, 120, 0.1);">Mid-size merchants needing orchestration flexibility without PCI burden</td>
</tr>
<tr>
<td style="background-color: rgba(120, 120, 120, 0.1);"><a href="self-hosted-orchestration-with-external-or-third-party-pci-vault.md">Third-Party Vault</a></td>
<td style="background-color: rgba(120, 120, 120, 0.1);">Non-PCI</td>
<td style="background-color: rgba(120, 120, 120, 0.1);">Businesses with existing vault investments (VGS, TokenEx) adding orchestration</td>
</tr>
<tr style="height: 10px;"><td colspan="4"></td></tr>
<tr>
<td rowspan="2" style="vertical-align: middle; background-color: rgba(100, 100, 100, 0.1);"><strong>SaaS Pay Orchestrator</strong></td>
<td style="background-color: rgba(100, 100, 100, 0.1);"><a href="saas-orchestration-with-juspay-vault.md">SaaS Hyperswitch Vault</a></td>
<td style="background-color: rgba(100, 100, 100, 0.1);">Managed by Hyperswitch</td>
<td style="background-color: rgba(100, 100, 100, 0.1);">Growing businesses seeking fully managed payment infrastructure</td>
</tr>
<tr>
<td style="background-color: rgba(100, 100, 100, 0.1);"><a href="saas-orchestration-with-third-party-vault.md">Third-Party Vault</a></td>
<td style="background-color: rgba(100, 100, 100, 0.1);">Shared / External PCI Responsibility</td>
<td style="background-color: rgba(100, 100, 100, 0.1);">SaaS companies with compliance requirements for specific vault providers</td>
</tr>
</tbody>
</table>

<div align="center"><img src="../../../.gitbook/assets/vault-external-vaults.png" alt=""></div>

All deployment models share the same `payment_method_id` token standard and are compatible with the [Vault-Then-Pay](../../payment-suite/payment-method-card/README.md) payment flow.
