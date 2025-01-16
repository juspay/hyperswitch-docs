---
icon: dharmachakra
description: Install Hyperswitch on your K8s setup using our Helm charts
---

# Deploy Hyperswitch on Kubernetes

## Part 1: Setting Up a Kubernetes Cluster on GCP

### Step 1: Set Up GCP Account and Enable Kubernetes Engine API

1. **Sign In to Google Cloud Console**:
   * Go to the Google Cloud Console.
2. **Create a Project**:
   * Click **Create Project**, provide a project name, and click **Create**.
   * If using an existing project, note the project ID for later use.
3. **Enable Kubernetes Engine API**:
   * Navigate to **APIs & Services > Library**.
   * Search for **Kubernetes Engine API** and click **Enable**.

### Step 2: Install Required Tools

1. **Install Google Cloud SDK**:
   *   On macOS:

       ```bash
       brew install --cask google-cloud-sdk
       ```
   * For Linux and Windows, refer to Google Cloud SDK installation guide.
2. **Initialize `gcloud` CLI**:
   *   Authenticate and configure your project:

       ```bash
       gcloud init
       ```
   * Follow the prompts to log in, select your project, and set a default compute region/zone.
3. **Install kubectl**:
   *   Use `gcloud` to install Kubernetes CLI:

       ```bash
       gcloud components install kubectl
       ```

### Step 3: Create a Kubernetes Cluster

1. **Create the Cluster**:
   *   Run the following command to create a Kubernetes cluster:

       ```bash
       gcloud container clusters create <CLUSTER_NAME> \
           --zone <ZONE> \
           --num-nodes <NUMBER_OF_NODES> \
           --machine-type e2-standard-4
       ```

       Replace:

       * `<CLUSTER_NAME>`: A unique name for your cluster.
       * `<ZONE>`: The GCP zone (e.g., `us-central1-a`).
       * `<NUMBER_OF_NODES>`: Number of nodes in your cluster.
       * `e2-standard-4`: Machine type with 4 CPUs and 16GB RAM per node.

       Example:

       ```bash
       gcloud container clusters create hypers-cluster \
           --zone us-central1-a \
           --num-nodes 3 \
           --machine-type e2-standard-4
       ```
2. **Verify the Cluster**:
   *   Fetch cluster credentials to allow `kubectl` to interact with it:

       ```bash
       gcloud container clusters get-credentials <CLUSTER_NAME> --zone <ZONE>
       ```
   *   Confirm the nodes are ready:

       ```bash
       kubectl get nodes
       ```

## Part 2: Deploy Hyperswitch on Kubernetes Using Helm

### Step 1: Add and Update the Hyperswitch Helm Repository

1.  Add the Hyperswitch Helm repository:

    ```bash
    helm repo add hyperswitch https://juspay.github.io/hyperswitch-helm
    ```
2.  Update Helm repository to fetch the latest charts:

    ```bash
    helm repo update
    ```

### Step 2: Prepare the Kubernetes Cluster

1. **Label Kubernetes Nodes**:
   * Ensure nodes meet the minimum requirements: **4 CPUs and 6GB memory**.&#x20;
   *   Label your nodes:

       ```bash
       kubectl label nodes <your-node-name> node-type=generic-compute
       ```
   *   List nodes to confirm labels:

       ```bash
       kubectl get nodes --show-labels
       ```
2. **Create a Namespace**:
   *   Create a dedicated namespace for Hyperswitch:

       ```bash
       kubectl create namespace hyperswitch
       ```

### Step 3: Install Hyperswitch

1.  Install Hyperswitch services using Helm:

    ```bash
    helm install hypers-v1 hyperswitch/hyperswitch-stack -n hyperswitch
    ```
2. Verify the Deployment:
   *   Check the status of all deployed pods:

       ```bash
       kubectl get pods -n hyperswitch
       ```
   * Ensure all pods are in the `Running` state.

{% hint style="success" %}
That's it! Hyperswitch should be up and running on your AWS account 🎉 🎉
{% endhint %}

## Post-Deployment Checklist

After deploying the Helm chart, you should verify that everything is working correctly

### App Server

* [ ] &#x20;Check that `hyperswitch_server/health` returns `health is good`

### Control Center

* [ ] &#x20;Verify if you are able to sign in or sign up
* [ ] &#x20;Verify if you are able to [create API key](https://opensource.hyperswitch.io/run-hyperswitch-locally/account-setup/using-hyperswitch-control-center#user-content-create-an-api-key)
* [ ] &#x20;Verify if you are able to [configure a new payment processor](https://opensource.hyperswitch.io/run-hyperswitch-locally/account-setup/using-hyperswitch-control-center#add-a-payment-processor)

### Test a payment

#### Step 1 - Make a payment using our Demo App

Use the Hyperswitch Demo app and [make a payment with test card](https://opensource.hyperswitch.io/hyperswitch-open-source/test-a-payment).

Refer our [postman collection](https://www.postman.com/hyperswitch/workspace/hyperswitch/folder/25176183-0103918c-6611-459b-9faf-354dee8e4437) to try out REST APIs

#### Step 2 - Deploy card vault

If you intend to save cards of your customers for future usage then you need a Card Vault. This helm chart doesn't cover inbuilt card vault support as it will violate PCI compliance. You can install manually by following the steps [here](https://opensource.hyperswitch.io/going-live/pci-compliance/card-vault-installation) or use [this doc to deploy card vault in aws](https://opensource.hyperswitch.io/hyperswitch-open-source/deploy-hyperswitch-on-aws/deploy-card-vault)

### Contribution guidelines

When you want others to use the changes you have added you need to package it and then index it

```
helm package .
helm repo index . --url https://juspay.github.io/hyperswitch-helm
```

#### Get Repo Info

```
helm repo add hyperswitch-helm https://juspay.github.io/hyperswitch-helm
helm repo update
```

## Next step:

{% content-ref url="account-setup/" %}
[account-setup](account-setup/)
{% endcontent-ref %}
