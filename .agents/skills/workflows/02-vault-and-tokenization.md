---
name: hyperswitch-docs-vault
description: Use this skill when the user asks about "Hyperswitch vault documentation", "vault setup guide", "how to configure the Hyperswitch locker", "external vault integration", "third-party vault with Hyperswitch", "PCI vault setup", "server-to-server vault tokenization", "payment methods management SDK", "vault SDK integration", "self-hosted vault", "Juspay vault", or needs to understand vault architecture options and configuration in the docs.
version: 1.0.0
tags: [hyperswitch, docs, vault, tokenization, PCI, locker]
---

# Vault & Tokenization

## Overview

Hyperswitch supports multiple vault architectures — from the built-in Juspay Vault to external third-party vaults and fully self-hosted PCI environments. This skill maps the vault documentation so you can find the right guide for your architecture.

**Doc reference:** `explore-hyperswitch/workflows/vault/README.md`

---

## Vault Architecture Options

| Architecture | Use When | Doc |
|-------------|----------|-----|
| **Hyperswitch SDK + Hyperswitch Vault** | Standard — let Hyperswitch handle everything | `about-hyperswitch/payment-suite-1/payment-with-vault-flow/hyperswitch-sdk-+-hyperswitch-vault-setup.md` |
| **Merchant SDK + Hyperswitch Vault** | You collect card data, Hyperswitch vaults it | `payment-with-vault-flow/merchant-sdk-+-hyperswitch-vault-setup.md` |
| **SaaS + Juspay Vault** | Hyperswitch Cloud with Juspay's PCI vault | `explore-hyperswitch/workflows/vault/saas-orchestration-with-juspay-vault.md` |
| **SaaS + Third-Party Vault** | Use Basis Theory, Skyflow, or similar | `saas-orchestration-with-third-party-vault.md` |
| **External Vault SDK + Storage** | External vault + Hyperswitch routing | `external-vault-sdk-+-storage/` |
| **Self-hosted + In-House PCI** | Full control, your own PCI environment | `self-hosted-and-in-house-pci.md` |
| **Connect External Vault** | Connect any vault to Hyperswitch | `connect-external-vaults-to-hyperswitch-orchestration.md` |

---

## Standard Flow: Hyperswitch SDK + Vault

The simplest setup — Hyperswitch handles card collection and storage:

```
PaymentElement (browser) → Hyperswitch Vault (tokenisation) → Connector
```

1. Render `PaymentElement` in your frontend (see Web SDK skill)
2. Customer enters card → SDK sends directly to Hyperswitch (never touches your server)
3. Hyperswitch stores encrypted token, sends to connector
4. `payment_method_id` returned for future charges

**Doc reference:** `about-hyperswitch/payment-suite-1/payment-with-vault-flow/hyperswitch-sdk-+-hyperswitch-vault-setup.md`

---

## Server-to-Server Vault Tokenization

For server-side card collection (non-SDK flow):

```json
POST /payment_methods
{
  "payment_method": "card",
  "payment_method_type": "credit",
  "card": {
    "card_number": "4242424242424242",
    "card_exp_month": "03",
    "card_exp_year": "2030",
    "card_holder_name": "Jane Smith"
  },
  "customer_id": "cus_abc123"
}
```

**Doc reference:** `explore-hyperswitch/workflows/vault/server-to-server-vault-tokenization.md`

> ⚠️ Server-to-server card collection puts your server in PCI scope. Only use if you are PCI DSS certified for cardholder data.

---

## External Vault Integration

### Connect Any External Vault

Hyperswitch can call out to an external vault to retrieve tokens before sending to the connector:

```
Payment Request → Hyperswitch → External Vault (detokenise) → Connector
```

**Doc reference:** `explore-hyperswitch/workflows/vault/connect-external-vaults-to-hyperswitch-orchestration.md`

### Supported External Vault Patterns

- **Vault SDK + External Storage**: `explore-hyperswitch/workflows/vault/external-vault-sdk-+-storage/`
  - Processing with external vault: `processing-payments-with-external-vault.md`
- **Hyperswitch SDK + External Vault**: `explore-hyperswitch/workflows/vault/hyperswitch-sdk-+-external-vault.md`
- **Pass-Through Proxy**: `vault-pass-through-proxy-payments.md`

---

## Payment Methods Management SDK

The standalone Payment Methods Management SDK lets customers add, view, and delete saved payment methods without going through a full checkout:

```javascript
// Render payment methods management component
const pmSDK = hyper.elements({ mode: 'setup' });
const pmElement = pmSDK.create('paymentMethodsManagement');
pmElement.mount('#pm-management');
```

**Doc reference:** `explore-hyperswitch/workflows/vault/payment-methods-management-sdk.md`
Also: `about-hyperswitch/payment-suite-1/payment-method-management-sdk.md`

---

## Vault SDK Integration Guides

- Standard integration: `explore-hyperswitch/workflows/vault/vault-sdk-integration.md`
- Alternative approach: `explore-hyperswitch/workflows/vault/vault-sdk-integration-1.md`

---

## Production Tips

- Choose your vault architecture before writing any integration code — migrating vaulted cards between vault providers is complex and may require customer re-enrollment.
- For new integrations with no existing PCI compliance, use **Hyperswitch SDK + Hyperswitch Vault** — it gives SAQ A compliance with minimal effort.
- If you already use a third-party vault (Basis Theory, Skyflow, TokenEx), use the external vault connector rather than migrating card data.
- The Payment Methods Management SDK is essential for subscription products — it lets customers update expiring cards without cancelling their subscription.
