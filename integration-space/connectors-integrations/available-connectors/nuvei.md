---
description: >-
  Accept card, network token, pay later, wallet, and bank redirect payments through Nuvei with Hyperswitch.
metaLinks:
  alternates:
    - nuvei.md
---

# Nuvei

Based in Canada, Nuvei is a fintech company. Merchants can accept cards, network tokens, Apple Pay, Google Pay, PayPal, Afterpay Clearpay, Klarna, and European bank redirects. Cards, network tokens, Apple Pay, and Google Pay support mandates, and every listed method supports refunds and manual capture. Card payments can use optional 3DS, while webhooks cover payment and dispute updates.

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch 93becbaee4ee3686e1a4d5750d2e547c56c27047; host http://localhost:8080; fetched 2026-09-10; matrix canonical-json-v1 sha256 27951de892af028b; 138 connectors.
     Do not edit by hand. This block regenerates from the connector's
     SupportedPaymentMethods declaration in code; edit that instead. -->

**Integration status:** live

**Category:** payment gateway

**Webhook flows:** disputes, payments

| Payment method | Type | Mandates | Refunds | Capture methods | 3DS | Card networks | Countries | Currencies |
|---|---|---|---|---|---|---|---|---|
| bank redirect | EPS | not supported | supported | automatic, manual, sequential automatic | not applicable | - | 10 ([full list](https://hyperswitch.io/pm-list)) | 90 ([full list](https://hyperswitch.io/pm-list)) |
| bank redirect | Giropay | not supported | supported | automatic, manual, sequential automatic | not applicable | - | - | EUR |
| bank redirect | iDEAL | not supported | supported | automatic, manual, sequential automatic | not applicable | - | - | EUR |
| bank redirect | Sofort | not supported | supported | automatic, manual, sequential automatic | not applicable | - | 10 ([full list](https://hyperswitch.io/pm-list)) | 90 ([full list](https://hyperswitch.io/pm-list)) |
| card | Credit Card | supported | supported | automatic, manual, sequential automatic | supported, optional | American Express, Cartes Bancaires, Diners Club, Discover, Interac, JCB, Mastercard, UnionPay, Visa | 249 ([full list](https://hyperswitch.io/pm-list)) | 90 ([full list](https://hyperswitch.io/pm-list)) |
| card | Debit Card | supported | supported | automatic, manual, sequential automatic | supported, optional | American Express, Cartes Bancaires, Diners Club, Discover, Interac, JCB, Mastercard, UnionPay, Visa | 249 ([full list](https://hyperswitch.io/pm-list)) | 90 ([full list](https://hyperswitch.io/pm-list)) |
| network token | Network Token | supported | supported | automatic, manual, sequential automatic | not applicable | - | - | - |
| pay later | Afterpay Clearpay | not supported | supported | automatic, manual, sequential automatic | not applicable | - | 10 ([full list](https://hyperswitch.io/pm-list)) | 90 ([full list](https://hyperswitch.io/pm-list)) |
| pay later | Klarna | not supported | supported | automatic, manual, sequential automatic | not applicable | - | 10 ([full list](https://hyperswitch.io/pm-list)) | 90 ([full list](https://hyperswitch.io/pm-list)) |
| wallet | Apple Pay | supported | supported | automatic, manual, sequential automatic | not applicable | - | 59 ([full list](https://hyperswitch.io/pm-list)) | 90 ([full list](https://hyperswitch.io/pm-list)) |
| wallet | Google Pay | supported | supported | automatic, manual, sequential automatic | not applicable | - | 237 ([full list](https://hyperswitch.io/pm-list)) | 90 ([full list](https://hyperswitch.io/pm-list)) |
| wallet | PayPal | not supported | supported | automatic, manual, sequential automatic | not applicable | - | 10 ([full list](https://hyperswitch.io/pm-list)) | 90 ([full list](https://hyperswitch.io/pm-list)) |

### Authentication

Supply the Merchant ID in the API key field, the Merchant Site ID in the `key1` field, and the Merchant Secret in the API secret field. Nuvei requests do not use an Authorization header; the connector places these authentication values and the request checksum in the request body. See [`NuveiAuthType::try_from()`](https://github.com/juspay/hyperswitch/blob/740e642eabb5b54094f589d4ebc08aa9e796fab1/crates/hyperswitch_connectors/src/connectors/nuvei/transformers.rs#L1734-L1757) and [`get_auth_header()`](https://github.com/juspay/hyperswitch/blob/740e642eabb5b54094f589d4ebc08aa9e796fab1/crates/hyperswitch_connectors/src/connectors/nuvei.rs#L127-L133).

### Before you start

1. Register with Nuvei.
2. Create or sign in to your account in the [Hyperswitch control center](https://app.hyperswitch.io/).
3. In the Nuvei dashboard, go to **Settings → My Account → Account Details** to find the API key.
4. Enable the same payment methods in Nuvei that you plan to select in Hyperswitch.
5. Have the credentials listed in [Authentication](#authentication) ready.

To connect Nuvei to your Hyperswitch account, follow [Activate a connector on Hyperswitch](../activate-connector-on-hyperswitch/README.md), then return here for what Nuvei supports.

### Webhooks

For payment direct merchant notifications, Hyperswitch verifies the advanced response checksum with SHA-256 ([source](https://github.com/juspay/hyperswitch/blob/93becbaee4ee3686e1a4d5750d2e547c56c27047/crates/hyperswitch_connectors/src/connectors/nuvei.rs#L1311-L1369)). Chargeback notifications use a checksum header, but the source marks the verification-message format as a placeholder. Confirm that format before enabling chargeback notifications ([source](https://github.com/juspay/hyperswitch/blob/93becbaee4ee3686e1a4d5750d2e547c56c27047/crates/hyperswitch_connectors/src/connectors/nuvei.rs#L1371-L1378)).

#### Payment and refund events

The payment mapper contains 11 branches for the combinations below. Incoming `DmnStatus` values are uppercase because the enum applies `#[serde(rename_all = "UPPERCASE")]` ([status enum](https://github.com/juspay/hyperswitch/blob/93becbaee4ee3686e1a4d5750d2e547c56c27047/crates/hyperswitch_connectors/src/connectors/nuvei/transformers.rs#L3434-L3443), [mapping](https://github.com/juspay/hyperswitch/blob/93becbaee4ee3686e1a4d5750d2e547c56c27047/crates/hyperswitch_connectors/src/connectors/nuvei/transformers.rs#L3634-L3675)):

| Nuvei status | Transaction type | Hyperswitch effect |
| --- | --- | --- |
| `SUCCESS` or `APPROVED` | `Auth` | Authorization succeeded |
| `SUCCESS` or `APPROVED` | `Sale` | Payment succeeded |
| `SUCCESS` or `APPROVED` | `Settle` | Capture succeeded |
| `SUCCESS` or `APPROVED` | `Void` | Payment canceled |
| `SUCCESS` or `APPROVED` | `Credit` | Refund succeeded |
| `ERROR` or `DECLINED` | `Auth` | Authorization failed |
| `ERROR` or `DECLINED` | `Sale` | Payment failed |
| `ERROR` or `DECLINED` | `Settle` | Capture failed |
| `ERROR` or `DECLINED` | `Void` | Cancellation failed |
| `ERROR` or `DECLINED` | `Credit` | Refund failed |
| `PENDING` | `Auth`, `Sale`, or `Settle` | Payment processing |

Other payment combinations are not supported.

#### Payout events

When payouts are enabled and the client request identifier has the payout prefix, the implementation uses 3 mapping branches ([source](https://github.com/juspay/hyperswitch/blob/93becbaee4ee3686e1a4d5750d2e547c56c27047/crates/hyperswitch_connectors/src/connectors/nuvei/transformers.rs#L3678-L3693)):

| Nuvei status | Transaction type | Hyperswitch effect |
| --- | --- | --- |
| `SUCCESS` or `APPROVED` | `Credit` | Payout succeeded |
| `PENDING` | Any declared transaction type | Payout processing |
| `DECLINED` or `ERROR` | Any declared transaction type | Payout failed |

Other payout combinations are not supported.

#### Dispute events

The dispute enum defines 51 exact event codes. The table accounts for all 51 ([event codes](https://github.com/juspay/hyperswitch/blob/93becbaee4ee3686e1a4d5750d2e547c56c27047/crates/hyperswitch_connectors/src/connectors/nuvei/transformers.rs#L3247-L3400), [mapping](https://github.com/juspay/hyperswitch/blob/93becbaee4ee3686e1a4d5750d2e547c56c27047/crates/hyperswitch_connectors/src/connectors/nuvei/transformers.rs#L3710-L3816)):

| Hyperswitch effect | Nuvei event codes |
| --- | --- |
| Dispute opened | `FC`, `CC`, `MCC`, `FC-CLSD-RCL`, `INQ` |
| Dispute accepted | `CC-A-ACPT`, `FC-A-ACPT`, `FC-A-ACPT-MCOLL`, `FC-M-ACPT`, `FC-SPCSE`, `RDR`, `MCC-M-ACPT`, `MCC-A-ACPT`, `INQ-M-RFND`, `IPA-M-ACPT`, `IPA-M-PART`, `IPA-A-ACPT`, `IPAR-M-ACPT`, `IPAR-A-ACPT` |
| Dispute lost | `FC-A-EPRD`, `FC-M-PART`, `FC-CLSD-CHF`, `PA-CLSD-CHF`, `MCC-CLSD-CHF` |
| Dispute challenged | `FC-M-RJCT`, `FC-A-RJCT`, `IPA`, `MPA-I-RJCT`, `INQ-M-RSP`, `IPA-M-RJCT` |
| Dispute expired | `FC-A-RJCT-EXP`, `FC-M-PART-EXP`, `FC-M-RJCT-EXP`, `MCC-EXPR`, `INQ-EXPR`, `IPA-M-PART-EXP`, `IPA-M-RJCT-EXP` |
| Dispute won | `MPA-I-ACPT`, `MPA-I-PART`, `FC-CLSD-MF`, `MCC-CLSD-MF`, `PA-CLSD-MF` |
| Dispute canceled | `FC-I-RCL`, `INQ-A-CNLD`, `PA-CLSD-RC`, `CC-I-RCLL` |
| No direct event; category fallback may apply | `MCC-A-RJCT`, `MCC-M-RJCT`, `INQ-A-RJCT`, `INQ-M-P-RFND`, `INQ-UPD` |

The category fallback defines 5 exact values ([source](https://github.com/juspay/hyperswitch/blob/93becbaee4ee3686e1a4d5750d2e547c56c27047/crates/hyperswitch_connectors/src/connectors/nuvei/transformers.rs#L3420-L3431)):

| Chargeback category | Hyperswitch effect |
| --- | --- |
| `cancelled` | Dispute canceled |
| `Duplicate` | Dispute canceled |
| `RDR-Refund` | Dispute accepted |
| `Regular` | No fallback event |
| `Soft_CB` | No fallback event |
