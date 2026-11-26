---
description: Save a customer's payment method for their next checkout, or to charge them later while they are away
icon: repeat
metaLinks:
  alternates:
    - ./
---

# Saving Payment Method

A customer has paid you once. Saving their payment method lets you charge the same card or wallet again without asking them to enter it again. Which kind of saving you need depends on one question: will the customer be there the next time you charge them?

| Will the customer be present next time?                                                   | Set this on the payment that saves the method | What happens next time                                                                                  |
| ----------------------------------------------------------------------------------------- | --------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| Yes. They come back to your site or app and pay again themselves.                        | `setup_future_usage: on_session`              | The saved method shows up at checkout. The customer picks it and enters their CVV or completes 3DS.      |
| No. You charge them while they are away, such as a subscription, a usage bill, or a delayed charge. | `setup_future_usage: off_session`             | Your server starts the charge with `off_session: true` and a `recurring_details` object naming the saved method. |

The card networks have names for these. The first is a Card-on-File Customer Initiated Transaction (COF-CIT). The second is a Merchant Initiated Transaction (MIT). The rest of this page uses those names.

### Saving a payment method for future on-session payments (COF CIT)

Use this when the same customer comes back and pays again themselves. They skip re-entering their card, which is faster and avoids typos, but they still authenticate each time by entering the CVV or completing 3DS.

Whether a saved method can be reused this way depends on the payment method and the processor. Cards are the common case. Wallets such as Apple Pay and most other alternative payment methods usually cannot be saved for on-session reuse.

### To save a customer's payment method used in a successful transaction for future CIT payments:

<details>

<summary>Follow Steps for SDK integration</summary>

Pass the following field in the `/payments` create request to indicate your intention to save the payment method

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
**Note:** Your checkout already shows a "Save this card" checkbox to signed-in customers. You do not need to turn it on. If you have hidden it with [`displaySavedPaymentMethodsCheckbox`](../../../payment-experience/payment/web/customization.md#display-saved-payment-methods-checkbox), the customer has no way to agree, so the card is not saved.
{% endhint %}

When the customer ticks that box, the SDK adds their consent to the confirm call for you. You do not send `customer_acceptance` yourself.

<figure><img src="../../../../.gitbook/assets/Screenshot 2024-04-18 at 12.49.35 PM.png" alt="" width="375"><figcaption><p>The customer's consent to save their card is expressed through this checkbox</p></figcaption></figure>

</details>

<details>

<summary>Follow Steps For API Integration</summary>

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
        "accepted_at": "2026-10-23T10:15:00.000Z",
        "online": {
            "ip_address": "203.0.113.10",
            "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Safari/605.1.15"
        }
    }
</strong>}'
</code></pre>

</details>

***

### Saving a payment method for future MIT payments

Use this when you will charge the customer without them being there: a monthly subscription, a usage-based bill, a charge after delivery. The amount and timing are up to you.

An MIT needs no customer authentication because the processor can point the card network to an earlier payment where the customer agreed to future charges. Sending `setup_future_usage: off_session` together with the customer's consent on that first payment is what sets up the agreement. Hyperswitch stores the reference and passes it on every later charge.

This works for cards on most processors, and for Apple Pay and Google Pay on many of them. Whether a given processor supports it for a given payment method is set in Hyperswitch's deployment configuration. If the processor does not, Hyperswitch still saves the method but as `on_session`, and the payment response's `setup_future_usage` comes back as `on_session`. Check that field before relying on the method for later charges.

#### To save a customer's payment method used in a successful transaction for future MIT payments:

<details>

<summary>Follow Steps for SDK integration</summary>

Pass the following field in the `/payments` create request to indicate your intention to save the payment method

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

When the customer ticks the "Save this card" box, the SDK adds their consent to the confirm call for you. You do not send `customer_acceptance` yourself.

{% hint style="info" %}
**Note:** The checkbox shows by default to signed-in customers. If you have hidden it with [`displaySavedPaymentMethodsCheckbox`](../../../payment-experience/payment/web/customization.md#display-saved-payment-methods-checkbox), the SDK still records consent for a signed-in customer on an off-session payment. The customer is simply not asked, so make sure you have their agreement some other way.
{% endhint %}

Once the payment is confirmed and the method is saved, the response carries two values worth keeping:

* **`payment_method_id`**: the ID Hyperswitch gave the saved method. Send it on every later charge. It is null on a create call without `confirm`, so read it from the confirm response or fetch the payment again.
* **`network_transaction_id`**: the card network's reference for this payment. You only need it if you are PCI compliant and hold the card data yourself. See [Processing MIT payments without a saved payment method](#processing-mit-payments-without-a-saved-payment-method).

```bash
curl --location 'https://sandbox.hyperswitch.io/payments/<pass the payment_id>' \
--header 'Accept: application/json' \
--header 'api-key: <enter your Hyperswitch API key here>'
```

</details>

<details>

<summary>Follow Steps for API integration</summary>

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
        "accepted_at": "2026-10-23T10:15:00.000Z",
        "online": {
            "ip_address": "203.0.113.10",
            "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Safari/605.1.15"
        }
    }
