---
description: >-
  Ideal for teams seeking data independence in a neutral vault combined with
  Hyperswitch’s optimized payment UI and routing .
---

# Using Hyperswitch SDK with External Vault

In this approach, the Hyperswitch SDK is used to capture card details, but card storage and tokenization are handled by an external vault. Hyperswitch backend orchestrates payments using tokens issued by the external vault.

The merchant configures connectors and routing rules in the Hyperswitch Dashboard. Hyperswitch backend translates orchestration decisions into PSP specific requests using the provided external vault tokens.

**The Workflow:**

* **Client:** The Hyperswitch SDK collects card details.
* **Routing:** The SDK sends the Card data to Hyperswitch Core/ Backend.
* **External Tokenization:** Hyperswitch detects an "External Vault" configuration. Instead of storing the Card Data in its own DB, it sends a request to the External Vault to store the Card Data.
* **Mapping:** The External Vault returns a third-party token (e.g., tok\_ext\_123). Hyperswitch saves this token and maps it to a Hyperswitch `payment_method_id.`
* **Payment:** When a payment is initiated, Hyperswitch retrieves the raw card data using the third-party token and sends the data to the Processor (Connector).

<figure><img src="../../../.gitbook/assets/External_Vault +HS_SDK .svg" alt=""><figcaption></figcaption></figure>

**Integration Documentation :**

* **Unified Checkout :**[ Integration guide](https://docs.hyperswitch.io/explore-hyperswitch/merchant-controls/integration-guide)
* **Primary Guide:**[ Unified Checkout: Saving Payment Methods](https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/tokenization-and-saved-cards/save-a-payment-method)
