---
icon: money-bills-simple
---

# Payments

The Payment Method SDK and `/payment-methods` API work in tandem with the `/payments` API to achieve any business objective as listed below. &#x20;

#### Guest Checkout Flow (S2S)

1. Collect card details and tokenise with HS [Create PM API](https://api-reference.hyperswitch.io/v2/payment-methods/payment-method--create-v1) to get a [PM ID](https://api-reference.hyperswitch.io/v2/payment-methods/payment-method--create-v1#response-id) (payment\_methd\_id)
2. Use the PM ID to authorize the [payment request](https://api-reference.hyperswitch.io/v1/payments/payments--confirm) during order confirmation
3. For extended sessions, where token expires before order completion, create a new PM ID with the same card details using the Create PM API

{% hint style="info" %}
Note - The PM ID in case of guest checkout is volatile in nature and has a default expiry of 1-hour which can be extended by Merchant at a session level.\
\
For guest checkout flow the PM ID is NOT unique to Customer + Payment method combination.
{% endhint %}

#### Customer Checkout Flow - First Time Payment (S2S)

1. Create a customer with HS using the [Create Customer API](https://api-reference.hyperswitch.io/v2/customers/customers--create-v1)
2. Use the customer\_id to tokenise the collected card details using Create PM API
3. Use the PM ID to authorize the [payment request](https://api-reference.hyperswitch.io/v1/payments/payments--confirm) during order confirmation
4. For extended sessions, where token expires before order completion update the PM with CVV using the [Update PM API](https://api-reference.hyperswitch.io/v2/payment-methods/payment-method--update-v1) and use this PM ID to complete the payment

{% hint style="info" %}
Note - The CVV storage is volatile in nature and can be stored for 1-hour be default which can be extended by Merchant at a session level. \
\
For logged-in user checkout flow the PM ID is unique to Customer + Payment method combination.
{% endhint %}

#### Customer Checkout Flow - Repeat Purchase (S2S)

1. Fetch the stored cards for the customer using [List Saved PMs API ](https://api-reference.hyperswitch.io/v2/payment-methods/payment-method--list-customer-saved-payment-methods-v1)which returns the masked card details with corresponding PM ID&#x20;
2. Update the PM ID of the user selected card along with CVV value collected from the user using the [Update PM API](https://api-reference.hyperswitch.io/v2/payment-methods/payment-method--update-v1)&#x20;
3. Use the PM ID to authorize the [payment request](https://api-reference.hyperswitch.io/v1/payments/payments--confirm) during order confirmation
4. For extended sessions, where token expires before order completion update the PM again with the collected CVV and use this PM ID to complete the payment

#### Payment Method SDK Checkout - Guest, New Customer and Repeat Customer Flows

1. Create a PM session using the [Session Create API ](https://api-reference.hyperswitch.io/v2/payment-method-session/payment-method-session--create-v1)to get a [client secret](https://api-reference.hyperswitch.io/v2/payment-method-session/payment-method-session--create-v1#response-client-secret)
2. For guest user, pass "storage\_type" as "volatile" and skip sending the Customer ID
3. Initialize and mount the [Vault SDK](https://docs.hyperswitch.io/explore-hyperswitch/payments-modules/vault/vault-sdk-integration-1#id-2.2-fetch-the-payment-method-session-and-mount-the-payment-methods-management-element) using the client secret and session\_id&#x20;
4. The SDK now takes care of the following flows based on user action:
5. Post which the SDK submits the card details via the [PM Confirm API](https://api-reference.hyperswitch.io/v1/payments/payments--confirm) and returns back a [PM Token](https://api-reference.hyperswitch.io/v1/payments/payments--confirm#response-payment-token-one-of-0) (short-lived) in the response
6. Pass this PM token to Merchant Server and exchange for a PM ID from the server using the [PM token exchange API](https://api-reference.hyperswitch.io/v2/payment-methods/payment-method--payment-method-token-to-payment-method-id-v1)
7. Use this PM ID to authorize the [payment request](https://api-reference.hyperswitch.io/v1/payments/payments--confirm)

{% hint style="info" %}
Note -  When using the HS SDK, the response always contains a temp token and you’ll need to exchange it to get the PM ID via a S2S call.
{% endhint %}

#### HS SDK Checkout for repeat customer - no CVV flow

1. Create a PM session using the [Session Create API ](https://api-reference.hyperswitch.io/v2/payment-method-session/payment-method-session--create-v1)to get a [client secret](https://api-reference.hyperswitch.io/v2/payment-method-session/payment-method-session--create-v1#response-client-secret)
2. Initialize and mount the [Vault SDK](https://docs.hyperswitch.io/explore-hyperswitch/payments-modules/vault/vault-sdk-integration-1#id-2.2-fetch-the-payment-method-session-and-mount-the-payment-methods-management-element) using the client secret and session\_id
3. The SDK lists the previously saved cards for customers to select&#x20;
4. If the card has been vaulted previously with an MIT setup for it, CVV is not collected for it and the SDK returns back a [PM Token](https://api-reference.hyperswitch.io/v1/payments/payments--confirm#response-payment-token-one-of-0) (short-lived) in the responseNote - The PM ID in case of guest checkout is volatile in nature and has a default expiry of 1-hour which can be extended by Merchant at a session level

{% hint style="info" %}
When using the HS SDK, the response always contains a temp token and you’ll need to exchange it to get the PM ID via a S2S call. Highlighted in detail in (4.)
{% endhint %}
