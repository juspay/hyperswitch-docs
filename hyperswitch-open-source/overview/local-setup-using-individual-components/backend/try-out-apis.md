---
icon: arrow-up-triangle-square
---

# Try out APIs

### Set up your merchant account

1. Sign up or sign in to [Postman](https://www.postman.com/).
2. Open our [Postman collection](https://www.postman.com/hyperswitch/workspace/hyperswitch-development/collection/25176162-630b5353-7002-44d1-8ba1-ead6c230f2e3) and switch to the ["Variables" tab](https://www.postman.com/hyperswitch/workspace/hyperswitch-development/collection/25176162-630b5353-7002-44d1-8ba1-ead6c230f2e3?tab=variables). Update the value under the "current value" column for the `baseUrl` variable to have the hostname and port of the locally running server (`http://localhost:8080` by default).
3. While on the "Variables" tab, add the admin API key you configured in the application configuration under the "current value" column for the `admin_api_key` variable.
   1. If you're running Docker Compose, you can find the configuration file at [`config/docker_compose.toml`](https://github.com/juspay/hyperswitch/blob/main/config/docker_compose.toml), search for `admin_api_key` to find the admin API key.
   2. If you set up the dependencies locally, you can find the configuration file at [`config/development.toml`](https://github.com/juspay/hyperswitch/blob/main/config/development.toml), search for `admin_api_key` to find the admin API key
4. Open the ["Quick Start" folder](https://www.postman.com/hyperswitch/workspace/hyperswitch-development/folder/25176162-0f61a2bb-f9d5-4c60-8b73-9b677bf8ebbc) in the collection.
5.  Open the ["Merchant Account - Create"](https://www.postman.com/hyperswitch/workspace/hyperswitch-development/request/25176162-3c5d5282-931b-4adc-a651-f88c8697ebcb) request, switch to the "Body" tab and update any request parameters as required.

    * If you want to use a different connector for making payments with than the provided default, update the `data` field present in the `routing_algorithm` field to your liking.

    Click on the "Send" button to create a merchant account (You may need to "create a fork" to fork this collection to your own workspace to send a request). You should obtain a response containing most of the data included in the request, along with some additional fields. Store the merchant ID and publishable key returned in the response.

### Create an API key

1. Open the ["API Key - Create"](https://www.postman.com/hyperswitch/workspace/hyperswitch-development/request/25176162-98ce39af-0dbc-4583-8c22-dcaa801851e0) request, switch to the "Body" tab and update any request parameters as required. Click on the "Send" button to create an API key. You should obtain a response containing the data included in the request, along with the plaintext API key. Store the API key returned in the response securely.

### Set up a payment connector account

1. Sign up on the payment connector's (say Stripe, Adyen, etc.) dashboard and store your connector API key (and any other necessary secrets) securely.
2.  Open the ["Payment Connector - Create"](https://www.postman.com/hyperswitch/workspace/hyperswitch-development/request/25176162-295d83c8-957a-4524-95c8-589a26d751cf) request, switch to the "Body" tab and update any request parameters as required.

    * Pay special attention to the `connector_name` and `connector_account_details` fields and update them. You can find connector-specific details to be included in this [spreadsheet](https://docs.google.com/spreadsheets/d/e/2PACX-1vQWHLza9m5iO4Ol-tEBx22_Nnq8Mb3ISCWI53nrinIGLK8eHYmHGnvXFXUXEut8AFyGyI9DipsYaBLG/pubhtml?gid=748960791\&single=true).
    * Open the ["Variables" tab](https://www.postman.com/hyperswitch/workspace/hyperswitch-development/collection/25176162-630b5353-7002-44d1-8ba1-ead6c230f2e3?tab=variables) in the [Postman collection](https://www.postman.com/hyperswitch/workspace/hyperswitch-development/collection/25176162-630b5353-7002-44d1-8ba1-ead6c230f2e3) and set the `connector_api_key` variable to your connector's API key.

    Click on the "Send" button to create a payment connector account. You should obtain a response containing most of the data included in the request, along with some additional fields.
3. Follow the above steps if you'd like to add more payment connector accounts.

### Create a Payment

Ensure that you have [set up your merchant account](try-out-apis.md#set-up-your-merchant-account) and [set up at least one payment connector account](try-out-apis.md#set-up-a-payment-connector-account) before trying to create a payment.

1. Open the ["Payments - Create"](https://www.postman.com/hyperswitch/workspace/hyperswitch-development/request/25176162-ee0549bf-dd38-41fd-9a8a-de74879f3cda) request, switch to the "Body" tab and update any request parameters as required. Click on the "Send" button to create a payment. If all goes well and you had provided the correct connector credentials, the payment should be created successfully. You should see the `status` field of the response body having a value of `succeeded` in this case.
   * If the `status` of the payment created was `requires_confirmation`, set `confirm` to `true` in the request body and send the request again.
2. Open the ["Payments - Retrieve"](https://www.postman.com/hyperswitch/workspace/hyperswitch-development/request/25176162-8baf2590-d2af-44d0-ba37-e9cab7ef891a) request and click on the "Send" button (without modifying anything). This should return the payment object for the payment created in Step 2.

### Create a Refund

1. Open the ["Refunds - Create"](https://www.postman.com/hyperswitch/workspace/hyperswitch-development/request/25176162-4d1315c6-ac61-4411-8f7d-15d4e4e736a1) request in the ["Quick Start" folder](https://www.postman.com/hyperswitch/workspace/hyperswitch-development/folder/25176162-0f61a2bb-f9d5-4c60-8b73-9b677bf8ebbc) folder and switch to the "Body" tab. Update the amount to be refunded, if required, and click on the "Send" button. This should create a refund against the last payment made for the specified amount. Check the `status` field of the response body to verify that the refund hasn't failed.
2. Open the ["Refunds - Retrieve"](https://www.postman.com/hyperswitch/workspace/hyperswitch-development/request/25176162-137d6260-24f7-4752-9e69-26b61b83df0d) request and switch to the "Params" tab. Set the `id` path variable in the "Path Variables" table to the `refund_id` value returned in the response during the previous step. This should return the refund object for the refund created in the previous step.

That's it! Hope you got a hang of our APIs. To explore more of our APIs, please check the remaining folders in the [Postman collection](https://www.postman.com/hyperswitch/workspace/hyperswitch-development/collection/25176162-630b5353-7002-44d1-8ba1-ead6c230f2e3).
