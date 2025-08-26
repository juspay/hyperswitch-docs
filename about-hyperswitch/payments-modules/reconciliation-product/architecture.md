# Architecture

{% hint style="info" %}
**Note**:

Reconciliation V2 is currently in Beta. For Reconciliation V1, please check [here](../reconciliation/).

We will continue to support Reconciliation V1 for all existing merchants. With the launch of V2, reconciliation is now a configurable experience — merchants will have the choice to continue with V1 or opt into V2 directly from the dashboard

All your existing configurations and setups will seamlessly carry over to V2 with no additional effort required on your end. We recommend beginning the transition to Reconciliation V2 to take advantage of the latest features.
{% endhint %}

Our V1 Reconciliation Engine has supported merchants since 5 years. It was purpose-built to solve high-volume transaction-matching problems like 2-way (processor ↔ internal) matches&#x20;

By focusing narrowly on the high-frequency scenarios, it could optimize its parsers and rule engine for speed and accuracy, rather than spreading complexity across edge cases

V1 was intentionally engineered to be the right tool for the right problems — replacing spreadsheets with an automated matching framework that solved the majority of everyday reconciliation pain for many customers

### Why we evolved (lessons learned from V1)

* **One-to-Many & Many-to-One Matching**
  * Enable matches where a single payment maps to multiple orders (1→many) or multiple captures roll up to a single payout (many→1)
  * Previously we couldn’t reconcile cases like one payout covering many orders or several partial captures for one order; the new model supports splits, merges and multi-leg settlements so each flow is attributed and reconciled correctly
* **N-way matching — include any number of accounts in a single flow**
  * V2 supports N-way matching: add as many accounts/legs as required and maintain per-account ledgers so every payment, fee, reserve or payout is recorded, attributed and auditable
  * V1 only supported fixed 2-way matches, which forced complex flows into a rigid model and caused attribution and reconciliation noise
* **Profile-scoped configs, ledgers & matching**
  * All configuration, ledger entries and matching logic are scoped to a profile (Org → Merchant → Profile) instead of a single merchant bucket like in V1
  * Each business unit / channel gets its own rules, chart of accounts, and ledgers — so flows are isolated, attribution is exact, and reconciliations don’t interfere with each other
* **Historic, point-in-time ledger balances**
  * Because we store every posting into per-account ledgers, we can reconstruct balances for any timestamp — essential for audits, investigations, month-end closes, and regulatory reporting
* **Explicit FX Accounting**
  * Merchants can supply a conversion rate that applies to a specific reconciliation
  * Post FX gains/losses separately to an FX gain/loss account so conversions are auditable, traceable, and don’t break reconciliation

| Module                | Feature                                                                                                           | Reconciliation v1 | Reconciliation v2  |
| --------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------- | ------------------ |
| Matching Engine       | <p>2-way and 3-way matching</p><p><br></p>                                                                        | ✅                 | ✅                  |
| Matching Engine       | N-way matching                                                                                                    | ❌                 | ✅                  |
| Reporting & Analytics | Analytics                                                                                                         | ✅                 | ✅                  |
| Reporting & Analytics | Scheduled Reconciliation Reports                                                                                  | ✅                 | ✅                  |
| Reporting & Analytics | Self Serve Reporting                                                                                              | ✅                 | ❌(Part of Roadmap) |
| Exceptions            | Ability to highlight amount, status exceptions                                                                    | ✅                 | ✅                  |
| Exceptions            | Ability to resolve exceptions via UI                                                                              | ✅                 | ❌(Part of Roadmap) |
| Accounts & Ledger     | Accounts are modeled after a ledger — each is typed as Debit or Credit, enabling point-in-time balance visibility | ❌                 | ✅                  |
| Accounts & Ledger     | Ability to add as many accounts as required                                                                       | ❌                 | ✅                  |
| Ingestion             | Manual uploads & basic scheduled fetch                                                                            | ✅                 | ✅                  |
| Auditability          | Immutable transaction evolution with audit trail                                                                  | ❌                 | ✅                  |

## Our Design

<figure><img src="../../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

### How We Model Money

