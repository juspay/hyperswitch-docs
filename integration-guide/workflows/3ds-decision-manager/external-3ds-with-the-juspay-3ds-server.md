<!-- truth manifest; hyperswitch cfbeb2bedf523da301d7d7b0a8dcbeaf2263c696; spec api-reference/v1/openapi_spec_v1.json@cfbeb2bedf523da301d7d7b0a8dcbeaf2263c696
     symbols: POST /account/{account_id}/business_profile/{profile_id} = crates/openapi/src/routes/profile.rs:40-70
     symbols: POST /account/{merchant_id}/connectors = crates/router/src/routes/app.rs:2183-2185
     symbols: POST /account/{merchant_id}/connectors/{merchant_connector_id} = crates/router/src/routes/app.rs:2188-2191
     symbols: juspaythreedsserver connector_auth NoKey = crates/connector_configs/toml/sandbox.toml:7048; crates/router/src/core/connector_validation.rs:378
     symbols: POST /payments = crates/router/src/routes/app.rs:1039-1043; crates/openapi/src/routes/payments.rs:1-8,650-655
     symbols: GET /payments/{payment_id}; force_sync; client_secret = crates/router/src/routes/app.rs:1052-1055; crates/openapi/src/routes/payments.rs:657-685
     symbols: POST or GET /payments/{payment_id}/{merchant_id}/authorize/{connector} = crates/router/src/routes/app.rs:1129-1133
     symbols: POST /payments/{payment_id}/3ds/authentication = crates/router/src/routes/app.rs:1135; crates/openapi/src/routes/payments.rs:1210-1224
     symbols: GET /poll/status/{poll_id} = crates/router/src/routes/app.rs:2440-2449; crates/openapi/src/routes/poll.rs:1-15
     symbols: request_external_three_ds_authentication = api-reference/v1/openapi_spec_v1.json:34256-34262
     symbols: browser_info = crates/api_models/src/payments.rs:1387-1400; crates/hyperswitch_connectors/src/connectors/unified_authentication_service/transformers.rs:977-997
     symbols: authentication_connector_details = crates/api_models/src/admin.rs:377-386
     symbols: NextActionData::ThreeDsInvoke = crates/api_models/src/payments.rs:6900-6903,6995-6999
     symbols: ThreeDsData = crates/api_models/src/payments.rs:7061-7087
     symbols: PollConfigResponse = crates/api_models/src/payments.rs:7129-7138
     symbols: PaymentsExternalAuthenticationRequest = crates/api_models/src/payments.rs:12175-12188
     symbols: ThreeDsCompletionIndicator = Y,N,U (3 values) = crates/api_models/src/payments.rs:12278-12291
     symbols: DeviceChannel = APP,BRW (2 values) = crates/api_models/src/payments.rs:12293-12313
     symbols: PaymentsExternalAuthenticationResponse = crates/api_models/src/payments.rs:12442-12467
     symbols: TransactionStatus = Y,N,U,A,R,C,D,I (8 values) = crates/common_enums/src/enums.rs:9633-9659
     symbols: PollResponse and PollStatus = pending,completed,not_found (3 values) = crates/api_models/src/poll.rs:5-20
     symbols: poll_status postMessage string fields = crates/router/src/core/utils.rs:2520-2566
     symbols: openurl_if_required postMessage = crates/router/src/core/utils.rs:2568-2597
     checked: 2026-10-01 -->

# External 3DS with the Juspay 3DS Server

Use this flow when the Juspay 3DS Server authenticates the cardholder and a separate payment processor authorizes the payment. Your backend creates and confirms the payment. Your browser then performs device fingerprinting, starts authentication, presents any challenge, and retrieves the final payment status.

This page owns the complete browser walkthrough for the Juspay 3DS Server. It covers both browser models:

* **Embedded iframe:** the challenge stays on your checkout page. You listen for `postMessage` events and poll a lightweight status endpoint to determine the authentication status.
* **Full-page redirect:** the browser navigates to the ACS and returns to your `return_url`. This is simpler to implement, but it does not provide an embedded experience.

The two models share the same setup, payment, fingerprinting, and authentication calls. They differ only in the target used for the final forms and how your application receives completion.

For the provider-neutral explanation, see [Standalone 3D Secure](external-authentication-for-3ds.md). Mobile 3DS is outside this browser walkthrough.

## How the integration works

A payment is created and confirmed on Hyperswitch. When external 3DS is requested, Hyperswitch uses Juspay as the authentication connector and returns a `three_ds_invoke` next action. Your frontend then completes device fingerprinting, calls the authentication endpoint, handles either a challenge or frictionless outcome, and retrieves the payment status.

