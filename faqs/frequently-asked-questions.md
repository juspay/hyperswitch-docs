---
description: Get answers to common questions about Juspay Hyperswitch capabilities integration options and payment orchestration features
---

# Frequently Asked Questions

## Getting Started

<details>

<summary>What is Juspay Hyperswitch and what does it offer?</summary>

Juspay Hyperswitch is an **open-source payments platform** designed to simplify global payments for digital businesses.

Built by Juspay, Hyperswitch is designed to handle high-scale payment processing infrastructure. Juspay processes **over 300 million daily transactions** with an **annualized total payment value exceeding $1 trillion**.

Hyperswitch provides two main solutions.

**Payments Suite**

An end-to-end orchestration layer that unifies payments across providers, networks, and channels.

Capabilities include:

- Unified checkout experiences
- Dynamic payment routing
- Retry mechanisms for failed transactions
- Redundancy for payment reliability

**Payment Modules**

A modular set of payment capabilities that can be integrated individually depending on business needs.

Available modules include:

- Intelligent routing
- Payment vault
- Reconciliation
- Cost observability
- Smart retries
- Alternative payment method widgets

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/payments-modules\
https://docs.hyperswitch.io/about-hyperswitch/payment-suite

</details>

<details>

<summary>What is payment orchestration?</summary>

Payment orchestration is a platform approach used to manage multiple payment service providers and payment methods through a single system.

It simplifies payment operations by providing a unified layer that coordinates payment processing across different providers.

Payment orchestration supports multiple stages of the payment lifecycle, including:

- Accepting payments from customers
- Managing payouts
- Processing recurring payments

**Key capabilities**

Payment orchestration platforms typically support:

- Integration with multiple payment processors
- Unified payment APIs
- Smart routing across providers
- Smart retries for failed transactions
- 3DS authentication and Strong Customer Authentication
- Fraud and risk management
- Subscription payment management

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration

</details>

<details>

<summary>How is Hyperswitch different from a PSP (payment service provider)?</summary>

Hyperswitch is **not a payment service provider**. It is a **payment orchestrator** that sits between the merchant and multiple PSPs.

**Key differences**

| Aspect         | PSP                                          | Hyperswitch                                        |
| -------------- | -------------------------------------------- | -------------------------------------------------- |
| Providers      | Single payment processor                     | Multiple processors through one integration        |
| Vendor lock-in | Processor-specific tokens and infrastructure | Merchant-owned tokens through a neutral vault      |
| Routing        | Limited routing capabilities                 | Dynamic routing across processors                  |
| Integration    | Separate integration per PSP                 | Unified API across multiple processors             |
| Operations     | Multiple PSP dashboards                      | Single Control Centre for operations and analytics |

Hyperswitch connects merchants to **multiple processors through a single integration**, allowing businesses to switch or combine providers without rebuilding payment infrastructure.

</details>

<details>

<summary>How is Hyperswitch different from a payment processor?</summary>

Hyperswitch is not a payment processor. It acts as a **payments switch** that routes transactions to multiple payment processors.

**Key differences**

| Aspect      | Payment Processor                                  | Hyperswitch                               |
| ----------- | -------------------------------------------------- | ----------------------------------------- |
| Function    | Executes transactions with card networks and banks | Routes transactions to optimal processors |
| Coverage    | Single processor capabilities                      | Supports multiple processors              |
| Latency     | Direct processing                                  | Adds minimal routing overhead (~25ms)    |
| Failover    | Single processor dependency                        | Automatic retries across processors       |
| Integration | Processor-specific APIs                            | Unified schemas across processors         |

Hyperswitch normalises processor APIs, error codes, and webhook formats into a unified interface.

</details>

<details>

<summary>How is Hyperswitch different from a payment gateway?</summary>

Hyperswitch differs from traditional payment gateways by providing a broader orchestration layer.

**Key differences**

| Aspect         | Payment Gateway                         | Hyperswitch                                   |
| -------------- | --------------------------------------- | --------------------------------------------- |
| Scope          | Single gateway connection to processors | Full payment orchestration platform           |
| Integration    | Individual integrations required        | Connector-based integrations                  |
| Routing        | Basic routing                           | Intelligent routing using multiple parameters |
| Platform model | Proprietary systems                     | Open-source platform                          |
| Architecture   | Monolithic                              | Modular architecture                          |

Hyperswitch allows businesses to integrate only the components they need, such as routing, vault, or reconciliation modules.

</details>

<details>

<summary>What deployment options are available for Hyperswitch?</summary>

Hyperswitch supports two primary deployment models: **SaaS (hosted)** and **self-hosted (open source)**. The deployment model determines how infrastructure, security, compliance, and operational responsibilities are managed.

**SaaS (Hosted Deployment)**

The SaaS deployment model provides a hosted environment managed by Juspay. This option allows businesses to start accepting payments without managing infrastructure, security operations, or platform upgrades.

Characteristics:

- Hosted infrastructure managed by Juspay
- Ready-to-use Control Centre environment
- Faster onboarding and deployment
- Managed upgrades and platform maintenance
- Integrated monitoring and operational tooling

Typical use cases:

- Businesses that want to integrate payments quickly
- Teams that prefer managed infrastructure
- Organisations that do not want to operate PCI compliant infrastructure

**Self-Hosted Deployment**

In the self-hosted model, merchants deploy and operate Hyperswitch on their own infrastructure. This option provides greater control over infrastructure, data residency, and platform customisation.

Deployment methods:

- Docker deployment — run Hyperswitch locally using Docker Compose for development or small deployments
- Kubernetes deployment — production deployments using AWS EKS, Terraform, and Helm charts
- Component level setup — backend, Control Centre, and SDK can be deployed independently

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

Documentation:\
https://docs.hyperswitch.io/hyperswitch-open-source/overview/unified-local-setup-using-docker\
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

```
git clone --depth 1 --branch latest https://github.com/juspay/hyperswitch
cd hyperswitch
scripts/setup.sh
```

This launches the Hyperswitch backend, Control Centre, and SDK frontend.

**Option C: Individual component setup**

Run the backend, Control Centre, and SDK components independently.

Typical configuration steps include:

- Configure payment processors through the **Connectors** tab in the Control Centre
- Use dummy processors such as **fauxpay** for testing without real PSP credentials
- Configure routing rules through **Workflow → Routing**

Documentation:\
https://docs.hyperswitch.io/hyperswitch-open-source/overview/unified-local-setup-using-docker\
https://docs.hyperswitch.io/hyperswitch-open-source/account-setup

</details>

<details>

<summary>What are the differences between sandbox and production environments?</summary>

| Aspect                 | Sandbox                | Production         |
| ---------------------- | ---------------------- | ------------------ |
| API URL                | sandbox.hyperswitch.io | api.hyperswitch.io |
| SDK Endpoint           | beta.hyperswitch.io/v1 | api.hyperswitch.io |
| Publishable key prefix | pk_snd_              | pk_prd_          |
| Connector credentials  | Test credentials       | Live credentials   |
| Transactions           | Test transactions      | Real payments      |

**Going live checklist**

Before switching to production:

- Sign the Hyperswitch services agreement
- Configure production connectors with live credentials
- Enable payment methods on processor dashboards
- Secure API keys and avoid exposing them in frontend applications
- Configure webhook endpoints
- Implement error handling and validation for payment responses

Documentation:\
https://docs.hyperswitch.io/check-list-for-production/going-live

</details>

<details>

<summary>How do I integrate Hyperswitch iOS SDK with my Swift or Objective-C app?</summary>

Integrate the Juspay Hyperswitch iOS SDK using CocoaPods. The SDK requires iOS 15.1 or later and supports Swift and SwiftUI implementations.

**Integration steps**

1. Add the Hyperswitch SDK to your Podfile.

```
pod 'hyperswitch-sdk-ios'
```

2. Install dependencies.

```
pod install
```

3. Initialize the SDK with your publishable key.

```
import Hyperswitch
paymentSession = PaymentSession(publishableKey: <YOUR_PUBLISHABLE_KEY>)
```

4. For open source deployments, configure custom backend endpoints.

```
paymentSession = PaymentSession(
  publishableKey: <YOUR_PUBLISHABLE_KEY>,
  customBackendUrl: <YOUR_SERVER_URL>,
  customLogUrl: <YOUR_LOG_URL>
)
```

5. Create the payment session on your backend to generate the client secret.
6. Initialize the payment session with the client secret and present the payment sheet.

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/payment-experience/payment/mobile/ios/swift-with-rest-api-integration

</details>

<details>

<summary>How do I integrate Hyperswitch Android SDK with my Kotlin or Java app?</summary>

Integrate the Juspay Hyperswitch Android SDK using Gradle. The SDK requires Android 7.0 (API level 24) or later, Android Gradle Plugin 8.13 or later, and AndroidX.

**Integration steps**

1. Add the classpath to your project-level build.gradle.

