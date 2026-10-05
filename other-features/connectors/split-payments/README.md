---
description: >-
  Unify your marketplace settlement logic across multiple processors through a
  single configuration.
icon: split
metaLinks:
  alternates:
    - ./
---

<!-- truth manifest; hyperswitch 59c3249bf29bc3800ce391de49fab00590c0cf9e
     symbols: split_txns_enabled = crates/api_models/src/admin.rs:2672,3070,3445; crates/hyperswitch_domain_models/src/payments.rs:1367-1371
     symbols: SplitPaymentsRequest has 4 externally tagged variants, stripe_split_payment, adyen_split_payment, xendit_split_payment, payload_split_payment = crates/common_types/src/payments.rs:35-66
     symbols: 4 connector implementations, Stripe, Adyen, Xendit, Payload = crates/hyperswitch_connectors/src/connectors/stripe.rs; adyen/transformers.rs; xendit.rs; payload/transformers.rs
     symbols: platform provider and connected processor resolution, X-Connected-Merchant-Id = crates/router/src/services/authentication.rs:6594-6648; crates/router/src/core/payments/helpers.rs:3179-3235
     symbols: Currency has 160 variants = crates/common_enums/src/enums.rs:979-1140
     absent: USDT = checked Currency and split request enums, 0 exact matches
     absent: RazorpaySplitPayment, CashfreeSplitPayment = checked SplitPaymentsRequest and connector consumers, 0 matches
     checked: 2026-10-05 -->

# Processors with Split Settlement

### Before you start

Enable split settlement for the Business Profile with `split_txns_enabled`, then configure the merchant connector account for that profile. Processor credentials stay with that profile's connector account.

A platform API key can act on behalf of a Connected merchant by sending `X-Connected-Merchant-Id`, but the payment still runs under the Connected merchant. Split rules are sent on that payment and use its selected connector account. See [Platform Organization](../../../integration-guide/account-management/multiple-accounts-and-profiles/platform-organization-concepts.md) for the account and credential boundaries.

### Overview

Split settlement refers to the process of dividing a single transaction into multiple parts, ensuring that funds are automatically distributed among different parties in real-time or through scheduled settlements.

This is essential for marketplaces, platforms, and businesses handling multi-party transactions, enabling seamless revenue sharing, commission deductions, and vendor settlements while maintaining accuracy and compliance.

### Hyperswitch Implementation

Juspay Hyperswitch provides payment functionality with connector-specific implementations supporting four processor integrations: Stripe, Adyen, Xendit, and Payload.

Each connector has distinct validation rules, data structures, and split models tailored to their specific requirements. This abstraction allows you to manage multi-party flows through a single orchestration layer.

### Connector-Specific Split Models

The table below outlines the specific capabilities supported by each processor integration:

| Processor                          | Key Capabilities                                                                                                                                |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| [Xendit](xendit-split-payments.md) | Supports both single splits and multiple route distributions, with flexible routing options including flat amounts and percentage-based splits. |
| [Adyen](adyen-split-payments.md)   | Provides various split types including balance accounts, commissions, and fees with detailed charge response tracking.                          |
| [Stripe](stripe-split-payments.md) | Implements application fees and destination accounts for revenue sharing scenarios.                                                             |
| Payload                            | Uses ledger entries to allocate amounts to receivers. This section does not yet have a Payload setup guide.                                      |

### Coverage boundaries

`SplitPaymentsRequest` has four processor variants. It has no Razorpay or Cashfree variant, so this request does not provide split settlement through those connectors. For UPI support, use the [Razorpay connector guide](../../../integration-space/connectors-integrations/available-connectors/razorpay.md) and the [connector catalog](../../../integration-space/connectors-integrations/available-connectors/README.md). A Cashfree connector guide was not present at the checked docs revision.

The split request and route currency fields use Hyperswitch's `Currency` enum. The enum has 160 values and no `USDT` entry. No crypto-asset variant appears in the split request enums, so USDT cannot be used for split settlement through this API shape.

Percentage-based processor traffic allocation is a routing concern, not settlement allocation. Use [Volume-Based Routing](../../../integration-guide/workflows/intelligent-routing/volume-based-routing.md) when the goal is to send a percentage of traffic to each processor.