1. Create and confirm a payment in Hyperswitch.
2. Receive `three_ds_invoke`.
3. Run device fingerprinting when required.
4. Call the 3DS authentication endpoint.
5. Handle challenge or frictionless authentication.
6. Finalize authorization and retrieve the payment status.

## Before you start

Keep a secret API key on your backend and a publishable key in the browser. Never expose the secret API key in browser code.

Complete the four setup steps below in order. They enable the feature, add the 3DS metadata to your payment connector, register the Juspay 3DS Server, and point the Business Profile at it.

### Step 1: Enable External 3DS for your account

Contact Hyperswitch Support to enable External 3DS. It can be enabled at either level:

* **Organization ID:** External 3DS is enabled for the organization, and every Merchant ID under it is enabled by default.
* **Merchant ID:** External 3DS is enabled only for the specified Merchant ID.

### Step 2: Add External 3DS metadata to the payment connector

The Merchant Connector Account for the payment processor needs additional metadata for the External 3DS flow. If the connector already exists, update it rather than creating a second one.

The example below updates a Nuvei connector.

```bash
curl --request POST \
  --url 'https://sandbox.hyperswitch.io/account/<merchant id>/connectors/<mca id>' \
  --header 'Content-Type: application/json' \
  --header 'api-key: <secret api key>' \
  --data '{
    "connector_type": "payment_processor",
    "metadata": {
      "merchant_category_code": "5411",
      "merchant_country_code": "840",
      "merchant_name": "Dummy Merchant",
      "acquirer_bin": "444444",
      "endpoint_prefix": "test",
      "acquirer_merchant_id": "JuspayTest1",
      "acquirer_country_code": "356"
    }
  }'
```

Dashboard support for these fields is planned, so that they can be set while creating or updating the connector.

### Step 3: Register the Juspay 3DS Server

Add the Juspay 3DS Server as an authentication connector. This is what lets Hyperswitch use it for External 3DS.

```bash
curl --request POST \
  --url 'https://sandbox.hyperswitch.io/account/<merchant id>/connectors' \
  --header 'Content-Type: application/json' \
  --header 'Accept: application/json' \
  --header 'api-key: <secret api key>' \
  --data '{
    "connector_type": "authentication_processor",
    "connector_name": "juspaythreedsserver",
    "connector_label": "test",
    "profile_id": "<profile id>",
    "connector_account_details": {
      "auth_type": "NoKey"
    },
    "test_mode": true,
    "disabled": false,
    "metadata": {
      "merchant_category_code": "5411",
      "merchant_country_code": "840",
      "merchant_name": "Dummy Merchant",
      "endpoint_prefix": "",
      "three_ds_requestor_name": "hyperswitch_sbx",
      "three_ds_requestor_id": "hyperswitch_sbx",
      "pull_mechanism_for_external_3ds_enabled": true
    }
  }'
```

`auth_type` is `NoKey`: the connector configuration declares no credential fields for the Juspay 3DS Server, so the activation call carries metadata only. See the [Juspay 3DS Server connector page](../../../integration-space/connectors-integrations/3ds-providers/juspaythreedsserver.md).

### Step 4: Enable 3DS authentication on the Business Profile

Point the profile at the Juspay 3DS Server. `authentication_connector_details` carries the ordered authentication connector list and the 3DS requestor URL.

```bash
curl --request POST \
  --url 'https://sandbox.hyperswitch.io/account/<merchant id>/business_profile/<profile id>' \
  --header 'Content-Type: application/json' \
  --header 'api-key: <secret api key>' \
  --data '{
    "authentication_connector_details": {
      "authentication_connectors": ["juspaythreedsserver"],
      "three_ds_requestor_url": "https://<your domain>"
    },
    "merchant_country_code": "004",
    "merchant_category_code": "5411"
  }'
```

## 1. Create and confirm the payment

Set `request_external_three_ds_authentication` to `true`, use `authentication_type: "three_ds"`, and provide a `return_url`.

Send `browser_info`. It is reused later for the authentication step in step 4, which does not accept browser data of its own. The v1 schema allows `browser_info` to be omitted, and the authentication transformer then supplies an empty browser object, so send the real browser values for a browser transaction rather than relying on that fallback.

