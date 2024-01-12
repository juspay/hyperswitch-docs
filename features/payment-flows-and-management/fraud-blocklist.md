# 🛑 Fraud Blocklist

## What is Blocklist?

A blocklist in the context of payment processing refers to a security feature that allows merchants to restrict specific fingerprints associated with payment methods or block certain card bins. A fingerprint is a unique identifier linked to a particular payment method, and a card bin encompasses the first six digits of a credit card number, with an extended card bin covering the first eight digits.

Merchants can utilize the blocklist functionality to enhance security and control over their payment processing systems. This capability enables them to thwart transactions from identified problematic sources or potentially fraudulent payment methods. Here's how the blocklist feature works:

### Blocking Specific Fingerprints:

Merchants can identify and block specific fingerprints associated with payment methods. This is particularly useful in preventing transactions from certain payment instruments (card in our case) that may have a history of suspicious activity.

### Blocking Card Bins

The blocklist also allows merchants to block entire card bins, focusing on the first six digits of credit card numbers. Additionally, they can extend this restriction to cover the first eight digits(extended\_card\_bin), providing a more comprehensive control mechanism.

### Listing Blocklists

To manage and monitor these security measures, merchants have the option to list their specified blocklists. They can categorize these blocklists based on the type of restriction, such as payment method, card bin, or extended card bin.

### Specifying Blocklist Types:

Merchants can define the type of blocklist they want to view, allowing for a granular understanding of the restrictions in place. This categorization may include payment method blocklists, card bin blocklists, or extended card bin blocklists.

### Unblocking

Should the need arise, merchants can selectively unblock specific fingerprints, or card bins from the blocklist. This flexibility ensures that legitimate transactions are not inadvertently hindered by the security measures in place.

In summary, a blocklist feature empowers merchants to proactively manage the security of their payment processing systems by blocking specific fingerprints, card bins, or extended card bins. This not only safeguards against potential fraud but also provides a customizable and flexible approach to control and monitor payment transactions effectively.



## How does Blocklist work at Hyperswitch?

Currently we support blocking three types of resources i.e. card numbers (payment instrument), card bin, and extended card bin.

### For Card Bin and Extended Card Bin:

* Setup a Merchant Account and any Connector account.
* Make a payment with a certain card (ensure it succeeds).
* Block the card's card bin or extended card bin.
* Try the payment again (should fail this time with an API response saying that the payment was blocked)

### For Payment Instrument:

* Repeat steps 1 and 2 of previous section.
*   In the payment confirm response, there will be an additional field called "fingerprint". This

    is the fingerprint id that can be used to block a particular payment method. Use this to

    block the card.
* Try the payment again (should fail)

## How to configure Blocklist on Hyperswitch using API?

1. Create and confirm a card payment through Hyperswitch by passing raw card details

```
{
   "amount": 150,
   "currency": "USD",
   "confirm": true,
   "profile_id": "PROFILE-ID",
   "capture_method": "automatic",
   "customer_id": "CUSTOMER-ID",
   "amount_to_capture": 150,
   "email": "guest@example.com",
   "name": "John Doe",
   "phone": "999999999",
   "payment_method": "card",
   "payment_method_data": {
       "card": {
           "card_number": "4242424242424242",
           "card_exp_month": "03",
           "card_exp_year": "2030",
           "card_holder_name": "joseph Doe",
           "card_cvc": "737"
       }
   },
   "phone_country_code": "+65",
   "authentication_type": "no_three_ds",
   "description": "Its my first payment request",
   "return_url": "https://google.com",
   "metadata": {
   }
}

```

2. Make note of the "fingerprint" field from payments/confirm response which is the unique fingerprint for a card passed to Hyperswitch:

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
  
  
   "fingerprint": "fingerprint_CKz5s9W4FX03eydwgGun"
}
```

3. Block a fingerprint using the [Blocklist endpoint](https://api-reference.hyperswitch.io/api-reference/blocklist/post-blocklist):

```
curl --location 'https://sandbox.hyperswitch.io/blocklist' \
--header 'Content-Type: application/json' \
--header 'api-key: YOUR_API_KEY' \
--data '{
    "type": "fingerprint",
    "data": "fingerprint_CKz5s9W4FX03eydwgGun"
}
```

4. [Show Blocked fingerprints](https://api-reference.hyperswitch.io/api-reference/blocklist/get-blocklist)

```
curl --location 'https://sandbox.hyperswitch.io/blocklist?data_kind=payment_method' \
--header 'api-key: YOUR_API_KEY'
```



5. Now create and confirm a payment using the same card details. The payment will fail with error:

```
   "error": {
       "type": "invalid_request",
       "message": "The payment is blocked",
       "code": "HE_03"
   }
```

6. [Unblock a fingerprint](https://api-reference.hyperswitch.io/api-reference/blocklist/delete-blocklist)

```
curl --location --request DELETE 'https://sandbox.hyperswitch.io/blocklist' \
--header 'Content-Type: application/json' \
--header 'api-key: YOUR_API_KEY' \
--data '{
    "type": "fingerprint",
    "data": "fingerprint_FtYY2OGsTokIrLN7TE9Y"
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



## FAQ:

### 1. Can I configure Fraud Blocklist through Hyperswitch Control centre?

Currently, the Control centre's capability to configure fraud blocklist is under development and will be available in Q1'24.
