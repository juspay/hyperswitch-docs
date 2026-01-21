---
description: >-
  Best for merchants who need to retain a custom UI and maintain their existing
  integrations with processors.
---

# Using Merchant SDK and Vault

The Headless Proxy Integration is the architectural choice for brands that treat their checkout experience as a critical differentiator. It allows you to build a fully custom User Interface (UI) using your own design system while utilizing Hyperswitch’s client-side tokenization to secure the data. Like the Standard approach, it preserves your existing backend processor integrations.

#### The Workflow

1. **Capture (Frontend):** The user enters payment details into the Merchant's Custom UI (your own input fields and design).
2. **Tokenization:** Your backend securely sends card data directly to the Hyperswitch. The Hyperswitch Vault returns a secure token (`payment_method_id`) .
3. **Request Construction:** Your backend constructs the payload intended for the processor (e.g., Stripe) but inserts placeholders (e.g., `{{$card_number}}`) where the raw data would normally go.
4. **Proxy Tunneling:** Your backend sends this constructed request to the Hyperswitch Proxy Endpoint, including the target processor's URL, request body and headers.
5. **Card Forwarding :** Hyperswitch receives the request, retrieves the real card data from the Vault using the token, swaps the placeholders with the actual details, and forwards the complete request to the processor.

<figure><img src="../../../.gitbook/assets/HS_SDK and Vault.svg" alt=""><figcaption></figcaption></figure>

**Integration Documentation :**&#x20;

**Tokenisation :** [Server to Server Vault tokenization](https://docs.hyperswitch.io/about-hyperswitch/payments-modules/vault/server-to-server-vault-tokenization)

**Payment Execution :** [Proxy Payment API](https://docs.hyperswitch.io/about-hyperswitch/payments-modules/vault/hyperswitch-vault-pass-through-proxy-payments)
