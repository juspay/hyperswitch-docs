# Payment Settings

## Payment settings

**Payment settings** is where you tune how payments behave: what checkout collects, how failed payments can be retried, which authentication and vault services to use, and where payment updates go.

Start by checking your **mode (Test/Live)** and **selected Business Profile**. Most settings on this page belong to that profile.&#x20;

***

### Open Payment settings

1. Go to **Developers → Payment settings**.
2. Check the merchant, profile, and mode you want to configure.
3. Open the relevant tab, make your changes, and click **Update**. Acquirer configuration forms use their own **Save** or **Update** buttons; blocklist actions also save separately.
4. Run a test payment that exercises the setting you changed.

The tabs you see depend on your account's enabled features, connected processors, and integration version.

| Tab                   | What you'll configure                                                       |
| --------------------- | --------------------------------------------------------------------------- |
| **Payment Behaviour** | Wallet details, retries, tokenization, and callback URLs                    |
| **3DS**               | Authentication preferences, authentication connectors, and acquirer details |
| **Vault**             | An external vault and the fields sent for tokenization                      |
| **Surcharge**         | The external service used to calculate surcharges                           |
| **Block List**        | Payment-method restrictions and blocked card identifiers                    |
| **Custom Headers**    | Extra HTTP headers on outgoing webhooks                                     |
| **Metadata Headers**  | Additional information stored on the profile                                |
| **Payment Link**      | The payment-link domain and sites allowed to embed links                    |

> **Can't see a tab?** Vault and Surcharge require the corresponding feature and a processor connected to the selected profile

### Check the profile details

The information at the top helps you confirm which profile you're editing.

<figure><img src="../../.gitbook/assets/Group 1.svg" alt=""><figcaption></figcaption></figure>

| Field                         | What it means                                                                                                                                                                                                          |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Profile Name**              | The display name of the selected Business Profile. Read-only on this page.                                                                                                                                             |
| **Profile ID**                | The profile's unique identifier. Use the copy icon when sharing it with your integration team.                                                                                                                         |
| **Merchant ID**               | The merchant account the profile belongs to.                                                                                                                                                                           |
| **Payment Response Hash Key** | The secret used to sign outgoing webhooks and, when enabled, payment redirect responses. The screen shortens the displayed value; the copy icon copies the full key. Keep it on your server when verifying signatures. |

***

### Payment Behaviour

#### Collect billing details from wallets

Choose whether supported wallets, such as Apple Pay and Google Pay, should collect billing details during checkout.

* **Off** — this setting does not request billing details from the wallet.
* **Only If Required By Connector** — collect details when the payment connector requires them.
* **Always** — request details regardless of the connector's required fields.

This controls wallet collection. It does not remove information your integration already supplies.

#### Collect shipping details from wallets

Use the same choices for shipping details: **Off**, **Only If Required By Connector**, or **Always**. For example, choose **Always** when you need a delivery address even if the payment processor doesn't require one.

#### Auto Retries

Allow Hyperswitch to retry eligible failed payments using the same payment details and the configured connector routing. Retries stop when a payment succeeds, the retry limit is reached, or no eligible retry remains.

The failure response and routing setup still determine whether a payment can be retried. Enabling this switch does not make every decline retryable.

#### Max Auto Retries

When **Auto Retries** is on, enter a whole number from **1 to 5**. This is the profile's maximum number of additional automatic attempts after the first attempt. A merchant-level retry configuration can take precedence over this value.

#### Manual Retries

Allow an eligible failed payment to be attempted again using its original payment ID. Your integration can reuse the payment details or supply a different payment method.

The payment must still be within its allowed retry window. This switch enables retry behaviour; saving it does not immediately retry existing failed payments.

#### Extended Authorization

Request a longer authorization window for supported payments. This is useful when you need more time between authorizing a payment and capturing it, such as when an order ships later.

The connector and payment method must support extended authorization. A payment-specific setting can override the profile default, and the actual authorization window depends on the processor.

#### Always Enable Overcapture

Allow supported, manually captured payments to capture more than the originally authorized amount, within the connector's limits. For example, a final amount may include an adjustment made after authorization.

The payment must use **manual capture**, and the connector must support overcapture. A payment-specific setting can override this profile default.

#### Connector Agnostic

Allow eligible **merchant-initiated transactions (MITs)**, such as recurring charges, to use a different connector from the original **customer-initiated transaction (CIT)**, according to your routing setup.

