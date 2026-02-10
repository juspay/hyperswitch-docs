---
description: Hyperswitch is designed to facilitate the management of saved payment methods
icon: bars-progress
---

# Payment Methods Management

The Hyperswitch Payment Methods Management SDK provides a secure solution for merchants to handle and store payment information without the burden of PCI DSS compliance requirements. By leveraging Hyperswitch's Vault service, merchants can securely store customer payment methods (credit cards, digital wallets, etc.) while minimizing their exposure to sensitive payment data.

## **Key Features of Payment Method Management in Hyperswitch**

Hyperswitch simplifies the complexities of payment method management, so you can offer a seamless, secure experience to your customers with minimal effort.

1. **Payment Method Creation**: Easily allow your customers to save new payment methods during checkout, providing a convenient option for future transactions.
2. **Storing Payment Methods**: Hyperswitch securely stores customer payment details, enabling repeat purchases without requiring them to re-enter their information each time.
3. **Retrieving Payment Methods**: Customers can quickly access their saved payment methods, streamlining their checkout process and enhancing their overall experience.
4. **Deleting/Deactivating Payment Methods**: Keep payment options up to date by allowing customers to manage outdated or inactive methods, ensuring a clean and efficient payment experience.

<figure><img src="../../../.gitbook/assets/Screenshot 2024-10-03 at 12.27.38 PM.png" alt="" width="563"><figcaption><p>image displaying the payment method management UI.</p></figcaption></figure>

#### 1. Server-Side Setup <a href="#id-1.-server-side-setup" id="id-1.-server-side-setup"></a>

First, you'll need to set up your server to create payment method sessions, which establish secure connections between your frontend and the Hyperswitch Vault.

**Obtaining Your API Keys**

Get your API key from the [Hyperswitch dashboard](https://app.hyperswitch.io/developers?tabIndex=1) under Developers -> API Keys section. You'll need both your API key and profile ID for server and client integration.

All Vault API (V2) requests require authentication using specific API keys generated from your Vault Merchant account. These keys are distinct from your standard payment processing keys.

To generate your Vault API keys, follow these steps:

1. **Access Dashboard:** Log into the Hyperswitch Dashboard.
2. **Navigate to Vault:** In the left-hand navigation menu, select Vault.
3. **Generate Key:** Navigate to the API Keys section and click the Create New API Key button.
4. **Secure Storage:** Copy the generated key and store it securely. You must use this key to authenticate all Vault API (V2) calls.

**Note:** We are currently working on unifying authentication across our platforms. Soon, you will be able to use a single API key for both Payments and Vault APIs.

**Creating a Payment Methods Session Endpoint**

Add an endpoint on your server that creates payment methods sessions. This endpoint will return the necessary session information to your client application.

```
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

#### 2. Client-Side Integration <a href="#id-2.-client-side-integration" id="id-2.-client-side-integration"></a>

Once your server endpoint is set up, you'll need to integrate the Vault/Payment Methods Management SDK into your client application.

**2.1 Define the Payment Methods Management Form**

Add one empty placeholder `div` to your page for the Payment Methods Management widget that you'll mount.

```
<form id="payment-methods-management-form">
  <div id="payment-methods-management-elements">
    <!--HyperLoader injects the Payment Methods Management SDK-->
  </div>
</form>
```

**2.2 Fetch the Payment Method Session and Mount the Payment Methods Management Element**

Make a request to the endpoint on your server to create a new payment method session. The `id` and `clientSecret` returned by your endpoint are used to initialize and display the customer's saved payment methods. Following this, create a `paymentMethodsManagementElements` element and mount it to the placeholder `div` in your form. This embeds an iframe with a dynamic interface that displays saved payment methods, allowing your customer to view, manage, and delete their payment methods.

> Note: Make sure to never share your API key with your client application as this could potentially compromise your payment flow.

```
// Fetches a payment method session and mounts the payment methods management element
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
    const paymentMethodsManagementElements =
      hyper.paymentMethodsManagementElements({
        appearance,
        pmSessionId: id,
        pmClientSecret: clientSecret,
      });

    // Step 6: Create and mount the paymentMethodsManagement element
    const paymentMethodsManagement = paymentMethodsManagementElements.create(
      "paymentMethodsManagement"
    );
    paymentMethodsManagement.mount("#payment-methods-management-elements");
  };
  document.body.appendChild(script);
}

// Call initialize when page loads or when user clicks a button
initialize();
```

**2.3 Complete tokenization and handle errors**

Call `confirmTokenization()`, passing the mounted Payment Methods Management widgets and a `return_url` to indicate where Hyper should redirect the user after any required authentication. Depending on the payment method, Hyper may redirect the customer to an authentication page. After authentication is completed, the customer is redirected back to the `return_url`.

If there are any immediate errors (for example, invalid request parameters), Hyper returns an error object. Show this error message to your customer so they can try again.

```
async function handleSubmit(e) {
  setMessage("");
  e.preventDefault();

  // Ensure Hyper is initialized
  if (!hyper || !paymentMethodsManagementElements) {
    return;
  }

  setIsLoading(true);

  try {
    const response = await hyper.confirmTokenization({
      paymentMethodsManagementElements,
      confirmParams: {
        // URL to redirect the user after authentication (if required)
        return_url: "https://example.com/complete",
      },
      redirect: "always", // if you wish to redirect always, otherwise it is defaulted to "if_required"
    });

    // Tokenization succeeded
    if (response?.id) {
      // You can use the returned payment method/session token here
      handleTokenRetrieval(response);
    } else {
      // Handle immediate errors returned by Hyper
      const error = response?.error;

      if (error) {
        if (error.type === "card_error" || error.type === "validation_error") {
          setMessage(error.message);
        } else {
          if (error.message) {
            setMessage(error.message);
          } else {
            setMessage("An unexpected error occurred.");
          }
        }
      } else {
        setMessage("An unexpected error occurred.");
      }
    }
  } catch (err) {
    setMessage(err.message || "An unexpected error occurred.");
  } finally {
    setIsLoading(false);
  }
}
```

Now that you have integrated the Hyperswitch Payment Methods Management on your app, you can customize it to blend with the rest of your website.

\
<br>
