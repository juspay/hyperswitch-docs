---
description: >-
  Server to Server tokenization with Hyperswitch Vault Service for PCI compliant
  merchants
---

# Server to Server Vault tokenization

### Secure, Direct Card Tokenization from Your Server

Tokenize payment cards directly from your servers to Hyperswitch's Vault Service, bypassing client-side tokenization. This server-to-server approach provides enhanced security and flexibility, ideal for PCI-compliant businesses managing payment methods programmatically.

### Key Features

* **Full Token Management** – Create, retrieve, update, and delete payment tokens directly from your server.
* **PSP and Network Tokenization** – Generate both PSP tokens and network tokens through a single API.
* **Secure Storage** – Store tokens safely in Hyperswitch’s Vault.
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

#### 1. Create a Payment Method Token

* Endpoint: `POST /payment_methods`
* Purpose: Generate a token for a card

```bash
curl --location 'https://sandbox.hyperswitch.io/v2/payment-methods' \
--header 'Content-Type: application/json' \
--header 'api-key: <api-key>' \
--data '{
  "payment_method_type": "card",
  "payment_method_subtype": "credit",
  "metadata": {},
  "customer_id": "12345_cus_01926c58bc6e77c09e809964e72af8c8",
  "payment_method_data": {
"card": {
   "card_number": "4111111145551142",
   "card_exp_month": "10",
   "card_exp_year": "25",
   "card_holder_name": "John Doe",
   "nick_name": "John Doe",
   "card_issuing_country": "AF",
   "card_network": "Visa",
   "card_issuer": "<string>",
   "card_type": "credit",
   "card_cvc": "242"
}
  },
  "billing": {
"address": {
   "city": "New York",
   "country": "AF",
   "line1": "123, King Street",
   "line2": "Powelson Avenue",
   "line3": "Bridgewater",
   "zip": "08807",
   "state": "New York",
   "first_name": "John",
   "last_name": "Doe"
},
"phone": {
   "number": "9123456789",
   "country_code": "+1"
},
"email": "abc@gmail.com"
  }
}'
```

**a. Creating a Payment Method Token along with PSP Tokens**

Use the same endpoint to generate PSP tokens for a card by passing the following parameters:

```bash
curl --location 'https://sandbox.hyperswitch.io/v2/payment-methods' \
--header 'Content-Type: application/json' \
--header 'api-key: <api-key>' \
--data '{
  "payment_method_type": "card",
  "payment_method_subtype": "ach",
  "metadata": {},
  "customer_id": "12345_cus_01926c58bc6e77c09e809964e72af8c8",
  "payment_method_data": {
	"card": {
  	"card_number": "4111111145551142",
  	"card_exp_month": "10",
  	"card_exp_year": "25",
  	"card_holder_name": "John Doe",
  	"nick_name": "John Doe",
  	"card_issuing_country": "AF",
  	"card_network": "Visa",
  	"card_issuer": "<string>",
  	"card_type": "credit",
  	"card_cvc": "242"
	}
  },
  "billing": {
	"address": {
  	"city": "New York",
  	"country": "AF",
  	"line1": "123, King Street",
  	"line2": "Powelson Avenue",
  	"line3": "Bridgewater",
  	"zip": "08807",
  	"state": "New York",
  	"first_name": "John",
  	"last_name": "Doe"
	},
	"phone": {
  	"number": "9123456789",
  	"country_code": "+1"
	},
	"email": "abc@gmail.com"
  },
  "psp_tokenization": {
	"tokenization_type": "single_use",
	"connector_id": "<string>"
  }
}'
```

**b. Creating a Payment Method Token along with Network Tokens**

Use the same endpoint to generate network tokens for a card by passing the following parameters:

```bash
curl --location 'https://sandbox.hyperswitch.io/v2/payment-methods' \
--header 'Content-Type: application/json' \
--header 'api-key: <api-key>' \
--data '{
  "payment_method_type": "card",
  "payment_method_subtype": "ach",
  "metadata": {},
  "customer_id": "12345_cus_01926c58bc6e77c09e809964e72af8c8",
  "payment_method_data": {
	"card": {
  	"card_number": "4111111145551142",
  	"card_exp_month": "10",
  	"card_exp_year": "25",
  	"card_holder_name": "John Doe",
  	"nick_name": "John Doe",
  	"card_issuing_country": "AF",
  	"card_network": "Visa",
  	"card_issuer": "<string>",
  	"card_type": "credit",
  	"card_cvc": "242"
	}
  },
  "billing": {
	"address": {
  	"city": "New York",
  	"country": "AF",
  	"line1": "123, King Street",
  	"line2": "Powelson Avenue",
  	"line3": "Bridgewater",
  	"zip": "08807",
  	"state": "New York",
  	"first_name": "John",
  	"last_name": "Doe"
	},
	"phone": {
  	"number": "9123456789",
  	"country_code": "+1"
	},
	"email": "<string>"
  },
  "network_tokenization": {
	"enable": "Enable"
  }
}'
```

#### 2. Retrieve a Payment Method Token

* Endpoint: `GET /payment_methods/:pm_id`
* Purpose: Fetch details of an existing token.

```bash
curl --location --globoff 'https://sandbox.hyperswitch.io/v2/payment-methods/{id}' \
--header 'api-key: <api-key>'
```

#### 3. Update a Payment Method Token

* Endpoint: `PATCH /payment_methods/:pm_id/update_saved_payment_method`
* Purpose: Modify token details.

```bash
curl --location --globoff --request PATCH 'https://sandbox.hyperswitch.io/v2/payment-methods/{id}/update-saved-payment-method' \
--header 'Content-Type: application/json' \
--header 'api-key: <api-key>' \
--data '{
  "payment_method_data": {
	"card": {
  	"card_holder_name": "John Doe",
  	"nick_name": "John Doe"
	}
  },
  "connector_token_details": {
	"token": "pm_9UhMqBMEOooRIvJFFdeW",
	"connector_token_request_reference_id": "<string>"
  }
}'
```

#### 4. Delete a Payment Method Token

* Endpoint: `DELETE /payment_methods/:pm_id`
* Purpose: Remove a token from the vault.

```bash
curl --location --globoff --request DELETE 'https://sandbox.hyperswitch.io/v2/payment-methods/{id}' \
--header 'api-key: <api-key>'
```
