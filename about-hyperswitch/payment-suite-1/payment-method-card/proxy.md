---
icon: almost-equal-to
---

# Proxy

**📌 What is it?**

The **Proxy Payments Service** allows merchants to tokenize cards via Hyperswitch Vault and make API calls to PSPs using those tokens. The Vault intercepts these requests, replaces tokens with raw card data (detokenization), and forwards them securely to the PSP.

#### ✅ Why use it?

* **No PSP re-integration needed** – Keep your existing PSP connections.
* **PCI DSS scope reduction** – Raw card data stays within Vault.
* **Data security** – Detokenization happens only during the request lifecycle.
* **Centralized token management** – One vault, many PSPs.

#### ⚙️ How it works

#### **Understanding Payment and Vault Flow**&#x20;

<figure><img src="../../../.gitbook/assets/image (3) (4).png" alt=""><figcaption></figcaption></figure>



#### Vaulting&#x20;

**1. Create Payment Method Session (Server-Side)** The merchant server initiates the flow by calling the Hyperswitch [`Create-payment-method-session`](https://api-reference.hyperswitch.io/v2/payment-method-session/payment-method-session--create#payment-method-session-create) API with the `customer_id`. Hyperswitch responds with a `session_id` and `client_secret`, which are required to authenticate the client-side session.

**2. Initialize SDK (Client-Side)** The merchant client loads the `HyperLoader.js` script and initializes `window.Hyper` using the Publishable Key. Using the `session_id` and `client_secret`, the SDK creates a Payment Method Management (PMM) group and mounts the specific widget instance to the UI.

**3. Collect and Vault Card (Client-Side)** The customer enters their card details directly into the SDK-managed widget. Upon confirmation, the SDK calls the /`Confirm a payment method session` API. Hyperswitch securely receives the data, stores it in the Vault (retaining the CVV temporarily for the transaction TTL), and returns a success response with the `session_id` to the client.

**4. Retrieve Payment Method ID (Server-Side)** The merchant server calls the "List Payment Methods" API using the `session_id`. Hyperswitch returns a list of payment methods associated with the customer, from which the merchant server selects the appropriate `PM_ID` (Payment Method ID) to use for the transaction.

#### Payments

**Execute Proxy Payment (Server-Side)** The merchant server initiates the payment by sending a request to the [Hyperswitch vault proxy](https://docs.hyperswitch.io/~/revisions/01bZ2maqjwpnmrttix7i/explore-hyperswitch/payments-modules/vault/hyperswitch-vault-pass-through-proxy-payments) endpoint using the `payment_method_id` . The proxy securely replaces the token with the actual card data from the Vault and forwards the request to the Payment Service Provider (PSP), returning the final payment response to the merchant.

#### 🧪 Proxy Payment Request

Include the following details:

1. **Include the Hyperswitch Proxy payments related fields in the headers:**
   1. **URL:** Proxy endpoint **(**&#x68;ttps://sandbox.hyperswitch.io/prox&#x79;**)**
   2. **API Key:** Your API key for the merchant\_id under which the vault service was created on Hyperswitch dashboard
   3. **Profile\_id:** Your profile\_id for the merchant\_id under which the vault service was created on Hyperswitch dashboard
2. **Include the following details in the body:**
   1. **`request_body`:** Include the request body of the PSP payment request
   2. **`destination_url`, `method`, `headers`:** Pass your PSP url as destination url, PSP endpoint method and headers under the respective fields
   3. **Vault tokens:**
      1. `token_type` : Choose payment\_method\_id or tokenization\_id
      2. `token:` Plug the payment\_method\_id or tokenization\_id that you would have received when tokenizing card data or PII data at Hyperswitch vault
   4. **Placeholders for token data:** In the `request_body`**,** Plug in the dynamic placeholders`{{$card_number}}`, `{{$card_exp_month}}`,`{{$card_exp_year}}` against the PSP request fields where you want the actual values of the tokens from the Vault to be substituted

**Sample Proxy payment request (Checkout.com)**

<pre class="language-bash"><code class="lang-bash">curl --location 'https://sandbox.hyperswitch.io/proxy' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'X-Profile-Id: pro_p3ifmp0HzuC0Bp1KhMnK' \
--header 'Authorization: api-key=dev_bBPAkg0KX9Wn4Zewavrd0W76LsgDpGSey8iMARauXDWqzX4zwk4D03d0851Tx0EV' \
--header 'api-key: dev_30hnPzj6Kk6UAETk9hjWdaIxdVVuTk3mjmz2kxh6CIhq1K1DJ4nTZdpGt986L53G' \
--data '{
    "request_body": {
        "source": {
            "type": "card",
            "number": "{{$card_number}}",
            "expiry_month": "{{$card_exp_month}}",
            "expiry_year": "{{$card_exp_year}}",
            "billing_address": {
                "address_line1": "123 High St.",
                "address_line2": "Flat 456",
                "city": "London",
                "state": "GB",
                "zip": "SW1A 1AA",
                "country": "GB"
            }
        },
        "processing_channel_id": "pc_jx5lvimg..",
        "amount": 6540,
        "currency": "USD",
        "payment_type": "Regular",
        "reference": "ORD-5023-4E89",
        "description": "Set of 3 masks",
        "capture": true,
        "capture_on": "2019-09-10T10:11:12Z",
    },
    "destination_url": "https://api.sandbox.checkout.com/payments",
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "Bearer sk_sbox_3uu..."
    },
<strong>    "token": "12345_pm_0196f252baa1736190bf0fc81b9651ea",
</strong>    "token_type": "payment_method_id",
    "method": "POST"

}'
</code></pre>

#### 📥 Sample Response

```bash
{
    "response": {
        "id": "pay_7f6x6vki25futmy54uot5c3ama",
        "action_id": "act_egzzg6mojknungbe3367fvsiaq",
        "amount": 6540,
        "currency": "USD",
        "approved": true,
        "status": "Authorized",
        "auth_code": "690380",
        "response_code": "10000",
        "response_summary": "Approved",
        "risk": {
            "flagged": false,
            "score": 0.0
        },
        "source": {
            "id": "src_jliqxofnudseteb5dl4hl7frh4",
            "type": "card",
            "expiry_month": 12,
            "expiry_year": 2026,
            "scheme": "Visa",
            "last4": "0093",
            "fingerprint": "EEF6D525CC7C861D6AB1CEB56F9285839AE850E79BA43D7D8C06790B7A0ABD7C",
            "bin": "476136",
            "card_type": "CREDIT",
            "card_category": "CONSUMER",
            "issuer": "YES BANK, LTD.",
            "issuer_country": "IN",
            "product_id": "F",
            "product_type": "Visa Classic",
            "avs_check": "G",
            "payment_account_reference": "V001711066651680047",
            "regulated_indicator": false
        },
        "processed_on": "2025-05-21T10:10:42.7625936Z",
        "reference": "ORD-5023-4E89",
        "scheme_id": "509352732623965",
        "processing": {
            "acquirer_transaction_id": "096359746174895421192",
            "retrieval_reference_number": "404030119279",
            "merchant_category_code": "5815",
            "scheme_merchant_id": "75155",
            "scheme": "VISA",
            "aft": false,
            "pan_type_processed": "fpan",
            "cko_network_token_available": false,
            "provision_network_token": false
        },
        "expires_on": "2025-06-20T10:10:42.7625936Z",
        "_links": {
            "self": {
                "href": "https://api.sandbox.checkout.com/payments/pay_7f6x6vki25futmy54uot5c3ama"
            },
            "actions": {
                "href": "https://api.sandbox.checkout.com/payments/pay_7f6x6vki25futmy54uot5c3ama/actions"
            },
            "capture": {
                "href": "https://api.sandbox.checkout.com/payments/pay_7f6x6vki25futmy54uot5c3ama/captures"
            },
            "void": {
                "href": "https://api.sandbox.checkout.com/payments/pay_7f6x6vki25futmy54uot5c3ama/voids"
            }
        }
    },
    "status_code": 201,
    "response_headers": {
        "date": "Wed, 21 May 2025 10:10:42 GMT",
        "cko-version": "1.1049.0+54597dfad",
        "strict-transport-security": "max-age=16000000; includeSubDomains; preload;",
        "location": "https://api.sandbox.checkout.com/payments/pay_7f6x6vki25futmy54uot5c3ama",
        "content-length": "1883",
        "content-type": "application/json; charset=utf-8",
        "connection": "keep-alive",
        "cko-request-id": "61354917-3541-44fc-8ec7-98dd385aa0b4"
    }
}
```
