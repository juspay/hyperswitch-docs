---
description: >-
  Simplify implementation of orchestration and payment outcomes by taking
  advantage of normalized request and response fields and values to avoid
  changes by engineering teams
icon: arrow-progress
---

# Workflows

Workflows allow merchants to control the flow of payments by invoking different systems/ connectors or set of rules :

#### [**3DS workflows** ](3ds-decision-manager/)

Allows the merchant to introduce authentication in the following forms - via PSP, external to Hyperswitch but the authentication parameters are passed in the /payments request, or add an independent 3DS solution (Juspay's or any other) and authenticate external via Hyperswitch.

#### [**FRM workflows**](fraud-and-risk-management/)

Allows the merchant to introduce a fraud and risk module in the following forms - pre-authorize flow such that the FRM module is invoked first followed by the PSP or post-authorize flow such that the PSP is invoked first followed by the FRM module

#### [**Vault workflows**](vault/)

Allows the merchant to introduce an external vault for storing the payment method details/ credentials in the following forms - collection using Hyperswitch SDK but storage in the external vault or collection using external vault SDK and storage in the external vault as well. The retrieval fo credentials from the external vault happens either using the tokenize-de-tokenize APIs or card forwarding. &#x20;

#### [**Smart retry workflows** ](smart-retries/)

Allows the merchant to retry a failed transaction with the same PSP or a different PSP in the following forms - Cascading Retry with same or enhanced payload, Step-Up Retry, Clear PAN Retry, Global Network Retry and Manual retry &#x20;

#### [**Intelligent routing workflows**](intelligent-routing/)

Allows the merchant to route a transaction via a PSP in the following forms - Static routing like Rule-based, Volume-based, Fallback or Dynamic routing like real-time Auth-rate based or Least cost routing
