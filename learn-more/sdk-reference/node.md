---
description: Node SDK to access the Hyperswitch API
---

# Node

{% hint style="info" %}
In this section, we will cover the steps to do an easy integration of your Node Backend server
{% endhint %}

## Using Node SDK for app server is OPTIONAL. You can use our REST APIs for the&#x20;

## Requirements

Node 12 or higher.

## Installation

Install the package with:

```sh
npm install @juspay-tech/hyperswitch-node --save
# or
yarn add @juspay-tech/hyperswitch-node
```

## Usage

The package needs to be configured with your account's secret key, which is available in the Hyperswitch Dashboard. Require it with the key's value:

```js
const hyperswitch = require('hyperswitch')('snd_efe...');

hyperswitch.paymentIntents.create(
  {
    // Refer the request body of payments from this API https://app.swaggerhub.com/apis-docs/bernard-eugine/HyperswitchAPI/0.0.1#/Payments/Create%20a%20Payment
    amount: 10000,
    currency: "USD",
    capture_method: "automatic",
    amount_to_capture: 10000,
    customer_id: "hyperswitchCustomer",
    email: "guest@example.com",
    name: "John Doe",
    phone: "999999999",
    phone_country_code: "+65",
    description: "Its my first payment request",
    authentication_type: "no_three_ds",
    return_url: "https://app.hyperswitch.io",
    shipping: {
      address: {
        line1: "1467",
        line2: "Harrison Street",
        line3: "Harrison Street",
        city: "San Fransico",
        state: "California",
        zip: "94122",
        country: "US",
        first_name: "John",
        last_name: "Doe"
      },
      phone: {
        number: "123456789",
        country_code: "+1"
      }
    },
    billing: {
      address: {
        line1: "1467",
        line2: "Harrison Street",
        line3: "Harrison Street",
        city: "San Fransico",
        state: "California",
        zip: "94122",
        country: "US",
        first_name: "John",
        last_name: "Doe"
      },
      phone: {
        number: "123456789",
        country_code: "+1"
      }
    },
    metadata: {
      order_details: {
        product_name: "Apple iphone 15",
        quantity: 1
      },
    }
  }
)
  .then(customer => console.log(customer.id))
  .catch(error => console.error(error));
```

If you are using ES modules and `async`/`await`,

```js
import Hyperswitch from 'hyperswitch';
const hyperswitch = new Hyperswitch('snd_efe...');

const payments_response = await hyperswitch.paymentIntents.create(
  {
    // Refer the request body of payments from this API https://app.swaggerhub.com/apis-docs/bernard-eugine/HyperswitchAPI/0.0.1#/Payments/Create%20a%20Payment
    amount: 10000,
    currency: "USD",
    capture_method: "automatic",
    amount_to_capture: 10000,
    customer_id: "hyperswitchCustomer",
    email: "guest@example.com",
    name: "John Doe",
    phone: "999999999",
    phone_country_code: "+65",
    description: "Its my first payment request",
    authentication_type: "no_three_ds",
    return_url: "https://app.hyperswitch.io",
    shipping: {
      address: {
        line1: "1467",
        line2: "Harrison Street",
        line3: "Harrison Street",
        city: "San Fransico",
        state: "California",
        zip: "94122",
        country: "US",
        first_name: "John",
        last_name: "Doe"
      },
      phone: {
        number: "123456789",
        country_code: "+1"
      }
    },
    billing: {
      address: {
        line1: "1467",
        line2: "Harrison Street",
        line3: "Harrison Street",
        city: "San Fransico",
        state: "California",
        zip: "94122",
        country: "US",
        first_name: "John",
        last_name: "Doe"
      },
      phone: {
        number: "123456789",
        country_code: "+1"
      }
    },
    metadata: {
      order_details: {
        product_name: "Apple iphone 15",
        quantity: 1
      },
    }
  }
);
console.log(customer.id);
```

## Sample server code using Hyperswitch Node SDK

There is a sample server code that uses the node sdk. Below are the available functions that work with the current latest node sdk version.

| Payments        | <p></p><ul><li>Create a payment</li></ul><ul><li>Retrieve a payment</li></ul><ul><li>Confirm a payment</li></ul><ul><li>Capture a payment</li></ul><ul><li>Cancel a payment</li></ul> |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Refunds         | <p></p><ul><li>Create a refund</li></ul><ul><li>Retrieve a refund</li></ul>                                                                                                           |
| Customers       | <p></p><ul><li>Create a customer</li></ul><ul><li>Retrieve a customer</li></ul><ul><li>Delete a customer</li></ul>                                                                    |
| Payment Methods | <p></p><ul><li>Create a payment method</li></ul><ul><li>List customer's payment methods</li></ul><ul><li>List merchant's payment methods</li></ul>                                    |

