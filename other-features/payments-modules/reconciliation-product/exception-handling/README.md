---
description: >-
  Understand how Juspay Hyperswitch captures, classifies, and manages
  reconciliation exceptions—including Mismatched and Expected transaction
  anomalies—to maintain financial data integrity.
---

# Exception Handling

### Overview

The Exception Module is responsible for capturing, classifying, and managing anomalies detected during the reconciliation process. This module ensures that no transaction is lost and that financial data integrity is maintained between the internal data (Left Side) and the external partner/gateway (Right Side).

### Exception Classifications

Exceptions are categorized into two distinct types based on the presence of counterpart data and the result of the matching logic.

#### Type A: Mismatched (Data Integrity)

* **Definition:** Records exist on both sides, and the system has attempted reconciliation. However, the comparison logic failed because key attributes do not match.
* **Reconciliation Status:** `MISMATCHED`
* **Business Context:** This represents a data integrity error requiring investigation (e.g., amount discrepancies, status discrepancies, or metadata corruption).

#### Type B: Expected (Timing/Availability)

* **Definition:** These are one-sided transactions. The system has a record on one side (e.g., Internal Ledger), but the corresponding record on the other side (e.g., Bank Statement) has not arrived yet.
* **Reconciliation Status:** `EXPECTED`
* **Business Context:** This is often a temporary state caused by processing latency, batch cut-off times, or network delays.
