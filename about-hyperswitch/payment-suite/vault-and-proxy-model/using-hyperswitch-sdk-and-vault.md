---
description: >-
  Best for merchants who do not want to handle card data and want to maintain
  their current integration with the processors.
---

# Using Hyperswitch SDK and Vault

In this workflow, the customer enters payment details into the Hyperswitch SDK, which tokenizes the data directly with the Hyperswitch Vault. Your backend then constructs a request intended for your processor (e.g., Stripe, Adyen) using placeholders instead of raw card data. This request is routed through the Hyperswitch Proxy, which injects the actual card details just before forwarding the request to the processor. This ensures raw card data never touches your servers, while allowing you to maintain your legacy backend logic.

#### The Workflow

* **Client:** The Hyperswitch SDK collects card details.
* **Token Storage:** The SDK securely sends card data directly to the Hyperswitch Vault, which returns a token (`payment_method_id`).
* **Merchant Backend:** The merchant Backend constructs a request intended for the processor, inserting placeholders (e.g., `{{$card_number}}`) instead of raw card data.
* **Orchestration:** Merchant Backend sends this constructed request to the Hyperswitch Proxy Endpoint, including the target processor's URL in the headers.
* **Proxy:** Hyperswitch receives the request, retrieves the real card data from the Vault using the token, and swaps the placeholders with the actual card details.
* **Card Forwarding:** Hyperswitch forwards the complete request (with raw data) to the external Processor (e.g., Stripe, Checkout.com).

<figure><img src="../../../.gitbook/assets/HS_SDK and Vault only.svg" alt=""><figcaption></figcaption></figure>

**Integration Documentation :**&#x20;

**Unified Checkout :**[ Integration guide](https://docs.hyperswitch.io/explore-hyperswitch/merchant-controls/integration-guide)

**Payment Execution :** [Proxy Payment API](https://docs.hyperswitch.io/about-hyperswitch/payments-modules/vault/hyperswitch-vault-pass-through-proxy-payments)
