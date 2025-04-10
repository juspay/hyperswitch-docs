---
icon: laptop
---

# Control Center

{% hint style="danger" %}
This setup is meant for development. If you want a quick trial of Hyperswitch (without contributing), use [this guide](https://docs.hyperswitch.io/hyperswitch-open-source/overview/unified-local-setup-using-docker).
{% endhint %}

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
    npm install
    ```
4.  Start the ReScript compiler:

    ```
    npm run re:start
    ```
5.  In another terminal window, start the backend server, and SDK:

    ```
    git clone --depth 1 --branch latest https://github.com/juspay/hyperswitch
    cd hyperswitch
    docker compose up -d --scale hyperswitch-control-center=0
    ```
6.  Update the config.toml file

    ```
    api_url = your-backend-url #e.g: http://localhost:8080
    sdk_url = your-sdk-url  #e.g: http://localhost:9050/HyperLoader.js
    ```
7.  In another terminal window, start the development server:

    <pre><code><strong>npm run start
    </strong></code></pre>

### Accessing the Application

Once the containers are up and running, you can access the application by navigating to [http://localhost:9000](http://localhost:9000/) in your web browser.

