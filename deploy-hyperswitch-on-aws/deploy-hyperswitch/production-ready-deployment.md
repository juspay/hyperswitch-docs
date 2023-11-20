---
description: Use our CDK script to deploy our production-ready K8s setup inside your stack
---

# Production ready deployment

{% hint style="info" %}
In this chapter, you will deploy Hyperswitch server on AWS cloud. You can either try out a quick standalone deployment or a more scalable production ready setup
{% endhint %}

***

## Video

{% embed url="https://youtu.be/H9el_IHsd2g" %}

## Production ready deployment

### This setup includes:

| Component       | Instance Type  | Default Configuration |
| --------------- | -------------- | --------------------- |
| EKS (1 Cluster) | t3.medium      | 2 Nodes               |
| Load Balancer   | Application LB | 2 LBs                 |
| RDS             | t4g.medium     | 1 cluster             |
| ElasticCache    | t4g.medium     | 1 cluster             |

The following services will be installed in the 2 Nodes inside your EKS cluster

| Service Name           | Number of Pods                              | Default Configuration                |
| ---------------------- | ------------------------------------------- | ------------------------------------ |
| Hyperswitch App Server | 3 pods                                      | <p>CPU : 400m<br>Memory : 500 Mi</p> |
| Producer (Scheduler)   | 1 pod                                       | <p>CPU : 100m<br>Memory : 100 Mi</p> |
| Consumer (Scheduler)   | 2 pods                                      | <p>CPU : 100m<br>Memory : 100 Mi</p> |
| Promtail               | Daemon Set (will be deployed in every node) | <p>CPU : 200m<br>Memory : 128 Mi</p> |
| Loki                   | 1 pod                                       | <p>CPU : 100m<br>Memory : 128 Mi</p> |
| Grafana                | 1 pod                                       | <p>CPU : 100m<br>Memory : 128 Mi</p> |



<figure><img src="../../.gitbook/assets/K8S Helm Charts (4).png" alt=""><figcaption></figcaption></figure>

## Steps to Deploy Hyperswitch on AWS

### **What do you need to get started**

* An AWS user account with admin access (you can create an account [here](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?refid=em\_127222) if you do not have one)
* `git` installed on your local machine

<details>

<summary>Optional - Create a new user with Admin access (if you do not have a non-root user)</summary>

Follow the steps mentioned in this [guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/id\_users\_create.html#id\_users\_create\_console) and create a new user in your AWS account. While setting permissions, provide admin access to the user as shown below

<img src="../../.gitbook/assets/image (68).png" alt="" data-size="original">

</details>

#### Step 1 - Configure your AWS credentials in your terminal

For this step you would need the following from your AWS account

1. Preferred AWS region
2. Access key ID
3. Secret Access Key
4. Session Token (if you MFA set up)

You can create or manage your access keys from `IAM > Users` inside your AWS Console. For more information, [click here](https://docs.aws.amazon.com/IAM/latest/UserGuide/id\_credentials\_access-keys.html#Using\_CreateAccessKey)

<figure><img src="../../.gitbook/assets/Screenshot 2023-11-02 at 5.48.06 PM.png" alt=""><figcaption></figcaption></figure>

Once you have the keys run the below command

```json
export AWS_DEFAULT_REGION=<Your AWS_REGION> // e.g., export AWS_DEFAULT_REGION=us-east-2
export AWS_ACCESS_KEY_ID=<Your Access_Key_Id> // e.g., export AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
export AWS_SECRET_ACCESS_KEY=<Your Secret_Access_Key> // e.g., export AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
export AWS_SESSION_TOKEN="<Your AWS_SESSION_TOKEN>" //optional
```

#### Step 2 - Deploy Hyperswitch application

Run the below commands in the same terminal session

```bash
git clone https://github.com/juspay/hyperswitch-cdk.git
cd hyperswitch-cdk
sh install.sh
```

Once the script is run you will have to configure the following

1. DB password (should be more than 8 chars)
2. Admin Api key for Hyperswitch APIs&#x20;

{% hint style="warning" %}
Make sure to save the passwords you provide while running the script
{% endhint %}

On successful execution of the script, you will receive the following outputs

| Output                      | What is it used for                                                                                                           |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Hostname of the app server  | Access the application's APIs using the given base URL                                                                        |
| Hostname of the log server  | View real-time logs for all processes                                                                                         |
| Control Center URL          | Access the Hyperswitch control center and explore multiple settings                                                           |
| Hyperloader.js URL          | Use the `hyperloader` to [integrate our web client](../../going-live/integrate-web-client-on-your-web-app.md) in your website |
| Demo App URL                | Test payments quickly using our web checkout in the demo store                                                                |

{% hint style="success" %}
That's it! Hyperswitch should be up and running on your AWS account

Verify the health of the application by hitting `http://<host>/health`. The expected response is 'health is good'
{% endhint %}

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
11. **How can I monitor the performance and health of Hyperswitch on EKS?** You can Use AWS CloudWatch, Prometheus, or other monitoring solutions to track performance metrics and set up alerts. Refer [our guide](../../going-live/monitoring.md) for more information
12. **Is there a recommended backup and disaster recovery strategy for Hyperswitch and associated AWS resources?** Yes, it's essential to implement regular backups for RDS and have a disaster recovery plan in place. AWS provides tools and services for this purpose.
13. **Are there any specific security considerations when deploying Hyperswitch on AWS EKS?** You should follow our [best practices](../../going-live/security.md) for securing your EKS cluster and your Hyperswitch application, including network policies, IAM roles, and encryption.
14. **How do I upgrade Hyperswitch and its dependencies on EKS?** We will be providing an update CDK script soon
15. **What do I do if I encounter issues during the deployment process?** If you encounter issues, consult the troubleshooting section of the documentation or [reach out to our support team](https://hyperswitch.io/contact) for assistance.
16. **Where can I find further documentation on Hyperswitch?** You can find additional documentation, tutorials, and support resources on our website and in our api docs.

</details>
