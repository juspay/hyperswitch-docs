---
name: hyperswitch-docs-analytics-disputes
description: Use this skill when the user asks about "Hyperswitch analytics", "payment analytics dashboard", "exporting payment data", "dispute management in Hyperswitch", "how to handle chargebacks", "dispute documentation", "analytics and operations", "payment reports", "export CSV", "reconciliation data", or needs to understand the operational and analytics features documented in Hyperswitch.
version: 1.0.0
tags: [hyperswitch, docs, analytics, disputes, operations, reconciliation]
---

# Analytics & Dispute Management

## Overview

This skill covers the operational side of Hyperswitch — payment analytics, data export, and dispute (chargeback) management, as documented in the Hyperswitch docs.

---

## Analytics & Operations

**Doc reference:** `explore-hyperswitch/account-management/analytics-and-operations/README.md`

The Hyperswitch dashboard provides:
- Real-time payment success rates by connector, payment method, currency
- Conversion funnel analytics (initiated → confirmed → succeeded)
- Routing breakdown (which connector handled what % of volume)
- Refund and dispute rates
- Revenue and volume metrics

---

## Exporting Payment Data

**Doc reference:** `explore-hyperswitch/account-management/analytics-and-operations/exporting-payments-data.md`

Export payments data for reconciliation or offline analysis:

1. Dashboard → Analytics → Payments
2. Apply filters (date range, status, connector, currency)
3. Click **Export** → choose CSV or JSON
4. For automated exports, use the API:

```bash
POST /analytics/v1/payments/export
{
  "time_range": {
    "start_time": "2024-06-01T00:00:00Z",
    "end_time": "2024-06-30T23:59:59Z"
  },
  "filters": {
    "status": ["succeeded"],
    "connector": ["stripe"]
  }
}
```

---

## Dispute Management

**Doc reference:** `explore-hyperswitch/account-management/disputes.md`

### Dispute Lifecycle in the Dashboard

1. **Dashboard → Disputes** — shows all open disputes
2. Each dispute shows:
   - Dispute ID, payment ID, amount, reason
   - `challenge_required_by` deadline
   - Current stage: `pre_dispute` / `dispute` / `pre_arbitration`

### Responding to a Dispute

1. Click the dispute in the dashboard
2. Review the dispute reason (e.g., `product_not_received`, `fraudulent`)
3. Choose **Accept** or **Challenge**
4. If challenging: upload evidence documents
   - Shipping confirmation / tracking
   - Customer communication logs
   - Service access logs
   - Cancellation/refund policy
5. Submit before the `challenge_required_by` deadline

### Via API

```bash
# Submit evidence
POST /disputes/{dispute_id}/evidence
{
  "customer_communication": "<base64_or_url>",
  "shipping_documentation": "<base64_or_url>",
  "product_description": "Digital service — user accessed plan features on 2024-06-01",
  "customer_email_address": "customer@example.com"
}
```

---

## Fraud & Risk Management

**Doc reference:** `explore-hyperswitch/workflows/fraud-and-risk-management/README.md`

- **FRM setup guide:** `activating-frm-in-hyperswitch.md` — integrate Riskified, Signifyd, or other FRM providers
- **Fraud blocklist:** `fraud-blocklist.md` — block specific cards, emails, or IPs

---

## Surcharge Configuration

**Doc reference:** `explore-hyperswitch/account-management/surcharge/surcharge-setup-guide.md`

Configure surcharges for specific payment methods (e.g., add a 1.5% fee for credit card payments):

1. Dashboard → Account Management → Surcharge
2. Define surcharge rules by payment method type
3. Hyperswitch applies the surcharge to the payment amount automatically

---

## Multi-Tenancy & Account Management

**Doc reference:** `explore-hyperswitch/account-management/multiple-accounts-and-profiles/`

- **Account structure:** `hyperswitch-account-structure.md` — Organisation → Merchant → Business Profile hierarchy
- **Platform/Org setup:** `platform-org-and-merchant-setup.md`
- **Multi-tenancy:** `explore-hyperswitch/account-management/multi-tenancy-with-hyperswitch.md`

---

## Production Tips

- Set up automated data exports to your data warehouse daily — real-time reconciliation reduces month-end close time significantly.
- Monitor `dispute_rate` per connector in analytics — a connector with >0.5% dispute rate is a strong signal to adjust routing rules or review fraud controls.
- Respond to all disputes promptly, even losing ones — unanswered disputes are auto-lost and affect your chargeback ratio with card networks.
- Use the fraud blocklist proactively after confirmed fraud events — blocking the card BIN/email immediately reduces repeat fraud from the same actor.
