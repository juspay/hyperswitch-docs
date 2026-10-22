---
description: >-
  Save a customer's payment method for their next checkout, or to charge them
  later while they are away
icon: repeat
metaLinks:
  alternates:
    - ./
---

<!-- truth manifest; hyperswitch 52e9e9e69df823a667dcc2dac1fef3b0df5129a4
     symbols: recurring_details is a tagged enum (type, data, snake_case) with nine variants = crates/api_models/src/mandates.rs:165-209
     symbols: off_session request field, "when making a recurring payment ... this parameter is mandatory" = crates/api_models/src/payments.rs:1320-1323
     symbols: payment_method_id and network_transaction_id are fields of the v1 payment response, so they arrive on create, confirm and retrieve = crates/api_models/src/payments.rs:7529,7980-7988
     symbols: a request carrying recurring_details or mandate_id is validated as a recurring mandate transaction; payment_method_id and mandate_id require customer_id, confirm true ("`confirm` must be `true` for mandates") and off_session true ("`off_session` should be `true` for mandates"); the other seven variants skip those checks = crates/router/src/core/payments/helpers.rs:1209-1231,1425-1455
     symbols: recurring_details cannot be combined with mandate_data, payment_token or mandate_id = crates/router/src/core/payments/helpers.rs:1216,1233-1255
     symbols: payment_method_id MIT loads the saved method (PaymentMethodNotFound otherwise) and rejects a customer_id that is not the saved method's owner ("customer_id must match mandate customer_id") = crates/router/src/core/payments/helpers.rs:571-600,1504-1519
     symbols: public errors: PaymentMethodNotFound is HTTP 404 HE_02 "Payment method does not exist in our records"; IncorrectPaymentMethodConfiguration is HTTP 400 IR_39 "No eligible connector was found for the current payment method configuration", raised when no connector passes the NTID MIT filter = crates/hyperswitch_domain_models/src/errors/api_error_response.rs:467-469,693-695; crates/router/src/core/payments.rs:11768-11774
     symbols: processor_payment_token with merchant_connector_id resolves that connector account (MerchantConnectorAccountNotFound otherwise); routing classifies the payment as ppt_mandate = crates/router/src/core/payments/helpers.rs:500-549; crates/router/src/core/payments/routing.rs:280-290
     symbols: the five NTID-based variants are eligible only for connectors in network_transaction_id_supported_connectors; card_with_limited_data only for card_only_mit_supported_connectors; payment_method_id, mandate_id and processor_payment_token are not proxy flows = crates/router/src/core/payments.rs:11778-11809; config/deployments/production.toml:336-340
     symbols: mandate_data requires setup_future_usage off_session = crates/router/src/core/payments/helpers.rs:9277-9291
     symbols: a mandate record needs mandate_data, customer_id and customer_acceptance = crates/router/src/core/payments/helpers.rs:4840-4863
     symbols: decrypted wallet token variant fields: decrypted_token, token_exp_month, token_exp_year, card_holder_name, network_transaction_id, transaction_link_id, eci, token_source = crates/common_types/src/payments.rs:1307-1345
     symbols: VaultCardData.card_number carries the vault alias; expiry required; holder name, issuer, network, type, issuing country, bank code, nick name, bin_number, last_four optional = crates/api_models/src/mandates.rs:487-552
     symbols: NetworkTransactionIdAndVaultCardDetails = vault_card_data, network_transaction_id, transaction_link_id (optional, Mastercard TLID) = crates/api_models/src/mandates.rs:559-575
     symbols: NetworkTokenWithVaultCardFallback = network_token (NetworkTokenDetails, no NTID or cryptogram), network_transaction_id shared by both arms, transaction_link_id optional, vault_card_data = crates/api_models/src/mandates.rs:430-485,583-603
     symbols: the fallback wrapper is checked ahead of the single-core gates on both create and confirm = crates/router/src/routes/payments.rs:2863-2880
     symbols: fallback runs the network token arm, then at most once the vault card arm as a fresh attempt on the same payment_id through the external vault proxy confirm operation; the caller receives the last arm's response = crates/router/src/core/payments.rs:4040-4154
     symbols: fallback eligibility: token arm status failed, connector on the external vault proxy path, profile is_clear_pan_retries_enabled true (unreadable profile counts as off), GSM row for the decline decides Retry with clear_pan_possible = crates/router/src/core/payments.rs:3931-4026
     symbols: is_clear_pan_retries_enabled on profile create, profile response and profile update; the same flag gates clear-PAN auto retries = crates/api_models/src/admin.rs:2546,2933,3336; crates/router/src/core/payments/retry.rs:181-191
     symbols: list a customer's saved payment methods = crates/router/src/routes/app.rs:1583-1584
     symbols: off_session is downgraded to on_session when the connector is not in mandates.supported_payment_methods for the payment method type; the applied value is recorded on the attempt and returned as setup_future_usage on create, confirm and retrieve = crates/router/src/core/payments/flows/authorize_flow.rs:941-970; crates/router/src/core/payments/operations/payment_response.rs:723-725; crates/hyperswitch_domain_models/src/payments/payment_attempt.rs:1822-1830; crates/router/src/core/payments/transformers.rs:3862,4393-4395; config/deployments/production.toml:294-300
     symbols: missing customer_id on a payment_method_id MIT is IR_04 "Missing required param: customer_id" = crates/router/src/core/payments/helpers.rs:1440; crates/hyperswitch_domain_models/src/errors/api_error_response.rs:575-577
     symbols: processor-token MIT refuses a currency different from the saving payment, HE_03 "Cross currency mandates not supported" = crates/router/src/core/payments.rs:12775-12783; crates/hyperswitch_domain_models/src/errors/api_error_response.rs:513-515
     symbols: a saved-method MIT builds per-connector charge options in order processor mandate, network token with NTID, card with NTID; the first connector with any option is used, else IR_39 = crates/router/src/core/payments.rs:12657-12699,13159-13215
     symbols: mandate_id MIT also requires the mandate to belong to the merchant (HE_02 "Mandate does not exist in our records"), be active (IR_16 "mandate is not active"), and stay within mandate amount and currency (HE_03) = crates/router/src/core/payments/helpers.rs:830-905,1458-1500; crates/hyperswitch_domain_models/src/errors/api_error_response.rs:488-490
     symbols: processor_payment_token with merchant_connector_id pins routing to that connector account; without it the first eligible routed connector is used = crates/router/src/core/payments/routing.rs:1265-1289; crates/router/src/core/payments.rs:12574-12598
     symbols: card_with_limited_data has no merchant-level switch in code; the enforced gate is card_only_mit_supported_connectors = crates/api_models/src/mandates.rs:199-203; crates/router/src/core/payments.rs:11794-11800
     symbols: the five NTID-based variants dispatch through the proxy path = crates/router/src/routes/payments/helpers.rs:101-118
     symbols: NTID-based types skip the saved-method lookup and the customer_id check; payment_method is not required on the proxy connector-call path = crates/router/src/core/payments/helpers.rs:497-499,1431-1437,5052-5075; crates/router/src/core/payments.rs:7774-7988
     symbols: test fixture for an NTID card charge sends amount, currency, confirm, off_session, payment_method card and recurring_details, no customer_id = cypress-tests/cypress/fixtures/create-ntid-mit.json
     symbols: customer_id is required only for payment_method_id and mandate_id, for requests that set setup_future_usage, and on the permanent-token vault paths; not for the NTID card type = crates/router/src/core/payments/helpers.rs:1325-1336,1439,3089,3241
     symbols: vault-card MIT dispatches to the external vault proxy confirm operation; the processor request is sent through the vault's proxy (VGS proxy_url or Hyperswitch Vault endpoint), Tokenex rejected = crates/router/src/routes/payments/helpers.rs:122-131; crates/router/src/core/payments/flows/external_proxy_flow.rs:507-545; crates/router/src/core/unified_connector_service.rs:3010-3120; crates/api_models/src/enums.rs:287-291
     symbols: the profile's external_vault_connector_details.vault_connector_id is required, else InternalServerError "mca_id not present for external vault" = crates/router/src/core/payments.rs:7339-7346; crates/api_models/src/admin.rs:2596-2599
     symbols: both fallback arms are built from one payload and share network_transaction_id and transaction_link_id = crates/api_models/src/mandates.rs:621-640
     symbols: the decline-code mapping (GSM) is admin-key only, not merchant-configurable = crates/router/src/routes/gsm.rs:11; crates/router/src/routes/app.rs:2838
     symbols: the fallback's vault arm runs the external-vault prerequisites, so it needs external_vault_connector_details on the profile like the vault-card type = crates/router/src/core/payments.rs:2183,7339-7346
     symbols: the processor sees a mandate setup only when customer_acceptance is present and setup_future_usage is off_session = crates/hyperswitch_connectors/src/utils.rs:2455-2460
     symbols: payment_method_id and network_transaction_id on the response come from the attempt and are set after the save step, so they are null on an unconfirmed create = crates/router/src/core/payments/transformers.rs:4507-4508; crates/router/src/core/payments/operations/payment_response.rs:349,907
     checked: 2026-10-22 -->

