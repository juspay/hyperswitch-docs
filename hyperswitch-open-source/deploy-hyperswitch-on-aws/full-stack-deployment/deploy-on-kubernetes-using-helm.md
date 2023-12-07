# Deploy on Kubernetes using Helm

The Helm chart is designed to facilitate the deployment of Hyperswitch services, including the AppServer, Control Center, Scheduler services, and the Demo web application

## Prerequisites

1. Active redis service
2. Create a Postgres database and run the schema migration using the below commands

{% code overflow="wrap" fullWidth="false" %}
```bash
git  clone https://github.com/juspay/hyperswitch.git

diesel  migration --database-url postgres://{{user}}:{{password}}@localhost:5432/hyperswitch run 
```
{% endcode %}

## Installation

### Step 1 - Update Configurations

To deploy the Helm chart, you need to update following values for each service in `values.yaml`

<table><thead><tr><th width="140.33333333333331">Service</th><th width="298">Configuration Key</th><th>Description</th></tr></thead><tbody><tr><td>App Server</td><td><code>application.server.server_base_url</code></td><td>Set to the hostname of your Hyperswitch backend for redirection scenarios.</td></tr><tr><td></td><td><code>application.server.secrets.admin_api_key</code></td><td>Used for all admin operations. Replace <code>"admin_api_key"</code> with your actual admin API key.</td></tr><tr><td></td><td><code>application.server.locker.host</code></td><td><a href="https://opensource.hyperswitch.io/going-live/pci-compliance/card-vault-installation">Card Vault</a> Hostname</td></tr><tr><td></td><td><code>redis.host</code></td><td>Hostname of your redis service. it should run in default port 6379</td></tr><tr><td></td><td><code>db.name</code></td><td>Postgres Database name.</td></tr><tr><td></td><td><code>db.host</code></td><td>Database Host name</td></tr><tr><td></td><td><code>db.user_name</code></td><td>Database username</td></tr><tr><td></td><td><code>db.password</code></td><td>Database password</td></tr><tr><td>Control Center</td><td><code>application.dashboard.env.apiBaseUrl</code></td><td>Set to the hostname of your Hyperswitch backend, so that Control center can access the Hyperswitch backend.</td></tr><tr><td></td><td><code>application.dashboard.env.sdkBaseUrl</code></td><td>Set to the URL of your hosted Hyperloader, so that you can test Hyperswitch Web SDK in the Control Center.<br>Eg: https://{{your_host}}/0.5.6/v0/HyperLoader.js</td></tr><tr><td>Hyperswitch Demo Store</td><td><code>application.sdkDemo.env.hyperswitchServerUrl</code></td><td>Set to the hostname of your Hyperswitch backend to access the Hyperswitch backend.</td></tr><tr><td></td><td><code>application.sdkDemo.env.hyperSwitchClientUrl</code></td><td>Set to the URL of your hosted Hyperloader to access the Hyperswitch SDK.<br>Eg: https://{{your_host}}/0.5.6/v0</td></tr></tbody></table>

### Step 2 - Install Hyperswitch

Use below command to install hyperswitch services with above configs

```bash
helm install hyperswitch-v1 . -n hyperswitch
```

{% hint style="success" %}
That's it! Hyperswitch should be up and running on your AWS account :tada::tada:
{% endhint %}

## Post-Deployment Checklist

After deploying the Helm chart, you should verify that everything is working correctly

### App Server

* [ ] &#x20;Check that `hyperswitch_server/health` returns `health is good`

### Control Center

* [ ] &#x20;Verify if you are able to sign in or sign up
* [ ] &#x20;Verify if you are able to [create API key](https://opensource.hyperswitch.io/run-hyperswitch-locally/account-setup/using-hyperswitch-control-center#user-content-create-an-api-key)
* [ ] &#x20;Verify if you are able to [configure a new payment processor](https://opensource.hyperswitch.io/run-hyperswitch-locally/account-setup/using-hyperswitch-control-center#add-a-payment-processor)

## Test a payment

Hyperswitch Demo store will mimic the behavior of your checkout page. But demo store needs merchant API Key and Publishable Key to work. You can do this by following the below steps

### Step 1 - Configure below details again in your `values.yaml`

| Service                | Configuration Key                                   | Description                                                                                                      |
| ---------------------- | --------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| Hyperswitch Demo Store | `application.sdkDemo.env.hyperswitchPublishableKey` | This should be set to your merchant publishable key. You will get this once you create a merchant.               |
|                        | `application.sdkDemo.env.hyperswitchSecretKey`      | This should be set to your merchant secret key. You can create this from the control center or via the REST API. |

### Step 2 - Run helm upgrade to restart pods with updated config

```
helm upgrade --install hyperswitch-v1 . -n hyperswitch -f values.yaml
```

### Step 3 - Make a payment using our Demo App

Use the Hyperswitch Demo app and [make a payment with test card](https://opensource.hyperswitch.io/hyperswitch-open-source/test-a-payment).

Refer our [postman collection](https://www.postman.com/hyperswitch/workspace/hyperswitch/folder/25176183-0103918c-6611-459b-9faf-354dee8e4437) to try out REST APIs\




\
