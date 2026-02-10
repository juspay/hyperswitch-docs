---
icon: building-magnifying-glass
---

# Authorizations

### **Advanced Authorization Types**

This section outlines the specialized authorization flows supported by Hyperswitch. These methods allow you to verify payment instruments or manage fluctuating transaction totals without requiring the customer to re-enter their details.

**1. $0 Authorization (Account Verification)**

Commonly used for card-on-file or subscription setups, this flow verifies that a payment method is valid and active without actually blocking any funds. It is an essential step for "Save Card" features to ensure the payment\_method\_id is linked to a legitimate account before future use.

**2. Estimate Authorization**

This allows a business to block a calculated amount on a customer’s card based on an expected total, such as a hotel stay or a car rental deposit. It ensures the customer has sufficient credit available before the service is rendered, providing a safety net for the merchant.

**3. Incremental Authorization**

If the final cost exceeds the initial estimate (e.g., a guest extends their stay or adds room service), this flow allows you to increase the authorized amount on the existing transaction. It avoids the need for a completely new transaction, keeping the checkout experience seamless and consolidated.

**4. Extended Authorization**

Standard authorizations typically expire within 3 to 7 days; however, Extended Authorization keeps the hold active for a longer duration. This is ideal for businesses with long lead times, such as custom-manufactured goods or pre-orders, where shipping might occur weeks after the initial order.

**5. Partial Authorization**

In scenarios where a customer's card balance is lower than the total purchase amount, a Partial Authorization allows you to capture the remaining available balance. The customer can then cover the difference using a secondary payment method, effectively preventing a total transaction decline.
