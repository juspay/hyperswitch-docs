---
description: >-
  Learn about the different options available to handle saved card transactions
  when working with an external vault provider.
icon: money-bill-wave
metaLinks:
  alternates:
    - processing-payments-with-external-vault.md
---

# Processing payments with external vault

When working with an external vault provider, here are the options available to handle a saved card transaction with **Juspay Hyperswitch**.

**Option 1 -** Hyperswitch server uses the proxy payments flow of external vaults to send vault tokens in the PSP payment request. These tokens are replaced with raw card data by the external vault before the request is forwarded to the PSP.

<figure><img src="../../../../.gitbook/assets/unknown (2).png" alt=""><figcaption></figcaption></figure>

* **Option 2 -** Hyperswitch server uses the detokenize payments flow of external vaults to detokenize vault tokens and obtain the raw card info. This raw card info is used in the payment request before the request is sent to the PSP.

<figure><img src="../../../../.gitbook/assets/unknown (3).png" alt=""><figcaption></figcaption></figure>

* **Option 3 -** Merchant server uses proxy payments flow of external vaults to send vault tokens in the Hyperswitch payment request. These tokens are replaced with raw card data by the external vault before the request is forwarded to Hyperswitch. This Hyperswitch request with raw card info is sent to the PSP by Hyperswitch.

<figure><img src="../../../../.gitbook/assets/unknown (4).png" alt=""><figcaption></figcaption></figure>
