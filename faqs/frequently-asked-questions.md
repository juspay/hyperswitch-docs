---
description: Find answers to common questions about Juspay Hyperswitch features, integration, and troubleshooting to accelerate your payment implementation
---
# Frequently Asked Questions

## Getting Started

<details>

<summary>What is Juspay Hyperswitch and what does it offer?</summary>

Juspay Hyperswitch is an **open-source payments platform** designed to simplify global payments for digital businesses.

Built by Juspay, HyperSwitch is designed to handle high-scale payment processing infrastructure. Juspay processes **over 300 million daily transactions** with an **annualised total payment value exceeding $1 trillion**.

HyperSwitch provides two main solutions:

**Payments Suite**

An end-to-end orchestration layer that unifies payments across providers, networks, and channels.

Capabilities include:

* Unified checkout experiences
* Dynamic payment routing
* Retry mechanisms for failed transactions
* Redundancy for payment reliability

**Payment Modules**

A modular set of payment capabilities that can be integrated individually depending on business needs.

Available modules include:

* Intelligent routing
* Payment vault
* Reconciliation
* Cost observability
* Smart retries
* Alternative payment method widgets

Documentation:

https://docs.hyperswitch.io/explore-hyperswitch/payments-modules

https://docs.hyperswitch.io/about-hyperswitch/payment-suite

</details>

<details>

<summary>What is payment orchestration?</summary>

Payment orchestration is a platform approach used to manage multiple payment service providers and payment methods through a single system.

It simplifies payment operations by providing a unified layer that coordinates payment processing across different providers.

Payment orchestration supports multiple stages of the payment lifecycle, including:

* Accepting payments from customers
* Managing payouts
* Processing recurring payments

**Key capabilities**

Payment orchestration platforms typically support:

* Integration with multiple payment processors
* Unified payment APIs
* Smart routing across providers
* Smart retries for failed transactions
* 3DS authentication and Strong Customer Authentication
* Fraud and risk management
* Subscription payment management

Documentation:

https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration

</details>

<details>

<summary>How is HyperSwitch different from a PSP (payment service provider)?</summary>

HyperSwitch is **not a payment service provider**. It is a **payment orchestrator** that sits between the merchant and multiple PSPs.

**Key differences**

| Aspect         | PSP                                          | HyperSwitch                                        |
| -------------- | -------------------------------------------- | -------------------------------------------------- |
| Providers      | Single payment processor                     | Multiple processors through one integration        |
| Vendor lock-in | Processor-specific tokens and infrastructure | Merchant-owned tokens through a neutral vault      |
| Routing        | Limited routing capabilities                 | Dynamic routing across processors                  |
| Integration    | Separate integration per PSP                 | Unified API across multiple processors             |
| Operations     | Multiple PSP dashboards                      | Single Control Centre for operations and analytics |

HyperSwitch connects merchants to **multiple processors through a single integration**, allowing businesses to switch or combine providers without rebuilding payment infrastructure.

</details>

<details>

<summary>How is HyperSwitch different from a payment processor?</summary>

HyperSwitch is not a payment processor. It acts as a **payments switch** that routes transactions to multiple payment processors.

**Key differences**

| Aspect      | Payment Processor                                  | HyperSwitch                               |
| ----------- | -------------------------------------------------- | ----------------------------------------- |
| Function    | Executes transactions with card networks and banks | Routes transactions to optimal processors |
| Coverage    | Single processor capabilities                      | Supports multiple processors              |
| Latency     | Direct processing                                  | Adds minimal routing overhead (~25ms)     |
| Failover    | Single processor dependency                        | Automatic retries across processors       |
| Integration | Processor-specific APIs                            | Unified schemas across processors         |

HyperSwitch normalises processor APIs, error codes, and webhook formats into a unified interface.

</details>

<details>

<summary>How is HyperSwitch different from a payment gateway?</summary>

HyperSwitch differs from traditional payment gateways by providing a broader orchestration layer.

**Key differences**

| Aspect         | Payment Gateway                         | HyperSwitch                                   |
| -------------- | --------------------------------------- | --------------------------------------------- |
| Scope          | Single gateway connection to processors | Full payment orchestration platform           |
| Integration    | Individual integrations required        | Connector-based integrations                  |
| Routing        | Basic routing                           | Intelligent routing using multiple parameters |
| Platform model | Proprietary systems                     | Open-source platform                          |
| Architecture   | Monolithic                              | Modular architecture                          |

HyperSwitch allows businesses to integrate only the components they need, such as routing, vault, or reconciliation modules.

</details>

<details>

<summary>What deployment options are available for HyperSwitch?</summary>

HyperSwitch supports two primary deployment models: **SaaS (hosted)** and **self-hosted (open source)**. The deployment model determines how infrastructure, security, compliance, and operational responsibilities are managed.

