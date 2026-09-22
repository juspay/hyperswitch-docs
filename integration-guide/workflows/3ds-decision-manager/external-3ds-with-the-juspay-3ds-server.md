# External 3DS with the Juspay 3DS Server

Configure and run external 3DS authentication with the **Juspay 3DS Server**. Juspay performs the cardholder authentication, while your configured payment processor (PSP) authorizes the payment.

This guide is written for server-to-server (S2S) merchants who drive checkout from their own backend. The server setup (Steps 1–5) is shared across platforms; Step 6 then splits into the **web** flow (browser iframe or full-page redirect) and the **mobile** flow (native challenge or in-app browser).

### How the integration works

A payment is created and confirmed on Hyperswitch. When external 3DS is requested, Hyperswitch uses Juspay as the authentication connector and returns a `three_ds_invoke` next action. Your client (web frontend or mobile app) then completes device data collection, calls the authentication endpoint, handles either a challenge or frictionless outcome, and finally retrieves the payment status.

1. Create and confirm a payment in Hyperswitch.
2. Receive `three_ds_invoke`.
3. Collect device data (a hidden fingerprinting iframe on web; the native 3DS SDK on mobile).
4. Call the 3DS authentication endpoint.
5. Handle challenge or frictionless authentication.
6. Finalize authorization and retrieve the payment status.

The client-side handling differs by platform:

| Platform   | Models                                                                                                                                           |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Web**    | Embedded iframe flow (cardholder stays on your page) or full-page redirect flow (browser navigates to the ACS and returns to your `return_url`). |
| **Mobile** | Native 3DS flow (challenge rendered by a native 3DS SDK inside your app) or redirected 3DS flow (challenge in an in-app browser).                |

{% hint style="info" %}
The most important platform difference is the **device channel**. Web sends `device_channel: "BRW"` and collects data via `browser_info` plus a hidden fingerprinting iframe. Mobile sends `device_channel: "APP"` and collects device data through the native 3DS SDK — there is **no** device-fingerprinting step and **no** `browser_info` on mobile.
{% endhint %}

### Step 1: Enable External 3DS

