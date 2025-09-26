# Roadmap

{% hint style="info" %}
**Note**:

Reconciliation V2 is currently in Beta. For Reconciliation V1, please check [here](../reconciliation/).

We will continue to support Reconciliation V1 for all existing merchants. With the launch of V2, reconciliation is now a configurable experience — merchants will have the choice to continue with V1 or opt into V2 directly from the dashboard

All your existing configurations and setups will seamlessly carry over to V2 with no additional effort required on your end. We recommend beginning the transition to Reconciliation V2 to take advantage of the latest features.
{% endhint %}

#### Advanced Data Management - 15 Sep

* A dedicated module that isolates problematic records during ingestion, prevents them from polluting the reconciliation flow, and provides tools for users to review and correct them before reprocessing

#### Interface to fix Reconciliation Exceptions - 19 Sept

* Instantly resolve mismatches in transaction amounts, status, or other metadata through a simple interface
* The system will provide the ability to view discrepancies in side-by-side comparisons across multiple sources, highlight the exact mismatched fields, and offer resolution options such as editing values while maintaining a clear audit trail for every action taken

#### Smarter Rules for Advanced Businesses - 29 Sep

* Support for one-to-many & many-to-one rules ensure the system works whether a single payout covers many sales or one sale spans multiple payouts
* Tolerance handling — configure acceptable thresholds for amount differences, so small variances don’t block reconciliation

#### **FX reconciliation - 20th Oct**

* Support for merchant-provided exchange rates in cross-currency reconciliation. This will allow settlements and bank deposits in different currencies to be automatically aligned using the chosen FX rate, removing the need for manual conversions

#### **AI-Driven Exception Handling - 20th Oct**

* AI-powered recommendations to help resolve unmatched transactions faster. When an exception occurs, the system will automatically analyze metadata (amounts, dates, identifiers, references) and surface the most likely matching transactions that can close the gap — so operators can review and resolve exceptions in a fraction of the time

#### Self-serve Reporting - 30th Oct

* Ability to customise columns – Users can choose which columns (e.g., transaction ID, amount, date, metadata fields) to include in the reconciliation report and reorder them as needed
