---
description: Check payment eligibility before deposit
---

# Real time Eligibility Checks

A gaming merchant operating in 20+ markets cannot accept every card the world has issued. Some BINs are blocked by issuers from gambling MCC (4829, 7995). Some issuers in some countries are high-risk for the merchant’s acquirer routing. Some card types - prepaid, virtual, corporate - are explicitly off-limits under the merchant’s risk policy or regulation. The question is not whether to enforce these constraints, but when.

The naïve answer is to enforce them at authorization: let the player enter card details, submit, fail at the PSP, then handle the error. This is the worst possible UX. The player has invested time, expectation, and emotion, and the merchant is now telling them their card was rejected - without explaining why, without offering an alternative, and without any guarantee they’ll come back to try again. A failed deposit at the moment of intent is one of the most damaging conversion events an operator can put in front of a player - they have invested attention and emotion, and a generic error message rarely brings them back to retry.

Juspay’s Card Eligibility Engine moves the check to the moment the card details are entered - before the player presses “Deposit.”<br>

<figure><img src="../../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

Here's an example of inline card-not-accepted messaging at point of entry, allowing the player to switch payment method without ever experiencing a failed authorization:

<figure><img src="../../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

### What can be restricted

Juspay’s Card Eligibility Engine supports restrictions on four dimensions, applied individually or combined:

* Card BIN (first 6 digits) and extended card BIN (first 8 digits) - block specific issuer ranges
* Card issuer (named) - block named banks regardless of BIN range
* Issuer country - block cards issued in specified countries
* Card type - block credit, debit, prepaid, corporate, or consumer cards independently

These restrictions are dashboard-configurable under Settings → Card Restrictions (and via the /blocklist API for programmatic control). Restrictions can be set per business profile, so a merchant operating multiple jurisdictions can run different rules per market without redeploying code.

### High-risk BIN handling

Beyond outright blocks, Juspay supports risk-tiered BIN handling. High-risk or historically low-approval BINs can be:

* Routed to an alternative PSP that performs better on that BIN range
* Step-up retried with 3DS challenge if the first no-3DS attempt declines
* Surfaced with a soft warning to the player (“Your card may be charged a fee by your issuer for this merchant category”)
* Blocked entirely if approval rates fall below a configurable threshold

The BIN tier list is editable in the dashboard and can be updated as risk results change over time. Juspay’s analytics module shows per-BIN approval rate, chargeback rate, and lifetime value, so the eligibility configuration is a live decision, not a static one.

<br>
