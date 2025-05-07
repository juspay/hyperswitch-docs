---
icon: lock-keyhole
description: Store your customers cards securely in a centralized and PCI compliant vault
---

# Tokenization & Card Vault

The Hyperswitch Card Vault enables you to securely store customer card details in a centralized, PCI DSS Level 1-compliant vault. It simplifies payment flows by offering tokenized card storage and retrieval. This ensures secure and seamless transactions, particularly for recurring payments, enhancing user experience and operational efficiency.

### Benefits:

* **Enhanced Security**: By tokenizing and securely storing sensitive card details, the feature reduces the risk of data breaches and simplifies compliance.
* **Improved User Experience**: Customers can reuse saved cards across transactions, reducing checkout friction.
* **Seamless Recurring Payments**: Automatic updates to tokenized card details ensure uninterrupted subscription payments, minimizing churn.
* **Global Compatibility**: Supports various payment processors and is compliant with international standards like PCI DSS and PCI SSS.

### How to store cards?

During checkout, customers can opt to save their card details by selecting the **'Save card details' checkbox** while entering their card information for payment. Once the transaction is successfully processed:

* The card details are securely tokenized and stored in the Hyperswitch Card Vault.
* A `payment_token` is generated, which can be used for future transactions, ensuring a seamless payment experience.

<figure><img src="../../../../.gitbook/assets/savedCards1.png" alt="" width="280"><figcaption></figcaption></figure>

### **How to retrieve saved cards?**

When a returning customer initiates a payment:

1. The [`list-customer-saved-payment-methods-for-a-payment` API](https://api-reference.hyperswitch.io/api-reference/payment-methods/list-customer-saved-payment-methods-for-a-payment) retrieves saved card details using the customer's unique `customer_id` .
2. These saved cards are displayed in the Unified Checkout, enabling the customer to select a card for payment.

<figure><img src="../../../../.gitbook/assets/savedCards2.png" alt="" width="300"><figcaption></figcaption></figure>

### **How to use a saved card?**

Once a card is selected, the `payment_token` is used to securely retrieve the card details from the vault for payment processing.

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

<details>

<summary>FAQs</summary>

1. How can I tokenize and add a card to my existing customer?

You can use the payment method API to add a card to against any of your customers. You can find the API reference [here](https://api-reference.hyperswitch.io/api-reference/payment-methods/paymentmethods--create).

</details>

{% content-ref url="network-tokenisation.md" %}
[network-tokenisation.md](network-tokenisation.md)
{% endcontent-ref %}
