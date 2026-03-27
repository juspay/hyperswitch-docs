---
icon: right-from-bracket
description: Import payment data securely from your current payment processor to Hyperswitch
---

# Import Data to Hyperswitch

We help you with smooth migration from your current payment processor, ensuring uninterrupted business operations.

## Performing the Import Data Process

1. **Merchant initiates a request** to our team for data import
2. We will share our PCI Attestation of Compliance (AoC) certificate to Merchant
3. **Merchant requests a data export** (for both customer records and associated payment data) from their current payment processor, by providing Hyperswitch's PCI AoC certificate
4. We will provide our public PGP key for Merchant's current payment processor to encrypt their export data
5. An encrypted CSV file containing all the export data needs to be sent through SFTP by Merchant's current payment processor
6. We will import the data
7. **Post migration** of data, we will send an updated customer-payment method reference IDs to Merchant

## Import File Format

The CSV file for import should be formatted in accordance with the following requirements:

- The first line contains the names of the fields
- Each subsequent line should contain the fields for a single record
- Delimit rows by a single newline character `\n` (not `\r\n`)
- Delimit columns by `,`
- Leave empty fields entirely empty (no character in between delimiters). You must not denote a missing field with NULL, N/A, or any other value
- Fields can't contain comma, newline characters `(\r or \n or ,)` within a field
  - Example of what to avoid: `1st Ave\nApt 1`
- All rows must have the same number of columns
- Field names and values are case-sensitive
- Multi-line fields are not allowed
- Save the file in UTF-8 format (to support non-western characters)
- Encrypt the file using the public PGP key provided by Hyperswitch

## To Import Card Data

### Required Fields

| **Field** | **Description** |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| card_number | Primary Account Number (PAN) of the customer card |
| card_expiry_month | Card expiry month |
| card_expiry_year | Card expiry year |
| payment_instrument_id | Unique reference ID of payment method saved (PSP token)<br><br>Note: This is required for mapping to Hyperswitch payment_method_id |
| original_network_transaction_id | Original Transaction ID of the first transaction where the customer signed up for recurring payments. For eg. Visa - Visa Transaction ID, Mastercard - Mastercard Trace ID.<br><br>Note: This is only required for connector agnostic MIT |

### Optional Fields

Note: Billing details are mandatorily required if AVS (Address Verification Service) check is enabled.

| **Field** | **Description** |
| ----------------------------- | ------------------------------------------------------------- |
| name | Name of the customer |
| email | Email id of the customer |
| payment_method | Payment method used by customer (Eg: card - for cards import) |
| payment_method_type | Payment method type used by the customer (eg: credit / debit) |
| card_scheme | Card network (Eg: Visa, Mastercard, American Express) |
| phone | Customer mobile number |
| phone_country_code | Country code of customer mobile number |
| billing_address_first_name | Customer First Name for billing address |
| billing_address_last_name | Customer Last Name for billing address |
| billing_email | Billing email id of the customer |
| billing_address_line1 | Street Name/Address Line 1 of the billing address |
| billing_address_line2 | Locality Name/Address Line 2 of the billing address |
| billing_address_city | City of the billing address |
| billing_address_state | State of the billing address |
| billing_address_zip | Postal code of the billing address |
| billing_address_country | Country of the billing address |

{% hint style="info" %}
To import other payment methods like SEPA, ACH, PayPal, Klarna, kindly reach out to [hyperswitch@juspay.in](mailto:hyperswitch@juspay.in)
{% endhint %}