# Saving Payment Method

A customer has paid you once. Saving their payment method lets you charge the same card or wallet again without asking them to type it in. Hyperswitch supports two kinds of reuse, and you pick one with the `setup_future_usage` field on the payment that saves the method.

| You want to                                                                       | Who is present next time               | Set on the saving payment         | What you send next time                                                                             |
| --------------------------------------------------------------------------------- | -------------------------------------- | --------------------------------- | --------------------------------------------------------------------------------------------------- |
| Let the customer pay faster at their next checkout                               | The customer, on your site or app      | `setup_future_usage: on_session`  | Nothing special. The saved method shows up in the checkout, and the customer enters CVV or does 3DS. |
| Charge the customer while they are away: a subscription, a usage bill, a delayed charge | Nobody. Your server starts the charge. | `setup_future_usage: off_session` | `off_session: true` plus a `recurring_details` object that says which saved method to charge.       |

The card networks have names for these. The first is a Card-on-File Customer Initiated Transaction (COF-CIT). The second is a Merchant Initiated Transaction (MIT).

If the processor cannot run merchant-initiated charges for that payment method, Hyperswitch still saves it, but as `on_session`, and the payment response's `setup_future_usage` comes back as `on_session`. Check that field before relying on the method for later charges.

Both need the customer's consent to store the method. If you use the Hyperswitch SDK, the consent comes from the "save this card" checkbox. If you build your own form, send `customer_acceptance` on the create or confirm call, as shown below.

