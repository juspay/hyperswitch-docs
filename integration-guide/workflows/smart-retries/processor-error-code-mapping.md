---
icon: signs-post
---

# Understanding Decline Codes

Every failed payment comes back with an error, but not every error means the same thing. Some declines are worth retrying immediately, some only after authentication, and some will never succeed no matter how many times you try.

The difficulty is that each processor describes failures in its own language. Stripe returns **card\_declined**, Adyen returns **Refused** - and both may be relaying the exact same issuer decision underneath.

Hyperswitch normalises this through the Gateway Status Map (GSM): a rule table that turns any processor's error into a retry decision and a single, consistent error for your systems and your customers.



### The codes on a failed payment

| Code                 | What it tells you                                                                                                                                              |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Processor error code | How the PSP described the failure. Specific to that processor                                                                                                  |
| Issuer decline code  | The card network decline code from the issuer, e.g. `05` (Do not honor), `51` (Insufficient funds). Same meaning across every processor that passes it through |
| Network advice code  | The scheme's guidance on whether a merchant-initiated transaction may be re-attempted. Configured separately, outside GSM                                      |

The issuer code is the more useful of the two GSM uses, because it describes the _issuer's_ behaviour rather than the processor's wording and does so without any process syntactic sugar. Hyperswitch therefore checks it first.

### How a rule is matched

1. **Issuer code** - used when both the decline code and the card network are known for the attempt.
2. **Processor code** - the fallback, matched on the PSP's own code and message.
3. **Neither matches** - no auto-retry, and the unified error `UE_9000 - Something went wrong` is returned.

Rules are scoped to a processor, flow and sub-flow, e.g. `(adyen, Payment, Authorize)` . For complete list of flows and sub-flows check out the [Hyperswitch repository](https://github.com/juspay/hyperswitch) and the [API reference](https://api-reference.hyperswitch.io/introduction)



### What a GSM rule decides

| Outcome         | When it applies                                                |
| --------------- | -------------------------------------------------------------- |
| Cascading retry | Re-attempt on the next eligible processor                      |
| Step-up retry   | Re-attempt once on the same processor with 3DS enforced        |
| Clear PAN retry | Re-attempt with the raw card number instead of a network token |
| Network retry   | Re-attempt over an alternate card network                      |
| No retry        | Hard declines, where further attempts only add cost            |

Each rule also sets the **unified error code, message, stadardised message, user-friendly message (to show on the Checkout page) , description** returned in the payments API response





**Note: Not every processor sends an issuer code.** In case not present Hyperswitch  fall back to the processor code silently.