```
buildscript {
  dependencies {
    classpath "io.hyperswitch:hyperswitch-gradle-plugin:$latest_version"
  }
}
```

2. Add the plugin to your app-level build.gradle.

```
plugins {
  id 'io.hyperswitch.plugin'
}
```

3. Configure SDK options.

```
hyperswitch {
  sdkVersion = "1.1.5"
  features = [HyperFeature.SCANCARD, HyperFeature.NETCETERA]
}
```

4. Implement HyperInterface in your Activity and initialize PaymentSession.

```
val paymentSession = PaymentSession(applicationContext, "YOUR_PUBLISHABLE_KEY")
```

5. Present the payment sheet and handle results.

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/payment-experience/payment/mobile/android/kotlin-with-rest-api-integration

</details>

<details>

<summary>How do I migrate from Stripe iOS or Android SDK to Hyperswitch?</summary>

Hyperswitch provides a migration path from Stripe SDK integrations.

**iOS migration**

Install dependencies.

```
npm install @juspay-tech/react-native-hyperswitch @juspay-tech/hyper-node
```

Update server-side import.

From:

```
const stripe = require("stripe")("your_stripe_api_key");
```

To:

```
const stripe = require("@juspay-tech/hyper-node")("your_hyperswitch_api_key");
```

Update Podfile sources.

```
source 'https://github.com/juspay/hyperswitch-pods.git'
source 'https://cdn.cocoapods.org/'
```

Replace Stripe dependency from `pod 'StripePaymentSheet'` to `pod 'hyperswitch', '1.0.0-alpha01'`

Update imports from StripePaymentSheet to hyperswitch.

**Android migration**

Install dependency.

```
npm install @juspay-tech/hyperswitch-node
```

Replace dependency from `implementation 'com.stripe:stripe-android:20.27.3'` to `implementation 'io.hyperswitch:hyperswitch-android:1.0.1'`

Update imports from `com.stripe.android.*` to `io.hyperswitch.*`.

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/migrate-from-stripe/ios\
https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/migrate-from-stripe/android

</details>

<details>

<summary>What test card numbers are available for different scenarios (success, decline, 3DS)?</summary>

Hyperswitch provides dummy connector test cards for common payment scenarios.

**Successful payments**

Visa — 4111111111111111 / 4242424242424242\
Mastercard — 5555555555554444\
Diners Club — 38000000000006\
American Express — 378282246310005\
Discover — 6011111111111117

**Decline scenarios**

Card declined — 4000000000000002\
Insufficient funds — 4000000000009995\
Lost card — 4000000000009987\
Stolen card — 4000000000009979

**3DS flows**

3DS success — 4000003800000446

For dummy connector cards, expiry date can be any future date and CVV can be any valid value.

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/payment-methods-setup/test-credentials

</details>

## Product FAQs

### SDK

<details>

<summary>How do I integrate Hyperswitch iOS SDK with my Swift or Objective-C app?</summary>

Integrate the Juspay Hyperswitch iOS SDK using CocoaPods. The SDK requires iOS 15.1 or later and supports Swift and SwiftUI implementations.

**Integration steps**

1. Add the Hyperswitch SDK to your Podfile.

```
pod 'hyperswitch-sdk-ios'
```

2. Install dependencies.

```
pod install
```

3. Initialize the SDK with your publishable key.

```
import Hyperswitch
paymentSession = PaymentSession(publishableKey: <YOUR_PUBLISHABLE_KEY>)
```

4. For open source deployments, configure custom backend endpoints.

```
paymentSession = PaymentSession(
  publishableKey: <YOUR_PUBLISHABLE_KEY>,
  customBackendUrl: <YOUR_SERVER_URL>,
  customLogUrl: <YOUR_LOG_URL>
)
```

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

```
buildscript {
  dependencies {
    classpath "io.hyperswitch:hyperswitch-gradle-plugin:$latest_version"
  }
}
```

2. Add the plugin to your app-level build.gradle.

```
plugins {
  id 'io.hyperswitch.plugin'
}
```

3. Configure SDK options.

```
hyperswitch {
  sdkVersion = "1.1.5"
  features = [HyperFeature.SCANCARD, HyperFeature.NETCETERA]
}
```

4. Implement HyperInterface in your Activity and initialize PaymentSession.

```
val paymentSession = PaymentSession(applicationContext, "YOUR_PUBLISHABLE_KEY")
```

5. Present the payment sheet and handle results.

