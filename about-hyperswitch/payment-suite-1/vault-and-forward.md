---
description: >-
  Best for merchants who do not want to handle card data and want to maintain
  their current integration with the processors.
hidden: true
---

# Vault and Forward

In this approach, the Direct Payment Control Model functions by treating Juspay Hyperswitch as a secure "pipe." This setup grants you full control over your orchestration logic and the specific API calls sent to processors. The process initiates when the customer enters payment details into the Juspay Hyperswitch Vault SDK, where the data is directly tokenized within the Juspay Hyperswitch Vault.

For payments, your backend constructs a request intended for your specific processor, such as Stripe or Adyen, utilizing placeholders instead of raw card data. This request is then routed through the Juspay Hyperswitch Proxy. The proxy injects the actual card details immediately before forwarding the request to the processor, ensuring that raw card data never touches your servers.

This architecture allows you to maintain your legacy backend logic while significantly reducing PCI scope. It is particularly well-suited for scenarios where you plan to keep existing processor integrations. but require the removal of sensitive card data from your internal systems.

#### **Understanding Payment and Vault Flow**&#x20;

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
    participant C as Consumer
    participant MFE as Merchant FE
    participant SDK as Hyperswitch PM SDK
    participant MBE as Merchant BE
    participant HS as Hyperswitch BE
    participant V as Vault
    participant PSP as PSP

    MFE->>MBE: Create-payment-method-session with customer_id
    MBE->>HS: "Create-payment-method-session" API<br/>using Merchant HS API Key & Profile ID
    HS-->>MBE: Session id & client_secret
    MBE-->>MFE: Session id & client_secret

    Note over MFE: Create a script tag to load HyperLoader.js
    Note over MFE: Initialize window.Hyper using<br/>the Publishable Key
    Note over MFE: Create PMM elements group using<br/>SessionId & ClientSecret
    Note over MFE: Create specific widget instance<br/>& mount SDK

    C->>SDK: Add Payment method
    SDK->>HS: "Payment Method Session -<br/>Confirm a payment method session" API<br/>with card details
    HS->>V: Store card details
    Note over V: CVV is stored temporarily<br/>for a specific TTL or until first txn
    V-->>HS: Response
    HS-->>SDK: Response (Session id & associated_token_id)

    MBE->>HS: "Payment Method Session -<br/>List Payment Methods" API with Session id
    HS-->>MBE: Response (PM_ID)
    Note over MBE: Response contains all payment<br/>methods associated with customer
    Note over MBE: Choose the PM_ID for the<br/>Session id of the session
    Note over MBE: Making a proxy payment

    MBE->>HS: Send PSP payment request to<br/>Vault proxy endpoint with PM_ID
    HS->>PSP: Send PSP payment request to PSP<br/>(PM_ID replaced with actual card data)
    PSP-->>HS: Payment response
    HS-->>MBE: Payment response

    classDef default  fill:#F7F7F7,stroke:#CCCCCC,color:#1A1A1A,rx:6
    classDef accent   fill:#3F8CFF,stroke:#3F8CFF,color:#ffffff,rx:6
    classDef decision fill:#FFF8E1,stroke:#CCCCCC,color:#1A1A1A
    class C,MBE,PSP accent
```

*Caption: The complete Vault and Forward flow showing how merchants can tokenize card data using the Hyperswitch Vault SDK and later use the tokenized payment method ID for proxy payments. The flow includes session creation, SDK initialization, card vaulting, payment method retrieval, and the proxy payment execution where Hyperswitch replaces the token with actual card data before forwarding to the PSP.*



#### Vaulting&#x20;

**1. Create Payment Method Session (Server-Side)** The merchant server initiates the flow by calling the Hyperswitch [`Create-payment-method-session`](https://api-reference.hyperswitch.io/v2/payment-method-session/payment-method-session--create#payment-method-session-create) API with the `customer_id`. Hyperswitch responds with a `session_id` and `client_secret`, which are required to authenticate the client-side session.

**2. Initialize SDK (Client-Side)** The merchant client loads the `HyperLoader.js` script and initializes `window.Hyper` using the Publishable Key. Using the `session_id` and `client_secret`, the SDK creates a Payment Method Management (PMM) group and mounts the specific widget instance to the UI.

**3. Collect and Vault Card (Client-Side)** The customer enters their card details directly into the SDK-managed widget. Upon confirmation, the SDK calls the /`Confirm a payment method session` API. Hyperswitch securely receives the data, stores it in the Vault (retaining the CVV temporarily for the transaction TTL), and returns a success response with the `session_id` to the client.

**4. Retrieve Payment Method ID (Server-Side)** The merchant server calls the "List Payment Methods" API using the `session_id`. Hyperswitch returns a list of payment methods associated with the customer, from which the merchant server selects the appropriate `PM_ID` (Payment Method ID) to use for the transaction.



#### Payment

**Execute Proxy Payment (Server-Side)** The merchant server initiates the payment by sending a request to the [Hyperswitch vault proxy](https://docs.hyperswitch.io/~/revisions/01bZ2maqjwpnmrttix7i/explore-hyperswitch/payments-modules/vault/hyperswitch-vault-pass-through-proxy-payments) endpoint using the `payment_method_id` . The proxy securely replaces the token with the actual card data from the Vault and forwards the request to the Payment Service Provider (PSP), returning the final payment response to the merchant.



**Integration Documentation :**&#x20;

* [Vault SDK Integration](https://docs.hyperswitch.io/~/revisions/TGn71uwTlQJmyyiYgHpt/explore-hyperswitch/payments-modules/vault/vault-sdk-integration)
* [Proxy Payment Integration Guide](https://docs.hyperswitch.io/~/revisions/01bZ2maqjwpnmrttix7i/explore-hyperswitch/payments-modules/vault/hyperswitch-vault-pass-through-proxy-payments)
