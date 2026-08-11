---
icon: lock-hashtag
---

# Tokenized Card Collection

**Collect card details using the secure components of your chosen vault - through a single Hyperswitch SDK integration.**

Hyperswitch SDK supports **vault-specific card collection**. Based on the vault configured for your merchant account, the SDK loads the appropriate secure card-collection experience.

You can use:

* **Hyperswitch Vault**
* A supported third-party vault, such as **VGS**

The selected vault collects and tokenizes the card details. Hyperswitch then processes the payment using the returned token.

### Why Use Vault-Native Collection?

#### One SDK, Multiple Vaults

Integrate the Hyperswitch SDK once. The SDK loads the card-collection components required by the vault configured for your account.

You do not need to build and maintain a separate checkout integration for each supported vault provider.

#### Keep Card Data with Your Vault

When using an external or managed vault, card details are entered into vault-controlled fields and sent directly to the selected vault for tokenization.

Your payment flow uses a secure token instead of raw card details.

#### Self-Host Payments Without Self-Hosting Card Data

You can self-host the open-source Hyperswitch Payments Router while using:

* Hyperswitch Vault as a managed service
* A third-party vault such as VGS

This lets you control payment orchestration while keeping raw card data outside your self-hosted payments environment, helping reduce your PCI DSS scope and operational burden.

#### Choose the Deployment Model That Fits You

Use any supported combination:

* Self-hosted Hyperswitch Payments with Hyperswitch Vault SaaS
* Self-hosted Hyperswitch Payments with a third-party vault
* Self-hosted Hyperswitch Payments and Vault
* Hyperswitch SaaS with Hyperswitch Vault
* Hyperswitch SaaS with a supported third-party vault

### How It Works

1. Configure your preferred vault in the Hyperswitch Dashboard.
2. Initialize the Hyperswitch SDK using your existing payment-session flow.
3. The SDK identifies the configured vault.
4. The SDK loads that vault’s secure card-collection components.
5. The customer enters their card details.
6. The vault tokenizes the card and returns a token.
7. Hyperswitch processes the payment using the token.

**Card details → Selected vault → Vault token → Hyperswitch → Payment processor**

#### Example: VGS

When VGS is configured:

1. The Hyperswitch SDK loads the VGS card-collection experience.
2. The customer enters card details into VGS-controlled fields.
3. VGS tokenizes the card and returns a token.
4. Hyperswitch processes the payment using the VGS token.

Your application continues to use the Hyperswitch SDK without requiring a separate payment integration for VGS.

{% hint style="info" %}
**PCI DSS consideration:** Using a managed or third-party vault can significantly reduce the PCI DSS scope of your self-hosted payments environment. It does not automatically remove all PCI DSS responsibilities; the requirements depend on your complete integration and deployment architecture.
{% endhint %}
