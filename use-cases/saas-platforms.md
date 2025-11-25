---
description: All the payment use-cases for SaaS providers
hidden: true
icon: desktop
---

# SaaS Platforms

Across SaaS platforms operating in commerce, bookings, operations, professional services, and other verticals, several common payment patterns appear consistently. These platforms typically onboard multiple merchants, each with their own PSPs, routing needs, onboarding workflows, and operational requirements. A recurring theme we observe is the need for a composable payment layer that standardizes these differences without requiring custom engineering for each merchant.

Hyperswitch supports SaaS providers with modular capabilities that help streamline merchant onboarding, unify diverse PSP behaviors, and create consistent payment experiences across verticals — while fitting into the platform’s existing product and operational model.

The sections below outline the most frequent patterns seen across SaaS platforms.

### Use Case 1 - Supporting merchants who bring their own PSPs

A large number of SaaS platforms onboard merchants who already use specific PSPs or APMs. Patterns across teams show challenges around maintaining multiple processor integrations, normalizing APIs, handling different webhook types, and safely collecting PSP credentials. This often slows down merchant onboarding cycles.

#### Solution

Hyperswitch provides a connector layer that standardizes PSP interactions, enabling SaaS teams to support merchant-specific processors without building custom integrations. Platforms typically adopt one of three models:

* **Full-Stack Mode** - Hyperswitch manages UI, tokenization, 3DS, and routing.
* **Backend-Only Mode** - the platform keeps its UI but uses Hyperswitch for processor calls.
* **Stateless Mode** - used when merchants require strict data boundaries.

These patterns reduce onboarding time and simplify multi-PSP support.

### Use Case 2 - Maintaining merchant-level isolation (Org → Merchant → Profile)

Most SaaS platforms require clean separation between merchants — including PSP keys, routing preferences, business units, and operational users. Engineering teams often highlight the friction of building and maintaining custom multi-tenant boundaries.

#### Solution

Hyperswitch provides a built-in **Organization → Merchant → Profile** hierarchy that platforms use to:

* Segment PSP configurations
* Separate routing logic
* Manage dashboards and operational roles
* Maintain regional or business-unit splits
* Produce merchant-specific reports and analytics

This structure simplifies multi-tenant support and reduces custom permissioning work.

### Use Case 3 - Programmatic merchant onboarding (MoR & Non-MoR)

A recurring requirement among SaaS platforms is a predictable, programmatic onboarding flow. Some platforms act as Merchant-of-Record (MoR), while others allow merchants to use their own PSP keys. Across both models, teams often look for ways to streamline credential onboarding while maintaining security.

#### Solution

Hyperswitch’s **Platform Account APIs** support:

* Creating merchants via API
* Uploading or connecting PSP accounts
* Handling MoR and non-MoR flows
* Embedding credential setup into the SaaS product
* Standardizing all merchants into a single payment lifecycle format

This reduces onboarding overhead and provides consistent onboarding behavior across merchants and PSPs.

### Use Case 4 - Standardizing diverse payment flows across verticals

SaaS platforms commonly support varied flows depending on their vertical — including $0 auth, 3DS, multi-capture, partial refunds, or recurring billing. Teams often highlight PSP fragmentation as a recurring operational challenge.

#### Solution

Hyperswitch normalizes:

* $0 verification flows
* 3DS flows
* Auth / capture sequences
* Partial and multi-capture
* Refund and dispute flows
* Wallet parameters
* L2/L3 data requirements
* Raw PSP response delivery

This allows SaaS platforms to expose a single, unified flow while still supporting multiple processors.

### Use Case 5 - Flexible vaulting for multi-merchant environments

Vaulting requirements vary widely across merchants. Some rely on PSP-native vaults; others require unified vaults, external vaults, or merchant-scoped setups. SaaS engineering teams often note the difficulty of supporting multiple vaulting choices consistently.

#### Solution

Hyperswitch supports multiple vaulting models used across SaaS platforms:

1. **External Vault** (merchant-owned vault)
2. **Unified Vault** (portable tokens across PSPs)
3. **PSP-Native Vaulting**
4. **Merchant-Scoped Vaults**

These options help platforms satisfy different merchant requirements without custom implementations.

### Use Case 6 - Participating in only part of the payment lifecycle

Some SaaS platforms do not manage full payment flows; they only need to perform operations like refunds, captures, or voids. Teams frequently highlight the challenge of interacting with PSPs consistently across different processors.

#### Solution

Hyperswitch’s **Relay APIs** provide a common interface for:

* Captures
* Refunds
* Voids and cancels
* Metadata updates
* Retrieving PSP transaction state

This allows platforms to integrate operational workflows without orchestrating checkout or auth.

### Use Case 7 - Unifying operational workflows across merchants

Many SaaS teams highlight the operational overhead of managing refunds, disputes, errors, and webhooks across different PSPs. Differences in payloads and flows frequently cause support friction.

#### Solution

Hyperswitch unifies:

* Refund and dispute workflows
* Error models
* Transaction statuses
* Webhook structures
* Operational logs and metadata

This helps platforms maintain consistent support tooling and operational flows across PSPs.

### Use Case 8 - Monitoring & SLA visibility for multi-merchant platforms

SaaS platforms often need detailed operational visibility - connector health, PSP performance, incident context, and merchant-level SLAs. This is especially common in platforms with global merchant distribution.

#### Solution

Hyperswitch provides:

* Real-time connector health checks
* PSP latency/performance metrics
* Retry/fallback visibility
* Audit logs
* Distributed tracing
* Merchant/profile-level SLA segmentation

These tools help SaaS teams maintain reliable operations at scale.