```bash
curl --request POST \
  --url 'https://sandbox.hyperswitch.io/payments' \
  --header 'Content-Type: application/json' \
  --header 'api-key: <secret api key>' \
  --data '{
    "amount": 15100,
    "currency": "USD",
    "confirm": true,
    "capture_method": "automatic",
    "profile_id": "<profile id>",
    "customer_id": "TestCustomer",
    "email": "test@example.com",
    "name": "John Doe",
    "phone": "999999999",
    "phone_country_code": "+1",
    "description": "External 3DS test payment",
    "authentication_type": "three_ds",
    "return_url": "https://<your domain>/payments/return",
    "request_external_three_ds_authentication": true,
    "payment_method": "card",
    "payment_method_type": "debit",
    "browser_info": {
      "accept_header": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
      "ip_address": "203.0.113.10",
      "java_enabled": false,
      "java_script_enabled": true,
      "language": "en-US",
      "color_depth": 24,
      "screen_height": 1080,
      "screen_width": 1920,
      "time_zone": 330,
      "user_agent": "<browser user agent>"
    },
    "payment_method_data": {
      "card": {
        "card_number": "5204730541001215",
        "card_exp_month": "07",
        "card_exp_year": "31",
        "card_holder_name": "CL-BRW2",
        "card_cvc": "123"
      }
    },
    "billing": {
      "address": {
        "line1": "1467 Harrison Street",
        "city": "San Francisco",
        "state": "CA",
        "zip": "94122",
        "country": "US",
        "first_name": "John",
        "last_name": "Doe"
      }
    }
  }'
```

A payment that needs this flow returns `next_action.type` as `three_ds_invoke`.

## 2. Read `three_ds_invoke`

The response shape is a tagged `next_action` object. `poll_config.delay_in_secs` and `poll_config.frequency` are integers here.

```json
{
  "next_action": {
    "type": "three_ds_invoke",
    "three_ds_data": {
      "three_ds_authentication_url": "https://<hyperswitch host>/payments/<payment id>/3ds/authentication",
      "three_ds_authorize_url": "https://<hyperswitch host>/payments/<payment id>/<merchant id>/authorize/<payment connector>",
      "three_ds_method_details": {
        "three_ds_method_data_submission": true,
        "three_ds_method_data": "<encoded 3DS method data>",
        "three_ds_method_url": "https://<acs host>/<3ds method path>",
        "three_ds_method_key": "threeDSMethodData",
        "consume_post_message_for_three_ds_method_completion": false
      },
      "poll_config": {
        "poll_id": "external_authentication_<payment id>",
        "delay_in_secs": 2,
        "frequency": 5
      },
      "message_version": "2.2.0",
      "directory_server_id": "<directory server id>",
      "card_network": "<card network>",
      "three_ds_connector": "juspaythreedsserver"
    }
  }
}
```

| Field | Use |
| --- | --- |
| `three_ds_method_details.three_ds_method_data_submission` | Whether device fingerprinting in step 3 is required. |
| `three_ds_method_url`, `three_ds_method_data`, `three_ds_method_key` | Inputs for the fingerprinting POST. For the Juspay 3DS Server, `three_ds_method_key` is always `threeDSMethodData`. |
| `three_ds_method_details.consume_post_message_for_three_ds_method_completion` | For the Juspay 3DS Server this is always `false`. |
| `three_ds_authentication_url` | Endpoint for the authentication call in step 4. |
| `three_ds_authorize_url` | Endpoint to post the challenge or non-challenge result to in step 5. |
| `poll_config` | Poll id, delay and maximum attempts for the lightweight status poll. Used only in the embedded iframe model. |
| `message_version`, `directory_server_id`, `card_network`, `three_ds_connector` | Context returned for the selected 3DS path. |

## 3. Perform device fingerprinting

Check `three_ds_method_data_submission` before creating the form.

* If it is `false`, skip the form and send `threeds_method_comp_ind: "U"` in step 4.
* If it is `true`, submit the method data in a hidden iframe. Send `"Y"` when your method completion handling succeeds. Send `"N"` when it fails.

`threeds_method_comp_ind` has exactly three wire values:

| Value | Meaning |
| --- | --- |
| `Y` | The 3DS method completed. |
| `N` | The 3DS method did not complete successfully. |
| `U` | The 3DS method URL was unavailable or no submission was requested. |

```html
<iframe name="threeDSMethodFrame" hidden></iframe>
<form
  id="threeDSMethodForm"
  method="POST"
  action="<three ds method url>"
  target="threeDSMethodFrame"
>
  <input
    type="hidden"
    name="<three ds method key>"
    value="<encoded three ds method data>"
  />
</form>
<script>
  document.getElementById("threeDSMethodForm").submit();
</script>
```

The hidden iframe is required in both browser models. Fingerprinting must run invisibly in the background without navigating your page away.

