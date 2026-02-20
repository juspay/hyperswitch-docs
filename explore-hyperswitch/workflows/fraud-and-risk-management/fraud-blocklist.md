---
description: Blocking card bins selectively based on observed fraudulent activity
icon: ban
---

# Fraud Blocklist

### Card bin blocklist

A blocklist in the context of payment processing refers to a security feature that allows merchants to restrict specific fingerprints associated with payment methods or block certain card bins. A fingerprint is a unique identifier linked to a particular payment method, and a card bin encompasses the first six digits of a credit card number, with an extended card bin covering the first eight digits.

Merchants can utilize the blocklist functionality to enhance security and control over their payment processing systems. This capability enables them to thwart transactions from identified problematic sources or potentially fraudulent payment methods. Here's how the blocklist feature works:

#### Blocking Specific Fingerprints

Merchants can identify and block specific fingerprints associated with payment methods. This is particularly useful in preventing transactions from certain payment instruments (card in our case) that may have a history of suspicious activity.

#### Blocking Card Bins

The blocklist also allows merchants to block entire card bins, focusing on the first six digits of credit card numbers. Additionally, they can extend this restriction to cover the first eight digits(extended\_card\_bin), providing a more comprehensive control mechanism.

#### Listing Blocklists

To manage and monitor these security measures, merchants have the option to list their specified blocklists. They can categorize these blocklists based on the type of restriction, such as payment method, card bin, or extended card bin.

#### Specifying Blocklist Types:

Merchants can define the type of blocklist they want to view, allowing for a granular understanding of the restrictions in place. This categorization may include payment method blocklists, card bin blocklists, or extended card bin blocklists.

#### Unblocking

Should the need arise, merchants can selectively unblock specific fingerprints, or card bins from the blocklist. This flexibility ensures that legitimate transactions are not inadvertently hindered by the security measures in place.

In summary, a blocklist feature empowers merchants to proactively manage the security of their payment processing systems by blocking specific fingerprints, card bins, or extended card bins. This not only safeguards against potential fraud but also provides a customizable and flexible approach to control and monitor payment transactions effectively.

### Blocklist via Hyperswitch

Currently we support blocking three types of resources i.e. card numbers (payment instrument), card bin, and extended card bin. A prerequisite to use this feature is to enable it using the /blocklist API as mentioned below.

#### For Card Bin and Extended Card Bin

* Setup a Merchant Account and any Connector account.
* Make a payment with a certain card (ensure it succeeds).
* Block the card's card bin or extended card bin.
* Try the payment again (should fail this time with an API response saying that the payment was blocked)

#### For Payment Instrument

* Repeat steps 1 and 2 of previous section.
*   In the payment confirm response, there will be an additional field called "fingerprint". This

    is the fingerprint id that can be used to block a particular payment method. Use this to

    block the card.
* Try the payment again (should fail)

#### Enabling blocklist guard on Hyperswitch

```
curl --location --request POST '{{base_url}}/blocklist/toggle?status=true' \
--header 'api-key: dev_xxxxxxxxxxxxxxxx'
```

### Configuring blocklist on Hyperswitch using API

1. Create card payment through Hyperswitch using [Payments Create API](https://api-reference.hyperswitch.io/v1/payments/payments--create)
2. In the [Payments response](https://api-reference.hyperswitch.io/v1/payments/payments--create#response-fingerprint-one-of-0), make note of the `fingerprint` field which is the unique fingerprint for a card passed to Hyperswitch

```markup
{
   "payment_id": "pay_Gbc5vC0SF4UMGXUm3yvl",
   "merchant_id": "merchant_1705052192",
   "status": "succeeded",
   "amount": 150,
   "net_amount": 150,
   "currency": "USD",
   "amount_received": 150,
   "connector": "stripe",
   "payment_method": "card",
   "payment_method_data": {
       "card": {
           "last4": "4242",
           "card_type": null,
           "card_network": null,
           "card_issuer": null,
           "card_issuing_country": null,
           "card_isin": "424242",
           "card_extended_bin": "42424242",
           "card_exp_month": "03",
           "card_exp_year": "2030",
           "card_holder_name": "joseph Doe"
       }
   },
  
  ...
  
  
   "fingerprint": "CKz5s9W4FX03eydwgGun"
}
```

3. Block a fingerprint using the [Blocklist endpoint](https://api-reference.hyperswitch.io/v1/blocklist/post-blocklist):

```
curl --location 'https://sandbox.hyperswitch.io/blocklist' \
--header 'Content-Type: application/json' \
--header 'api-key: YOUR_API_KEY' \
--data '{
    "type": "fingerprint",
    "data": "CKz5s9W4FX03eydwgGun"
}
```

4. [Show Blocked fingerprints](https://api-reference.hyperswitch.io/v1/blocklist/get-blocklist)

```
curl --location 'https://sandbox.hyperswitch.io/blocklist?data_kind=payment_method' \
--header 'api-key: YOUR_API_KEY'
```

5. [Toggle blocklist guard](https://api-reference.hyperswitch.io/v1/blocklist/post-blocklisttoggle), which will block the payment from the bins that are blocked.
6. Now when we create a payment using the same card details, the payment will fail with error:

```
   "error": {
       "type": "invalid_request",
       "message": "The payment is blocked",
       "code": "HE_03"
   }
```

6. [Unblock a fingerprint](https://api-reference.hyperswitch.io/v1/blocklist/delete-blocklist)

```
curl --location --request DELETE 'https://sandbox.hyperswitch.io/blocklist' \
--header 'Content-Type: application/json' \
--header 'api-key: YOUR_API_KEY' \
--data '{
    "type": "fingerprint",
    "data": "FtYY2OGsTokIrLN7TE9Y"
}
```

7. Block a Card BIN/ISIN (First 6 digits)

```
curl --location 'https://sandbox.hyperswitch.io/blocklist' \
--header 'Content-Type: application/json' \
--header 'api-key: YOUR_API_KEY' \
--data '{
    "type": "card_bin",
    "data": "424242"
}
```

8. Block an ExtendedCardBin (First 8 digits)

```
curl --location 'https://sandbox.hyperswitch.io/blocklist' \
--header 'Content-Type: application/json' \
--header 'api-key: YOUR_API_KEY' \
--data '{
    "type": "extended_card_bin",
    "data": "42424242"
}
```
