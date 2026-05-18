---
description: >-
  Two integration paths for storing payment methods in Juspay Hyperswitch Vault:
  Server-to-Server API or the Vault SDK
icon: plug-circle-bolt
metaLinks:
  alternates:
    - integration.md
---

# Vault Integration

Juspay Hyperswitch Vault supports two integration paths. Choose the one that matches your architecture:

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Server to Server</strong></td><td>Your backend directly calls the Vault REST API with raw card data. Requires your own PCI DSS compliance to handle card data on your servers.</td><td><a href="server-to-server-vault-tokenization.md">server-to-server-vault-tokenization.md</a></td></tr><tr><td><strong>SDK (Vault SDK)</strong></td><td>Card data is collected and tokenized entirely within Hyperswitch's PCI-compliant SDK iframe — no raw card data touches your servers.</td><td><a href="sdk-integration.md">sdk-integration.md</a></td></tr></tbody></table>

### Prerequisites (both paths)

Before integrating, complete the following on the Hyperswitch Control Centre:

1. Generate your **Vault API Key** and note your **Profile ID** — see [Vault Configuration](configuration.md).
2. Create at least one **Customer** record in the Vault so that saved payment methods can be associated with a `customer_id`.

### Which path should I use?

| | Server to Server | SDK |
|---|---|---|
| **PCI scope** | You handle raw card data → full PCI DSS required | Hyperswitch iframe handles card data → minimal PCI scope |
| **Frontend dependency** | None — pure backend API calls | Requires loading HyperLoader.js or the React/npm packages |
| **Best for** | B2B flows, migrations, batch tokenization, existing PCI-certified merchants | Consumer-facing checkout, fastest time-to-market |
| **Customer-facing UI** | Build your own | Pre-built, customizable Payment Methods Management widget |