Contact [Hyperswitch Support](https://hyperswitch.io/contact-us) to enable External 3DS for your account. External 3DS can be enabled at either of the following levels:

* **Organization ID** — External 3DS is enabled for the organization, and all Merchant IDs (MIDs) under the organization are enabled for External 3DS by default.
* **Merchant ID** — External 3DS is enabled only for the specified MID.

### Step 2: Configure the payment connector with additional data

For External 3DS, the Merchant Connector Account (MCA) requires additional configuration metadata specific to the External 3DS flow. If you already have a payment connector configured, update the existing Merchant Connector Account to include the additional metadata required for the External 3DS flow.

The following is an example of an MCA update request for the Nuvei connector, including the additional fields required to support External 3DS:

```bash
curl --location 'https://sandbox.hyperswitch.io/account/{{merchant_id}}/connectors/{{mca_id}}' \
--header 'Content-Type: application/json' \
--header 'api-key: {{api_key}}' \
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

{% hint style="info" %}
Dashboard support for configuring these additional fields directly while setting up or updating a connector is on the way. Until then, set them through the API request shown above.
{% endhint %}

### Step 3: Configure the Juspay 3DS Server

Configure the Juspay 3DS Server as a 3DS authenticator. This enables Hyperswitch to use the Juspay 3DS Server for External 3DS authentication.

```bash
curl --location 'https://sandbox.hyperswitch.io/account/{{merchant_id}}/connectors' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'api-key: {{api_key}}' \
--data '{
    "connector_type": "authentication_processor",
    "connector_name": "juspaythreedsserver",
    "connector_label": "test",
    "profile_id": "{{profile_id}}",
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

### Step 4: Enable 3DS authentication on the business profile

Configure your business profile to use the Juspay 3DS Server.

```bash
curl --location 'https://sandbox.hyperswitch.io/account/{{merchant_id}}/business_profile/{{profile_id}}' \
--header 'Content-Type: application/json' \
--header 'api-key: {{api_key}}' \
--data '{
    "authentication_connector_details": {
        "authentication_connectors": [
            "juspaythreedsserver"
        ],
        "three_ds_requestor_url": "https://your-domain.com"
    },
    "merchant_country_code": "004",
    "merchant_category_code": "5411"
}'
```

### Step 5: Create the payment with External 3DS

Set [`request_external_three_ds_authentication`](https://api-reference.hyperswitch.io/v1/payments/payments--create#body-request-external-three-ds-authentication-one-of-0) to `true` to use the external 3DS flow instead of the processor's native 3DS.

{% hint style="warning" %}
On **web**, the `browser_info` object below is **required** and is reused later for the authentication step (Step 6 · Web). Collect it on your checkout page before confirming the payment. On **mobile**, `browser_info` is not sent — device data is supplied as `sdk_information` at authentication time (Step 6 · Mobile), gathered by the native 3DS SDK. If you use the Hyperswitch mobile SDK, it creates and confirms the payment for you.
{% endhint %}

```bash
curl --location 'https://sandbox.hyperswitch.io/payments' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'api-key: {{secret_api_key}}' \
--data '{
    "amount": 15100,
    "currency": "USD",
    "confirm": true,
    "capture_method": "automatic",
    "profile_id": "{{profile_id}}",
    "customer_id": "TestCustomer",
    "email": "test@example.com",
    "name": "John Doe",
    "phone": "999999999",
    "phone_country_code": "+1",
    "description": "External 3DS test payment",
    "authentication_type": "three_ds",
    "return_url": "https://your-domain.com/return",
    "request_external_three_ds_authentication": true,
    "payment_method": "card",
    "payment_method_type": "debit",
    "browser_info": {
        "accept_header": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "ip_address": "192.168.1.1",
        "java_enabled": false,
        "java_script_enabled": true,
        "language": "en-US",
        "color_depth": 24,
        "screen_height": 1080,
        "screen_width": 1920,
        "time_zone": 330,
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
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

The response returns a `next_action`, indicating that 3DS authentication is required. Continue to Step 6 for your platform.

### Step 6: Handle the 3DS flow

The client branches on `next_action.type`:

| `next_action.type` | Meaning                                                                                         |
| ------------------ | ----------------------------------------------------------------------------------------------- |
| `three_ds_invoke`  | External 3DS via the Juspay 3DS Server (produced only when External 3DS is enabled, Steps 1–5). |
| `redirect_to_url`  | Processor-native 3DS or fallback (produced when External 3DS is not used).                      |

Follow the section for your platform below.

### Step 6 · Web

Hyperswitch supports two web integration models. Choose the one that fits your UX requirements:

* **Embedded iframe flow** — device fingerprinting, the 3DS challenge, and result handling are performed within iframes embedded on your page. The cardholder remains on your checkout page throughout. You listen for `postMessage` events and poll a lightweight status endpoint to determine the authentication status.
* **Full-page redirect flow** — the 3DS challenge is presented by navigating the entire browser window. Once authentication completes, the cardholder is redirected to your configured `return_url`, where the final status can be retrieved. This is simpler to implement but does not provide an embedded experience.

{% hint style="info" %}
The device fingerprinting step (Web 6.2) always uses a **hidden** iframe, regardless of the integration model you select. It runs invisibly in the background and needs no cardholder interaction.
{% endhint %}

#### Web 6.1 — The `next_action` response

For the web flow, the response contains a `three_ds_invoke` action with a `three_ds_data` object:

```json
"next_action": {
  "type": "three_ds_invoke",
  "three_ds_data": {
    "three_ds_authentication_url": "https://SANDBOX_URL/payments/pay_XXXX/3ds/authentication",
    "three_ds_authorize_url": "https://SANDBOX_URL/payments/pay_XXXX/merchant_XXXX/authorize/nuvei",
    "three_ds_method_details": {
      "three_ds_method_data_submission": true,
      "three_ds_method_data": "eyJ0aHJlZURTU2VydmVyVHJhbnNJRCI6Ii4uLiJ9",
      "three_ds_method_url": "https://acs-public.tp.mastercard.com/api/v1/3ds_method",
      "three_ds_method_key": "threeDSMethodData",
      "consume_post_message_for_three_ds_method_completion": false
    },
    "poll_config": {
      "poll_id": "external_authentication_pay_XXXX",
      "delay_in_secs": 2,
      "frequency": 5
    },
    "message_version": "2.2.0",
    "directory_server_id": "A000000004",
    "card_network": "Mastercard"
  }
}
```

| Parameter                                                                     | Description                                                                                                                      |
| ----------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `three_ds_method_details.three_ds_method_data_submission`                     | Whether device fingerprinting (Web 6.2) is required.                                                                             |
| `three_ds_method_url` / `three_ds_method_data` / `three_ds_method_key`        | Inputs for the fingerprinting POST. For Juspay 3DS, `three_ds_method_key` is always `"threeDSMethodData"`.                       |
| `three_ds_method_details.consume_post_message_for_three_ds_method_completion` | For Juspay 3DS this is always `false`.                                                                                           |
| `three_ds_authentication_url`                                                 | Endpoint for the authentication call (Web 6.3).                                                                                  |
| `three_ds_authorize_url`                                                      | Endpoint to post the challenge/frictionless result to (Web 6.4).                                                                 |
| `poll_config`                                                                 | Poll id, delay, and max attempts for the lightweight status poll. Only used in the embedded iframe flow (Web 6.5, embedded tab). |

#### Web 6.2 — Device fingerprinting

{% hint style="info" %}
Perform this **only if** `three_ds_method_data_submission` is `true`. Otherwise skip directly to Web 6.3 with `threeds_method_comp_ind = "U"`.
{% endhint %}

Submit a hidden form (POST) to `three_ds_method_url`, targeting a hidden iframe, with one field named by `three_ds_method_key` (`threeDSMethodData`) carrying `three_ds_method_data`. The hidden iframe is required here in **both** web integration models — fingerprinting must run invisibly in the background without navigating your page away.

**Completion detection:**

* Detect the hidden iframe navigating away from `about:blank`. Cross-origin access to the iframe throws a `SecurityError`, which you can treat as completion.
* Apply a timeout of \~15 seconds as a fallback.

**Set the indicator (`threeds_method_comp_ind`) for Web 6.3:**

* `"Y"` — fingerprinting completed.
* `"N"` — timeout/error.
* `"U"` — fingerprinting was skipped (i.e. `three_ds_method_data_submission` was `false`).

```html
<iframe name="threeDSMethodFrame" style="display:none"></iframe>

<form id="tdsMethodForm" method="POST"
      action="{{three_ds_method_url}}" target="threeDSMethodFrame">
  <input name="{{three_ds_method_key}}" value="{{three_ds_method_data}}">
</form>

<script>document.getElementById('tdsMethodForm').submit();</script>
```

#### Web 6.3 — Authentication call

Call `three_ds_authentication_url` with the publishable API key. Send `client_secret`, `device_channel` (always `"BRW"` for browser), and the `threeds_method_comp_ind` from Web 6.2.

{% hint style="warning" %}
Do **not** send `browser_info` here — this endpoint does not accept it. Browser data is taken from the `browser_info` you already provided in the confirm request (Step 5).
{% endhint %}

**Request:**

```bash
curl --location 'https://sandbox.hyperswitch.io/payments/{{payment_id}}/3ds/authentication' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'api-key: {{publishable_api_key}}' \
--data '{
    "client_secret": "{{client_secret}}",
    "device_channel": "BRW",
    "threeds_method_comp_ind": "Y"
}'
```

**Response:**

```json
{
    "trans_status": "C",
    "acs_url": "https://.../acs/trigger-otp?redirectUrl=...",
    "challenge_request": "BASE64_ENCODED_CREQ",
    "challenge_request_key": "creq",
    "acs_trans_id": "UUID",
    "three_dsserver_trans_id": "UUID"
}
```

Based on `trans_status`:

* `trans_status = "C"` — a challenge is required (Web 6.4, challenge).
* Any other value — frictionless (Web 6.4, frictionless).

#### Web 6.4 — Submit the result

How you target the form in this step determines your integration model — target a visible iframe to keep the cardholder on your page, or submit in the top-level window to redirect the whole browser.

{% tabs %}
{% tab title="Embedded iframe flow" %}
**Challenge (`trans_status = "C"`)** — submit a form (POST) to `acs_url` with one field named by `challenge_request_key` (default `creq`) carrying `challenge_request`, targeting a **visible** iframe. The ACS renders the challenge (e.g. OTP) inside your page.

```html
<iframe name="threeDsAuthFrame" style="width:100%;min-height:500px"></iframe>

<form id="acsForm" method="POST" action="{{acs_url}}" target="threeDsAuthFrame">
  <input name="{{challenge_request_key}}" value="{{challenge_request}}">
</form>

<script>document.getElementById('acsForm').submit();</script>
```

**Frictionless (any other `trans_status`)** — no challenge is shown. Submit a form (POST) to `three_ds_authorize_url` targeting the same visible iframe to finalize authorization.

```html
<iframe name="threeDsAuthFrame" style="width:100%;min-height:500px"></iframe>

<form id="authorizeForm" method="POST" action="{{three_ds_authorize_url}}" target="threeDsAuthFrame">
</form>

<script>document.getElementById('authorizeForm').submit();</script>
```

Continue to Web 6.5 (embedded iframe tab).
{% endtab %}

{% tab title="Full-page redirect flow" %}
**Challenge (`trans_status = "C"`)** — submit a form (POST) to `acs_url` in the top-level window (no `target`). The whole browser navigates to the ACS challenge page.

```html
<form id="acsForm" method="POST" action="{{acs_url}}">
  <input name="{{challenge_request_key}}" value="{{challenge_request}}">
</form>

<script>document.getElementById('acsForm').submit();</script>
```

**Frictionless (any other `trans_status`)** — no challenge is shown. Submit a form (POST) to `three_ds_authorize_url` in the top-level window.

```html
<form id="authorizeForm" method="POST" action="{{three_ds_authorize_url}}"></form>

<script>document.getElementById('authorizeForm').submit();</script>
```

Continue to Web 6.5 (full-page redirect tab).
{% endtab %}
{% endtabs %}

#### Web 6.5 — Completion

When the challenge/frictionless result reaches `three_ds_authorize_url`, Hyperswitch responds with an HTML page containing a small script. That script detects at runtime whether it is running inside an iframe or in the top-level window and behaves accordingly. Use the completion section below that matches how you submitted the form in Web 6.4.

{% tabs %}
{% tab title="Embedded iframe flow" %}
Since the authorized response is loaded inside your iframe, its script does not redirect. Instead it sends a `postMessage` to the parent (merchant) window. Add a listener on the parent window. Two message shapes are possible:

* When authorization is still finalizing (HS intent status `requires_customer_action`), you receive a `poll_status` message:

```json
{
  "poll_status": {
    "poll_id": "external_authentication_pay_XXXX",
    "frequency": "5",
    "delay_in_secs": "2",
    "return_url_with_query_params": "https://your-domain.com/return?payment_id=pay_XXXX&status=..."
  }
}
```

* When authorization is already resolved, you receive an `openurl_if_required` message whose value is the return URL string:

```json
{ "openurl_if_required": "https://your-domain.com/return?payment_id=pay_XXXX&status=..." }
```

{% hint style="info" %}
In the `poll_status` message, `frequency` and `delay_in_secs` are **strings**. In the `poll_config` object from Web 6.1 they are integers.
{% endhint %}

**Parent-window listener:**

```javascript
window.addEventListener("message", async (event) => {
  const data = event.data || {};

  // Case 1: authorization still finalizing -> poll, then retrieve
  if (data.poll_status) {
    const { poll_id, delay_in_secs, frequency, return_url_with_query_params } = data.poll_status;
    const delayMs = parseInt(delay_in_secs, 10) * 1000;
    const maxAttempts = parseInt(frequency, 10);

    for (let i = 0; i < maxAttempts; i++) {
      const res = await fetch(`{{SANDBOX_URL}}/poll/status/${poll_id}`, {
        headers: { "api-key": "{{publishable_api_key}}" }
      });
      const poll = await res.json();
      if (poll.status === "completed" || poll.status === "not_found") break;
      await new Promise(r => setTimeout(r, delayMs));
    }

    await retrieveAndFinish(return_url_with_query_params);
  }

  // Case 2: already resolved -> just retrieve
  if (data.openurl_if_required) {
    await retrieveAndFinish(data.openurl_if_required);
  }
});

async function retrieveAndFinish(returnUrl) {
  // force_sync=true makes Hyperswitch sync with the connector for the freshest status
  const res = await fetch(
    `{{SANDBOX_URL}}/payments/{{payment_id}}?force_sync=true&client_secret={{client_secret}}`,
    { headers: { "api-key": "{{publishable_api_key}}" } }
  );
  const payment = await res.json();
  // payment.status is now succeeded / failed / requires_capture / etc.
  // Update your UI, or redirect to returnUrl.
}
```

**Poll endpoint — `GET /poll/status/{poll_id}`:**

```bash
curl --location '{{SANDBOX_URL}}/poll/status/{{poll_id}}' \
--header 'api-key: {{publishable_api_key}}'
```

```json
{ "poll_id": "external_authentication_pay_XXXX", "status": "pending" }
```

`status` will be one of `pending`, `completed`, or `not_found`. Poll while `pending` (waiting `delay_in_secs` between calls, up to `frequency` attempts). Once `completed`, retrieve the payment for the final status:

```bash
curl --location '{{SANDBOX_URL}}/payments/{{payment_id}}?force_sync=true&client_secret={{client_secret}}' \
--header 'api-key: {{publishable_api_key}}'
```
{% endtab %}

{% tab title="Full-page redirect flow" %}
Since the authorized response is loaded in the top-level window, its script runs the redirect branch and navigates the browser directly to `return_url`, with `payment_id`, `status`, `payment_intent_client_secret`, `amount`, and `manual_retry_allowed` query params appended. No `postMessage` is sent and `/poll/status` is not used in this model.

{% hint style="warning" %}
The redirect is immediate. The `status` in the return URL is the status **at the moment of redirect** and may not yet be terminal — the return URL does not wait for authorization to finalize. You must confirm the final status yourself on your return page.
{% endhint %}

On your return page, retrieve the payment with `force_sync=true` and retry until the status is terminal:

```bash
curl --location '{{SANDBOX_URL}}/payments/{{payment_id}}?force_sync=true&client_secret={{client_secret}}' \
--header 'api-key: {{publishable_api_key}}'
```

**Example return-page logic:**

```javascript
// On your return page, read payment_id and payment_intent_client_secret from the
// query params and use them for the retrieve call:
// const params = new URLSearchParams(window.location.search);
// const paymentId = params.get("payment_id");
// const clientSecret = params.get("payment_intent_client_secret");

async function confirmFinalStatus(paymentId, clientSecret) {
  const terminal = ["succeeded", "failed", "cancelled", "requires_capture"];
  for (let i = 0; i < 10; i++) {
    const res = await fetch(
      `{{SANDBOX_URL}}/payments/${paymentId}?force_sync=true&client_secret=${clientSecret}`,
      { headers: { "api-key": "{{publishable_api_key}}" } }
    );
    const payment = await res.json();
    if (terminal.includes(payment.status)) return payment;
    await new Promise(r => setTimeout(r, 2000)); // wait, then retry
  }
}
```

{% hint style="warning" %}
Ensure `return_url` is set in the confirm request (Step 5). In this model it is load-bearing — the backend redirects the top-level window to it.
{% endhint %}
{% endtab %}
{% endtabs %}

### Step 6 · Mobile

On mobile there is no browser page or iframe, so device data collection and challenge rendering are handled by a **native 3DS SDK** embedded in your app rather than by browser iframes. The External 3DS flow itself is identical to web — the same authentication and authorize endpoints, the same challenge/frictionless branch — only the client that performs it changes.

There are two ways to run this flow on mobile:

* **Hyperswitch mobile SDK (iOS, Android, React Native)** — the SDK performs the entire flow below for you, including bundling and driving a native 3DS SDK. It is 3DS-provider agnostic: it detects an available 3DS SDK at runtime (the Juspay 3DS SDK or Netcetera) and drives it, so you don't integrate a 3DS SDK yourself. If you take this path, the steps below describe what happens under the hood so you can configure it correctly and understand the states your app will surface.
* **Direct server-to-server integration** — if you want to stay fully S2S and drive checkout from your own app _without_ the Hyperswitch mobile SDK, integrate a **native 3DS SDK directly** and make the same Hyperswitch API calls the web flow uses. The **Juspay 3DS SDK** is the recommended option for S2S merchants. The 3DS SDK is used only to gather device data and render the challenge; every network call in the steps below is a plain Hyperswitch API call your app makes itself.

{% hint style="info" %}
The **Juspay 3DS Server** (Steps 1–5) and the **Juspay 3DS SDK** are different components despite the similar names. The 3DS Server is the server-side `authentication_processor` connector that performs the authentication; the 3DS SDK is a client-side library embedded in your mobile app that collects device data and renders the challenge. You can use either 3DS SDK provider (Juspay or Netcetera) with the Juspay 3DS Server.
{% endhint %}

Either way, the client branches on `next_action.type`:

| `next_action.type` | Flow                                                | Section          |
| ------------------ | --------------------------------------------------- | ---------------- |
| `three_ds_invoke`  | Native 3DS (External 3DS via the Juspay 3DS Server) | Mobile 6.1 → 6.M |
| `redirect_to_url`  | Redirected 3DS (processor-native 3DS or fallback)   | Mobile 6.R       |

#### Mobile 6.1 — The `next_action` response (`three_ds_invoke`)

Similar shape to web, but without `three_ds_method_details` (there is no fingerprinting step on mobile):

```json
"next_action": {
  "type": "three_ds_invoke",
  "three_ds_data": {
    "three_ds_authentication_url": "https://SANDBOX_URL/payments/pay_XXXX/3ds/authentication",
    "three_ds_authorize_url": "https://SANDBOX_URL/payments/pay_XXXX/merchant_XXXX/authorize/nuvei",
    "poll_config": {
      "poll_id": "external_authentication_pay_XXXX",
      "delay_in_secs": 2,
      "frequency": 5
    },
    "message_version": "2.2.0",
    "directory_server_id": "A000000004",
    "card_network": "Mastercard"
  }
}
```

| Parameter                     | Description                                                                                                                       |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `three_ds_authentication_url` | Endpoint for the native authentication call (Mobile 6.M.2).                                                                       |
| `three_ds_authorize_url`      | Endpoint to POST to after challenge/frictionless to finalize authorization (Mobile 6.M.4).                                        |
| `message_version`             | 3DS protocol version. Passed to the native SDK to generate the authentication request (AReq) parameters.                          |
| `directory_server_id`         | Card-network directory server ID. Passed to the native SDK to generate AReq parameters.                                           |
| `poll_config`                 | `poll_id`, `delay_in_secs`, and max attempts (`frequency`) for the status poll used while authorization finalizes (Mobile 6.M.5). |

{% hint style="info" %}
Unlike web, mobile does **not** use `three_ds_method_details` (device fingerprinting). Device data is gathered natively by the 3DS SDK, so the fingerprinting iframe and `threeds_method_comp_ind` / `three_ds_method_url` inputs are not part of the mobile flow.
{% endhint %}

#### Mobile 6.M — Native 3DS flow (`device_channel = "APP"`)

**Prerequisite: integrate a native 3DS SDK**

Native 3DS on mobile is powered by a **native 3DS SDK** that generates the authentication request (AReq) parameters and renders the challenge screen. Hyperswitch is provider agnostic here. To enable it:

1. Add the 3DS SDK dependency to your app (iOS pod / Android gradle / React Native package, as documented in that SDK's integration guide).
2. Provide the **3DS SDK API key** in the configuration (`threeDsSdkApiKey`) (Optional, provider dependent).

{% hint style="info" %}
If you use the Hyperswitch mobile SDK, it detects an available 3DS SDK at runtime (Juspay 3DS SDK or Netcetera) and drives it for you — you only supply the dependency and API key. If you integrate directly, you call the 3DS SDK yourself at the points noted below.
{% endhint %}

{% hint style="danger" %}
If no native 3DS SDK is present, the native flow cannot run and the payment fails with an external-3DS error. Ensure a 3DS SDK dependency is added before testing.
{% endhint %}

The flow then runs the following sequence.

**Mobile 6.M.1 — Initialize the 3DS SDK and generate AReq parameters**

Initialize the native 3DS SDK (once per session), then generate the **authentication request (AReq) parameters** using `message_version`, `directory_server_id`, and `card_network` from Mobile 6.1. This yields the encrypted device data, SDK app ID, SDK transaction ID, SDK reference number, and an ephemeral public key.

**Mobile 6.M.2 — Authentication call**

POST to `three_ds_authentication_url` with `device_channel: "APP"` and an `sdk_information` object built from the AReq parameters. There is **no `browser_info`** — device data lives inside `sdk_information`:

```json
{
  "client_secret": "{{client_secret}}",
  "device_channel": "APP",
  "threeds_method_comp_ind": "N",
  "sdk_information": {
    "sdk_app_id": "…",
    "sdk_enc_data": "…",
    "sdk_ephem_pub_key": { "kty": "…", "crv": "…", "x": "…", "y": "…" },
    "sdk_trans_id": "…",
    "sdk_reference_number": "…",
    "sdk_max_timeout": 10
  }
}
```

Headers: `Content-Type: application/json`, and either `api-key: <publishable key>` **or** `Authorization: <sdkAuthorization>` when using an ephemeral/session token.

**Response (APP channel):**

```json
{
  "trans_status": "C",
  "acs_signed_content": "…",
  "acs_reference_number": "…",
  "acs_trans_id": "UUID",
  "three_dsserver_trans_id": "UUID"
}
```

Based on `trans_status`:

* `trans_status = "C"` — a **challenge** is required (Mobile 6.M.3a).
* Any other value — **frictionless** (Mobile 6.M.3b).

{% hint style="info" %}
The APP-channel response returns `acs_signed_content` (not the web `acs_url` + `creq`). This signed content is handed directly to the native SDK to render the challenge — there is no form POST to an ACS URL.
{% endhint %}

**Mobile 6.M.3a — Challenge flow (`trans_status = "C"`)**

Pass `acs_signed_content`, `acs_reference_number`, `acs_trans_id`, and `three_dsserver_trans_id` to the native 3DS SDK, which renders the **challenge screen natively** inside your app (the OTP/biometric UI is drawn by the 3DS SDK — there is no iframe and no browser). On completion, proceed to Mobile 6.M.4.

**Mobile 6.M.3b — Frictionless flow (any other `trans_status`)**

No challenge screen is shown. Proceed directly to Mobile 6.M.4.

**Mobile 6.M.4 — Finalize authorization**

POST (empty body) to `three_ds_authorize_url` to finalize authorization — the mobile equivalent of the web "authorize" submission. This is done for both the challenge and frictionless paths.

**Mobile 6.M.5 — Completion (retrieve + short-poll)**

Authorization can take a moment to settle at the connector, so confirm the final status yourself:

1. **Retrieve** the payment (`GET /payments/{payment_id}` with `force_sync=true`).
2. If the status is already terminal, surface it:
   * `succeeded` / `processing` → **success**
   * `failed` → **failure**
3. If the status is not yet terminal (still `requires_customer_action`), **short-poll** `GET /poll/status/{poll_id}` using `poll_config` — waiting `delay_in_secs` between calls, up to `frequency` attempts — until `status = "completed"`, then **retrieve once more** for the final status.

```bash
curl --location '{{SANDBOX_URL}}/poll/status/{{poll_id}}' \
--header 'api-key: {{publishable_api_key}}'
```

```json
{ "poll_id": "external_authentication_pay_XXXX", "status": "pending" }
```

`status` is one of `pending`, `completed`, or `not_found`. This mirrors the web embedded-iframe completion (Web 6.5, embedded tab), except you poll directly instead of listening for a `postMessage` from an iframe.

#### Mobile 6.R — Redirected 3DS flow (`redirect_to_url`)

When the intent returns `status: "requires_customer_action"` with a `next_action.type` of `redirect_to_url`, open the authentication URL in an in-app browser. This is the mobile equivalent of the web full-page redirect (Web 6.5, redirect tab), and is the flow used for **processor-native 3DS** (i.e. when External 3DS is not enabled). No native 3DS SDK is required for this flow.

```json
"next_action": {
  "type": "redirect_to_url",
  "redirect_to_url": "https://SANDBOX_URL/payments/redirect/pay_XXXX/…"
}
```

**Mobile 6.R.1 — Prerequisite: `return_url`**

Set `return_url` in the confirm request (Step 5).

{% hint style="warning" %}
`return_url` is **load-bearing** on mobile: the in-app browser watches for a navigation to your `return_url` carrying a `status=` query parameter, and uses that to know the flow is finished. Ensure the `return_url` scheme/host is registered with your app's redirect configuration.
{% endhint %}

**Mobile 6.R.2 — Open the authentication URL**

Open `redirect_to_url` in a secure in-app browser:

{% tabs %}
{% tab title="iOS" %}
`SFSafariViewController` / `ASWebAuthenticationSession` (ephemeral session for card payments).
{% endtab %}

{% tab title="Android" %}
Chrome Custom Tabs.
{% endtab %}
{% endtabs %}

The cardholder completes the ACS challenge (e.g. OTP) in that browser.

**Mobile 6.R.3 — Return and finalize**

When the ACS redirects to your `return_url`, inspect the appended `status=` query parameter:

* `status=succeeded` / `processing` / `requires_capture` / `partially_captured` → treat as **success**, then **retrieve** the payment for the authoritative final status.
* `status=failed` / `requires_payment_method` → **failure**.
* Browser dismissed without a status → **cancelled**.

As on web, the status in the return URL is the status _at the moment of redirect_ and may not yet be terminal — always perform a **retrieve** to confirm the final state before reporting the result to your app:

```bash
curl --location '{{SANDBOX_URL}}/payments/{{payment_id}}?force_sync=true&client_secret={{client_secret}}' \
--header 'api-key: {{publishable_api_key}}'
```

#### Choosing native vs redirected on mobile

You do not choose the flow per request — it is determined by your configuration:

* **Enable External 3DS (Steps 1–5) + integrate a native 3DS SDK** → confirm returns `three_ds_invoke` → **native flow (Mobile 6.M)**, with the challenge rendered inside your app.
* **Do not enable External 3DS** → the processor returns a standard `redirect_to_url` → **redirected flow (Mobile 6.R)**, with the challenge in an in-app browser.

{% hint style="info" %}
If External 3DS is requested but the native 3DS SDK cannot initialize or generate AReq parameters, retrieve the payment and surface the resulting status rather than silently failing. (The Hyperswitch mobile SDK does this automatically.)
{% endhint %}

### Web vs mobile at a glance

| Aspect                        | Web                                             | Mobile                                                      |
| ----------------------------- | ----------------------------------------------- | ----------------------------------------------------------- |
| Device channel                | `BRW`                                           | `APP`                                                       |
| Device data source            | `browser_info` + hidden fingerprinting iframe   | Native 3DS SDK (`sdk_information`)                          |
| Fingerprinting step (Web 6.2) | Required (hidden iframe)                        | Not applicable                                              |
| Challenge rendering           | Iframe or full-page redirect                    | Native SDK screen **or** in-app browser                     |
| Auth response                 | `acs_url` + `creq`                              | `acs_signed_content`                                        |
| Completion signal             | `postMessage` (iframe) or return URL (redirect) | Retrieve + `/poll/status` (native) or return URL (redirect) |
| Final status                  | Retrieve with `force_sync=true`                 | Retrieve with `force_sync=true`                             |

### Sandbox testing

* **Test OTP** — choose any of the answers in the MCQ presented by the ACS.
* **Test card** — `2221008123677736` (Nuvei-specific).
* For native mobile testing, confirm a **native 3DS SDK dependency** (Juspay 3DS SDK or Netcetera) is bundled and `threeDsSdkApiKey` is set; otherwise the app falls back to an error on `three_ds_invoke`.
