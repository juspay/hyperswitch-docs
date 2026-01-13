# Roadmap

#### Smarter Rules for Advanced Businesses

* Support for **one-to-many & many-to-one rules** ensure the system works whether a single payout covers many sales or one sale spans multiple payouts

#### Forex Handling

* Support for merchant-provided exchange rates in cross-currency reconciliation. This will allow settlements and bank deposits in different currencies to be automatically aligned using the chosen FX rate, removing the need for manual conversions

#### Exceptions Aging & Tolerance Handling

* Track how long each exception remains unresolved and investigate cases breaching SLA thresholds, ensuring timely closure and improved reconciliation hygiene
* Tolerance handling — configure acceptable thresholds for amount differences, so small variances don’t block reconciliation

#### **AI-Driven Exception Handling**

* AI-powered recommendations to help resolve unmatched transactions faster. When an exception occurs, the system will automatically analyze metadata (amounts, dates, identifiers, references) and surface the most likely matching transactions that can close the gap — so operators can review and resolve exceptions in a fraction of the time

#### Advanced Data Management

* A dedicated module that isolates problematic records during ingestion, prevents them from polluting the reconciliation flow, and provides tools for users to review and correct them before reprocessing
