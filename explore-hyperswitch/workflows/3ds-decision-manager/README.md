---
icon: badge-check
---

# 3DS / Strong Customer Authentication

3D Secure (3DS) is a robust security protocol designed to prevent fraud in card-not-present transactions. By employing multi-factor authentication mechanisms such as biometrics or OTPs, 3DS helps issuers verify the authenticity of transactions.

The **Hyperswitch 3DS Decision Manager** allows merchants to define advanced rules based on payment parameters, ensuring that 3DS authentication is selectively enforced for high-risk transactions.

### Benefits of Using the 3DS Decision Manager:

* **Fraud Reduction:** Enforce 3DS on high-risk transactions to mitigate fraudulent activities.
* **Enhanced Compliance:** Meet regulatory requirements for Strong Customer Authentication (SCA) in regions like the EEA.
* **Improved Customer Experience:** Apply 3DS only when necessary, minimizing friction during checkout for low-risk transactions.

Hyperswitch 3DS Decision Manager allows the merchant to configure advanced rules using various payment parameters such as amount, currency etc., to enforce 3D Secure authentication for card payments to reduce fraudulent transactions.

{% embed url="https://youtu.be/-VTnngditlU" %}

## How does it work?

#### 3DS Decision Flow:

Hyperswitch integrates with multiple payment processors, enabling seamless 3D Secure authentication.

<figure><img src="../../../.gitbook/assets/final2.drawio.png" alt="" width="375"><figcaption><p>3DS Decision Flow</p></figcaption></figure>

The **3DS Decision Manager** in the Hyperswitch Control Center provides merchants with a rule-based interface to enforce authentication selectively.

For example: If you wish to enforce 3DS for transactions over $100, you can define a rule that automatically sets `authentication_type` as `three_ds` for such transactions. Payments meeting this rule will trigger 3DS authentication.

<figure><img src="../../../.gitbook/assets/3ds-rule_example (1).png" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
* Rules set in the **3DS Decision Manager** can be overridden if an explicit value is passed in the `/payments` request using the `authentication_type` parameter. ([API Reference](https://api-reference.hyperswitch.io/api-reference/payments/payments--create))
* Some processors may mandate 3DS regardless of your configuration.
{% endhint %}

{% content-ref url="3ds-intelligence-engine/get-started-with-3ds-decision-manager.md" %}
[get-started-with-3ds-decision-manager.md](3ds-intelligence-engine/get-started-with-3ds-decision-manager.md)
{% endcontent-ref %}

{% content-ref url="../../../hyperswitch-open-source/account-setup/test-a-payment.md" %}
[test-a-payment.md](../../../hyperswitch-open-source/account-setup/test-a-payment.md)
{% endcontent-ref %}
