---
description: Configurable cashier features
---

# Features

The Cashier Payments Suite includes 3DS Intelligence, Card Eligibility, Credit-card blocking, Closed-loop validation, Name verification, Smart Router for Payouts, Smart Retries, the Customizable Cashier SDK, and a PCI-compliant Vault. Each module is documented in detail in the sections that follow.

What unifies them is how they're operated.

### **One integration, every feature configurable**

Every feature is controlled by configuration, not code. Once a merchant integrates Juspay – via the Unified Checkout SDK, the Headless SDK, or server-to-server with the Cards SDK – engineering work is done. The cashier responds to dashboard changes and configuration API calls from that point on, not to redeployments.

* **Payment methods** turn on and off via dashboard toggle. No SDK rebuild, no app store release for mobile.
* **3DS behaviour** is expressed as rules in the 3DS Decision Manager – force challenge on fresh cards, frictionless on COF, exempt low-value, cascade silent retries.
* **Card restrictions** – BIN ranges, card types, issuer countries – are dashboard-configurable through the Card Eligibility Engine and the `/blocklist` API.
* **Payout routing** – rail ordering, volume splits, new connectors, retry cascades – lives in the Smart Router for Payouts.
* **Cashier UI** – theme, payment-method ordering, promoted methods, suggested amounts, wallet visibility – is controlled at runtime through the SDK options object.

Orchestration logic lives on Juspay's side of the integration boundary. The merchant's code talks to a stable API; Juspay's runtime resolves configuration at request time.

#### **Organization, Merchant, and Profile**

Configuration is scoped at three levels:

* **Organization** – the operator group. Global PSP credentials, shared vault tokens, group-wide defaults.
* **Merchant** – a brand within the group. Brand-specific connectors, themes, retry policies, analytics.
* **Profile** – a market or player segment within a brand. Jurisdiction-specific rules live here: UK Profile blocks credit cards, German Profile enforces Sofort name verification, Ontario Profile uses Interac.

An operator running five brands across twelve jurisdictions does not run sixty integrations – it runs one Organization, five Merchants, and as many Profiles as it has brand-jurisdiction pairs. Adding a thirteenth jurisdiction is a Profile creation, not an engineering project.
