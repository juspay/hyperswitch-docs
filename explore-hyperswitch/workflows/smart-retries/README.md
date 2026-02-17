---
description: Automatically retry payments with an alternative processor
icon: magnifying-glass-arrows-rotate
---

# Smart Retries

Smart retry is a Hyperswitch feature to improve the payment success rates in a single or multi-processor setup. If the payment fails through the primary processor due to specific reasons, the payment will be retried with the same or an alternative payment processor to increase the chances of making the payment successful.

The Auto Retry engine handles varied Retry strategy based on the type of error encountered such as:

1. **Cascading Retry** - Re-attempting an authorization request to an alternate processor with the same or enhanced payload
2. **Step-Up Retry -** Re-attempting an authorization request to the same/different processors with additional authentication data (frictionless and challenge flows)
3. **Clear PAN Retry -** Re-attempting a tokenised authorization request with a Clear PAN in case of de-tokenisation failures
4. **Global Network Retry -** Re-attempting an authorization request with a signature network in case of debit network failure

Hyperswitch’s error handling engine is enriched with mappings for error codes and error messages across 100+ processors, acquirers, issuers. Processors have anywhere between 400 to 1,000 and at times more error codes. The database contains these combinations of error code and error messages for every processor and is constantly refreshed with newer codes that are encountered.

<figure><img src="../../../.gitbook/assets/unknown (3).png" alt=""><figcaption></figcaption></figure>

### Error code segregation

1. For each PSP all the published + encountered error codes are segregated in two categories “Retriable” and “Non-retriable”
2. This is a dynamic list and continue to grow for each PSP as they change their error mapping or introduce new errors
3. We’re also implementing a feedback loop from “Non-retriable” errors to “Retriable” errors basis retry exploration _(bottom branch on the image above)_  &#x20;

Each of the error codes are mapped individually as to whether they are eligible for the various retry capabilities.&#x20;

| <h4><strong>Category</strong></h4> | <h4><strong>Example codes from a PSP</strong></h4>                                                   |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Cascading retry                    | Refused, System malfunction, Processing temporarily unavailable                                      |
| Step-up retry                      | 3D Secure required, Strong customer authentication required, Suspected Fraud                         |
| Clear PAN retry                    | Invalid cryptogram, Network token not supported, Payment token expired                               |
| Network retry                      | Transaction not permitted on this network, Invalid card for selected network, Function not supported |

### Merchant config enablement&#x20;

1. Merchant needs to be enabled across the required flows
2. Merchant can be eligible to all 4 or some of retry flows - **Cascading Retry, Step-Up Retry, Clear PAN Retry, Global Network Retry**&#x20;
3. Merchant needs to specify N = Number of retries permitted

### Retry Decision Flow&#x20;

1. Payment fails → GSM lookup determines retry eligibility retry
2. Check retry flags:
   1. _step\_up\_possible_ → Attempt 3DS if no 3DS was used
   2. _clear\_pan\_possible_ → Retry with PAN for network tokens
   3. _alternate\_network\_possible_ → Try different debit network
3. Execute _retry via do\_retry()_ function retry with SAME or ENHANCED payload
4. Exhaustion handling → Stop when retries/connectors depleted retry

### How it all comes together

#### Use Case 1

| <h4>Attempt</h4> | <h4>PSP</h4> | <h4>Flow</h4>                                 | <h4>Outcome</h4> |
| ---------------- | ------------ | --------------------------------------------- | ---------------- |
| 1                | PSP1         | Original payload (non-3ds)                    | Suspected fraud  |
| 2                | PSP1         | Step up - Independent 3DS (frictionless flow) | Generic decline  |
| 3                | PSP2         | Original payload + Authentication data        | Succesful        |

#### Use case 2

| <h4>Attempt</h4> | <h4>PSP</h4> | <h4>Flow</h4>                              | <h4>Outcome</h4> |
| ---------------- | ------------ | ------------------------------------------ | ---------------- |
| 1                | PSP1         | Original payload (non-3ds)                 | Suspected fraud  |
| 2                | PSP1         | Step up - Independent 3DS (challenge flow) | Generic decline  |
| 3                | PSP2         | Original payload + Authentication data     | Succesful        |