This requires compatible saved payment details and connector support. The backend's card flow checks for a stored network transaction ID. With the setting off, the documented default is to keep the MIT with the original connector.

#### Network Tokenization

Enable network tokenization for eligible card flows on the profile. A network token can be used in place of the card number in supported future transactions. Token creation and use also depend on the integration flow and processor support.

Network tokenization requires additional setup on the Hyperswitch side beyond enabling this toggle. Reach out to the Hyperswitch team to complete the setup

#### Account Updater

Account Updater is intended to keep saved card details current when a card expires, is replaced, or is reissued.

The control is currently **disabled on this page**.  Account Updater requires additional setup on the Hyperswitch side beyond enabling this toggle. Please reach out to the Hyperswitch team to enable this feature

#### Merchant Category Code

Select the **Merchant Category Code (MCC)** that describes your business. This four-digit classification supplies business-category information to payment processing and related routing flows.

The field appears when the debit-routing feature is enabled. Use the MCC agreed with your processor or acquirer.

#### Click to Pay

Enable Click to Pay for a supported checkout integration so customers can use cards saved with the service. This setting appears when the feature is enabled and your role can view connectors.

#### Click to Pay - Connector ID

When Click to Pay is on, select the configured authentication connector account that should handle it. The dropdown shows each connector's label and account ID. Choose the account provisioned for your Click to Pay setup.

#### Return URL

Enter the default URL where customers should land after a payment's redirect flow, such as `https://shop.example.com/payment-result`.

A return URL supplied for an individual payment takes precedence over this profile value. Use an HTTPS URL in Live mode.

#### Webhook URL

Enter the endpoint on your server that receives payment-event notifications, such as `https://api.example.com/hyperswitch/webhooks`.

Use HTTPS in Live mode. The screen asks you to contact the Hyperswitch team to allowlist the endpoint before activation. After saving, make a test payment and confirm that your server receives the event and verifies its signature.

***

### 3DS

Use this tab to configure authentication preferences and the external authentication services connected to your profile.

#### Force 3DS Challenge

Request a 3DS challenge for applicable authentication flows. A challenge asks the customer to actively authenticate, for example through their bank's app.

Payment-specific settings and 3DS decision rules can affect the final request; the authentication provider and issuer determine the resulting flow.

#### Authentication Connectors

Select the external authentication connectors to use for the profile. Connect an authentication processor first to make this section available.

#### 3DS Requestor URL

Enter your merchant website's requestor URL for external 3DS authentication, using the value agreed with your authentication provider. The field becomes editable after you select an authentication connector, and the form requires a valid URL when connectors are configured.

#### 3DS Requestor App URL

For a mobile-app integration, enter the URL or deep link that lets the authentication app return the customer to your merchant app after out-of-band authentication. For example, your integration might use `myshop://payment-authentication`.

This field is optional and becomes editable after you select an authentication connector.

#### Acquirer Config Settings

When enabled for your account, this section stores the merchant and network details needed by your acquirer configuration. It appears below the 3DS form in the v1 interface.

1. Click **Acquirer config group**.
2. Enter the merchant details and add the first card-network configuration.
3. Click **Save**.
4. Expand the group to add or edit network configurations.
5. To choose a different default group, click **Change Default**, select the group, and click **Save as Default**.

| Field                           | What to enter                                                                                                                                                               |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Acquirer merchant name**      | The merchant name associated with this acquirer configuration. Required when creating a group.                                                                              |
| **Acquirer Merchant ID**        | The merchant identifier assigned by the acquirer. Required when creating a group.                                                                                           |
| **Card Network**                | The network this configuration applies to. Required. A group can contain separate entries for different networks; an existing entry's network is locked while editing.      |
| **Acquirer BIN**                | The acquiring institution's identifier for the network. Required; the form accepts 4–20 digits.                                                                             |
| **Acquirer ICA (optional)**     | The ICA identifier supplied by your acquirer, where applicable.                                                                                                             |
| **Fraud Rate (%) (optional)**   | The fraud-rate value supplied for this acquirer configuration. The form accepts values from 0 to 100. Confirm the expected value with your authentication/integration team. |
| **Acquirer Country (optional)** | The country associated with the acquirer.                                                                                                                                   |
| **Default group**               | The fallback acquirer configuration group. The first group becomes the default when none exists.                                                                            |
| **Acquirer configuration ID**   | The generated ID displayed for the group. Use it to identify the configuration; it is separate from the acquirer-assigned merchant ID.                                      |

***

### Vault

The **Vault** tab connects the profile to an external vault. It appears when external vault processing is available and a vault processor is connected to the selected profile.