**Detecting completion.** Watch for the hidden iframe navigating away from `about:blank`. Cross-origin access to the iframe throws a `SecurityError`, which you can treat as completion. Apply a timeout of about 15 seconds as a fallback, and send `"N"` if it expires.

## 4. Start 3DS authentication

Call `POST /payments/{payment_id}/3ds/authentication` with the publishable key. When the request does not use an SDK Authorization header, `client_secret` is required. Browser requests use `device_channel: "BRW"`.

Do not send `browser_info` to this endpoint. Its request object has four fields: `client_secret`, `sdk_information`, `device_channel`, and `threeds_method_comp_ind`. The browser information comes from the payment created in step 1.

```bash
curl --request POST \
  --url 'https://sandbox.hyperswitch.io/payments/<payment id>/3ds/authentication' \
  --header 'Content-Type: application/json' \
  --header 'api-key: <publishable key>' \
  --data '{
    "client_secret": "<payment client secret>",
    "device_channel": "BRW",
    "threeds_method_comp_ind": "Y"
  }'
```

The response carries `trans_status` and, when needed, ACS challenge fields.

```json
{
  "trans_status": "C",
  "acs_url": "https://<acs host>/<challenge path>",
  "challenge_request": "<encoded challenge request>",
  "challenge_request_key": "creq",
  "acs_reference_number": "<acs reference number>",
  "acs_trans_id": "<acs transaction id>",
  "three_dsserver_trans_id": "<3ds server transaction id>",
  "three_ds_requestor_url": "https://<your domain>"
}
```

`trans_status` has eight wire values. The list below contains all eight values declared by the API enum.

| Value | Meaning |
| --- | --- |
| `Y` | Authentication or account verification succeeded. |
| `N` | Authentication failed or the transaction was denied. |
| `U` | Authentication could not be performed. |
| `A` | An authentication attempt was recorded, but the cardholder was not verified. |
| `R` | The issuer rejected authentication and requests that authorization not be attempted. |
| `C` | A challenge is required. |
| `D` | Decoupled authentication is pending. |
| `I` | Informational response only. |

Only `C` uses the ACS challenge form in this browser walkthrough. Do not treat every non-`C` value as success. Continue to the authorize URL so Hyperswitch can finalize the payment, then use the final payment status as the result.

## 5. Submit the challenge or non-challenge result

The payload is the same for both integration models. Only the form target changes.

### Challenge response when `trans_status` is `C`

Submit `challenge_request` to `acs_url`. Name the field with `challenge_request_key`.

**Embedded iframe**

```html
<iframe name="threeDSChallengeFrame" title="3DS challenge"></iframe>
<form
  id="threeDSChallengeForm"
  method="POST"
  action="<acs url>"
  target="threeDSChallengeFrame"
>
  <input
    type="hidden"
    name="<challenge request key>"
    value="<encoded challenge request>"
  />
</form>
<script>
  document.getElementById("threeDSChallengeForm").submit();
</script>
```

**Full-page redirect**

```html
<form id="threeDSChallengeForm" method="POST" action="<acs url>">
  <input
    type="hidden"
    name="<challenge request key>"
    value="<encoded challenge request>"
  />
</form>
<script>
  document.getElementById("threeDSChallengeForm").submit();
</script>
```

The ACS renders the challenge page, for example an OTP prompt. On completion it posts the result to `three_ds_authorize_url`, which returns the script that finalizes the flow.

### Non-challenge response

Submit an empty form to `three_ds_authorize_url`.

**Embedded iframe**

```html
<form
  id="threeDSAuthorizeForm"
  method="POST"
  action="<three ds authorize url>"
  target="threeDSChallengeFrame"
></form>
<script>
  document.getElementById("threeDSAuthorizeForm").submit();
</script>
```

**Full-page redirect**

```html
<form
  id="threeDSAuthorizeForm"
  method="POST"
  action="<three ds authorize url>"
></form>
<script>
  document.getElementById("threeDSAuthorizeForm").submit();
</script>
```

## 6. Complete the selected browser model

When the challenge or non-challenge result reaches `three_ds_authorize_url`, Hyperswitch responds with an HTML page containing a small script. That script detects at runtime whether it is running inside an iframe or in the top-level window, and behaves accordingly. This is why the same authorize URL serves both models. Use the section below that matches how you submitted the form in step 5.

### Embedded iframe

The authorize response runs inside the iframe. It posts one of two message shapes to the parent window:

* `poll_status` means authorization is still being finalized.
* `openurl_if_required` carries the return URL when no polling instruction is needed.