**SaaS (Hosted Deployment)**

The SaaS deployment model provides a hosted environment managed by Juspay. This option allows businesses to start accepting payments without managing infrastructure, security operations, or platform upgrades.

Characteristics:

* Hosted infrastructure managed by Juspay
* Ready-to-use Control Centre environment
* Faster onboarding and deployment
* Managed upgrades and platform maintenance
* Integrated monitoring and operational tooling

Typical use cases:

* Businesses that want to integrate payments quickly
* Teams that prefer managed infrastructure
* Organisations that do not want to operate PCI compliant infrastructure

**Self-Hosted Deployment**

In the self-hosted model, merchants deploy and operate HyperSwitch on their own infrastructure. This option provides greater control over infrastructure, data residency, and platform customisation.

Deployment methods:

* Docker deployment — run HyperSwitch locally using Docker Compose for development or small deployments
* Kubernetes deployment — production deployments using AWS EKS, Terraform, and Helm charts
* Component level setup — backend, Control Centre, and SDK can be deployed independently

**SaaS vs Self-Hosted comparison**

| Factor                    | SaaS (Hosted)            | Self-Hosted                 |
| ------------------------- | ------------------------ | --------------------------- |
| Infrastructure management | Managed by Juspay        | Managed by merchant         |
| Setup time                | Minutes to hours         | Hours to days               |
| Platform upgrades         | Managed automatically    | Managed by merchant         |
| Data residency            | Hosted in Juspay cloud   | Controlled by merchant      |
| Customisation             | Limited to configuration | Full platform customisation |
| PCI DSS responsibility    | Juspay maintains PCI DSS | Merchant responsible        |
| Operational overhead      | Low                      | High                        |

Documentation:

https://docs.hyperswitch.io/hyperswitch-open-source/overview/unified-local-setup-using-docker

https://docs.hyperswitch.io/deploy-hyperswitch-on-aws/deploy-hyperswitch

</details>

<details>

<summary>How do I set up and configure a sandbox environment for testing?</summary>

Juspay Hyperswitch provides multiple ways to set up a sandbox environment depending on your development workflow.

**Option A: Hyperswitch Cloud Sandbox**

Sandbox URL: https://sandbox.hyperswitch.io

SDK sandbox endpoint: https://beta.hyperswitch.io/v1

Publishable keys for sandbox environments start with `pk_snd_`

**Option B: Local setup using Docker**

```bash
git clone --depth 1 --branch latest https://github.com/juspay/hyperswitch
cd hyperswitch
scripts/setup.sh
```

This launches the HyperSwitch backend, Control Centre, and SDK frontend.

**Option C: Individual component setup**

Run the backend, Control Centre, and SDK components independently.

Typical configuration steps include:

* Configure payment processors through the **Connectors** tab in the Control Centre
* Use dummy processors such as **fauxpay** for testing without real PSP credentials
* Configure routing rules through **Workflow → Routing**

Documentation:

https://docs.hyperswitch.io/hyperswitch-open-source/overview/unified-local-setup-using-docker

https://docs.hyperswitch.io/hyperswitch-open-source/account-setup

</details>

<details>

<summary>What are the differences between sandbox and production environments?</summary>

| Aspect                 | Sandbox                | Production         |
| ---------------------- | ---------------------- | ------------------ |
| API URL                | sandbox.hyperswitch.io | api.hyperswitch.io |
| SDK Endpoint           | beta.hyperswitch.io/v1 | api.hyperswitch.io |
| Publishable key prefix | pk_snd_                | pk_prd_            |
| Connector credentials  | Test credentials       | Live credentials   |
| Transactions           | Test transactions      | Real payments      |

**Going live checklist**

Before switching to production:

* Sign the HyperSwitch services agreement
* Configure production connectors with live credentials
* Enable payment methods on processor dashboards
* Secure API keys and avoid exposing them in frontend applications
* Configure webhook endpoints
* Implement error handling and validation for payment responses

Documentation:

https://docs.hyperswitch.io/check-list-for-production/going-live

</details>

<details>

<summary>How do I integrate Hyperswitch iOS SDK with my Swift or Objective-C app?</summary>

Integrate the Juspay Hyperswitch iOS SDK using CocoaPods. The SDK requires iOS 15.1 or later and supports Swift and SwiftUI implementations.

**Integration steps**

1. Add the Hyperswitch SDK to your Podfile.

```ruby
pod 'hyperswitch-sdk-ios'
```

2. Install dependencies.

```bash
pod install
```

3. Initialize the SDK with your publishable key.

```swift
import Hyperswitch
paymentSession = PaymentSession(publishableKey: <YOUR_PUBLISHABLE_KEY>)
```

