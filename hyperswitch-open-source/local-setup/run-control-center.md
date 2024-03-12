---
description: The one-stop dashboard to manage all your payment operations
---

# 🔌 Run control center

{% hint style="info" %}
In this section, you would be running the control center through which you can manage and control your payments
{% endhint %}

The Hyperswitch control center is the unified dashboard to manage all your payment operations and analytics. You can connect multiple payment processors, view & manage transactions, configure customized payment routing rules and access advanced analytics to make sense of your payments data.

## Video

***

{% embed url="https://youtu.be/3-KxwGUBybE" %}

## Standard Installation

{% hint style="info" %}
Ensure Node.js and npm are installed on your machine.
{% endhint %}

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

## Next step:

{% content-ref url="../account-setup/" %}
[account-setup](../account-setup/)
{% endcontent-ref %}
