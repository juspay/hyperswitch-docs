---
icon: person-walking-arrow-loop-left
---

# Manual/User triggere Retries

### Feature Overview

The Manual or User triggered Retries feature in Hyperswitch allows customers to retry a failed payment attempt under the same Payment Intent, without needing to restart the entire checkout flow.

This capability helps merchants recover from transient payment failures — such as card declines or temporary PSP issues — and significantly improves authorization success rates and customer experience.

Once enabled, Hyperswitch automatically determines if a failed payment is eligible for retry through a new response field: `manual_retry_allowed`.

### Configuring Manual Retries

1. Log in to your Hyperswitch Dashboard.
2. Navigate to Developers → Payment Settings → Manual Retries.
3. Toggle the setting ON to enable Manual Retries for your profile.

Once enabled, the `manual_retry_allowed` field will be included in payment responses whenever a payment attempt fails.

### Integration Behavior

#### Case 1: Frictionless Flows (No Redirection)

For payments without redirection (e.g., standard card transactions, wallet flows):

* The Hyperswitch SDK automatically handles retries when `manual_retry_allowed` is true.
* Merchants need not make any code changes.
* The SDK automatically invokes the retry flow under the same payment\_id.
* Customers can update their card or payment details directly in the checkout UI and reattempt payment — all within the same session.

**Example Flow:**

1. Customer enters card details → clicks Pay Now.
2. SDK triggers /payments/confirm internally.
3. Payment fails.
4. SDK detects `manual_retry_allowed : true` and displays retry UI.
5. Customer re-enters updated payment details → retry succeeds.

#### Case 2: Redirect Flows (e.g., 3DS / SCA)

For payment flows that involve redirection (like 3-D Secure authentication):

* After the customer completes redirection and returns to your site, your frontend regains control.
* If the payment fails and `manual_retry_allowed : true`, you should remount the Hyperswitch SDK using the same client\_secret corresponding to that Payment Intent.
* This allows the customer to retry within the same checkout context.

#### SDK Integration sample logic:

```javascript
// Manual Retry: determine whether to reuse the existing client secret
if (manualRetryAllowed && existingClientSecret) {
  // Reuse the existing client secret for retry
  // No need to create a new payment intent
  paymentIntentData = { clientSecret: existingClientSecret };
} else {
  // Fallback: request a new payment intent from the backend
  paymentIntentData = await fetchNewPaymentIntent();
}

```

**Behavior**:

* The SDK is re-initialized on the same Payment Intent.
* The customer can retry payment by entering updated details.
* The SDK then performs /payments/confirm again under the same payment\_id.\


### API Workflow

#### 1️⃣ Create a Payment Intent

Create a Payment Intent before initiating checkout.

```json
{
  "amount": 1000,
  "currency": "EUR",
  "confirm": false,
  "capture_method": "automatic",
  "capture_on": "2022-09-10T10:11:12Z",
  "customer_id": "{{customer_id}}",
  "email": "guest@example.com",
  "name": "John Doe",
  "authentication_type": "three_ds",
  "return_url": "https://hyperswitch.io",
  "billing": {
    "address": {
      "city": "Vienna",
      "country": "AT",
      "line1": "123 Test Street",
      "zip": "560095"
    }
  },
  "setup_future_usage": "on_session"
}

```

#### 2️⃣ Confirm the Payment (Triggered by Checkout SDK)

When the customer enters card details and clicks Pay Now, the Hyperswitch SDK automatically makes a /payments/confirm call.

```json
{
  "payment_method": "card",
  "payment_method_data": {
    "card": {
      "card_number": "4242424242424242",
      "card_exp_month": "02",
      "card_exp_year": "2026",
      "card_holder_name": "John Doe",
      "card_cvc": "999"
    }
  },
  "connector": ["cybersource"],
  "client_secret": "{{client_secret}}"
}

```

If this payment fails, the response will include:

`manual_retry_allowed : true`

#### 3️⃣ Retry the Payment (If Allowed)

If `manual_retry_allowed :  true` , you can retry on the same Payment Intent.\


* For redirect flows, this can be done by remounting the SDK as described earlier.
* For SDK-managed (non-redirect) flows, Hyperswitch automatically handles this internally.

**Example Retry Request (for redirect flows):**

```json
{
  "payment_method": "card",
  "payment_method_data": {
    "card": {
      "card_number": "4000000000000002",
      "card_exp_month": "03",
      "card_exp_year": "2028",
      "card_holder_name": "Jane Doe",
      "card_cvc": "123"
    }
  },
  "connector": ["cybersource"],
  "client_secret": "{{client_secret}}"
}

```

### Response Field Reference

**Field:** `manual_retry_allowed`\
**Type:** Boolean / null

Specifies whether manual retry is supported for a failed payment.

| Value   | Description                                            |
| ------- | ------------------------------------------------------ |
| `true`  | Manual retry is allowed on the same Payment Intent.    |
| `false` | Manual retry is not allowed.                           |
| `null`  | Manual retry is not enabled for this merchant profile. |

### Customer Journey Example

**Frictionless Flow**

1. Customer fills card details → clicks Pay Now
2. /payments/confirm triggered by SDK
3. Payment fails → SDK detects manual\_retry\_allowed = true
4. Retry prompt shown → customer retries within same checkout
5. Payment succeeds

**Redirect Flow (e.g., 3DS)**

1. Customer completes 3DS authentication → redirected back to merchant
2. Payment fails → manual\_retry\_allowed = true in response
3. Merchant frontend remounts Hyperswitch SDK with the same client\_secret
4. Customer retries payment → payment succeeds

### Support

For any questions, PSP enablement requests, or integration issues related to Manual Retries,  please reach out to the Hyperswitch Support Team.

\
