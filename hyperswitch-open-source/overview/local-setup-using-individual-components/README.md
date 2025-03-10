---
icon: diamonds-4
---

# Local Setup using Individual Components

## Hyperswitch Components&#x20;

Hyperswitch has three components, and all three components have a very detailed setup considering various use cases, listed in their individual repositories-&#x20;

* [**Hyperswitch Backend**](https://github.com/juspay/hyperswitch): Hyperswitch backend enables seamless payment processing with comprehensive support for various payment flows - authorization, authentication, void and capture workflows along with robust management of post-payment processes like refunds and chargeback handling. Additionally, Hyperswitch supports non-payment use cases by enabling connections with external FRM or authentication providers as part of the payment flow. The backend optimizes payment routing with customizable workflows, including success rate-based routing, rule-based routing, volume distribution, fallback handling, and intelligent retry mechanisms for failed payments based on specific error codes.
* [**SDK (Frontend)**](https://github.com/juspay/hyperswitch-web): The SDK, available for web, [Android, and iOS](https://github.com/juspay/hyperswitch-client-core), unifies the payment experience across various methods such as cards, wallets, BNPL, bank transfers, and more, while supporting the diverse payment flows of underlying PSPs. When paired with the locker, it surfaces the user's saved payment methods.
* [**Control Center**](https://github.com/juspay/hyperswitch-control-center): The Control Center enables users to manage the entire payments stack without any coding. It allows the creation of workflows for routing, payment retries, and defining conditions to invoke 3DS, fraud risk management (FRM), and surcharge modules. The Control Center provides access to transaction, refund, and chargeback operations across all integrated PSPs, transaction-level logs for initial debugging, and detailed analytics and insights into payment performance.

### Setup Guides

<table data-view="cards"><thead><tr><th></th><th data-hidden></th><th data-hidden></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><mark style="color:blue;"><strong>Hyperswitch Backend</strong></mark></td><td></td><td></td><td><a href="set-up-hyperswitch-backend.md">set-up-hyperswitch-backend.md</a></td></tr><tr><td><mark style="color:blue;"><strong>SDK (Frontend)</strong></mark></td><td></td><td></td><td><a href="set-up-hyperswitch-sdk-frontend.md">set-up-hyperswitch-sdk-frontend.md</a></td></tr><tr><td><mark style="color:blue;"><strong>Control Center</strong></mark></td><td></td><td></td><td><a href="set-up-hyperswitch-control-center.md">set-up-hyperswitch-control-center.md</a></td></tr></tbody></table>

