---
icon: diamonds-4
---

# Development Environment Setup

{% hint style="warning" %}
These setup guides are meant for development. If you want a quick trial of Hyperswitch (without contributing), use [this guide](https://docs.hyperswitch.io/hyperswitch-open-source/overview/unified-local-setup-using-docker).
{% endhint %}

### Setup Guides

<table data-view="cards"><thead><tr><th></th><th data-hidden></th><th data-hidden></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><mark style="color:blue;"><strong>Hyperswitch Backend</strong></mark></td><td></td><td></td><td><a href="set-up-hyperswitch-backend.md">set-up-hyperswitch-backend.md</a></td></tr><tr><td><mark style="color:blue;"><strong>SDK (Frontend)</strong></mark></td><td></td><td></td><td><a href="set-up-hyperswitch-sdk-frontend.md">set-up-hyperswitch-sdk-frontend.md</a></td></tr><tr><td><mark style="color:blue;"><strong>Control Center</strong></mark></td><td></td><td></td><td><a href="set-up-hyperswitch-control-center.md">set-up-hyperswitch-control-center.md</a></td></tr></tbody></table>

### **Hyperswitch Components**

Hyperswitch is built as a modular system, comprising three key components. Each component is designed for specific roles in the payment stack and has detailed development environment setup guides, linked above and also available in their individual repositories.

### [**Hyperswitch App Server**](https://github.com/juspay/hyperswitch):&#x20;

The Hyperswitch App Server is the core engine for processing payments. It offers full support for various payment flows, including:

* **Core Operations**: Authorization, authentication, voids, captures, refunds, and chargeback handling.
* **Post-Payment Management**: Robust handling of disputes and reconciliations.
* **Routing Flexibility**:
  * Success-rate-based routing
  * Rule-based routing
  * Volume distribution
  * Fallback strategies
  * Intelligent retries using error-code-specific flows
* **Extensibility**: Connects with external fraud risk management (FRM) tools and authentication providers as part of the payment journey.

### [**SDK (Frontend)**](https://github.com/juspay/hyperswitch-web)**:**&#x20;

The Hyperswitch SDK delivers a seamless and unified checkout experience across platforms:

* **Platform Support**: Available for [Web](https://docs.hyperswitch.io/explore-hyperswitch/merchant-controls/integration-guide/web), [Android, and iOS](https://github.com/juspay/hyperswitch-client-core),.
* **Multi-Method Support**: Handles cards, wallets, BNPL, bank transfers, and more.
* **Flow Adaptability**: Supports the nuances of different PSPs’ payment flows.
* **Saved Payment Methods**: When integrated with the locker, the SDK automatically displays stored cards or other saved instruments for returning users.

### [**Control Center**](https://github.com/juspay/hyperswitch-control-center):&#x20;

The Control Center is a no-code interface to manage and monitor your entire payment stack:

* **Workflow Management**: Configure smart routing, retries, 3DS invocation, fraud checks, and surcharge logic through a visual interface.
* **Operational Controls**:
  * Trigger and track refunds and chargebacks
  * View PSP-agnostic transaction logs for quick debugging
* **Insights and Analytics**: Access detailed reports and metrics on success rates, payment drop-offs, retry performance, and more.

