---
description: >-
  Best for PCI compliant merchants requiring full control over UI rendering
  while leveraging Hyperswitch Vault for secure storage and payment routing.
---

# Using Merchant SDK with Hyperswitch Vault

In this approach, the merchant uses their own frontend SDK to capture card details. Card data is sent to Hyperswitch backend and stored in Hyperswitch Vault. The merchant must ensure PCI DSS compliance for card capture.

Once tokenized, Hyperswitch backend handles orchestration, routing, retries, and connector execution using vault tokens. All orchestration configuration is managed through the Hyperswitch Dashboard.

**The Workflow:**

* **Client:** The user enters card data into the Merchant's Custom UI.
* **Merchant Backend:** The client sends the raw card data to the Merchant's Backend Server.
* **API Call:** The Merchant Backend calls the Hyperswitch API (`/payment_methods`), passing the raw card details in the body.
* **Vaulting:** Hyperswitch stores the card in the Hyperswitch Vault and returns a `payment_method_id`.
* **Payment:** The Merchant Backend triggers a payment using payment method id.

<figure><img src="../../../.gitbook/assets/Untitled (3).svg" alt=""><figcaption></figcaption></figure>



**Integration Documentation :**&#x20;

1. **Tokenization :** [Server to Server Vault tokenization](https://docs.hyperswitch.io/about-hyperswitch/payments-modules/vault/server-to-server-vault-tokenization)
2. &#x20;**Payment Execution :** [Payment Create API ](https://api-reference.hyperswitch.io/v1/payments/payments--create) & [Payment Confirm API](https://api-reference.hyperswitch.io/v1/payments/payments--confirm)
