---
description: Connect external vaults to store cards instead of the integrated vault that comes within your Juspay Hyperswitch Orchestration account
hidden: true
icon: plug
---

# Connect External Vaults to Juspay Hyperswitch Orchestration

### Modular Vaulting in Juspay Hyperswitch

Juspay Hyperswitch addresses the challenges with traditional vaults through Modular Vaulting: a flexible, merchant-centric approach to payment data infrastructure that emphasizes control, interoperability, and security.

Modular Vaulting is a key component of Juspay’s payment system, offering merchants the flexibility to either use Juspay Hyperswitch’s built-in PCI-compliant vault with advanced tokenization and security features or connect to any third party vault provider. This flexibility enables businesses to start simple and scale confidently without re-architecting their entire system.

<div align="center"><img src="../../../.gitbook/assets/0.png" alt=""></div>

### Modular Vaulting Options <a href="#h8bov2tye5ch" id="h8bov2tye5ch"></a>

Juspay Hyperswitch supports both an integrated vault as well as external vaults for merchants using Juspay Hyperswitch as their payments orchestration solution in both self-hosted and Juspay-hosted deployment modes.

<div align="center"><img src="../../../.gitbook/assets/1 (1).png" alt=""></div>

### Integrated Vault <a href="#isz5d0a9wa7s" id="isz5d0a9wa7s"></a>

Juspay Hyperswitch’s Payments Orchestration comes bundled with an integrated vault in both Merchant Self-Hosted as well as Juspay Hosted versions. In both cases, merchants don’t need to enable any additional configurations to use the Vault. It addresses PCI Compliance challenges, Integration Complexities and Data Migration Challenges

### External Vault <a href="#id-20wg2qacxxxe" id="id-20wg2qacxxxe"></a>

Juspay’s Modular Payments architecture enables merchants to connect to [external vault](https://juspay.io/integrations). This external vault could either be:

1. [Juspay Hosted Vault + SDK](../../../about-hyperswitch/payment-suite-1/payment-method-card/proxy.md) as a standalone solution
2. Third party vaults such as VGS, Tokenex, Voltage, Hashicorp, etc. in case of both SaaS and Self-deployed orchestration

#### Juspay Hosted Vault <a href="#c2bgyexb6gra" id="c2bgyexb6gra"></a>

Merchants can outsource their PCI compliance to Juspay by opting to use [Juspay’s Hosted Vault + SDK ](../../../about-hyperswitch/payment-suite-1/payment-method-card/proxy.md)as a standalone solution.

#### Third Party Vault <a href="#id-65rhdjnka52m" id="id-65rhdjnka52m"></a>

Through Juspay Hyperswitch, Merchants can add [external vault providers](https://juspay.io/integrations) such as VGS, HashiCorp, and Voltage, leveraging their SDKs to collect and tokenize cards. This ensures flexibility in vault selection while maintaining compliance, security, and seamless token management across multiple payment processors. Additionally, we also support other extended features vai an external vault such as:

* Network Tokenization - Merchants can configure Network Tokenization through either Juspay as TSP or use the External Vault as TSP, ensuring flexibility and control over token provisioning
* Proxy Payments through External Vaults - Support for processing payments through Proxy layers to ensure PCI compliance
* Card Forwarding & Receiving - To seamlessly transfer tokenized data across third-party endpoints, enabling effortless PSP migration

**SDK Options for Third Party Vault**

In case of using External vaults, merchants also have the option to choose which SDK to use to collect payment method details from their customers.

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

flowchart TD
    subgraph Option1["Option 1: Juspay Hyperswitch Unified Checkout SDK"]
        A1[Customer Browser/App] -- Card details entered --> B1[Juspay Hyperswitch Unified Checkout SDK]
        B1 -- Cards sent to --> C1[Juspay Hyperswitch Server]
        C1 -- Tokenize cards --> D1[External Vault]
        D1 -- Return vault token --> C1
        C1 -- Store token --> E1[(Juspay Hyperswitch Database)]

        F1[Payment Request] -- Retrieve vault token --> C1
        C1 -- Get raw card details using token --> D1
        D1 -- Return raw card details --> C1
        C1 -- Forward complete payment request --> G1[PSP]
    end

    subgraph Option2["Option 2: External Vault SDK"]
        A2[Customer Browser/App] -- Card details entered --> B2[External Vault SDK]
        B2 -- Capture & tokenize directly --> C2[External Vault]
        C2 -- Return vault token --> B2
        B2 -- Token passed to --> D2[Juspay Hyperswitch Server]
        D2 -- Store token --> E2[(Juspay Hyperswitch Database)]

        F2[Payment Request] -- Send vault token via proxy flow --> D2
        D2 -- Forward token to --> C2
        C2 -- De-tokenize & forward request --> G2[PSP]
    end

    classDef default  fill:#F7F7F7,stroke:#CCCCCC,color:#1A1A1A,rx:6
```

*Caption: This diagram illustrates the two flexible external vaulting options available in Juspay Hyperswitch. Option 1 uses the Juspay Hyperswitch Unified Checkout SDK where cards are collected by Juspay Hyperswitch and tokenized via the external vault, with the server retrieving raw card details for payment processing. Option 2 uses the External Vault SDK where cards are captured and tokenized directly in the external vault, bypassing Hyperswitch servers, and payments are processed through the vault's proxy flow.*

1. Juspay Hyperswitch Unified Checkout SDK - Cards are collected via the Juspay Hyperswitch Unified Checkout SDK and sent to the Hyperswitch server, which tokenizes them in an external vault. When processing payments, the Hyperswitch server retrieves the raw card details using the vault token and forwards the complete payment request to the PSP.
2. External Vault SDK - The External Vault SDK can be loaded on the Juspay Hyperswitch Unified Checkout SDK or independently. Cards are captured and tokenized directly in the external vault, bypassing  Hyperswitch server. For payments, the Hyperswitch server sends vault tokens via the vault’s proxy flow, and the external vault de-tokenizes and forwards the request to the PSP.
