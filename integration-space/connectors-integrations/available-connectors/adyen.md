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

Configure an API key and merchant account for Adyen. Hyperswitch also accepts an optional review key in the connector credentials. Requests are sent as `application/json`. See [`AdyenAuthType`](https://github.com/juspay/hyperswitch/blob/f35edab780c97dd12efdd366246ff3f7fbc0e940/crates/hyperswitch_connectors/src/connectors/adyen/transformers.rs#L1511-L1516) and its [`ConnectorAuthType` mapping](https://github.com/juspay/hyperswitch/blob/f35edab780c97dd12efdd366246ff3f7fbc0e940/crates/hyperswitch_connectors/src/connectors/adyen/transformers.rs#L1762-L1782).

### Status and capabilities

<!-- generated from GET /feature_matrix; hyperswitch f35edab780c97dd12efdd366246ff3f7fbc0e940; host http://localhost:8080; fetched 2026-09-08; matrix canonical-json-v1 sha256 36360b019f2761dd; 138 connectors.
     Do not edit by hand. This block regenerates from the connector's
     SupportedPaymentMethods declaration in code; edit that instead. -->

**Integration status:** live  
**Category:** payment gateway  
**Webhook flows:** disputes, mandates, payments, payouts, refunds

| Payment method | Type | Mandates | Refunds | Capture methods | 3DS | Card networks | Countries | Currencies |
|---|---|---|---|---|---|---|---|---|
| bank debit | ACH Direct Debit | supported | supported | automatic, manual, sequential automatic | not applicable | - | USA | USD |
| bank debit | BACS Direct Debit | supported | supported | automatic, manual, sequential automatic | not applicable | - | GBR | GBP |
| bank debit | SEPA Direct Debit | supported | supported | automatic, manual, sequential automatic, manual multiple | not applicable | - | 14 ([full list](https://hyperswitch.io/pm-list)) | EUR |
| bank redirect | Bancontact Card | supported | supported | automatic, sequential automatic | not applicable | - | BEL | EUR |
| bank redirect | Bizum | not supported | supported | automatic, sequential automatic | not applicable | - | ESP | EUR |
| bank redirect | BLIK | not supported | supported | automatic, sequential automatic | not applicable | - | POL | PLN |
| bank redirect | EPS | not supported | supported | automatic, sequential automatic | not applicable | - | AUT | EUR |
| bank redirect | iDEAL | supported | supported | automatic, sequential automatic | not applicable | - | NLD | EUR |
| bank redirect | Online Banking Czech Republic | not supported | supported | automatic, sequential automatic | not applicable | - | CZE | CZK, EUR |
| bank redirect | Online Banking Finland | not supported | supported | automatic, sequential automatic | not applicable | - | FIN | EUR |
| bank redirect | Online Banking FPX | not supported | supported | automatic, sequential automatic | not applicable | - | MYS | MYR |
| bank redirect | Online Banking Poland | not supported | supported | automatic, sequential automatic | not applicable | - | POL | PLN |
| bank redirect | Online Banking Slovakia | not supported | supported | automatic, sequential automatic | not applicable | - | SVK | CZK, EUR |
| bank redirect | Online Banking Thailand | not supported | supported | automatic, sequential automatic | not applicable | - | THA | THB |
| bank redirect | Open Banking UK | supported | supported | automatic, sequential automatic | not applicable | - | GBR | GBP |
| bank redirect | Trustly | supported | supported | automatic, sequential automatic | not applicable | - | 12 ([full list](https://hyperswitch.io/pm-list)) | CZK, DKK, EUR, GBP, NOK, SEK |
| bank transfer | BCA Bank Transfer | not supported | supported | automatic, sequential automatic | not applicable | - | IDN | IDR |
| bank transfer | BNI Virtual Account | not supported | supported | automatic, sequential automatic | not applicable | - | IDN | IDR |
| bank transfer | BRI Virtual Account | not supported | supported | automatic, sequential automatic | not applicable | - | IDN | IDR |
| bank transfer | CIMB Virtual Account | not supported | supported | automatic, sequential automatic | not applicable | - | IDN | IDR |
| bank transfer | Danamon Virtual Account | not supported | supported | automatic, sequential automatic | not applicable | - | IDN | IDR |
| bank transfer | Mandiri Virtual Account | not supported | supported | automatic, sequential automatic | not applicable | - | IDN | IDR |
| bank transfer | Permata Bank Transfer | not supported | supported | automatic, sequential automatic | not applicable | - | IDN | IDR |
| bank transfer | Pix | not supported | supported | automatic, sequential automatic | not applicable | - | BRA | BRL |
| card | Credit Card | supported | supported | automatic, manual, sequential automatic, manual multiple | supported, optional | American Express, Cartes Bancaires, Diners Club, Discover, Interac, JCB, Maestro, Mastercard, UnionPay, Visa | - | - |
| card | Debit Card | supported | supported | automatic, manual, sequential automatic, manual multiple | supported, optional | American Express, Cartes Bancaires, Diners Club, Discover, Interac, JCB, Maestro, Mastercard, UnionPay, Visa | - | - |
| card redirect | Benefit | not supported | supported | automatic, sequential automatic | not applicable | - | - | - |
| card redirect | KNET | not supported | supported | automatic, sequential automatic | not applicable | - | - | - |
| card redirect | MoMo ATM | not supported | supported | automatic, sequential automatic | not applicable | - | - | - |
| gift card | Givex | not supported | supported | automatic, manual, sequential automatic | not applicable | - | - | - |
| gift card | PaySafeCard | not supported | supported | automatic, sequential automatic | not applicable | - | 46 ([full list](https://hyperswitch.io/pm-list)) | 27 ([full list](https://hyperswitch.io/pm-list)) |
| pay later | Affirm | not supported | supported | automatic, manual, sequential automatic, manual multiple | not applicable | - | USA | USD |
| pay later | Afterpay Clearpay | not supported | supported | automatic, manual, sequential automatic, manual multiple | not applicable | - | 8 ([full list](https://hyperswitch.io/pm-list)) | GBP |
| pay later | Alma | not supported | supported | automatic, manual, sequential automatic | not applicable | - | - | - |
| pay later | Atome | not supported | supported | automatic, sequential automatic | not applicable | - | MYS, SGP | MYR, SGD |
| pay later | Klarna | supported | supported | automatic, manual, sequential automatic | not applicable | - | 22 ([full list](https://hyperswitch.io/pm-list)) | 12 ([full list](https://hyperswitch.io/pm-list)) |
| pay later | PayBright | not supported | supported | automatic, manual, sequential automatic, manual multiple | not applicable | - | CAN | CAD |
| pay later | Walley | not supported | supported | automatic, manual, sequential automatic | not applicable | - | DNK, FIN, NOR, SWE | DKK, EUR, NOK, SEK |
| voucher | Alfamart | not supported | supported | automatic, sequential automatic | not applicable | - | IDN | IDR |
| voucher | Boleto Bancário | not supported | not supported | automatic, sequential automatic | not applicable | - | BRA | BRL |
| voucher | FamilyMart | not supported | not supported | automatic, sequential automatic | not applicable | - | JPN | JPY |
| voucher | Indomaret | not supported | supported | automatic, sequential automatic | not applicable | - | IDN | IDR |
| voucher | Lawson | not supported | not supported | automatic, sequential automatic | not applicable | - | JPN | JPY |
| voucher | Mini Stop | not supported | not supported | automatic, sequential automatic | not applicable | - | JPN | JPY |
| voucher | OXXO | not supported | not supported | automatic, sequential automatic | not applicable | - | MEX | MXN |
| voucher | PayEasy | not supported | not supported | automatic, sequential automatic | not applicable | - | JPN | JPY |
| voucher | Seicomart | not supported | not supported | automatic, sequential automatic | not applicable | - | JPN | JPY |
| voucher | 7-Eleven | not supported | not supported | automatic, sequential automatic | not applicable | - | JPN | JPY |
| wallet | Alipay | not supported | supported | automatic, sequential automatic | not applicable | - | 28 ([full list](https://hyperswitch.io/pm-list)) | 13 ([full list](https://hyperswitch.io/pm-list)) |
| wallet | AlipayHK | not supported | supported | automatic, sequential automatic | not applicable | - | HKG | HKD |
| wallet | Apple Pay | supported | supported | automatic, manual, sequential automatic, manual multiple | not applicable | - | 40 ([full list](https://hyperswitch.io/pm-list)) | 59 ([full list](https://hyperswitch.io/pm-list)) |
| wallet | DANA | supported | supported | automatic, sequential automatic | not applicable | - | - | - |
| wallet | GCash | supported | supported | automatic, sequential automatic | not applicable | - | PHL | PHP |
| wallet | GoPay | supported | supported | automatic, sequential automatic | not applicable | - | IDN | IDR |
| wallet | Google Pay | supported | supported | automatic, manual, sequential automatic, manual multiple | not applicable | - | 33 ([full list](https://hyperswitch.io/pm-list)) | 58 ([full list](https://hyperswitch.io/pm-list)) |
| wallet | KakaoPay | supported | supported | automatic, sequential automatic | not applicable | - | KOR | KRW |
| wallet | MB WAY | not supported | supported | automatic, sequential automatic | not applicable | - | PRT | EUR |
| wallet | MobilePay | not supported | supported | automatic, manual, sequential automatic, manual multiple | not applicable | - | DNK, FIN | DKK, EUR, NOK, SEK |
| wallet | MoMo | supported | supported | automatic, sequential automatic | not applicable | - | VNM | VND |
| wallet | PayPal | supported | supported | automatic, manual, sequential automatic, manual multiple | not applicable | - | 46 ([full list](https://hyperswitch.io/pm-list)) | 23 ([full list](https://hyperswitch.io/pm-list)) |
| wallet | Paze | not supported | supported | automatic, manual, sequential automatic | not applicable | - | - | - |
| wallet | Samsung Pay | not supported | supported | automatic, manual, sequential automatic | not applicable | - | - | - |
| wallet | Swish | not supported | supported | automatic, sequential automatic | not applicable | - | SWE | SEK |
| wallet | Touch 'n Go | not supported | supported | automatic, sequential automatic | not applicable | - | MYS | MYR |
| wallet | TWINT | supported | supported | automatic, manual, sequential automatic | not applicable | - | - | - |
| wallet | Vipps | supported | supported | automatic, manual, sequential automatic, manual multiple | not applicable | - | - | - |
| wallet | WeChat Pay | not supported | supported | automatic, sequential automatic | not applicable | - | 26 ([full list](https://hyperswitch.io/pm-list)) | 10 ([full list](https://hyperswitch.io/pm-list)) |


### Connector-Specific Notes

- **Webhook verification:** Adyen uses HMAC-SHA256 signature verification. The HMAC key is found in your Adyen dashboard under **Developers → Webhooks → your webhook → HMAC key**. This key is stored in Hyperswitch and used to verify the `HmacSignature` field in every incoming Adyen notification. See [Adyen HMAC documentation](https://docs.adyen.com/development-resources/webhooks/verify-hmac-signatures/#enable-hmac-signatures) for setup steps.
- **Raw card data:** Adyen requires explicit enablement of raw card data handling. Contact Adyen support at support@adyen.com to enable this for your account before using Hyperswitch to process card payments directly.
- **Klarna via Adyen — mandatory fields:** For Klarna payments routed through Adyen, the following fields must be present on the payment request: `email`, `billing.first_name`, `billing.last_name`, `billing.city`, `billing.country`, `billing.line1`, `billing.line2`, `billing.zip`, and `order_details`. Additionally, `customer_id` is required — create a customer first via the [Hyperswitch Create Customer API](https://api-reference.hyperswitch.io/v1/customers/customers--create).
- **Sandbox capture behaviour for Klarna and PayPal:** In Adyen's sandbox environment, Automatic Capture does not work as intended for Klarna and PayPal — payments must be explicitly captured before refunds can be processed. This is an Adyen sandbox account configuration issue, not a Hyperswitch bug. If this persists in production, contact Adyen support to disable automatic captures for these methods.
- **Sofort deprecation:** Adyen has discontinued support for Sofort as a payment method. The Hyperswitch–Adyen integration retains the Sofort implementation but its availability depends on your Adyen account configuration. Contact Adyen support if Sofort is not functioning as expected.
- For a full list of supported payment methods, visit [hyperswitch.io/pm-list](https://hyperswitch.io/pm-list).

### Webhooks

Adyen recognizes 34 named webhook event codes. Four are active only when payout support is enabled. Incoming names follow the enum's `SCREAMING_SNAKE_CASE` serialization. The event set comes from [`WebhookEventCode`](https://github.com/juspay/hyperswitch/blob/f35edab780c97dd12efdd366246ff3f7fbc0e940/crates/hyperswitch_connectors/src/connectors/adyen/transformers.rs#L5606-L5650), and the effects come from [`get_adyen_webhook_event()`](https://github.com/juspay/hyperswitch/blob/f35edab780c97dd12efdd366246ff3f7fbc0e940/crates/hyperswitch_connectors/src/connectors/adyen/transformers.rs#L5719-L5883).

| Incoming event | Source variant | Effect |
|---|---|---|
| `AUTHORISATION` | `Authorisation` | Payment succeeds or fails according to the event's success value. |
| `AUTHORISATION_ADJUSTMENT` | `AuthorisationAdjustment` | Authorization extension succeeds or fails according to the event's success value. |
| `REFUND` | `Refund` | Refund succeeds or fails according to the event's success value. |
| `CANCEL_OR_REFUND` | `CancelOrRefund` | Refund succeeds or fails according to the event's success value. |
| `CANCELLATION` | `Cancellation` | Payment cancellation succeeds or fails according to the event's success value. |
| `CAPTURE` | `Capture` | Capture succeeds or fails according to the event's success value. |
| `CAPTURE_FAILED` | `CaptureFailed` | Capture fails. |
| `REFUND_FAILED` | `RefundFailed` | Refund fails. |
| `REFUNDED_REVERSED` | `RefundedReversed` | Refund moves to review. |
| `NOTIFICATION_OF_CHARGEBACK` | `NotificationOfChargeback` | Dispute opens. |
| `CHARGEBACK` | `Chargeback` | Dispute opens, is accepted, is won, or is lost according to the dispute status. |
| `CHARGEBACK_REVERSED` | `ChargebackReversed` | Dispute is challenged when pending; otherwise, the dispute is won. |
| `SECOND_CHARGEBACK` | `SecondChargeback` | Dispute is lost. |
| `PREARBITRATION_WON` | `PrearbitrationWon` | Dispute is won. |
| `PREARBITRATION_LOST` | `PrearbitrationLost` | Dispute is lost. |
| `REQUEST_FOR_INFORMATION` | `RequestForInformation` | Dispute opens or expires according to the dispute status. |
| `NOTIFICATION_OF_FRAUD` | `NotificationOfFraud` | No payment, refund, or dispute state update. |
| `INFORMATION_SUPPLIED` | `InformationSupplied` | Dispute is challenged when responded; otherwise, the dispute opens. |
| `PREARBITRATION_OPEN` | `PrearbitrationOpen` | Dispute opens. |
| `PREARBITRATION_ACCEPTED` | `PrearbitrationAccepted` | Dispute is accepted. |
| `PREARBITRATION_DECLINED` | `PrearbitrationDeclined` | Dispute is challenged. |
| `PREARBITRATION_ISSUER_WITHDRAWN` | `PrearbitrationIssuerWithdrawn` | Dispute is won. |
| `SCHEME_ARBITRATION` | `SchemeArbitration` | Dispute opens. |
| `SCHEME_ARBITRATION_WON` | `SchemeArbitrationWon` | Dispute is won. |
| `SCHEME_ARBITRATION_LOST` | `SchemeArbitrationLost` | Dispute is lost. |
| `DISPUTE_DEFENSE_PERIOD_ENDED` | `DisputeDefensePeriodEnded` | Dispute is accepted or lost according to the dispute status. |
| `ISSUER_RESPONSE_TIMEFRAME_EXPIRED` | `IssuerResponseTimeframeExpired` | Dispute is won. |
| `ISSUER_COMMENTS` | `IssuerComments` | No payment, refund, or dispute state update. |
| `OFFER_CLOSED` | `OfferClosed` | Payment expires. |
| `RECURRING_CONTRACT` | `RecurringContract` | Payment succeeds or fails according to the event's success value. |
| `PAYOUT_THIRDPARTY` | `PayoutThirdparty` | Payout is created when payout support is enabled. |
| `PAYOUT_DECLINE` | `PayoutDecline` | Payout fails when payout support is enabled. |
| `PAYOUT_EXPIRE` | `PayoutExpire` | Payout expires when payout support is enabled. |
| `PAYOUT_REVERSED` | `PayoutReversed` | Payout is reversed when payout support is enabled. |

Hyperswitch verifies each webhook by calculating an HMAC-SHA256 signature over the notification fields and comparing it with the supplied HMAC signature. Configure the HMAC key from the Adyen dashboard in your connector webhook settings. See [`verify_webhook_source()`](https://github.com/juspay/hyperswitch/blob/f35edab780c97dd12efdd366246ff3f7fbc0e940/crates/hyperswitch_connectors/src/connectors/adyen.rs#L2061-L2097).

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

**Hyperswitch owns:** routing decisions, retry scheduling, mandate record storage, and webhook fan-out to your endpoint. **Adyen owns:** payment execution, fraud decisioning, payment method availability, and webhook delivery to Hyperswitch's endpoint.

**Hyperswitch owns:** capture orchestration, including when and how much to capture. **Adyen owns:** execution of each capture call against the original authorization.

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