</strong>}'
</code></pre>

Once the payment is confirmed and the method is saved, the response carries two values worth keeping:

* **`payment_method_id`**: the ID Hyperswitch gave the saved method. Send it on every later charge. It is null on a create call without `confirm`, so read it from the confirm response or fetch the payment again.
* **`network_transaction_id`**: the card network's reference for this payment. You only need it if you are PCI compliant and hold the card data yourself. See [Processing MIT payments without a saved payment method](#processing-mit-payments-without-a-saved-payment-method).

```bash
curl --location 'https://sandbox.hyperswitch.io/payments/<pass the payment_id>' \
--header 'Accept: application/json' \
--header 'api-key: <enter your Hyperswitch API key here>'
```

</details>

***

### Using a saved payment method to do a MIT payment

Once the method is saved for off-session use, charge it with one create call. Four fields are mandatory together: the customer who owns the method, `confirm: true`, `off_session: true`, and the saved method's ID in `recurring_details`.

<pre class="language-bash"><code class="lang-bash">curl --location 'https://sandbox.hyperswitch.io/payments' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'api-key: &#x3C;enter your Hyperswitch API key here>' \
--data-raw '{
    "amount": 6540,
    "currency": "USD",
    "profile_id": "&#x3C;enter the relevant profile id>",
<strong>    "customer_id": "customer123",
    "confirm": true,
    "off_session": true,
    "recurring_details": {
        "type": "payment_method_id",
        "data": "pm_lmTnIO5EdCiiMgRPrV9x"
    }
</strong>}'
</code></pre>

What Hyperswitch checks before charging:

* `customer_id` must be present and must be the customer the method was saved for. Missing gives `IR_04`; a different customer gives `IR_16`.
* `confirm` and `off_session` must both be `true`, or the request fails with `IR_16`.
* `recurring_details` cannot be sent together with `payment_token` or `mandate_id`.
* An ID Hyperswitch does not recognise returns `HE_02`.

