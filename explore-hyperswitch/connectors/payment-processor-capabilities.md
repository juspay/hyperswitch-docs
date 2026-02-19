---
description: >-
  A technical reference for the parameters and lifecycle flows supported across
  card and wallet integrations.
icon: money-bill-1-wave
---

# Payment Processor Capabilities

### Core Payment Flows

Hyperswitch supports a wide range of parameters through the Payments Create API for the underlying payment connectors it integrates with. The diagram below illustrates the various parameters and flows supported as part of a typical payment connector integration.

Card Payment Flow Configurations

Hyperswitch enables multiple card payment configurations designed to support a wide range of industry-specific use cases through the unified [Payment Confirm](https://api-reference.hyperswitch.io/v1/payments/payments--confirm#payments-confirm) request.

<figure><img src="../../.gitbook/assets/Juspay hyperswitch - Architecture deepdive (6).png" alt=""><figcaption></figcaption></figure>

* Verification: Facilitates $0 verification, $0 verification for [subscriptions](https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/subscriptions), and AVS & CVV integrity checks.
* Authentication: Modular support for External authentication providers or native PSP authentication.
* Capture Strategy: Configuration for [Automatic capture](https://docs.hyperswitch.io/about-hyperswitch/payment-suite-1/payments-cards#id-1.-instant-payment-automatic-capture) or Manual/Multiple manual capture logic.
* Voiding: Explicit support for Voids initiated both before capture and before settlement.

#### Card-Specific Parameters

The Payments API supports an extensive set of card parameters to ensure regional flexibility and compliance across retail and subscription billing.

<figure><img src="../../.gitbook/assets/Juspay hyperswitch - Architecture deepdive (5).png" alt=""><figcaption></figcaption></figure>

**Transaction Initiation Types**

* Customer Initiated (CIT): Supports [Raw Card](https://docs.hyperswitch.io/about-hyperswitch/payment-suite-1/payment-method-card) and Network Token inputs.
* Merchant Initiated (MIT): Optimized for recurring billing using Processor Tokens, Raw Card + NTID, or Network Token + NTID.
* Agent Initiated: Securely handle Shared Payment Tokens for delegated payment scenarios.

**Advanced Data Fields**

* Pre-transaction: Integration of [3DS Authentication Data](https://docs.hyperswitch.io/explore-hyperswitch/workflows/3ds-decision-manager) and Risk/Fraud check data.
* Order Metadata: Deep support for L2/L3 data fields, full order information, and complex [Routing Data](https://docs.hyperswitch.io/explore-hyperswitch/workflows/intelligent-routing).
* Additional Flags: granular control for Moto, Estimated Auth, Incremental Auth, and Partial Authorizations.

#### Digital Wallet Integration

Hyperswitch provides comprehensive parameters that streamline transaction management across leading digital wallets like Google Pay and Apple Pay.

<figure><img src="../../.gitbook/assets/Juspay hyperswitch - Architecture deepdive (4).png" alt=""><figcaption></figcaption></figure>

* Experience Models: Support for Native, Redirect, and 3rd-party SDK integration patterns to ensure a [seamless checkout experience](https://docs.hyperswitch.io/explore-hyperswitch/merchant-controls).
* Payload Management: Robust handling of both Decrypted (with cryptogram and wallet data) and Encrypted payment data payloads.

#### Post-Transaction: Refunds, Disputes, and Errors

Hyperswitch offers a unified interface to track, respond to, and reconcile outcomes across multiple PSPs from a single orchestration layer.

<figure><img src="../../.gitbook/assets/Juspay hyperswitch - Architecture deepdive (8).png" alt=""><figcaption></figcaption></figure>

* Refund Management: Unified parameters for [Complete Refunds](https://api-reference.hyperswitch.io/v2/refunds/refunds--create) and multiple Partial Refund scenarios.
* Chargebacks: Streamlined [Unification of reporting and submission](https://docs.hyperswitch.io/explore-hyperswitch/account-management/disputes) across different processors.
* Unified Error Handling: Transparent access to Unified & Raw error codes, including Issuer-specific messages, PSP error codes, and MAC-level messages for faster resolution.
