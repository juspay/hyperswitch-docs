---
description: >-
  Use the standalone deployment script to deploy Hyperswitch control center on
  AWS quickly
---

# Standalone control center deployment for prototyping

{% hint style="info" %}
In this chapter, you will deploy Hyperswitch control center on AWS cloud. You can either try out a quick standalone deployment or a more scalable production ready setup
{% endhint %}

***

## Standalone deployment

### This setup includes:

| Component | Instance Type | Default Configuration |
| --------- | ------------- | --------------------- |
| EC2       | t3.medium     | 1 instance            |



## Steps to Deploy Hyperswitch control center on AWS

### **What do you need to get started**

* An AWS account (you can create an account [here](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?refid=em\_127222) if you do not have one)

### **Let's begin!**

> #### Note
>
> You can directly start from [Step 3](https://hyperswitch-juspay.stoplight.io/studio/installation-guide:main?source=8jifq2qd#step-3---setup-hyperswitch) if you have installed and configured AWS CLI

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

<figure><img src="../../.gitbook/assets/Screenshot 2023-10-12 at 6.00.50 PM.png" alt=""><figcaption></figcaption></figure>

Once you have the keys run the below command

```json
export AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
export AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
```

#### Step 3 - Setup Hyperswitch

You can now deploy the hyperswitch application by running the below command in the same terminal session

{% hint style="info" %}
Takes around 10-15 min to execute successfully
{% endhint %}

```json
curl https://raw.githubusercontent.com/juspay/hyperswitch-control-center/main/aws/hyperswitch_control_control_aws_setup.sh | bash
```

{% hint style="warning" %}
Make sure to save the passwords you provide while running the script
{% endhint %}

Once the script is executed, you will receive a `Public IP` as the response (e.g. `http://34.207.75.225`). This IP is the base URL for accessing the application.

#### Clean Up

If you want to delete the application from your account simply run the below clean up script

{% hint style="info" %}
You need JQ installed for this. For more information, [click here](https://jqlang.github.io/jq/download/)
{% endhint %}

```json
curl https://raw.githubusercontent.com/juspay/hyperswitch-control-center/main/aws/hyperswitch_control_center_cleanup_setup.sh | bash
```