#### Enable External Vault

Turn this on to use the configured external vault for supported vaulting flows. Turning it off sets the profile to skip external vaulting and clears the external-vault details from the form.

#### Vault Connectors

Choose the connected vault account to use. Each option shows the connector label and account ID. A vault connector is required when external vaulting is enabled.

#### Vault Token

Select which fields to include in custom tokenization with the external vault. Available selections are listed below. Leaving the selection empty uses the standard vaulting payload rather than selecting no data.

| Option                         | Data selected                                                    |
| ------------------------------ | ---------------------------------------------------------------- |
| **Card Number**                | The card number field                                            |
| **Card Cvc**                   | The card security-code field, when present in the supported flow |
| **Card Expiry Year**           | The card's expiry year                                           |
| **Card Expiry Month**          | The card's expiry month                                          |
| **Network Token**              | The network token number                                         |
| **Network Token Cryptogram**   | The cryptogram associated with the network token                 |
| **Network Token Expiry Month** | The network token's expiry month                                 |
| **Network Token Expiry Year**  | The network token's expiry year                                  |

The selection controls the fields passed into the external vault's custom tokenization flow. Actual handling depends on the vault connector and the data available for the transaction.

***

### Surcharge

#### Surcharge Connectors

Select the connected surcharge service that should calculate external surcharges for supported payments on this profile, then click **Update**.

The tab appears when surcharge processing is enabled and the profile has a surcharge processor. This field selects the service; surcharge amounts depend on its configuration and the payment flow.

***

### Block List

Use this tab to restrict payments by card attributes or manage specific blocked BINs and fingerprints.

> **Before relying on blocking:** the backend blocklist guard must be enabled for your merchant. This page does not expose that switch. Confirm enablement with your integration team and test a payment that should be blocked. Adding an entry or saving a restriction alone does not verify enforcement.

#### Payment Method Blocking

Expand **Card**, **Apple Pay**, or **Google Pay** and configure the restrictions for that payment method. Each section has the same fields. Click **Update** to save.

Selections are values to **block**. A matching configured restriction can block a payment; the customer does not need to match every field. Rules rely on the card information available to Hyperswitch. Wallet rules also require access to the relevant decrypted token information.

| Field                                  | What it blocks                                                                                                                           |
| -------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **Issuing Country**                    | Cards issued in any selected country                                                                                                     |
| **Card Types**                         | Cards matching any selected type                                                                                                         |
| **Card Networks**                      | Cards on any selected network                                                                                                            |
| **Funding Sources**                    | Cards matching any selected funding-source classification                                                                                |
| **Card Segment Types**                 | Cards matching any selected segment classification                                                                                       |
| **Card Subtypes**                      | Cards matching any selected subtype                                                                                                      |
| **Block virtual cards**                | Cards identified as virtual in the BIN record                                                                                            |
| **Block non-reloadable prepaid cards** | Cards marked as prepaid and not reloadable                                                                                               |
| **Block gambling BINs**                | Cards whose BIN record carries the gambling-blocked flag                                                                                 |
| **Block if BIN info unavailable**      | Payments for which Hyperswitch cannot find the applicable BIN record. With this off, a missing record does not itself trigger this rule. |

#### Check, add, or remove an entry

When the additional Blocklist tools are enabled, you can manage individual card identifiers.

* **Check Blocklist** — enter a value in **Data** and click **Check** to see whether that exact entry is blocked under any supported entry type. This lookup checks stored entries; it is not a simulation of all payment-method rules.
* **Add to Blocklist** — choose a **Type**, enter **Data**, and click **Add Entry**.
* **Remove from Blocklist** — choose a **Type**, enter the blocked **Data**, and click **Remove Entry**.

| Field                       | What to enter                                                                                      |
| --------------------------- | -------------------------------------------------------------------------------------------------- |
| **Type**                    | **Generic Card BIN** for a card-number prefix, or **Fingerprint** for a payment-method fingerprint |
| **Data — Generic Card BIN** | A numeric prefix of **6–10 digits**, such as `411111`                                              |
| **Data — Fingerprint**      | The fingerprint identifier to add or remove                                                        |
| **Data — Check Blocklist**  | The exact BIN or fingerprint to look up, up to **20 characters**                                   |

#### Upload a CSV

For multiple entries, click **Download Sample File**, fill it in, choose the file, and click **Upload**.

Use a `.csv` file with up to **100,000 data rows**, excluding the header, and a maximum size of **5 MB** as shown in the screen. The limit is 5 × 1,024 × 1,024 bytes.

