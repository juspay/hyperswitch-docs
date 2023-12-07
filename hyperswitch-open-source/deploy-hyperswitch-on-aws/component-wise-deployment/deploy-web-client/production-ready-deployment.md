---
description: Deploy web client on AWS
---

# Production ready deployment

{% hint style="info" %}
In this section, you will be deploying the web client on your AWS account
{% endhint %}



**End goal**

* Hyperswitch Web SDK deployed and active on your AWS account.
* The script to be accessible to anybody who tries to fetch it and be able to open the SDK using that.

**What do you need to get started**

* An AWS account (you can create an account [here](https://portal.aws.amazon.com/billing/signup?refid=em\_127222\&redirect\_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation#/start/email) if you do not have one)

### **Let's begin!**

> #### Note
>
> You can directly start from [Step 3](production-ready-deployment.md#step-3-setup-hyperswitch) if you have installed and configured AWS CLI

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

1. Access key ID
2. Secret Access Key

You can create or manage your access keys from the Security Credentials tab inside your AWS Console. For more information, [click here](https://docs.aws.amazon.com/IAM/latest/UserGuide/id\_credentials\_access-keys.html#Using\_CreateAccessKey)

<figure><img src="../../../../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

Once you have the keys run the below command

```json
export AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
export AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
```

#### Step 3 - Setup Hyperswitch Web Client

You can now deploy the Hyperswitch web client by running the below command in the same terminal session

{% hint style="info" %}
Takes around 10-15 min to execute successfully
{% endhint %}

```json
curl https://raw.githubusercontent.com/juspay/hyperswitch-web/main/aws/hyperswitch_aws_production_deployment.sh | bash
```

On running the above command, you will get an option to configure the following&#x20;

1. **AWS region** - This is the AWS region that you want your SDK to be deployed to. In case not provided, it will default to us-east-2
2. **Option to either create a new bucket on S3 or use your existing S3 bucket** - You can enter either Y (yes) or N (No) to create a new bucket depending on your preference.
3. **Bucket Details** - If you choose to use your existing S3 bucket, you need to provide your S3 bucket location here. In case you choose to create a new S3 bucket, please provide a unique name here.
4. Self-hosted App server URL - This is the self hosted app server URL (eg., `http://34.207.75.225` ). If not provided, this will default to `https://sandbox.hyperswitch.io` and will work with Hyperswitch's SaaS app server.&#x20;

{% hint style="warning" %}
Depending on the API version and changes made to the web client, the web client may or may not be compatible with the SaaS app server.
{% endhint %}

Once the script is executed, you will receive an URL as the response (e.g. `http://my-bucket.s3.us-east-2.amazonaws.com/HyperLoader.js`). This is the base URL of your web client.&#x20;

{% hint style="success" %}
That's it! Hyperswitch web client should be up and running on your AWS account

Verify the health of the web client by hitting `http://my-bucket.s3.us-east-2.amazonaws.com/HyperLoader.js`. You should be able to see the bundled code in your browser.
{% endhint %}

**Great!**\
Your Web Client is hosted and can be accessed by this URL.

Now that the web client is hosted, you can integrate it with your app and go live. The detailed steps follow.

##
