---
description: Ensure compliance with seamless payments
---

# Regulatory compliance

Gaming merchants operate under some of the strictest payments compliance regimes in the world. Three patterns in particular show up across regulated markets, and Juspay’s compliance workflows address each.

### Credit card blocking for regulated markets

On 14 April 2020, the UK Gambling Commission banned the use of credit cards for gambling under LCCP Licence Condition 6.1.2. Similar bans now apply in Australia (effective 11 June 2024, under the Interactive Gambling Amendment (Credit and Other Measures) Act 2023, enforced by the ACMA) and Ireland (Gambling Regulation Act 2024, signed 23 October 2024; provisions are being commenced in phases by the Gambling Regulatory Authority of Ireland). For merchants operating in these markets, every credit card transaction is a regulatory liability - and the ban extends not just to manually-entered cards but to credit cards stored inside Apple Pay, Google Pay, PayPal balance, and any other wallet that may proxy a credit card behind a token.

Juspay handles this with a single dashboard toggle, applied per business profile:

* Block credit cards - refuses any card whose BIN resolves to card\_type = credit
* Block credit-card-backed wallet tokens - for Apple Pay and Google Pay, inspects the underlying funding source returned in the device payment token and blocks if it is a credit card; for PayPal, requires the funding source to be balance, debit card, or bank transfer
* Show inline messaging - the cashier UI surfaces the restriction in player-friendly language before the player attempts the deposit

The result: a fully compliant cashier where credit cards never reach authorization, even when proxied through a digital wallet.

<figure><img src="../../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

### Closed-loop withdrawals (net deposit)

Anti-money-laundering regulations across the UK, EU, Canada, and Australia require that withdrawals from a gaming account return to the same payment instruments that funded the deposits - and only up to the amount actually deposited from each source. This is the closed-loop principle (also called the net deposit rule). A player who deposits £100 via Visa and £50 via PayPal cannot withdraw £150 to a brand-new bank account; the £150 must split between the Visa card and the PayPal account.

Juspay’s role here is deliberately scoped, and it matters. Juspay validates closed-loop eligibility; the merchant decides the split. The operator’s ledger and AML logic - which already track KYC tier, net deposit per source, source-of-funds declarations, and player risk - are the right place for the allocation decision. Juspay accepts the split as input and enforces eligibility on each leg. This keeps the regulatory decision inside the operator’s compliance perimeter rather than buried inside a third-party black box, and it means the merchant can demonstrate the AML logic directly during audit.

The full flow when a withdrawal is initiated:

1. Merchant-controlled split. The merchant submits a withdrawal request specifying how the amount is allocated across one or more of the player’s deposit instruments - based on its own ledger, KYC rules, and net-deposit tracking.
2. Closed-loop validation. Juspay checks that every requested payout destination is an instrument the player has previously deposited from. Any leg targeting an unrecognized instrument is rejected before authorization.
3. Rule-based routing per leg. For each leg of the split, Juspay’s Smart Router for Payouts selects the appropriate rail based on the merchant’s configured payout rules - e.g., Visa Direct for card payouts, PayPal payout for PayPal balance, Trustly refund for bank-transfer originated deposits.
4. Cascading retries on retriable failures. If a payout leg fails for a retriable reason (acquirer-side soft decline, connector timeout, recoverable network error), Juspay automatically re-attempts the leg through the next eligible connector in the configured cascade. Method consistency is preserved - a failed bank transfer is retried as a bank transfer, not as a card payout.
5. Failure handling. Non-retriable failures and closed-loop-ineligible requests are surfaced back to the merchant via webhook with an explicit error code, so the operator’s withdrawal queue can hold them for manual review or trigger an alternate workflow.

<figure><img src="../../.gitbook/assets/image (9).png" alt=""><figcaption></figcaption></figure>

The closed-loop logic ensures that only payment methods approved as deposit instruments can be used for withdrawals - eliminating a common AML failure mode where a merchant accidentally allows a player to deposit via card and withdraw to a third-party bank account.



<br>
