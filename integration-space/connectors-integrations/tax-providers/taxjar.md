---
description: >-
  Automate sales tax calculations on transactions through TaxJar integrated via
  Juspay Hyperswitch.
---

# TaxJar

TaxJar connects to Hyperswitch as a `TaxCalculationProvider`. It is a cloud-based platform that automates sales tax calculations, reporting, and filing for businesses across multiple channels. Hyperswitch calls TaxJar during the payment flow with order and address details; TaxJar returns the applicable tax amount, which Hyperswitch includes in the transaction before authorization.

### Authentication

TaxJar uses `HeaderKey` authentication — a single API key sent as a Bearer token on every request.

| Credential | Description |
| --- | --- |
| **API Key** | Bearer token issued by TaxJar. Found in your TaxJar account under Account → TaxJar API. |

### How Tax Calculation Works

When a payment is initiated with a TaxJar connector configured:

1. Hyperswitch sends order details (line items, amounts, shipping address, billing address) to TaxJar.
2. TaxJar computes the applicable sales tax based on jurisdiction rules, product taxability, and nexus configuration.
3. TaxJar returns the tax amount to Hyperswitch.
4. Hyperswitch includes the tax in the transaction before forwarding to the payment processor for authorization.

### Common Failure Modes

**API key rejected**
Symptom: Tax calculation requests return 401 Unauthorized. Fix: Verify the API key stored in Hyperswitch matches the one in your TaxJar account. Ensure the key has the correct permissions for tax calculation (not a read-only reporting key).

**Tax not calculated for jurisdiction**
Symptom: TaxJar returns zero tax or no nexus match. Fix: Confirm your TaxJar account has nexus configured for the relevant states or jurisdictions. TaxJar only calculates tax where nexus is established.

**Missing address details**
Symptom: TaxJar returns an error about incomplete address. Fix: Ensure shipping address (city, state, zip, country) is provided on the payment. TaxJar requires a destination address to determine the applicable tax rate.

---

### Activating TaxJar via Hyperswitch

#### Prerequisites

1. A registered TaxJar account. Sign up at [taxjar.com](https://www.taxjar.com/).
2. A registered Hyperswitch account, accessible from the [Hyperswitch control center](https://app.hyperswitch.io/).
3. API Key from your TaxJar account under Account → TaxJar API.

[Steps to activate a connector on the Hyperswitch control center](../activate-connector-on-hyperswitch/README.md)

---

Connector implementation: `crates/hyperswitch_connectors/src/connectors/taxjar.rs`.
