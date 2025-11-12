---
description: >-
  Network Tokenization in Hyperswitch: Increase Security and Authorization Rates
  with Minimal Changes
icon: shield-check
layout:
  width: default
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
---

# Network Tokenisation

## What is Network Tokenization?

Network tokenization is the process of replacing sensitive card details (like PAN) with a unique, merchant-specific token issued and managed by card networks (Visa, Mastercard, etc.). These tokens can be safely used in transactions and stored without increasing PCI scope.

As more issuers and networks prioritize token-first infrastructure, network tokenization is rapidly becoming the standard for secure and high-converting card payments globally.

A network token is scoped to a Merchant, Customer & Token Requestor ensuring a more secure payment experience. Every entity to the left of Network will transact using a token and the entities to the right will have card details. Each token is also unique to the Network provider.

<div data-full-width="false"><figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXdTTFA15C5uBOpzeRHfpxLyVSOXUgTzo8hhhECmHMzVp_Tg8NvSQ2PBi1ptG99ZhinPI5seKzESVf4IBoku_NYKe-CYn6zfV4gnC9yTMevLJmETNa8U8D39B8eNZOBisNzBGmPSXw?key=L_7zrdqKs_cTzmvGXIqAyQ" alt=""><figcaption></figcaption></figure></div>

### Key Advantages for Merchants:

1. **Reduced Security Vulnerability:** By using network tokens instead of sensitive card information, you minimize the impact of data breaches, as the network token is specific to a merchant and is of no use to malicious actors. This helps you maintain customer trust and avoid the financial and reputational damage associated with security incidents.
2. **Up-to-date Cardholder Information:** Tokenization automatically updates cardholder information if the card is lost, expired, or reissued. This ensures uninterrupted recurring payments, increasing customer retention and reducing payment disruptions.
3. **Improved Authorization Rates:** Transactions using network tokens are considered more authentic by networks due to richer metadata. This leads to fewer declines and significantly improves your authorization rates by up to 3-5%
4. **Reduced Fraud:** Network tokens are less prone to frauds and have been shown to reduce fraud by up to 26%, which means fewer chargebacks and losses for your business, ultimately improving your bottom line.
5. **Simplified Compliance:** With tokenization, your business doesn’t need to store sensitive card data, reducing the scope and cost of compliance efforts.
6. **Reduced Interchange costs:** Networks in certain geographies provide interchange cost savings to merchants up to 10bps in case of using network tokenization

## **Supported Networks via Hyperswitch**

Currently supported: Visa, Mastercard, American Express

(Additional networks may be added based on merchant needs and network readiness.)

## Juspay as Token Requestor / Token Service Provider

Juspay is certified as both a Token Requestor (TR) and Token Service Provider (TSP). This means:

* As a Token Requestor, we initiate token provisioning with card networks on your behalf.
* As a TSP, we securely manage token lifecycle events: provisioning, detokenization, refresh, suspension, and deletion.

Juspay’s tokenization suite is capable of handling the complete token lifecycle management. We’ve issued more than 150 million network tokens globally.

By leveraging Juspay’s infrastructure through Hyperswitch, you get seamless access to tokenization features without having to integrate with each network independently or worry about certifications.

### **Bring your own Token Requestor credentials**

We also offer you the flexibility to bring your own Token Requestor credentials and configure them within our system so that all network tokenization requests are made using your own credentials. This could ensure better control, compliance alignment, and consistency across your systems.

## Hyperswitch: Network Tokenization Support Modes

Hyperswitch supports three distinct Network Tokenization flows, depending on how you’re integrated:

#### 1. Network Tokenization during Payments (via Hyperswitch Orchestration)

When you process payments using Hyperswitch’s orchestration layer, you can perform tokenized payments directly - Hyperswitch handles provisioning and using the network token dynamically at payment time. We also take care of optimizing authorization rates and latency by switching between network tokens and clear PAN.

#### 2. Network Tokenization during Vaulting (via Hyperswitch Vault service)

You can network tokenize cards at the time of storage in Hyperswitch’s Vault service. These network tokens can later be used for recurring payments, subscriptions, or one-click checkouts in combination with NTID or cryptogram.

#### 3. Standalone Network Tokenization API Service

Use Juspay’s standalone Network Tokenization API service to provision, manage, or detokenize network tokens - without using Hyperswitch’s payment orchestration or vault services.

***

### 1. Network Tokenization during Payments (via Hyperswitch Orchestration)

_No changes required to your PSP integrations — Hyperswitch handles the token lifecycle, retries, and PAN fallback automatically._

