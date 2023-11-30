---
description: Store your customers cards securely in a centralized compliant vault
---

# 🔓 Tokenization & saved cards

Hyperswitch provides you with the capability to store your customers cards securely in a centralized PCI DSS Level 1 compliant vault. Our Unified checkout automatically handles save cards flow when customers choose the Save card details checkbox while providing their card details for the payment and the transaction is successfully processed.

<figure><img src="../.gitbook/assets/savedCards1.png" alt=""><figcaption></figcaption></figure>

For a returning customer, our Unified Checkout automatically shows the list of their saved cards from previous sessions if the same customer\_id is passed during payments/create API call from your server.

<figure><img src="../.gitbook/assets/savedCards2.png" alt=""><figcaption></figcaption></figure>

Internally, Hyperswitch handles saving cards through multiple layers of tokenization to communicate with our secure vault. All the complexities with tokenization during saved cards flow are taken care of by our Unified checkout and Hyperswitch backend.

## Migrating your customers’ saved cards from your processors to Hyperswitch

Hyperswitch also supports migrating your customers’ saved cards from your processors’ vaults to Hyperswitch. This process typically involves requesting your processor’s support team to share your customers’ saved cards data to Hyperswitch in a secure file transfer format and may involve sharing Hyperswitch’s PCI DSS certificate with them. Please write to <mark style="color:blue;">hyperswitch@juspay.in</mark> to know more and kickstart your card migration process.

## Network Tokenization - Coming Soon!

Soon, Hyperswitch will be able to support Network Tokenization which will enable you to securely store your customers’ card details with various networks such as Visa, Mastercard, American Express, etc. This would bring in additional benefits such as higher authorization rates, fraud reduction, liability shift, lower network fees in some cases, etc.
