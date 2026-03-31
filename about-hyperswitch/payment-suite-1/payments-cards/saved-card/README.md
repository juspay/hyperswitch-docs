---
description: Implement secure saved card flows using the Hyperswitch SDK to vault card data and enable seamless checkout experiences for new and returning customers
icon: hard-drive
---

# Saved Card

In this approach, the Hyperswitch SDK is used on the frontend to capture card details. Card data is securely sent to the Hyperswitch backend and stored in Hyperswitch Vault. Payment orchestration, routing, and connector logic are handled entirely by the Hyperswitch backend.

The merchant uses the Hyperswitch Dashboard to configure connectors, routing rules, and orchestration logic. All payment requests are initiated using vault tokens, and raw card data never reaches merchant systems. Since card details are handled entirely by Hyperswitch, merchants are not required to be PCI DSS compliant for card data handling.&#x20;

#### **New User (Payments SDK)**

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
  participant MS as Merchant Server
  participant MC as Merchant Client
  participant HSDK as Hyperswitch SDK
  participant HS as Hyperswitch Server
  participant PS as Processor Server
  participant HV as Hyperswitch Vault

  MS->>HS: payments/create call with amount, currency, etc and api_key
  HS-->>MS: payments/create response with payment_id, client_secret, etc.
  MS->>MC: pass client_secret, publishable_key
  MC->>HSDK: initiate SDK with client_secret, publishable_key
  HSDK->>HS: /payment_methods_list call with client_secret
  HS-->>HSDK: /payment_methods_list response with eligible payment methods
  Note over HSDK: Display the payment sheet with relevant payment methods
  Note over HSDK: Customer selects their desired payment method (say card and enters their card details)
  HSDK->>HS: payments/confirm call with client_secret and payment_method_data containing card details, etc
  HS->>PS: payments/confirm call to processor with payment method details and merchant's processor credentials
  PS-->>HS: payments/confirm response with status
  HS->>HV: request to store the card
  HV-->>HS: response along with payment method id
  HS-->>HSDK: payments/confirm response with status
  HSDK->>MC: return to return_url with status
```

*Caption: The new user payment flow with card vaulting. The merchant creates a payment, the SDK collects card details, Hyperswitch authorizes the payment with the processor, and securely stores the card in the vault, returning a reusable payment method ID for future transactions.*



##### **1. Create Payment (Server-Side)**

The merchant server creates a payment by calling the Hyperswitch [`payments/create`](https://api-reference.hyperswitch.io/v1/payments/payments--create) API with transaction details such as amount and currency. Hyperswitch responds with a `payment_id`, `customer_id` and `client_secret`, which are required for client-side processing.

```json
curl --location 'https://sandbox.hyperswitch.io/payments' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'api-key: <enter your Hyperswitch API key here>' \
--data-raw '{
    "amount": 6540,
    "currency": "USD",
    "profile_id": <enter the relevant profile id>,
    "customer_id": "customer123",
    "description": "Its my first payment request",
    "return_url": "https://example.com", //
}'
```

{% hint style="info" %}
Note - In case the merchant does not pass the customer ID, then the transaction is treated as a Guest customer checkout &#x20;
{% endhint %}

##### **2. Initialize SDK (Client-Side)**

The merchant client initializes the Hyperswitch SDK using the `client_secret` and `publishable_key`. The SDK fetches eligible payment methods from Hyperswitch and renders a secure payment UI.

```js
// Fetches a payment intent and captures the client secret
async function initialize() {
  const response = await fetch("/create-payment", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({currency: "USD",amount: 100}),
  });
  const { clientSecret } = await response.json();

  // Initialise Hyperloader.js
  var script = document.createElement('script');
  script.type = 'text/javascript';
  script.src = "https://beta.hyperswitch.io/v1/HyperLoader.js";

  let hyper;
  script.onload = () => {
      hyper = window.Hyper("YOUR_PUBLISHABLE_KEY",{
      customBackendUrl: "YOUR_BACKEND_URL",
      //You can configure this as an endpoint for all the api calls such as session, payments, confirm call.
      })
      const appearance = {
          theme: "midnight",
      };
      const widgets = hyper.widgets({ appearance, clientSecret });
      const unifiedCheckoutOptions = {
          layout: "tabs",
          wallets: {
              walletReturnUrl: "https://example.com/complete",
              //Mandatory parameter for Wallet Flows such as Googlepay, Paypal and Applepay
          },
      };
      const unifiedCheckout = widgets.create("payment", unifiedCheckoutOptions);
      unifiedCheckout.mount("#unified-checkout");
  };
  document.body.appendChild(script);
}
```

##### **3. Collect Card Details**

The customer selects a card payment method and enters their card details directly within the SDK-managed interface, ensuring sensitive data never passes through merchant systems.

##### **4. Authorize and Store Card**

The SDK submits a [`payments/confirm`](https://api-reference.hyperswitch.io/v1/payments/payments--confirm) request to Hyperswitch. Hyperswitch authorizes the payment with the processor and securely stores the card in the Hyperswitch Vault, generating a reusable `payment_method_id`.

#### **5. Return Status**

The final payment and vaulting status is returned to the SDK, which redirects the customer to the merchant's configured `return_url`.

#### **Returning or Repeat User (Payments SDK)**

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
  participant MS as Merchant Server
  participant MC as Merchant Client
  participant HSDK as Hyperswitch SDK
  participant HS as Hyperswitch Server
  participant PS as Hyperswitch Connector
  participant HV as Hyperswitch Vault

  MS->>HS: payments/create call with amount, currency, etc and api_key
  HS-->>MS: payments/create response with payment_id, client_secret, etc.
  MS->>MC: pass client_secret, publishable_key
  MC->>HSDK: initiate SDK with client_secret, publishable_key
  HSDK->>HS: /payment_methods_list call with client_secret
  HS-->>HSDK: /payment_methods_list response with eligible payment methods
  Note over HSDK: Display the payment sheet with relevant payment methods
  Note over HSDK: Customer selects a saved card
  HSDK->>HS: payments/confirm call with client_secret and payment_method_data containing card details, etc
  HS->>HV: request along with payment method id
  HV-->>HS: response along with raw card data
  HS->>PS: payments/confirm call to processor with payment method details, merchant's processor credentials and raw card data
  PS-->>HS: payments/confirm response with status
  HS-->>HSDK: payments/confirm response with status
  HSDK->>MC: return to return_url with status
```

