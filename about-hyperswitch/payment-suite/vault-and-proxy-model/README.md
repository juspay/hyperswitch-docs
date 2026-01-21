# Vault & Proxy Model

The Vault & Proxy model treats Hyperswitch as a secure "pipe." You maintain full control over the orchestration logic and the specific API calls sent to processors.

#### How it Works

1. **Tokenization (Vault):** Sensitive payment data is sent directly from the client to the Hyperswitch Vault. You receive a non-sensitive token in return.
2. **Custom Orchestration:** Your backend decides exactly when and where to process the payment.
3. **Secure Passthrough (Proxy):** When you are ready to charge, you send the request to the Hyperswitch Proxy API, targeting the processor's native endpoint.
4. **Redaction & Injection:** The Proxy identifies the token in your payload, injects the real card data from the Vault, and forwards the full request to the processor.



This model is ideal if you are planning to keep existing processor integrations (e.g., direct calls to Checkout.com or legacy gateways) but need to remove raw card data from your systems to reduce PCI scope.

### Integration Flavors

Below are the common combinations using this model :

1. [**Using Hyperswitch SDK and Hyperswitch Vault**](https://docs.hyperswitch.io/~/revisions/wda8x2AP0s0eeYYw2jGt/about-hyperswitch/payment-suite/using-hyperswitch-sdk-and-vault-hs-as-external-vault-solution)
2. [**Using Merchant SDK and Hyperswitch Vault**](https://docs.hyperswitch.io/~/revisions/MdbUFT5VyrEZi4hV6Si5/about-hyperswitch/payment-suite/using-merchant-sdk-and-vault-hs-as-external-vault-solution)
