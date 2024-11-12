---
description: >-
  A platform that gives you complete control of your reconciliation process,
  making it faster, efficient, and scalable
icon: handshake-simple
---

# Reconciliation

{% hint style="info" %}
This section outlines how to configure and use Hyperswitch Reconciliation module to streamline your financial processes
{% endhint %}

## Overview&#x20;

Hyperswitch Reconciliation module allows reconciliation between the transaction data from Hyperswitch,  the settlement data shared by payment gateways and the merchant account statement from the bank. This process is designed to ensure financial accuracy and streamlines settlement processes. The system ensures that businesses receive reconciliation results promptly.

## Use cases

1. Three-way recon - Hyperswitch Recon Engine can execute 3-way reconciliation between merchant, PSP, and bank. This intricate reconciliation paradigm ensures that financial transactions traverse seamlessly across these entities, validated based on crucial attributes such as Amount, Status, Fees & Taxes, and more, as stipulated during configuration.
2. Two-way recon - Hyperswitch Recon Engine also offers the flexibility to execute 2-way reconciliation between the Merchant and PSP.

## Activate & Configure the Reconciliation module

1. Go to Reconciliation tab on the Hyperswitch control centre.
2. Click on send an email. Hyperswitch team will reach out to you over email. We will need to configure the file formats of PSPs and bank reports that you plan to use via the Reconciliation module.&#x20;
   * To configure PSP or a bank report file format, you need to have sample data in the right format. PSPs support various API reports tailored for different use cases. You must select the report that aligns with your specific business requirements. We provide support for multiple file formats for a single PSP.
   * It usually take 2-5 days for the team to configure the module as per your requirements depending on the file formats and other specifications.&#x20;
   * Merchants can also choose whether they want to do Manual reconciliation or Automated reconciliation.
   * We also allow merchants to specify the details of computations based on transaction values, fees, and taxes.&#x20;
     * For instance, consider an order of $100 sent via Hyperswitch to the payment processor which will ultimately send this amount to the merchant's bank for settlement. However, in between, the payment procesor will deduct fees as well as taxes, let's say 5% each. Therefore, the settled amount will be $90, with a $5 fee and a $5 tax.&#x20;
     * The payment processor report should contain these details. However, in case these details are not present in the report , the merchant can specify these values. Based on the merchant configured specifications, we will reconcile the bank's settled amount.
3. Once reconciliation is active for your merchant account, you will be notified through an email. You can log into Hyperswitch dashboard and click on 'Go to recon tab'. You will be redirected to the Reconciliation dashboard.&#x20;

<figure><img src="../../../.gitbook/assets/Screenshot 2024-01-23 at 1.23.01 PM.png" alt=""><figcaption></figcaption></figure>

4. The merchant will be granted **Merchant admin** access to the Reconciliation dashboard and will have the ability to add their internal team members as **Users** with customisable permissions from the Admin tab.

[Know more about Hyperswitch Reconciliation module and how to use it](getting-started-with-recon.md).
