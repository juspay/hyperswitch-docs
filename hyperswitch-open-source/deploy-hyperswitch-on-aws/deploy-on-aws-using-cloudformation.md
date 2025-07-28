---
description: Use our CDK script to deploy Hyperswitch into your AWS stack
icon: aws
---

# Deploy on AWS using CloudFormation

{% embed url="https://www.youtube.com/watch?v=c2igjE3-EDc" %}

## Steps to Deploy Hyperswitch on AWS

### **Prerequisites**

* `git` installed on your local machine
* node version 18+
* An AWS user account with admin access (you can create an account [here](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?refid=em_127222) if you do not have one)

### Step 1 - \[Optional] - Create a new user with admin access&#x20;

<figure><img src="../../.gitbook/assets/aws user (1).gif" alt=""><figcaption></figcaption></figure>

If you do not have a user with admin access, follow these steps:

#### 1. Sign into the AWS Management Console

* Go to [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/)
* In the left-hand menu, click **Users**
* Click the **Add users** button

#### 2. Set the username

* **User name:** `hyperswitch`

<figure><img src="../../.gitbook/assets/1-specify-user.png" alt=""><figcaption></figcaption></figure>

#### 3. Attach Permissions

* Choose **Attach policies directly**.
* In the search bar, type `AdministratorAccess`
* Check the box for:\
  🔐 **AdministratorAccess** – _AWS managed, job function_

<figure><img src="../../.gitbook/assets/2-policies.png" alt=""><figcaption></figcaption></figure>

#### 4. Review and Create

* Confirm the details:
* User name: `hyperswitch`
* Permissions: `AdministratorAccess`
* Click on **Create user**

<figure><img src="../../.gitbook/assets/3-create-user.png" alt=""><figcaption></figcaption></figure>

#### 5. Save Access Credentials

* Click on the newly created user `hyperswitch` to view its details.
* Navigate to the **Security credentials** tab.
*   Under the **Access keys** section:

    * Click **Create access key**
    * Choose **Command Line Interface (CLI)**)
    * Click **Next**, then **Create access key**
    * **Download the `.csv` file** or **securely copy** the:
      * **Access Key ID**
      * **Secret Access Key**

    <figure><img src="../../.gitbook/assets/aws-access-key (1).png" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
⚠️ You won’t be able to view the Secret Access Key again later — store it in a password manager or other secure location.
{% endhint %}

### Step 2 - Configure your AWS credentials in your terminal

For this step you would need the following from your AWS account

* Preferred AWS region
* Access key ID
* Secret Access Key
* Session Token (if you MFA set up)

Once you have the keys run the below command

```json
export AWS_DEFAULT_REGION=<Your AWS_REGION> // e.g., export AWS_DEFAULT_REGION=us-east-2
export AWS_ACCESS_KEY_ID=<Your Access_Key_Id> // e.g., export AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
export AWS_SECRET_ACCESS_KEY=<Your Secret_Access_Key> // e.g., export AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
export AWS_SESSION_TOKEN="<Your AWS_SESSION_TOKEN>" //optional
```

### Step 3 - Deploy Hyperswitch application

Run the below commands in the same terminal session

```bash
git clone https://github.com/juspay/hyperswitch-cdk.git
cd hyperswitch-cdk
bash install.sh
```

Once the script is run you will have to provide the following as inputs:

