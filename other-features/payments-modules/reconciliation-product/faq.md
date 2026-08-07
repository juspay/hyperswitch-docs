# FAQ

### Table of Contents

* File Ingestion & Formats
* Matching & Reconciliation Logic
* Exceptions & Mismatches
* Reporting & Visibility
* Configuration & Control
* Data Integrity & Security
* Operational

***

### File Ingestion & Formats

#### How do we handle file time/timezone differences (bank file cutoff vs. our processing time)?

We standardize all files to a single timezone so that the UI is easy to use and consistent across sources.

#### Does it matter what time a file arrives, or do we need to align with a bank's cutoff?

Our engine is always running, so files arriving at different times doesn't matter — we pick them up as they arrive and reconcile them against the created expectations.

#### When can exceptions happen during reconciliation?

An exception (flagged for manual review) can occur when:

* No matching rule applies to an entry
* A currency mismatch is detected
* A required field is missing
* A duplicate entry is detected
* No matching expectation is found, or multiple conflicting expectations are found
* An amount, balance-direction, or metadata mismatch is found against the expected transaction

#### What report formats do we support for output/export?

Our reports are set up custom for merchants based on the ask. We support CSV and Excel-based reporting out of the box, and can accommodate other formats on request.

#### How does reconciliation work when there's a single consolidated bank deposit covering multiple transactions?

We support grouping many individual source transactions and matching them together as a set against one consolidated deposit on the bank side (many-to-one matching).

#### What's the maximum file size we support per upload?

Up to 25MB per manual upload.

#### How do we handle duplicate files or duplicate rows within a file?

Duplicate rows — based on your configured unique field — are automatically detected and routed to manual review rather than being silently processed twice.



#### Can we ingest files via SFTP/API/manual upload?

Yes, three methods are supported:

1. Automated PSP webhook ingestion
2. Secure managed file-drop ingestion (SFTP-style)
3. Manual upload through the dashboard
4. API based fetch from PSP

#### What happens if a file fails schema validation — is it rejected entirely or partially processed?

Processing is partial and row-level. Valid rows are still processed even if other rows in the same file have errors — failing rows are reported individually instead of blocking the entire file.

***

### Matching & Reconciliation Logic

#### What matching strategies are used (1:1, 1:many, many:1, many:many)?

All standard patterns are supported:

* **One-to-one** — a single source entry matched to a single expected entry
* **One-to-many** — one source split across multiple expected entries (e.g., a payment split into principal + fees)
* **Many-to-one** — many source entries aggregated into one consolidated deposit
* **Many-to-many** — batch settlement matching
* **One-to-many across accounts** — one source entry reconciled against multiple destination accounts (e.g., marketplace payouts)

#### How are partial payments or split settlements reconciled?

If a settlement arrives in multiple parts, the remaining balance is tracked and the expectation stays open until fully matched. It's only flagged as a mismatch if the total ends up over- or under-paid relative to what was expected.

#### Can matching rules be customized per merchant/processor/bank?

Yes. Rules, trigger conditions, and field mappings are fully configurable per business profile and per account, so different banks or processors can each run their own independent logic.

***

### Exceptions & Mismatches

#### What are all the categories of exceptions the system can raise?

* No matching rule found
* Currency mismatch
* Missing required field
* Duplicate entry
* No matching expectation found / multiple conflicting expectations found
* Amount mismatch
* Balance-direction mismatch
* Metadata mismatch
* Split mismatch
* Over-payment / under-payment

#### How are exceptions routed for manual review — is there a queue/workflow?

Flagged items appear in a filterable list (by status) in the dashboard, each with suggested resolution actions.

#### Can exceptions be auto-resolved after a grace period, or do they always need human action?

Exceptions always require an explicit resolution action (force reconcile, edit, void, link entries, etc.). The one exception to this is that a late-arriving matching entry can still naturally confirm an open expectation without manual intervention.

#### How far back can we re-run reconciliation to catch late-arriving matches?

There's no fixed lookback window. Open expectations remain open indefinitely, so a late-arriving file can still match against an older expectation whenever it shows up.

#### What audit trail is kept when someone manually resolves an exception?

Every resolution preserves the prior state, requires a reason where applicable, and records who made the change. The full history is viewable as a chronological activity timeline.

#### Can we set custom thresholds for what counts as a mismatch (e.g. tolerance)?

Yes — a configurable amount tolerance band (lower/upper bound) is supported.

***

### Configuration & Control

#### Can each merchant/legal entity have its own reconciliation config (skip rules, transformation rules)?

Yes. Transformation rules, skip rules, and matching rules can all be configured independently per merchant, business profile, and account.

#### Can we reconcile against multiple banks/PSPs simultaneously in one run?

Yes. Multiple accounts, rules, and even multiple destination banks (for split payouts) can all be processed concurrently.

#### How are certain records filtered or excluded from a reconciliation run?

Skip rules can be configured by row number or by field-value conditions, so certain rows are filtered out and never enter the system in the first place. Records that have already been processed, voided, or archived are automatically excluded from being reconciled again.

***

### Data Integrity & Security

#### How is PII/sensitive data in uploaded files masked or secured?

Transaction metadata is encrypted at rest by default, using merchant-specific keys. Specific fields can be explicitly opted in as unencrypted only if needed for search or reporting — everything else remains encrypted.

#### What happens to a file after processing — is it purged, archived, or retained?

Files are retained and remain re-downloadable — there's no automatic purge or archival step after processing today.

#### Is there role-based access control over who can view/resolve exceptions?

Access is scoped and permissioned per business profile, with separate read/write permissions. Formal named roles (e.g. analyst vs. approver) are managed at the account/user-management layer — reach out to your account team to discuss specifics.

***

### Operational

#### What's the expected turnaround time from file upload to reconciliation completion?

Typically on the order of seconds once a file has been ingested and queued for processing.

#### What happens if reconciliation fails midway (partial run) — do we get a consistent retry/resume?

Yes. Each entry's processing is all-or-nothing — there's no partially-applied state. Failed entries are clearly flagged for review, and a single failure doesn't block the rest of the batch from processing.
