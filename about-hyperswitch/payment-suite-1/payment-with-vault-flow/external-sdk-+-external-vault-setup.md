---
description: >-
  Best for teams with strict existing vault dependencies who want to leverage
  Hyperswitch for payment routing.
---

# External SDK + External Vault Setup

In this approach, card data is captured and tokenized using an external vault SDK. Hyperswitch backend receives vault tokens and handles orchestration, routing, retries, and PSP communication via connectors.

The merchant configures connectors and orchestration logic in the Hyperswitch Dashboard. Hyperswitch does not participate in card capture or storage.



#### **Understanding Payment and Vault flow**

<figure><img src="../../../.gitbook/assets/Untitled (11).svg" alt=""><figcaption></figcaption></figure>

**1. Payment Initialization**

Your Merchant Server initiates the process by calling the [`payments/create`](https://api-reference.hyperswitch.io/v1/payments/payments--create) API. Hyperswitch returns the `payment_id` and `client_secret`. These credentials are then passed to your frontend to begin the secure session.



**2. Dual SDK Initialization**

The Hyperswitch SDK initializes on the frontend and performs two critical tasks:

* Retrieval: It fetches the list of available payment methods from the Hyperswitch Server.
* Vault Integration: It triggers the loading of the External Vault SDK. This creates a secure "iframe" or isolated field specifically for capturing card data.



**3. Secure Data Capture**

The customer enters their payment details into the checkout form.

* Isolation: The card numbers are entered directly into the External Vault SDK fields.
* Tokenization: Before the payment is even submitted to the processor, the Vault SDK sends the details to the External Vault, which returns a secure "token" representing that card.



**4. Payment Confirmation via Token**

When the customer clicks "Pay," the Hyperswitch SDK sends a confirmation request to the Hyperswitch Server. Instead of containing actual card numbers, this request contains the Vault Token.



**5. Orchestration and Processing**

The Hyperswitch Server uses this token to facilitate the transaction:

* Authorization: Hyperswitch communicates with the Hyperswitch Connector (the processor) to authorize the payment using the merchant’s credentials.
* Verification: The server confirms the transaction status and performs any necessary post-payment synchronization with the vault to ensure the record is updated.



**6. Completion**

Once the processor provides a final status, Hyperswitch communicates this back through the SDK. The customer is then redirected to your `return_url` to finalize the order experience.



#### **Handling Saved Card Payments When Using External Vault -**&#x20;

When working with an external vault provider, here’re the options available to handle a saved card transaction. (The above sequence diagram explain the flow using the 2nd option.)

**Option 1  -** Hyperswitch server uses the proxy payments flow of external vaults to send vault tokens in the PSP payment request. These tokens are replaced with raw card data by the external vault before the request is forwarded to the PSP.<br>

<figure><img src="../../../.gitbook/assets/unknown.png" alt=""><figcaption></figcaption></figure>

* **Option 2 -** Hyperswitch server uses the detokenize payments flow of external vaults to detokenize vault tokens and obtain the raw card info. This raw card info is used in the payment request before the request is sent to the PSP.\
  <br>

<figure><img src="../../../.gitbook/assets/unknown (1).png" alt=""><figcaption></figcaption></figure>

\
<br>

* **Option 3 -** Merchant server uses proxy payments flow of external vaults to send vault tokens in the Hyperswitch payment request. These tokens are replaced with raw card data by the external vault before the request is forwarded to the Hyperswitch. This Hyperswitch request with raw card info is sent to the PSP by Hyperswitch.

<figure><img src="../../../.gitbook/assets/unknown (2).png" alt=""><figcaption></figcaption></figure>



**Integration Documentation :**&#x20;

* **Unified Checkout :**[ Integration guide](https://docs.hyperswitch.io/explore-hyperswitch/merchant-controls/integration-guide)
* [Create Payment API](https://api-reference.hyperswitch.io/v1/payments/payments--create)
* [Unified Checkout: Saving Payment Methods](https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/tokenization-and-saved-cards/save-a-payment-method)
