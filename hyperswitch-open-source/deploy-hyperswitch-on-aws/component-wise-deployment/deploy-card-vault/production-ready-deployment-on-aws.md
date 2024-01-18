---
description: CDK script to deploy Hyperswitch Card Vault on AWS
---

# Production ready deployment on AWS

{% hint style="info" %}
This section covers the steps for deploying the Hyperswitch card vault as an individual component
{% endhint %}

If you're looking for a production grade deployment of the card vault to be used along with the Hyperswitch application, refer to the the [full-stack deployment guide ](../../full-stack-deployment/deploy-on-aws-using-cloudformation.md)of Hyperswitch which includes the card locker as well.

## Standalone deployment of the Hyperswitch Card Vault

{% hint style="warning" %}
Pre-requisites

* `git` installed on your local machine
* node version 18
* An AWS user account with admin access (you can create an account [here](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?refid=em\_127222) if you do not have one)
{% endhint %}

### Step 1 - \[Optional] - Create a new user with Admin access (if you do not have a non-root user)

* Create a new user in your AWS account from [`IAM -> Users`](https://us-east-1.console.aws.amazon.com/iam/home?region=us-east-2#/users) (as shown below)
* While setting permissions, **provide admin access** to the user

<figure><img src="../../../../.gitbook/assets/aws user (1).gif" alt=""><figcaption></figcaption></figure>

### Step 2 - Configure your AWS credentials in your terminal

For this step you would need the following from your AWS account

1. Preferred AWS region
2. Access key ID
3. Secret Access Key
4. Session Token (if you MFA set up)

You can create or manage your access keys from `IAM > Users` inside your AWS Console. For more information, [click here](https://docs.aws.amazon.com/IAM/latest/UserGuide/id\_credentials\_access-keys.html#Using\_CreateAccessKey)

<figure><img src="../../../../.gitbook/assets/Screenshot 2023-11-02 at 5.48.06 PM.png" alt=""><figcaption></figcaption></figure>

Once you have the keys run the below command

```json
export AWS_DEFAULT_REGION=<Your AWS_REGION> // e.g., export AWS_DEFAULT_REGION=us-east-2
export AWS_ACCESS_KEY_ID=<Your Access_Key_Id> // e.g., export AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
export AWS_SECRET_ACCESS_KEY=<Your Secret_Access_Key> // e.g., export AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
export AWS_SESSION_TOKEN="<Your AWS_SESSION_TOKEN>" //optional
```

### Step 3 - Deploy Card Vault

Run the below commands in the same terminal session

```bash
git clone https://github.com/juspay/hyperswitch-cdk.git
cd hyperswitch-cdk
sh install-locker.sh
```

Once the script is run you will have to provide the following as inputs

1. Provide the master-key when prompted (command to generate the master-key will be displayed on the terminal; also note down the two custodian keys to start the locker)
2. Provide the Locker DB password of your choice when prompted
3. If you want to deploy the card vault in an existing VPC of yours, provide the VPC ID when prompted.

{% hint style="warning" %}
Note: The VPC should have at least one private subnet with egress to deploy the card vault
{% endhint %}

1. If you don't have one or want to set up a new VPC leave the input blank and proceed

### **Unlocking the Card Vault**

At this point your locker setup on the AWS account is complete. Please following the setups below to unlock the locker to make it read for use.

* Run the following command to generate the key for the jump-server

```bash
aws ssm get-parameter --name /ec2/keypair/$(aws ec2 describe-key-pairs --filters Name=key-name,Values=LockerJump-ec2-keypair --query "KeyPairs[*].KeyPairId" --output text) --with-decryption --query Parameter.Value --output text > locker-jump.pem
```

* Run the following command to update the permissions for your jump server key

```bash
chmod 400 locker-jump.pem
```

* Run the following command to SSH access your Card Vault instance through a jump server

```bash
ssh -i locker-jump.pem ec2-user@$JUMP_SERVER_ID
```

* Use the custodian keys to activate the locker (You can find the cURLs [here](https://api-reference.hyperswitch.io/api-reference/key-custodian/unlock-the-locker)) These cURLs are also displayed at the end of the script.&#x20;
* The locker\_public key and the tenant\_private key to use the locker with your application (Hyperswitch or otherwise) would be generated and available in the Parameter Store. **Use the commands provided to fetch them.**

```bash
aws ssm get-parameter --name /locker/public_key:1 --query 'Parameter.Value' --output text
aws ssm get-parameter --name /tenant/private_key:1 --query 'Parameter.Value' --output text
```

### Output

On successful deployment of the Card Vault you will receive the following

| Output                | What it is used for                                                                                             |
| --------------------- | --------------------------------------------------------------------------------------------------------------- |
| Jump Locker SSH Key   | This is used to Jump Locker SSH key to access the jump server                                                   |
| Jump Locker Public IP | The IP Address of the the Jump Server where you can activate the Card Vault                                     |
| Locker IP             | The URL of the Card Vault service                                                                               |
| Locker Public Key     | The public key of the card vault that needs to be used to JWE encrypt the requests to the card vault            |
| Tenant Private Key    | The private key of the tenant application that needs to be used to JWE decrypt the response from the card vault |

{% hint style="warning" %}
Make sure to save the keys and passwords you provide while running the script
{% endhint %}

### Integrating it with your Application&#x20;

To start using it with Hyperswitch update the following environment variables while deploying. You can use it with any other tenant application using the respective card vault URL and JWE keys.

```bash
ROUTER__LOCKER__HOST= # add the ip address of the ec2 instance created
ROUTER__JWEKEY__VAULT_ENCRYPTION_KEY= # add the JWE public key of locker generated above
ROUTER__JWEKEY__VAULT_PUBLIC_KEY= # add the JWE private key of tenant generated above
```

## Next step:

{% content-ref url="../../../testing/test-a-payment.md" %}
[test-a-payment.md](../../../testing/test-a-payment.md)
{% endcontent-ref %}
