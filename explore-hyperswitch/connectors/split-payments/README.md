---
icon: split
---

# Processors with Split Settlement

Split settlement refer to the process of dividing a single transaction into multiple parts, ensuring that funds are automatically distributed among different parties in real-time or through scheduled settlements. This is essential for marketplaces, platforms, and businesses handling multi-party transactions, enabling seamless revenue sharing, commission deductions, and vendor settlements while maintaining accuracy and compliance.

#### Hyperswitch Implementation

Hyperswitch provides payment functionality with connector-specific implementations supporting three major payment processors: Stripe, Adyen, and Xendit. Each connector has distinct validation rules, data structures, and split models tailored to their specific requirements.

Configuration Requirements

Split Settlement must be enabled at the business profile level through the `split_txns_enabled`, allowing merchants to configure this functionality per profile. Proper merchant connector account setup is required before split settlement can be utilized.

Connector-Specific Split Models

Xendit: Supports both single splits and multiple route distributions, with flexible routing options including flat amounts and percentage-based splits.

Adyen: Provides various split types including balance accounts, commissions, and fees with detailed charge response tracking.

Stripe: Implements application fees and destination accounts for revenue sharing scenarios.
