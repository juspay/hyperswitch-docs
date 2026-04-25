---
description: >-
  Automate sales tax calculation on transactions through tax providers
  integrated with Juspay Hyperswitch.
icon: receipt
---

# Tax Providers

Juspay Hyperswitch integrates with tax calculation providers as a distinct connector category — classified as `TaxCalculationProvider`. Tax providers compute the applicable sales tax for a transaction based on the order details, customer location, and product type, and return the tax amount to be included in the payment.

### How tax calculation works in Hyperswitch

When a tax provider is configured, Hyperswitch calls the tax provider during the payment flow with order and address details. The provider returns the calculated tax amount, which Hyperswitch includes in the transaction before authorization.

### Supported Tax Providers

| Provider | Type | Description |
| --- | --- | --- |
| **TaxJar** | TaxCalculationProvider | Cloud-based platform that automates sales tax calculations, reporting, and filing for businesses across multiple channels |

### Activating a Tax Provider

Tax providers are activated through the same connector onboarding flow as payment processors.

[Steps to activate a connector on the Hyperswitch control center](../activate-connector-on-hyperswitch/README.md)