4. For open source deployments, configure custom backend endpoints.

```swift
paymentSession = PaymentSession(
  publishableKey: <YOUR_PUBLISHABLE_KEY>,
  customBackendUrl: <YOUR_SERVER_URL>,
  customLogUrl: <YOUR_LOG_URL>
)
```

5. Create the payment session on your backend to generate the client secret.
6. Initialize the payment session with the client secret and present the payment sheet.

Documentation:

https://docs.hyperswitch.io/explore-hyperswitch/payment-experience/payment/mobile/ios/swift-with-rest-api-integration

</details>

<details>

<summary>How do I integrate Hyperswitch Android SDK with my Kotlin or Java app?</summary>

Integrate the Juspay Hyperswitch Android SDK using Gradle. The SDK requires Android 7.0 (API level 24) or later, Android Gradle Plugin 8.13 or later, and AndroidX.

**Integration steps**

1. Add the classpath to your project-level build.gradle.

```groovy
buildscript {
  dependencies {
    classpath "io.hyperswitch:hyperswitch-gradle-plugin:$latest_version"
  }
}
```

2. Add the plugin to your app-level build.gradle.

```groovy
plugins {
  id 'io.hyperswitch.plugin'
}
```

3. Configure SDK options.

```groovy
hyperswitch {
  sdkVersion = "1.1.5"
  features = [HyperFeature.SCANCARD, HyperFeature.NETCETERA]
}
```

4. Implement HyperInterface in your Activity and initialize PaymentSession.

```kotlin
val paymentSession = PaymentSession(applicationContext, "YOUR_PUBLISHABLE_KEY")
```

5. Present the payment sheet and handle results.

Documentation:

https://docs.hyperswitch.io/explore-hyperswitch/payment-experience/payment/mobile/android/kotlin-with-rest-api-integration

</details>

<details>

<summary>How do I migrate from Stripe iOS or Android SDK to HyperSwitch?</summary>

HyperSwitch provides a migration path from Stripe SDK integrations.

**iOS migration**

Install dependencies.

```bash
npm install @juspay-tech/react-native-hyperswitch @juspay-tech/hyper-node
```

Update server-side import.

From:

```javascript
const stripe = require("stripe")("your_stripe_api_key");
```

To:

```javascript
const stripe = require("@juspay-tech/hyper-node")("your_hyperswitch_api_key");
```

Update Podfile sources.

```ruby
source 'https://github.com/juspay/hyperswitch-pods.git'
source 'https://cdn.cocoapods.org/'
```

Replace Stripe dependency from `pod 'StripePaymentSheet'` to `pod 'hyperswitch', '1.0.0-alpha01'`

Update imports from StripePaymentSheet to hyperswitch.

**Android migration**

Install dependency.

```bash
npm install @juspay-tech/hyperswitch-node
```

Replace dependency from `implementation 'com.stripe:stripe-android:20.27.3'` to `implementation 'io.hyperswitch:hyperswitch-android:1.0.1'`

Update imports from `com.stripe.android.*` to `io.hyperswitch.*`.

Documentation:

https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/migrate-from-stripe/ios

https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/migrate-from-stripe/android

</details>

<details>

<summary>What test card numbers are available for different scenarios (success, decline, 3DS)?</summary>

HyperSwitch provides dummy connector test cards for common payment scenarios.

**Successful payments**

* Visa — 4111111111111111 / 4242424242424242
* Mastercard — 5555555555554444
* Diners Club — 38000000000006
* American Express — 378282246310005
* Discover — 6011111111111117

**Decline scenarios**

* Card declined — 4000000000000002
* Insufficient funds — 4000000000009995
* Lost card — 4000000000009987
* Stolen card — 4000000000009979

**3DS flows**

* 3DS success — 4000003800000446

For dummy connector cards, expiry date can be any future date and CVV can be any valid value.

Documentation:

https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/payment-methods-setup/test-credentials

</details>

## Product FAQs

### SDK

<details>

<summary>What mobile-specific payment flows are supported?</summary>

HyperSwitch supports multiple wallet payment methods on mobile.

**Apple Pay**

* Available in 75+ countries
* Supported on iOS (in-app) and Web (Safari)
* Requires Apple Developer Account, Merchant ID, and domain verification
* Supports both Hyperswitch decryption and PSP decryption flows

**Google Pay**

* Available in 70+ countries on Web and Android
* iOS support limited to US and India
* Supports in-app and web transactions
* Requires Google Pay test cards for sandbox testing
* Production deployment requires Google approval

**Other wallets**

* PayPal
* Samsung Pay

The Android SDK also provides widgets for Google Pay, PayPal, and Express Checkout.

Documentation:

https://docs.hyperswitch.io/explore-hyperswitch/wallets/apple-pay