We treat money as accounting data: named **accounts** hold balances, **entries** record every change, and **transactions** group entries into balanced, atomic actions. That double-entry approach gives mathematical guarantees (nothing can be lost), an auditable history, and clear point-in-time balances for finance teams.

#### Accounts

* Accounts map technical data to business meaning. Eg. Order Sales
* Each account has a clear purpose -  bank money, processor money, revenue, fees, etc.
* Each account is for one currency only — this avoids confusing conversions and keeps the balances healthy
* Accounts are of two types - CREDIT and DEBIT

An account is a named ledger location that represents where money sits or how it is categorized

#### Entries — the smallest recorded unit (what & why)

An entry records a single posting to an account: amount, direction (DEBIT/CREDIT), account, currency, and a status (PENDING / EXPECTED / POSTED / etc.). Entries never exist alone — they belong to a [transaction](architecture.md#transactions-grouped-balanced-atomic)

An entry is the smallest recorded action: “$50 moved into Bank:USD-1234” or “$3 moved to Processing Fees.”

* Entries are atomic building blocks that let us trace exactly which account changed and why.
* Because entries record direction and status, we can show “money expected,” “money pending,” and “money posted” separately — essential for transparent cash visibility.

#### Transactions — grouped, balanced, atomic

A transaction is a group of entries that together represent one logical movement.

* Transactions enforce the **double-entry bookkeeping rule: sum(debits) == sum(credits)**, which guarantees money cannot be created or lost. For eg: Moving money between two wallets — you must remove from one wallet and put into the other. A transaction does both together. If one side fails, the whole move is cancelled so we never have half a move.
  * **Clear provenance**: You can always answer “why did balance change?” — sales, refunds, fees, or bank adjustments are explicit entries, not hidden deltas
  * **Mathematical safety / self-check**: If total debits ≠ total credits, something is wrong. That immediate invariant helps detect data corruption, coding bugs, or missing feeds
  * **Easier reconciliation**: Matching expected vs actual items becomes a comparison of entries, not guesswork in net numbers
  * **Better audit & compliance posture**: Auditors prefer seeing debit/credit flows and versioned history; double-entry gives a clear, standard format.
* Transactions are **atomic**: either all entries are written, or none are — preventing partial or inconsistent states
  * **Consistency under failure**: If a process crashes mid-write (or a downstream system fails), atomicity prevents having a debit without the matching credit (or vice-versa)
  * **No half-transfers**: Prevents the scary cases where bookkeeping shows money removed but not placed anywhere — a clear path to lost funds or reconciliation chaos.
  * **Easier rollback & immutability**: If something must be corrected, you can create a new version or a reversing transaction rather than leaving partial writes to patch
* Transactions are the only mechanism that creates or changes entries — this simplifies reasoning, auditing and reconciliation

### Data Management

#### Data Ingestion Service

Our ingestion service connects to merchant and processor data sources using secure, flexible channels so you get timely, reliable inputs without manual work

**Supported connection types**

* **Direct processor integrations (API / webhooks)**
  * Real-time ingestion via processor APIs or webhook events.
  * Eliminates polling and manual downloads for low-latency, continuous reconciliation
* **SFTP / Scheduled file pulls**
  * Secure SFTP connectors that poll data on a configurable schedule
  * Supports directory monitoring and incremental retrieval to avoid duplicate processing
* **Manual file uploads / UI drag-and-drop**
  * Upload files through the dashboard for ad-hoc imports or backfills

#### Data Transformation Service

The transformation service is the intelligent data processing engine that bridges the gap between diverse payment processor formats and your reconciliation requirements. It automatically converts raw financial data from any source into a standardized, reconciliation-ready format.

The transformation service handles virtually any data format your payment processors provide. Structured Data Formats:

* CSV Files: Delimiter-separated values with configurable column mappings
* JSON: Nested data structures with complex field extraction
* Fixed-Width: Legacy formats like COBOL with position-based field extraction



**Flexible Configuration**

* Custom transformation rules per connection
* Support for multiple file formats from the same source
* Configurable field mappings and business logic
* Version control for transformation configurations

**Error Management**

* Detailed error categorization and resolution guidance
* Automatic alerts for systematic data issues

### How Reconciliation Works

The reconciliation engine is the intelligent core that automatically matches and validates transactions between different systems. Building on the standardized data from the transformation service, it applies sophisticated business rules to identify, match, and reconcile transactions across your payment ecosystem.

<figure><img src="../../../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

#### The Complete Flow

**1. Staging Entry Processing**

After transformation, all standardized data becomes "staging entries" - validated but unreconciled transactions waiting for processing

**2. Rule Evaluation**

The reconciliation engine evaluates each staging entry against configured business rules to determine the appropriate reconciliation action

**3. Expectation Creation**

When rules match, the system creates "expectations" - records that define what matching transactions should look like in target systems

**4. Transaction Matching**

Incoming transactions are automatically matched against existing expectations to complete the reconciliation process

**5. Exception Highlighting**

The engine automatically flags unmatched staging entries and categorizes them — amount discrepancy, status conflict, or any metadata mismatch defined in rules

**6. Exception Handling**

Operators can resolve exceptions via UI. Every action is auditable and triggers automatic re-evaluation of the expectation

### Rules Architecture

Each reconciliation rule consists of three core components that work together to define matching logic:

| Components  | Their role                                  |
| ----------- | ------------------------------------------- |
| Filters     | Should this rule apply to this transaction? |
| Identifiers | How do I find the matching transaction?     |
| Rules       | How do I know this is the right match?      |

#### 1. Filters

**Purpose**: Determines which staging entries a rule should process

**How It Works:**

* Evaluates staging entry data against specified conditions
* Only staging entries that satisfy the trigger are processed by this rule
* Supports field extraction from both standard fields and nested metadata
* Multiple trigger operators available: equals, not\_equals

**Example Scenarios:**

* Trigger on amount range: "Apply this rule to transactions over $1000"
* Trigger on merchant ID: "Use this rule for specific merchant transactions"

\
**2. Identifiers**

**Purpose**: Defines which fields to use for finding matching transactions in target systems

**How It Works:**

* Maps source staging entry fields to target system search criteria
* Creates searchable expectations in the system
* Enables efficient lookup when target transactions arrive
* Forms the primary key for matching incoming transactions

**Search Process:**

1. Extract value from staging entry's source\_field
2. Create expectation with this value mapped to target\_field
3. When target transaction arrives, search using target\_field value
4. Match found transactions against the expectation

Identifier fallbacks (per rule) — Each rule can list multiple search identifiers. The engine will attempt the first identifier; if it finds no candidate, it will try the next identifier in that same rule, and so on

#### 3. Rules

**Purpose**: Defines how to compare staging entry data with target system transactions

**How It Works:**

* Compares specified fields between staging entries and expected transactions
* All match rules must pass for successful reconciliation
* Supports both standard fields (amount, currency) and custom metadata fields
* Currently supports equals operator

**Matching Logic:**

* Source Field: Data from the staging entry (left side of reconciliation)
* Target Field: Expected data in the target system (right side of reconciliation)
* Validation: Both fields must exist and match exactly

**Flow for a source-type staging entry (creates an expectation)**

1. Find all rules whose filters match the staging entry.
2. Select the single rule with the highest numeric priority.
3. Inside that rule, try the rule’s identifiers in order (e.g., order\_id → merchant\_txn\_id → batch\_id) until one produces candidates.
4. When an identifier returns candidates, create an Expectation (status = EXPECTED) with the chosen columns

**Flow for a target-type staging entry (consumes an expectation)**

1. Find rules whose target account matches the staging entry’s target account.
2. For each matching rule (starting with higher priority), try that rule’s identifiers (in their specified order) to locate candidate Expectations.

For the first matching Expectation found, evaluate the rule’s match\_rules against the target staging entry. If all match\_rules pass, mark the Expectation POSTED and create the atomic Transaction/Entries.

#### 4. Priority-Based Selection

**How It Works:**

* Rule priority selection — When multiple rules’ filters match a staging entry, the engine selects the rule with the highest numeric priority and applies only that rule

