# Payment with Vault Flow

In the Payment with Vault flow setup, Hyperswitch acts as the central intelligence layer. You interact with a single unified API, and Hyperswitch manages the entire payment lifecycle across multiple processors.

#### How it Works

1. **Unified Request:** Your backend sends a generic payment request to the Hyperswitch API.
2. **Smart Routing:** The Hyperswitch Orchestrator evaluates your configured business rules (e.g., routing by volume, cost, or region).
3. **Execution:** Hyperswitch transforms the request into the specific format required by the target Connector (Stripe, Adyen, Braintree, etc.).
4. **State Management:** Hyperswitch maintains the payment state machine, handling webhooks, retries, and status updates automatically.

#### Technical Advantages

* **Abstracted Complexity:** You do not need to write or maintain processor-specific code.
* **Dynamic Routing:** Switch traffic between processors in real-time via the Hyperswitch dashboard or during payment initiation API calls.
* **Unified Reporting:** Transaction data across all processors is normalized into a single schema.
* Every transaction is processed via a PSP and based on the API calls you can have -  zero dollar validation, multi-stage manual capture, or sophisticated recurring logic payment flows.

#### Choose the Right Setup

Depending on your UI strategy and data sovereignty requirements, the Payment with Vault Flow offers multiple implementation patterns. Each option is designed to help you balance user experience, engineering complexity, and PCI compliance scope in a way that best fits your business.

The four primary patterns are:

* [**Hyperswitch SDK + Hyperswitch Vault** ](https://docs.hyperswitch.io/~/revisions/gkH4cp2rB1DvMiW6aktj/about-hyperswitch/payment-suite-1/orchestrator-model/hyperswitch-sdk-+-hyperswitch-vault-setup)— _Unified Flow_:\
  The quickest path to launch, offering a fully integrated experience with zero PCI scope.
* [**Merchant SDK + Hyperswitch Vault**](https://docs.hyperswitch.io/~/revisions/Rp0vynFYJnlasuYRM3en/about-hyperswitch/payment-suite-1/orchestrator-model/merchant-sdk-+-hyperswitch-vault-setup) — _Headless Flow_:\
  Enables a fully custom UI while retaining secure vaulting, giving you greater control with added implementation effort.
* [**Hyperswitch SDK + External Vault**](https://docs.hyperswitch.io/~/revisions/Rp0vynFYJnlasuYRM3en/about-hyperswitch/payment-suite-1/orchestrator-model/hyperswitch-sdk-+-external-vault-setup) — _Hybrid Flow_:\
  Combines Hyperswitch-managed UI with third-party data storage for teams with specific vaulting requirements.
* [**External SDK + External Vault**](https://docs.hyperswitch.io/~/revisions/Rp0vynFYJnlasuYRM3en/about-hyperswitch/payment-suite-1/orchestrator-model/external-sdk-and-external-vault-setup) — _External Vault Flow_:\
  Provides maximum decoupling and flexibility, ideal for advanced setups that demand full control across the stack.