```csv
type,data,metadata
generic_card_bin,411111,source=fraud_team;reason=chargeback
fingerprint,fp_abc123,
```

| CSV field    | What it contains                                                                                                        |
| ------------ | ----------------------------------------------------------------------------------------------------------------------- |
| **type**     | The identifier type. Use `generic_card_bin` or `fingerprint` for the current UI's types.                                |
| **data**     | The BIN prefix or fingerprint to block. Preserve BINs as text when editing in a spreadsheet.                            |
| **metadata** | Optional context in `key=value` format, with multiple pairs separated by semicolons. Leave the value empty when unused. |

#### Counts, jobs, and exports

The summary shows blocked **Card BINs** or a breakdown such as **6-digit BINs**, plus **Fingerprints**. Refresh the page after adding or removing entries to update these counts.

Click **Generate Export** to create a CSV of the profile's blocklist. Track uploads and exports in the jobs table, refresh active jobs, and download an export once it is ready.

| Field                               | What it tells you                                                        |
| ----------------------------------- | ------------------------------------------------------------------------ |
| **Card BINs / digit-length counts** | The number of blocked BIN entries, with a length breakdown when supplied |
| **Fingerprints**                    | The number of blocked fingerprint entries                                |
| **Job ID**                          | The identifier for the upload or export job                              |
| **Type**                            | Whether the job is an upload or an export                                |
| **Status**                          | The job's state: Initiated, Processing, Completed, or Failed             |
| **Total Rows**                      | The job's reported row count                                             |
| **Succeeded**                       | Successfully processed upload rows; exports show a dash                  |
| **Failed**                          | Failed upload rows; exports show a dash                                  |
| **Created At**                      | When the job was created                                                 |
| **Updated At**                      | When the job was last updated                                            |

***

### Custom Headers

Add HTTP headers that Hyperswitch should include when sending outgoing webhooks to your server. For example, your webhook receiver may expect an `X-Webhook-Token` header.

The form provides **four key/value pairs**.

| Field     | What to enter                                                                                                    |
| --------- | ---------------------------------------------------------------------------------------------------------------- |
| **Key**   | The HTTP header name. Use a valid name without spaces, up to 64 characters; the UI rejects purely numeric names. |
| **Value** | The value your webhook receiver expects for that header.                                                         |

To replace a saved configuration, click **Edit → Proceed**, enter the full set of headers you want to retain, and click **Update**. Proceeding clears the current header values from the edit form, so include every header you still need before saving.

***

### Metadata Headers

This tab stores additional **profile metadata**, such as an internal business-unit name or integration reference. The section is titled **Custom Metadata Headers** and provides **two key/value pairs**.

| Field     | What to enter                                             |
| --------- | --------------------------------------------------------- |
| **Key**   | A name for the profile attribute, such as `business_unit` |
| **Value** | Its string value, such as `online_store`                  |

Click **Edit → Proceed** to change an existing configuration, then **Update** to save. These values are saved on the profile. Use **Custom Headers** when you need to add HTTP headers to outgoing webhooks.

***

### Payment Link

Use **Payment Link Domain** to configure where your payment links are hosted and which sites may embed them.

#### Domain Name

Enter the domain used to generate payment links, such as `pay.example.com`. Enter the hostname without `https://` or a path; the backend builds an HTTPS base URL from it.

Arrange the domain's hosting, DNS, and certificate setup with your integration team before using it. Saving this value selects the domain used in links.

#### Allowed Domain

Enter the site or sites allowed to embed payment links. For multiple sites, use a comma-separated list without spaces, for example `shop.example.com,checkout.example.com`.

When changing existing values, click **Edit → Proceed**, update the fields, and click **Update**. The current form validates both **Domain Name** and **Allowed Domain**, so supply both when saving this section.

***

### Check your changes

Choose a test that matches what you changed:

* **Wallet details** — open the relevant wallet and check the billing or shipping details requested.
* **Retries** — use an eligible test failure and inspect the payment's attempts.
* **3DS** — run a supported authentication test and check the resulting flow.
* **Webhooks** — confirm your endpoint receives the event, verifies the signature, and sees any custom headers.
* **Blocking** — test an identifier or attribute you expect to be blocked, after confirming guard enablement.
* **Payment links** — open a generated link and test embedding it from an allowed site.

If the result is unexpected, first confirm the **profile and mode**, then check the payment's own settings and the connected processor's capabilities.

***
