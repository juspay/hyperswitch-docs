---
metaLinks:
  alternates:
    - enterprise-deployment.md
---

# Enterprise Deployment

### Use Terraform to Provision and Maintain Infrastructure Resources

In case you are setting up your payments infrastructure on **Amazon Web Services** for the first time you can use **Juspay Hyperswitch’s Terraform configuration files** to do so.

**Using Terraform -**

Navigate to the Juspay Hyperswitch [Terraform Documentation](https://github.com/juspay/hyperswitch-suite/tree/main/terraform/aws) and refer to the **aws/live** folder for the type of environment you want to set up.

The documentation outlines the following:

* Terraform module architecture
* Services available
* Environment Types
* Steps to Deploy
* State Management
* Troubleshooting

{% hint style="info" %}
**Note:** Terraform needs to provision resources in the following order to ensure an error-free deployment -

1. Virtual Private Cloud (VPC)
2. Elastic Kubernetes Service (EKS)
3. Cloudfront
4. Rest of the resources
{% endhint %}

In case you are setting up your infrastructure on any other managed cloud providers you need to ensure the following resources are provisioned before you proceed with the Juspay Hyperswitch application installation -

* Kubernetes cluster + node pools
* Networking (VPC, subnets, firewall rules)
* Load balancer + ingress
* PostgreSQL database
* Redis cache
* Persistent storage
* Secrets management
* Monitoring/logging stack

### Deploying Juspay Hyperswitch

Juspay Hyperswitch can be installed in 3 different environments -

1. Production
2. Sandbox
3. Integration Test (integ)

The recommended method to install Juspay Hyperswitch is by running the Helm charts present in the **‘hyperswitch-helm’** repository. It contains the **‘values.yaml’** file that renders the configuration TOML file required by the application.

Since this is a Kubernetes installation the Helm chart and values.yaml file allow the merchant to modify the file based on their requirements and deploy their customized version of the application.

If not modified, the commands will install Juspay Hyperswitch with the default parameters.

#### 1. Add the Juspay Hyperswitch Helm Repository

`helm repo add hyperswitch https://juspay.github.io/hyperswitch-helm`

Update the repository to fetch the latest charts:

`helm repo update`

#### 2. Prepare the Kubernetes Cluster

Label the Node for Juspay Hyperswitch:

Replace \<node-name> with the name of your node (use kubectl get nodes to find it). We saved the name on Part I, Step 7.<br>

`kubectl label nodes <node-name> node-type=generic-compute`<br>

Example:

`kubectl label nodes aks-nodepool1-40058682-vmss000000 node-type=generic-compute`

#### 3. Create a Namespace

Namespaces help organize and isolate resources within your Kubernetes cluster. To create a new namespace, use the following command:<br>

`kubectl create namespace <namespace>`

Example:

`kubectl create namespace hyperswitch-dev`

This creates a namespace called hyperswitch-dev where you can deploy and manage related workloads separately from other environments.<br>

{% hint style="info" %}
**Note:** It is recommended that the merchant create a namespace for each of the environments they are deploying.
{% endhint %}

#### 4. Customize the Helm Chart

Please refer to the link for a standard **values.yaml** file in the hyperswitch-helm chart that needs to be modified for a production ready setup - [Link](https://github.com/juspay/hyperswitch-helm/blob/main/charts/incubator/hyperswitch-stack/values.yaml)

{% hint style="info" %}
**Note:** You can further customize each component of the stack by modifying the values.yaml file under each component folder. The component specific values file contains several more parameters compared to the standard values file and can give you more control over your deployment.
{% endhint %}

You can run the following command to see the default schema:

`helm show values hyperswitch/hyperswitch-stack`

After going through the file, the merchant can create minimal override files with the parameters they need customized for their deployment for each of the environments as follows -

* values-prod.yaml
* values-sandbox.yaml
* values-integ.yaml

These files will be passed as parameters in the next step to install the different Juspay Hyperswitch environments

Please reach out to the Juspay Hyperswitch team in case you need additional guidance on how to configure values.yaml for your environment.

{% hint style="info" %}
**Note:** The default helm chart provided in hyperswitch-helm repository populates values from bitnami, redisconf, postgres etc. and it may not be ready for merchants’ production environment requirements.
{% endhint %}

If the merchant is using the Community Edition of Juspay Hyperswitch it is recommended to review all the values in the values.yaml file prior to production installation.

#### 5. Install Juspay Hyperswitch

{% hint style="info" %}
**Note:** Please modify the ‘values.yaml’ file before this step as it will install Juspay Hyperswitch based on the configuration provided in the file.
{% endhint %}

There are 3 primary scenarios merchants can use to install Juspay Hyperswitch on Kubernetes:

1. All 3 environments in the same Kubernetes cluster under different namespaces
2. Production environment in a separate cluster and Integ and Sandbox in one cluster - Minimum recommended setup for enterprise deployments
3. All 3 environments in separate Kubernetes clusters - Strongest isolation and security

**Scenario-1**

Use Helm to deploy Juspay Hyperswitch into your Kubernetes cluster. You need to run this for each environment you are deploying.

Replace \<release-name> with your chosen release name and \<namespace> with the namespace you previously created based on the environment you are installing:

`helm install <release-name> hyperswitch/hyperswitch-stack -n <namespace>`

Example:

`helm install hyperswitch-dev hyperswitch/hyperswitch-stack -n hyperswitch-dev`

This command installs the Juspay Hyperswitch stack into the specified namespace, allowing you to manage and upgrade the deployment easily through Helm.

***

**Scenario-2**

To deploy Production environments in a separate cluster and Integ and Sandbox in another you need to first create the clusters and then switch context and install Juspay Hyperswitch in the specified namespace within the cluster.

The cluster can be created directly via the cloud provider or using Terraform. After creating the cluster run the following commands to switch cluster context and install Juspay Hyperswitch:

`kubectl config use-context <dev_integ-cluster>`

`helm install <dev-release-name> hyperswitch/hyperswitch-stack -n <dev-namespace> -f <values-dev.yaml>`

`kubectl config use-context <dev_integ-cluster>`

`helm install <integ-release-name> hyperswitch/hyperswitch-stack -n <integ-namespace> -f <values-integ.yaml>`

`kubectl config use-context <prod-cluster>`

`helm install <prod-release-name> hyperswitch/hyperswitch-stack -n <prod-namespace>-f <values-prod.yaml>`

This creates a Juspay Hyperswitch release for Dev and Integ in 2 different namespaces in the same cluster and a release for Prod in a separate namespace in a different cluster.

***

**Scenario-3**

In this case you deploy each release in a separate cluster with its own namespace

For Dev Release:

`kubectl config use-context dev-cluster`

`helm install <dev-release-name> hyperswitch/hyperswitch-stack -n <dev-namespace> -f <values-dev.yaml>`

For Integ Release:

`kubectl config use-context integ-cluster`

`helm install <integ-release-name> hyperswitch/hyperswitch-stack -n <integ-namespace> -f <values-staging.yaml>`

For Prod Release:

`kubectl config use-context prod-cluster`

`helm install <prod-release-name> hyperswitch/hyperswitch-stack -n <prod-namespace> -f <values-prod.yaml>`

This gives you maximum isolation between environments and ensures scaling, application or infrastructure issues in merchant Dev or Integ environments does not impact Production.

{% hint style="info" %}
**Note:** The above installation scenarios detail out guidance for Kubernetes level isolation.

For enterprise grade deployments merchants can deploy Production in a separate managed cloud account/tenant depending on their requirements.

This is the most optimal setup for large-scale deploymenets.
{% endhint %}

#### 6. Verify Installation

Check Pod Status:

Ensure all pods are in the Running state:

`kubectl get pods -n <namespace>`<br>

Example:

`kubectl get pods -n hyperswitch`

#### 7. Check Helm Release:

\
`helm list -n <namespace>`

Example:

`helm list -n hyperswitch`

Post completion of these steps Juspay Hyperswitch should be up and running in your environment.