***

### Save a payment method for the customer's next checkout (COF-CIT)

Use this when the same customer comes back and pays again themselves. They skip re-entering the card, which is faster and avoids typos, but they still authenticate: they enter the CVV or complete 3DS. This guide uses cards as the example.

<details>

<summary>Follow steps for SDK integration</summary>

Create the payment with `setup_future_usage` set to `on_session`.

<pre class="language-bash"><code class="lang-bash">curl --location 'https://sandbox.hyperswitch.io/payments' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'api-key: &#x3C;enter your Hyperswitch API key here>' \
--data-raw '{
    "amount": 6540,
    "currency": "USD",
    "profile_id": "&#x3C;enter the relevant profile id>",
<strong>    "setup_future_usage": "on_session",
</strong>    "customer_id": "customer123",
    "description": "My first payment request",
    "return_url": "https://example.com"
}'
</code></pre>

{% hint style="info" %}
**Note:** The checkout shows the save checkbox by default. If you have turned [`displaySavedPaymentMethodsCheckbox`](../../../payment-experience/payment/web/customization.md) off in your SDK configuration, the customer cannot consent and nothing is saved.
{% endhint %}

When the customer ticks the checkbox, the SDK sends `customer_acceptance` on the confirm call for you.

<figure><img src="../../../../.gitbook/assets/Screenshot 2024-04-18 at 12.49.35 PM.png" alt="" width="375"><figcaption><p>The customer's consent to save their card is expressed through this checkbox</p></figcaption></figure>

</details>

<details>

<summary>Follow steps for API integration</summary>

**Step 1.** Create the payment with `setup_future_usage` set to `on_session`.

<pre class="language-bash"><code class="lang-bash">curl --location 'https://sandbox.hyperswitch.io/payments' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'api-key: &#x3C;enter your Hyperswitch API key here>' \
--data-raw '{
    "amount": 6540,
    "currency": "USD",
    "profile_id": "&#x3C;enter the relevant profile id>",
<strong>    "setup_future_usage": "on_session",
</strong>    "customer_id": "customer123",
    "description": "My first payment request",
    "return_url": "https://example.com"
}'
</code></pre>

**Step 2.** Confirm the payment with the card details and the customer's consent to store the card.

