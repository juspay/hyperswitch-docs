---
description: Find answers to common questions about Hyperswitch setup, configuration, and troubleshooting using the frequently asked questions configuration.
---
# Frequently Asked Questions

## Mobile SDKs

<details>

<summary>How do I integrate Hyperswitch iOS SDK with my Swift or Objective-C app?</summary>

Integrate the Juspay Hyperswitch iOS SDK using CocoaPods. The SDK requires iOS 15.1 or later and supports Swift and SwiftUI implementations.

**Integration steps**

1. Add the Hyperswitch SDK to your Podfile.

pod 'hyperswitch-sdk-ios'

2. Install dependencies.

pod install

3. Initialize the SDK with your publishable key.

import Hyperswitch\
paymentSession = PaymentSession(publishableKey: \<YOUR\_PUBLISHABLE\_KEY>)

4. For open source deployments, configure custom backend endpoints.

paymentSession = PaymentSession(\
publishableKey: \<YOUR\_PUBLISHABLE\_KEY>,\
customBackendUrl: \<YOUR\_SERVER\_URL>,\
customLogUrl: \<YOUR\_LOG\_URL>\
)

5. Create the payment session on your backend to generate the client secret.
6. Initialize the payment session with the client secret and present the payment sheet.

Documentation:\
[https://docs.hyperswitch.io/explore-hyperswitch/payment-experience/payment/mobile/ios/swift-with-rest-api-integration](https://docs.hyperswitch.io/explore-hyperswitch/payment-experience/payment/mobile/ios/swift-with-rest-api-integration)

</details>

<details>

<summary>How do I integrate Hyperswitch Android SDK with my Kotlin or Java app?</summary>

Integrate the Juspay Hyperswitch Android SDK using Gradle. The SDK requires Android 7.0 (API level 24) or later, Android Gradle Plugin 8.13 or later, and AndroidX.

**Integration steps**

1. Add the classpath to your project-level build.gradle.

buildscript {\
 dependencies {\
  classpath "io.hyperswitch:hyperswitch-gradle-plugin:$latest\_version"\
 }\
}

2. Add the plugin to your app-level build.gradle.

plugins {\
 id 'io.hyperswitch.plugin'\
}

3. Configure SDK options.

hyperswitch {\
 sdkVersion = "1.1.5"\
 features = \[HyperFeature.SCANCARD, HyperFeature.NETCETERA]\
}

4. Implement HyperInterface in your Activity and initialize PaymentSession.

val paymentSession = PaymentSession(applicationContext, "YOUR\_PUBLISHABLE\_KEY")

5. Present the payment sheet and handle results.

Documentation:\
[https://docs.hyperswitch.io/explore-hyperswitch/payment-experience/payment/mobile/android/kotlin-with-rest-api-integration](https://docs.hyperswitch.io/explore-hyperswitch/payment-experience/payment/mobile/android/kotlin-with-rest-api-integration)

</details>

<details>

<summary>How do I migrate from Stripe iOS or Android SDK to Hyperswitch?</summary>

Hyperswitch provides a migration path from Stripe SDK integrations.

**iOS migration**

Install dependencies.

npm install @juspay-tech/react-native-hyperswitch @juspay-tech/hyper-node

Update server-side import.

From:\
const stripe = require("stripe")("your\_stripe\_api\_key");

To:\
const stripe = require("@juspay-tech/hyper-node")("your\_hyperswitch\_api\_key");

Update Podfile sources.

source '[https://github.com/juspay/hyperswitch-pods.git](https://github.com/juspay/hyperswitch-pods.git)'\
source '[https://cdn.cocoapods.org/](https://cdn.cocoapods.org/)'

Replace Stripe dependency.

From:\
pod 'StripePaymentSheet'

To:\
pod 'hyperswitch', '1.0.0-alpha01'

Update imports from StripePaymentSheet to hyperswitch.

**Android migration**

Install dependency.

npm install @juspay-tech/hyperswitch-node

Replace dependency.

From:\
implementation 'com.stripe:stripe-android:20.27.3'

To:\
implementation 'io.hyperswitch:hyperswitch-android:1.0.1'

Update imports from com.stripe.android.\* to io.hyperswitch.\*.

Documentation:\
[https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/migrate-from-stripe/ios](https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/migrate-from-stripe/ios)\
[https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/migrate-from-stripe/android](https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/migrate-from-stripe/android)

</details>

<details>

<summary>What mobile-specific payment flows are supported?</summary>

Hyperswitch supports multiple wallet payment methods on mobile.

**Apple Pay**

• Available in 75+ countries\
• Supported on iOS (in-app) and Web (Safari)\
• Requires Apple Developer Account, Merchant ID, and domain verification\
• Supports both Hyperswitch decryption and PSP decryption flows

**Google Pay**

• Available in 70+ countries on Web and Android\
• iOS support limited to US and India\
• Supports in-app and web transactions\
• Requires Google Pay test cards for sandbox testing\
• Production deployment requires Google approval

**Other wallets**

• PayPal\
• Samsung Pay

The Android SDK also provides widgets for Google Pay, PayPal, and Express Checkout.

Documentation:\
[https://docs.hyperswitch.io/explore-hyperswitch/wallets/apple-pay](https://docs.hyperswitch.io/explore-hyperswitch/wallets/apple-pay)\
[https://docs.hyperswitch.io/explore-hyperswitch/wallets/google-pay](https://docs.hyperswitch.io/explore-hyperswitch/wallets/google-pay)

</details>

<details>

<summary>How do I handle deep linking for mobile redirects such as 3DS or wallets?</summary>

Hyperswitch supports native 3DS authentication designed to minimize redirections.

**Native 3DS authentication**

• In-line 3DS challenge flows\
• Frictionless authentication using risk-based evaluation\
• Native OTP experience instead of web views

External 3DS providers such as Netcetera and 3DSecure.io can be integrated.

**Redirect flow handling**

The SDK automatically handles redirects for:

• 3DS card payments\
• Bank redirects such as iDEAL, Giropay, eps\
• Wallet flows such as PayPal and Klarna\
• Bank transfer flows

Documentation:\
[https://docs.hyperswitch.io/explore-hyperswitch/workflows/3ds-decision-manager/native-3ds-authentication-for-mobile-payments](https://docs.hyperswitch.io/explore-hyperswitch/workflows/3ds-decision-manager/native-3ds-authentication-for-mobile-payments)

</details>

<details>

<summary>Can I customize the payment sheet appearance on mobile?</summary>

Yes. Hyperswitch provides customization options for payment sheet UI on both iOS and Android.

**Fonts**

Configure custom fonts using:

• typography.fontResId on Android\
• configuration.appearance.font.base on iOS

**Colors**

appBarIcon — icons in payment page\
component — background of inputs\
componentBorder — border color for components\
error — error message colors\
primary — primary theme color\
surface — payment page background\
placeholderText — input placeholder text

**Shapes**

cornerRadiusDp — corner radius for input fields\
borderStrokeWidthDp — border width for components

Example Android configuration:

val appearance = PaymentSheet.Appearance(\
 typography = PaymentSheet.Typography(10.0f, R.font.MY\_FONT)\
)

Documentation:\
[https://docs.hyperswitch.io/explore-hyperswitch/payment-experience/payment/mobile/android/customization](https://docs.hyperswitch.io/explore-hyperswitch/payment-experience/payment/mobile/android/customization)\
[https://docs.hyperswitch.io/explore-hyperswitch/payment-experience/payment/mobile/ios/customization](https://docs.hyperswitch.io/explore-hyperswitch/payment-experience/payment/mobile/ios/customization)

</details>

<details>

<summary>What is the SDK size and performance impact on mobile apps?</summary>

Hyperswitch provides two SDK variants.

**Lite SDK**

• Artifact size under 300 KB\
• Web-based UI components\
• Minimal dependencies\
• Faster initialization\
• Full payment processing capabilities

**Full SDK**

• Larger artifact size\
• Native UI components\
• Additional features including card scanning and Netcetera 3DS

**Platform requirements**

Android — 7.0 (API 24)\
Android Lite — 6.0 (API 23)\
iOS — 15.1

Documentation:\
[https://docs.hyperswitch.io/explore-hyperswitch/payment-experience/payment/mobile/android/lite-sdk](https://docs.hyperswitch.io/explore-hyperswitch/payment-experience/payment/mobile/android/lite-sdk)\
[https://docs.hyperswitch.io/explore-hyperswitch/payment-experience/payment/mobile/ios/lite-sdk](https://docs.hyperswitch.io/explore-hyperswitch/payment-experience/payment/mobile/ios/lite-sdk)

</details>

## Testing & Sandbox

<details>

<summary>How do I set up and configure a sandbox environment for testing?</summary>

Juspay Hyperswitch provides multiple ways to set up a sandbox environment depending on your development workflow.

#### Option A: Hyperswitch Cloud Sandbox

You can use the hosted sandbox environment through the Hyperswitch dashboard.

Sandbox URL\
[https://sandbox.hyperswitch.io](https://sandbox.hyperswitch.io)

SDK sandbox endpoint\
[https://beta.hyperswitch.io/v1](https://beta.hyperswitch.io/v1)

Publishable keys for sandbox environments start with:

pk\_snd\_

#### Option B: Local setup using Docker

Clone the Hyperswitch repository and run the setup script.

git clone --depth 1 --branch latest [https://github.com/juspay/hyperswitch](https://github.com/juspay/hyperswitch)\
cd hyperswitch\
scripts/setup.sh

This launches the following components:

• Hyperswitch backend\
• Control Centre\
• SDK frontend

#### Option C: Individual component setup

You can also run the backend, control centre, and SDK components independently using the development environment setup guides.

Typical configuration steps include:

• Configure payment processors through the **Connectors** tab in the Control Centre\
• Use dummy processors such as **fauxpay** for testing without real PSP credentials\
• Configure routing rules through **Workflow → Routing**

Documentation:\
[https://docs.hyperswitch.io/hyperswitch-open-source/overview/unified-local-setup-using-docker](https://docs.hyperswitch.io/hyperswitch-open-source/overview/unified-local-setup-using-docker)\
[https://docs.hyperswitch.io/hyperswitch-open-source/account-setup](https://docs.hyperswitch.io/hyperswitch-open-source/account-setup)

</details>

<details>

<summary>What test card numbers are available for different scenarios (success, decline, 3DS)?</summary>

Hyperswitch provides dummy connector test cards for common payment scenarios.

#### Successful payments

Visa\
4111111111111111\
4242424242424242

Mastercard\
5555555555554444

Diners Club\
38000000000006

American Express\
378282246310005

Discover\
6011111111111117

#### Decline scenarios

Card declined\
4000000000000002

Insufficient funds\
4000000000009995

Lost card\
4000000000009987

Stolen card\
4000000000009979

#### 3DS flows

3DS success\
4000003800000446

For dummy connector cards:

• Expiry date can be any future date\
• CVV can be any valid value

Documentation:\
[https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/payment-methods-setup/test-credentials](https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/payment-methods-setup/test-credentials)

</details>

<details>

<summary>How do I simulate specific error codes and decline scenarios for testing?</summary>

Error scenarios can be simulated using dummy connector card numbers.

#### Example test cards

Generic decline\
4000000000000002

Insufficient funds\
4000000000009995

Lost card\
4000000000009987

Stolen card\
4000000000009979

Hyperswitch standardizes upstream processor error codes into common enums such as:

• insufficient\_funds\
• expired\_card\
• card\_declined\
• risk\_decline

This allows merchants to handle errors consistently across multiple payment processors.

Documentation:\
[https://api-reference.hyperswitch.io/essentials/error\_codes](https://api-reference.hyperswitch.io/essentials/error_codes)

</details>

<details>

<summary>How do I test 3D Secure authentication flows in sandbox?</summary>

3D Secure authentication flows can be tested using sandbox test cards.

#### Test card

3DS success\
4000003800000446

#### Testing the 3DS Intelligence Engine

You can configure custom 3DS exemption rules through the Hyperswitch Control Centre.

Navigate to:

Workflow → 3DS Exemption Rules

Example rule conditions include:

• Issuer country\
• Transaction amount\
• Card network\
• Customer device type

A demo playground is available for testing 3DS authentication scenarios:

[https://demostore3ds.netlify.app/](https://demostore3ds.netlify.app/)

Documentation:\
[https://docs.hyperswitch.io/explore-hyperswitch/workflows/3ds-decision-manager](https://docs.hyperswitch.io/explore-hyperswitch/workflows/3ds-decision-manager)

</details>

<details>

<summary>How do I test webhook handling locally during development?</summary>

To test webhook integrations locally:

1. Create an HTTP or HTTPS endpoint on your server to receive webhooks.
2. Configure the endpoint in the Hyperswitch Control Centre.

Navigate to:

Developer → Payment Settings → Webhook Setup

#### Webhook endpoints

Sandbox\
sandbox.hyperswitch.io/webhooks/{merchant\_id}/{merchant\_connector\_id}

Production\
api.hyperswitch.io/webhooks/{merchant\_id}/{merchant\_connector\_id}

#### Signature verification

Webhook payloads include an HMAC signature header:

x-webhook-signature-512

To verify the signature:

1. Encode the webhook payload as JSON.
2. Generate an HMAC-SHA512 signature using the **payment\_response\_hash\_key**.
3. Compare the generated signature with the header value.

#### Retry behavior

If a webhook delivery does not return an HTTP 2XX response, Hyperswitch retries delivery for up to **24 hours**.

Documentation:\
[https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/webhooks](https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/webhooks)

</details>

<details>

<summary>What are the differences between sandbox and production environments?</summary>



| Aspect                 | Sandbox                | Production         |
| ---------------------- | ---------------------- | ------------------ |
| API URL                | sandbox.hyperswitch.io | api.hyperswitch.io |
| SDK Endpoint           | beta.hyperswitch.io/v1 | api.hyperswitch.io |
| Publishable key prefix | pk\_snd\_              | pk\_prd\_          |
| Connector credentials  | Test credentials       | Live credentials   |
| Transactions           | Test transactions      | Real payments      |

Going live checklist

Before switching to production:

• Sign the Hyperswitch services agreement\
• Configure production connectors with live credentials\
• Enable payment methods on processor dashboards\
• Secure API keys and avoid exposing them in frontend applications\
• Configure webhook endpoints\
• Implement error handling and validation for payment responses

Documentation:\
[https://docs.hyperswitch.io/check-list-for-production/going-live](https://docs.hyperswitch.io/check-list-for-production/going-live)



</details>

<details>

<summary>What test bank account numbers are available for ACH or SEPA testing?</summary>

Hyperswitch supports several bank debit methods depending on region.

| Method | Region         | Currency | Settlement time        |
| ------ | -------------- | -------- | ---------------------- |
| ACH    | United States  | USD      | Up to 4 business days  |
| SEPA   | European Union | EUR      | Up to 14 business days |
| BACS   | United Kingdom | GBP      | Up to 6 business days  |
| BECS   | Australia      | AUD      | Up to 3 business days  |

Supported bank transfer methods include:

• ACH bank transfer\
• SEPA bank transfer\
• BACS bank transfer\
• Multibanco\
• Indonesian bank transfers

Documentation:\
[https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/payment-methods-setup/banks/bank-debits](https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/payment-methods-setup/banks/bank-debits)

</details>

<details>

<summary>How do I run load tests through Hyperswitch? Are test calls billed?</summary>

Hyperswitch provides a CLI testing tool using Newman wrapped in Rust.

#### Install Newman

npm install -g '[https://github.com/knutties/newman.git#feature/newman-dir](https://github.com/knutties/newman.git#feature/newman-dir)'

#### Configure connector authentication

export CONNECTOR\_AUTH\_FILE\_PATH=/path/to/connector\_auth.toml

#### Run tests

cargo run --package test\_utils --bin test\_utils --\
\--connector-name=\<connector\_name>\
\--base-url=[http://127.0.0.1:8080](http://127.0.0.1:8080)\
\--admin-api-key=test\_admin

#### Available options

\--delay\
Add delay between requests.

\--folder\
Run specific test folders.

\--header\
Add custom headers.

\--verbose\
Print detailed logs.

A routing simulation tool is also available for testing routing behavior:

[https://hyperswitch-ten.vercel.app/](https://hyperswitch-ten.vercel.app/)

Documentation:\
[https://docs.hyperswitch.io/learn-more/test-payments-through-newman-wrapped-in-rust](https://docs.hyperswitch.io/learn-more/test-payments-through-newman-wrapped-in-rust)

</details>

## Operational&#x20;

<details>

<summary>How do I rotate API credentials for a connector securely?</summary>

API credentials for connectors can be rotated through the Hyperswitch Control Centre.

#### Steps

1. Navigate to the **Connectors** section in the Hyperswitch Control Centre.
2. Locate the connector integration for the relevant business profile.
3. Click the **edit icon** next to the API credentials.
4. Update the required credential fields. All required credentials must be re-entered during the update process.
5. Save the updated configuration.

#### Security model

Hyperswitch secures connector credentials using multiple layers of encryption.

• Each merchant account has a unique **Data Encryption Key (DEK)** used to encrypt connector API keys.\
• Credentials are encrypted using **AES-256 symmetric encryption** through a master key.\
• Sensitive values are masked during transmission and are not stored on local systems.

#### Access control

Connector credential management permissions are typically available to:

• Merchant Developer\
• Profile Developer

These roles allow secure management of connector configuration and credentials.

Documentation:\
[https://docs.hyperswitch.io/explore-hyperswitch/connectors/activate-connector-on-hyperswitch](https://docs.hyperswitch.io/explore-hyperswitch/connectors/activate-connector-on-hyperswitch)\
[https://docs.hyperswitch.io/explore-hyperswitch/security-and-compliance/security](https://docs.hyperswitch.io/explore-hyperswitch/security-and-compliance/security)\
[https://docs.hyperswitch.io/explore-hyperswitch/account-management/manage-your-team](https://docs.hyperswitch.io/explore-hyperswitch/account-management/manage-your-team)

</details>

<details>

<summary>What is the runbook for handling a connector outage?</summary>

Hyperswitch provides several mechanisms to handle connector outages and maintain payment reliability.

#### Elimination routing

Elimination routing automatically tracks incidents such as gateway downtime or technical errors and deprioritizes connectors experiencing issues.\
This logic is applied after other routing rules have been evaluated.

#### Authorization rate based routing

Hyperswitch uses a **Multi-Armed Bandit (MAB)** model to optimize routing decisions.

This approach:

• Continuously evaluates processor performance\
• Sends a small percentage of traffic to alternative gateways\
• Adapts routing decisions dynamically based on authorization rates

The model uses a **sliding window of recent performance metrics** to respond quickly to changes in gateway behavior.

#### Smart retries

If a transaction fails, the system analyzes error codes to determine whether the payment is retryable.

Retryable categories may include:

• System malfunction\
• Processing temporarily unavailable\
• Transaction not permitted on network\
• Invalid cryptogram\
• Network token not supported

#### Configuration options

Routing behavior can be tuned through configuration parameters such as:

• exploration\_percent\
• routing bucket size\
• aggregation pipeline size

Documentation:\
[https://docs.hyperswitch.io/explore-hyperswitch/workflows/intelligent-routing](https://docs.hyperswitch.io/explore-hyperswitch/workflows/intelligent-routing)\
[https://docs.hyperswitch.io/explore-hyperswitch/workflows/intelligent-routing/auth-rate-based-routing](https://docs.hyperswitch.io/explore-hyperswitch/workflows/intelligent-routing/auth-rate-based-routing)\
[https://docs.hyperswitch.io/explore-hyperswitch/workflows/smart-retries](https://docs.hyperswitch.io/explore-hyperswitch/workflows/smart-retries)

</details>

<details>

<summary>What monitoring alerts should I set up for payment operations?</summary>

Hyperswitch deployments typically rely on a monitoring stack for infrastructure metrics, logs, and distributed tracing.

#### Monitoring components

| Component               | Purpose                      |
| ----------------------- | ---------------------------- |
| Promtail                | Collects application logs    |
| Grafana Loki            | Stores and queries logs      |
| OpenTelemetry Collector | Collects application metrics |
| Prometheus              | Pull-based metrics retrieval |
| Grafana                 | Visualization dashboards     |
| Tempo                   | Distributed tracing          |
| CloudWatch              | AWS infrastructure metrics   |

#### Health check endpoint

Hyperswitch exposes a readiness endpoint to check service health.

curl [http://localhost:8080/health/ready](http://localhost:8080/health/ready)

The endpoint verifies:

• Database connectivity\
• Redis connectivity\
• Vault availability (if configured)\
• Analytics component health\
• Outgoing network connectivity

#### Kubernetes readiness probe example

readinessProbe:\
 httpGet:\
  path: /health/ready\
  port: 8080\
 initialDelaySeconds: 5\
 periodSeconds: 15

#### Key operational metrics to monitor

Recommended metrics include:

• Payment success and failure rates per connector\
• Gateway latency for successful and failed transactions\
• Distribution of processor error codes\
• Webhook delivery success rates

Documentation:\
[https://docs.hyperswitch.io/check-list-for-production/going-live/for-on-prem-setup/monitoring](https://docs.hyperswitch.io/check-list-for-production/going-live/for-on-prem-setup/monitoring)\
[https://docs.hyperswitch.io/hyperswitch-open-source/troubleshooting](https://docs.hyperswitch.io/hyperswitch-open-source/troubleshooting)\
[https://docs.hyperswitch.io/learn-more/hyperswitch-architecture](https://docs.hyperswitch.io/learn-more/hyperswitch-architecture)

</details>

## Reporting & Analytics

<details>

<summary>How do I create custom reports for my business needs?</summary>

Hyperswitch does not currently provide a built-in custom report builder in the Control Centre. However, merchants can export payment data and build custom reports using external analytics or business intelligence tools.

Payment data is exported as **CSV files to Amazon S3**, which can then be ingested into **Amazon Redshift** or other analytics platforms.

#### Exported data fields

Exported datasets may include fields such as:

• payment\_id\
• attempt\_id\
• status\
• amount\
• currency\
• customer\_id\
• created\_at\
• connector\
• payment\_method\
• error\_message\
• metadata

Once the data is available in your data warehouse, you can generate reports using SQL queries or integrate with BI tools such as Tableau, Looker, or Power BI.

Documentation:\
[https://docs.hyperswitch.io/explore-hyperswitch/account-management/analytics-and-operations/exporting-payments-data](https://docs.hyperswitch.io/explore-hyperswitch/account-management/analytics-and-operations/exporting-payments-data)

</details>

<details>

<summary>How do I export payment data to my data warehouse (Snowflake or BigQuery)?</summary>

Hyperswitch supports exporting payment data through **S3-based data pipelines**, which can then be ingested into data warehouses such as Snowflake, BigQuery, or Amazon Redshift.

#### Setup requirements

• An AWS account with Amazon Redshift or another data warehouse\
• An IAM role with permission to read from S3\
• The IAM role ARN shared with the Hyperswitch team for configuration

#### Export workflow

1. Hyperswitch writes payment data files to an S3 bucket.
2. Data is exported in **CSV format with headers**.
3. Files are typically organized by merchant ID and date.

Example S3 path format:

s3://\<bucket>/\<merchant\_id>/\<version>/payments/\<date>.csv

#### Update frequency

• Data is updated approximately every **6 hours**\
• S3 storage maintains **7 days of data retention**

Merchants can configure ingestion pipelines using tools such as:

• Redshift COPY jobs\
• Lambda-based loaders\
• Scheduled ETL jobs

Documentation:\
[https://docs.hyperswitch.io/explore-hyperswitch/account-management/analytics-and-operations/exporting-payments-data](https://docs.hyperswitch.io/explore-hyperswitch/account-management/analytics-and-operations/exporting-payments-data)

</details>

<details>

<summary>What metrics are available for measuring payment performance?</summary>

Hyperswitch provides several metrics to help merchants measure payment performance and optimize their payment infrastructure.

#### Core metrics

| Metric                  | Description                                            |
| ----------------------- | ------------------------------------------------------ |
| Overall Conversion Rate | Successful payments divided by total payments created  |
| Payment Success Rate    | Successful payments divided by user-confirmed payments |
| Processed Amount        | Total amount of payments with status = succeeded       |
| Average Ticket Size     | Total payment amount divided by number of payments     |
| Successful Payments     | Total number of payments completed successfully        |

#### Payment funnel metrics

The analytics dashboard also provides insights into the payment conversion funnel, including:

• Payments created\
• Checkout confirmation rate\
• 3DS verification outcomes\
• Fraud declines\
• Authorized but pending capture payments\
• Successfully completed transactions

These metrics help merchants identify drop-off points and improve checkout performance.

Documentation:\
[https://docs.hyperswitch.io/explore-hyperswitch/account-management/analytics-and-operations](https://docs.hyperswitch.io/explore-hyperswitch/account-management/analytics-and-operations)

</details>

<details>

<summary>How do I set up custom dashboards for different teams?</summary>

Hyperswitch supports role-based access control that allows different teams to access relevant operational and analytics data.

#### Configuring team access

1. Navigate to **Settings → Users** in the Control Centre.
2. Create or assign roles for different team members.
3. Grant permissions based on operational or analytical responsibilities.

#### Example roles

| Role                          | Access level                                |
| ----------------------------- | ------------------------------------------- |
| Organization Admin            | Full platform access                        |
| Merchant or Profile Admin     | Full merchant-level access                  |
| Merchant or Profile Developer | Analytics access and API key management     |
| Merchant or Profile Operator  | Payment operations and analytics visibility |
| Customer Support              | Transaction-level access                    |
| View Only roles               | Read-only access to analytics dashboards    |

Custom roles can also be created to align with internal organizational workflows.

Documentation:\
[https://docs.hyperswitch.io/explore-hyperswitch/account-management/manage-your-team](https://docs.hyperswitch.io/explore-hyperswitch/account-management/manage-your-team)

</details>

<details>

<summary>Is real-time payment analytics available?</summary>

Yes. Hyperswitch provides real-time analytics through the Control Centre.

The analytics dashboard provides visibility into the payment lifecycle and checkout funnel.

#### Real-time insights include

• Payment status updates as transactions progress\
• Checkout analytics showing user behavior\
• Drop-off analysis at different stages of the payment flow\
• 3DS authentication outcomes\
• Fraud detection results

In addition to dashboard analytics, **webhooks provide real-time event notifications** for payment lifecycle events such as:

• payment\_succeeded\
• payment\_failed\
• refund\_succeeded

These events allow merchants to synchronize their internal systems with payment status updates.

Documentation:\
[https://docs.hyperswitch.io/explore-hyperswitch/account-management/analytics-and-operations](https://docs.hyperswitch.io/explore-hyperswitch/account-management/analytics-and-operations)\
[https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/webhooks](https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/webhooks)

</details>

<details>

<summary>What audit logs are available for compliance and debugging?</summary>

Hyperswitch provides multiple mechanisms for maintaining auditability and operational traceability.

#### Reconciliation audit trail

The reconciliation system is built on **double-entry accounting principles**, providing:

• A complete audit trail of financial events\
• Point-in-time balances for finance teams\
• Immutable transaction history\
• Auditable exception handling processes

#### Application logs (self-hosted deployments)

Self-hosted deployments use the following logging stack:

| Component     | Purpose                          |
| ------------- | -------------------------------- |
| Promtail      | Log collection                   |
| Grafana Loki  | Log storage and querying         |
| OpenTelemetry | Metrics and telemetry collection |

These logs allow teams to track system behavior and debug payment processing issues.

#### Webhook events

Hyperswitch also emits event notifications through webhooks, including:

Payment events\
• payment\_succeeded\
• payment\_failed\
• payment\_processing\
• payment\_authorized\
• payment\_captured

Refund events\
• refund\_succeeded\
• refund\_failed

Dispute events\
• dispute\_opened\
• dispute\_won\
• dispute\_lost

Mandate events\
• mandate\_active\
• mandate\_revoked

#### Cost observability audit

The cost observability system helps detect anomalies such as:

• Processor billing discrepancies\
• Invoice mismatches\
• Unexpected fee changes

Documentation:\
[https://docs.hyperswitch.io/explore-hyperswitch/payments-modules/reconciliation-product](https://docs.hyperswitch.io/explore-hyperswitch/payments-modules/reconciliation-product)\
[https://docs.hyperswitch.io/check-list-for-production/going-live/for-on-prem-setup/monitoring](https://docs.hyperswitch.io/check-list-for-production/going-live/for-on-prem-setup/monitoring)\
[https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/webhooks](https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/webhooks)\
[https://docs.hyperswitch.io/explore-hyperswitch/payments-modules/ai-powered-cost-observability](https://docs.hyperswitch.io/explore-hyperswitch/payments-modules/ai-powered-cost-observability)

</details>

## Webhooks

<details>

<summary>How do I verify webhook signatures for security?</summary>

Hyperswitch uses HMAC-based signature verification to ensure webhook authenticity.

When a business profile is created, a secret key is configured in the `payment_response_hash_key` field. If no key is provided, Hyperswitch generates a secure random key automatically.

#### Signature generation process

1. The webhook payload is encoded as a JSON string.
2. A signature is generated using the **HMAC-SHA512** algorithm with the `payment_response_hash_key`.
3. The generated digest is included in the webhook header:

`x-webhook-signature-512`

#### Verification steps

To verify webhook authenticity:

1. Retrieve the webhook payload.
2. Encode the payload as a JSON string.
3. Generate an HMAC-SHA512 signature using your stored `payment_response_hash_key`.
4. Compare the generated signature with the `x-webhook-signature-512` header.

If both values match, the webhook request is authentic and has not been modified.

If your system does not support SHA512, you can use the alternative header:

`x-webhook-signature-256`

This header contains a signature generated using **HMAC-SHA256**.

Documentation:\
[https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/webhooks](https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/webhooks)

</details>

<details>

<summary>What is the retry policy for failed webhook deliveries?</summary>

A webhook delivery is considered successful when the receiving server returns an **HTTP 2XX response**.

If a webhook request does not receive a 2XX response, Hyperswitch automatically retries delivery using increasing intervals for up to **24 hours**.

#### Retry schedule

| Retry attempt      | Interval   |
| ------------------ | ---------- |
| 1st retry          | 1 minute   |
| 2nd and 3rd retry  | 5 minutes  |
| 4th to 8th retry   | 10 minutes |
| 9th to 13th retry  | 1 hour     |
| 14th to 16th retry | 6 hours    |

The first retry interval is measured from the initial delivery attempt. Subsequent retries are measured from the previous retry attempt.

Documentation:\
[https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/webhooks](https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/webhooks)

</details>

<details>

<summary>How do I handle duplicate webhook events?</summary>

Because webhook deliveries may be retried, your system may receive the same webhook event multiple times.

Each webhook payload contains a unique field:

`event_id`

This identifier can be used to detect duplicate events.

#### Recommended handling process

1. Extract the `event_id` from the webhook payload.
2. Store processed `event_id` values in a persistent datastore such as a relational database or Redis.
3. Before processing a webhook, check whether the `event_id` has already been processed.
4. If it exists, ignore the event as a duplicate.
5. If it does not exist, process the event and store the `event_id`.

Since webhooks may retry for up to **24 hours**, it is recommended to retain processed event IDs for at least that duration.

Documentation:\
[https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/webhooks](https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/webhooks)

</details>

<details>

<summary>Are webhooks delivered in order? How should I handle out-of-order events?</summary>

Webhook events are delivered asynchronously and may occasionally arrive out of order due to network latency or retry behavior.

To ensure your system processes the most recent state of an object:

Use the `updated` timestamp field in the webhook payload.

#### Recommended approach

1. Extract the `updated` timestamp from the webhook payload.
2. Compare it with the latest known timestamp for the same payment or object.
3. Only apply updates if the incoming event reflects a more recent state.

This ensures that older events do not overwrite the latest payment state in your system.

Documentation:\
[https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/webhooks](https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/webhooks)

</details>

<details>

<summary>What timeout should my webhook endpoint support?</summary>

Webhook requests should return an HTTP 2XX response after successful processing.

If the endpoint does not respond successfully, Hyperswitch treats the delivery as failed and schedules retries according to the retry policy.

#### Recommended implementation practices

• Ensure webhook endpoints respond quickly to avoid retries.\
• Process heavy business logic asynchronously if needed.\
• Return a success response once the event has been accepted for processing.

If your webhook processing requires longer execution time, consider using message queues or background workers to process events after acknowledging the request.

Documentation:\
[https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/webhooks](https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/webhooks)

</details>

<details>

<summary>What webhook events are available?</summary>

Hyperswitch emits webhook events for multiple payment lifecycle stages.

#### Payment events

• payment\_succeeded\
• payment\_failed\
• payment\_processing\
• payment\_cancelled\
• payment\_authorized\
• payment\_captured

#### Refund events

• refund\_succeeded\
• refund\_failed

#### Dispute events

• dispute\_opened\
• dispute\_expired\
• dispute\_accepted\
• dispute\_cancelled\
• dispute\_challenged\
• dispute\_won\
• dispute\_lost

#### Mandate events

• mandate\_active\
• mandate\_revoked

These events allow merchants to synchronize payment states with internal systems such as order management, accounting, or customer notifications.

Documentation:\
[https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/webhooks](https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/webhooks)

</details>

## Vault & Tokenization

<details>

<summary>How do I migrate existing tokens from another provider to Hyperswitch?</summary>

Hyperswitch provides a structured process for importing existing payment tokens from another provider.

#### Migration process

1. The merchant requests a data import from the Hyperswitch team.
2. Hyperswitch shares its **PCI Attestation of Compliance (AoC)** certificate with the merchant.
3. The merchant requests a secure data export from their existing payment processor using the Hyperswitch AoC.
4. Hyperswitch provides a **public PGP key** for encryption.
5. The existing processor encrypts the token data and transfers it via **SFTP**.
6. Hyperswitch imports the data into its vault.
7. Updated customer and payment method reference IDs are shared with the merchant.

#### Required fields for card import

The following fields are typically required when importing card data.

• card\_number (PAN)\
• card\_expiry\_month\
• card\_expiry\_year\
• payment\_instrument\_id (PSP token used for mapping)\
• original\_network\_transaction\_id (required for connector-agnostic merchant initiated transactions)

#### Optional fields

Additional customer or card details may also be included:

• customer name\
• email address\
• phone number\
• billing address\
• card scheme

After the import is completed, merchants can begin using the migrated tokens through the Hyperswitch APIs.

Documentation:\
[https://docs.hyperswitch.io/explore-hyperswitch/account-management/data-migration/import-data-to-hyperswitch](https://docs.hyperswitch.io/explore-hyperswitch/account-management/data-migration/import-data-to-hyperswitch)

</details>

<details>

<summary>Can tokens be used across multiple connectors or processors?</summary>

Yes. Hyperswitch supports token portability across connectors through its unified token model.

#### Universal payment method token

Hyperswitch provides a **unified `payment_method_id`**, which abstracts connector-specific tokens.

This token can represent:

• vault\_token\
• psp\_token\
• customer\_id

This abstraction allows merchants to route payments through different processors without re-collecting card details.

#### Connector-agnostic merchant initiated transactions

Hyperswitch supports **connector-agnostic merchant initiated transactions (MIT)**.

When a customer performs an initial **customer initiated transaction (CIT)**, Hyperswitch stores the **network transaction ID** returned by the processor.

This network transaction ID can later be used to process recurring or merchant initiated payments through different eligible connectors.

#### Enabling connector-agnostic MIT

Merchants can enable this capability through an API call.

POST /account/:merchant\_id/business\_profile/:profile\_id/toggle\_connector\_agnostic\_mit

Request body

{\
"enabled": true\
}

#### Supported processors

Connector-agnostic recurring payments are currently supported with processors including:

• Stripe\
• Adyen\
• Cybersource

This approach allows merchants to change processors without requiring customers to re-enter payment details.

Documentation:\
[https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/tokenization-and-saved-cards/pg-agnostic-recurring-payments](https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/tokenization-and-saved-cards/pg-agnostic-recurring-payments)\
[https://docs.hyperswitch.io/explore-hyperswitch/workflows/vault/self-hosted-orchestration-with-outsourced-pci-vault](https://docs.hyperswitch.io/explore-hyperswitch/workflows/vault/self-hosted-orchestration-with-outsourced-pci-vault)

</details>