Use the `payment_method_id` from the confirm response or the retrieve call of the payment that saved the method. To see every method saved for a customer, call [List Customer Payment Methods](https://api-reference.hyperswitch.io/v1/payment-methods/list-payment-methods-for-a-customer):

```bash
curl --request GET \
  --url https://sandbox.hyperswitch.io/customers/{customer_id}/payment_methods \
  --header 'api-key: <api-key>'
```

***

### Processing MIT payments without a saved payment method

If you are PCI compliant and hold the card details yourself, you can charge without a saved method by sending the card and the network transaction ID from the first payment in one create call. No `customer_id` is needed.

<pre class="language-bash"><code class="lang-bash">curl --location 'https://sandbox.hyperswitch.io/payments' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'api-key: &#x3C;enter your Hyperswitch API key here>' \
--data-raw '{
    "amount": 6540,
    "currency": "USD",
    "profile_id": "&#x3C;enter the relevant profile id>",
    "confirm": true,
    "payment_method": "card",
<strong>    "off_session": true,
    "recurring_details": {
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

Only some processors accept a card plus network transaction ID. Hyperswitch routes the charge to the first eligible processor among those configured on your profile, and if none is eligible the request fails with `IR_39`. The eligible set is fixed per environment:

| Environment | Processors that accept a card with a network transaction ID                                                                                   |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Production  | Adyen, Archipel, Authorize.net, Checkout, Cybersource, Stripe, Nuvei, Worldpay Vantiv, Revolv3, Peach Payments, TSYS Transit, JPMorgan          |
| Sandbox     | The production list plus Novalnet and Worldpay                                                                                                |

***

### MIT with an externally vaulted card

If the customer's card lives in an external vault such as VGS or Hyperswitch Vault, you can charge it without ever handling the card number. You send the vault's alias in place of the number, plus the network transaction ID from the first payment. Hyperswitch sends the processor request through the vault, which swaps the alias for the real number on the way out.

**Before you start:** the business profile must have the vault connected under `external_vault_connector_details`. Without it the request fails with an internal server error rather than a validation message. Tokenex vaults are not supported on this path.

<pre class="language-bash"><code class="lang-bash">curl --location 'https://sandbox.hyperswitch.io/payments' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'api-key: &#x3C;enter your Hyperswitch API key here>' \
--data-raw '{
    "amount": 6540,
    "currency": "USD",
    "profile_id": "&#x3C;enter the relevant profile id>",
    "confirm": true,
    "payment_method": "card",
<strong>    "off_session": true,
    "recurring_details": {
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

Inside `vault_card_data`, `card_number` is the alias and the expiry is required. Cardholder name, network, issuer and the other card descriptors are optional. `transaction_link_id` is Mastercard's transaction link identifier and is optional. The same per-environment processor list as the previous section applies.

***

### MIT with a network token and external vault card fallback

If you hold both a network token and the card in an external vault, you can try the token first and let Hyperswitch fall back to the vaulted card when the token is declined for a reason that a clear card number would get past. Both attempts share the same network transaction ID, and the fallback runs at most once.

**Before you start:** the business profile needs the vault connected under `external_vault_connector_details`, the same as the previous section, and `is_clear_pan_retries_enabled` set to true. With that flag off, a declined token attempt is final.

<pre class="language-bash"><code class="lang-bash">curl --location 'https://sandbox.hyperswitch.io/payments' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'api-key: &#x3C;enter your Hyperswitch API key here>' \
--data-raw '{
    "amount": 6540,
    "currency": "USD",
    "profile_id": "&#x3C;enter the relevant profile id>",
    "confirm": true,
    "payment_method": "card",
<strong>    "off_session": true,
    "recurring_details": {
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

The fallback runs only when all of these hold:

* the token attempt failed;
* your processor is reachable on Hyperswitch's vault proxy path, which depends on your deployment;
* `is_clear_pan_retries_enabled` is true on the profile;
* Hyperswitch's decline-code mapping says the processor's error is worth retrying with the clear card number. That mapping is maintained by Hyperswitch, not per merchant, so which declines qualify depends on your deployment. See [Understanding Decline Codes](../../../workflows/smart-retries/processor-error-code-mapping.md).

When the fallback runs, the response you receive is from the vault-card attempt. The token decline is recorded as the first attempt on the same payment, so you can see both on the payment's attempt list. Processor eligibility is the same per-environment list as the previous two sections.

***

### All supported recurring_details types

Every charge of a saved or self-held method goes through `recurring_details`. Pick the type by what you hold:

| Type                                                        | What you hold                                                                    | Needs `customer_id`, `confirm: true`, `off_session: true` | Which processors                                                                                                       | On this page                                                                                              |
| ----------------------------------------------------------- | -------------------------------------------------------------------------------- | --------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `mandate_id`                                                | A Hyperswitch mandate ID                                                         | Yes                                                       | Any. The mandate must be active, belong to that customer, and the charge must stay within its amount and currency      |                                                                                                           |
| `payment_method_id`                                         | A saved method ID                                                                | Yes                                                       | Any                                                                                                                    | [Using a saved payment method](#using-a-saved-payment-method-to-do-a-mit-payment)                         |
| `processor_payment_token`                                   | The processor's own token. Add `merchant_connector_id` to pin the connector      | No                                                        | Any. The currency must match the original payment                                                                      |                                                                                                           |
| `network_transaction_id_and_card_details`                   | Card number plus NTID                                                            | No                                                        | NTID list                                                                                                              | [Without a saved payment method](#processing-mit-payments-without-a-saved-payment-method)                 |
| `network_transaction_id_and_network_token_details`          | Network token plus NTID                                                          | No                                                        | NTID list                                                                                                              |                                                                                                           |
| `network_transaction_id_and_decrypted_wallet_token_details` | Decrypted Apple Pay or Google Pay token plus NTID                                | No                                                        | NTID list                                                                                                              |                                                                                                           |
| `network_transaction_id_and_vault_card_details`             | Vault alias plus NTID                                                            | No                                                        | NTID list, and a vault on the profile                                                                                  | [Externally vaulted card](#mit-with-an-externally-vaulted-card)                                           |
| `card_with_limited_data`                                    | Card number only, no reference                                                   | No                                                        | Peach Payments only                                                                                                    |                                                                                                           |
| `network_token_with_vault_card_fallback`                    | Network token and vault alias                                                    | No                                                        | NTID list, a vault on the profile, and clear-PAN retries on                                                            | [Network token with fallback](#mit-with-a-network-token-and-external-vault-card-fallback)                 |

"NTID list" is the per-environment processor table under [Processing MIT payments without a saved payment method](#processing-mit-payments-without-a-saved-payment-method). The [confirm payment API reference](https://api-reference.hyperswitch.io/v1/payments/payments--confirm) carries the full request and response schemas for each type.
