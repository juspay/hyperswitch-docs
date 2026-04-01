---
description: >-
  Self-host Hyperswitch orchestration while outsourcing PCI compliance to an
  external vault provider like VGS or Tokenex
icon: up-right-from-square
---

# Self-Hosted Orchestration with external or third party PCI Vault

> **Deployment Model:** Merchant self-hosts Hyperswitch Orchestration Layer
>
> **PCI Scope:** Outsourced to an external vault provider like VGS

### Overview

In this deployment model, merchants **self-host** the Juspay Hyperswitch orchestration layer on their own infrastructure while **outsourcing** all PCI DSS responsibilities to an external, PCI-compliant vault provider. Sensitive cardholder data (PAN, CVV, expiry) never touches the merchant's servers.

This architecture gives merchants full control over orchestration logic, routing rules, and business configurations while eliminating the burden of achieving and maintaining PCI DSS Level 1 compliance in-house

### Why This Model?

<table><thead><tr><th width="204.40625">Concern</th><th>How It's Addressed</th></tr></thead><tbody><tr><td><strong>PCI Compliance</strong></td><td>Fully offloaded to the vault provider (VGS, Tokenex, etc.)</td></tr><tr><td><strong>Hosting Independence</strong></td><td>Merchant retains complete control of the Hyperswitch deployment</td></tr><tr><td><strong>Sensitive Data Exposure</strong></td><td>Raw card data never enters the merchant's environment</td></tr><tr><td><strong>Token Portability</strong></td><td><code>payment_method_id</code> unifies <code>vault_token</code> + <code>psp_token</code> + <code>customer_id</code> for cross-platform use</td></tr><tr><td><strong>Operational Simplicity</strong></td><td>No need to manage HSMs, key rotation, or cardholder data environments</td></tr></tbody></table>

#### **Supported providers include (but are not limited to):**

* **VGS (Very Good Security)** — Provides inbound/outbound proxy routes for card data. Hyperswitch sends PSP payloads through VGS's forward proxy, which replaces tokens with raw card data in transit.
* **Tokenex** — Offers a transparent gateway proxy. Hyperswitch sends tokenized payloads to Tokenex's proxy, which detokenizes and forwards to the PSP.
* **Any vault with a proxy/detokenize API** — Hyperswitch's modular vault architecture supports any vault that exposes a tokenize + proxy (or detokenize) HTTP API.

Hyperswitch's modular vault architecture supports configuring multiple vault connectors simultaneously. You can route different merchants or payment methods to different vaults based on your business logic.

### Integration Steps

#### Option 1: Merchant Managed Client

The merchant client/checkout integrates the external vault SDK **directly** which takes away the PCI scope for the merchant, collect the card details and tokenizes it. The merchant server then passes the resulting token and metadata to Hyperswitch Backend for payment processing.

<details>

<summary><strong>New User Payment Flow</strong></summary>