<pre class="language-bash"><code class="lang-bash">curl --location 'https://sandbox.hyperswitch.io/payments/&#x3C;pass the payment_id>/confirm' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'api-key: &#x3C;enter your Hyperswitch API key here>' \
--data-raw '{
    "payment_method": "card",
    "payment_method_data": {
        "card": {
            "card_number": "4242424242424242",
            "card_exp_month": "10",
            "card_exp_year": "28",
            "card_holder_name": "joseph Doe",
            "card_cvc": "123"
        }
    },
<strong>    "customer_acceptance": {
        "acceptance_type": "online",
        "accepted_at": "2026-10-22T10:15:00.000Z",
        "online": {
            "ip_address": "203.0.113.10",
            "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Safari/605.1.15"
        }
    }
</strong>}'
</code></pre>

</details>

***

### Save a payment method to charge the customer later (MIT)

Use this when you will charge the customer without them being there: a monthly subscription, a usage-based bill, a charge after delivery. The amount and timing are up to you.

An MIT needs no customer authentication because the processor can point the card network to an earlier payment where the customer agreed to future charges. Sending `setup_future_usage: off_session` together with `customer_acceptance` on that first payment is what tells the processor to set up the agreement. Hyperswitch stores the reference and passes it on every later charge. Depending on the processor, Apple Pay and Google Pay can be saved this way too.

The payment response carries two values you may want to keep:

* **`payment_method_id`**: the ID Hyperswitch assigns to the saved method. Send it on every later charge. It is set once the payment is confirmed and the method is saved, so read it from the confirm response or from `GET /payments/{payment_id}`. On a create call without `confirm`, it is still null.

* **`network_transaction_id`**: the card network's reference for the saving transaction. You only need it if you are PCI compliant and plan to hold the card data yourself. See [Charge a card you store yourself](#charge-a-card-you-store-yourself-pci-compliant-merchants).

<details>

<summary>Follow steps for SDK integration</summary>

Create the payment with `setup_future_usage` set to `off_session`.

<pre class="language-bash"><code class="lang-bash">curl --location 'https://sandbox.hyperswitch.io/payments' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'api-key: &#x3C;enter your Hyperswitch API key here>' \
--data-raw '{
    "amount": 6540,
    "currency": "USD",
    "profile_id": "&#x3C;enter the relevant profile id>",
<strong>    "setup_future_usage": "off_session",
</strong>    "customer_id": "customer123",
    "description": "My first payment request",
    "return_url": "https://example.com"
}'
</code></pre>

When the customer ticks the "save" checkbox, the SDK sends `customer_acceptance` on the confirm call for you.

{% hint style="info" %}
**Note:** The checkout shows the save checkbox by default. If you have turned [`displaySavedPaymentMethodsCheckbox`](../../../payment-experience/payment/web/customization.md) off in your SDK configuration, the customer cannot consent and nothing is saved.
{% endhint %}

Once the payment succeeds, read `payment_method_id` from the payment and store it against the customer. You can get it from the confirm response or by retrieving the payment:

```bash
curl --location 'https://sandbox.hyperswitch.io/payments/<pass the payment_id>' \
--header 'Accept: application/json' \
--header 'api-key: <enter your Hyperswitch API key here>'
```

</details>

<details>

<summary>Follow steps for API integration</summary>

**Step 1.** Create the payment with `setup_future_usage` set to `off_session`.

<pre class="language-bash"><code class="lang-bash">curl --location 'https://sandbox.hyperswitch.io/payments' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'api-key: &#x3C;enter your Hyperswitch API key here>' \
--data-raw '{
    "amount": 6540,
    "currency": "USD",
    "profile_id": "&#x3C;enter the relevant profile id>",
<strong>    "setup_future_usage": "off_session",
</strong>    "customer_id": "customer123",
    "description": "My first payment request",
    "return_url": "https://example.com"
}'
</code></pre>

**Step 2.** Confirm the payment with the card details and the customer's consent to store the card.

<pre class="language-bash"><code class="lang-bash">curl --location 'https://sandbox.hyperswitch.io/payments/&#x3C;pass the payment_id>/confirm' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'api-key: &#x3C;enter your Hyperswitch API key here>' \
--data-raw '{
    "payment_method": "card",
    "payment_method_data": {
        "card": {
            "card_number": "4242424242424242",
            "card_exp_month": "10",
            "card_exp_year": "28",
            "card_holder_name": "joseph Doe",
            "card_cvc": "123"
        }
    },
