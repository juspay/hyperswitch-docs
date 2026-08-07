---
description: Smarter 3DS decisioning for deposits
---

# 3DS

3D Secure is the largest lever in iGaming deposit conversion. Applied universally, it taxes every deposit with friction and pushes drop-off rates into double digits. Applied too leniently, the merchant absorbs chargebacks and loses 3DS-conferred liability shift on fraud. Juspay’s 3DS Intelligence Engine (the 3DS Decision Manager and standalone 3DS server) lets merchants apply 3DS surgically - challenge where it matters, skip where it doesn’t.

### The gaming-specific decision pattern

In iGaming, the bulk of deposit volume comes from returning players paying with a card-on-file (COF). These players have a transaction history with the merchant, they've passed prior fraud checks, and the issuer is highly likely to authenticate them frictionlessly anyway. Forcing a challenge flow on every COF deposit creates friction without reducing fraud meaningfully.

Fresh-card transactions are the opposite. A first-time card on a fresh account is the highest-risk profile an iGaming merchant sees – and exactly where 3DS challenge delivers the strongest fraud reduction and liability shift.

Juspay's 3DS Decision Manager lets merchants express this kind of logic – and several others – as configurable rules, applied per business profile.

**Common rule patterns in iGaming deployments:**

* **Fresh-card vs COF.** Force challenge on the first transaction from a new card; allow frictionless or no-3DS for tokenized COF that has passed FRM screening.
* **Smart exemption requests in SCA markets.** In EEA and UK profiles, request Low-Value Exemption for deposits under €30, Transaction Risk Analysis for traffic under the acquirer's fraud threshold, and Trusted Beneficiary when the player has whitelisted the operator. The issuer makes the final call; the merchant decides which exemption is worth requesting.
* **Market-aware 3DS enforcement.** PSD2-regulated profiles (EEA, UK) request 3DS by default and configure exemptions selectively. Non-PSD2 profiles (US, Canada, Australia) opt into 3DS only for high-risk segments – fresh cards, high-value transactions, geo-mismatched traffic – treating it as a fraud lever, not a compliance one.
* **Amount-threshold escalation.** Always challenge above a configurable amount (commonly €500 / £500 / $500 for mid-market operators), regardless of COF status. Protects the operator's fraud exposure on high-value deposits without taxing the long tail.
* **FRM-score routing.** Inbound FRM risk score above a threshold forces challenge; below the threshold, request an exemption or skip 3DS where the market allows. Lets the operator's fraud engine and 3DS engine work as one system rather than two independent checks.
* **Payment-method awareness.** Rules recognize the underlying payment method – PIX, UPI, Trustly, Sofort, and other A2A rails skip the 3DS branch entirely, since 3DS is a card-network concept.

Below is an example of a real time evaluation of 3DS strategy during the deposit initiation:

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

Each rule is keyed off the same payload fields – card BIN, card type, card network, billing country, business country, amount, currency, capture method, payment method, customer transaction history, and custom metadata – and can combine via AND/OR operators. Rules are versioned, applied per Profile, and changeable from the dashboard without a release cycle.

### 3DS Cascading: step-up and silent retries

Juspay’s 3DS Cascading pattern combines smart retries with standalone 3DS authentication, turning declined deposits into recovered revenue without forcing the player to re-authenticate. Two distinct retry shapes operate under the same umbrella.

**Step-up retries.** When a deposit is declined for a soft-fraud reason (typical issuer responses: do\_not\_honor, generic\_decline), Juspay’s Smart Retries engine automatically re-attempts the transaction with a 3DS challenge added - converting a declined no-3DS attempt into an authenticated transaction that the issuer will approve. This is one of the highest-leverage retry configurations a gaming merchant can adopt: it recovers transactions that would otherwise have been hard declines, and it shifts fraud liability to the issuer on the retry. The player sees one 3DS prompt and the deposit completes; the alternative was a flat decline and a possible drop-off.

**Silent retries across PSPs.** When a deposit fails for a processor-specific reason rather than a fraud reason - an acquirer-side decline, a soft network error, a connector timeout, a “do\_not\_honor” from a particular acquirer that has nothing to do with the cardholder - Juspay silently re-attempts the same transaction through a different PSP in the merchant’s configured cascade. The player sees no spinner, no challenge prompt, no second attempt; the retry is invisible. This works because Juspay separates authentication from authorization: a successful 3DS authentication produces a cryptogram that can be submitted to any PSP that accepts external 3DS data. The cardholder authenticates once; Juspay then authorizes across multiple processors in sequence, reusing the same authentication, until one succeeds. For high-frequency iGaming deposit traffic, where PSP-specific decline patterns differ meaningfully across acquirers, silent multi-PSP cascading is often the single biggest deposit-SR lever available.

<figure><img src="../../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

### Easy Dashboard configuration

Rules are configured in the Juspay Control Center under **Workflows → 3DS Exemption Manager**, which presents the merchant's complete 3DS rule set for a given Business Profile as an ordered list. Each rule is a condition expression paired with an authentication action. The engine evaluates the list top-down at transaction time: the first rule whose condition matches the incoming payment wins, and its action is applied. A default fallback at the bottom catches transactions that match no explicit rule.

Conditions are built from boolean operators (`AND`, `OR`) and comparison operators (`is`, `is_not`, `contains`, `greater_than`, `less_than`), and can reference any field on the payment payload – **BIN range**, **card type,** **card network**, **issuer country**, **billing country**, **business country**, **amount**, **currency**, **capture method**, **payment type** (one-time vs. recurring), **card discovery method** (manual vs. saved card), **customer device platform** and **type**, **FRM risk score**, and any **custom metadata** the merchant sets on the payment. Conditions can be nested, so a single rule can encode something like _(amount > 100 AND currency = USD) OR card\_type = credit_. Matching actions apply one of the engine's authentication outcomes: mandate a 3DS challenge, request no-3DS, request a specific SCA exemption (Low Value, TRA, MIT, or Trusted Beneficiary), or pass through frictionless.

Rules are scoped per Business Profile, so the UK, German, and Ontario Profiles each carry their own ordered ruleset and can diverge without affecting one another. Every change is versioned with a full audit trail; new rules can be tested against historical traffic before going live, and the same configuration is editable via the routing API for merchants who prefer to manage rules as code.

<figure><img src="../../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>
