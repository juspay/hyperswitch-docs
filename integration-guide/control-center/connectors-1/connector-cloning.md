# Connector Cloning

## Cloning a payment connector to another business profile

### What this feature does

If you already have a payment connector (like Paypal) set up and working in one business profile, you no longer need to set it up again from scratch in another profile. **Clone connector** copies the connector's configuration — credentials, webhook setup, payment methods, and label — into a different business profile in a couple of clicks.

This saves you from re-entering the same API keys and re-selecting the same payment methods every time you add a new business profile.

### Who can do this

* You need the **Organisation Administrator** or **Merchant Administrator** role. Other roles, including custom roles, don't have access to this action.
* If you don't see the `Clone connector` button on a connector's page, cloning either isn't enabled for that connector or isn't turned on for your account — contact your Hyperswitch account team.

### What gets copied

When you clone a connector, the new copy in the destination profile gets:

* ✅ **Credentials** — API keys and account details
* ✅ **Payment methods** — the cards and other payment methods enabled on the source connector

**Note on payment methods:** not every payment method type is guaranteed to carry over automatically — we support all payment methods apart from Bank Debits

### How to clone a connector

{% embed url="https://scribehow.com/o/qzpN4gAaRXWhBwFWaO3hnQ/viewer/How_to_Clone_a_PayPal_Connector_Profile_in_Hyperswitch__QwbwY87OSYO9iuIDl-hKcA" %}

1. Go to the connector's detail page in the business profile you want to clone **from**.
2. Click **Clone connector**.
3. In the dialog that opens:
   * The source connector and source profile are shown for reference (read-only).
   * Choose the **destination profile** — this is the profile you're copying the connector _into_. You can't clone into the same profile you're already in.
   * Enter a **new connector label** for the cloned connector — this is required.
   * Review the "Included in the clone" and "Not copied" summary shown in the dialog.
4. Click **Clone connector** to confirm.
5. You'll see a success message once the new connector is created in the destination profile.

### After cloning — what to check

* Open the new connector in the destination profile and confirm the payment methods you expect are enabled.

| Message you might see                       | What it means                                                                                               | What to do                                                                                                      |
| ------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| "Connector label already exists."           | The label you entered is already used by another connector in the destination profile                       | Enter a different, unique label and try again                                                                   |
| You don't see a destination profile to pick | You may only have one business profile, or a temporary issue is preventing your other profiles from loading | Confirm you have more than one business profile under your merchant account; retry if the list looks incomplete |

### FAQ

**Does cloning affect the original connector?** No. The source connector is untouched — cloning only creates a new, separate connector account in the destination profile.

**Can I clone the same connector to multiple profiles?** Yes. Repeat the process for each destination profile you want to set it up in.

**Will the cloned connector go live immediately?** The cloned connector keeps the same status (test/live, enabled/disabled) as the source connector at the time of cloning. Review it before relying on it in production.