https://docs.hyperswitch.io/explore-hyperswitch/wallets/google-pay

</details>

<details>

<summary>How do I handle deep linking for mobile redirects such as 3DS or wallets?</summary>

HyperSwitch supports native 3DS authentication designed to minimize redirections.

**Native 3DS authentication**

* In-line 3DS challenge flows
* Frictionless authentication using risk-based evaluation
* Native OTP experience instead of web views

External 3DS providers such as Netcetera and 3DSecure.io can be integrated.

**Redirect flow handling**

The SDK automatically handles redirects for:

* 3DS card payments
* Bank redirects such as iDEAL, Giropay, eps
* Wallet flows such as PayPal and Klarna
* Bank transfer flows

Documentation:

https://docs.hyperswitch.io/explore-hyperswitch/workflows/3ds-decision-manager/native-3ds-authentication-for-mobile-payments

</details>

<details>

<summary>Can I customize the payment sheet appearance on mobile?</summary>

Yes. HyperSwitch provides customization options for payment sheet UI on both iOS and Android.

**Fonts**

* `typography.fontResId` on Android
* `configuration.appearance.font.base` on iOS

**Colors**

* `appBarIcon` — icons in payment page
* `component` — background of inputs
* `componentBorder` — border color for components
* `error` — error message colors
* `primary` — primary theme color
* `surface` — payment page background
* `placeholderText` — input placeholder text

**Shapes**

* `cornerRadiusDp` — corner radius for input fields
* `borderStrokeWidthDp` — border width for components

Example Android configuration:

```kotlin
val appearance = PaymentSheet.Appearance(
  typography = PaymentSheet.Typography(10.0f, R.font.MY_FONT)
)
```

Documentation:

https://docs.hyperswitch.io/explore-hyperswitch/payment-experience/payment/mobile/android/customization

https://docs.hyperswitch.io/explore-hyperswitch/payment-experience/payment/mobile/ios/customization

</details>

<details>

<summary>What is the SDK size and performance impact on mobile apps?</summary>

HyperSwitch provides two SDK variants.

**Lite SDK**

* Artifact size under 300 KB
* Web-based UI components
* Minimal dependencies
* Faster initialization
* Full payment processing capabilities

**Full SDK**

* Larger artifact size
* Native UI components
* Additional features including card scanning and Netcetera 3DS

**Platform requirements**

* Android — 7.0 (API 24)
* Android Lite — 6.0 (API 23)
* iOS — 15.1

Documentation:

https://docs.hyperswitch.io/explore-hyperswitch/payment-experience/payment/mobile/android/lite-sdk

https://docs.hyperswitch.io/explore-hyperswitch/payment-experience/payment/mobile/ios/lite-sdk

</details>

<details>

<summary>Does the SDK support multiple payment methods and region-specific flows?</summary>

Yes. The Hyperswitch SDK supports multiple payment methods and adapts to regional payment requirements.

**Supported payment method categories**

* Cards — Visa, Mastercard, Amex, Discover, Diners, and others
* Wallets — Apple Pay, Google Pay, PayPal, Samsung Pay
* Bank redirects — iDEAL, Giropay, EPS, and others
* Bank transfers — ACH, SEPA, BACS, BECS, Multibanco
* Buy Now Pay Later — Klarna, Afterpay, and others

**Region-specific flows**

* 3DS authentication for card payments, including native 3DS for mobile
* PSD2 Strong Customer Authentication for European transactions
* Local wallet flows such as Apple Pay (75+ countries) and Google Pay (70+ countries)

Payment methods displayed in the checkout are determined by the connector and payment method configuration set in the relevant business profile, allowing different payment method sets to be presented for different regions or storefronts.

The complete list of supported payment methods and connectors is available at:

https://juspay.io/integrations

Documentation:

https://docs.hyperswitch.io/explore-hyperswitch/payment-experience

https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/payment-methods-setup

</details>

<details>

<summary>How are webhooks, callbacks, and asynchronous payment states handled?</summary>

HyperSwitch uses webhooks to notify your server of payment lifecycle events in real time.

**Webhook events**

HyperSwitch emits events for all key payment state transitions including `payment_succeeded`, `payment_failed`, `payment_processing`, `refund_succeeded`, `refund_failed`, `dispute_opened`, and `mandate_active` among others.

**Asynchronous payment states**

When a payment is submitted to a connector and the outcome is not immediately known:

1. HyperSwitch sets the payment status to `processing`.
2. When the connector sends a webhook with the final outcome, HyperSwitch updates the payment record.
3. The updated status is available via the Payments Retrieve API and delivered to your webhook endpoint.

**Signature verification**

All webhook requests include an HMAC signature in the `x-webhook-signature-512` header. Verify this signature using your `payment_response_hash_key` before processing events.