In this flow:

* Hyperswitch dynamically provisions a network token at the time of payment.
* The network token is used in real-time to complete the transaction.
* If a payment fails when using Network token due to Network token specific errors, Hyperswitch silently retries the payment using Clear PAN + CVV/NTI to optimize for higher authorization rates
* Hyperswitch also optimizes for latency by falling back to Clear PAN + CVV/NTI

#### Flow Summary:

<div data-full-width="false"><figure><img src="../../../../.gitbook/assets/image (163) (1).png" alt=""><figcaption></figcaption></figure></div>

1. You enable Network tokenization on your Hyperswitch orchestration merchant account by reaching out to our support team.
   1. You can either bring your own TRID or use Juspay’s TRID to request network tokens
2. The end user enters their card details on your checkout
3. Hyperswitch provisions a network token and cryptogram if the card is eligible for tokenization
4. If tokenization succeeds, Hyperswitch passes the network token + cryptogram to the PSPs for payments processing
5. If tokenization fails, Hyperswitch uses clear PAN + CVV to process payments through the PSPs
6. If the end user had agreed to store the card, the Network token is stored in Hyperswitch vault and optionally, the token can be returned to the merchant for future use

#### **How to Try:**

Contact our support team to enable Network Tokenization on your merchant account and receive access. You can test tokenized payment flows in sandbox before going live.

***

### 2. Network Tokenization during Vaulting (via Hyperswitch Vault)

In this flow:

* You integrate with [Hyperswitch’s standalone Vault service](../../../../about-hyperswitch/payments-modules/vault/).
* Card details are securely captured and stored alongside PSP tokens and network tokens
* These tokens can be used across multiple gateways via your own payments setup or Hyperswitch by retrieving them along with cryptogram every time you intend to make a payment

#### Flow Summary:

<div data-full-width="false"><figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXeq8-6ydB04z4YzTZKf7dYTmwcB1TT4eSCS_-MPXUQR-1CZ-wSFT_XeCiQrTWaXBRhJq0f81Tyk80zgaUCv63WPSBrlOgrCleJbmnZ2ydjexjsKY7hQzQ2Cd7dm50ddNxb7akEG?key=L_7zrdqKs_cTzmvGXIqAyQ" alt=""><figcaption></figcaption></figure></div>

1. Merchant signs up for [Hyperswitch’s standalone vault service ](../../../../about-hyperswitch/payments-modules/vault/)and requests network tokenization in every payment method session create request
2. Card details are captured from the end users via Hyperswitch’s PCI-compliant UI SDK or merchant passes them using the Server to Server APIs.
3. Hyperswitch provisions a network token and stores it securely along with the card details if the merchant chooses to vault clear PAN in Hyperswitch vault
4. The network token along with PSP tokens and NTI (if returned by the PSP) is passed back to the merchant
5. Token can be retrieved later by the merchant along with cryptogram using the Retrieve payment method endpoint
6. Merchant can use the retrieved Network token + cryptogram or NTI to process payments later through their own payments system

#### How to Try?

Contact our support team to enable Network Tokenization on your merchant account and receive access. You can test tokenized payment flows in sandbox before going live. You can learn more and try out our Vault service here.

***

### 3. Standalone Network Tokenization Service (via Juspay Tokenization service)

This is a lightweight, standalone integration when you:

* Already have your own PCI compliant vault or orchestration system but want to add Network Tokenization for better auth rates and lower costs
* You only want to use Juspay to provision and manage network tokens

#### Flow Summary:

<div data-full-width="false"><figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXd_HAbjBj9cDcO_pV9LWsyBICza6Ag9zR1lpAnfDOrYKaJd07ELel2Lchuf785tKNYE3n_8OK5MmtZsLdv-Orp-e-kqHa91rxe1vGy5l6soFd2A9O47VeCZWrXZCuFowLeRHRPC-Q?key=L_7zrdqKs_cTzmvGXIqAyQ" alt=""><figcaption></figcaption></figure></div>

* You sign up for Juspay’s Network Tokenization service by reaching out to our support team
* You can either use Juspay’s TR ID or setup your own TR ID
* You use [Juspay’s Tokenization APIs](https://juspay.io/in/docs/api-reference/docs/tokenization-apis/generate-network-token) to:
  * Generate Network Tokens for a given PAN
  * Update or delete tokens
  * Retrieve Network tokens and cryptogram to make payment through your own payments system

#### How to Try?

Contact our support to set up your credentials and get access to our Token Provisioning and Cryptogram APIs.

\\
