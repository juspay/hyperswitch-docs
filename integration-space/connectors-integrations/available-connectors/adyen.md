---
description: >-
  Accept payments globally through Adyen via Hyperswitch, supporting cards,
  wallets, and local payment methods.
metaLinks:
  alternates:
    - adyen.md
---

# Adyen

<img src="https://hyperswitch.io/icons/homePageIcons/logos/adyenLogo.svg" alt="" data-size="original">

Adyen connects to Hyperswitch as a `PaymentGateway` connector using `HeaderKey` authentication — the API key is passed as an `X-API-Key` header on every request, and requests are sent as `application/json`. Adyen is one of the few connectors in Hyperswitch that supports `ManualMultiple` capture, allowing a single authorized amount to be captured in multiple partial steps — a capability required for hospitality and travel use cases where final amounts are confirmed at checkout time.

### Connector-Specific Notes

- **ManualMultiple capture:** Adyen supports capturing a single authorization in multiple partial steps. This is controlled at the Hyperswitch level via `capture_method: manual_multiple` and maps to Adyen's multi-capture API. Capture methods supported: Automatic, Manual, SequentialAutomatic, ManualMultiple.
- **Webhook verification:** Adyen uses HMAC-SHA256 signature verification. The HMAC key is found in your Adyen dashboard under **Developers → Webhooks → your webhook → HMAC key**. This key is stored in Hyperswitch and used to verify the `HmacSignature` field in every incoming Adyen notification. See [Adyen HMAC documentation](https://docs.adyen.com/development-resources/webhooks/verify-hmac-signatures/#enable-hmac-signatures) for setup steps.
- **Raw card data:** Adyen requires explicit enablement of raw card data handling. Contact Adyen support at support@adyen.com to enable this for your account before using Hyperswitch to process card payments directly.
- **Klarna via Adyen — mandatory fields:** For Klarna payments routed through Adyen, the following fields must be present on the payment request: `email`, `billing.first_name`, `billing.last_name`, `billing.city`, `billing.country`, `billing.line1`, `billing.line2`, `billing.zip`, and `order_details`. Additionally, `customer_id` is required — create a customer first via the [Hyperswitch Create Customer API](https://api-reference.hyperswitch.io/v1/customers/customers--create).
- **Sandbox capture behaviour for Klarna and PayPal:** In Adyen's sandbox environment, Automatic Capture does not work as intended for Klarna and PayPal — payments must be explicitly captured before refunds can be processed. This is an Adyen sandbox account configuration issue, not a Hyperswitch bug. If this persists in production, contact Adyen support to disable automatic captures for these methods.
- **Sofort deprecation:** Adyen has discontinued support for Sofort as a payment method. The Hyperswitch–Adyen integration retains the Sofort implementation but its availability depends on your Adyen account configuration. Contact Adyen support if Sofort is not functioning as expected.
- For a full list of supported payment methods, visit [hyperswitch.io/pm-list](https://hyperswitch.io/pm-list).

### Supported Country-Currency Matrix

| Payment Method | Countries | Currencies |
| :---: | --- | --- |
| Credit/Debit Cards | All enabled on your Adyen account | All enabled on your Adyen account |
| Apple Pay | `AU,NZ,CN,JP,HK,SG,MY,BH,AE,KW,BR,ES,GB,SE,NO,AT,NL,DE,HU,CY,LU,CH,BE,FR,DK,FI,RO,HR,LI,UA,MT,SI,GR,PT,IE,CZ,EE,LT,LV,IT,PL,IS,CA,US` | `AUD,CHF,CAD,EUR,GBP,HKD,SGD,USD` |
| Google Pay | `AU,NZ,JP,HK,SG,MY,TH,VN,BH,AE,KW,BR,ES,GB,SE,NO,SK,AT,NL,DE,HU,CY,LU,CH,BE,FR,DK,RO,HR,LI,MT,SI,GR,PT,IE,CZ,EE,LT,LV,IT,PL,TR,IS,CA,US` | All enabled on your Adyen account |
| PayPal | `AU,NZ,CN,JP,HK,MY,TH,KR,PH,ID,AE,KW,BR,ES,GB,SE,NO,SK,AT,NL,DE,HU,CY,LU,CH,BE,FR,DK,FI,RO,HR,UA,MT,SI,GI,PT,IE,CZ,EE,LT,LV,IT,PL,IS,CA,US` | `AUD,BRL,CAD,CZK,DKK,EUR,HKD,HUF,INR,JPY,MYR,MXN,NZD,NOK,PHP,PLN,RUB,GBP,SGD,SEK,CHF,THB,USD` |
| iDEAL | `NL` | `EUR` |
| Sofort | `AT,BE,DE,ES,CH,NL` | `CHF,EUR` |
| Klarna | `AU,AT,BE,CA,CZ,DK,FI,FR,DE,GR,IE,IT,NO,PL,PT,RO,ES,SE,CH,NL,GB,US` | `AUD,EUR,CAD,CZK,DKK,NOK,PLN,RON,SEK,CHF,GBP,USD` |

If your desired country-currency combination is not listed, contact Hyperswitch Support to enable it.

---

### Activating Adyen via Hyperswitch

#### Prerequisites

1. You need to be registered with Adyen. Sign up at [adyen.com/signup](https://www.adyen.com/signup).
2. You should have a registered Hyperswitch account, accessible from the [Hyperswitch control center](https://app.hyperswitch.io/register).
3. Request the Adyen support team to enable raw card data handling via email (support@adyen.com).
4. The Adyen API key and Account ID are available in your Adyen dashboard under **Home → Developers → API credentials**.
5. Select all payment methods you wish to use Adyen for. Ensure these match the ones configured in your Adyen dashboard under **Settings → Payment methods**.
6. Navigate to **Developers → Webhooks** in your Adyen dashboard and create a new standard webhook.

[Steps to activate Adyen on the Hyperswitch control center](https://docs.hyperswitch.io/hyperswitch-cloud/connectors/activate-connector-on-hyperswitch)

---

### Responsibility Boundaries

**Hyperswitch owns:** routing decisions, retry scheduling, mandate record storage, and webhook fan-out to your endpoint. **Adyen owns:** payment execution, fraud decisioning, payment method availability per region, and webhook delivery to Hyperswitch's endpoint. Adyen's country-currency availability for each payment method is determined by your Adyen account configuration — Hyperswitch cannot enable methods that Adyen has not activated for your merchant account.

**Hyperswitch owns:** capture method orchestration (deciding when and how much to capture). **Adyen owns:** execution of the capture call against the original authorization. When using ManualMultiple capture, Hyperswitch sends separate capture requests to Adyen for each partial amount — Adyen enforces that the total captured does not exceed the authorized amount.

---

### Common Failure Modes

**Raw card data not enabled**
Symptom: Card payments fail at the Adyen API before authorization. Fix: Contact Adyen support (support@adyen.com) to enable raw card data handling for your account.

**HMAC key mismatch**
Symptom: Adyen webhooks arrive at Hyperswitch but are rejected — payment statuses do not update. Fix: The HMAC key in Hyperswitch must match the one shown in **Developers → Webhooks → your webhook → HMAC key** in the Adyen dashboard.

**Klarna payment failure due to missing fields**
Symptom: Klarna payments via Adyen fail with a validation error. Fix: Ensure all mandatory Klarna fields are present (`email`, billing address fields, `order_details`, `customer_id`).

**Payment method not available in Adyen account**
Symptom: A payment method selected in Hyperswitch fails at Adyen with a method availability error. Fix: Verify the method is enabled in your Adyen dashboard under **Settings → Payment methods** and that your Adyen account is approved for that method in the target country.

**Sofort payments not processing**
Symptom: Sofort payments fail or are unavailable. Fix: Adyen has deprecated Sofort — contact Adyen support to confirm whether Sofort remains available on your specific account.

---

Connector implementation: `crates/hyperswitch_connectors/src/connectors/adyen.rs`. For Adyen for Platforms (marketplace payouts), see the separate [Adyen for Platforms](adyen-for-platforms.md) page.
