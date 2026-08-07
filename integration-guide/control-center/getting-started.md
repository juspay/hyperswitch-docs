# Getting Started

## Getting Started with the Control Center

The **Control Center** is Hyperswitch's no-code dashboard. It sits on top of the Hyperswitch payments engine and lets your team connect processors, run and monitor payments, configure smart routing, manage refunds and disputes, and administer users — all without writing code.

This guide gets you from _"I just logged in"_ to _"I understand what I'm looking at and made my first test payment."_

***

### What is the Control Center?

| If you are a…            | You'll mostly use…                                        |
| ------------------------ | --------------------------------------------------------- |
| **Operations / Support** | Payments, Refunds, Disputes, Customers                    |
| **Developer**            | API Keys, Webhooks, Payment settings                      |
| **Admin / Owner**        | Connectors, Routing workflows, Team & Roles, Org settings |

***

### Step 1 — Log in and pick your environment

1. Open the Sandbox Control Center URL [https://app.hyperswitch.io/](https://app.hyperswitch.io/) and **sign up**.
2. On first sign-up your **Organization** and a **Merchant account** are created for you&#x20;

{% embed url="https://scribehow.com/o/qzpN4gAaRXWhBwFWaO3hnQ/viewer/How_To_Create_A_New_Hyperswitch_Dashboard_Account__lHF-8nuFRhekl36qQnEYRw" %}

#### Test vs. Live mode

* **Test / Sandbox** — a safe playground. Use test card numbers, no real money moves. Start here.
* **Live** — real processors, real money. Enabled after you've tested your setup.

You'll be taken to Test mode by default. Access to Production mode is granted only after the required agreements have been signed

***

### Step 2 — Understand the account hierarchy

This is the concept new users trip on the most. Everything in the Control Center is scoped to a three-level hierarchy:

```
Organization              ← your company (top-level tenant)
  └── Merchant Account     ← a business/brand under the org
        └── Business Profile ← an environment or product line
              ├── Connectors      (processors are attached here)
              ├── Payments
```

* **Organization** — the top-level account for your company.
* **Merchant Account** — a business unit under the organization. Larger companies may have several. API keys are under Merchant Account
* **Business Profile** — the level where you actually attach **connectors, routing logic** process **transactions**. A merchant can have multiple profiles (e.g. one per region, brand, or product line).

Refer the below guide to understand how to create a new Profile and rename Merchant/Profiles

{% embed url="https://scribehow.com/o/qzpN4gAaRXWhBwFWaO3hnQ/viewer/How_To_Create_A_New_Merchant_Profile_In_Hyperswitch__JTMVn-g1RjOqDDl5QM1KDA" %}

You switch between merchants and profiles using the **switcher** near the top of the sidebar. **Connectors and settings live at the profile level**, so if a connector "disappears," confirm you're on the right profile.

***

### Step 3 — Take the dashboard tour

The left sidebar is grouped into sections you'll return to constantly:

| Section             | What lives there                                       |
| ------------------- | ------------------------------------------------------ |
| **Overview / Home** | Snapshot of volume, success rate, recent activity      |
| **Operations**      | Payments, Refunds, Disputes, Customers, Payouts        |
| **Connectors**      | Payment processors and payment-method configuration    |
| **Analytics**       | Insights, charts                                       |
| **Workflow**        | Routing, 3DS Decision Manager, Surcharge, Fraud & Risk |
| **Vault**           | Stored customers and tokens                            |
| **Developers**      | API Keys, Webhooks, Payment settings                   |
| **Users(top left)** | Team & roles, Invites                                  |
| **Theme(top left)** | Configure control center to your branding              |

#### Exploring other product modules

{% embed url="https://scribehow.com/o/qzpN4gAaRXWhBwFWaO3hnQ/viewer/Exploring_Modular_Products__HIKCmkFETpSWDpW5zNjVSw" %}

Hyperswitch is more than payments. Alongside the sections above, the dashboard gives you direct access to the wider **product suite**:

| Module                             | What it's for                                                    |
| ---------------------------------- | ---------------------------------------------------------------- |
| **Orchestrator**                   | The core payments dashboard (everything described in this guide) |
| **Vault(part of Orchestrator)**    | Secure storage and tokenization of payment credentials           |
| **Recon(available on request)**    | Automated reconciliation for finance teams                       |
| **Revenue Recovery(Demo mode)**    | Recover failed and churned payments                              |
| **Cost Observability(Demo mode)**  | Visibility into your payment processing costs                    |
| **Intelligent Routing(Demo mode)** | Success-rate–based dynamic routing                               |

You can jump into any of these straight from the dashboard.

> 🆕 **First-time visitors:** the first time you open a module, the Control Center automatically **creates a merchant account for you** for that product so you can start exploring immediately — no manual setup required. Each module is scoped to its own account under your organization, so you can try one without affecting the others.

***

### Step 4 — Make your first test payment

{% embed url="https://scribehow.com/o/qzpN4gAaRXWhBwFWaO3hnQ/viewer/Make_your_first_test_payment__yq92BXFUSbaDhiIOTSgd6w" %}

The fastest way to see the dashboard come alive:

1. Go to **Connectors → Payment Processors** and connect a test processor (a dummy/test connector works).
2. Go to **Overview -> Try It Out** to open the checkout SDK
3. Use the **test card details** for making a payment
4. Go to **Operations → Payments** and watch your payment appear. Click it to explore the payment details, timeline, and available actions (capture, refund).

***

### Where to go next

* **Operations** → day-to-day management of payments, refunds, and disputes.
* **Connectors** → connect real processors and enable payment methods.
* **Workflow** → set up routing and smart-payment features.
* **Developers** → API keys and webhooks for your integration.
* **Users** → invite your team and manage roles.

> 💡 **New-user tip:** If something looks empty or wrong, check the two things that scope everything — your **mode (Test/Live)** and your **selected merchant/profile**.
