# Developers

## Developers

The **Developers** section is the bridge between the dashboard and your code. It's where you get the **API keys** that authenticate your integration, set up **webhooks** so your systems hear about payment events, and tune **payment settings** that govern how payments behave.

Everything here is scoped to a **Business Profile** and to your current **mode (Test/Live)**

This section covers:

* API Keys
* Webhooks
* Payment settings

***

### API Keys

API keys authenticate requests from your servers to Hyperswitch. Your integration can't do anything without one.

#### Managing keys

1. Go to **Developers → API Keys**.
2. **Create a key**, give it a name, and (optionally) an expiry.
3. **Copy it immediately** — the secret is shown only once at creation.
4. Use **Test keys** while developing; generate **Live keys** only when you go to production.

{% embed url="https://scribehow.com/o/qzpN4gAaRXWhBwFWaO3hnQ/viewer/How_To_Create_A_New_API_Key_In_Hyperswitch__yCo1jmdPS_yVVcMUh1eTYQ" %}

#### Good practices

* **Never commit keys** to source control or expose them in client-side code.
* **Rotate** keys periodically and whenever one may have leaked — create a new key, switch your integration over, then revoke the old one.
* **Revoke** any key that's unused or compromised.

> 🔑 There's a difference between your **secret API key** (server-side, full access) and the **publishable key** used by the client-side SDK. Keep the secret key server-side only.

***

### Webhooks

**Webhooks** let Hyperswitch notify _your_ server when something happens — a payment succeeds, a refund completes, a dispute opens — so you don't have to poll.

#### Setting up a webhook

1. Go to **Developers → Payment Settings -> Payment Behaviour**.
2. Add your **endpoint URL** (an HTTPS endpoint on your server that receives events).
3. For live mode, your webhook URL needs to be whitelisted by the Hyperswitch team
4. Save and send a **test event(eg. test payment)** to confirm your endpoint responds.

{% embed url="https://scribehow.com/o/qzpN4gAaRXWhBwFWaO3hnQ/viewer/Configuring_and_Testing_Webhooks_in_Hyperswitch__px5kHeD6TVelR0EZVXihXw" %}

***

### Payment settings

**Payment settings** control default payment behavior for the profile — the knobs that shape how payments are created and handled.

Typical settings include:

* **Capture behavior** — automatic capture vs. manual (authorize now, capture later).
* **Return / redirect URLs** — where customers land after completing payment.
* **Payment-method and tokenization behavior** — including **network tokenization** (see Vault).
* **Profile-level defaults** applied to payments created under this profile.

> These defaults affect every payment on the profile, so change them deliberately and validate in **Test mode** first.
