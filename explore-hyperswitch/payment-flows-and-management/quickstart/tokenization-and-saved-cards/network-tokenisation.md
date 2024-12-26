---
icon: shield-check
---

# Network Tokenisation

## What is Network Tokenization?

Network tokenization replaces sensitive card details with a unique, non-sensitive token provisioned and managed by networks. This token is specific to the merchant(Token requestor) and can be used for secure transactions instead of the actual card number.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXeJM1RFlI6IXOJZqZZUMEVlBqx8YEYqQagqNRCBYFWJDvDuCoHrYp9Lux2C7dhuuspU8JPPOMsMahGTT3NXi8rIXvMNdJLc_24LCcju4hQ63kpG5VwMvDa6lDpdbwQKeMdZmoVBxkYvvkczCw1T9vpiggH1?key=igtH0ZBSttWMfUaLaUgfgg" alt="" width="563"><figcaption></figcaption></figure>

## Benefits of using Network Tokenization:

1. Reduced Security Vulnerability: By using network tokens instead of sensitive card information, you minimize the impact of data breaches, as the network token is specific to a merchant and is of no use to malicious actors. This helps you maintain customer trust and avoid the financial and reputational damage associated with security incidents.
2. Up-to-date Cardholder Information: Tokenization automatically updates cardholder information if the card is lost, expired, or reissued. This ensures uninterrupted recurring payments, increasing customer retention and reducing payment disruptions.
3. Improved Authorization Rates: Transactions using network tokens are considered to be more authentic by the networks as they carry richer data, leading to fewer declines and higher authorization rates.
4. Reduced Fraud: Network tokens are less prone to frauds and have been shown to [reduce fraud by up to 26%,](https://navigate.visa.com/na/money-movement/why-2021-is-set-to-be-the-year-of-the-token/) which means fewer chargebacks and losses for your business, ultimately improving your bottom line.
5. Simplified Compliance: With tokenization, your business doesn’t need to store sensitive card data, reducing the scope and cost of compliance efforts.

## Use Cases with Hyperswitch:

* Subscription and Repeat Based Businesses: Ideal for businesses with recurring payments, tokenization ensures seamless payments by automatically updating card information, improving authorization rates.
* Gateway Agnostic: Hyperswitch’s Network tokenization works across payment gateways, allowing merchants to make recurring MIT(Merchant Initiated transaction) payments with the payment gateway of their choice.

## How Network Tokenization Works:

<figure><img src="../../../../.gitbook/assets/Screenshot 2024-10-17 at 12.01.54 PM.png" alt=""><figcaption></figcaption></figure>

1. Card Information Submission: The customer provides their card details during a transaction.
2. Token Generation: The payment network (e.g., VISA, Mastercard) replaces the card details with a unique token specific to the merchant.
3. Token Use: The merchant uses this token to process payments instead of the actual card number.
4. Transaction Completion: The payment network links the token to the card and completes the transaction securely.
5. Recurring Transactions: For future payments, the same token is used, ensuring up-to-date card details even if the card is lost, reissued, or expired.
6. In this above flow Merchant server is the TR (Token Requester) and Hyperswitch is the TR/TSP (Token Service Provider).

## How to Enable Network Tokenisation:

Network Tokenisation is an on-request offering from Hyperswitch.&#x20;

To enable Network Tokenisation for your merchant account, Kindly reach out to hyperswitch@juspay.in

{% content-ref url="../payment-links/" %}
[payment-links](../payment-links/)
{% endcontent-ref %}

\