### Use case 3

| <h4>Attempt</h4> | <h4>PSP</h4> | <h4>Flow</h4>              | <h4>Outcome</h4> |
| ---------------- | ------------ | -------------------------- | ---------------- |
| 1                | PSP1         | Original payload (non-3ds) | Generic decline  |
| 2                | PSP2         | Original payload (non-3ds) | Succesful        |

### Use case 4

| <h4>Attempt</h4> | <h4>PSP</h4> | <h4>Flow</h4>                                                                                             | <h4>Outcome</h4> |
| ---------------- | ------------ | --------------------------------------------------------------------------------------------------------- | ---------------- |
| 1                | PSP1         | <p>Original payload (non-3ds)<br><br>Limited data fields on customer info, device/IP, product details</p> | Generic decline  |
| 2                | PSP2         | Additional payload (non-3ds)                                                                              | Succesful        |

### Use case 5

| <h4>Attempt</h4> | <h4>PSP</h4> | <h4>Flow</h4>                        | <h4>Outcome</h4> |
| ---------------- | ------------ | ------------------------------------ | ---------------- |
| 1                | PSP1         | Original payload (Network token PAN) | Do not honor     |
| 2                | PSP1         | Original payload (Clear PAN)         | Generic decline  |
| 3                | PSP2         | Original payload (Clear PAN)         | Succesful        |

**User Consent-based Retries:** These retries are applicable for payment flows that need an additional level of user authentication (example: Apple Pay, Google Pay, 3DS cards, bank transfers). Such payment flows need an additional authentication from the user. Hence smart retries are not possible for such scenarios.



### Gateway error code mapping

Smart Retry is an intelligent optimization engine designed to maximize transaction success rates. By leveraging an advanced AI model, we analyze error codes returned from payment processors to determine the root cause of a failure.

Upon receiving an error from a processor, the system classifies the transaction into one of two primary categories: Non-Retryable , Retryable. If an error is deemed Retryable, the AI dynamically selects the optimal retry strategy from the following categories:





## How to enable Smart Retries?

**Step 1:** Ensure that you have enabled the pecking order of payment processors on the Hyperswitch dashboard. You can access the settings from Routing > Default fallback > Manage.

**Step 2:** Drop a request to hyperswitch@juspay.in with the below information.

* Confirmation on the retry flows to be enaled&#x20;
* Maximum number of payment retry attempts&#x20;

## FAQs

### What is a primary processor?

Primary processor is the first choice of processor for the particular transaction to be processed. This is evaluated based on the smart routing rules configured in the Hyperswitch dashboard’s routing module.

### Why can I not enable Automatic Retry from the Hyperswitch dashboard?

For reconciliation purposes, some merchants prefer having the same payment\_id being passed to both Hyperswitch and the Payment Processors. Smart retry would not be feasible if such a use case exists. Hence, Smart retry is as an additional configuration that can be enabled only by contacting our support (hyperswitch@juspay.in).

Since Smart retry involves multiple payment attempts for a single payment\_id, Hyperswitch appends the attempt number to the payment\_id that the merchant sends to Hyperswitch before passing it on to the processors.

For example, if the merchant had sent pay\_abcd145efg, then Hyperswitch will send the following payment\_id to the processors during each attempt:

* Payment attempt 1: pay\_abcd145efg\_1
* Payment attempt 2: pay\_abcd145efg\_2
* Payment attempt 3: pay\_abcd145efg\_3

### What will the user experience look like during Smart Retry?

The user experience will not be different from a regular checkout experience, since all retry attempts will happen silently in the background. However, there is a possibility of the user receiving multiple payment attempt notifications / sms from the card issuing bank due to the card payment being attempted for more than once.

### What is the difference between fallback and smart retry?

Fallback is a pecking order of all the configured processors which is used to route traffic standalone or when other smart routing rules are not applicable for the particular transaction. You can reorder the list with simple drag and drop from the Routing > Default fallback > Manage section in the dashboard.

Smart retry is a feature to improve the chances of success of a payment by silently retrying with an alternative processor.
