---
description: Detailed description about Hyperswitch Reconciliation module
---

# Getting Started with Recon

{% hint style="info" %}
This section outlines the supported features of Hyperswitch Reconciliation module and provides guidance on how to use them.
{% endhint %}

## Using the Reconciliation module is a 5-step process &#x20;

1. [Upload & prepare file](getting-started-with-recon.md#id-1.-upload-and-prepare-files)
2. [Run Reconciliation](getting-started-with-recon.md#id-2.-run-reconciliation)
3. [Reconciliation Report ](getting-started-with-recon.md#id-3.-reconciliation-reports)
4. [Reconciliation Analytics](getting-started-with-recon.md#id-4.-reconciliation-analytics)
5. [Post Reconciliation run](getting-started-with-recon.md#id-5.-post-reconciliation-run)

### 1. Upload & prepare files

Efficient file management is at the core of Hyperswitch Recon's data integration process. This entire stage usually takes < 30 secs post file upload. Following are the 3-steps involved in preparing files for reconciliation —&#x20;

Upload, Validate, and Transform

#### **1.1 Upload**

The first phase of the process involves uploading your data files into the Reconciliation system. Hyperswitch Reconciliation provides multiple methods for this purpose:

* **Manual upload to the dashboard:** For ease of use, manually upload your files directly through the Reconciliation Dashboard.

{% hint style="info" %}
Files need to be uploaded in **PGName\_yyyymmdd/ MERCHANTNAME\_yyyymmdd/ BANK\_NAME\_yyyymmdd** format.
{% endhint %}

* **Automated upload to dashboard:** In order to feed your PSP and bank files to the Reconciliation module you can select one of the below options during configuration. In case of automated upload of files, case all subsequent steps are also executed in an automated fashion and the reconciliation output is generated.
  * Via Recon uploader API: The Reconciliation module can ingest reports via APIs in case the payment processor and banks support that feature. This feature needs to be enabled during the activation and configuration stage. In order to enable this feature the merchant will need to specify &#x20;
    * API endpoint, API keys and schedule
  * Via Merchant's SFTP: We allow files to be transferred to the Reconciliation module via pull based connection. You can specify a location where you'd place the files to be reconciled. Hyperswitch will pull the files from that location on a periodic basis using.an SFTP connection. This feature needs to be enabled during the activation and configuration. In order to enable this feature the merchant will need to specify&#x20;
    * &#x20;Portal User ID, Portal password and SFTP url and pick up schedule

Possible errors at this stage are:

* File naming convention error - The files need to be named as specified above to avoid any error in upload
* Invalid file format - The following file formats are supported - csv, excel and XML

#### **1.2 Validate**

After the files are uploaded, they enter the Validate phase, where records undergo validation to ensure data integrity. This phase involves a series of checks to vet records based on various conditions, including:

* **Column check:** Verify that all required columns are present and correctly formatted.
* **Data type validation:** Validate data types to ensure they conform to the expected format.
* **Duplicate value detection:** Identify and eliminate duplicate records to prevent redundancy.
* **Date format verification:** Ensure date values are correctly formatted and are consistent.
* **Other custom conditions:** Apply additional custom conditions relevant to your use case.

Records that fail any of these validation checks are identified and separated from the dataset. These failed records are not forwarded to subsequent steps, minimising the risk of inaccurate reconciliations.

Possible errors at this stage are:

* Report content invalid  - The format, structure and content of the files need to be in line with what was configured during the activation and configuration stage.

#### 1.3 Transform

The final stage of the File Management process is the Transform phase. In this phase, various computations and transformations are applied to the validated records to prepare them for reconciliation within the engine.&#x20;

* **Settled amount calculation:** Compute settled amounts based on transaction values and statuses.
* **Fee & tax computation:** These primarily include fees and tax calculations to enable us to reconcile the settlement report with the bank after deduction of these values. These transformations need to be enabled as part of the activation and configuration stage. In case those are not explicitly present in the payment processor's report, the merchant will need to specify them.

This below specified table indicates the progress and outcome across each section.&#x20;

* Yellow status :  The particular stage is being initiated for execution
* Green status : The particular stage is successfully executed&#x20;
* Red status : The particular stage has some errors which need to be rectified
* Partial Red status : Some of the records are invalid and have been excluded from the process

<figure><img src="broken-reference" alt=""><figcaption></figcaption></figure>

### 2. Run Reconciliation&#x20;

Once the files are uploaded and prepared, we need to run the reconciliation engine. In case of automated Reconciliation, the recon engine would move to the next step automatically. Automated reconciliation needs to be enabled during the activation and configuration stage. The Run Recon section is divided into 4 parts:

Date selection, File selection, Recon status and Engine capabilities&#x20;

<figure><img src="broken-reference" alt=""><figcaption></figcaption></figure>

#### 2.1 Date selection

Specify the dates for which you want to see the output of Reconciliation engine run. In case of both automated and manual Reconciliation, all the records would be picked for processing.

**2.2** **File selection**&#x20;

Select the files on which you need to run reconciliation. In case of automated Reconciliation this step is not needed&#x20;

#### 2.3 Recon status&#x20;

The Green status signifies that the reconciliation engine has run successfully

<figure><img src="broken-reference" alt=""><figcaption></figcaption></figure>

In case you face any errors at this stage please contact the Hyperswitch support team.

### 3. Reconciliation Reports

Once the uploaded files are processed by the Reconciliation engine, the output is shown on the Reports section. The Reports section is largely divided into 3 parts: &#x20;

Date selection, Reconciliation reports and Reconciliation output table

#### 3.1 Date selection&#x20;

It allows you to see the reconciliation status for any time window of your choice. The Reconciliation modules stores all the data that is ingested in it to ensure you have a view of reconciliation that's driven by dates or length-of-time.&#x20;

The reconciliation engine performs backdated reconciliation by reviewing entries from previous dates. If matching entries are found, reconciliation is seamlessly executed, ensuring historical accuracy. By default, the engine considers backdated entries spanning the last 90-days, configurable based on merchant needs.&#x20;

#### 3.2 Reconciliation reports

Within the Reports module, users can access an array of essential reports that cover various aspects of the reconciliation process:

* **Overall transaction report:** Gain a comprehensive view of reconciliation outcomes across all transactions.
* **Merchant transaction report:** Focus specifically on merchant-level transaction alignment.
* **PSP settlement report:** Analyse transaction reconciliation outcomes within the context of PSP settlements.
* **Bank settlement report:** Gain insights into transaction alignment concerning bank settlements.

#### 3.3 Reconciliation output table

The output table provides access to specific information categories such as Gateway, Status, and Sub-status. These intricate details enable users to dissect reconciliation outcomes based on diverse attributes, facilitating pinpoint analysis.&#x20;

-> Customisable column views: Users have the ability to customise their column views within the output table:

* **Select desired columns:** Choose which columns to view, tailoring the report to focus on specific attributes like transaction ID, amount, status, and reconciliation status.
* **Column naming:** Assign specific names to columns, enhancing clarity and alignment with your business's terminology. This change needs to be done by the Hyperswitch team.
* **Column positioning :** Assign a specific order to columns, enhancing clarity and alignment with your business' requirements . This change needs to be done by the Hyperswitch team.

-> Key columns and status definitions (these are the default names) :&#x20;

* **Recon status -** This is the reconciliation status between the Merchant report and the PSP report. Possible values are&#x20;
  * Matched : Transactions that are matched across systems.&#x20;
  * Mismatch: Transactions are present across the systems, but any of the fields, such as amount, tax, or currency, is mismatched.
  * Missing : Transactions which are not present in at least one of the files
* **Recon sub-status -** This column is available only for 3-way recon. Possible values are&#x20;
  * Matched: Transactions that are matched across systems.&#x20;
  * Probable\_match : Potential match for a transaction which is identified using the secondary identifier column.
  * Amount\_mismatch : Transactions that have matched, but there is a discrepancy in the amount. Merchants can configure column-level mismatch statuses while onboarding.
  * Missing : Transactions which are not present in both the systems but present in bank file
  * Missing\_in : Transactions which are not present in at least one system
* **Secondary status** - This is the reconciliation status between the PSP report and the Bank report. This column is available only for 3-way recon.  Possible values are similar to Recon status
* **Secondary sub-status** - This column is available only for 3-way recon. Possible values are similar to Recon sub status.&#x20;

In case of 3-way recon, the columns Recon status and Recon sub-status are used to indicate the reconciliation outcome of Hyperswitch and PSP file whereas columns secondary status and Secondary sub-status are used to indicate the reconciliation outcome of PSP and bank file. In case of 2-way recon a single column from the above is displayed along with the respective status.

-> Confidence score-potential matched : Recon happens on transaction identifiers however at times payment entities (banks, PSPs) share different identifiers for refund, split transactions etc. For such cases, Reconciliation module would check for a nearby match and assign a confidence score to that reconciled row.

-> Download Data : The reconciliation module allows merchants to download data in the form of excel.

### 4. Reconciliation Analytics

The Recon Dashboard is characterised by several components that facilitate analysis:

<figure><img src="broken-reference" alt=""><figcaption></figcaption></figure>

**4.1  User controls :** The merchant can specify the date, type of report (monthly, daily), PSP and settlement currency for which analytics should be displayed on dashboard.

**4.2 Statistical analytics :** This section contains of four components

* Matched - Number of transactions and total amount that have been matched across all the systems after reconciliation.&#x20;
* Matched buffer - A buffer amount can be set by the merchant during the activation and configuration stage. Number of transactions and total amount that have been matched with the buffer across all the systems after reconciliation.
* Mismatched - Number of transactions and total amount that have mismatched data in at least one of the systems.
* Not found - Number of transactions and total amount that have not been found in at least one system.

**4.3 Graphical analytics :** Bar graph representation of Number of transactions vs date range.

**4.4 Summary table :** This table contains information about pending amount from last period, amount expected, amount received and balance receivable for all PSP's after last reconciliation run.

* Balance last period : Balance left to receive from all previous reconciliation runs.
* Amount expected : Amount that is expected from PSP as per merchant report.
* Amount  received : Amount that is received from PSP  as per PSP report.
* Balance receivable : Sum of balance last period and difference between amount expected and amount received.

### 5. Post reconciliation run

Once the reconciliation engine has been executed, there maybe a few records which fall under the mismatched or missing category. &#x20;

1. Missing category&#x20;
   * Majority of records that fall in this category are essentially missed in one of the files due to different systems following different cut over times. To elaborate, PSP or bank or Hyperswitch will have their own cut over times for generating report, settling transactions etc. Therefore a few records may just be missed due to the difference in the cut over time.
   * The reconciliation engine performs backdated reconciliation by reviewing entries from previous dates. If matching entries are found, reconciliation is seamlessly executed, ensuring historical accuracy. By default, the engine considers backdated entries spanning the last 90-days, configurable based on merchant needs.&#x20;

Records that don't fall under the purview of the above examples will need to be investigated with the respective teams (Hyperswitch, PSP or bank). We are also working on a feature that will enable you to track and  close Reconciliation issues within the Reconciliation module ([Recon open issues](broken-reference)).