<strong>    "customer_acceptance": {
        "acceptance_type": "online",
        "accepted_at": "2026-10-22T10:15:00.000Z",
        "online": {
            "ip_address": "203.0.113.10",
            "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Safari/605.1.15"
        }
    }
</strong>}'
</code></pre>

**Step 3.** Once the payment succeeds, read `payment_method_id` from the confirm response and store it against the customer. You can also retrieve the payment later to get it:

```bash
curl --location 'https://sandbox.hyperswitch.io/payments/<pass the payment_id>' \
--header 'Accept: application/json' \
--header 'api-key: <enter your Hyperswitch API key here>'
```

</details>

***

### Charge a saved payment method

When it is time to charge, create a payment with `confirm: true`, `off_session: true`, the customer the method belongs to, and the `payment_method_id` inside `recurring_details`. No card data and no customer interaction are involved.

<pre class="language-bash"><code class="lang-bash">curl --location 'https://sandbox.hyperswitch.io/payments' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'api-key: &#x3C;enter your Hyperswitch API key here>' \
--data-raw '{
    "amount": 6540,
    "currency": "USD",
    "profile_id": "&#x3C;enter the relevant profile id>",
    "customer_id": "customer123",
    "confirm": true,
<strong>    "off_session": true,
    "recurring_details": {
        "type": "payment_method_id",
        "data": "pm_lmTnIO5EdCiiMgRPrV9x"
    }
</strong>}'
</code></pre>

A few rules apply to this request:

* **`customer_id` is required and must be the customer the method was saved for.** Leaving it out returns HTTP 400, code `IR_04`, "Missing required param: customer_id". A different customer is rejected with `customer_id must match mandate customer_id`. An unknown `payment_method_id` returns HTTP 404, code `HE_02`, "Payment method does not exist in our records".
* **`confirm` and `off_session` must both be `true`.** Otherwise the request is rejected with `` `confirm` must be `true` for mandates `` or `` `off_session` should be `true` for mandates ``.
* **Send `recurring_details` on its own.** It cannot be combined with `mandate_data`, `payment_token` or `mandate_id` in the same request.
* **Keep the currency the same as the saving payment.** When Hyperswitch charges with the processor token, a different currency is refused with HTTP 400, code `HE_03`, "Mandate Validation Failed", reason "Cross currency mandates not supported".

