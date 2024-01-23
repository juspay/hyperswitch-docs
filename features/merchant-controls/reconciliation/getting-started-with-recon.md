---
description: Detailed description about Hyperswitch Reconcilation dashboard
---

# Getting Started with Recon

{% hint style="info" %}
This section addresses the supported features of Hyperswitch Recon and provides guidance on how to utilize them.
{% endhint %}

## Reconciliation Features&#x20;

* [File Management](getting-started-with-recon.md#file-management)
* [Recon engine ](getting-started-with-recon.md#recon-engine-capabilities-precision)
* [Recon Dashboard](getting-started-with-recon.md#recon-dashboard-components)
* [Recon Report ](getting-started-with-recon.md#recon-reports)
* [Recon open issues ](getting-started-with-recon.md#recon-open-issues)

### File management

Efficient file management is at the core of Hyperswitch Recon's data integration process. It ensures that your financial data is seamlessly processed, validated, and transformed before being fed into the Recon Engine. This section elaborates on the 3-step journey—Upload, Validate, and Transform—involved in preparing files for reconciliation.

#### **Step 1: Uploader**

The first phase of the process involves uploading your data files into the Recon system. Hyperswitch Recon provides multiple methods for this purpose:

1. **Manual upload to the dashboard:** For ease of use, manually upload your files directly through the Recon Dashboard.

**In order to feed your PSP and bank files to the Recon module you can**

1. **Via Recon uploader API:** Utilize the Recon Uploader API to programmatically submit your files for reconciliation.
2. **Via Merchant's SFTP:** Leverage your own Secure File Transfer Protocol (SFTP) infrastructure to securely transfer files.

{% hint style="info" %}
Files need to be uploaded in **PGName\_yyyymmdd/MERCHANTNAME\_yyyymmdd** format.
{% endhint %}

#### **Step 2: Validator**

After the files are uploaded, they enter the Validator phase, where records undergo  validation to ensure data integrity. This phase involves a series of checks to vet records based on various conditions, including:

* **Column check:** Verify that all required columns are present and correctly formatted.
* **Data type validation:** Validate data types to ensure they conform to the expected format.
* **Duplicate value detection:** Identify and eliminate duplicate records to prevent redundancy.
* **Date format verification:** Ensure date values are correctly formatted and consistent.
* **Other custom conditions:** Apply additional custom conditions relevant to your business use case.

Records that fail any of these validation checks are identified and separated from the dataset. These failed records are not forwarded to subsequent steps, minimizing the risk of inaccurate reconciliations.

#### Step 3: Transformer

The final stage of the File Management process is the Transformer phase. In this phase, various computations and transformations are applied to the validated records to prepare them for reconciliation within the Recon Engine. These transformations can include:

* **Settled amount calculation:** Compute settled amounts based on transaction values and statuses.
* **Fee & tax computation:** Calculate applicable fees and taxes associated with transactions.
* **Offers customization:** Apply customizable offer computations to reflect promotional adjustments.

Merchants are granted the flexibility to tailor Fee, Tax, and Offer computations to their specific business needs. This customization empowers you to align the reconciliation process with your unique financial requirements.

### Recon Engine - Capabilities&#x20;

This section delves deeper into the engine's capabilities, including multi-dimensional reconciliation and advanced techniques to enhance performance.

#### The automatic trigger

When all the respective merchant files are seamlessly ingested into the Recon system, the Reconciliation Engine gets auto triggered.&#x20;

#### Multi-dimensional reconciliation

Hyperswitch Recon Engine can execute 3-way reconciliation between merchant, PSP, and bank. This intricate reconciliation paradigm ensures that financial transactions traverse seamlessly across these entities, validated based on crucial attributes such as Amount, Status, Fee & Taxes, and more, as stipulated in the Configurator.

#### Confidence score-potential matched

In the intricate landscape of transactions, entities often share identifiers across various columns due to nuances like refunds and split transactions. In response, the Recon Engine employs an innovative approach—confidence score-based reconciliation. This technique, built upon transaction identifiers, enhances overall performance by confidently matching transactions even in complex scenarios.

#### Backdated Reconnaissance

The Recon engine's effectively performs backdated recon by scrutinizing entries from previous dates. If matching entries are found, reconciliation is seamlessly executed, ensuring historical accuracy. By default, the engine considers backdated entries spanning the last 7 days, fostering precision in historical data alignment.

### Recon Dashboard components

The Recon Dashboard is characterised by several components that facilitate analysis:

1. **Single stats snapshot:** Gain immediate insights into reconciliation results with a concise overview. The dashboard showcases counts of **matched**, **mismatched**, **missing**, and even matched with a buffer for the selected time range. The below snapshot encapsulates the essence of reconciliation outcomes at a glance.
2. **Time series graph:** Visualize reconciliation trends over time with a dynamic time series graph. Dive into historical patterns, observe fluctuations, and identify performance benchmarks for enhanced strategic decision-making.
3. **Amount calculation insights:** Unveil deeper financial insights through calculated amounts, including Balance from the last period, amount expected/received, and balance receivable. These calculations provide a comprehensive picture of your financial alignment.
4. **Bank <> PSP <> Merchant transactions:**  The Recon Dashboard maps bank, PSP, and merchant transactions, fostering a holistic understanding of your financial ecosystem.

<figure><img src="../../../.gitbook/assets/Screenshot 2024-01-23 at 3.58.02 PM.png" alt=""><figcaption></figcaption></figure>

### Recon reports

The **Reports** module within the Recon Dashboard empowers users with a detailed and structured exploration of reconciliation outcomes.&#x20;

#### **Transaction-level reconnaissance**

This dynamic platform consolidates transaction data, facilitating thorough evaluation and informed decision-making.

#### Recon statuses:&#x20;

* **Matched :** Transactions that are matched across systems.&#x20;
* **Mis-matched :** Transactions are present across the systems, but any of the fields, such as amount, tax, or currency, is mismatched.
* **Missing :** Transactions which are not present in at least one of the files

<figure><img src="../../../.gitbook/assets/Screenshot 2024-01-23 at 3.18.15 PM.png" alt=""><figcaption></figcaption></figure>

#### Variety of report options

Within the Reports module, users can access an array of essential reports that cover various aspects of the reconciliation process:

* **Overall transaction report:** Gain a comprehensive view of reconciliation outcomes across all transactions.
* **Merchant transaction report:** Focus specifically on merchant-level transaction alignment, fostering granular insight.
* **PSP settlement report:** Analyze transaction reconciliation outcomes within the context of PSP settlements.
* **Bank settlement report:** Gain insights into transaction alignment concerning bank settlements.

#### Specific information availability

The Reports module provides access to specific information categories such as Gateway, Status, and Sub-status. These intricate details enable users to dissect reconciliation outcomes based on diverse attributes, facilitating pinpoint analysis.

#### Customizable column views

Users have the ability to customize their column views within the Reports module:

* **Select desired columns:** Choose which columns to view, tailoring the report to focus on specific attributes like transaction ID, amount, status, and reconciliation status.
* **Column naming:** Assign specific names to columns, enhancing clarity and alignment with your business's terminology.
* **Streamlined insights:** View only the columns that are relevant to your analysis, ensuring a streamlined and efficient reporting experience.

#### **PSP level summary reports**

The Recon Dashboard extends its analytical reach, allowing users to access PSP level summary reports. These reports present transaction reconciliation outcomes at a more detailed level, including:

* **Order-level Reconciliation**: Delve into order-level reconciliation results, shedding light on the alignment between transactions and settlements.
* **Refund-level reconciliation**: Uncover insights into refund-level reconciliation outcomes, ensuring precise financial accuracy across various refund scenarios.
* **Bank settlement <> PSP <> Merchant transaction report**: Gain unparalleled visibility into the transaction journey across bank, PSP, and merchant realms, facilitating comprehensive analysis.

### **Recon open issues**

The O**pen issues** module within HyperSwitch Recon serves as a dynamic platform for addressing reconciliation discrepancies head-on. This section elucidates the functionality of the Open Issues module, offering users a structured pathway to identify, resolve, and re-evaluate transactions with mismatched or missing reconciliation statuses.

#### **Addressing mismatched and missing recon statuses**

The Open Issues module is a pivotal component that enables users to tackle reconciliation anomalies with precision. All transactions with a Recon status marked as **Mismatched** or **Missing** find their place within this module. These records serve as focal points for addressing discrepancies and enhancing financial alignment.

#### The Resolution process

To initiate the resolution process, users can follow these straightforward steps:

1. **Select records:** Users can meticulously choose the records with mismatched or missing reconciliation statuses that require resolution.
2. **Resolve button:** Click the "Resolve" button, which serves as the gateway to rectifying the discrepancies.

<figure><img src="../../../.gitbook/assets/Screenshot 2024-01-23 at 3.11.42 PM.png" alt=""><figcaption><p>This is a representation of the dashboard with sample data.</p></figcaption></figure>

#### Data entry and modification

Upon clicking the **Resolve** button, users enter the resolution arena. This involves entering data into the respective fields relevant to the transaction. After furnishing the required information, users simply save their changes.

**Dynamic recon status modification**

Upon successful resolution, the Open Issues module triggers a sequence of actions:

1. **Reconciliation update:** The Recon Engine re-evaluates the transaction with the updated data.
2. **Status modification:** The transaction's Recon status is dynamically modified in response to the resolution outcome.

## FAQs

<details>

<summary>Is 3-way reconciliation supported ?</summary>

Yes, we do support 3-way reconciliation between merchant, PSP, and bank. You need configure your bank report by raising request via email or slack.

</details>

<details>

<summary>Can I configure the file format in Recon dashboard for existing PSP or a new PSP?</summary>

No, the Recon team will configure your desired transaction report for you

</details>