**Idempotent processing**

Each webhook payload includes a unique `event_id`. Store processed event IDs to safely handle duplicate deliveries caused by retries.

Documentation:

https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/webhooks

</details>

### Core Payments / Orchestration

<details>

<summary>How does HyperSwitch prevent duplicate charges during retries?</summary>

HyperSwitch supports idempotency keys to ensure that duplicate API requests do not result in duplicate transactions.

When you include an idempotency key in a request, HyperSwitch checks whether a request with the same key has already been processed. If a matching request exists, the original response is returned without creating a new transaction.

Include the idempotency key in the request header:

```
Idempotency-Key: <your-unique-key>
```

The key should be a unique string generated by your system, such as a UUID.

Documentation:

https://api-reference.hyperswitch.io/essentials/idempotency

</details>

<details>

<summary>Can I customise orchestration logic based on business rules?</summary>

Yes. HyperSwitch supports rule-based routing that allows merchants to define orchestration logic based on payment method, payment method type, transaction amount, currency, customer country, card network, and business profile.

Traffic can also be split across multiple connectors using percentage-based volume distribution.

3DS orchestration logic can be customised through the 3DS Decision Manager with rules based on issuer country, card network, transaction amount, and device type.

All routing rules can be configured and updated through the Control Centre without requiring code changes or redeployment.

Documentation:

https://docs.hyperswitch.io/explore-hyperswitch/workflows/intelligent-routing/rule-based-routing

https://docs.hyperswitch.io/explore-hyperswitch/workflows/3ds-decision-manager/3ds-intelligence-engine

</details>

### Connectors

<details>

<summary>What payment methods are available in different regions?</summary>

The complete list of supported payment methods and processor integrations can be viewed at:

https://juspay.io/integrations

</details>

<details>

<summary>How do I enable a new payment method for my account?</summary>

1. Navigate to the **Connectors** section in the Hyperswitch Control Centre: `app.hyperswitch.io/connectors`
2. Select the desired connector and click **+ Connect**.
3. Enter the authentication credentials from your payment processor dashboard.
4. Select the payment methods you want to enable from the payment methods configuration screen.
5. If the connector supports webhooks, copy the webhook URL from the Control Centre and configure it in the connector dashboard.
6. Enable the connector to start processing payments.

Documentation:

https://docs.hyperswitch.io/explore-hyperswitch/connectors

https://docs.hyperswitch.io/explore-hyperswitch/connectors/activate-connector-on-hyperswitch

</details>

<details>

<summary>Can I route specific payment methods through specific connectors?</summary>

Yes. Using Intelligent Routing, routing rules can be configured based on payment method, payment method type, transaction amount, currency, and customer country.

Traffic can be distributed across processors using percentage-based volume routing. If no routing rule applies, HyperSwitch uses the configured priority order of processors.

Documentation:

https://docs.hyperswitch.io/explore-hyperswitch/workflows/intelligent-routing

https://docs.hyperswitch.io/explore-hyperswitch/workflows/intelligent-routing/rule-based-routing

</details>

<details>

<summary>How do I integrate Apple Pay, Google Pay, and other wallets?</summary>

* Apple Pay — https://docs.hyperswitch.io/explore-hyperswitch/wallets/apple-pay
* Google Pay — https://docs.hyperswitch.io/explore-hyperswitch/wallets/google-pay
* PayPal — https://docs.hyperswitch.io/explore-hyperswitch/wallets/paypal

</details>

<details>

<summary>How does HyperSwitch normalize different PSP APIs into a single interface?</summary>

When a payment request is received, HyperSwitch accepts the request in its unified API format, translates it into the connector-specific format, submits it to the processor, translates the response back into the HyperSwitch unified format, and returns the normalised response to the merchant.

What is normalised across all connectors:

* Payment request and response schemas
* Error codes and decline reasons mapped to unified enums
* Webhook event formats
* Payment status values

Documentation:

https://docs.hyperswitch.io/explore-hyperswitch/connectors

https://api-reference.hyperswitch.io/essentials/error_codes

</details>

<details>

<summary>What happens if a connector is temporarily unavailable?</summary>

**Elimination routing**

Automatically tracks gateway downtime and technical errors, deprioritising affected connectors. Applied after other routing rules have been evaluated.

**Authorization rate based routing**

The Multi-Armed Bandit (MAB) model continuously evaluates processor performance, sends a small percentage of traffic to alternative gateways, and adapts routing dynamically using a sliding window of recent performance metrics.

**Smart retries**

Retryable error categories include system malfunction, processing temporarily unavailable, transaction not permitted on network, invalid cryptogram, and network token not supported.

Documentation:

https://docs.hyperswitch.io/explore-hyperswitch/workflows/intelligent-routing

https://docs.hyperswitch.io/explore-hyperswitch/workflows/smart-retries

</details>

<details>

<summary>How do I rotate API credentials for a connector securely?</summary>

1. Navigate to the **Connectors** section in the Control Centre.
2. Locate the connector integration for the relevant business profile.
3. Click the **edit icon** next to the API credentials.
4. Update the required credential fields — all required credentials must be re-entered.
5. Save the updated configuration.

**Security model**

* Each merchant account has a unique **Data Encryption Key (DEK)** used to encrypt connector API keys.
* Credentials are encrypted using **AES-256 symmetric encryption** through a master key.
* Sensitive values are masked during transmission and are not stored on local systems.

Connector credential management permissions are available to Merchant Developer and Profile Developer roles.

Documentation:

https://docs.hyperswitch.io/explore-hyperswitch/connectors/activate-connector-on-hyperswitch

https://docs.hyperswitch.io/explore-hyperswitch/security-and-compliance/security

</details>

### Control Centre

<details>

<summary>What monitoring alerts should I set up for payment operations?</summary>

**Monitoring components**

| Component               | Purpose                      |
| ----------------------- | ---------------------------- |
| Promtail                | Collects application logs    |
| Grafana Loki            | Stores and queries logs      |
| OpenTelemetry Collector | Collects application metrics |
| Prometheus              | Pull-based metrics retrieval |
| Grafana                 | Visualization dashboards     |
| Tempo                   | Distributed tracing          |
| CloudWatch              | AWS infrastructure metrics   |

**Health check endpoint**

```
https://live.hyperswitch.io/api/health
```

Verifies database connectivity, Redis connectivity, vault availability, analytics component health, and outgoing network connectivity.

**Kubernetes readiness probe**

```yaml
readinessProbe:
  httpGet:
    path: /health/ready
    port: 8080
  initialDelaySeconds: 5
  periodSeconds: 15
```

**Key metrics to monitor**

* Payment success and failure rates per connector
* Gateway latency for successful and failed transactions
* Distribution of processor error codes
* Webhook delivery success rates

Documentation:

https://docs.hyperswitch.io/check-list-for-production/going-live/for-on-prem-setup/monitoring

https://docs.hyperswitch.io/learn-more/hyperswitch-architecture

</details>

<details>

<summary>What is the runbook for handling a connector outage?</summary>

**Elimination routing**

Automatically tracks incidents such as gateway downtime or technical errors and deprioritises connectors experiencing issues, applied after other routing rules.

**Authorization rate based routing**

The Multi-Armed Bandit (MAB) model continuously evaluates processor performance, sends a small percentage of traffic to alternative gateways, and adapts routing decisions dynamically. The model uses a **sliding window of recent performance metrics** to respond quickly to changes in gateway behavior.

**Smart retries**

Retryable categories include system malfunction, processing temporarily unavailable, transaction not permitted on network, invalid cryptogram, and network token not supported.

**Configuration options**

* `exploration_percent`
* Routing bucket size
* Aggregation pipeline size

Documentation:

https://docs.hyperswitch.io/explore-hyperswitch/workflows/intelligent-routing

https://docs.hyperswitch.io/explore-hyperswitch/workflows/intelligent-routing/auth-rate-based-routing

https://docs.hyperswitch.io/explore-hyperswitch/workflows/smart-retries

</details>

<details>

<summary>How is reconciliation handled across multiple PSPs?</summary>

The HyperSwitch reconciliation module is built on **double-entry accounting principles**, providing a complete audit trail of financial events, point-in-time balances for finance teams, immutable transaction history, and auditable exception handling processes.

The reconciliation system also surfaces billing anomalies such as processor billing discrepancies, invoice mismatches, and unexpected fee changes.

Documentation:

https://docs.hyperswitch.io/explore-hyperswitch/payments-modules/reconciliation-product

</details>

<details>

<summary>Can I manage routing rules and configurations without redeploying code?</summary>

Yes. The following configurations can be updated in real time through the Control Centre without any code changes or redeployment:

* Routing rules — rule-based, volume-based, and fallback routing
* Connector priority order
* Active connectors and payment methods per profile
* 3DS exemption rules
* Webhook endpoints
* API key management

Navigate to **Workflow → Routing** to update routing rules. Changes are applied immediately to live traffic.

Routing rules can also be updated programmatically via the HyperSwitch API.

Documentation:

https://docs.hyperswitch.io/explore-hyperswitch/workflows/intelligent-routing

https://docs.hyperswitch.io/explore-hyperswitch/workflows/intelligent-routing/rule-based-routing

</details>

<details>

<summary>How are disputes, refunds, and settlement data tracked?</summary>

**Refunds**

