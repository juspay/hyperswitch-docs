# Why we evolved(V1 vs V2)

{% hint style="info" %}
**Note**:

Reconciliation V2 is currently in Beta. For Reconciliation V1, please check [here](../reconciliation/).

We will continue to support Reconciliation V1 for all existing merchants. With the launch of V2, reconciliation is now a configurable experience — merchants will have the choice to continue with V1 or opt into V2 directly from the dashboard

All your existing configurations and setups will seamlessly carry over to V2 with no additional effort required on your end. We recommend beginning the transition to Reconciliation V2 to take advantage of the latest features.
{% endhint %}

Our V1 Reconciliation Engine has supported merchants since 5 years. It was purpose-built to solve high-volume transaction-matching problems like 2-way (processor ↔ internal) matches&#x20;

By focusing narrowly on the high-frequency scenarios, it could optimize its parsers and rule engine for speed and accuracy, rather than spreading complexity across edge cases

V1 was intentionally engineered to be the right tool for the right problems — replacing spreadsheets with an automated matching framework that solved the majority of everyday reconciliation pain for many customers

### Evolving from V1: Key Improvements in V2

#### **Matching Flexibility**

* Beyond 2-way matching: V1 only supported fixed 2-way matches. V2 introduces N-way matching to handle complex flows with multiple accounts
* One-to-many & many-to-one: The new model supports a single payment mapping to multiple orders or vice versa, correctly handling splits, merges, and multi-leg settlements

#### **Enhanced Accounting & Reporting**

* Profile-scoped ledgers: V2 allows for isolated ledgers and rules for each business unit, ensuring accurate attribution and preventing reconciliation conflicts
* Point-in-time balances: With every posting stored, V2 can reconstruct ledger balances for any historical date, essential for audits and reporting
* Explicit FX accounting: V2 provides a dedicated way to account for FX gains and losses, ensuring all conversions are auditable and traceable without affecting reconciliation

#### Auditable History

V2 provides a complete, immutable audit trail for every transaction, a feature V1 lacked. This means that every change to a transaction is recorded and traceable. We provide full visibility into the entire data lifecycle, from the moment a file is ingested to the final reconciled transaction

This comprehensive auditability includes:

* Ingestion: A clear record of every file upload or scheduled data pull
* Transformation: Visibility into how raw data from a source file was processed and transformed into a standardized, reconciliation-ready format
* Transaction Evolution: An immutable history of every change to a transaction, ensuring that nothing is ever lost or altered without a record

