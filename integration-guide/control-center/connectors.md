---
hidden: true
---

# Connectors

## Connectors

**Connectors** are the integrations that actually move money — payment processors like your acquirer or gateway, plus specialized processors for fraud, tax, 3DS, and more. Connecting at least one **payment processor** is what turns your account from empty into functional.

Remember: **connectors are attached at the Business Profile level.** Make sure you're on the right profile and mode before you begin — see Getting Started.

This section covers:

* Connect a payment processor
* Configure payment methods (PMTs)
* Other processor types

***

### Connect a payment processor

The **Connectors → Payment Processors** screen lists everything you've connected and lets you add more.

#### Adding a processor

1. Go to **Connectors → Payment Processors → + Connect**.
2. **Pick your processor** from the list of supported connectors.
3. Choose the **environment** — Test (sandbox credentials) or Live (production credentials). This should match your current mode.
4. **Enter credentials** — API keys, secrets, and any processor-specific fields.
5. **Select the payment methods** you want to enable through this processor (cards, wallets, bank transfers, BNPL, etc.).
6. **Save**. The connector becomes active and is now eligible to process payments for this profile.

#### Tips

* **Test first.** Connect in Test mode, run a payment, confirm success, _then_ repeat with live credentials.
* **Multiple connectors** for the same profile are normal — that's what enables **Routing** (see the Workflow section) to choose the best one per transaction.
* **Credentials live per profile.** The same processor connected under two profiles is two separate connector records.

> 🔐 Credentials are stored securely. Anyone with access to the profile can _use_ a connector, but editing keys should be restricted via **Roles** — see the Settings section.

***

### Configure payment methods (PMTs)

Connecting a processor makes it _available_; **Configure PMTs** decides _which payment methods are actually offered_ to your customers and how.

On the payment-method configuration screen you can:

* **Enable / disable** methods per connector — cards, wallets (Apple Pay, Google Pay, etc.), bank debits/transfers, BNPL, and more.
* Set **acceptance rules** such as which card networks or currencies a method applies to.
* Control how methods surface in the checkout / SDK.

> A payment method only works if **(a)** the connector supports it **and (b)** you've enabled it here. If a method isn't showing up at checkout, this screen is the first place to check.

***

### Other processor types

Beyond payment processors, the Connectors section supports specialized processors. You only need the ones relevant to your setup.

| Processor type           | What it does                                                   |
| ------------------------ | -------------------------------------------------------------- |
| **Payment Processor**    | Core acquiring/gateway that charges the customer               |
| **Payout Processor**     | Sends money _out_ to recipients (powers the Payouts screen)    |
| **Fraud & Risk**         | Screens transactions for fraud before/after authorization      |
| **3DS / Authentication** | Handles 3D Secure authentication for cards                     |
| **PM Auth Processor**    | Payment-method authentication (e.g. bank account verification) |
| **Tax Processor**        | Calculates tax on transactions                                 |
| **Billing Processor**    | Handles subscription / recurring billing                       |
| **Surcharge Processor**  | Applies surcharges to transactions                             |
| **Vault Processor**      | Securely stores and tokenizes payment credentials              |

Each is connected the same way as a payment processor: pick it, choose environment, enter credentials, save. Several of these pair with a **Workflow** feature — for example, the 3DS processor is driven by the **3DS Decision Manager**, and the Surcharge processor by **Surcharge** rules.

***

### Where to go next

* **Configure PMTs** above — turn on the methods your customers will use.
* **Workflow** → route across your connected processors and add 3DS, surcharge, and fraud rules.
* **Operations → Payments** → watch transactions flow through the connectors you just set up.