*Caption: The returning user payment flow with saved cards. The merchant creates a payment, the SDK fetches and displays saved payment methods, the customer selects a saved card, and Hyperswitch retrieves the vaulted card data to authorize the payment with the processor.*

#### **1. Create Payment (Server-Side)**

The merchant server initiates the payment by calling the [`payments/create`](https://api-reference.hyperswitch.io/v1/payments/payments--create) API with transaction details such as amount and currency. Hyperswitch responds with a `payment_id` , `customer_id` and `client_secret`, which are required for client-side processing.

```json
curl --location 'https://sandbox.hyperswitch.io/payments' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'api-key: <enter your Hyperswitch API key here>' \
--data-raw '{
    "amount": 6540,
    "currency": "USD",
    "profile_id": <enter the relevant profile id>,
    "customer_id": "customer123",
    "description": "Its my first payment request",
    "return_url": "https://example.com", //
}'
```

{% hint style="info" %}
Note - The merchant needs to pass the same customer ID for the SDK to fetch the saved customer payment methods and display them
\
In case the merchant is not using the SDK then they need to use the List Customer Saved Payment Methods API to fetch the stored payment methods against a customer&#x20;
{% endhint %}

##### **2. Initialize SDK and Fetch Saved Cards**

The merchant client initializes the Hyperswitch SDK. The SDK requests eligible payment methods from Hyperswitch, including any saved cards associated with the customer.

```js
// Fetches a payment intent and captures the client secret
async function initialize() {
  const response = await fetch("/create-payment", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({currency: "USD",amount: 100}),
  });
  const { clientSecret } = await response.json();

  // Initialise Hyperloader.js
  var script = document.createElement('script');
  script.type = 'text/javascript';
  script.src = "https://beta.hyperswitch.io/v1/HyperLoader.js";

  let hyper;
  script.onload = () => {
      hyper = window.Hyper("YOUR_PUBLISHABLE_KEY",{
      customBackendUrl: "YOUR_BACKEND_URL",
      //You can configure this as an endpoint for all the api calls such as session, payments, confirm call.
      })
      const appearance = {
          theme: "midnight",
      };
      const widgets = hyper.widgets({ appearance, clientSecret });
      const unifiedCheckoutOptions = {
          layout: "tabs",
          wallets: {
              walletReturnUrl: "https://example.com/complete",
              //Mandatory parameter for Wallet Flows such as Googlepay, Paypal and Applepay
          },
      };
      const unifiedCheckout = widgets.create("payment", unifiedCheckoutOptions);
      unifiedCheckout.mount("#unified-checkout");
  };
  document.body.appendChild(script);
}
```

##### **3. Customer Selects a Saved Card**

The SDK displays the saved cards in the payment UI, customer enters the CVV.

##### **4. Retrieve Card Data and Authorize**

The SDK sends a [`payments/confirm`](https://api-reference.hyperswitch.io/v1/payments/payments--confirm) request with the selected `payment_method_id`. Hyperswitch securely retrieves the card data from the Hyperswitch Vault and submits the authorization request to the processor via the Hyperswitch Connector.

##### **5. Return Status**

The processor returns the authorization result to Hyperswitch, which forwards the final status to the SDK. The customer is redirected to the merchant's `return_url` with the payment outcome.



#### Integration Guide :&#x20;

[Unified Checkout ](https://docs.hyperswitch.io/~/revisions/DXTxY8PvOykOfdbFcGmW/explore-hyperswitch/payment-experience/payment/web)

[Payments API](https://api-reference.hyperswitch.io/v1/payments/payments--create)
