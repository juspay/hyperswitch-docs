---
hidden: true
---

# Workflow

## Workflow

**Workflow** is where Hyperswitch earns its "orchestration" name. Once you have multiple connectors and payment methods, these features decide _how_ each payment behaves — which processor handles it, whether 3DS is triggered, whether a surcharge applies, and whether it's blocked for fraud.

All of these are configured **per Business Profile**. Start with Routing; the rest are optional layers you add as you need them.

This section covers:

* Routing
* Intelligent (Dynamic) Routing
* 3DS Decision Manager
* Surcharge
* Fraud & Risk / Blocklist

***

### Routing

**Routing** decides _which connector_ processes each payment. If you've connected more than one processor, routing is how you put them to work.

#### Routing strategies

| Strategy                      | How it chooses a connector                                   |
| ----------------------------- | ------------------------------------------------------------ |
| **Default / Fallback**        | A fixed priority order — try connector A, then B, then C     |
| **Volume-based split**        | Distribute traffic by percentage (e.g. 70% A / 30% B)        |
| **Rule-based (Advanced)**     | `if` conditions on payment attributes → pick a connector     |
| **Auth-rate / Debit routing** | Optimize based on authorization rates or debit-network rules |

#### Building a rule-based route

1. Go to **Workflow → Routing** and create a new configuration.
2. Add conditions on attributes like **amount, currency, country, payment method, or card network**.
3. Point each condition at a **connector (or ordered list of connectors)**.
4. **Activate** the configuration — only one routing config is active per profile at a time.

#### Managing configurations

* Only **one active** routing config runs at a time; others are saved as drafts.
* **History** lets you see previously active configs and switch back.
* Test a new strategy in **Test mode** before activating it in Live.

> 💡 A simple, reliable start: set a **Default** route with your primary connector and one fallback. Add advanced rules later as you learn your traffic.

***

### Intelligent (Dynamic) Routing

**Intelligent Routing** goes beyond static rules — it uses live **success-rate data** to automatically send each payment to the connector most likely to approve it.

* **Success-rate based** — continuously favors the best-performing connector for the given conditions.
* **Reduces failed payments** without you hand-tuning rules.
* Enable it from the routing area and let it optimize; monitor the impact in **Analytics**.

> Think of static Routing as _rules you write_ and Intelligent Routing as _rules the system learns_. Many teams run a baseline route and let Intelligent Routing optimize within it.

***

### 3DS Decision Manager

The **3DS Decision Manager** controls when **3D Secure authentication** is triggered. Good 3DS strategy balances fraud protection against checkout friction.

* Write **rules** for when to request 3DS — e.g. based on amount, currency, country, or card network.
* Choose to **request**, **skip**, or apply **exemptions** where regulation allows.
* Works together with your connected **3DS / Authentication processor** (see Connectors).

#### 3DS Exemption Manager

A related tool lets you apply **exemptions** (e.g. low-value or low-risk transactions) so eligible payments skip the 3DS challenge while staying compliant. Use it to cut friction on transactions that qualify.

> ⚖️ 3DS rules interact with regional regulation (like SCA in Europe). Configure conservatively and validate with your acquirer.

***

### Surcharge

**Surcharge** lets you add a fee to certain transactions — for example, a percentage on credit-card payments where it's permitted.

* Define **surcharge rules** by payment method, card network, or other conditions.
* Set the surcharge as a **fixed amount or percentage**.
* The surcharge is calculated and applied during payment, and pairs with a **Surcharge processor** (see Connectors).

> Surcharging is regulated in many regions. Confirm what's allowed for your business before enabling it.

***

### Fraud & Risk / Blocklist

Protect yourself from bad transactions before they cost you.

* **Fraud & Risk** connects a fraud-screening provider (see Connectors) and lets payments be evaluated and acted on based on risk.
* **Blocklist** lets you manually block specific values — card fingerprints, customer identifiers, or other attributes — so matching payments are rejected outright.

Use the Blocklist for known-bad actors, and a Fraud & Risk processor for automated, scored screening at volume.

***

### Where to go next

* **Connectors** → several workflow features need a matching processor (3DS, Surcharge, Fraud & Risk).
* **Analytics** → measure the impact of routing and 3DS changes on success rates.
* **Operations → Payments** → inspect a payment's **attempts** and **timeline** to see routing in action.