Track via the Refunds Retrieve API, webhook events (`refund_succeeded`, `refund_failed`), and the Payment Operations dashboard in the Control Centre.

**Disputes**

Webhook events are emitted for all dispute lifecycle stages: `dispute_opened`, `dispute_challenged`, `dispute_won`, `dispute_lost`, `dispute_expired`, `dispute_accepted`, `dispute_cancelled`.

**Settlement data**

Payment and settlement data is exported to Amazon S3 in CSV format for ingestion into data warehouses or accounting systems.

Documentation:

https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/webhooks

https://docs.hyperswitch.io/explore-hyperswitch/payments-modules/reconciliation-product

https://docs.hyperswitch.io/explore-hyperswitch/account-management/analytics-and-operations/exporting-payments-data

</details>

<details>

<summary>How do I create custom reports for my business needs?</summary>

HyperSwitch does not currently provide a built-in custom report builder. Payment data is exported as **CSV files to Amazon S3**, which can then be ingested into Amazon Redshift or other analytics platforms.

Exported fields include `payment_id`, `attempt_id`, `status`, `amount`, `currency`, `customer_id`, `created_at`, `connector`, `payment_method`, `error_message`, and `metadata`.

Once available in your data warehouse, generate reports using SQL queries or integrate with BI tools such as Tableau, Looker, or Power BI.

Documentation:

https://docs.hyperswitch.io/explore-hyperswitch/account-management/analytics-and-operations/exporting-payments-data

</details>

<details>

<summary>How do I export payment data to my data warehouse (Snowflake or BigQuery)?</summary>

HyperSwitch exports payment data through **S3-based data pipelines** for ingestion into Snowflake, BigQuery, or Amazon Redshift.

Data is exported in **CSV format with headers**, organised by merchant ID and date, updated approximately every **6 hours**, and retained for **7 days**.

```
s3://<bucket>/<merchant_id>/<version>/payments/<date>.csv
```

Merchants can configure ingestion pipelines using Redshift COPY jobs, Lambda-based loaders, or scheduled ETL jobs.

Documentation:

https://docs.hyperswitch.io/explore-hyperswitch/account-management/analytics-and-operations/exporting-payments-data

</details>

<details>

<summary>What metrics are available for measuring payment performance?</summary>

| Metric                  | Description                                            |
| ----------------------- | ------------------------------------------------------ |
| Overall Conversion Rate | Successful payments divided by total payments created  |
| Payment Success Rate    | Successful payments divided by user-confirmed payments |
| Processed Amount        | Total amount of payments with status = succeeded       |
| Average Ticket Size     | Total payment amount divided by number of payments     |
| Successful Payments     | Total number of payments completed successfully        |

The analytics dashboard also provides payment funnel metrics including payments created, checkout confirmation rate, 3DS verification outcomes, fraud declines, authorised but pending capture payments, and successfully completed transactions.

Documentation:

https://docs.hyperswitch.io/explore-hyperswitch/account-management/analytics-and-operations

</details>

<details>

<summary>How do I set up custom dashboards for different teams?</summary>

Navigate to **Settings → Users** in the Control Centre to create or assign roles for different team members.

| Role                          | Access level                                |
| ----------------------------- | ------------------------------------------- |
| Organization Admin            | Full platform access                        |
| Merchant or Profile Admin     | Full merchant-level access                  |
| Merchant or Profile Developer | Analytics access and API key management     |
| Merchant or Profile Operator  | Payment operations and analytics visibility |
| Customer Support              | Transaction-level access                    |
| View Only roles               | Read-only access to analytics dashboards    |

Documentation:

https://docs.hyperswitch.io/explore-hyperswitch/account-management/manage-your-team

</details>

<details>

<summary>Is real-time payment analytics available?</summary>

Yes. HyperSwitch provides real-time analytics through the Control Centre, including payment status updates, checkout analytics, drop-off analysis, 3DS outcomes, and fraud detection results.

Webhooks also provide real-time event notifications for `payment_succeeded`, `payment_failed`, and `refund_succeeded` among other events.

Documentation:

https://docs.hyperswitch.io/explore-hyperswitch/account-management/analytics-and-operations

https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/webhooks

</details>

<details>

<summary>What audit logs are available for compliance and debugging?</summary>

**Reconciliation audit trail**

Built on double-entry accounting principles — complete audit trail of financial events, point-in-time balances, immutable transaction history, and auditable exception handling.

**Application logs (self-hosted deployments)**

| Component     | Purpose                          |
| ------------- | -------------------------------- |
| Promtail      | Log collection                   |
| Grafana Loki  | Log storage and querying         |
| OpenTelemetry | Metrics and telemetry collection |

**Cost observability audit**

