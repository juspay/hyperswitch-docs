---
description: Store your customers cards securely in a centralized and PCI compliant vault
---

# 🔓 Tokenization & saved cards

{% hint style="info" %}
In this section, you will learn how to store your customers cards securely and use them on subsequent payments
{% endhint %}

Hyperswitch provides you with the capability to store your customers cards securely in a centralized PCI DSS Level 1 compliant vault. Our Unified checkout automatically handles saved cards flow. Customers choose the 'Save card details' checkbox while providing their card details for the payment and the transaction is successfully processed while the card is tokenized and stored securely in the card vault.

<figure><img src="../../.gitbook/assets/savedCards1.png" alt="" width="280"><figcaption></figcaption></figure>

For a returning customer, our Unified Checkout automatically shows the list of their saved cards from previous sessions if the same `customer_id` is passed during payments/create API call from your server.

The list customer payment methods API is used here which retrieve the list of cards saved against that customer in a tokenized form. These payment\_tokens can then be used to confirm a payment. ([API Reference](https://api-reference.hyperswitch.io/api-reference/payment-methods/list-payment-methods-for-a-customer-1))

<figure><img src="../../.gitbook/assets/savedCards2.png" alt="" width="300"><figcaption></figcaption></figure>

Once the user selects a particular card on the checkout page, the corresponding `payment_token` is used by Hyperswitch to  communicate with the card vault and securely retrieve card information to make the payment.

## Vaulting a payment method in non-purchase flows

To save the customer's payment method during account onboarding or in the billing/payment management, use the following API to store the card for future on-session payments.&#x20;

```bash
curl --request POST \
  --url https://sandbox.hyperswitch.io/payment_methods \
  --header 'Content-Type: application/json' \
  --header 'api-key: <api-key>' \
  --data '{
  "card": {
    "card_exp_month": "11",
    "card_exp_year": "25",
    "card_holder_name": "John Doe",
    "card_number": "4242424242424242"
  },
  "customer_id": "{{customer_id}}",
  "payment_method": "card",
  "payment_method_issuer": "Visa",
  "payment_method_type": "credit"
}'
```

If you are not able to handle the sensitive payment card info, you can collect it using the Hyperswitch Unified Checkout. Use the client secret obtained from the above API's response to initialise the SDK.

Cards saved using this API will be listed under saved payment methods for future on-session payments for the customers to use.

## Migrating your customers’ saved cards from your processors to Hyperswitch

Hyperswitch also supports migrating your customers’ saved cards from your processors’ vaults to Hyperswitch. This process typically involves requesting your processor’s support team to share your customers’ saved cards data to Hyperswitch in a secure file transfer format and may involve sharing Hyperswitch’s PCI DSS certificate with them. Please write to <mark style="color:blue;">biz@hyperswitch.io</mark> to know more and kickstart your card migration process.

## Network Tokenization

This features is current not present in Hyperswitch. Submit a feature request [here](https://github.com/juspay/hyperswitch/discussions/new?category=ideas-feature-requests). Hyperswitch can support Network Tokenization which will enable you to securely store your customers’ card details with various networks such as Visa, Mastercard, American Express, etc. This would bring in additional benefits such as higher authorization rates, fraud reduction, liability shift, lower network fees in some cases, etc.&#x20;

<details>

<summary>FAQs</summary>

1. How can I tokenize and add a card to my existing customer?

You can use the payment method API to add a card to against any of your customers. You can find the API reference [here](https://api-reference.hyperswitch.io/api-reference/payment-methods/paymentmethods--create).

</details>
