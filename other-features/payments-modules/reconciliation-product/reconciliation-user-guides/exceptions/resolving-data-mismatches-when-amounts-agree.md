# Resolving Data Mismatches When Amounts Agree

_Time needed: \~10 minutes · Works on the Exceptions screen_

Both systems show **100.00**, but the transaction still says **Data Mismatch**. Why?

Your matching rule checks more than money. In this setup, it links the OMS **Order Id** to the PSP 1 **Merchant Reference**, then validates the reference, **Status**, **Amount**, and **Currency**. A difference in status can keep the transaction from matching even when the amounts agree.

<figure><img src="../../../../../.gitbook/assets/Screenshot 2026-09-20 at 1.43.58 PM.png" alt=""><figcaption></figcaption></figure>



***

#### The example

Your rule links the OMS and PSP 1 entries for **ORD-10540011** using **Order Id → Merchant Reference**. Both sides show **100.00** in the same currency. In this example, the OMS status is **`success`**, so the PSP 1 status is expected to be **`success`** too — but the PSP entry contains **`charged`**.

| Compared value                | OMS           | PSP 1         |
| ----------------------------- | ------------- | ------------- |
| Order Id → Merchant Reference | ORD-10540011  | ORD-10540011  |
| Amount                        | 100.00        | 100.00        |
| Currency                      | Same currency | Same currency |
| Status                        | `success`     | `charged`     |

The status comparison fails: **expected `success`, actual `charged`**. The matching reference identifies the same payment, but the rule still requires the status values to agree.

Here, **Status** is a field from the source data. It is separate from the reconciliation result **Data Mismatch** shown on the transaction.

#### Step 1: Open the mismatch details

Go to **Exceptions → Recon**, and open the transaction showing **Data Mismatch**.

Read the **expected value versus actual value** for each mismatched field. For this example, look for the status difference: **`success` expected, `charged` received**. Then inspect the entries grouped by account.

Confirm that:

* The entries represent the same real payment.
* The amounts, currency, and credit/debit directions make sense together.
* You have checked every reported field difference, not just the first one.

> 💡 A matching amount does not establish that two entries belong together. Check the payment references and source records before accepting a difference.

#### Step 2: Decide what the difference means

| What you find                                                             | Appropriate next step                                                            |
| ------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| Both values are accurate and describe the same thing in different systems | Consider Force Match for this explained, eligible mismatch.                      |
| The values describe genuinely different payments or business events       | Keep the exception open while you investigate the pairing and source data.       |
| The same difference appears repeatedly                                    | Ask the Hyperswitch team to review the transformation or matching configuration. |

For this example, check the original PSP record and your configured status mapping. If the verified value should be **`success`** but the entry contains **`charged`**, correct the entry. If the PSP genuinely uses **`charged`** to mean a successful payment, confirm that meaning with your team before accepting the difference. The two labels are not automatically interchangeable.

#### Step 3: Resolve a verified data error

If the PSP entry should contain **`success`**, choose **Edit Entry** and change its status field from **`charged`** to **`success`**, using the original file, source-system record, or verified mapping as evidence. Keep the verified amount, currency, and reference unchanged, and review the resulting transaction entries before confirming.

Add a specific remark, such as:

_"Corrected PSP status from charged to success for ORD-10540011 after verifying the source record and expected status mapping. Amount 100.00, currency, and merchant reference verified."_

After saving, inspect the resulting status and entries. Both source-data status fields should now show **`success`**. If this was the only issue and the transaction is fully resolved, check that it shows **Matched (Manual)**.

#### A note on transformation configuration

If your PSP reports a successful payment as **`charged`**, the normal setup should handle this in the **transformation configuration**: ask hyperswitch team to map the incoming value **`charged`** to **`success`** and store **`success`** in the transformed entry's status field.

That way, reconciliation compares **`success`** on the OMS side with **`success`** on the PSP side, so matching continues automatically when the other checks agree.

**This guide is for the rare scenario where a status mismatch still reaches Exceptions and needs a one-off manual resolution.** Routine differences in how your systems name a successful payment should be handled during transformation.

If you encounter this mismatch repeatedly, share an example with the Hyperswitch team so they can add or correct the mapping in your transformation configuration. Resolve existing exceptions separately; updating the mapping does not automatically close earlier mismatches.
