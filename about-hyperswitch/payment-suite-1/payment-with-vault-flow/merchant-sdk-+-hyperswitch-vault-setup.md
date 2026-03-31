---
description: >-
  Best for PCI compliant merchants requiring full control over UI rendering
  while leveraging Hyperswitch Vault for secure storage and payment routing.
---

# Merchant SDK + Hyperswitch Vault Setup

In this approach, the merchant uses their own frontend SDK to capture card details. Card data is sent to Hyperswitch backend and stored in Hyperswitch Vault. The merchant must ensure PCI DSS compliance for card capture.

Once tokenized, Hyperswitch backend handles orchestration, routing, retries, and connector execution using vault tokens. All orchestration configuration is managed through the Hyperswitch Dashboard.

#### Understanding Payment and Vault Workflow

#### **Vaulting :**

```mermaid
%%{
  init: {
    'theme': 'base',
    'themeVariables': {
      'fontFamily': "'Inter', sans-serif",
      'background': '#ffffff00',
      'primaryColor': '#F7F7F7',
      'primaryBorderColor': '#CCCCCC',
      'primaryTextColor': '#1A1A1A',
      'lineColor': '#999999',
      'edgeLabelBackground': '#ffffff00'
    }
  }
}%%
sequenceDiagram
    participant User
    participant MerchantServer as Merchant Server
    participant MerchantSDK as Merchant SDK
    participant HSServer as Hyperswitch Server
    participant HSConnector as Hyperswitch Connector
    participant HSVault as Hyperswitch Vault

    MerchantServer->>HSServer: POST /payments/create (customer_id, amount, currency, api_key)
    HSServer-->>MerchantServer: Response with payment_id
    MerchantServer-->>MerchantSDK: Forward payment data
    Note over MerchantSDK: Displays Payment Methods
    Note over MerchantSDK: Customer selects payment method
    User->>MerchantSDK: Selects payment method
    MerchantSDK->>MerchantServer: Send transaction request with card details
    MerchantServer->>HSServer: POST /payments/confirm (payment_id)
    activate HSServer
    HSServer->>HSConnector: Send Request to Payment Processor
    activate HSConnector
    HSConnector-->>HSServer: Connector Response (Authorization)
    deactivate HSConnector
    HSServer->>HSVault: Send Request to store card data
    activate HSVault
    Note over HSVault: Vault stores Card Data,
 generates Token
    HSVault-->>HSServer: Response with payment_method_id
    deactivate HSVault
    HSServer-->>MerchantServer: Final payment response (status, payment_method_id)
    deactivate HSServer

classDef default  fill:#F7F7F7,stroke:#CCCCCC,color:#1A1A1A,rx:6
classDef accent   fill:#3F8CFF,stroke:#3F8CFF,color:#ffffff,rx:6
classDef decision fill:#FFF8E1,stroke:#CCCCCC,color:#1A1A1A
class User,MerchantServer accent
```

*Caption: The vaulting flow for storing card details securely. The merchant creates a payment, collects card details via their SDK, confirms the payment through Hyperswitch, and upon successful authorization, the card data is tokenized and stored in Hyperswitch Vault with a payment_method_id returned for future use.*



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

After successful authorization, Hyperswitch securely stores the card data in the Hyperswitch Vault. The vault tokenizes the card details and generates a `payment_method_id` value which can be used further.

**7. Return Payment Response**

Hyperswitch sends the final payment response, including transaction status and the vaulted `payment_method_id`, back to the merchant server.



#### **Payment Using Stored Card :**