1. Create a DB password of your choice (should be more than 8 chars).
2. Provide an Admin API key of your choosing via [Hyperswitch Dashboard](https://app.hyperswitch.io/dashboard/developer-api-keys).
3. If you choose to opt-in for the card vault service, provide a master-key when prompted (command to generate the master-key will be displayed on the terminal; also note down the two custodian keys to start the locker)
   * Provide the Locker DB password of your choice when prompted

After the deployment is completed, use the custodian keys to activate the locker (You can find the cURLs [here](https://api-reference.hyperswitch.io/api-reference/key-custodian/unlock-the-locker)). The host URL of the locker to run these cURLs will be displayed on terminal.

{% hint style="warning" %}
Make sure to save the passwords you provide while running the script.
{% endhint %}

### Output

On successful execution of the script, you will receive the following outputs

| Output                      | What is it used for                                                                                                                                      |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Hostname of the app server  | Access the application's APIs using the given base URL                                                                                                   |
| Hostname of the log server  | View real-time logs for all processes                                                                                                                    |
| Control Center URL          | Access the Hyperswitch control center and explore multiple settings                                                                                      |
| Hyperloader.js URL          | Use the `hyperloader` to [integrate our web client](component-wise-deployment/deploy-web-client/integrate-web-client-on-your-web-app.md) in your website |
| Demo App URL                | Test payments quickly using our web checkout in the demo store                                                                                           |
| Locker URL                  | Access the Hyperswitch card vault using this host URL                                                                                                    |

{% hint style="success" %}
That's it! Hyperswitch should be up and running on your AWS account. Open the Demo Store and make a test transaction using any test card :tada::tada:
{% endhint %}

## **Estimated cost of running the above setup**

The table below offers an estimated cost for operating the setup generated by the CDK script within your AWS environment. This cost is computed under the following assumptions:

* &#x20;The system is handling a traffic of 1000 transactions per day
* The number of hours per month for each component is 720 (24\*30)

<table data-full-width="false"><thead><tr><th width="138">Component</th><th width="125">Instances</th><th width="164">Storage</th><th width="176">Throughput cost</th><th>Total Cost ($)</th></tr></thead><tbody><tr><td>EKS</td><td>1 cluster</td><td>-</td><td></td><td>73</td></tr><tr><td>EC2</td><td>3 x t3.medium</td><td>-</td><td></td><td>45.11</td></tr><tr><td>Aurora Postgresql</td><td>1 x t3.medium</td><td>500 MB * ( 0.05 USD) Assuming 30k transactions per month</td><td><p>0.07 USD **</p><p>(3 baseline i/o per minute, 9 peak i/o per minute) </p></td><td><p>59.98</p><p>(59.86 + 0.05 + 0.07)</p></td></tr><tr><td>ElastiCache</td><td>1 x t3.micro</td><td>-</td><td></td><td>12.24</td></tr><tr><td>S3</td><td>1</td><td>1 GB</td><td><p>0.24 ***</p><p>(290 GB outbound data transfer assuming 1000 new user logins per day)</p></td><td>1.14</td></tr><tr><td>Load Balancer</td><td>4</td><td>-</td><td></td><td>65.72</td></tr><tr><td><mark style="color:red;"><strong>Total</strong></mark></td><td></td><td></td><td></td><td><mark style="color:red;"><strong>257.19</strong></mark></td></tr></tbody></table>

\*Avg data written per transaction = 16 kb

\*\*Assuming 3.5k API requests per day with 5 i/o operations each and 18 hours peak time per day

\*\*\*Assuming 30 GET requests per login. Avg new user would receive 10 mb data per request. For 1000 new logins the data transfer = (10\*30\*1000\*) / 1024 \~ 290 GB

<details>

<summary>FAQs</summary>

1. **Why use AWS EKS for deploying Hyperswitch?** AWS Elastic Kubernetes Service (EKS) provides a managed Kubernetes cluster, ensuring high availability and scalability for Hyperswitch.
2. **How do I deploy Hyperswitch on EKS using Helm charts?** You can deploy Hyperswitch on EKS by following our Helm chart documentation, which provides step-by-step instructions.
3. **What versions of EKS are supported for deploying Hyperswitch?** Hyperswitch supports all versions of EKS that are officially provided by AWS.
4. **Can I use my existing RDS instance for the database with Hyperswitch?** Yes, you can configure Hyperswitch to use your existing RDS instance as the database.
5. **What database engines are supported for RDS when using Hyperswitch?** Hyperswitch supports various database engines, including PostgreSQL, MySQL, SQL Server, and Oracle, depending on your requirements.
6. **How do I configure RDS with Hyperswitch using Helm charts?** Our Helm chart documentation provides detailed instructions for setting up RDS as the database for Hyperswitch.
7. **Do I need to make any specific configurations in RDS for Hyperswitch to work optimally?** Yes, you may need to configure database parameters such as connection limits and database user credentials. Consult the documentation for details.
8. **Can I use Amazon Elastic Cache (Redis) as a caching layer with Hyperswitch?** Yes, you can configure Hyperswitch to use Amazon Elastic Cache (Redis) for caching purposes, which can improve performance.
9. **What Redis configurations are recommended for optimal performance with Hyperswitch?** The recommended Redis configurations can vary based on your workload, but you should typically configure Redis to use the appropriate instance type and set the eviction policies correctly.
10. **How can I scale Hyperswitch on EKS to handle increased traffic?** You can scale Hyperswitch by adjusting the number of pods in the deployment or using Kubernetes' Horizontal Pod Autoscaling based on resource utilization.
11. **How can I monitor the performance and health of Hyperswitch on EKS?** You can Use AWS CloudWatch, Prometheus, or other monitoring solutions to track performance metrics and set up alerts. Refer [our guide](../../check-list-for-production/going-live/for-on-prem-setup/monitoring.md) for more information
12. **Is there a recommended backup and disaster recovery strategy for Hyperswitch and associated AWS resources?** Yes, it's essential to implement regular backups for RDS and have a disaster recovery plan in place. AWS provides tools and services for this purpose.
13. **Are there any specific security considerations when deploying Hyperswitch on AWS EKS?** You should follow our [best practices](../../check-list-for-production/going-live/for-on-prem-setup/security.md) for securing your EKS cluster and your Hyperswitch application, including network policies, IAM roles, and encryption.
14. **How do I upgrade Hyperswitch and its dependencies on EKS?** Please refer to the [Updates](../../check-list-for-production/going-live/for-on-prem-setup/updates.md) section for more details
15. **What do I do if I encounter issues during the deployment process?** If you encounter issues, consult the troubleshooting section of the documentation or [reach out to our support team](https://hyperswitch.io/contact) for assistance.
16. **Where can I find further documentation on Hyperswitch?** You can find additional documentation, tutorials, and support resources on our website and in our api docs.

</details>

## Tear down the AWS Deployment

You'll need to destroy the Hyperswitch CDK Stack. To tear down all AWS resources provisioned by the Hyperswitch CDK stack, run the following command. This ensures the required `aws_arn` context is passed during the destroy process:

```bash
cdk destroy -c aws_arn=$(aws sts get-caller-identity --query Arn --output text)
```

You’ll be prompted to confirm the deletion. Type `y` when prompted to proceed.

> 💡 This command removes all infrastructure created by the CDK, including EKS clusters, VPCs, IAM roles, and other resources.

You can check to see if there is anything running:

```
aws cloudformation list-stacks --stack-status-filter CREATE_COMPLETE UPDATE_COMPLETE
```

If the CDK Toolkit exist, you can execute this command:

```
aws cloudformation delete-stack --stack-name CDKToolkit
```

## What you deployed in this tutorial

The following components and services were provisioned as part of a new stack in your AWS account:

| Component       | Instance Type  | Default Configuration |
| --------------- | -------------- | --------------------- |
| EKS (1 Cluster) | t3.medium      | 2 Nodes               |
| Load Balancer   | Application LB | 2 LBs                 |
| RDS             | t4g.medium     | 2 cluster             |
| ElastiCache     | t4g.medium     | 1 cluster             |
| EC2             | t3.medium      | 1 instance            |

The following services are installed in the 2 Nodes across the EKS cluster

| Service Name           | Number of Pods                              | Default Configuration                |
| ---------------------- | ------------------------------------------- | ------------------------------------ |
| Hyperswitch App Server | 3 pods                                      | <p>CPU : 400m<br>Memory : 500 Mi</p> |
| Producer (Scheduler)   | 1 pod                                       | <p>CPU : 100m<br>Memory : 100 Mi</p> |
| Consumer (Scheduler)   | 1 pods                                      | <p>CPU : 100m<br>Memory : 100 Mi</p> |
| Promtail               | Daemon Set (will be deployed in every node) | <p>CPU : 200m<br>Memory : 128 Mi</p> |
| Loki                   | 1 pod                                       | <p>CPU : 100m<br>Memory : 128 Mi</p> |
| Grafana                | 1 pod                                       | <p>CPU : 100m<br>Memory : 128 Mi</p> |
| Control Center         | 1 pod                                       | <p>CPU : 100m<br>Memory : 100 Mi</p> |
| Hyperswitch Demo Store | 1 pod                                       | <p>CPU : 100m<br>Memory : 100 Mi</p> |

### Architecture Diagram

<figure><img src="../../.gitbook/assets/K8S Helm Charts (13).png" alt=""><figcaption></figcaption></figure>

## Next step:

{% content-ref url="../account-setup/" %}
[account-setup](../account-setup/)
{% endcontent-ref %}

{% content-ref url="../../explore-hyperswitch/payment-orchestration/quickstart/connectors/test-a-payment-with-connector.md" %}
[test-a-payment-with-connector.md](../../explore-hyperswitch/payment-orchestration/quickstart/connectors/test-a-payment-with-connector.md)
{% endcontent-ref %}

###

### Explore Further

Once you are done with the test payment, you can explore more about these:

<table data-card-size="large" data-view="cards"><thead><tr><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><mark style="color:blue;"><strong>How to set up routing rules</strong></mark></td><td><a href="../../explore-hyperswitch/payment-orchestration/smart-router.md">smart-router.md</a></td></tr><tr><td><mark style="color:blue;"><strong>How to integrate Hyperswitch with your app</strong></mark></td><td><a href="../../explore-hyperswitch/merchant-controls/integration-guide/">integration-guide</a></td></tr><tr><td><mark style="color:blue;"><strong>List of supported payment processors and payment methods</strong></mark></td><td><a href="https://hyperswitch.io/pm-list">https://hyperswitch.io/pm-list</a></td></tr><tr><td><mark style="color:blue;"><strong>AI Powered observability to reduce cost</strong></mark></td><td><a href="../../about-hyperswitch/payments-modules/ai-powered-cost-observability/">ai-powered-cost-observability</a></td></tr></tbody></table>
