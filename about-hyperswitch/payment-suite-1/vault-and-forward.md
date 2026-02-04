---
description: >-
  Best for merchants who do not want to handle card data and want to maintain
  their current integration with the processors.
---

# Vault and Forward

In this approach, the Direct Payment Control Model functions by treating Hyperswitch as a secure "pipe." This setup grants you full control over your orchestration logic and the specific API calls sent to processors. The process initiates when the customer enters payment details into the Hyperswitch Vault SDK, where the data is directly tokenized within the Hyperswitch Vault.

For payments, your backend constructs a request intended for your specific processor, such as Stripe or Adyen, utilizing placeholders instead of raw card data. This request is then routed through the Hyperswitch Proxy. The proxy injects the actual card details immediately before forwarding the request to the processor, ensuring that raw card data never touches your servers.

This architecture allows you to maintain your legacy backend logic while significantly reducing PCI scope. It is particularly well-suited for scenarios where you plan to keep existing processor integrations. but require the removal of sensitive card data from your internal systems.

#### **Understanding Payment and Vault Flow**&#x20;

<figure><img src="../../.gitbook/assets/image (3) (4).png" alt=""><figcaption></figcaption></figure>



#### Vaulting&#x20;

**1. Create Payment Method Session (Server-Side)** The merchant server initiates the flow by calling the Hyperswitch [`Create-payment-method-session`](https://api-reference.hyperswitch.io/v2/payment-method-session/payment-method-session--create#payment-method-session-create) API with the `customer_id`. Hyperswitch responds with a `session_id` and `client_secret`, which are required to authenticate the client-side session.

**2. Initialize SDK (Client-Side)** The merchant client loads the `HyperLoader.js` script and initializes `window.Hyper` using the Publishable Key. Using the `session_id` and `client_secret`, the SDK creates a Payment Method Management (PMM) group and mounts the specific widget instance to the UI.

**3. Collect and Vault Card (Client-Side)** The customer enters their card details directly into the SDK-managed widget. Upon confirmation, the SDK calls the /`Confirm a payment method session` API. Hyperswitch securely receives the data, stores it in the Vault (retaining the CVV temporarily for the transaction TTL), and returns a success response with the `session_id` to the client.

**4. Retrieve Payment Method ID (Server-Side)** The merchant server calls the "List Payment Methods" API using the `session_id`. Hyperswitch returns a list of payment methods associated with the customer, from which the merchant server selects the appropriate `PM_ID` (Payment Method ID) to use for the transaction.



#### Payment

**Execute Proxy Payment (Server-Side)** The merchant server initiates the payment by sending a request to the [Hyperswitch vault proxy](https://docs.hyperswitch.io/~/revisions/01bZ2maqjwpnmrttix7i/explore-hyperswitch/payments-modules/vault/hyperswitch-vault-pass-through-proxy-payments) endpoint using the `payment_method_id` . The proxy securely replaces the token with the actual card data from the Vault and forwards the request to the Payment Service Provider (PSP), returning the final payment response to the merchant.



**Integration Documetation :**&#x20;

* [Vault SDK Integration](https://docs.hyperswitch.io/~/revisions/TGn71uwTlQJmyyiYgHpt/explore-hyperswitch/payments-modules/vault/vault-sdk-integration)
* [Proxy Payment Integration Guide](https://docs.hyperswitch.io/~/revisions/01bZ2maqjwpnmrttix7i/explore-hyperswitch/payments-modules/vault/hyperswitch-vault-pass-through-proxy-payments)
