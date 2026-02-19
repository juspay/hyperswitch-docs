---
description: >-
  Unify your marketplace settlement logic across multiple processors through a
  single configuration.
icon: split
---

# Processors with Split Settlement

### Overview

Split settlement refers to the process of dividing a single transaction into multiple parts, ensuring that funds are automatically distributed among different parties in real-time or through scheduled settlements.

This is essential for marketplaces, platforms, and businesses handling multi-party transactions, enabling seamless revenue sharing, commission deductions, and vendor settlements while maintaining accuracy and compliance.

#### Hyperswitch Implementation

Hyperswitch provides payment functionality with connector-specific implementations supporting three major payment processors: Stripe, Adyen, and Xendit.

Each connector has distinct validation rules, data structures, and split models tailored to their specific requirements. This abstraction allows you to manage multi-party flows through a single orchestration layer.

Configuration Requirements

* Business Profile: Split Settlement must be enabled at the business profile level through the `split_txns_enabled` flag. This allows merchants to configure this functionality per profile.
* Account Setup: Proper merchant connector account (MCA) setup is required before split settlement can be utilized.

#### Connector-Specific Split Models

The table below outlines the specific capabilities supported by each processor integration:

| Processor                          | Key Capabilities                                                                                                                                |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| [Xendit](xendit-split-payments.md) | Supports both single splits and multiple route distributions, with flexible routing options including flat amounts and percentage-based splits. |
| [Adyen](adyen-split-payments.md)   | Provides various split types including balance accounts, commissions, and fees with detailed charge response tracking.                          |
| [Stripe](stripe-split-payments.md) | Implements application fees and destination accounts for revenue sharing scenarios.                                                             |
