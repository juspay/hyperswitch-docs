---
description: >-
  Server to Server tokenization with Hyperswitch Vault Service for PCI compliant
  merchants
icon: server
metaLinks:
  alternates:
    - server-to-server-vault-tokenization.md
---

# Server to Server Vault tokenization

### Secure, Direct Card Tokenization from Your Server

Tokenize payment cards directly from your servers to Juspay Hyperswitch's Vault Service, bypassing client-side tokenization. This server-to-server approach provides enhanced security and flexibility, ideal for PCI-compliant businesses managing payment methods programmatically.

#### Key Features

* **Full Token Management** – Create, retrieve, update, and delete payment tokens directly from your server.
* **PSP and Network Tokenization** – Generate both PSP tokens and network tokens through a single API.
* **Secure Storage** – Store tokens safely in Hyperswitch's Vault.
* **Reduced Frontend Complexity** – Shift tokenization processes to the backend, minimizing frontend dependencies.

### Prerequisites

To implement server-to-server tokenization, you need:

* **PCI DSS compliance to handle card data securely:** Make sure you have necessary PCI compliance to handle raw card data directly
* **Secure API authentication to protect transactions:** Generate your Hyperswitch API key from Developers --> API Keys section on your Hyperswitch dashboard
* **Robust error handling for tokenization failures:** Implement necessary handling for failure cases

### How It Works

1. **Collect Card Details** – Your server collects card details (requires PCI compliance).
2. **Send a Tokenization Request** – Make a POST request to /payment\_methods with the card details.
3. **Token Creation & Validation** – Hyperswitch validates the request and generates a secure token in the vault.
4. **PSP & Network Tokenization (Optional)** – If configured through your Hyperswitch dashboard, we also generate PSP and/or network tokens when you pass relevant parameters as mentioned below
5. **Receive Payment Method ID** – You get a pm\_id, which can be used for future payments.

### API Requests for Server to Server Tokenization

{% hint style="info" %}
All Vault API (V2) requests require a **Vault API Key** and your **Profile ID**. See [Vault Configuration](configuration.md) for step-by-step instructions on generating these credentials from the Hyperswitch Control Centre.
{% endhint %}

#### 1. Create a Customer

* Endpoint: `POST /customers`
* Purpose: Create a customer to enable storing their payment methods

For detailed request parameters and examples, refer to the [Create Customer API Reference](https://api-reference.hyperswitch.io/v2/customers/customers--create-v1).

#### 2. Create a Payment Method Id

* Endpoint: `POST /payment_methods`
* Purpose: Generate a Id for a card

For detailed request parameters and examples, including how to create payment method tokens with PSP tokens or network tokens, refer to the [Create Payment Method API Reference](https://api-reference.hyperswitch.io/v2/payment-methods/payment-method--create-v1).

#### 3. Retrieve a Payment Method Id

* Endpoint: `POST /payment_methods/:pm_id`
* Purpose: Retrieve a Payment Method for a Id

For detailed request parameters and examples, including how to retrieve payment method id with network tokens, refer to the [Retrieve Payment Method API Reference](https://api-reference.hyperswitch.io/v2/payment-methods/payment-method--retrieve-v1).

#### 4. Update a Payment Method Id

* Endpoint: `PATCH /payment_methods/:pm_id/update_saved_payment_method`
* Purpose: Modify Payment Method details.

For detailed request parameters and examples, refer to the [Update Payment Method API Reference](https://api-reference.hyperswitch.io/v2/payment-methods/payment-method--update-v1).

#### 5. Delete a Payment Method Id

* Endpoint: `DELETE /payment_methods/:pm_id`
* Purpose: Remove a Id from the vault.

For detailed request parameters and examples, refer to the [Delete Payment Method API Reference](https://api-reference.hyperswitch.io/v2/payment-methods/payment-method--delete-v1).
