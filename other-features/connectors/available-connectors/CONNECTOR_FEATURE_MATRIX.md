# Connector Feature Matrix

This document provides a comprehensive overview of all supported payment connectors in Hyperswitch, their capabilities, and geographic availability.

## Overview

Hyperswitch supports **34+ payment connectors** spanning global acquirers, regional payment service providers (PSPs), wallets, and alternative payment methods (APMs).

## Connector Categories

| Category | Count | Description |
|----------|-------|-------------|
| Global Acquirers | 12 | International payment processors (Stripe, Adyen, etc.) |
| Regional PSPs | 14 | Region-specific providers (Trustpay, Volt, etc.) |
| Wallets & APMs | 8 | Digital wallets and alternative methods (PayPal, Klarna, etc.) |

## Quick Reference Matrix

| Connector | Payment Methods | 3DS Support | Refunds | Webhooks | Payouts | Regions |
|-----------|----------------|-------------|---------|----------|---------|---------|
| **Stripe** | Cards, Wallets, Bank Transfer, Buy Now Pay Later | Full | ✓ | ✓ | ✓ | Global |
| **Adyen** | Cards, Wallets, Bank Transfer, Buy Now Pay Later | Full | ✓ | ✓ | ✓ | Global |
| **Checkout.com** | Cards, Wallets | Full | ✓ | ✓ | ✓ | Global |
| **Braintree** | Cards, PayPal, Venmo | Full | ✓ | ✓ | ✗ | US, EU |
| **Cybersource** | Cards, Apple Pay, Google Pay | Full | ✓ | ✓ | ✓ | Global |
| **Authorize.Net** | Cards | Basic | ✓ | ✓ | ✗ | US, CA |
| **PayPal** | PayPal Balance, Cards, Pay Later | Partial | ✓ | ✓ | ✓ | Global |
| **Klarna** | Pay in 4, Pay Later, Pay Now | N/A | ✓ | ✓ | ✗ | EU, UK, US |
| **Airwallex** | Cards, Wallets, Local Methods | Full | ✓ | ✓ | ✓ | APAC, EU, US |
| **Rapyd** | Cards, Wallets, Bank Transfer | Partial | ✓ | ✓ | ✓ | Global |

## Detailed Connector Documentation

### Global Acquirers

#### Stripe
- **Website**: [stripe.com](https://stripe.com)
- **Supported Methods**: Credit/Debit Cards, Apple Pay, Google Pay, Link, Bank Transfers, ACH, SEPA, Buy Now Pay Later (Klarna, Affirm)
- **Key Features**: 
  - Full 3D Secure support
  - Automatic webhook forwarding
  - Real-time dispute handling
  - Multi-currency support (135+ currencies)
- **Geographic Coverage**: Global (46+ countries)
- **Integration Complexity**: ⭐⭐⭐☆☆ (Easy)
- **Documentation**: [stripe.md](./stripe.md)

#### Adyen
- **Website**: [adyen.com](https://adyen.com)
- **Supported Methods**: Cards, Apple Pay, Google Pay, PayPal, iDEAL, Sofort, Klarna, 100+ local methods
- **Key Features**:
  - Native 3DS authentication
  - RevenueProtect (fraud prevention)
  - Unified commerce support
  - Local acquiring in 30+ countries
- **Geographic Coverage**: Global (Europe, Americas, APAC)
- **Integration Complexity**: ⭐⭐⭐⭐☆ (Medium)
- **Documentation**: [adyen.md](./adyen.md)

#### Checkout.com
- **Website**: [checkout.com](https://checkout.com)
- **Supported Methods**: Cards, Wallets, Bank Debits, Alternative Payments
- **Key Features**:
  - Intelligent Acceptance optimization
  - Risk management tools
  - Webhook signature verification
- **Geographic Coverage**: Global (50+ countries)
- **Integration Complexity**: ⭐⭐⭐☆☆ (Easy)
- **Documentation**: [checkout.md](./checkout.md)

### Regional PSPs

#### Trustpay (Europe)
- **Website**: [trustpay.eu](https://trustpay.eu)
- **Supported Methods**: Cards, Bank Transfers, Local Methods
- **Regions**: EU, UK, Switzerland
- **Integration Complexity**: ⭐⭐⭐⭐☆ (Medium)

#### Volt (Open Banking)
- **Website**: [volt.io](https://volt.io)
- **Supported Methods**: Bank Transfers (Open Banking)
- **Regions**: UK, EU
- **Integration Complexity**: ⭐⭐☆☆☆ (Very Easy)

#### Nuvei
- **Website**: [nuvei.com](https://nuvei.com)
- **Supported Methods**: Cards, APMs
- **Regions**: North America, Europe, LATAM
- **Integration Complexity**: ⭐⭐⭐⭐☆ (Medium)

### Digital Wallets & APMs

#### PayPal
- **Website**: [paypal.com](https://paypal.com)
- **Methods**: PayPal balance, cards, Pay Later
- **Features**: Express checkout, buyer protection
- **Coverage**: 200+ markets

#### Klarna
- **Website**: [klarna.com](https://klarna.com)
- **Methods**: Pay in 4, Pay in 30 days, Financing
- **Regions**: Europe, UK, US, Australia
- **Best For**: E-commerce BNPL

## Feature Definitions

### 3DS Support Levels
- **Full**: Native + external 3DS, frictionless flow, challenge handling
- **Partial**: External 3DS only
- **Basic**: Challenge flow only
- **N/A**: Not applicable (wallet redirects)

### Payment Methods Legend
- **Cards**: Credit/Debit cards (Visa, Mastercard, Amex, etc.)
- **Wallets**: Apple Pay, Google Pay, Samsung Pay, PayPal
- **Bank Transfer**: ACH, SEPA, Wire transfers
- **APM**: iDEAL, Sofort, Bancontact, etc.

### Integration Complexity
- ⭐⭐☆☆☆: Very Easy - Simple API key setup
- ⭐⭐⭐☆☆: Easy - Standard OAuth/API key
- ⭐⭐⭐⭐☆: Medium - Additional configuration required
- ⭐⭐⭐⭐⭐: Complex - Extensive setup, multiple credentials

## Connector Selection Guide

### For E-commerce
1. **Global**: Stripe or Adyen
2. **Europe**: Stripe + Klarna/Sofort
3. **US**: Stripe + PayPal
4. **APAC**: Airwallex or Stripe

### For Marketplaces
1. **Stripe Connect** (full marketplace features)
2. **Adyen for Platforms**
3. **PayPal Commerce Platform**

### For Subscription Businesses
1. **Stripe** (best recurring support)
2. **Braintree** (PayPal integration)
3. **Checkout.com** (flexible billing)

## Getting Started

To activate any connector:
1. Visit the [Control Center](https://app.hyperswitch.io)
2. Navigate to **Connectors**
3. Select your desired connector
4. Follow the setup guide linked above

For detailed activation steps, see:
- [Activate Connector Guide](../../../hyperswitch-cloud/connectors/activate-connector-on-hyperswitch/)
- [Test Credentials](../../../hyperswitch-cloud/connectors/available-connectors/test-credentials.md)

---

**Last Updated**: April 2026  
**Total Connectors**: 34+  
**Supported Countries**: 150+  
**Supported Currencies**: 135+