The request body(req.body) for all API's below can be referred from [API reference](https://app.swaggerhub.com/apis-docs/bernard-eugine/HyperswitchAPI/0.0.1)

```js
const express = require("express");
const app = express();
// This is a public sample test API key.
// Don't submit any personally identifiable information in requests made with this key.
// Sign in to see your own test API key embedded in code samples.

const hyperswitch = require('@juspay-tech/hyperswitch-node')('snd_b8df3xxx......');

app.use(express.static("public"));
app.use(express.json());

// The request body(req.body) for all API's below can be referred from https://app.swaggerhub.com/apis-docs/bernard-eugine/HyperswitchAPI/0.0.1

// Customer API

app.get("/customer_create", async (req, res) => { // Api Endpoint that the merchant has 
  try {
    const resp = await hyperswitch.customers.create(
      req.body // send the customer request body as it is in openapi spec
    );
    res.send(resp);
  } catch (e) {
    // handle error here 
    res.send(e);
  }
});

app.get("/customer_retrieve/:customer_id", async (req, res) => { // Api endpoint that customer has
  try {
    const resp = await hyperswitch.customers.retrieve(
      req.params.customer_id,
    );
    res.send(resp);
  } catch (e) {
    // handle error here 
    res.send(e);
  }
});

app.get("/customer_delete/:customer_id", async (req, res) => {
  try {
    const resp = await hyperswitch.customers.del(
      req.params.customer_id,
    );
    res.send(resp);
  } catch (e) {
    // handle error here 
    res.send(e);
  }
});


// Payments API

app.get("/payment_create", async (req, res) => {
  try {
    const resp = await hyperswitch.paymentIntents.create(
      req.body
    );
    res.send(resp);
  } catch (e) {
    // handle error here 
    res.send(e);
  }
});

app.get("/payment_confirm/:payment_id", async (req, res) => {
  try {
    const resp = await hyperswitch.paymentIntents.confirm(
      req.params.payment_id,
      req.body
    );
    res.send(resp);
  } catch (e) {
    // handle error here 
    res.send(e);
  }
});

app.get("/payment_retrieve/:payment_id", async (req, res) => {
  try {
    const resp = await hyperswitch.paymentIntents.retrieve(
      req.params.payment_id,
    );
    res.send(resp);
  } catch (e) {
    // handle error here 
    res.send(e);
  }
});

app.get("/payment_capture/:payment_id", async (req, res) => {
  try {
    const resp = await hyperswitch.paymentIntents.capture(
      req.params.payid,
      req.body
    );
    res.send(resp);
  } catch (e) {
    // handle error here 
    res.send(e);
  }
});

app.get("/payment_cancel/:payment_id", async (req, res) => {
  try {
    const resp = await hyperswitch.paymentIntents.cancel(
      req.params.payment_id,
      req.body
    );
    res.send(resp);
  } catch (e) {
    // handle error here 
    res.send(e);
  }
});


// Refunds API 

app.get("/refunds_create", async (req, res) => {
  try {
    const resp = await hyperswitch.refunds.create(
      req.body
    );
    res.send(resp);
  } catch (e) {
    // handle error here 
    res.send(e);
  }
});

app.get("/refunds_retrieve/:refund_id", async (req, res) => {
  try {
    const resp = await hyperswitch.refunds.retrieve(
      req.params.refund_id,
      req.body
    );
    res.send(resp);
  } catch (e) {
    // handle error here 
    res.send(e);
  }
});

// Payment Methods API

app.get("/payment_method_create", async (req, res) => {
  try {
    const resp = await hyperswitch.paymentMethods.create(
      req.body
    );
    res.send(resp);
  } catch (e) {
    // handle error here 
    res.send(e);
  }
});

app.get("/payment_method_list", async (req, res) => {
  try {
    const resp = await hyperswitch.paymentMethods.list(
    );
    res.send(resp);
  } catch (e) {
    // handle error here 
    res.send(e);
  }
});

app.get("/payment_method_list_by_customer/:customer_id", async (req, res) => {
  try {
    const resp = await hyperswitch.customers.listPaymentMethods(
      req.params.customer_id,
    );
    res.send(resp);
  } catch (e) {
    // handle error here 
    res.send(e);
  }
});

app.listen(4242, () => console.log("Node server listening on port 4242!"));

```
