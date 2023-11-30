---
description: The one-stop dashboard to manage all your payment operations
---

# 🔌 Run control center

{% hint style="info" %}
In this section, you would be running the control center through which you can manage and control your payments
{% endhint %}

## Features

1. Connect to multiple payment processors like Stripe, Braintree, Adyen etc. in a few clicks
2. View and manage payments (payments, refunds, disputes) processed through multiple processors
3. Easily configure routing rules (volume-based, rule-based) to intelligently route your payments
4. Advanced analytics to make sense of your payments data

***

## Standard Installation

### Prerequisites

1. Node.js and npm installed on your machine.

### Installation Steps

Follow these simple steps to set up Hyperswitch on your local machine.

1.  Clone the repository:

    ```
    git clone https://github.com/juspay/hyperswitch-control-center.git
    ```
2.  Navigate to the project directory:

    ```
     cd hyperswitch-control-center
    ```
3.  Install project dependencies:

    ```
    npm install --force
    ```
4.  Update the .env file in the root directory.

    ```
    apiBaseUrl = your-backend-url
    sdkBaseUrl = your-sdk-url
    ```
5.  Start the ReScript compiler:

    ```
    npm run re:start
    ```
6.  In another terminal window, start the development server:

    ```
    npm run start
    ```
7. Access the application in your browser at [http://localhost:9000](http://localhost:9000/).
