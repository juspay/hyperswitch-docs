---
description: >-
  Optimize processing fees on debit payments by routing traffic to the cheapest
  available debit network
icon: hand-holding-dollar
---

# Least Cost Routing

## Get started with Least Cost Routing

Least Cost Routing (LCR) enables merchants to minimize transaction costs by dynamically selecting the most cost-efficient debit network for each transaction. The Hyperswitch routing engine evaluates parameters like network fees, interchange rates, ticket size, issuer type, and more to automatically route transactions through the cheapest network in real time.

## Pre-requisites for enabling Least Cost Routing

To get started with LCR in Hyperswitch, ensure the following setup is complete:

_**Step 1:**_ Configure connectors supporting transactions through local networks

_**Step 2:**_ Enable Debit Card Support

_**Step 3:**_ Enable one or more local debit networks in both connector and Hyperswitch dashboards\\

## Steps to configure Least Cost Routing in Smart Router:

_**Step 1:**_ Configure Prerequisites\
Ensure that connectors supporting transactions through local networks are set up with local networks enabled

_**Step 2:**_ Navigate to `Workflow` ->`Routing` -> `Least Cost Routing`

<figure><img src="../../../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

_**Step 3:**_ A popup will guide you to confirm the three prerequisites - 1.) Connector setup, 2.) Debit card enablement, and 3.) Local networks configuration. Click on `Enable` to activate LCR

<figure><img src="../../../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>

_**Step 4:**_ Once enabled, you can view Least Cost Routing as your active routing algorithm along with all previously configured algorithms on the [Hyperswitch Dashboard](https://app.hyperswitch.io/routing)

<figure><img src="../../../.gitbook/assets/Screenshot 2025-05-26 at 5.42.34 PM.png" alt=""><figcaption></figcaption></figure>

## Supported Configuration for Least Cost Routing

**Geographies**: US

**Networks**

* Star
* Pulse
* NYCE
* Accel

**Payment Methods**: Cards

## Real-time cost computaion

We perform real-time computation to see if a Global network (Visa/ Mastercard) vs Local network is preferable or which local network to choose

* We calculate transaction cost estimate using the MCC code supplied by merchant&#x20;

<figure><img src="../../../.gitbook/assets/image (3) (1).png" alt=""><figcaption></figcaption></figure>

* We look into amount (value) of transaction and Card Issuer bank to compute a cost of transction and determine the right network to process.
* The system has default values baked-in to compute cost of transaction and make decisions. The LCR system is being designed to accept cost inputs from merchants. Specifically, if they have any PSP–Network level contracts that should be considered during network selection.
* We perform debit routing by specifying the network to be used in the API request to the PSP.
