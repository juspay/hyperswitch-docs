---
description: >-
  Learn how to tokenize cards at Hyperswitch Vault Service using our Payment
  Methods Management SDK
hidden: true
icon: gear
coverY: 0
---

# Payment Methods Management SDK

## Secure Tokenization using Hyperswitch's PCI Compliant Payment Methods Management SDK

The Hyperswitch Payment Methods Management SDK provides a secure solution for merchants to handle and store payment information without the burden of PCI DSS compliance requirements. By leveraging Hyperswitch's Vault service, merchants can securely store customer payment methods (credit cards, digital wallets, etc.) while minimizing their exposure to sensitive payment data.

## Key Benefits

* **Simplified PCI Compliance**: Reduce your PCI scope by outsourcing the storage of sensitive payment data to Hyperswitch's secure vault
* **Enhanced Customer Experience**: Allow customers to save and reuse payment methods for faster checkout experiences
* **Reduced Cart Abandonment**: Enable one-click payments for returning customers
* **Secure Token System**: Access saved payment methods via secure tokens without handling raw card data
* **Customizable UI**: Integrate a pre-built, customizable payment method management interface into your application

## Payment Methods Management SDK Integration Walkthrough

This document provides step-by-step instructions for integrating the Hyperswitch Payment Methods Management SDK into your application.

### 1. Server-Side Setup

First, you'll need to set up your server to create payment method sessions, which establish secure connections between your frontend and the Hyperswitch Vault.

#### Obtaining Your API Keys

Get your API key from the [Hyperswitch dashboard](https://app.hyperswitch.io/developers?tabIndex=1) under Developers -> API Keys section. You'll need both your API key and profile ID for server and client integration.

#### Creating a Payment Methods Session Endpoint

{% hint style="info" %}
All Vault API (V2) requests require authentication using specific API keys generated from your Vault Merchant account. These keys are distinct from your standard payment processing keys.

To generate your Vault API keys, follow these steps:

1. **Access Dashboard:** Log into the Hyperswitch Dashboard.
2. **Navigate to Vault:** In the left-hand navigation menu, select Vault.
3. **Generate Key:** Navigate to the API Keys section and click the Create New API Key button.
4. **Secure Storage:** Copy the generated key and store it securely. You must use this key to authenticate all Vault API (V2) calls.

**Note:** We are currently working on unifying authentication across our platforms. Soon, you will be able to use a single API key for both Payments and Vault APIs.
{% endhint %}

Add an endpoint on your server that creates payment methods sessions. This endpoint will return the necessary session information to your client application:

> Note: Please ensure that the **customer\_id** is included in the request body when creating a payment method session.\
> For more details, kindly refer to the [API](https://api-reference.hyperswitch.io/v2/payment-method-session/payment-method-session--create) reference documentation.

```javascript
// Create-Payment-Methods-Session
const app = express();

app.post(`/create-payment-methods-session`, async (req, res) => {
  try {
    const response = await fetch(
      `https://sandbox.hyperswitch.io/v2/payment-methods-session`,
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "x-profile-id": "YOUR_PROFILE_ID",
          Authorization: "api-key=YOUR_API_KEY",
        },
        body: JSON.stringify(req.body),
      }
    );
    
    const data = await response.json();
    
    res.send({
      pmSessionId: data.id,
      pmClientSecret: data.client_secret,
    });
  } catch (err) {
    return res.status(400).send({
      error: {
        message: err.message,
      },
    });
  }
});
```

> **Note**: Replace `YOUR_PROFILE_ID` and `YOUR_API_KEY` with your actual credentials from the Hyperswitch dashboard.

### 2. Client-Side Integration (React)

Once your server endpoint is set up, you'll need to integrate the Payment Methods Management SDK into your client application. The following steps outline the process for a React application.

#### 2.1 Install Required Libraries

Install the Hyperswitch JavaScript and React libraries:

```bash
$ npm install @juspay-tech/hyper-js
$ npm install @juspay-tech/react-hyper-js
```

#### 2.2 Add Hyperswitch to Your React App

Import the necessary components and hooks:

```javascript
import React, { useState, useEffect } from "react";
import { loadHyper } from "@juspay-tech/hyper-js";
import { HyperManagementElements } from "@juspay-tech/react-hyper-js";
```

#### 2.3 Initialize the Hyperswitch Library

Configure the library with your publishable API key and profile ID:

```javascript
const hyperPromise = loadHyper({
  publishableKey: "YOUR_PUBLISHABLE_KEY",
  profileId: "YOUR_PROFILE_ID",
});
```

> **Security Note**: Your publishable key is safe to expose in client-side code, but never include your secret API key in the frontend.

#### 2.4 Fetch Session Details

Make a request to your server endpoint to create a new payment methods session:

```javascript
const [pmClientSecret, setPmClientSecret] = useState(null);
const [pmSessionId, setPmSessionId] = useState(null);

useEffect(() => {
  fetch("/create-payment-methods-session", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({customer_id: "customer_id"}),
  })
  .then((res) => res.json())
  .then((data) => {
    setPmClientSecret(data.pmClientSecret);
    setPmSessionId(data.pmSessionId);
  });
}, []);
```

> **Important**: Replace `"customer_id"` with your actual customer identifier to associate saved payment methods with specific customers.

#### 2.5 Initialize the HyperManagementElements Component

Pass the promise from `loadHyper` to the `HyperManagementElements` component along with the session details:

```javascript
const options = {
  pmSessionId: pmSessionId,
  pmClientSecret: pmClientSecret,
};

return (
  <div className="App">
    {pmSessionId && pmClientSecret && (
      <HyperManagementElements options={options} hyper={hyperPromise}>
        <PaymentMethodsManagementElementForm />
      </HyperManagementElements>
    )}
  </div>
);
```

#### 2.6 Add the Payment Methods Management Elements

Create a `PaymentMethodsManagementElementForm` component that includes the `PaymentMethodsManagementElement`:

```javascript
import { PaymentMethodsManagementElement } from "@juspay-tech/react-hyper-js";

const PaymentMethodsManagementElementForm = () => {
  return (
    <div>
      <h2>Your Saved Payment Methods</h2>
      <PaymentMethodsManagementElement id="payment-methods-management-element" />
    </div>
  );
};
```

The `PaymentMethodsManagementElement` embeds an iframe with a dynamic form that displays saved payment methods, allowing your customers to view, manage, and save new payment methods securely.