Surfaces processor billing discrepancies, invoice mismatches, and unexpected fee changes.

Documentation:

https://docs.hyperswitch.io/explore-hyperswitch/payments-modules/reconciliation-product

https://docs.hyperswitch.io/check-list-for-production/going-live/for-on-prem-setup/monitoring

https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/webhooks

https://docs.hyperswitch.io/explore-hyperswitch/payments-modules/ai-powered-cost-observability

</details>

### Retries & Routing

<details>

<summary>How does intelligent routing work in HyperSwitch?</summary>

HyperSwitch supports the following routing types, all configurable through the Control Centre without code deployment:

* **Rule-based routing** — conditions based on payment method, amount, currency, card network, and customer country
* **Volume-based routing** — percentage-based traffic distribution across multiple connectors
* **Elimination routing** — connectors with elevated failure rates are deprioritised dynamically
* **Default fallback routing** — the configured connector priority order is used if no rule applies
* **Authorization rate based routing** — a Multi-Armed Bandit (MAB) model continuously evaluates and adjusts routing based on real-time authorisation performance

Documentation:

https://docs.hyperswitch.io/explore-hyperswitch/workflows/intelligent-routing

https://docs.hyperswitch.io/explore-hyperswitch/workflows/intelligent-routing/auth-rate-based-routing

</details>

<details>

<summary>How are retry strategies configured to avoid revenue leakage?</summary>

HyperSwitch classifies decline codes into retryable and non-retryable categories. Non-retryable declines are not retried, avoiding unnecessary processing fees.

**Retry types**

* **Cascading retry** — retry through an alternative processor
* **Step-up retry** — retry with 3DS authentication added for suspected fraud declines
* **Network retry** — retry through alternative debit networks where available

The `manual_retry_allowed` flag permits customers to retry payments manually, for example by updating card details or selecting a different payment method.

Documentation:

https://docs.hyperswitch.io/explore-hyperswitch/workflows/smart-retries

https://docs.hyperswitch.io/explore-hyperswitch/workflows/smart-retries/processor-error-code-mapping

</details>

<details>

<summary>What do different decline codes mean?</summary>

| Decline Code                       | Meaning                                                                    |
| ---------------------------------- | -------------------------------------------------------------------------- |
| `insufficient_funds`               | Customer account does not have enough funds                                |
| `do_not_honor` / `card_declined`   | Generic decline — card cannot be used for the purchase                     |
| `fraudulent`                       | Transaction declined due to suspected fraud                                |
| `call_issuer`                      | Issuer declined for unspecified reason; customer should contact their bank |
| `card_not_supported`               | Card does not support the requested transaction type                       |
| `invalid_cvc`                      | Card security code is invalid                                              |
| `incorrect_number`                 | Card number is invalid                                                     |
| `invalid_expiry_month/year`        | Card expiration date is invalid                                            |
| `account_closed`                   | Bank account linked to the payment method has been closed                  |
| `pickup_card`                      | Card cannot be used — reported lost or stolen                              |
| `pin_try_exceeded`                 | Maximum number of PIN attempts exceeded                                    |
| `card_decline_rate_limit_exceeded` | Card declined too many times — cannot be retried for 24 hours              |

Documentation:

https://docs.hyperswitch.io/explore-hyperswitch/workflows/smart-retries/processor-error-code-mapping

</details>

<details>

<summary>How do I handle bank-level declines that I cannot control?</summary>

Bank-level declines originate from the card issuer and are outside the merchant's direct control. Examples include `insufficient_funds`, `call_issuer`, `account_closed`, and `pickup_card`.

**Smart retry mechanisms**

* **Cascading retry** — attempts the payment through an alternative processor
* **Step-up retry** — retries with 3DS authentication when fraud is suspected
* **Network retry** — attempts through different debit networks when available

The `manual_retry_allowed` setting allows customers to update card details or use a different payment method.

Documentation:

https://docs.hyperswitch.io/explore-hyperswitch/workflows/smart-retries

https://docs.hyperswitch.io/explore-hyperswitch/workflows/smart-retries/manual-user-triggered-retries

</details>

<details>

<summary>How do I differentiate fraud declines from other decline types?</summary>

Inspect the `error_code` field in the payment response.

**Fraud-related decline codes**

| Error Code           | Description                                       |
| -------------------- | ------------------------------------------------- |
| `fraudulent`         | Processor declined due to suspected fraud         |
| `merchant_blacklist` | Transaction blocked by a merchant-level blocklist |
| `risk_decline`       | Transaction declined by a risk or fraud engine    |

Fraud declines should generally not be retried automatically, as repeated attempts may trigger additional fraud flags.

Documentation:

https://docs.hyperswitch.io/explore-hyperswitch/workflows/smart-retries/processor-error-code-mapping

</details>