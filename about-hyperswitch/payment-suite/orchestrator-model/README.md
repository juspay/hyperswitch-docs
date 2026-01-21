# Orchestrator Model

In the Orchestrator Model, Hyperswitch acts as the central intelligence layer. You interact with a single unified API, and Hyperswitch manages the entire payment lifecycle across multiple processors.

#### How it Works

1. **Unified Request:** Your backend sends a generic payment request to the Hyperswitch API.
2. **Smart Routing:** The Hyperswitch Orchestrator evaluates your configured business rules (e.g., routing by volume, cost, or region).
3. **Execution:** Hyperswitch transforms the request into the specific format required by the target Connector (Stripe, Adyen, Braintree, etc.).
4. **State Management:** Hyperswitch maintains the payment state machine, handling webhooks, retries, and status updates automatically.

#### Technical Advantages

* **Abstracted Complexity:** You do not need to write or maintain processor-specific code.
* **Dynamic Routing:** Switch traffic between processors in real-time via the Hyperswitch dashboard or during payment initiation API calls.
* **Unified Reporting:** Transaction data across all processors is normalized into a single schema.

### Integration Flavors

Depending on your UI requirements and where you choose to store sensitive card data, the Orchestrator Model supports four distinct implementation combination :



1. [**Using Hyperswitch SDK and Hyperswitch Vault**](https://docs.hyperswitch.io/~/revisions/Fopdcyyzdnm7k9t2ns1Z/about-hyperswitch/payment-suite/using-hyperswitch-sdk-with-hyperswitch-vault) **:** The standard Unified flow (Fastest, No PCI Scope).
2. [**Using Merchant SDK and Hyperswitch Vault**](https://docs.hyperswitch.io/~/revisions/Fopdcyyzdnm7k9t2ns1Z/about-hyperswitch/payment-suite/using-merchant-sdk-with-hyperswitch-vault) **:** The Headless flow (Custom UI, higher control).
3. [**Using Hyperswitch SDK and External Vault** ](https://docs.hyperswitch.io/~/revisions/Fopdcyyzdnm7k9t2ns1Z/about-hyperswitch/payment-suite/using-hyperswitch-sdk-with-external-vault)**:** The Hybrid flow (Hyperswitch UI, 3rd-party storage).
4. [**Using External SDK and External Vault**](https://docs.hyperswitch.io/~/revisions/oTBffJ434XZteBygVlO3/about-hyperswitch/payment-suite/using-external-sdk-and-vault) **:** The External Vault flow (Max decoupling).