```mermaid
%%{
  init: {
    'theme': 'base',
    'themeVariables': {
      'fontFamily': "'Inter', sans-serif",
      'background': '#ffffff00',
      'primaryColor': '#F7F7F7',
      'primaryBorderColor': '#CCCCCC',
      'primaryTextColor': '#1A1A1A',
      'lineColor': '#999999',
      'edgeLabelBackground': '#ffffff00'
    }
  }
}%%
sequenceDiagram
    participant User
    participant MerchantServer as Merchant Server
    participant MerchantSDK as Merchant SDK
    participant HSServer as Hyperswitch Server
    participant HSConnector as Hyperswitch Connector
    participant HSVault as Hyperswitch Vault

    MerchantServer->>HSServer: GET /customers/{id}/payment_methods
    HSServer-->>MerchantServer: Response with payment_method_id(s)
    MerchantServer-->>MerchantSDK: Forward saved payment methods
    Note over MerchantSDK: Displays Payment Methods along with saved cards
    Note over MerchantSDK: User selects a payment method
    User->>MerchantSDK: Selects saved card
    MerchantServer->>HSServer: POST /payments/create (confirm=true, payment_method_id)
    activate HSServer
    HSServer->>HSVault: Fetch tokens (payment_method_id)
    activate HSVault
    HSVault-->>HSServer: Return Raw Card Data
    deactivate HSVault
    HSServer->>HSConnector: Process Payment Using Raw Card Data
    activate HSConnector
    HSConnector-->>HSServer: Connector Response
    deactivate HSConnector
    HSServer-->>MerchantSDK: Payment status update
    HSServer-->>MerchantServer: payment/create response with payment status
    deactivate HSServer

classDef default  fill:#F7F7F7,stroke:#CCCCCC,color:#1A1A1A,rx:6
classDef accent   fill:#3F8CFF,stroke:#3F8CFF,color:#ffffff,rx:6
classDef decision fill:#FFF8E1,stroke:#CCCCCC,color:#1A1A1A
class User,MerchantServer accent
```

*Caption: The payment flow using a stored card. The merchant retrieves saved payment methods for the customer, the user selects a vaulted card, and the merchant creates a payment with auto-confirmation. Hyperswitch fetches the raw card data from the vault and processes the payment through the connector, returning the final status to the merchant.*

**1. Fetch Saved Payment Methods**

The Merchant Server initiates a [list payment method API](https://api-reference.hyperswitch.io/v1/payment-methods/list-payment-methods-for-a-customer) call to the Hyperswitch Server to retrieve a list of previously stored payment instruments associated with a specific `customer_id`. The server returns `payment_method_id` for each saved card.

**2. UI Rendering and Instrument Selection**

The Merchant SDK populates the checkout interface with the retrieved saved cards. The User selects their preferred card on the merchant UI. Based on this selection, the merchant logic identifies the corresponding `payment_method_id` to be used for the transaction.

**3. Payment Creation with Auto-Confirmation**

The Merchant Server calls [`v2/payments/create`](https://api-reference.hyperswitch.io/v2/payments/payments--create-and-confirm-intent) API along with the `payment_method_id` and setting the `confirm` parameter to `true`.

**4. Vault Decryption and Token Retrieval**

The Hyperswitch server sends payment method ID to the Hyperswitch Vault to fetch raw card data. The Vault retrieves the Raw Card Data required for the upstream processor and pass it in the API response.

**5. Transaction Routing and Connector Execution**

The Hyperswitch Server forwards the raw credentials to processor for authorization.

**6. Processor Authorization**

The Hyperswitch Connector handles the synchronous handshake with the external processor. Once the processor authorizes the transaction, the connector normalizes the response and transmits the authorization status back to the Hyperswitch

**7. Final Status Propagation**

The Hyperswitch Server sends the final transaction state (e.g., `succeeded`, `failed`) to Merchant Server. This allows the backend to update the order status while the frontend notifies the user of the successful payment.



**API Reference :**

1. [Payment Create API](https://api-reference.hyperswitch.io/v1/payments/payments--create)&#x20;
2. [Payment Confirm API](https://api-reference.hyperswitch.io/v1/payments/payments--confirm)&#x20;
3. [List Payment Method](https://api-reference.hyperswitch.io/v1/payment-methods/list-payment-methods-for-a-customer)
4. [Payment Create and Confirm API](https://api-reference.hyperswitch.io/v2/payments/payments--create-and-confirm-intent)
