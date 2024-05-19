# ♻️ Smart Retries in Payout

Retries are attempts to make payouts after initial failure. Retries are used for recovering failed payouts. Smart Retries enables retry based on error type and connectors available. This significantly increase the success rate of the payout.

{% hint style="info" %}
Please drop a note to `biz@hyperswitch.io` to enable Smart Retries for Payout (applicable only for Hyperswitch Cloud users).
{% endhint %}

Smart retries are configured based on error specific to connector and would retry only if the error configuration is suitable to increase transaction's success rate.

#### Types of Smart Retries

{% tabs %}
{% tab title="Single Connector Retry" %}
If a single connector is enabled to merchant for a particular payment method, eligible errors would be attempted for retry through the same connector
{% endtab %}

{% tab title="Multiple Connector Retry" %}
In case of multiple available connectors for merchant for a particular payment method, eligible error would trigger retry through other available connectors on the priority list&#x20;
{% endtab %}
{% endtabs %}

#### Available Payout Methods for Smart Retries

<table><thead><tr><th width="243">Connector</th><th>Payout Methods</th></tr></thead><tbody><tr><td>Adyen</td><td>Cards, Banks and Wallets</td></tr><tr><td>Cybersource</td><td>Cards</td></tr><tr><td>Ebanx</td><td>Banks</td></tr><tr><td>Paypal</td><td>Wallets</td></tr><tr><td>Stripe</td><td>Cards and Banks</td></tr><tr><td>Wise</td><td>Banks</td></tr></tbody></table>

#### Retry Conditions

* Multi Connector Retry will work  if there are multiple connectors available with a specific payout method enabled. The payout method is not changed in this case.
* Single Connector Retry will not change its payout method for retrying the payment
* Error Configuration must be loaded on our end (can be submitted by merchant)
* Retry Count is set for every connector, which is 5 by default but can be customised as per merchant.&#x20;
* Smart Retry is continued till the payout is successful, retry count is exhausted or connectors are exhausted

