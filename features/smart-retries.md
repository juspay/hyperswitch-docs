---
description: Automatically retry failed payments with an alternative processor to improve authorization rates
---

# Smart Retries

{% hint style="info" %}
This section covers how smart retries function, the supported payment processors, and how to enable it.
{% endhint %}

Smart retry is a Hyperswitch feature to improve the payment success rates in a multi-processor setup. If the payment fails through the primary processor due to specific reasons, the payment will be retried with an alternative payment processor to increase the chances of making the payment successful.

There are two possible types of payment retry flows:

**Smart Retries:** These retries are applicable where a user action is not required (after entering the card information) to complete a payment. Below are some example scenarios:

* Scenario 1: If the payment is a non-3DS card transaction and the payment is declined by the primary processor due to technical or business failures, it will be retried.
* Scenario 2: If the payment is a 3DS card transaction and the payment is declined by the primary processor due to a technical failure, the payment will be retried.
* Scenario 3: If the payment is a 3DS card transaction and the payment is declined by the primary processor due to a business failure, the payment will not be retried.

**User Consent-based Retries:** These retries are applicable for payment flows that need an additional level of user authentication (example: Apple Pay, Google Pay, 3DS cards, bank transfers). Such payment flows need an additional authentication from the user. Hence smart retries are not possible for such scenarios.

**Note:** Currently, Hyperswitch supports Smart retries as an out-of-the-box capability. In order to enable user consent based retry for payment failures, you can create a fresh payment and re-trigger the Hyperswitch checkout.

## Supported Payment Processors

Hyperswitch supports the following primary processors for automatic retries.

* Stripe
* Bluesnap
* Checkout.com
* Trustpay

In case you wish more primary processors to be covered for automatic retry, please submit a feature request [here](https://github.com/juspay/hyperswitch/discussions/new?category=ideas-feature-requests).

## How Does It Work?

Smart retry will be attempted whenever the payment fails through the primary processor for card transactions.

Primary processor is the first choice of payment processor for the particular transaction. This is evaluated based on the smart routing rules configured in the Hyperswitch dashboard's routing module.

The flow looks like below.

<figure><img src="../.gitbook/assets/smartRetry-arch.png" alt=""><figcaption></figcaption></figure>

## How to Enable Smart Retries?

**Step 1:** Ensure that you have enabled the pecking order of payment processors on the Hyperswitch dashboard. You can access the settings from Routing > Default fallback > Manage.

<figure><img src="../.gitbook/assets/smartretry-1 (2).png" alt=""><figcaption></figcaption></figure>

**Step 2:** Drop a request to biz@hyperswitch.io with the below information.

* Confirmation to enable automatic retry
* Maximum number of payment retry attempts (It is recommended to start with 1 retry attempt. However we can support more retry attempts based on the number of processors)

## FAQs

### What is a Primary Processor?

Primary processor is the first choice of processor for the particular transaction to be processed. This is evaluated based on the smart routing rules configured in the Hyperswitch dashboard's routing module.

### Why Can I Not Enable Automatic Retry from the Hyperswitch Dashboard?

For reconciliation purposes, some merchants prefer having the same payment ID being passed to both Hyperswitch and the payment processors. Smart retry would not be feasible if such a use case exists. Hence, Smart retry is an additional configuration that can be enabled only by contacting our support (hyperswitch@juspay.in).

Since Smart retry involves multiple payment attempts for a single payment ID, Hyperswitch appends the attempt number to the payment ID that the merchant sends to Hyperswitch before passing it on to the processors.

For example, if the merchant had sent `pay_abcd145efg`, then Hyperswitch will send the following payment ID to the processors during each attempt:

* Payment attempt 1: `pay_abcd145efg_1`
* Payment attempt 2: `pay_abcd145efg_2`
* Payment attempt 3: `pay_abcd145efg_3`

### What Will the User Experience Look Like During Smart Retry?

The user experience will not be different from a regular checkout experience, since all retry attempts will happen silently in the background. However, there is a possibility of the user receiving multiple payment attempt notifications or SMS from the card issuing bank due to the card payment being attempted for more than once.

### What is the Difference Between Fallback and Smart Retry?

Fallback is a pecking order of all the configured processors which is used to route traffic standalone or when other smart routing rules are not applicable for the particular transaction. You can reorder the list with simple drag and drop from the Routing > Default fallback > Manage section in the dashboard.

Smart retry is a feature to improve the chances of success of a payment by silently retrying with an alternative processor.
