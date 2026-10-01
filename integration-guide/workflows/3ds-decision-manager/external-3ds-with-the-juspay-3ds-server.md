<!-- truth manifest; hyperswitch cfbeb2bedf523da301d7d7b0a8dcbeaf2263c696; spec api-reference/v1/openapi_spec_v1.json@cfbeb2bedf523da301d7d7b0a8dcbeaf2263c696
     symbols: POST /account/{account_id}/business_profile/{profile_id} = crates/openapi/src/routes/profile.rs:40-70
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

* **Embedded iframe:** the challenge stays on your checkout page. Completion arrives through `postMessage`.
* **Full-page redirect:** the browser opens the challenge at the top level and returns to your `return_url`.

The two models share the same setup, payment, fingerprinting, and authentication calls. They differ only in the target used for the final forms and how your application receives completion.

For the provider-neutral explanation, see [Standalone 3D Secure](external-authentication-for-3ds.md). Mobile 3DS is outside this browser walkthrough.

## Before you start

1. Configure the payment processor that will authorize the payment.
2. Configure the [Juspay 3DS Server authentication connector](../../../integration-space/connectors-integrations/3ds-providers/juspaythreedsserver.md). Connector credentials and activation belong on that connector page.
3. Add the authentication connector to the Business Profile used by the payment.
4. Keep both a secret API key on your backend and a publishable key in the browser. Never expose the secret API key in browser code.

### Add the authentication connector to the Business Profile

Update the profile with your secret API key. `authentication_connector_details` contains the ordered authentication connector list and the 3DS requestor URL.

```bash
curl --request POST \
  --url 'https://sandbox.hyperswitch.io/account/<merchant id>/business_profile/<profile id>' \
  --header 'Content-Type: application/json' \
  --header 'api-key: <secret api key>' \
  --data '{
    "authentication_connector_details": {
      "authentication_connectors": ["juspaythreedsserver"],
      "three_ds_requestor_url": "https://<your domain>"
    }
  }'
```

## 1. Create and confirm the payment

Set `request_external_three_ds_authentication` to `true`, use `authentication_type: "three_ds"`, and provide a `return_url`.

The v1 schema allows `browser_info` to be omitted. The authentication transformer then supplies an empty browser object. Send the real browser values for a browser transaction so the authentication request does not rely on that fallback.

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
        "card_number": "<card number>",
        "card_exp_month": "<expiry month>",
        "card_exp_year": "<expiry year>",
        "card_holder_name": "<cardholder name>",
        "card_cvc": "<card cvc>"
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
| `three_ds_authentication_url` | Send the browser authentication request in step 4. |
| `three_ds_authorize_url` | Finalize the challenge or non-challenge result in step 5. |
| `three_ds_method_details` | Build the hidden fingerprinting form in step 3. |
| `poll_config` | Poll after an embedded completion message asks you to do so. |
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

The ACS posts its result to `three_ds_authorize_url`.

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

The authorize response runs in the top-level window and redirects to `return_url`. Read `payment_id` and `payment_intent_client_secret` from the return URL, then retrieve the payment. Do not use the query-string status as the final result.

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
