---
description: Export your payments data to Redshift from Hyperswitch
icon: tachograph-digital
---

# Exporting payments data

Exporting your payments data to Amazon Redshift enhances analytics by leveraging Redshift's high-performance query capabilities. This allows for efficient data analysis, reporting, and business intelligence there by deriving valuable insights

## Architecture

<figure><img src="https://lh7-us.googleusercontent.com/WzE4ZW_U-xsElfE6iZ0f5tu4Br-2gyGF9AakdL0RervgWtWE_myxps_Z1EEQySF8xcAME5h4UNogQOcJVo0AOn_pMXeSsNOiaPEGyn89v-MmgONxoEqAAPue7tm1bOrV9P9tHF1nuGrJQMEdgAnUF8g" alt=""><figcaption></figcaption></figure>

## Integration steps

1. &#x20;Prerequisite: You need to have an AWS account with redshift enabled. More details can be found here [https://aws.amazon.com/redshift/](https://aws.amazon.com/redshift/)
2.  You are required to create a new IAM role for Redshift use and provide Hyperswitch with the corresponding role ARN. This IAM role must be configured with S3 read permissions.\


    <figure><img src="https://lh7-us.googleusercontent.com/r4vnr22w42Pz2k5V7O7TsVBrlVhDrfjYveoH-CWMnJW9XNR95k0XmJBlC9Q7lb1mpJa7aFyf9fRDDf6SHBoSLs-BP-TriQfwG57j3XhsdeJEW417zi0UO2069oDcxPEdzifYm_alen5GJsCGWhYOL2g" alt=""><figcaption><p>Example image of an IAM role created</p></figcaption></figure>
