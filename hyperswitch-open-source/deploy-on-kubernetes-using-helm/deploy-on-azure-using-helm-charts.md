# Deploy on Azure Using Helm Charts

### Prerequisites

Ensure the following tools are installed and configured:

**1. Azure CLI**

The Azure Command-Line Interface (CLI) is a cross-platform tool that allows you to manage Azure resources. To install please visit the[ official Microsoft ](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)documentation.

Before setting up AKS, you'll need to [create an Azure account](https://signup.azure.com/signup?offer=ms-azr-0044p\&appId=102\&ref=\&redirectURL=https:%2F%2Fazure.microsoft.com%2Fget-started%2Fwelcome-to-azure%3Fsrc%3Dacom_free\&l=en-us). Simply follow the on-screen instructions. Note that billing information will be required during the sign-up process.

**2. kubectl**

`kubectl` is the command-line tool for interacting with Kubernetes clusters. To install `kubectl` please refer to the [Kubernetes documentation](https://kubernetes.io/docs/tasks/tools/).

**3. Helm**

Helm is a package manager for Kubernetes applications. To install please refer to [helm documentation](https://helm.sh/docs/intro/install/#through-package-managers).

### **Part 1: Setting Up AKS**

1. **Log In to Azure**

Authenticate with your Azure account:

```bash
az login
```

Follow the browser prompts to log in.

2. **Create a Resource Group**

Before provisioning your AKS cluster, create a resource group to organize and manage related resources.

Use the following command, replacing `<resource-group-name>` with your desired name and `<location>` with your preferred Azure region (e.g., `eastus`):

```bash
az group create --name <resource-group-name> --location <location>
```

&#x20;**Example:**

```bash
az group create --name myAKSResourceGroup --location eastus
```

This will create a new resource group named `myAKSResourceGroup` in the `eastus` region.

3. **Enable the Microsoft.Compute Resource Provider**

To use AKS, you must register the `Microsoft.Compute` resource provider:

```bash
az provider register --namespace Microsoft.Compute
```

If the registration state shows `"Registering"`, wait a few minutes for it to complete. You can check the current state with:

```bash
az provider show --namespace Microsoft.Compute --query "registrationState"
```

Proceed once the status returns `"Registered"`.

4. **Register the Operational Insights Resource Provider**

To enable monitoring features in AKS, register the `Microsoft.OperationalInsights` provider:

```bash
az provider register --namespace Microsoft.OperationalInsights
```

You can check the registration status with:

```bash
az provider show --namespace Microsoft.OperationalInsights --query "registrationState"
```

Wait until the status shows `"Registered"` before proceeding.

5. **Register the Microsoft.ContainerService Provider**

Before creating your AKS cluster, you must register the `Microsoft.ContainerService` resource provider, which is required to manage Kubernetes clusters in Azure.

Run the following command:

```bash
az provider register --namespace Microsoft.ContainerService
```

Then check the registration status:

```bash
az provider show --namespace Microsoft.ContainerService --query "registrationState"
```

Wait until the output returns:

```bash
"Registered"
```

Once it's registered, you can proceed with creating your AKS cluster.

6. **Create an AKS Cluster**

Create an AKS cluster with your specified parameters. Replace `<resource-group-name>` with your resource group name, `<cluster-name>` with your desired AKS cluster name, and adjust other parameters as needed:

```bash
az aks create --resource-group <resource-group-name> \
    --name <cluster-name> \
    --node-count 1 \
    --node-vm-size Standard_A4_v2 \
    --enable-managed-identity \
    --generate-ssh-keys
```

_For example:_&#x20;

```
az aks create \
  --resource-group myAKSResourceGroup \
  --name myAKSCluster \
  --node-count 1 \
  --node-vm-size Standard_A4_v2 \
  --enable-managed-identity \
  --generate-ssh-keys
```

_Note_: The `--generate-ssh-keys` parameter will create SSH keys if they do not already exist.

7. **Connect to the AKS Cluster**

Once your AKS cluster is created, you can connect to it using `kubectl`.

8. &#x20;**Retrieve the cluster credentials:**

This command configures your local `kubectl` context to interact with the AKS cluster:

```bash
az aks get-credentials --resource-group myAKSResourceGroup --name myAKSCluster
```

9. **Verify the connection:**

Run the following to ensure you're connected and the node is active:

```bash
kubectl get nodes
```

You should see an output similar to the one below. Make sure to note the **Name** of your node.  You’ll need it in Part 2

```
NAME                                STATUS   ROLES    AGE    VERSION
aks-nodepool1-40058682-vmss000000   Ready    <none>   3m6s   v1.31.8
```

You should see your AKS node listed in the output. If so, you're now connected and ready to deploy to your cluster!

### **Part 2: Deploy Hyperswitch Using Helm**

1. **Add the Hyperswitch Helm Repository**

```bash
helm repo add hyperswitch https://juspay.github.io/hyperswitch-helm
```

Update the repository to fetch the latest charts:

```bash
helm repo update
```

2. **Prepare the Kubernetes Cluster**

* **Label the Node for Hyperswitch**:

Replace `<node-name>` with the name of your node (use `kubectl get nodes` to find it). We saved the name on  Part I, Step 7.&#x20;

```bash
kubectl label nodes <node-name> node-type=generic-compute
```

For example:&#x20;

```
kubectl label nodes aks-nodepool1-40058682-vmss000000 node-type=generic-compute
```

* **Create a Namespace**:

Namespaces help organize and isolate resources within your Kubernetes cluster. To create a new namespace, use the following command:

```bash
kubectl create namespace <namespace>
```

**Example:**

```bash
kubectl create namespace hyperswitch
```

This creates a namespace called `hyperswitch-dev` where you can deploy and manage related workloads separately from other environments.

3. **Install Hyperswitch**

Use Helm to deploy Hyperswitch into your Kubernetes cluster. Replace `<release-name>` with your chosen release name and `<namespace>` with the namespace you previously created:

```bash
helm install <release-name> hyperswitch/hyperswitch-stack -n <namespace>
```

**Example:**

```bash
helm install hyperswitch-dev hyperswitch/hyperswitch-stack -n hyperswitch
```

This command installs the Hyperswitch stack into the specified namespace, allowing you to manage and upgrade the deployment easily through Helm.

4. **Verify Installation**

* **Check Pod Status**:

Ensure all pods are in the `Running` state:

```bash
kubectl get pods -n <namespace>
```

**Example:**

```
kubectl get pods -n hyperswitch
```

* **Check Helm Release**:

```bash
helm list -n <namespace>
```

**Example:**

```
helm list -n hyperswitch
```

That's it! Hyperswitch should be up and running on your Azure account 🎉&#x20;

### Expose Hyperswitch Services Locally&#x20;

Use the following command for port-forwarding to access the services. Replace `<namespace>` with your namespace:

```bash
kubectl port-forward service/hyperswitch-server 8080:80 -n <namespace> > /dev/null 2>&1 & \
kubectl port-forward service/hyperswitch-control-center 9000:80 -n <namespace> > /dev/null 2>&1 & \
kubectl port-forward service/hyperswitch-web 9050:9050 -n <namespace> > /dev/null 2>&1 & \
kubectl port-forward service/<release-name>-grafana 3000:80 -n <namespace> > /dev/null 2>&1 & \
kubectl port-forward service/<release-name>-vector 3103:3103 -n <namespace> > /dev/null 2>&1 & \
kubectl port-forward service/mailhog 8025:8025 -n <namespace> > /dev/null 2>&1 &
```

Access the services at:

* App server: [http://localhost:8080](http://localhost:8080)
* Control center: [http://localhost:9000](http://localhost:9000)
* Hyperswitch Web: [http://localhost:9050/HyperLoader.js](http://localhost:9050/HyperLoader.js)
* Grafana: [http://localhost:3000](http://localhost:3000)
* Vector: [http://localhost:3103](http://localhost:3103)
* Mailhog: [http://localhost:8025](http://localhost:8025)

The quickest way to explore Hyperswitch is via the [Control Center](http://localhost:9000/). You can create an account or sign in with your email:

<figure><img src="../../.gitbook/assets/Screenshot 2025-05-20 at 5.02.02 PM.png" alt=""><figcaption></figcaption></figure>

A magic link will be sent to [Mailhog](http://localhost:8025/). Click on the link in white:

<figure><img src="../../.gitbook/assets/Screenshot 2025-05-20 at 5.13.10 PM.png" alt=""><figcaption></figcaption></figure>

Afterwards, you’ll be taken straight to the Control Center. If you're just taking things for a spin, feel free to skip authentication and start exploring right away.

### Test a payment

Use can now use the Hyperswitch Control Center and [make a payment with dummy card](https://opensource.hyperswitch.io/hyperswitch-open-source/test-a-payment).&#x20;

Refer our [postman collection](https://www.postman.com/hyperswitch/workspace/hyperswitch/folder/25176183-0103918c-6611-459b-9faf-354dee8e4437) to try out REST APIs.

### Explore Further

Once you are done with the test payment, you can explore more about these:

### **Uninstall Hyperswitch & Delete AKS Cluster**

1. **Uninstall Hyperswitch:**

```sh
helm uninstall <release-name> -n <namespace>
```

**Example**:

`helm uninstall hyperswitch -n hyperswitch`

2. **Delete the namespace:**

`kubectl delete namespace <namespace>`

**Example**:

`kubectl delete namespace hyperswitch`

3. **Delete the AKS cluster completely**:

```sh
az aks delete --name <cluster-name> --resource-group <resource-group> --yes --no-wai
```

**Example**:

```
az aks delete --resource-group myAKSResourceGroup --name myAKSCluster --yes
```

### **Troubleshooting**

*   **View Pod Logs**:

    To view logs for a specific pod:

    ```bash
    kubectl logs <pod-name> -n <namespace>
    ```
*   **View Events**:

    To view events in the namespace:

    ```bash
    kubectl get events -n <namespace> --sort-by='.metadata.creationTimestamp'
    ```
*   **Reinstall Chart**:

    If issues persist, uninstall and reinstall Hyperswitch:

    ```bash
    helm uninstall <release-name> -n <namespace>
    helm install <release-name> hyperswitch/hyperswitch-stack -n <namespace>
    ```

### **Customization & Configuration**

To customize Hyperswitch, clone the Helm chart repository and modify `values.yaml`:

```sh
git clone https://github.com/juspay/hyperswitch-helm.git
```

Update the `values.yaml` file inside `hyperswitch-stack/` and apply changes with:

```sh
helm upgrade --install <release-name> hyperswitch/hyperswitch-stack -n <namespace>
```



<table data-card-size="large" data-view="cards"><thead><tr><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><mark style="color:blue;"><strong>How to set up routing rules</strong></mark></td><td><a href="../../explore-hyperswitch/payment-orchestration/smart-router.md">smart-router.md</a></td></tr><tr><td><mark style="color:blue;"><strong>How to integrate Hyperswitch with your app</strong></mark></td><td><a href="../../explore-hyperswitch/merchant-controls/integration-guide/">integration-guide</a></td></tr><tr><td><mark style="color:blue;"><strong>List of supported payment processors and payment methods</strong></mark></td><td><a href="https://hyperswitch.io/pm-list">https://hyperswitch.io/pm-list</a></td></tr><tr><td><mark style="color:blue;"><strong>AI Powered observability to reduce cost</strong></mark></td><td><a href="../../about-hyperswitch/payments-modules/ai-powered-cost-observability.md">ai-powered-cost-observability.md</a></td></tr></tbody></table>
