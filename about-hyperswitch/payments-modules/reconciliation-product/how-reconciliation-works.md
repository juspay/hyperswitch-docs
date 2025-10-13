# How Reconciliation Works

{% hint style="info" %}
**Note**:

For Reconciliation V1, please check [here](../reconciliation/).

We will continue to support Reconciliation V1 for all existing merchants. With the launch of V2, reconciliation is now a configurable experience — merchants will have the choice to continue with V1 or opt into V2 directly from the dashboard

All your existing configurations and setups will seamlessly carry over to V2 with no additional effort required on your end. We recommend beginning the transition to Reconciliation V2 to take advantage of the latest features.
{% endhint %}

### Reconciliation Engine: Rule-Based Architecture

The Reconciliation Engine is the intelligent core that automatically matches and validates financial data. It does this by evaluating incoming **Staging Entries** against a set of configurable business rules. These rules dictate how transactions are processed and matched, providing the flexibility to handle complex reconciliation scenarios without code changes

#### The Complete Flow

The reconciliation process follows a robust, end-to-end flow to ensure that every transaction is accounted for

1. **Staging Entry Processing**: After a file has been ingested and transformed, all standardized data becomes a **Staging Entry**. This is a temporary, validated but unreconciled record waiting for processing by the engine
2. **Rule Evaluation**: The reconciliation engine continuously evaluates each new staging entry against your configured business rules to determine the appropriate action
3. **Expectation Creation**: When a rule matches a staging entry, the system creates an **Expectation**. An expectation is a record that defines what a corresponding transaction should look like from a target system
4. **Transaction Matching**: As new transactions are ingested, they are automatically matched against existing expectations to complete the reconciliation process
5. **Exception Highlighting**: The engine automatically flags and categorizes any unmatched staging entries. These exceptions can be due to amount discrepancies, status conflicts, or any metadata mismatch defined in your rules
6. **Exception Handling**: Operators can resolve exceptions via the UI. Every action is auditable and triggers an automatic re-evaluation to post the transaction correctl

<figure><img src="../../../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

### Rules Architecture

Each rule consists of three core components that work together to define your matching logic:

1. **Filters**: Determines which staging entries a rule should apply to
2. **Identifiers**: Defines the unique fields used to find a matching transaction
3. **Rules**: Specifies the conditions that must be met for a successful match

<figure><img src="../../../.gitbook/assets/Screenshot 2025-09-10 at 2.20.42 PM.png" alt="Image showing rules setup in the reconciliation product"><figcaption></figcaption></figure>

#### **1.**&#x46;ilters: Defining the "When"

**Purpose**: Determines which staging entries a rule should process. It's the first condition that must be met for a rule to be considered

* **How It Works**: The engine evaluates staging entry data against specified conditions. Only staging entries that satisfy the trigger will be processed by this rule
* **Key Capabilities**:
  * Supports field extraction from both standard fields and nested metadata.
  * Multiple trigger operators are available, such as `equals` and `not_equals`
* **Example Scenarios**:
  * `"Apply this rule to all transactions over $1000"` (triggered on amount range)
  * `"Use this rule for a specific merchant ID"` (triggered on `merchant_id`)

#### **2.** Identifiers: Defining the "How"

**Purpose**: Defines which fields to use for finding a matching transaction in a target system. This is what allows the engine to link a staging entry (e.g., from an Order Management System) to a transaction expectation (e.g., from a Payment Service Provider)

* **How It Works**:
  * Maps a source staging entry field (e.g., `order_id`) to a target system's search criteria (e.g., `original_reference`)
  * The engine uses the identifier to create a searchable **Search Expectation**. When a new staging entry arrives from a different source, the engine uses the same identifier to look up a potential match
* **Fallbacks**: You can specify multiple identifiers in order of preference. The engine will try the first identifier, and if it fails to find a match, it will move to the next one

#### **3.** Rules: Defining the "What"

**Purpose**: Rules are the final validation step. Once a potential match has been identified, these rules compare specific fields to confirm that the transactions are a valid pair

* **How It Works**: The engine compares the data from the source staging entry with the data from the potential target transaction. All match rules must pass for a successful reconciliation
* **Matching Logic**:
  * **Source Field**: Data from the staging entry (the left side of the reconciliation)
  * **Target Field**: Expected data in the target system (the right side of the reconciliation)
  * **Validation**: Both fields must exist and match exactly according to the rule's criteria

#### Priority-Based Selection

**How It Works**: When multiple rules' filters match a single staging entry, the engine selects the rule with the highest numeric priority and applies only that rule. This ensures that the most specific or important rules are always executed first.

### Transaction Processing Modes

The reconciliation engine operates in two distinct modes, depending on the type of staging entry being processed

#### **Transaction Mode**

This mode is for initial entries that act as the **source of a flow**. The goal is to create a new, double-entry transaction and define what is expected from a counterparty

1. **Incoming Staging Entry**: A staging entry (e.g., a customer order) is ingested
2. **Rule Application**: The engine finds the highest-priority rule with a matching filter
3. **Transaction Creation**: A new **Transaction** is created. This transaction is atomic, meaning all its entries succeed or fail together
4. **Entry Generation**: The transaction includes:
   * A **Direct Entry** for the source staging entry (e.g., a credit entry to the `Orders` account).
   * An **Expected Entry** for each target, which represents the money you are waiting to receive or pay out (e.g., a debit entry to the `PSP` account).
5. **Search Expectation**: A searchable **Search Expectation** is generated, linking the source entry to the expected entry for future matching

**Confirmation Mode**

This mode is for subsequent entries that confirm a previous transaction and allow the engine to complete the reconciliation flow

1. **Incoming Staging Entry**: A staging entry arrives from a counterparty (e.g., a PSP payment confirmation)
2. **Expectation Search**: The engine uses the configured identifiers to search for an existing, `EXPECTED` entry in the system
3. **Validation**: Once a match is found, the engine evaluates the rule's match rules to ensure the fields (e.g., amounts, currencies) are consistent
4. **Transaction Evolution**: If all match rules pass, the transaction is **evolved**. A new version of the transaction is created, marking the `EXPECTED` entry as **POSTED**. The old version is archived, preserving a complete, immutable audit trail
5. **Final Balance Update**: The system's balances are updated to reflect the posted transaction, moving the money from the `EXPECTED` to the `POSTED` state