* The merchant loads the external vault SDK in their checkout page.
* The end user enters their card details directly in the external vault SDK.
* The external vault SDK tokenizes the card and returns a `vault_token` and associated card metadata.
* The merchant calls the [Payments Create API](https://api-reference.hyperswitch.io/v1/payments/payments--create) to send the `vault_token` and card metadata to the self-hosted Hyperswitch backend.
* Hyperswitch constructs the PSP payload using the `vault_token`.
* The PSP payload (containing the `vault_token`) is sent to the **Proxy endpoint** of the external vault.
* The external vault replaces the `vault_token` with the raw card and forwards the request to the PSP.
* The PSP responds with `approved` or `declined` along with a `psp_token`. The vault proxy relays this response back to Hyperswitch.
* Hyperswitch generates a `payment_method_id` linking `customer_id`, `vault_token`, and `psp_token`.
* The `payment_method_id` and `vault_token` are returned to the merchant via webhooks.

</details>

<details>

<summary><strong>Repeat User Payment Flow</strong></summary>

* The merchant retrieves the customer's stored payment methods using the [Payment Method — List Customer Saved Payment Methods](https://api-reference.hyperswitch.io/v2/payment-methods/payment-method--list-customer-saved-payment-methods-v1) API with the `customer_id`
* The merchant calls the [Payments Create API](https://api-reference.hyperswitch.io/v1/payments/payments--create) with the corresponding `payment_method_id`
* Hyperswitch resolves the `payment_method_id` to identify the associated `psp_token` and processes the payment by sending the transaction to the corresponding PSP as a MIT

</details>

<details>

<summary><strong>Merchant-Initiated Transaction (MIT) Flow</strong></summary>

* The merchant triggers an [MIT or Recurring transaction](https://docs.hyperswitch.io/about-hyperswitch/payment-suite-1/payments-cards/recurring-payments) using the `payment_method_id.`
* Hyperswitch resolves the `payment_method_id` to identify the associated `psp_token` and processes the payment by sending the transaction to the corresponding PSP as a MIT

</details>

#### Option 2: Juspay Hyperswitch Managed Merchant Client

This is an extension of the previous approach where instead of the merchant client directly mounting the external Vault SDK on their checkout client, merchant client mounts the Hyperswitch SDK which internally loads the external Vault SDK and handles token management.

<details>

<summary><strong>New User Payment Flow</strong></summary>

* The merchant loads the [Hyperswitch Payments SDK](https://docs.hyperswitch.io/explore-hyperswitch/payment-experience/payment) via a [Payments Create API](https://api-reference.hyperswitch.io/v1/payments/payments--create) request. The Hyperswitch SDK in turn loads the external vault SDK configured in the merchant account.
* The end user enters their card details directly into the external vault SDK's secure iframe/fields.
* The external vault SDK tokenizes the card and returns a `vault_token` along with card metadata (last four digits, card brand, expiry) to the Hyperswitch SDK.
* The Hyperswitch SDK sends a [Payment Confirm API](https://api-reference.hyperswitch.io/v1/payments/payments--confirm) request containing the `vault_token` and card metadata to the self-hosted Hyperswitch backend.
* Hyperswitch constructs the PSP payload using the `vault_token`.
* The PSP payload (containing the `vault_token`) is sent to the **Proxy endpoint** of the external vault.
* The external vault replaces the `vault_token` with the raw card data and forwards the request to the PSP.
* The PSP responds with `approved` or `declined` along with a `psp_token`. The vault proxy relays this response back to Hyperswitch.
* Hyperswitch generates a `payment_method_id` linking `customer_id`, `vault_token`, and `psp_token`.
* The `payment_method_id` and `vault_token` are returned to the merchant via webhooks.

</details>

<details>

<summary><strong>Repeat User Payment Flow</strong></summary>

* The Hyperswitch SDK loads stored payment methods using the `customer_id` from the [Payments Create API](https://api-reference.hyperswitch.io/v1/payments/payments--create) request.
* The end user selects a saved card
* The SDK sends a [Payment Confirm API](https://api-reference.hyperswitch.io/v1/payments/payments--confirm) request and sends the corresponding `payment_method_id`
* Hyperswitch resolves the `payment_method_id` to identify the associated `psp_token` and processes the payment by sending the transaction to the corresponding PSP as a MIT

</details>

<details>

<summary><strong>Merchant-Initiated Transaction (MIT) Flow</strong></summary>

* The merchant triggers an [MIT or Recurring transaction](https://docs.hyperswitch.io/about-hyperswitch/payment-suite-1/payments-cards/recurring-payments) using the `payment_method_id.`
* Hyperswitch resolves the `payment_method_id` to identify the associated `psp_token` and processes the payment by sending the transaction to the corresponding PSP as a MIT

</details>

<details>

<summary><strong>Flow Diagram</strong></summary>



</details>

### Key Concepts

#### `payment_method_id`

A **universal, portable token** generated by Hyperswitch that serves as the single reference for a stored payment method. It connects:

| Entity        | Description                                                         |
| ------------- | ------------------------------------------------------------------- |
| `customer_id` | The Hyperswitch customer identifier                                 |
| `vault_token` | The token issued by the external vault representing the stored card |
| `psp_token`   | The token issued by the PSP after a successful transaction          |

This abstraction allows merchants to:

* Switch PSPs without re-collecting card data.
* Switch vault providers without breaking existing customer references.
* Use a single identifier across all payment flows (first-time, repeat, MIT/recurring).

***

### Configuration Guide

#### Configuring the External Vault in Juspay Hyperswitch

To enable an external vault with your self-hosted Hyperswitch instance:

1. **Navigate to the Hyperswitch Dashboard:** `Orchestrator → Connector → Vault Processor`
2. **Select your vault provider** (VGS, Tokenex, or Custom)
3.  **Enter the required API credentials:**

    | Provider    | Required Credentials               |
    | ----------- | ---------------------------------- |
    | **VGS**     | Vault ID, Client Secret, Client ID |
    | **Tokenex** | Token Scheme, API Key, Tokenex ID  |
4. **Test the integration** — Use the Hyperswitch Payments API with the external vault token to verify the payment flows with the various PSP integrations

#### Environment Variables (Self-Hosted)

When self-hosting, ensure the following environment configuration in your `config/development.toml` (or equivalent):

```toml
[vault]
# Enable external vault integration
enabled = true

# Vault provider: "juspay", "vgs", "tokenex", or "custom"
provider = "juspay"

# Base URL for the vault API
base_url = "https://vault.juspay.in"

# Base URL for the vault proxy endpoint
proxy_url = "https://proxy.vault.juspay.in"
```

> **Important:** Vault credentials should be stored securely (e.g., via environment variables or a secrets manager) and never committed to version control.

***

### Comparison: Self-Hosted Vault Deployment Models

<table><thead><tr><th width="138.015625">Feature</th><th>Self-Hosted + In-House PCI</th><th>Self-Hosted + Outsourced PCI (This Model)</th><th>SaaS + Outsourced PCI</th></tr></thead><tbody><tr><td><strong>Hosting</strong></td><td>Merchant</td><td>Merchant</td><td>Juspay (SaaS)</td></tr><tr><td><strong>PCI Scope</strong></td><td>Merchant (Level 1)</td><td>Vault Provider</td><td>Juspay + Vault Provider</td></tr><tr><td><strong>Vault</strong></td><td>Merchant's own vault</td><td>VGS / Tokenex</td><td>VGS / Tokenex</td></tr><tr><td><strong>Card Data on Server</strong></td><td>Yes</td><td>No</td><td>No</td></tr><tr><td><strong>Orchestration Control</strong></td><td>Full</td><td>Full</td><td>Managed</td></tr><tr><td><strong>Setup Complexity</strong></td><td>High</td><td>Medium</td><td>Low</td></tr><tr><td><strong>Compliance Maintenance</strong></td><td>High</td><td>None</td><td>None</td></tr><tr><td><strong>Token Portability</strong></td><td>Depends</td><td>Yes (<code>payment_method_id</code>)</td><td>Yes (<code>payment_method_id</code>)</td></tr></tbody></table>

***

### Security Considerations

* **TLS Everywhere:** All communication between Hyperswitch, the vault, and PSPs must use TLS 1.2+.
* **Credential Rotation:** Regularly rotate vault API keys and proxy credentials.
* **Audit Logging:** Enable Hyperswitch audit logs for all vault operations (tokenize, detokenize, proxy calls) to maintain compliance evidence.
* **Network Segmentation:** Even though PCI is outsourced, restrict network access between your Hyperswitch deployment and the vault to only the required endpoints and ports.
* **Webhook Verification:** Always verify webhook signatures for `payment_method_id` callbacks to prevent spoofing.

***

### FAQ

**Q: Does raw card data ever touch my self-hosted Hyperswitch server?** A: No, the card is tokenized on the client side or by the vault SDK before it reaches your server.

**Q: Can I switch vault providers without affecting existing customers?** A: Yes. Since Hyperswitch uses `payment_method_id` as the universal reference, you can migrate vault tokens between providers. Hyperswitch will update the internal mapping from `payment_method_id` → new `vault_token`.

**Q: What PCI SAQ level applies to me in this model?** A: Typically **SAQ A-EP** (if you host the checkout page) or **SAQ A** (if the vault SDK iframe handles all card input). Consult your QSA for a definitive assessment.

**Q: Can I use multiple vault providers simultaneously?** A: Hyperswitch's modular vault architecture supports configuring multiple vault connectors. You can route different merchants or payment methods to different vaults based on your business logic.

***

### Related Documentation

* [Vault — Modular Vaulting in Hyperswitch](https://docs.hyperswitch.io/explore-hyperswitch/workflows/vault)
* [SaaS Orchestration with Third-Party Vault](https://docs.hyperswitch.io/explore-hyperswitch/workflows/vault/saas-orchestration-with-third-party-vault)
* [Payments SDK Integration](https://docs.hyperswitch.io/explore-hyperswitch/payment-experience/payment)
* [Recurring Payments](https://docs.hyperswitch.io/about-hyperswitch/payment-suite-1/payments-cards/recurring-payments)
* [PCI DSS 4.0 Compliance](https://hyperswitch.io/pci.pdf)
