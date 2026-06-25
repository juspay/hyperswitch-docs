# FAQs

#### **Who manages cashier functions outside of payments — player accounts, wallet balances, bonus engines, KYC, responsible-gaming controls?**&#x20;

Juspay handles the payments surface: deposit authorization, 3DS, card eligibility, payout routing, retries, vault, analytics. The non-payments surfaces of an iGaming cashier — Player Account Management (PAM), player wallet balance and ledger, bonus and promotion engines, KYC and AML player-side onboarding, responsible-gaming limits, self-exclusion enforcement, game session and bet history — sit with the operator's existing systems or with specialist PAM providers (Derivco, EveryMatrix, OpenBet, in-house). Juspay integrates with these via webhooks and APIs: deposit success events update the wallet ledger; closed-loop validation reads from the deposit history maintained by the operator; responsible-gaming deposit limits are enforced by the operator's pre-payment hook before Juspay sees the transaction. The operator owns the player relationship; Juspay owns the rails.

#### **Does the Suite support integrated fraud-service flows alongside payments?**&#x20;

Yes — and this is where Juspay's orchestrator model does more than a typical PSP integration. FRM providers (Signifyd, Riskified, Cybersource Decision Manager, Stripe Radar, or the operator's in-house FRM) are integrated as connectors into the same orchestration runtime that handles payments. A single deposit transaction triggers one orchestrated flow: FRM scoring → 3DS decision (keyed off the FRM score) → routing → authorization → settlement, with shared transaction signals and shared analytics across every step. This means the 3DS Decision Manager can route on FRM risk-score thresholds, the Smart Router can deprioritize PSPs that produce high chargeback rates against a given FRM segment, and analytics show fraud and payment outcomes in one dashboard rather than two disconnected ones. Pre-authorization FRM, post-authorization FRM, and chargeback-management flows are all supported.

#### **Can I keep full control over the cashier UI?**&#x20;

Yes. There are three integration patterns, and the last two give the merchant full UI control:

* **Headless SDK** — the merchant builds every UI component; the SDK is API-only on the client and handles tokenization, 3DS challenge orchestration, and redirects under the hood. Card data is routed by the SDK directly to Juspay's vault, so the merchant stays out of PCI scope despite owning the entire UI.
* **Server-to-server with the Cards SDK** — the merchant owns the UI and the backend integration with Juspay's REST APIs; only the card-input field is iframed via the Cards SDK. Same SAQ A scope, more backend work, maximum decoupling from third-party JavaScript.