Documentation:\
[https://docs.hyperswitch.io/explore-hyperswitch/payment-experience/payment/mobile/android/kotlin-with-rest-api-integration](https://docs.hyperswitch.io/explore-hyperswitch/payment-experience/payment/mobile/android/kotlin-with-rest-api-integration)

</details>

<details>

<summary>How do I migrate from Stripe iOS or Android SDK to Hyperswitch?</summary>

Hyperswitch provides a migration path from Stripe SDK integrations.

**iOS migration**

Install dependencies.

```
npm install @juspay-tech/react-native-hyperswitch @juspay-tech/hyper-node
```

Update server-side import.

From:
```
const stripe = require("stripe")("your_stripe_api_key");
```

To:
```
const stripe = require("@juspay-tech/hyper-node")("your_hyperswitch_api_key");
```

Update Podfile sources.

```
source 'https://github.com/juspay/hyperswitch-pods.git'
source 'https://cdn.cocoapods.org/'
```

Replace Stripe dependency.

From:
```
pod 'StripePaymentSheet'
```

To:
```
pod 'hyperswitch', '1.0.0-alpha01'
```

Update imports from StripePaymentSheet to hyperswitch.

**Android migration**

Install dependency.

```
npm install @juspay-tech/hyperswitch-node
```

Replace dependency.

From:
```
implementation 'com.stripe:stripe-android:20.27.3'
```

To:
```
implementation 'io.hyperswitch:hyperswitch-android:1.0.1'
```

Update imports from com.stripe.android.* to io.hyperswitch.*.

Documentation:\
[https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/migrate-from-stripe/ios](https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/migrate-from-stripe/ios)\
[https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/migrate-from-stripe/android](https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/migrate-from-stripe/android)

</details>

<details>

<summary>What mobile-specific payment flows are supported?</summary>

Hyperswitch supports multiple wallet payment methods on mobile.

**Apple Pay**

- Available in 75+ countries
- Supported on iOS (in-app) and Web (Safari)
- Requires Apple Developer Account, Merchant ID, and domain verification
- Supports both Hyperswitch decryption and PSP decryption flows

**Google Pay**

- Available in 70+ countries on Web and Android
- iOS support limited to US and India
- Supports in-app and web transactions
- Requires Google Pay test cards for sandbox testing
- Production deployment requires Google approval

**Other wallets**

- PayPal
- Samsung Pay

The Android SDK also provides widgets for Google Pay, PayPal, and Express Checkout.

Documentation:\
[https://docs.hyperswitch.io/explore-hyperswitch/wallets/apple-pay](https://docs.hyperswitch.io/explore-hyperswitch/wallets/apple-pay)\
[https://docs.hyperswitch.io/explore-hyperswitch/wallets/google-pay](https://docs.hyperswitch.io/explore-hyperswitch/wallets/google-pay)

</details>

<details>

<summary>How do I handle deep linking for mobile redirects such as 3DS or wallets?</summary>

Hyperswitch supports native 3DS authentication designed to minimize redirections.

**Native 3DS authentication**

- In-line 3DS challenge flows
- Frictionless authentication using risk-based evaluation
- Native OTP experience instead of web views

External 3DS providers such as Netcetera and 3DSecure.io can be integrated.

**Redirect flow handling**

The SDK automatically handles redirects for:

- 3DS card payments
- Bank redirects such as iDEAL, Giropay, eps
- Wallet flows such as PayPal and Klarna
- Bank transfer flows

Documentation:\
[https://docs.hyperswitch.io/explore-hyperswitch/workflows/3ds-decision-manager/native-3ds-authentication-for-mobile-payments](https://docs.hyperswitch.io/explore-hyperswitch/workflows/3ds-decision-manager/native-3ds-authentication-for-mobile-payments)

</details>

<details>

<summary>Can I customize the payment sheet appearance on mobile?</summary>

Yes. Hyperswitch provides customization options for payment sheet UI on both iOS and Android.

**Fonts**

Configure custom fonts using:

- typography.fontResId on Android
- configuration.appearance.font.base on iOS

**Colors**

appBarIcon — icons in payment page
component — background of inputs
componentBorder — border color for components
error — error message colors
primary — primary theme color
surface — payment page background
placeholderText — input placeholder text

**Shapes**

cornerRadiusDp — corner radius for input fields
borderStrokeWidthDp — border width for components

Example Android configuration:

```
val appearance = PaymentSheet.Appearance(
  typography = PaymentSheet.Typography(10.0f, R.font.MY_FONT)
)
```

Documentation:\
[https://docs.hyperswitch.io/explore-hyperswitch/payment-experience/payment/mobile/android/customization](https://docs.hyperswitch.io/explore-hyperswitch/payment-experience/payment/mobile/android/customization)\
[https://docs.hyperswitch.io/explore-hyperswitch/payment-experience/payment/mobile/ios/customization](https://docs.hyperswitch.io/explore-hyperswitch/payment-experience/payment/mobile/ios/customization)

</details>

<details>

<summary>What is the SDK size and performance impact on mobile apps?</summary>

Hyperswitch provides two SDK variants.

**Lite SDK**

- Artifact size under 300 KB
- Web-based UI components
- Minimal dependencies
- Faster initialization
- Full payment processing capabilities

**Full SDK**

- Larger artifact size
- Native UI components
- Additional features including card scanning and Netcetera 3DS

**Platform requirements**

Android — 7.0 (API 24)
Android Lite — 6.0 (API 23)
iOS — 15.1

Documentation:\
[https://docs.hyperswitch.io/explore-hyperswitch/payment-experience/payment/mobile/android/lite-sdk](https://docs.hyperswitch.io/explore-hyperswitch/payment-experience/payment/mobile/android/lite-sdk)\
[https://docs.hyperswitch.io/explore-hyperswitch/payment-experience/payment/mobile/ios/lite-sdk](https://docs.hyperswitch.io/explore-hyperswitch/payment-experience/payment/mobile/ios/lite-sdk)

</details>

<details>

<summary>Does the SDK support multiple payment methods and region-specific flows?</summary>

Yes. The Hyperswitch SDK supports multiple payment methods and adapts to regional payment requirements.

**Supported payment method categories**

- Cards — Visa, Mastercard, Amex, Discover, Diners, and others
- Wallets — Apple Pay, Google Pay, PayPal, Samsung Pay
- Bank redirects — iDEAL, Giropay, EPS, and others
- Bank transfers — ACH, SEPA, BACS, BECS, Multibanco
- Buy Now Pay Later — Klarna, Afterpay, and others

**Region-specific flows**

- 3DS authentication for card payments, including native 3DS for mobile
- PSD2 Strong Customer Authentication for European transactions
- Local wallet flows such as Apple Pay (75+ countries) and Google Pay (70+ countries)

Payment methods displayed in the checkout are determined by the connector and payment method configuration set in the relevant business profile, allowing different payment method sets to be presented for different regions or storefronts.

The complete list of supported payment methods and connectors is available at:\
https://juspay.io/integrations

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/payment-experience\
https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/payment-methods-setup

</details>

<details>

<summary>How are webhooks, callbacks, and asynchronous payment states handled?</summary>

Hyperswitch uses webhooks to notify your server of payment lifecycle events in real time.

**Webhook events**

Hyperswitch emits events for all key payment state transitions including `payment_succeeded`, `payment_failed`, `payment_processing`, `refund_succeeded`, `refund_failed`, `dispute_opened`, and `mandate_active` among others.

**Asynchronous payment states**

When a payment is submitted to a connector and the outcome is not immediately known:

1. Hyperswitch sets the payment status to `processing`.
2. When the connector sends a webhook with the final outcome, Hyperswitch updates the payment record.
3. The updated status is available via the Payments Retrieve API and delivered to your webhook endpoint.

**Signature verification**

All webhook requests include an HMAC signature in the `x-webhook-signature-512` header. Verify this signature using your `payment_response_hash_key` before processing events.

**Idempotent processing**

Each webhook payload includes a unique `event_id`. Store processed event IDs to safely handle duplicate deliveries caused by retries.

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/webhooks

</details>

<details>

<summary>What mobile-specific payment flows are supported?</summary>

**Apple Pay**

- Available in 75+ countries
- Supported on iOS (in-app) and Web (Safari)
- Requires Apple Developer Account, Merchant ID, and domain verification
- Supports both Hyperswitch decryption and PSP decryption flows

**Google Pay**

- Available in 70+ countries on Web and Android
- iOS support limited to US and India
- Supports in-app and web transactions
- Requires Google Pay test cards for sandbox testing
- Production deployment requires Google approval

**Other wallets**

- PayPal
- Samsung Pay

The Android SDK also provides widgets for Google Pay, PayPal, and Express Checkout.

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/wallets/apple-pay\
https://docs.hyperswitch.io/explore-hyperswitch/wallets/google-pay

</details>

<details>

<summary>How do I handle deep linking for mobile redirects such as 3DS or wallets?</summary>

Hyperswitch supports native 3DS authentication designed to minimize redirections.

**Native 3DS authentication**

- In-line 3DS challenge flows
- Frictionless authentication using risk-based evaluation
- Native OTP experience instead of web views

External 3DS providers such as Netcetera and 3DSecure.io can be integrated.

**Redirect flow handling**

The SDK automatically handles redirects for 3DS card payments, bank redirects (iDEAL, Giropay, eps), wallet flows (PayPal and Klarna), and bank transfer flows.

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/workflows/3ds-decision-manager/native-3ds-authentication-for-mobile-payments

</details>

<details>

<summary>Can I customize the payment sheet appearance on mobile?</summary>

Yes. Hyperswitch provides customization options for payment sheet UI on both iOS and Android.

**Fonts**

- `typography.fontResId` on Android
- `configuration.appearance.font.base` on iOS

**Colors**

- `appBarIcon` — icons in payment page
- `component` — background of inputs
- `componentBorder` — border color for components
- `error` — error message colors
- `primary` — primary theme color
- `surface` — payment page background
- `placeholderText` — input placeholder text

**Shapes**

- `cornerRadiusDp` — corner radius for input fields
- `borderStrokeWidthDp` — border width for components

Example Android configuration:

```
val appearance = PaymentSheet.Appearance(
  typography = PaymentSheet.Typography(10.0f, R.font.MY_FONT)
)
```

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/payment-experience/payment/mobile/android/customization\
https://docs.hyperswitch.io/explore-hyperswitch/payment-experience/payment/mobile/ios/customization

</details>

<details>

<summary>What is the SDK size and performance impact on mobile apps?</summary>

Hyperswitch provides two SDK variants.

**Lite SDK**

- Artifact size under 300 KB
- Web-based UI components
- Minimal dependencies
- Faster initialization
- Full payment processing capabilities

**Full SDK**

- Larger artifact size
- Native UI components
- Additional features including card scanning and Netcetera 3DS

**Platform requirements**

- Android — 7.0 (API 24)
- Android Lite — 6.0 (API 23)
- iOS — 15.1

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/payment-experience/payment/mobile/android/lite-sdk\
https://docs.hyperswitch.io/explore-hyperswitch/payment-experience/payment/mobile/ios/lite-sdk

</details>

### Core Payments / Orchestration

<details>

<summary>How does Hyperswitch prevent duplicate charges during retries?</summary>

Hyperswitch supports idempotency keys to ensure that duplicate API requests do not result in duplicate transactions.

When you include an idempotency key in a request, Hyperswitch checks whether a request with the same key has already been processed. If a matching request exists, the original response is returned without creating a new transaction.

Include the idempotency key in the request header:

```
Idempotency-Key: <your-unique-key>
```

The key should be a unique string generated by your system, such as a UUID.

Documentation:\
https://api-reference.hyperswitch.io/essentials/idempotency

</details>

<details>

<summary>Can I customise orchestration logic based on business rules?</summary>

Yes. Hyperswitch supports rule-based routing that allows merchants to define orchestration logic based on payment method, payment method type, transaction amount, currency, customer country, card network, and business profile.

Traffic can also be split across multiple connectors using percentage-based volume distribution.

3DS orchestration logic can be customised through the 3DS Decision Manager with rules based on issuer country, card network, transaction amount, and device type.

All routing rules can be configured and updated through the Control Centre without requiring code changes or redeployment.

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/workflows/intelligent-routing/rule-based-routing\
https://docs.hyperswitch.io/explore-hyperswitch/workflows/3ds-decision-manager/3ds-intelligence-engine

</details>

### Connectors

<details>

<summary>What payment methods are available in different regions?</summary>

The complete list of supported payment methods and processor integrations can be viewed at:\
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

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/connectors\
https://docs.hyperswitch.io/explore-hyperswitch/connectors/activate-connector-on-hyperswitch

</details>

<details>

<summary>Can I route specific payment methods through specific connectors?</summary>

Yes. Using Intelligent Routing, routing rules can be configured based on payment method, payment method type, transaction amount, currency, and customer country.

Traffic can be distributed across processors using percentage-based volume routing. If no routing rule applies, Hyperswitch uses the configured priority order of processors.

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/workflows/intelligent-routing\
https://docs.hyperswitch.io/explore-hyperswitch/workflows/intelligent-routing/rule-based-routing

</details>

<details>

<summary>How do I integrate Apple Pay, Google Pay, and other wallets?</summary>

Apple Pay — https://docs.hyperswitch.io/explore-hyperswitch/wallets/apple-pay

Google Pay — https://docs.hyperswitch.io/explore-hyperswitch/wallets/google-pay

PayPal — https://docs.hyperswitch.io/explore-hyperswitch/wallets/paypal

</details>

<details>

<summary>How does Hyperswitch normalize different PSP APIs into a single interface?</summary>

When a payment request is received, Hyperswitch accepts the request in its unified API format, translates it into the connector-specific format, submits it to the processor, translates the response back into the Hyperswitch unified format, and returns the normalised response to the merchant.

What is normalised across all connectors:

- Payment request and response schemas
- Error codes and decline reasons mapped to unified enums
- Webhook event formats
- Payment status values

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/connectors\
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

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/workflows/intelligent-routing\
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

- Each merchant account has a unique **Data Encryption Key (DEK)** used to encrypt connector API keys.
- Credentials are encrypted using **AES-256 symmetric encryption** through a master key.
- Sensitive values are masked during transmission and are not stored on local systems.

Connector credential management permissions are available to Merchant Developer and Profile Developer roles.

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/connectors/activate-connector-on-hyperswitch\
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

```
readinessProbe:
  httpGet:
    path: /health/ready
    port: 8080
  initialDelaySeconds: 5
  periodSeconds: 15
```

**Key metrics to monitor**

- Payment success and failure rates per connector
- Gateway latency for successful and failed transactions
- Distribution of processor error codes
- Webhook delivery success rates

Documentation:\
https://docs.hyperswitch.io/check-list-for-production/going-live/for-on-prem-setup/monitoring\
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

- `exploration_percent`
- routing bucket size
- aggregation pipeline size

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/workflows/intelligent-routing\
https://docs.hyperswitch.io/explore-hyperswitch/workflows/intelligent-routing/auth-rate-based-routing\
https://docs.hyperswitch.io/explore-hyperswitch/workflows/smart-retries

</details>

<details>

<summary>How is reconciliation handled across multiple PSPs?</summary>

The Hyperswitch reconciliation module is built on **double-entry accounting principles**, providing a complete audit trail of financial events, point-in-time balances for finance teams, immutable transaction history, and auditable exception handling processes.

The reconciliation system also surfaces billing anomalies such as processor billing discrepancies, invoice mismatches, and unexpected fee changes.

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/payments-modules/reconciliation-product

</details>

<details>

<summary>Can I manage routing rules and configurations without redeploying code?</summary>

Yes. The following configurations can be updated in real time through the Control Centre without any code changes or redeployment:

- Routing rules — rule-based, volume-based, and fallback routing
- Connector priority order
- Active connectors and payment methods per profile
- 3DS exemption rules
- Webhook endpoints
- API key management

Navigate to **Workflow → Routing** to update routing rules. Changes are applied immediately to live traffic.

Routing rules can also be updated programmatically via the Hyperswitch API.

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/workflows/intelligent-routing\
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

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/webhooks\
https://docs.hyperswitch.io/explore-hyperswitch/payments-modules/reconciliation-product\
https://docs.hyperswitch.io/explore-hyperswitch/account-management/analytics-and-operations/exporting-payments-data

</details>

<details>

<summary>How do I create custom reports for my business needs?</summary>

Hyperswitch does not currently provide a built-in custom report builder. Payment data is exported as **CSV files to Amazon S3**, which can then be ingested into Amazon Redshift or other analytics platforms.

Exported fields include `payment_id`, `attempt_id`, `status`, `amount`, `currency`, `customer_id`, `created_at`, `connector`, `payment_method`, `error_message`, and `metadata`.

Once available in your data warehouse, generate reports using SQL queries or integrate with BI tools such as Tableau, Looker, or Power BI.

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/account-management/analytics-and-operations/exporting-payments-data

</details>

<details>

<summary>How do I export payment data to my data warehouse (Snowflake or BigQuery)?</summary>

Hyperswitch exports payment data through **S3-based data pipelines** for ingestion into Snowflake, BigQuery, or Amazon Redshift.

Data is exported in **CSV format with headers**, organised by merchant ID and date, updated approximately every **6 hours**, and retained for **7 days**.

```
s3://<bucket>/<merchant_id>/<version>/payments/<date>.csv
```

Merchants can configure ingestion pipelines using Redshift COPY jobs, Lambda-based loaders, or scheduled ETL jobs.

Documentation:\
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

Documentation:\
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

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/account-management/manage-your-team

</details>

<details>

<summary>Is real-time payment analytics available?</summary>

Yes. Hyperswitch provides real-time analytics through the Control Centre, including payment status updates, checkout analytics, drop-off analysis, 3DS outcomes, and fraud detection results.

Webhooks also provide real-time event notifications for `payment_succeeded`, `payment_failed`, and `refund_succeeded` among other events.

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/account-management/analytics-and-operations\
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

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/payments-modules/reconciliation-product\
https://docs.hyperswitch.io/check-list-for-production/going-live/for-on-prem-setup/monitoring\
https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/webhooks\
https://docs.hyperswitch.io/explore-hyperswitch/payments-modules/ai-powered-cost-observability

</details>

### Retries & Routing

<details>

<summary>How does intelligent routing work in Hyperswitch?</summary>

Hyperswitch supports the following routing types, all configurable through the Control Centre without code deployment:

- **Rule-based routing** — conditions based on payment method, amount, currency, card network, and customer country
- **Volume-based routing** — percentage-based traffic distribution across multiple connectors
- **Elimination routing** — connectors with elevated failure rates are deprioritised dynamically
- **Default fallback routing** — the configured connector priority order is used if no rule applies
- **Authorization rate based routing** — a Multi-Armed Bandit (MAB) model continuously evaluates and adjusts routing based on real-time authorisation performance

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/workflows/intelligent-routing\
https://docs.hyperswitch.io/explore-hyperswitch/workflows/intelligent-routing/auth-rate-based-routing

</details>

<details>

<summary>How are retry strategies configured to avoid revenue leakage?</summary>

Hyperswitch classifies decline codes into retryable and non-retryable categories. Non-retryable declines are not retried, avoiding unnecessary processing fees.

**Retry types**

- **Cascading retry** — retry through an alternative processor
- **Step-up retry** — retry with 3DS authentication added for suspected fraud declines
- **Network retry** — retry through alternative debit networks where available

The `manual_retry_allowed` flag permits customers to retry payments manually, for example by updating card details or selecting a different payment method.

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/workflows/smart-retries\
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

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/workflows/smart-retries/processor-error-code-mapping

</details>

<details>

<summary>How do I handle bank-level declines that I cannot control?</summary>

Bank-level declines originate from the card issuer and are outside the merchant's direct control. Examples include `insufficient_funds`, `call_issuer`, `account_closed`, and `pickup_card`.

**Smart retry mechanisms**

- **Cascading retry** — attempts the payment through an alternative processor
- **Step-up retry** — retries with 3DS authentication when fraud is suspected
- **Network retry** — attempts through different debit networks when available

The `manual_retry_allowed` setting allows customers to update card details or use a different payment method.

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/workflows/smart-retries\
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

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/workflows/smart-retries/processor-error-code-mapping\
https://api-reference.hyperswitch.io/essentials/error_codes

</details>

<details>

<summary>Which decline codes are retryable (soft) vs non-retryable (hard)?</summary>

**Retryable (soft) declines**

| Decline Code                           | Reason                                              |
| -------------------------------------- | --------------------------------------------------- |
| `processing_temporarily_unavailable`   | Processor or network temporarily unavailable        |
| `system_malfunction`                   | Technical issue at the processor                    |
| `transaction_not_permitted_on_network` | Network-level restriction that may resolve on retry |
| `invalid_cryptogram`                   | Cryptographic token issue that may resolve on retry |
| `network_token_not_supported`          | Network token not supported by this processor       |

**Non-retryable (hard) declines**

| Decline Code                       | Reason                                  |
| ---------------------------------- | --------------------------------------- |
| `insufficient_funds`               | Insufficient balance                    |
| `fraudulent`                       | Transaction flagged as fraudulent       |
| `lost_card`                        | Card reported as lost                   |
| `stolen_card`                      | Card reported as stolen                 |
| `expired_card`                     | Card has expired                        |
| `pickup_card`                      | Card cannot be used                     |
| `do_not_honor`                     | Issuer declined without specific reason |
| `card_decline_rate_limit_exceeded` | Card declined too many times            |

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/workflows/smart-retries/processor-error-code-mapping

</details>

<details>

<summary>What is the structure of error responses?</summary>

| Field     | Type   | Description                                                |
| --------- | ------ | ---------------------------------------------------------- |
| `type`    | string | Error category (e.g. `invalid_request`, `connector_error`) |
| `message` | string | Human-readable description of the error                    |
| `code`    | string | Hyperswitch-specific error code                            |
| `reason`  | string | Additional context about the error, if available           |

**Example**

```json
{
  "type": "invalid_request",
  "message": "Missing required field: amount",
  "code": "IR_06",
  "reason": "The amount field is required to create a payment"
}
```

**HTTP status codes**

- `400` — Invalid request or missing required fields
- `401` — Authentication failure
- `404` — Resource not found
- `422` — Unprocessable entity
- `500` — Internal server error

Documentation:\
https://api-reference.hyperswitch.io/essentials/error_codes

</details>

<details>

<summary>How are connector-specific error codes normalised?</summary>

Hyperswitch maps processor-specific error codes into a unified set of error enums.

| Connector | Raw error code       | Hyperswitch error code |
| --------- | -------------------- | ---------------------- |
| Stripe    | `card_declined`      | `card_declined`        |
| Adyen     | `Refused`            | `card_declined`        |
| Stripe    | `insufficient_funds` | `insufficient_funds`   |
| Adyen     | `NotEnoughBalance`   | `insufficient_funds`   |

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/workflows/smart-retries/processor-error-code-mapping\
https://api-reference.hyperswitch.io/essentials/error_codes

</details>

### Cost Observability

<details>

<summary>How can I track payment processing fees across multiple PSPs?</summary>

Hyperswitch provides an **AI-powered cost observability module** that surfaces processing fees per connector, billing discrepancies, unexpected fee changes, and cost trends over time.

Cost data can be exported via the S3 data pipeline for finance reporting and invoice reconciliation.

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/payments-modules/ai-powered-cost-observability

</details>

<details>

<summary>How does Hyperswitch surface hidden fees or inefficiencies?</summary>

The cost observability module detects:

- **Processor billing discrepancies** — differences between expected and actual processor invoices
- **Invoice mismatches** — amounts charged that do not match expected fee structures
- **Unexpected fee changes** — sudden changes in processing rates or fee categories
- **Cost anomalies** — unusual patterns in processing costs

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/payments-modules/ai-powered-cost-observability

</details>

<details>

<summary>How do I export cost and transaction data for finance teams?</summary>

Payment data is exported to S3 in CSV format, updated approximately every **6 hours**, and retained for **7 days**.

```
s3://<bucket>/<merchant_id>/<version>/payments/<date>.csv
```

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/account-management/analytics-and-operations/exporting-payments-data

</details>

### Revenue Recovery & Refunds

<details>

<summary>How does Hyperswitch recover failed payments automatically?</summary>

When a payment fails, Hyperswitch analyses the error code and automatically retries through an alternative connector for retryable declines.

**Retry types**

- **Cascading retry** — routes through an alternative processor
- **Step-up retry** — retries with 3DS authentication added for suspected fraud declines
- **Network retry** — retries through alternative debit networks where available

Elimination routing automatically deprioritises connectors with elevated failure rates.

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/workflows/smart-retries

</details>

<details>

<summary>How are soft declines handled differently from hard declines?</summary>

**Soft declines (retryable)** — temporary failures caused by processor or network issues. Hyperswitch automatically retries through alternative connectors.

Examples: `processing_temporarily_unavailable`, `system_malfunction`, `invalid_cryptogram`

**Hard declines (non-retryable)** — definitive rejections that will not succeed regardless of the connector. Hyperswitch does not automatically retry hard declines.

Examples: `fraudulent`, `stolen_card`, `expired_card`, `insufficient_funds`, `do_not_honor`

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/workflows/smart-retries\
https://docs.hyperswitch.io/explore-hyperswitch/workflows/smart-retries/processor-error-code-mapping

</details>

<details>

<summary>What happens when a refund fails?</summary>

When a refund fails, Hyperswitch sends a **`refund_failed`** webhook event. The refund status is updated to failed, the failure details are available via the Refunds Retrieve API, and the failed refund appears in the **Payment Operations dashboard**.

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/webhooks\
https://docs.hyperswitch.io/explore-hyperswitch/account-management/analytics-and-operations

</details>

<details>

<summary>How long do refunds take to appear on customer statements?</summary>

Refund timing depends on the payment processor and card issuer. In most cases, refunds appear within **5 to 14 business days**.

</details>

<details>

<summary>How do I track refund status and completion?</summary>

**API**

```
GET /refunds/{refund_id}
```

**Webhooks**

- `refund_succeeded`
- `refund_failed`

**Control Centre**

Refund status is visible in the **Payment Operations dashboard**.

Documentation:\
https://api-reference.hyperswitch.io/v1/refunds/refunds--retrieve#refunds-retrieve

</details>

<details>

<summary>Can I issue multiple partial refunds for a single payment?</summary>

Yes. Specify an amount less than the original payment. The total refunded amount must not exceed the original payment value. Each partial refund is processed as a separate operation linked to the original payment.

Documentation:\
https://api-reference.hyperswitch.io/v1/refunds/refunds--create#refunds-create

</details>

<details>

<summary>What refund reason codes are available?</summary>

- `duplicate` — The payment was processed more than once
- `fraudulent` — The transaction was identified as fraudulent
- `customer_request` — The customer requested the refund
- `other` — Any other refund reason

The `reason` field is optional.

Documentation:\
https://api-reference.hyperswitch.io/v1/refunds/refunds--create

</details>

<details>

<summary>How do I issue full vs partial refunds?</summary>

**Full refund**

```json
POST /refunds
{
  "payment_id": "pay_xxxxx"
}
```

**Partial refund**

```json
POST /refunds
{
  "payment_id": "pay_xxxxx",
  "amount": 500
}
```

Documentation:\
https://api-reference.hyperswitch.io/v1/refunds/refunds--create

</details>

### Trust & Reliability

<details>

<summary>How does Hyperswitch ensure high availability and fault tolerance?</summary>

**Health check endpoint**

```
curl http://localhost:8080/health/ready
```

**Kubernetes deployment**

- Horizontal pod autoscaling
- Readiness and liveness probes
- Automatic pod restart on failure
- Multi-availability-zone deployments

**Multi-connector failover**

- Elimination routing — deprioritises connectors with elevated failure rates
- Smart retries — routes failed transactions to alternative connectors
- Fallback routing — defaults to a secondary connector if a primary is unavailable

Documentation:\
https://docs.hyperswitch.io/check-list-for-production/going-live/for-on-prem-setup/monitoring\
https://docs.hyperswitch.io/learn-more/hyperswitch-architecture

</details>

<details>

<summary>How are webhooks verified and reconciled safely?</summary>

Generate an HMAC-SHA512 signature using your `payment_response_hash_key` and compare against the `x-webhook-signature-512` header.

Use the `event_id` field in the webhook payload to detect and ignore duplicate deliveries.

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/webhooks

</details>

<details>

<summary>What are the security best practices for integrating Hyperswitch?</summary>

**API key management**

- Never expose secret keys in frontend code or public repositories
- Use publishable keys (`pk_snd_` or `pk_prd_`) only in client-side code
- Rotate credentials if a key is suspected to be compromised

**Webhook security**

- Verify all incoming webhook requests using the `x-webhook-signature-512` header
- Reject requests with invalid or missing signatures
- Use HTTPS endpoints for webhook receivers

**Connector credentials**

- Encrypted using AES-256 symmetric encryption with a unique DEK per merchant account
- Avoid storing in unencrypted configuration files or environment variables

**Access control**

- Use role-based access control to restrict team member permissions
- Regularly review and revoke access for team members who no longer require it

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/security-and-compliance/security\
https://docs.hyperswitch.io/check-list-for-production/going-live

</details>

### Vault & Tokenization

<details>

<summary>How do I migrate existing tokens from another provider to Hyperswitch?</summary>

1. Request a data import from the Hyperswitch team.
2. Hyperswitch shares its **PCI Attestation of Compliance (AoC)** certificate.
3. Request a secure data export from your existing processor using the Hyperswitch AoC.
4. Hyperswitch provides a **public PGP key** for encryption.
5. The existing processor encrypts the token data and transfers it via **SFTP**.
6. Hyperswitch imports the data into its vault.
7. Updated customer and payment method reference IDs are shared with you.

**Required fields**: `card_number` (PAN), `card_expiry_month`, `card_expiry_year`, `payment_instrument_id`, `original_network_transaction_id`

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/account-management/data-migration/import-data-to-hyperswitch

</details>

<details>

<summary>Can tokens be used across multiple connectors or processors?</summary>

Yes. The **unified `payment_method_id`** abstracts connector-specific tokens and allows routing payments through different processors without re-collecting card details.

**Enable connector-agnostic MIT**

```
POST /account/:merchant_id/business_profile/:profile_id/toggle_connector_agnostic_mit
```

```json
{ "enabled": true }
```

Supported processors currently include Stripe, Adyen, and Cybersource.

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/tokenization-and-saved-cards/pg-agnostic-recurring-payments

</details>

<details>

<summary>How do I handle token expiration and card updates?</summary>

Network tokens automatically update when cards are replaced due to expiry, loss, or reissuance.

Juspay acts as both **Token Requestor (TR)** and **Token Service Provider (TSP)**, enabling automatic provisioning and refresh without requiring merchants to collect card details again.

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/tokenization-and-saved-cards/network-tokenisation

</details>

<details>

<summary>What is the difference between PSP tokens and network tokens?</summary>

| Token Type                              | Description                                            | Scope                                        | Portability                                    |
| --------------------------------------- | ------------------------------------------------------ | -------------------------------------------- | ---------------------------------------------- |
| Hyperswitch Token (`payment_method_id`) | Universal token generated by Hyperswitch Vault         | Merchant + Customer scoped                   | Portable across connectors and vault providers |
| Connector Token (PSP Token)             | Token issued by a specific processor                   | Connector-specific                           | Locked to that connector                       |
| Network Token                           | Token issued by card networks (Visa, Mastercard, Amex) | Merchant + Customer + Token Requestor scoped | Portable across processors                     |
| Vault Token                             | Internal reference to stored card in vault             | Vault-specific                               | Used internally for detokenisation             |

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/workflows/vault/self-hosted-orchestration-with-outsourced-pci-vault\
https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/tokenization-and-saved-cards/network-tokenisation

</details>

<details>

<summary>How do I implement card-on-file (COF) payment flows?</summary>

**CIT (first payment)**

Create the initial payment with `setup_future_usage`:

- `on_session` — for future customer-present payments
- `off_session` — for merchant-initiated payments

Include `customer_acceptance` in the request. The response returns a `payment_method_id` to store for future transactions.

**MIT (subsequent payments)**

```json
{
  "off_session": true,
  "recurring_details": {
    "type": "payment_method_id",
    "data": "pm_lmTnIO5EdCiiMgRPrV9x"
  }
}
```

Documentation:\
https://docs.hyperswitch.io/about-hyperswitch/payment-suite-1/payments-cards/saved-card/save-a-payment-method

</details>

<details>

<summary>Can I store cards in multiple vaults for redundancy?</summary>

Hyperswitch supports a **self-hosted orchestration architecture with outsourced PCI vaults**, allowing merchants to use Hyperswitch's native vault, integrate a bring-your-own vault, or support multiple vault backends.

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/workflows/vault/self-hosted-orchestration-with-outsourced-pci-vault

</details>

<details>

<summary>How do I update CVV on a stored card without re-tokenizing?</summary>

CVV is **not stored** by Hyperswitch or any PCI-compliant vault, in accordance with PCI DSS requirements. Because CVV is never stored, it cannot be updated on a stored card token.

For customer-initiated transactions requiring CVV, collect it at checkout and submit it as part of the payment request using the stored `payment_method_id`. It is transmitted directly to the processor and not stored.

For **merchant-initiated transactions (MIT)** and recurring payments, CVV is typically not required by the processor.

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/tokenization-and-saved-cards\
https://docs.hyperswitch.io/explore-hyperswitch/security-and-compliance/security

</details>

### 3DS & Authentication

<details>

<summary>What is the 3DS Decision Manager and how does it work?</summary>

The **3DS Decision Manager** determines when to apply 3D Secure during a payment transaction.

**Key capabilities**

- Intelligent 3DS routing based on transaction risk and merchant-configured rules
- Exemption management for SCA
- Native 3DS support inside mobile apps
- External 3DS result import

**Decision factors**

- Transaction amount and currency
- Customer device and location
- Card issuer country and risk profile
- Merchant-configured rules

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/workflows/3ds-decision-manager\
https://docs.hyperswitch.io/explore-hyperswitch/workflows/3ds-decision-manager/3ds-intelligence-engine

</details>

<details>

<summary>How do I configure 3DS exemption rules in Hyperswitch?</summary>

Navigate to **Workflow → 3DS Exemption Rules**.

**Condition parameters**: Card network, issuer country, transaction amount, currency, customer device type, transaction type (CIT or MIT).

**Outcome options**: Request 3DS exemption / Apply 3DS authentication / No preference (default).

**Supported exemption types**: Low-value, Transaction Risk Analysis (TRA), merchant-initiated transaction, recurring transaction.

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/workflows/3ds-decision-manager/3ds-intelligence-engine

</details>

<details>

<summary>How do I implement native 3DS authentication for mobile apps?</summary>

**Supported 3DS providers**: Netcetera, 3dsecure.io, Juspay native 3DS solution.

**Android setup**

```
hyperswitch {
  features = [HyperFeature.NETCETERA]
}
```

**iOS setup**

Configure the 3DS provider during SDK initialisation and handle authentication challenges directly inside the application.

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/workflows/3ds-decision-manager/native-3ds-authentication-for-mobile-payments

</details>

<details>

<summary>Which versions of 3D Secure does Hyperswitch support?</summary>

| Version | Description       | Key features                              |
| ------- | ----------------- | ----------------------------------------- |
| 3DS 1.0 | Original protocol | Browser redirect flow, static passwords   |
| 3DS 2.0 | Enhanced protocol | Risk-based authentication, mobile support |
| 3DS 2.1 | Current standard  | SCA compliant, device data collection     |
| 3DS 2.2 | Latest version    | Improved exemption support                |

Hyperswitch automatically uses 3DS 2.x if supported by the issuer, falling back to 3DS 1.0 if not.

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/workflows/3ds-decision-manager

</details>

<details>

<summary>Can I import 3DS authentication results from an external provider?</summary>

Yes. Include the external authentication data in the Payments Create API request.

```json
"three_ds_data": {
  "authentication_cryptogram": {
    "cavv": { "authentication_cryptogram": "3q2+78r+ur7erb7vyv66vv////8=" }
  },
  "ds_trans_id": "c4e59ceb-a382-4d6a-bc87-385d591fa09d",
  "version": "2.1.0",
  "eci": "05",
  "transaction_status": "Y",
  "exemption_indicator": "low_value"
}
```

**Required fields**: `ds_trans_id`, `authentication_value` (CAVV/AEV), `eci`

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/workflows/3ds-decision-manager/import-3d-secure-results

</details>

<details>

<summary>How do I test 3DS flows in the sandbox environment?</summary>

**Test card**: 3DS success — 4000003800000446

**Demo playground**: https://demostore3ds.netlify.app/

Navigate to **Workflow → 3DS Exemption Rules** to create test rules and verify rule behaviour.

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/payment-methods-setup/test-credentials\
https://docs.hyperswitch.io/explore-hyperswitch/workflows/3ds-decision-manager/3ds-intelligence-engine

</details>

<details>

<summary>How does 3DS authentication interact with payment routing decisions?</summary>

Routing rules can consider 3DS requirements when selecting a processor — some processors support better 3DS pass-through rates and routing rules may prioritise processors that support certain exemption types.

After authentication, the payment is sent to the selected processor with 3DS data (CAVV and ECI) included in the transaction request. Some processors perform 3DS internally; others accept external authentication data from Hyperswitch.

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/workflows/3ds-decision-manager\
https://docs.hyperswitch.io/explore-hyperswitch/workflows/intelligent-routing

</details>

<details>

<summary>How does Hyperswitch help with Strong Customer Authentication (SCA) compliance?</summary>

Hyperswitch supports **SCA** requirements under **PSD2** in the European Economic Area.

- 3DS 2.x support (versions 2.0, 2.1, and 2.2)
- Exemption management — low-value, TRA, MIT, and recurring
- 3DS intelligence engine — automatically applies merchant-defined exemption rules
- Delegated authentication support

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/workflows/3ds-decision-manager\
https://docs.hyperswitch.io/explore-hyperswitch/workflows/3ds-decision-manager/3ds-intelligence-engine

</details>

### Webhooks

<details>

<summary>How do I verify webhook signatures for security?</summary>

Generate an HMAC-SHA512 signature using your `payment_response_hash_key` and compare against the `x-webhook-signature-512` header. An alternative `x-webhook-signature-256` header is available for systems that do not support SHA512.

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/webhooks

</details>

<details>

<summary>What is the retry policy for failed webhook deliveries?</summary>

A webhook delivery is considered successful when the receiving server returns an **HTTP 2XX response**. Hyperswitch retries for up to **24 hours**.

| Retry attempt      | Interval   |
| ------------------ | ---------- |
| 1st retry          | 1 minute   |
| 2nd and 3rd retry  | 5 minutes  |
| 4th to 8th retry   | 10 minutes |
| 9th to 13th retry  | 1 hour     |
| 14th to 16th retry | 6 hours    |

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/webhooks

</details>

<details>

<summary>How do I handle duplicate webhook events?</summary>

Use the unique `event_id` field in each webhook payload to detect and ignore duplicates. Store processed event IDs in a persistent datastore and check before processing each event. Retain IDs for at least 24 hours.

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/webhooks

</details>

<details>

<summary>Are webhooks delivered in order? How should I handle out-of-order events?</summary>

Webhook events are delivered asynchronously and may arrive out of order. Use the `updated` timestamp field and only apply updates if the incoming event reflects a more recent state than what is already stored.

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/webhooks

</details>

<details>

<summary>What timeout should my webhook endpoint support?</summary>

Return an HTTP 2XX response quickly, process heavy business logic asynchronously, and return a success response once the event has been accepted for processing.

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/webhooks

</details>

<details>

<summary>What webhook events are available?</summary>

**Payment**: `payment_succeeded` · `payment_failed` · `payment_processing` · `payment_cancelled` · `payment_authorized` · `payment_captured`

**Refund**: `refund_succeeded` · `refund_failed`

**Dispute**: `dispute_opened` · `dispute_expired` · `dispute_accepted` · `dispute_cancelled` · `dispute_challenged` · `dispute_won` · `dispute_lost`

**Mandate**: `mandate_active` · `mandate_revoked`

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/webhooks

</details>

<details>

<summary>When should I use webhooks vs polling for payment status updates?</summary>

**Webhooks (recommended)** — use for real-time event notifications, event-driven workflows, and asynchronous events such as refunds and disputes.

**API polling** — use when your server cannot receive inbound webhook requests, or as a fallback alongside webhooks.

```
GET /payments/{payment_id}
```

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/webhooks

</details>

### Account Management

<details>

<summary>What is the account structure in Hyperswitch?</summary>

| Level                      | Description                            | Use Case                                          |
| -------------------------- | -------------------------------------- | ------------------------------------------------- |
| Organisation               | Top-level entity                       | Corporate parent or holding company               |
| Merchant                   | Business entity under the organisation | Individual business or subsidiary                 |
| Profile (Business Profile) | Operational unit within a merchant     | Website, mobile app, brand, or regional operation |

Each business profile maintains independent configurations for payment methods, connector credentials, routing rules, webhook endpoints, and API keys.

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/account-management/multiple-accounts-and-profiles/hyperswitch-account-structure

</details>

<details>

<summary>What roles and permissions are available for team management?</summary>

| Role               | Access Level | Capabilities                                        |
| ------------------ | ------------ | --------------------------------------------------- |
| Organisation Admin | Organisation | Full access across all merchants and profiles       |
| Merchant Admin     | Merchant     | Full access across all profiles within the merchant |
| Profile Admin      | Profile      | Full access to a specific business profile          |
| Merchant Developer | Merchant     | Manage API keys and view analytics                  |
| Profile Developer  | Profile      | Manage profile API keys and view analytics          |
| Merchant Operator  | Merchant     | Manage operational workflows and view analytics     |
| Profile Operator   | Profile      | Perform operational tasks within a profile          |
| Customer Support   | Merchant     | View transactions and search payments               |

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/account-management/manage-your-team

</details>

### Testing & Sandbox

<details>

<summary>How do I simulate specific error codes and decline scenarios for testing?</summary>

Generic decline — 4000000000000002\
Insufficient funds — 4000000000009995\
Lost card — 4000000000009987\
Stolen card — 4000000000009979

Hyperswitch standardises upstream processor error codes into common enums such as `insufficient_funds`, `expired_card`, `card_declined`, and `risk_decline`.

Documentation:\
https://api-reference.hyperswitch.io/essentials/error_codes

</details>

<details>

<summary>How do I test 3D Secure authentication flows in sandbox?</summary>

3DS success card — 4000003800000446

Navigate to **Workflow → 3DS Exemption Rules** to configure custom rules. Demo playground: https://demostore3ds.netlify.app/

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/workflows/3ds-decision-manager

</details>

<details>

<summary>How do I test webhook handling locally during development?</summary>

1. Create an HTTP or HTTPS endpoint on your server.
2. Navigate to **Developer → Payment Settings → Webhook Setup** in the Control Centre.

**Endpoints**\
Sandbox: `sandbox.hyperswitch.io/webhooks/{merchant_id}/{merchant_connector_id}`\
Production: `api.hyperswitch.io/webhooks/{merchant_id}/{merchant_connector_id}`

Generate an HMAC-SHA512 signature using the `payment_response_hash_key` and compare against the `x-webhook-signature-512` header. Hyperswitch retries delivery for up to **24 hours** if no HTTP 2XX response is received.

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/webhooks

</details>

<details>

<summary>What test bank account numbers are available for ACH or SEPA testing?</summary>

| Method | Region         | Currency | Settlement time        |
| ------ | -------------- | -------- | ---------------------- |
| ACH    | United States  | USD      | Up to 4 business days  |
| SEPA   | European Union | EUR      | Up to 14 business days |
| BACS   | United Kingdom | GBP      | Up to 6 business days  |
| BECS   | Australia      | AUD      | Up to 3 business days  |

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/payment-methods-setup/banks/bank-debits

</details>

<details>

<summary>How do I run load tests through Hyperswitch? Are test calls billed?</summary>

``` npm install -g 'https://github.com/knutties/newman.git#feature/newman-dir' ``` ``` cargo run --package test_utils --bin test_utils -- \
--connector-name= \
--base-url=http://127.0.0.1:8080 \
--admin-api-key=test_admin ```

Routing simulation tool: https://hyperswitch-ten.vercel.app/

Documentation:\
https://docs.hyperswitch.io/learn-more/test-payments-through-newman-wrapped-in-rust

</details>

### Payouts

<details>

<summary>What payout rails are available and how do they compare?</summary>

| Payout Rail    | Region         | Currency | Settlement Time                  |
| -------------- | -------------- | -------- | -------------------------------- |
| ACH            | United States  | USD      | 1–4 business days                |
| SEPA           | European Union | EUR      | 1–2 business days                |
| BACS           | United Kingdom | GBP      | 2–3 business days                |
| Card payouts   | Global         | Multiple | 1–3 business days                |
| Wallet payouts | Global         | Multiple | Near real-time to 1 business day |

Full connector list: https://juspay.io/integrations

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/payouts

</details>

<details>

<summary>How does Hyperswitch handle payout failures and retries?</summary>

When a payout fails, the status is updated to `failed` and a webhook event is sent with failure details. Resubmit retryable failures using an idempotency key to prevent duplicates. For non-retryable failures such as invalid account details, resolve the underlying issue before resubmitting.

**Payout webhook events**: `payout_success` · `payout_failed` · `payout_processing` · `payout_cancelled` · `payout_initiated` · `payout_expired` · `payout_reversed`

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/payouts

</details>

<details>

<summary>How do I track the status of payouts?</summary>

``` GET /payouts/{payout_id} ```

| Status                 | Description                |
| ---------------------- | -------------------------- |
| `initiated`            | Submitted to the processor |
| `processing`           | Being processed            |
| `success`              | Completed successfully     |
| `failed`               | Failed                     |
| `cancelled`            | Cancelled                  |
| `expired`              | Expired before completion  |
| `reversed`             | Reversed after completion  |
| `requires_fulfillment` | Awaiting fulfilment action |

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/payouts

</details>

<details>

<summary>Can I route payouts through different providers?</summary>

Yes. Routing decisions can be based on payout amount, currency, destination country, and payout method type. If no rule matches, Hyperswitch uses the configured priority order as a fallback.

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/payouts\
https://docs.hyperswitch.io/explore-hyperswitch/workflows/intelligent-routing

</details>

## Business FAQs

<details>

<summary>What are the tradeoffs between open source and SaaS orchestration?</summary>

**Open source (self-hosted)**

| Factor               | Detail                                                       |
| -------------------- | ------------------------------------------------------------ |
| Infrastructure       | Managed entirely by the merchant                             |
| Data residency       | Full control over where data is stored                       |
| Customisation        | Full access to the codebase for modifications                |
| PCI DSS              | Merchant responsible for compliance                          |
| Operational overhead | High — requires DevOps, security, and platform engineering   |
| Cost                 | No licensing fee; infrastructure and operational costs apply |
| Upgrades             | Managed by the merchant                                      |

**SaaS (hosted)**

| Factor               | Detail                                           |
| -------------------- | ------------------------------------------------ |
| Infrastructure       | Managed by Juspay                                |
| Data residency       | Hosted in Juspay's cloud infrastructure          |
| Customisation        | Limited to configuration options                 |
| PCI DSS              | Managed by Juspay for hosted components          |
| Operational overhead | Low — Juspay manages infrastructure and upgrades |
| Cost                 | Subscription or usage-based pricing              |
| Upgrades             | Managed automatically by Juspay                  |

Documentation:\
https://docs.hyperswitch.io/hyperswitch-open-source/overview/unified-local-setup-using-docker\
https://docs.hyperswitch.io/deploy-hyperswitch-on-aws/deploy-hyperswitch

</details>

<details>

<summary>Is Hyperswitch suitable for startups or small businesses?</summary>

Yes. The **SaaS (hosted) deployment** provides the fastest path to accepting payments without requiring infrastructure management.

Key advantages:

- No infrastructure setup required
- Ready-to-use Control Centre environment
- Single integration to access multiple payment processors
- Modular architecture — integrate only the components you need

The open-source nature of Hyperswitch also means smaller teams can start with a self-hosted deployment at no licensing cost.

Documentation:\
https://docs.hyperswitch.io/about-hyperswitch/payment-suite

</details>

<details>

<summary>What types of businesses benefit most from Hyperswitch?</summary>

Hyperswitch is designed for digital businesses that process payments at scale or operate across multiple geographies, including e-commerce platforms, marketplaces, subscription businesses, enterprises seeking to reduce PSP dependency, and businesses expanding globally.

Documentation:\
https://docs.hyperswitch.io/about-hyperswitch/payment-suite

</details>

<details>

<summary>What are the key benefits of using Hyperswitch?</summary>

- **Single integration, multiple processors** — connect to multiple payment processors through a single API
- **Improved payment reliability** — smart retries and fallback routing reduce failed transactions
- **Improved authorisation rates** — intelligent routing directs transactions to the processor most likely to authorise them
- **Reduced vendor lock-in** — a unified token vault allows switching processors without re-collecting card details
- **Unified operations** — single Control Centre for all processors
- **Open-source and extensible** — full codebase available for customisation
- **Modular architecture** — adopt only the modules you need

Documentation:\
https://docs.hyperswitch.io/about-hyperswitch/payment-suite\
https://docs.hyperswitch.io/explore-hyperswitch/payments-modules

</details>

### Reduce Cost

<details>

<summary>How do I avoid overpaying due to blind retries?</summary>

Hyperswitch classifies decline codes into retryable and non-retryable categories. Non-retryable declines such as `fraudulent`, `stolen_card`, `expired_card`, and `do_not_honor` are not retried, preventing fee accumulation on transactions that cannot succeed. Retries are only initiated for soft declines where an alternative connector has a reasonable likelihood of succeeding.

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/workflows/smart-retries\
https://docs.hyperswitch.io/explore-hyperswitch/workflows/smart-retries/processor-error-code-mapping

</details>

### Improve Authorization Rate

<details>

<summary>How does orchestration improve authorization rates?</summary>

Hyperswitch improves authorisation rates through the Multi-Armed Bandit (MAB) routing model, smart retries including step-up retries with 3DS for fraud declines, and network tokenisation which provides issuers with additional transaction context that reduces false declines.

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/workflows/intelligent-routing/auth-rate-based-routing\
https://docs.hyperswitch.io/explore-hyperswitch/workflows/smart-retries\
https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/tokenization-and-saved-cards/network-tokenisation

</details>

<details>

<summary>Can I route transactions based on historical success rates?</summary>

Yes. The Multi-Armed Bandit (MAB) algorithm continuously evaluates authorisation rates per connector using a sliding window of recent transaction data, routes the majority of traffic to the highest-performing connector, and adapts dynamically as performance changes.

Navigate to **Workflow → Routing → Auth Rate Based Routing**.

Configuration parameters include `exploration_percent`, routing bucket size, and aggregation pipeline size.

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/workflows/intelligent-routing/auth-rate-based-routing

</details>

<details>

<summary>How does failover increase successful payments?</summary>

When a primary connector returns a retryable error, Hyperswitch automatically retries through the next available connector using the same payment session — the customer does not need to re-enter payment details.

Elimination routing proactively deprioritises connectors with elevated error rates so failover decisions are informed by real-time connector health data.

**Supported retry types**: Cascading retry (alternative processor) · Step-up retry (adds 3DS) · Network retry (alternative debit networks)

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/workflows/smart-retries\
https://docs.hyperswitch.io/explore-hyperswitch/workflows/intelligent-routing

</details>

<details>

<summary>Can I A/B test PSPs to improve approval rates?</summary>

Hyperswitch supports volume-based routing that allows merchants to distribute traffic across multiple connectors using percentage-based allocation, enabling controlled traffic splits to compare authorisation rates and performance between PSPs.

The MAB model also continuously runs a small exploration percentage of traffic across alternative connectors to measure their current performance.

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/workflows/intelligent-routing/rule-based-routing\
https://docs.hyperswitch.io/explore-hyperswitch/workflows/intelligent-routing/auth-rate-based-routing

</details>

### Extend Connectors

<details>

<summary>Can I experiment with new providers without rewriting my stack?</summary>

Yes. Because Hyperswitch normalises all connector APIs into a unified interface, adding a new connector does not require changes to your existing integration. New connectors can be added through the Control Centre and traffic directed to them using volume-based routing for evaluation. Routing allocation can be adjusted through the Control Centre without any code deployment.

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/connectors/activate-connector-on-hyperswitch\
https://docs.hyperswitch.io/explore-hyperswitch/workflows/intelligent-routing/rule-based-routing

</details>

### Observability

<details>

<summary>How do I get unified visibility across all my payment providers?</summary>

Because all payments flow through Hyperswitch, all payment data is captured and normalised in a single system — eliminating the need to log in to multiple PSP dashboards.

The Control Centre provides payment performance metrics, transaction-level search, refund and dispute tracking, and cost observability data across all connected processors.

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/account-management/analytics-and-operations

</details>

<details>

<summary>Can finance and product teams access the same data view?</summary>

Yes. Role-based access control allows different teams to access relevant payment data through the same Control Centre.

| Team             | Recommended role                | Access                                                 |
| ---------------- | ------------------------------- | ------------------------------------------------------ |
| Finance          | Merchant Operator or View Only  | Payment operations, reconciliation, cost observability |
| Product          | Merchant Developer or View Only | Analytics, conversion metrics, payment funnel          |
| Engineering      | Merchant Developer              | API key management, analytics, webhook configuration   |
| Customer Support | Customer Support                | Transaction-level search and payment details           |

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/account-management/manage-your-team\
https://docs.hyperswitch.io/explore-hyperswitch/account-management/analytics-and-operations

</details>

### Industry Specific

<details>

<summary>How does orchestration help subscription businesses?</summary>

Hyperswitch supports card-on-file flows and merchant-initiated transactions, connector-agnostic recurring payments that allow routing recurring charges through different processors without customer re-authentication, smart retries for failed subscription payments, and network token auto-updates that reduce involuntary churn when cards are replaced.

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/tokenization-and-saved-cards/pg-agnostic-recurring-payments\
https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/tokenization-and-saved-cards/network-tokenisation\
https://docs.hyperswitch.io/explore-hyperswitch/workflows/smart-retries

</details>

<details>

<summary>How does Hyperswitch work for cross-border commerce?</summary>

Hyperswitch supports payment acceptance across multiple regions, currencies, and payment methods including cards, bank redirects (iDEAL, Giropay, EPS), wallets (Apple Pay in 75+ countries, Google Pay in 70+ countries, PayPal), and bank transfers (ACH, SEPA, BACS, BECS).

Routing rules can be configured based on customer country and currency. Hyperswitch supports 3DS 2.x and PSD2 SCA requirements for European transactions.

Full list of supported payment methods: https://juspay.io/integrations

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/payment-orchestration/quickstart/payment-methods-setup\
https://docs.hyperswitch.io/explore-hyperswitch/workflows/3ds-decision-manager

</details>

<details>

<summary>Can Hyperswitch handle high-volume flash sale traffic?</summary>

Juspay (Parent company of Hyperswitch) processes over **300 million daily transactions**. The routing layer adds approximately **25ms** of overhead per transaction. The Lite SDK variant provides faster initialisation with an artifact size under 300 KB.

For self-hosted deployments, Kubernetes-based deployments support horizontal pod autoscaling, stateless application instances behind a load balancer, and Redis for distributed caching.

Documentation:\
https://docs.hyperswitch.io/check-list-for-production/going-live/for-on-prem-setup/monitoring\
https://docs.hyperswitch.io/learn-more/hyperswitch-architecture

</details>

### Compliance

<details>

<summary>Where is payment data stored and controlled?</summary>

**SaaS deployment**

Payment data is hosted and managed by Juspay within Juspay's cloud infrastructure. Juspay maintains PCI DSS compliance for the hosted environment.

**Self-hosted deployment**

Payment data resides entirely within the merchant's own infrastructure. The merchant controls storage location, access, encryption, retention, and regional data residency compliance.

**Vault and card data**

Sensitive card data is stored in a PCI-compliant vault. For self-hosted deployments, merchants can use Hyperswitch's native vault, bring their own PCI-compliant vault provider, or configure a hybrid vault architecture.

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/security-and-compliance/security\
https://docs.hyperswitch.io/explore-hyperswitch/workflows/vault/self-hosted-orchestration-with-outsourced-pci-vault

</details>

<details>

<summary>Does orchestration increase compliance complexity?</summary>

Using Hyperswitch's hosted SDK and vault reduces the merchant's PCI DSS scope by ensuring sensitive card data does not pass through merchant infrastructure.

For SaaS deployments, Juspay maintains PCI DSS compliance for the hosted components. For self-hosted deployments, the merchant is responsible for compliance across their infrastructure.

Hyperswitch handles 3DS authentication and PSD2 SCA compliance through the 3DS Decision Manager.

Documentation:\
https://docs.hyperswitch.io/explore-hyperswitch/security-and-compliance/security\
https://docs.hyperswitch.io/explore-hyperswitch/workflows/3ds-decision-manager

</details>
