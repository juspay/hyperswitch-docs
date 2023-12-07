---
description: Quickly deploy your web client playground and see it in action
---

# Playground deployment for prototyping (OPTIONAL)

{% hint style="info" %}
Explore the web client's full stack playground for rapid prototyping using a single script to experience the product before integrating it into your app. You can also test your deployment on cloud, CDN configurations, etc. with this demo playground, before deploying your app.
{% endhint %}

Please note that this deployment is just for the demo-playground. This is **optional** and does not replace the integration step. In order to go-live, please integrate the web client onto your app before the deployment of your app

## Steps to Deploy Hyperswitch web client on AWS

### **What do you need to get started**

* An AWS account (you can create an account [here](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?refid=em\_127222) if you do not have one)

### **Let's begin!**

> #### Note
>
> You can directly start from [Step 3](playground-deployment-for-prototyping-optional.md#step-3-setup-hyperswitch-web-client-playground) if you have installed and configured AWS CLI

#### Step 1 - Install or Update the AWS CLI

{% tabs %}
{% tab title="Linux x86 (64-bit)" %}
{% code title="Run this on your terminal" fullWidth="false" %}
```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```
{% endcode %}

Confirm the installation with the following command

{% code title="Verify AWS CLI is installed" %}
```bash
aws --version
```
{% endcode %}

`aws-cli/2.10.0 Python/3.11.2 Linux/4.14.133-113.105.amzn2.x86_64 botocore/2.4.5` --> expected response
{% endtab %}

{% tab title="Linux ARM" %}
{% code title="Run this on your terminal" %}
```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-aarch64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```
{% endcode %}

Confirm the installation with the following command

{% code title="Verify AWS CLI is installed" %}
```
aws --version
```
{% endcode %}

`aws-cli/2.10.0 Python/3.11.2 Linux/4.14.133-113.105.amzn2.x86_64 botocore/2.4.5` --> expected response
{% endtab %}

{% tab title="MacOS" %}
{% code title="Run this on your terminal" %}
```bash
curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"
sudo installer -pkg AWSCLIV2.pkg -target /
```
{% endcode %}

To verify that the shell can find and run the aws command in your $PATH, use the following commands

{% code title="Verify AWS CLI is installed" %}
```bash
which aws
```
{% endcode %}

`/usr/local/bin/aws` --> expected response
{% endtab %}
{% endtabs %}

{% hint style="info" %}
For more information, [click here](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
{% endhint %}

#### Step 2 - Configure the AWS CLI

For this step you would need the following from you AWS account

1. `Access key ID`
2. `Secret Access Key`

You can create or manage your access keys from the Security Credentials tab inside your AWS Console. For more information, [click here](https://docs.aws.amazon.com/IAM/latest/UserGuide/id\_credentials\_access-keys.html#Using\_CreateAccessKey)

<figure><img src="../../../../.gitbook/assets/Screenshot 2023-10-12 at 6.00.50 PM.png" alt=""><figcaption></figcaption></figure>

Once you have the keys run the below command

```json
export AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
export AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
```

#### Step 3 - Setup Hyperswitch web client playground

{% hint style="danger" %}
The playground can help you get a look and feel of your checkout page and can be used for quickly prototyping your changes. The `React Demo App` in `hyperswitch-web` setups the playground for you-> which is a fullstack application. We ensure that the **secret key stays in the server side** and the publishable key stays in the client side, we insist you do the same for your application when you move to a Production ready setup
{% endhint %}

You can now deploy the Hyperswitch web client application by running the below command in the same terminal session

{% hint style="info" %}
Takes around 10-15 min to execute successfully
{% endhint %}

```bash
curl https://raw.githubusercontent.com/juspay/hyperswitch-web/main/aws/hyperswitch_web_aws_setup.sh | bash
```

On running the above command, you will get an option to configure the following:

**Mandatory:**&#x20;

1. **`Publishable Key` -** This is a public key that resides on your client side for authentication
2. **`Secret Key` -** This is the API key which should only be restricted to your app server

{% hint style="info" %}
You will either get these keys as an output when you host the app server, or for quick prototyping, you can create a new Hyperswitch sandbox account [here](https://app.hyperswitch.io/login) and get started.
{% endhint %}

**Optional:**

1. **URL where you have hosted Hyperswitch Backend -** The base URL where you have hosted the app server. If not provided, this will default to `https://sandbox.hyperswitch.io`
2. **URL where you have hosted Hyperswitch Client SDK** - This is the HyperLoader.js path (for e.g. `https://{domain}.s3.amazonaws.com/{path})`. If not provided, this will default to `https://beta.hyperswitch.io/v1`
3. **AWS Region -** This is the AWS region where you will host you web client. If not provided, it will default to `us-east-2`.

{% hint style="warning" %}
Depending on the API version and changes made to the web client, the web client may or may not be compatible with the SaaS app server.
{% endhint %}

Once the script is executed, you will receive a `Public IP` as the response (e.g. `http://34.207.75.225`). This IP is the base URL for accessing the web client playground.

{% hint style="success" %}
That's it! Hyperswitch web client should be up and running on your AWS account

Verify the application by opening this public IP in a web browser. Sometimes AWS can take upto 5 mins to initiate the EC2 instance.
{% endhint %}

#### Clean Up

If you want to delete the application from your account simply run the below clean up script

{% hint style="info" %}
You need JQ installed for this. For more information, [click here](https://jqlang.github.io/jq/download/)
{% endhint %}

```bash
curl https://raw.githubusercontent.com/juspay/hyperswitch-web/main/aws/hyperswitch_web_cleanup_setup.sh | bash
```
