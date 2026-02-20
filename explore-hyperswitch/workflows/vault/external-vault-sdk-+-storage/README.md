---
description: >-
  Best for teams with strict existing vault dependencies who want to leverage
  Hyperswitch for payment routing.
hidden: true
icon: up-right-from-square
---

# External  Vault SDK + Storage

In this approach, card data is captured and tokenized using an external vault SDK. Hyperswitch backend receives vault tokens and handles orchestration, routing, retries, and PSP communication via connectors.

The merchant configures connectors and orchestration logic in the Hyperswitch Dashboard. Hyperswitch does not participate in card capture or storage.

#### Configuring External Vault on Hyperswitch

For External Vaults to work with Hyperswitch you need to configure the required API credentials on the Hyperswitch dashboard. You can do this by navigating to _**Orchestrator > Connector > Vault Processor**_ and entering the required details.

#### External Vaults SDK Setup -&#x20;

When utilizing External Vaults, merchants have the flexibility to define how payment method details are collected. Depending on your security and user experience requirements, you can choose between two primary integration paths:

* **Layered Integration:** In this flow, the External Vault SDK is layered directly onto the Hyperswitch Unified Checkout SDK. The External Vault SDK captures card details and tokenizes them immediately at the vault. This ensures that sensitive card data never touches the Hyperswitch server.
* **Independent Integration:** The External Vault SDK manages the card data and user experience entirely independently of the Hyperswitch SDK. The card is tokenized directly with your chosen vault, after which  you will have to pass the token returned by external vault along with the card metadata to Hyperswitch to process the payment.



### **Understanding the flow**&#x20;

#### **Layered Integration**

<figure><img src="../../../../.gitbook/assets/Untitled (19).svg" alt=""><figcaption></figcaption></figure>

**1. Payment Initialization**

Your Merchant Server initiates the process by calling the [`payments/create`](https://api-reference.hyperswitch.io/v1/payments/payments--create) API. Hyperswitch returns the `payment_id` and `client_secret`. These credentials are then passed to your frontend to begin the secure session.



**2. Dual SDK Initialization**

The Hyperswitch SDK initializes on the frontend and performs two critical tasks:

* Retrieval: It fetches the list of available payment methods from the Hyperswitch Server.
* Vault Integration: It triggers the loading of the External Vault SDK. This creates a secure "iframe" or isolated field specifically for capturing card data.



**3. Secure Data Capture**

The customer enters their payment details into the checkout form.

* Isolation: The card numbers are entered directly into the External Vault SDK fields.
* Tokenization: Before the payment is even submitted to the processor, the external Vault SDK sends the details to the External Vault, which returns a secure token representing that card.



**4. Payment Confirmation via Token**

When the customer clicks "Pay," the Hyperswitch SDK sends a confirmation request to the Hyperswitch Server. Instead of containing actual card numbers, this request contains the Vault Token.



**5. Orchestration and Processing**

The Hyperswitch uses the poxy API of the external vault and passed the the token, the external vault resplace the token with raw card data and send the payment request to the PSP.



**6. Completion**

Once the processor provides a final status, the response is relayed back from the external vault to  the SDK. The customer is then redirected to your `return_url` to finalize the order experience.



#### **Independent Integration**

<figure><img src="../../../../.gitbook/assets/Untitled (20).svg" alt=""><figcaption></figcaption></figure>

**1.Card Tokenization**

&#x20;The merchant integrates the External Vault SDK to securely capture and tokenize the customer's card details.



**2.Payment Initiation**

The merchant server triggers the Hyperswitch `payments/create` API, passing the external vault token within the request payload alongside standard payment parameters.



**3.Card Data Retrieval**

Hyperswitch securely communicates with the external vault to exchange the token for the raw card data.



**4.Processor Handover**

Hyperswitch routes the payment request to the chosen Payment Service Provider (PSP) using the raw card credentials.



**5.Payment Confirmation**

&#x20;The merchant receives the final `payments/create` API response, confirming the transaction status and payment details.

