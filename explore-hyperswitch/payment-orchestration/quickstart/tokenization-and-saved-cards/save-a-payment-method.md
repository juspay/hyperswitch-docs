---
description: Setting up and managing recurring payments
icon: repeat
---

# Save a Payment Method

Hyperswitch supports the following ways of saving a payment method used in a successful payment:

1. Saving for future customer on-session payments (COF-CIT)
2. Saving for future customer off-session payments (MIT)

## :credit\_card: Saving a payment method for future on-session payments (COF CIT)

To improve conversion rates and eliminate friction for the customer during checkout, you can save the customer's card so that they wouldn't have to enter the card details every time. This is also minimises the risk of the customer entering incorrect card details.

Saving for future on-session payments implies that the customer will be available online during the checkout and can authenticate the payment by entering CVV or complete 3DS verification. These are known as Card-on-File Customer Initiated Transactions (COF-CIT).

This is typically limited for card payment methods and not for wallets (viz. Apple Pay) and other APMs.

For saving a customer's payment method used in a successful transaction:

* Pass the following field in the `/payments` create request to indicate your intention to save the payment method

```bash
"setup_future_usage": "on_session"
```

* Pass the customer's consent to store the card in the `/payments/:id:/confirm` request

```bash
"customer_acceptance": {
        "acceptance_type": "online",
        "accepted_at": "1963-05-03T04:07:52.723Z",
        "online": {
            "ip_address": "in sit",
            "user_agent": "amet irure esse"
        }
    }
```

{% hint style="info" %}
If you are using the Hyperswitch SDK, the `customer_acceptance` is sent in the `/payments/:id:/confirm` request on the basis of customer clicking the save card radio button

**Note:** Ensure to enable this functionality using the [_displaySavedPaymentMethodsCheckbox_](https://docs.hyperswitch.io/hyperswitch-cloud/integration-guide/web/customization#id-6.-handle-saved-payment-methods) property during SDK integration
{% endhint %}

<figure><img src="../../../../.gitbook/assets/Screenshot 2024-04-18 at 12.49.35 PM.png" alt="" width="375"><figcaption><p>The customer's consent to save their card is expressed through this checkbox</p></figcaption></figure>

***

## :floppy\_disk: Saving a payment method for future MIT payments

Let's say, you want to save a customer's payment method to charge them at a later point without the need for additional cardholder authentication. This is done by raising an MIT (Merchant Initiated Transaction) exemption to the card network by the payment processor with reference to an initial transaction where the customer has authorised recurring charges. These are typically used when you want to charge a customer periodically/sporadically with a flexibility on the amount to be charged and number of charges.

Based on the payment processors support, this functionality is also available for other payment methods like Apple Pay and Google Pay Wallets.

### To save a customer's payment method used in a successful transaction for future MIT payments:

* Pass the following field in the `/payments` create request to indicate your intention to save the payment method

```bash
"setup_future_usage": "off_session"
```

* Pass the customer's consent to store the card in the `/payments/:id:/confirm` request

```bash
"customer_acceptance": {
        "acceptance_type": "online",
        "accepted_at": "1963-05-03T04:07:52.723Z",
        "online": {
            "ip_address": "in sit",
            "user_agent": "amet irure esse"
        }
    }
```

{% hint style="info" %}
If you are using the Hyperswitch SDK, the `customer_acceptance` is sent in the `/payments/:id:/confirm` request on the basis of customer clicking the save card radio button

**Note:** Ensure to enable this functionality using the [_displaySavedPaymentMethodsCheckbox_](https://docs.hyperswitch.io/hyperswitch-cloud/integration-guide/web/customization#id-6.-handle-saved-payment-methods) property during SDK integration
{% endhint %}

Retrieve the `payment_method_id` that was created against the above payment by retrieving the payment. You will get the payment\_method\_id in the response. Store this ID for making subsequent MIT payments.

```bash
curl --location 'https://sandbox.hyperswitch.io/payments/<pass the payment_id>' \
--header 'Accept: application/json' \
--header 'api-key: <enter your Hyperswitch API key here>' \
```

***

## :money\_with\_wings: Using a saved payment method to do a MIT payment

Once a customer's payment method is saved for MIT payments you can start charging the customer by sending the following details in the `/payments` request

<pre class="language-bash"><code class="lang-bash"><strong>"off_session": true,
</strong>"recurring_details": {
        "type": "payment_method_id",
        "data": "pm_lmTnIO5EdCiiMgRPrV9x" //pass the payment method id here
}
</code></pre>

You would be using the same `payment_method_id` that was returned in the `/payments/:id:/retrieve` response for the initial transaction where the customer authorized saving for future use.

To get all the payment methods saved for a customer use the[ List Customer Payment Methods](https://api-reference.hyperswitch.io/api-reference/payment-methods/list-payment-methods-for-a-customer) API.

```bash
curl --request GET \
  --url https://sandbox.hyperswitch.io/customers/{customer_id}/payment_methods \
  --header 'api-key: <api-key>'
```

***

***

## 🔓 Processing MIT Payments Without a Saved Payment Method

If a merchant is PCI-compliant and has the customer payment method details stored, an MIT payment can be performed by passing the card details and the network transaction id directly in the confirm call.

<pre class="language-bash"><code class="lang-bash"><strong>"off_session": true,
</strong>"recurring_details": {
        "type": "network_transaction_id_and_card_details",
        "data": {
            "card_number": "4242424242424242",
            "card_exp_month": "10",
            "card_exp_year": "25",
            "card_holder_name": "joseph Doe",
            "network_transaction_id": "MCC5ZRGMI0925" //scheme transaction id
        }
}
</code></pre>

Certain connectors, such as Stripe, Adyen, and Cybersource, support this flow, with only the straight-through routing algorithm available.

Straight-through algorithm to be passed in the `/payments` request

```bash
"routing": {
        "type": "single",
        "data": {
            "connector": "cybersource", //connector name
            "merchant_connector_id": "mca_VRmwU23zUmlmgAPrJ8rF" //merchant connector id
        }
    }
```

If you would like additional processors to support this flow or want to enable volume-based and priority-based routing algorithms, please submit a feature request [here](https://github.com/juspay/hyperswitch/discussions/new?category=ideas-feature-requests).

{% hint style="info" %}
⚠️ **Stripe Configuration Required**

This feature is not enabled by default and must be explicitly enabled by Stripe.\


If you receive the error `Received unknown parameter: payment_method_options[card][mit_exemption]`, follow the steps below to request activation.

**Email Stripe Support** requesting:

* Access to the `mit_exemption` parameter for MIT (Merchant Initiated Transaction) payments
* Ability to pass `network_transaction_id` in the parameter: `payment_method_options[card][mit_exemption][network_transaction_id]`
* Explain your use case: enabling cross-processor MIT payments using network transaction IDs from card schemes
{% endhint %}

***

## FAQ:

### **1. I want to onboard my customers by collecting their card details, authenticate and store for future MIT payments without charging them now. How can I vault a payment method with Hyperswitch?**

Hyperswitch allows you to vault a payment method without charging the customer by using the[ Zero Amount Authorization ](zero-amount-authorization-1.md)flow where you can authenticate and store your customer's card. Later you can make MIT payments using this payment method.

This is specifically useful when you have a separate Add Payment Method flow/onboarding journey where you don't want to debit the customer but store and authenticate their payment method.\
\
Refer to this page to see how to use it:&#x20;

{% content-ref url="zero-amount-authorization-1.md" %}
[zero-amount-authorization-1.md](zero-amount-authorization-1.md)
{% endcontent-ref %}
