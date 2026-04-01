---
description: >-
  Best for PCI compliant merchants requiring full control over UI rendering
  while leveraging Hyperswitch Vault for secure storage and payment routing.
---

# Merchant SDK + Hyperswitch Vault Setup

In this approach, the merchant uses their own frontend SDK to capture card details. Card data is sent to Hyperswitch backend and stored in Hyperswitch Vault. The merchant must ensure PCI DSS compliance for card capture.

Once tokenized, Hyperswitch backend handles orchestration, routing, retries, and connector execution using vault tokens. All orchestration configuration is managed through the Hyperswitch Dashboard.

#### Understanding Payment and Vault Workflow&#x20;

#### **Vaulting :**

<figure><img src="../../../.gitbook/assets/Untitled (6).svg" alt=""><figcaption></figcaption></figure>



**1. Create Payment (Server-Side)**

The merchant server calls the Hyperswitch `p`[`ayments/create`](https://api-reference.hyperswitch.io/v1/payments/payments--create) API with details such as `customer_id`, `amount`, `currency`, and `api_key`. Hyperswitch responds with a `payment_id` and other metadata required to proceed.

**2. Display Payment Methods and Customer Selection**

The merchant SDK renders the payment UI and shows eligible payment methods. The customer selects their desired payment method.

**3. Submit Transaction Request**

The SDK sends the transaction request, including card details, back to the merchant server.

**4. Confirm Payment (Server-Side)**

The merchant server calls `/payments/confirm` on Hyperswitch with the `payment_id` to initiate authorization and processing.

**5. Processor Authorization via Hyperswitch Connector**

Hyperswitch forwards the payment request to the processor through the Hyperswitch Connector. The processor authorizes the transaction and returns the response to Hyperswitch.

**6. Vault Card Data**

After successful authorization, Hyperswitch securely stores the card data in the Hyperswitch Vault. The vault tokenizes the card details and generates a  `payment_method_id` value which can be used further.

**7. Return Payment Response**

Hyperswitch sends the final payment response, including transaction status and the vaulted `payment_method_id`, back to the merchant server.



#### **Payment Using Stored Card :**&#x20;

<figure><img src="../../../.gitbook/assets/Untitled (7).svg" alt=""><figcaption></figcaption></figure>

&#x20;

**1. Fetch Saved Payment Methods**

The Merchant Server initiates a [list payment method API](https://api-reference.hyperswitch.io/v1/payment-methods/list-payment-methods-for-a-customer) call to the Hyperswitch Server to retrieve a list of previously stored payment instruments associated with a specific `customer_id`. The server returns `payment_method_id` for each saved card.

**2. UI Rendering and Instrument Selection**

The Merchant SDK populates the checkout interface with the retrieved saved cards. The User selects their preferred card on the merchant UI. Based on this selection, the merchant logic identifies the corresponding `payment_method_id` to be used for the transaction.

**3. Payment Creation with Auto-Confirmation**

The Merchant Server calls [ `v2/payments/create`](https://api-reference.hyperswitch.io/v2/payments/payments--create-and-confirm-intent) API along with the `payment_method_id` and setting the `confirm` parameter to `true` .

**4. Vault Decryption and Token Retrieval**

The Hyperswitch server sends payment method ID to the Hyperswitch Vault to fetch raw card data. The Vault retrieves the Raw Card Data required for the upstream processor and pass it in the API response.

**5. Transaction Routing and Connector Execution**

The Hyperswitch Server forwards the raw credentials to processor for authorization.

**6. Processor Authorization**

The Hyperswitch Connector handles the synchronous handshake with the external processor. Once the processor authorizes the transaction, the connector normalizes the response and transmits the authorization status back to the Hyperswitch

**7. Final Status Propagation**

The Hyperswitch Server sends the final transaction state (e.g., `succeeded`, `failed`) to  Merchant Server. This allows the backend to update the order status while the frontend notifies the user of the successful payment.



**API Reference :**

1. [Payment Create API ](https://api-reference.hyperswitch.io/v1/payments/payments--create)&#x20;
2. [Payment Confirm API](https://api-reference.hyperswitch.io/v1/payments/payments--confirm)&#x20;
3. [List Payment Method](https://api-reference.hyperswitch.io/v1/payment-methods/list-payment-methods-for-a-customer)
4. [Payment Create and Confirm API](https://api-reference.hyperswitch.io/v2/payments/payments--create-and-confirm-intent)
