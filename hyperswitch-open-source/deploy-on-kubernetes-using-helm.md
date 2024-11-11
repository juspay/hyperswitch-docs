---
description: Install Hyperswitch on your K8s setup using our Helm charts
icon: dharmachakra
---

# Deploy Hyperswitch on Kubernetes

{% hint style="info" %}
This section outlines cloud-provider agnostic deployment steps for easy installation of the Hyperswitch stack on your K8s cluster
{% endhint %}

## Prerequisites

1. Active Redis service
2. Create a Postgres database and run the schema migration using the below commands

{% code fullWidth="false" %}
```bash
git clone https://github.com/juspay/hyperswitch.git
diesel migration --database-url postgres://{{user}}:{{password}}@{{host_name}}:5432/{{db_name}} run
```
{% endcode %}

3. Kubernetes Cluster
4. Add the following label to your node group &#x20;

```
node-type: generic-compute
```

{% hint style="info" %}
The concept of a "Node group" is a term used in both AWS and GCP to describe a collection of nodes within a cluster. In Azure, however, this is referred to as a "Node pool" within the hierarchy
{% endhint %}

5. Create a namespace `hyperswitch` in your kubernetes cluster using the below commands

```
kubectl create namespace hyperswitch
```

6. Load Balancer Controller Service specific to your Kubernetes cluster provider

{% hint style="info" %}
On Amazon Web Services (AWS) Cloud, deploy the [AWS Load Balancer Controller](https://docs.aws.amazon.com/eks/latest/userguide/aws-load-balancer-controller.html)\
On Azure Cloud, utilize the [Application Gateway Ingress Controller](https://learn.microsoft.com/en-us/azure/application-gateway/ingress-controller-overview)\
On Google Cloud Platform (GCP), deploy the [GKE Ingress Controller](https://cloud.google.com/compute/docs/labeling-resources)
{% endhint %}

## Installation

### Step 1 - Clone repo and Update Configurations

Clone the [hyperswitch-stack](https://github.com/juspay/hyperswitch-helm) repo and start updating the configs

```
git clone https://github.com/juspay/hyperswitch-helm.git
cd hyperswitch-helm/charts/incubator/hyperswitch-stack
```

### Step 2 - Install Hyperswitch

Before installing the service make sure you label your kubernetes nodes and create a namespace `hyperswitch`

```
kubectl label nodes <your-node-name> node-type=generic-compute
kubectl create namespace hyperswitch
```

Use below command to install hyperswitch services with above configs

```
helm install hyperswitch-v1 . -n hyperswitch
```

{% hint style="success" %}
That's it! Hyperswitch should be up and running on your AWS account 🎉 🎉
{% endhint %}

## Post-Deployment Checklist

After deploying the Helm chart, you should verify that everything is working correctly

#### App Server

* [ ] &#x20;Check that `hyperswitch_server/health` returns `health is good`

#### Control Center

* [ ] &#x20;Verify if you are able to sign in or sign up
* [ ] &#x20;Verify if you are able to [create API key](https://opensource.hyperswitch.io/run-hyperswitch-locally/account-setup/using-hyperswitch-control-center#user-content-create-an-api-key)
* [ ] &#x20;Verify if you are able to [configure a new payment processor](https://opensource.hyperswitch.io/run-hyperswitch-locally/account-setup/using-hyperswitch-control-center#add-a-payment-processor)

## Test a payment

### Step 1 - Deploy card vault

#### Card Vault Installation

If you intend to save cards of your customers for future usage then you need a Card Vault. This helm chart doesn't cover inbuilt card vault support as it will violate PCI compliance. You can install manually by following the steps [here](https://opensource.hyperswitch.io/going-live/pci-compliance/card-vault-installation) or use [this doc to deploy card vault in aws](https://opensource.hyperswitch.io/hyperswitch-open-source/deploy-hyperswitch-on-aws/deploy-card-vault)

### Step 2 - Make a payment using our Demo App

Use the Hyperswitch Demo app and [make a payment with test card](https://opensource.hyperswitch.io/hyperswitch-open-source/test-a-payment).

Refer our [postman collection](https://www.postman.com/hyperswitch/workspace/hyperswitch/folder/25176183-0103918c-6611-459b-9faf-354dee8e4437) to try out REST APIs

## Contribution guidelines

When you want others to use the changes you have added you need to package it and then index it

```
helm package .
helm repo index . --url https://juspay.github.io/hyperswitch-helm
```

### Get Repo Info

```
helm repo add hyperswitch-helm https://juspay.github.io/hyperswitch-helm
helm repo update
```

## Next step:

{% content-ref url="account-setup/" %}
[account-setup](account-setup/)
{% endcontent-ref %}