3. After sharing the ARN with Hyperswitch, We will share the S3 bucket & path that is to be synced for data along with providing access to the IAM role from where you will be able to get files from the S3
4.  Once the above step is done, you need to [create the table schema on Redshift](https://opensource.hyperswitch.io/features/account-management/exporting-payments-data#table-creation-schema)

    Post which you can proceed with the below

    1. [Handle the ingestion & post processing of data](https://opensource.hyperswitch.io/features/account-management/exporting-payments-data#table-creation-schema) using scripts

    (OR)

    2. [Auto-ingestion using Redshift](https://opensource.hyperswitch.io/features/account-management/exporting-payments-data#table-creation-schema)

## File format and paths specifications

1. The files will be plain csv files with 1st row being a header
2. The file path would look be s3://\<bucket>/\<merchant\_id>/\<version>/\<payments>/\<date>.csv
3. There will be one csv file corresponding to each day upto 7 days. Updates to the payments data will be in-place
4. Changes to file formats, content or likewise would change the version in the above path and would be communicated.

## Data updation frequency & retention:

| Data update schedule        | 6 hours frequency up to 7 days                                                                                                        |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| Data retention on S3 folder | 7 days                                                                                                                                |
| Type of data exposed        | payments as per [schema](https://opensource.hyperswitch.io/features/account-management/exporting-payments-data#table-creation-schema) |
| Data storage location       | us-east-1                                                                                                                             |

## Auto ingestion using Redshift

1. Redshift supports ingesting csv data directly from S3 files which we’ll rely on.
2. The ingestion to redshift would happen via a COPY job, this can be automated via the following options
   1. You can use the [auto copy job](https://docs.aws.amazon.com/redshift/latest/dg/loading-data-copy-job.html) if running a preview cluster
   2. Or the more mainstream [lambda loader](https://github.com/awslabs/aws-lambda-redshift-loader)

## Table creation/schema

```sql
CREATE TABLE payments (
  payment_id VARCHAR(64),
  attempt_id VARCHAR(64),
  status TEXT,
  amount INTEGER,
  currency VARCHAR(10),
  amount_to_capture INTEGER,
  customer_id VARCHAR(64),
  created_at TIMESTAMP,
  order_details VARCHAR(255),
  connector VARCHAR(255),
  error_message VARCHAR(255),
  connector_transaction_id VARCHAR(255),
  capture_method VARCHAR(255),
  authentication_type VARCHAR(255),
  mandate_id VARCHAR(64),
  payment_method VARCHAR(255),
  payment_method_type TEXT,
  metadata TEXT,
  setup_future_usage TEXT,
  statement_descriptor_name TEXT,
  description TEXT,
  off_session TEXT,
  business_country TEXT,
  business_label TEXT,
  business_sub_label TEXT,
  allowed_payment_method_types TEXT
);

```

## Ingesting data from S3

```sql
create temp table payments_stage (like payments);

copy payments_stage from 's3://<BUCKET_NAME>/<MERCHANT_ID>/<VERSION>/payments' 
credentials 'aws_iam_role=<ARN_ROLE>'
IGNOREHEADER 1
timeformat 'YYYY-MM-DD HH:MI:SS'
csv;

MERGE INTO payments USING payments_stage ON payments.payment_id = payments_stage.payment_id
WHEN MATCHED THEN UPDATE SET
payment_id = payments_stage.payment_id,
attempt_id = payments_stage.attempt_id,
status = payments_stage.status,
amount = payments_stage.amount,
currency = payments_stage.currency,
amount_to_capture = payments_stage.amount_to_capture,
customer_id = payments_stage.customer_id,
created_at = payments_stage.created_at,
order_details = payments_stage.order_details,
connector = payments_stage.connector,
error_message = payments_stage.error_message,
connector_transaction_id = payments_stage.connector_transaction_id,
capture_method = payments_stage.capture_method,
authentication_type = payments_stage.authentication_type,
mandate_id = payments_stage.mandate_id,
payment_method = payments_stage.payment_method,
payment_method_type = payments_stage.payment_method_type,
metadata = payments_stage.metadata,
setup_future_usage = payments_stage.setup_future_usage,
statement_descriptor_name = payments_stage.statement_descriptor_name,
description = payments_stage.description,
off_session = payments_stage.off_session,
business_country = payments_stage.business_country,
business_label = payments_stage.business_label,
business_sub_label = payments_stage.business_sub_label,
allowed_payment_method_types = payments_stage.allowed_payment_method_types
WHEN NOT MATCHED THEN INSERT VALUES (
payments_stage.payment_id,
payments_stage.attempt_id,
payments_stage.status,
payments_stage.amount,
payments_stage.currency,
payments_stage.amount_to_capture,
payments_stage.customer_id,
payments_stage.created_at,
payments_stage.order_details,
payments_stage.connector,
payments_stage.error_message,
payments_stage.connector_transaction_id,
payments_stage.capture_method,
payments_stage.authentication_type,
payments_stage.mandate_id,
payments_stage.payment_method,
payments_stage.payment_method_type,
payments_stage.metadata,
payments_stage.setup_future_usage,
payments_stage.statement_descriptor_name,
payments_stage.description,
payments_stage.off_session,
payments_stage.business_country,
payments_stage.business_label,
payments_stage.business_sub_label,
payments_stage.allowed_payment_method_types
);

drop table payments_stage;
```

The above query creates a temporary table to load all the csv data & then merges this with the main table while deduplicating based on payment\_id

## Self-Setup Guide for AWS

If you want to set up payment data export at your end using AWS infrastructure, you can implement your own data pipeline. This approach gives you full control over the data export process and allows customization based on your specific requirements.

### Architecture Overview

The self-setup approach involves three main components:

1. **Lambda Function/Server**: Queries payment data for the past 7 days from your Hyperswitch database
2. **Scheduled Execution**: A cron job or EventBridge rule that invokes the Lambda with merchant-specific parameters
3. **S3 Storage**: Stores the exported data with proper IAM role-based access control

### Step 1: Create S3 Bucket and Configure Access

First, set up the S3 bucket where payment data will be stored:

```bash
# Create S3 bucket
aws s3 mb s3://your-payments-export-bucket --region us-east-1

# Create IAM policy for S3 access
aws iam create-policy --policy-name PaymentsExportS3Policy --policy-document '{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject",
        "s3:DeleteObject"
      ],
      "Resource": "arn:aws:s3:::your-payments-export-bucket/*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "s3:ListBucket"
      ],
      "Resource": "arn:aws:s3:::your-payments-export-bucket"
    }
  ]
}'
```

### Step 2: Create Lambda Function for Data Export

Create a Lambda function that handles the data export logic:

**Function Requirements:**
- Query payment data from your Hyperswitch database for the past 7 days
- Filter data based on merchant_id parameter received from the event
- Generate CSV files with the same schema as mentioned in the table creation section
- Upload the CSV files to S3 with the path format: `s3://bucket/merchant_id/v1/payments/date.csv`
- Handle database connections, error handling, and logging

**Environment Variables Needed:**
- Database connection details (host, name, user, password)
- S3 bucket name
- Any API endpoints if using Hyperswitch APIs instead of direct DB access

**Deployment:**
You can deploy this Lambda function using AWS CLI, SAM, or the AWS Console with appropriate IAM permissions for S3 and database access.

### Step 3: Set Up Scheduled Execution

Create an EventBridge rule to trigger the Lambda function periodically:

```bash
# Create EventBridge rule for every 6 hours
aws events put-rule \
  --name payment-export-schedule \
  --schedule-expression "rate(6 hours)" \
  --description "Trigger payment data export every 6 hours"

# Add Lambda as target
aws events put-targets \
  --rule payment-export-schedule \
  --targets "Id"="1","Arn"="arn:aws:lambda:us-east-1:YOUR-ACCOUNT-ID:function:payment-export-lambda","Input"='{"merchant_id":"merchant_123","date_range":7}'

# Grant EventBridge permission to invoke Lambda
aws lambda add-permission \
  --function-name payment-export-lambda \
  --statement-id allow-eventbridge \
  --action lambda:InvokeFunction \
  --principal events.amazonaws.com \
  --source-arn arn:aws:events:us-east-1:YOUR-ACCOUNT-ID:rule/payment-export-schedule
```

### Step 4: Configure IAM Roles and Access

Create appropriate IAM roles for different components:

#### Lambda Execution Role:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "arn:aws:logs:*:*:*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "s3:PutObject",
        "s3:GetObject"
      ],
      "Resource": "arn:aws:s3:::your-payments-export-bucket/*"
    }
  ]
}
```

#### Data Access Role (for consumers):

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::your-payments-export-bucket",
        "arn:aws:s3:::your-payments-export-bucket/*"
      ],
      "Condition": {
        "StringEquals": {
          "aws:PrincipalAccount": "YOUR-TRUSTED-ACCOUNT-ID"
        }
      }
    }
  ]
}
```

### Step 5: Multi-Merchant Support

For handling multiple merchants, modify the EventBridge configuration:

```bash
# Create separate rules for each merchant
aws events put-rule \
  --name payment-export-merchant-123 \
  --schedule-expression "rate(6 hours)" \
  --description "Export for merchant 123"

aws events put-targets \
  --rule payment-export-merchant-123 \
  --targets "Id"="1","Arn"="arn:aws:lambda:us-east-1:YOUR-ACCOUNT-ID:function:payment-export-lambda","Input"='{"merchant_id":"merchant_123"}'

# Or use a single rule with different inputs
aws events put-targets \
  --rule payment-export-schedule \
  --targets file://merchant-targets.json
```

Where `merchant-targets.json` contains:

```json
[
  {
    "Id": "1",
    "Arn": "arn:aws:lambda:us-east-1:YOUR-ACCOUNT-ID:function:payment-export-lambda",
    "Input": "{\"merchant_id\":\"merchant_123\"}"
  },
  {
    "Id": "2", 
    "Arn": "arn:aws:lambda:us-east-1:YOUR-ACCOUNT-ID:function:payment-export-lambda",
    "Input": "{\"merchant_id\":\"merchant_456\"}"
  }
]
```

### Data Access and Security

Once the data is in S3, you can control access using:

1. **IAM Roles**: Grant specific roles access to the S3 bucket
2. **Bucket Policies**: Define fine-grained access controls
3. **Cross-Account Access**: Allow trusted AWS accounts to access the data

#### Example Cross-Account Bucket Policy:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "CrossAccountAccess",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::TRUSTED-ACCOUNT-ID:role/DataAnalysisRole"
      },
      "Action": [
        "s3:GetObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::your-payments-export-bucket",
        "arn:aws:s3:::your-payments-export-bucket/*"
      ]
    }
  ]
}
```

### Monitoring and Alerting

Set up CloudWatch alarms to monitor the export process:

```bash
# Create alarm for Lambda failures
aws cloudwatch put-metric-alarm \
  --alarm-name payment-export-failures \
  --alarm-description "Alert on Lambda function failures" \
  --metric-name Errors \
  --namespace AWS/Lambda \
  --statistic Sum \
  --period 300 \
  --threshold 1 \
  --comparison-operator GreaterThanOrEqualToThreshold \
  --dimensions Name=FunctionName,Value=payment-export-lambda \
  --evaluation-periods 1
```

### Cost Considerations

- **Lambda**: Charges based on requests and execution time
- **S3**: Storage and request costs
- **EventBridge**: Minimal costs for rule executions
- **Data Transfer**: Consider costs if accessing from different regions

This self-setup approach provides flexibility and control over your payment data export process while maintaining security and scalability.
