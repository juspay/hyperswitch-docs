---
description: >-
  Integrate fraud and risk management providers with Juspay Hyperswitch to
  assess transaction risk before payment authorization.
icon: shield-halved
---

# Fraud Providers

Juspay Hyperswitch integrates with Fraud and Risk Management (FRM) providers as a distinct connector category — separate from payment processors. An FRM connector receives transaction signals from Hyperswitch, evaluates risk, and returns a recommendation (approve, review, or decline) that Hyperswitch acts on before or after authorization.

### How FRM connectors work in Hyperswitch

FRM connectors sit in the payment flow between order creation and authorization. Hyperswitch sends order and payment metadata to the FRM provider, which responds with a risk decision. Depending on the provider's decision and your configuration, Hyperswitch can:

- Proceed to authorization (approve)
- Flag the payment for manual review
- Block the authorization (decline)

FRM connectors are configured independently from payment processors — you can use any FRM provider with any payment processor combination.

### Supported Fraud Providers

| Provider | Type | Description |
| --- | --- | --- |
| **Signifyd** | FraudAndRiskManagementProvider | AI-driven commerce protection platform for maximizing conversions and eliminating fraud risk with guaranteed fraud liability coverage |
| **Riskified** | FraudAndRiskManagementProvider | Real-time decisions and machine learning-powered ecommerce fraud prevention with guaranteed chargeback protection |

### Activating a Fraud Provider

Fraud providers are activated through the same connector onboarding flow as payment processors.

[Steps to activate a connector on the Hyperswitch control center](../activate-connector-on-hyperswitch/README.md)
