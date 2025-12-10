---
description: Learn how to tokenize cards at Hyperswitch Vault Service using our Vault SDK
icon: desktop
---

# Vault SDK JS with REST API Integration

## Secure Tokenization using Hyperswitch's PCI Compliant Vault SDK

The Hyperswitch Vault SDK provides a secure solution for merchants to handle and store payment information without the burden of PCI DSS compliance requirements. By leveraging Hyperswitch's Vault service, merchants can securely store customer payment methods (credit cards, digital wallets, etc.) while minimizing their exposure to sensitive payment data.

## Key Benefits

* **Simplified PCI Compliance**: Reduce your PCI scope by outsourcing the storage of sensitive payment data to Hyperswitch's secure vault
* **Enhanced Customer Experience**: Allow customers to save and reuse payment methods for faster checkout experiences
* **Reduced Cart Abandonment**: Enable one-click payments for returning customers
* **Secure Token System**: Access saved payment methods via secure tokens without handling raw card data
* **Customizable UI**: Integrate a pre-built, customizable payment method management interface into your application

## Vault SDK Integration Walkthrough

This document provides step-by-step instructions for integrating the Hyperswitch Vault SDK into your application.

### 1. Server-Side Setup

First, you'll need to set up your server to create payment method sessions, which establish secure connections between your frontend and the Hyperswitch Vault.

#### Obtaining Your API Keys

Get your API key from the [Hyperswitch dashboard](https://app.hyperswitch.io/developers?tabIndex=1) under Developers -> API Keys section. You'll need both your API key and profile ID for server and client integration.

#### Creating a Payment Methods Session Endpoint

Add an endpoint on your server that creates payment methods sessions. This endpoint will return the necessary session information to your client application:

> Note: Please ensure that the **customer\_id** is included in the request body when creating a payment method session.\
> For more details, kindly refer to the [API](https://api-reference.hyperswitch.io/introduction) reference documentation.

```javascript
// Create-Payment-Methods-Session
const app = express()

app.post("/create-payment-method-session", async (req, res) => {
  try {
    // Create payment method session on Hyperswitch
    const response = await fetch(
      `${HYPERSWITCH_SERVER_URL}/v2/payment-method-sessions`,
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "x-profile-id": YOUR_PROFILE_ID,
          Authorization: `api-key=${YOUR_API_KEY}`,
        },
        body: JSON.stringify(req.body),
      }
    );
    const data = await response.json();

    if (!response.ok) {
      console.error("Hyperswitch API Error:", data);
      return res.status(response.status).json({
        error: data.error || "Failed to create payment method session",
      });
    }
    // Return Payment method session ID and client secret to the frontend
    res.json({
      id: data.id,
      clientSecret: data.client_secret,
    });
  } catch (error) {
    console.error("Server Error:", error);
    res.status(500).json({
      error: "Internal server error",
      message: error.message,
    });
  }
});
```

> **Note**: Replace `YOUR_PROFILE_ID` and `YOUR_API_KEY` with your actual credentials from the Hyperswitch dashboard.

### 2. Client-Side Integration

Once your server endpoint is set up, you'll need to integrate the Vault SDK into your client application.

#### 2.1 Define the Payment Methods Management Form

Add one empty placeholder `div` to your page for the Vault widget that you'll mount.

```html
<form id="vault-form">
  <div id="vault-elements">
    <!--HyperLoader injects the Vault SDK-->
  </div>
</form>
```

#### 2.2 Fetch the Payment Method Session and Mount the Vault Element

Make a request to the endpoint on your server to create a new payment method session. The `id` and `clientSecret` returned by your endpoint are used to initialize and display the customer's saved payment methods.\
\
Following this, create a `vaultElements` element and mount it to the placeholder `div` in your form. This embeds an iframe with a dynamic interface that displays saved payment methods, allowing your customer to view, manage, and delete their payment methods.

> Note: Make sure to never share your API key with your client application as this could potentially compromise your payment flow.

```javascript
// Fetches a payment method session and mounts the vault element
async function initialize() {
  // Step 1: Create payment method session
  const response = await fetch("/create-payment-method-session", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      customer_id: "CUSTOMER_ID",
    }),
  });
  const { id, clientSecret } = await response.json();

  // Step 2: Initialize HyperLoader.js
  var script = document.createElement("script");
  script.type = "text/javascript";
  script.src = "https://beta.hyperswitch.io/v2/HyperLoader.js";

  let hyper;
  script.onload = () => {
    // Step 3: Initialize Hyper with your publishable key and profile ID
    hyper = window.Hyper({
      publishableKey: "YOUR_PUBLISHABLE_KEY",
      profileId: "YOUR_PROFILE_ID",
    });

    // Step 4: Configure appearance
    const appearance = {
      theme: "default",
    };

    // Step 5: Create payment methods management elements
    const vaultSDK =
      hyper.vaultSDK({
        appearance,
        pmSessionId: id,
        pmClientSecret: clientSecret,
      });

    // Step 6: Create and mount the vault element
    const vaultElements = vaultSDK.create(
      "vaultElements"
    );
    vaultElements.mount("#vault-elements");
  };
  document.body.appendChild(script);
}

// Call initialize when page loads or when user clicks a button
initialize();
```

Congratulations! Now that you have integrated the Hyperswitch Payment Methods Management on your app, you can customize it to blend with the rest of your website.