In `poll_status`, `frequency` and `delay_in_secs` are strings. This differs from the integer values in `next_action.three_ds_data.poll_config`.

```json
{
  "poll_status": {
    "poll_id": "external_authentication_<payment id>",
    "frequency": "5",
    "delay_in_secs": "2",
    "return_url_with_query_params": "https://<your domain>/payments/return?<query>"
  }
}
```

```json
{
  "openurl_if_required": "https://<your domain>/payments/return?<query>"
}
```

Register the listener before submitting the challenge or authorize form. Validate `event.origin` against the origin of `three_ds_authorize_url` before using the message.

```javascript
window.addEventListener("message", async (event) => {
  const authorizeOrigin = new URL("<three ds authorize url>").origin;
  if (event.origin !== authorizeOrigin) return;

  const data = event.data || {};

  if (data.poll_status) {
    const {
      poll_id: pollId,
      delay_in_secs: delayInSecs,
      frequency,
      return_url_with_query_params: returnUrl
    } = data.poll_status;

    const delayMs = Number.parseInt(delayInSecs, 10) * 1000;
    const maxAttempts = Number.parseInt(frequency, 10);

    for (let attempt = 0; attempt < maxAttempts; attempt += 1) {
      const response = await fetch(
        `https://sandbox.hyperswitch.io/poll/status/${encodeURIComponent(pollId)}`,
        { headers: { "api-key": "<publishable key>" } }
      );
      const poll = await response.json();

      if (poll.status === "completed" || poll.status === "not_found") break;
      await new Promise((resolve) => setTimeout(resolve, delayMs));
    }

    await retrieveFinalPayment(returnUrl);
    return;
  }

  if (data.openurl_if_required) {
    await retrieveFinalPayment(data.openurl_if_required);
  }
});
```

`GET /poll/status/{poll_id}` returns `pending`, `completed`, or `not_found`. It accepts the publishable key.

### Full-page redirect

The authorize response runs in the top-level window and redirects to `return_url`, appending `payment_id`, `status`, `payment_intent_client_secret`, `amount`, and `manual_retry_allowed` as query parameters. No `postMessage` is sent and `/poll/status` is not used in this model.

The redirect is immediate. The `status` in the return URL is the status at the moment of redirect and may not be terminal yet, because the return URL does not wait for authorization to finalize. Confirm the final status yourself on your return page.

Ensure `return_url` is set on the confirm request in step 1. In this model it is load-bearing: the backend redirects the top-level window to it.

Read `payment_id` and `payment_intent_client_secret` from the return URL, then retrieve the payment, retrying until the status is terminal.

```javascript
const params = new URLSearchParams(window.location.search);
const paymentId = params.get("payment_id");
const clientSecret = params.get("payment_intent_client_secret");

await retrieveFinalPayment(window.location.href, paymentId, clientSecret);
```

### Retrieve the final payment

Both models finish by retrieving the payment with `force_sync=true`. The retrieve endpoint accepts the publishable key when the payment client secret is supplied.

```javascript
async function retrieveFinalPayment(returnUrl, suppliedPaymentId, suppliedClientSecret) {
  const params = new URL(returnUrl).searchParams;
  const paymentId = suppliedPaymentId || params.get("payment_id");
  const clientSecret =
    suppliedClientSecret || params.get("payment_intent_client_secret");

  const response = await fetch(
    `https://sandbox.hyperswitch.io/payments/${encodeURIComponent(paymentId)}` +
      `?force_sync=true&client_secret=${encodeURIComponent(clientSecret)}`,
    { headers: { "api-key": "<publishable key>" } }
  );

  return response.json();
}
```

Use the returned payment `status` to decide what your application shows next.

In the full-page redirect model, retry the retrieve until the status is terminal:

```javascript
async function confirmFinalStatus(paymentId, clientSecret) {
  const terminal = ["succeeded", "failed", "cancelled", "requires_capture"];

  for (let attempt = 0; attempt < 10; attempt++) {
    const response = await fetch(
      `https://sandbox.hyperswitch.io/payments/${encodeURIComponent(paymentId)}` +
        `?force_sync=true&client_secret=${encodeURIComponent(clientSecret)}`,
      { headers: { "api-key": "<publishable key>" } }
    );
    const payment = await response.json();

    if (terminal.includes(payment.status)) {
      return payment;
    }
    await new Promise((resolve) => setTimeout(resolve, 2000));
  }
}
```

## Sandbox testing notes

* **Test OTP:** on the challenge page, choose any of the answers offered in the multiple-choice prompt.
* **Test card:** `2221008123677736`. This card is specific to Nuvei as the authorizing processor.