Hyperswitch decides which credential to charge with, based on what is enabled for your account: a processor token, a network token with the network transaction ID, or the card with the network transaction ID, in that order of preference. If none of the processors your routing picks can charge the method, for example because the MIT is routed to a processor that never saw the card, the request fails with HTTP 400, code `IR_39`, "No eligible connector was found for the current payment method configuration". To let MITs run on a different processor from the one that saved the method, see [Connector-agnostic MIT routing](../recurring-payments.md#connector-agnostic-mit-routing).

To see every method saved for a customer, call [List Customer Payment Methods](https://api-reference.hyperswitch.io/v1/payment-methods/list-payment-methods-for-a-customer):

```bash
curl --request GET \
  --url https://sandbox.hyperswitch.io/customers/{customer_id}/payment_methods \
  --header 'api-key: <api-key>'
```

***

### Which `recurring_details` type to send

`recurring_details` tells Hyperswitch what you are holding on your side. It always has a `type` and a `data` value: a string for the two ID types, an object for the rest. Pick the row that matches what you have.

| What you hold                                                      | `type`                                                     | What goes in `data`                                                                             | Good to know                                                                                                                                               |
| ------------------------------------------------------------------ | ---------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| A `payment_method_id` from Hyperswitch                             | `payment_method_id`                                        | The ID as a string                                                                              | The default. See [Charge a saved payment method](#charge-a-saved-payment-method).                                                                          |
| A `mandate_id` from Hyperswitch                                    | `mandate_id`                                               | The ID as a string                                                                              | For methods saved through the older `mandate_data` flow. Same rules as `payment_method_id`, plus the mandate must be active and the charge must stay within the mandate's amount and currency. |
| A token your processor issued for this customer                    | `processor_payment_token`                                  | `processor_payment_token`, and optionally `merchant_connector_id`                               | Pass `merchant_connector_id` to send the charge to the connector account that issued the token. Without it, the token goes to whichever processor your routing picks first. |
| The card itself, plus its network transaction ID                   | `network_transaction_id_and_card_details`                  | Card number, expiry, `network_transaction_id`, optional `transaction_link_id` and card descriptors | For PCI-compliant merchants. See [Charge a card you store yourself](#charge-a-card-you-store-yourself-pci-compliant-merchants).                            |
| The card itself, with no network transaction ID                    | `card_with_limited_data`                                   | Card number; expiry, holder name, `eci`, `network_transaction_id` and `transaction_link_id` optional | Must be enabled for your account.Ask Hyperswitch support before relying on it.                        |
| A network token for the card                                       | `network_transaction_id_and_network_token_details`         | `network_token`, `token_exp_month`, `token_exp_year`, `network_transaction_id`, optional descriptors | Routed like the card-plus-ID case.                                                                                                                         |
| A decrypted Apple Pay or Google Pay token                          | `network_transaction_id_and_decrypted_wallet_token_details` | `decrypted_token`, `token_exp_month`, `token_exp_year`, `network_transaction_id`, optional `token_source`, `eci`, `transaction_link_id`, `card_holder_name` | Routed like the card-plus-ID case.                                                                                                                         |
| An alias for the card in an external vault, plus its network transaction ID | `network_transaction_id_and_vault_card_details`            | `vault_card_data`, `network_transaction_id`, optional `transaction_link_id`                     | See [MIT with an externally vaulted card](#mit-with-an-externally-vaulted-card).                                                                           |
| A network token and a vault alias for the same card                | `network_token_with_vault_card_fallback`                   | `network_token`, `network_transaction_id`, optional `transaction_link_id`, `vault_card_data`     | Token first, card alias if the token is declined. See [MIT with a network token and external vault card fallback](#mit-with-a-network-token-and-external-vault-card-fallback). |

**Where the charge can go.** The first three rows go to the processor tied to the saved method or token, except that `payment_method_id` can reach other processors when connector-agnostic MIT is on. The rows that carry a network transaction ID can only be routed to processors that accept it. On Hyperswitch Cloud those are Adyen, Archipel, Authorize.net, Checkout, Cybersource, Stripe, Nuvei, Worldpay Vantiv, Revolv3, Peach Payments and TSYS Transit. `card_with_limited_data` is narrower still: Peach Payments only. Self-hosted deployments can change both lists in their deployment configuration. If none of your configured processors is on the list, the payment fails with HTTP 400, code `IR_39`, "No eligible connector was found for the current payment method configuration". Some processors also need the network transaction ID feature switched on at their end; see the note under [Network Transaction ID with Card Data](../recurring-payments.md#network-transaction-id-with-card-data).

The [confirm payment API reference](https://api-reference.hyperswitch.io/v1/payments/payments--confirm) has the full field list for each type.

***

### Charge a card you store yourself (PCI-compliant merchants)

If you are PCI compliant and keep the customer's card data in your own systems, you do not need Hyperswitch to have saved the method. Pass the card and the `network_transaction_id` you received when the customer first paid. The card network treats this as a continuation of that first transaction, so no customer authentication is needed.

<pre class="language-bash"><code class="lang-bash">curl --location 'https://sandbox.hyperswitch.io/payments' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'api-key: &#x3C;enter your Hyperswitch API key here>' \
--data-raw '{
    "amount": 6540,
    "currency": "USD",
    "profile_id": "&#x3C;enter the relevant profile id>",
    "confirm": true,
    "off_session": true,
    "payment_method": "card",
<strong>    "recurring_details": {
        "type": "network_transaction_id_and_card_details",
        "data": {
            "card_number": "4242424242424242",
            "card_exp_month": "10",
            "card_exp_year": "28",
            "card_holder_name": "joseph Doe",
            "network_transaction_id": "MCC5ZRGMI0925"
        }
    }
</strong>}'
</code></pre>

For Mastercard, also pass `transaction_link_id` when you have it. The request is routed only to processors that accept network transaction IDs, as listed above. You do not need `customer_id` for this type, since Hyperswitch is not looking up anything it has saved.

***

### MIT with an externally vaulted card

If the customer's card lives in an external vault that you connect to Hyperswitch, you hold an alias for the card number rather than the number itself. You can run an MIT with that alias: Hyperswitch sends the processor request through your vault's proxy, which swaps the alias for the real card number on the way out. Neither your systems nor Hyperswitch see the number. See [Connect external vaults to Hyperswitch orchestration](../../../workflows/vault/connect-external-vaults-to-hyperswitch-orchestration.md) for the vault setup. Your business profile needs `external_vault_connector_details` set to a VGS or Hyperswitch Vault connector; the vault page above covers that setup.

Send the alias in the `card_number` field of `vault_card_data`, together with the `network_transaction_id` from the first payment. For Mastercard, add `transaction_link_id` when you have it.

<pre class="language-bash"><code class="lang-bash">curl --location 'https://sandbox.hyperswitch.io/payments' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'api-key: &#x3C;enter your Hyperswitch API key here>' \
--data-raw '{
    "amount": 6540,
    "currency": "USD",
    "profile_id": "&#x3C;enter the relevant profile id>",
    "confirm": true,
    "off_session": true,
    "payment_method": "card",
<strong>    "recurring_details": {
        "type": "network_transaction_id_and_vault_card_details",
        "data": {
            "vault_card_data": {
                "card_number": "token_card_number",
                "card_exp_month": "10",
                "card_exp_year": "28",
                "card_holder_name": "joseph Doe"
            },
            "network_transaction_id": "MCC5ZRGMI0925",
            "transaction_link_id": "TL123456789"
        }
    }
</strong>}'
</code></pre>

The `card_number` inside `vault_card_data` is the vault alias, not a card number. `vault_card_data` needs the alias and the expiry. Everything else is optional: `card_holder_name`, `card_network`, `card_issuer`, `card_type`, `card_issuing_country`, `bank_code`, `nick_name`, `bin_number` and `last_four`.

***

### MIT with a network token and external vault card fallback

If you hold both a network token and a vault alias for the same card, you can ask Hyperswitch to try the token first and, if the token is declined for a reason the network treats as safe to retry on the card, charge the vault alias instead. The customer sees one charge, and you make one request.

<pre class="language-bash"><code class="lang-bash">curl --location 'https://sandbox.hyperswitch.io/payments' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'api-key: &#x3C;enter your Hyperswitch API key here>' \
--data-raw '{
    "amount": 6540,
    "currency": "USD",
    "profile_id": "&#x3C;enter the relevant profile id>",
    "confirm": true,
    "off_session": true,
    "payment_method": "card",
<strong>    "recurring_details": {
        "type": "network_token_with_vault_card_fallback",
        "data": {
            "network_token": {
                "network_token": "4604000460040787",
                "token_exp_month": "05",
                "token_exp_year": "28",
                "card_holder_name": "joseph Doe"
            },
            "network_transaction_id": "MCC5ZRGMI0925",
            "transaction_link_id": "TL123456789",
            "vault_card_data": {
                "card_number": "token_card_number",
                "card_exp_month": "10",
                "card_exp_year": "28",
                "card_holder_name": "joseph Doe"
            }
        }
    }
</strong>}'
</code></pre>

The `network_transaction_id` is shared by both attempts, and `transaction_link_id` is optional, for Mastercard. The `card_number` inside `vault_card_data` is the vault alias, not a card number.

**What happens.** Hyperswitch charges the network token. If that attempt ends as `failed`, it checks whether a card retry is allowed. If it is, Hyperswitch runs a second attempt on the same `payment_id` with the vault alias, under the same `network_transaction_id`. The fallback runs at most once, and the response you get is from the last attempt that ran. Both attempts stay on the payment, so you can see the token decline in the payment's attempt list.

**When the fallback runs.** All of these must be true, otherwise a declined token attempt is final:

* **Clear-PAN retries are on for the business profile.** Set `is_clear_pan_retries_enabled` to `true` on the profile create or update API. The same switch controls Hyperswitch's automatic card retries for network-token payments. If the flag is off, or the profile cannot be read, nothing is retried.
* **The decline is one the network allows to be retried on the card.** Hyperswitch keeps a mapping of processor decline codes and only falls back when the code for this decline is marked as retryable on the card. You do not configure this mapping yourself.
* **The processor supports the external vault path, and your profile has a vault connector.** The vault alias attempt uses the same processor as the token attempt, so that processor has to be one Hyperswitch can reach through the external vault, and `external_vault_connector_details` must be set on the business profile as in the section above.

If you only hold a network token and no vault alias, use `network_transaction_id_and_network_token_details` instead; there is no fallback in that case.
