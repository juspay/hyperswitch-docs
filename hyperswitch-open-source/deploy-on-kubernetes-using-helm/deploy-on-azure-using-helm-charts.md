# Deploy on Azure Using Helm Charts

#### Prerequisites

Ensure the following tools are installed and configured:

**1. Azure CLI**

The Azure Command-Line Interface (CLI) is a cross-platform tool that allows you to manage Azure resources. To install please visit the[ official Microsoft ](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)documentation.

**2. kubectl**

`kubectl` is the command-line tool for interacting with Kubernetes clusters. To install `kubectl` please refer to the [Kubernetes documentation](https://kubernetes.io/docs/tasks/tools/).

**3. Helm**

Helm is a package manager for Kubernetes applications. To install please refer to [helm documentation](https://helm.sh/docs/intro/install/#through-package-managers).

### **Part 1: Setting Up AKS**

1.  **Log In to Azure**

    Authenticate with your Azure account:

    ```bash
    az login
    ```

    Follow the browser prompts to log in.
2.  **Create a Resource Group**

    Create a resource group to manage your AKS cluster. Replace `<resource-group-name>` with your desired resource group name and `<location>` with your preferred Azure region (e.g., `eastus`):

    ```bash
    az group create --name <resource-group-name> --location <location>
    ```
3.  **Enable Microsoft Compute Service**

    Register the required resource provider:

    ```bash
    az provider register --namespace Microsoft.Compute
    ```
4.  **Create an AKS Cluster**

    Create an AKS cluster with your specified parameters. Replace `<resource-group-name>` with your resource group name, `<cluster-name>` with your desired AKS cluster name, and adjust other parameters as needed:

    ```bash
    az aks create --resource-group <resource-group-name> \
        --name <cluster-name> \
        --node-count 1 \
        --node-vm-size Standard_A4_v2 \
        --enable-managed-identity \
        --generate-ssh-keys
    ```

    _Note_: The `--generate-ssh-keys` parameter will create SSH keys if they do not already exist.
5.  **Connect to the AKS Cluster**

    Retrieve credentials to configure `kubectl`:

    ```bash
    az aks get-credentials --resource-group <resource-group-name> --name <cluster-name>
    ```

    Verify the connection to the cluster:

    ```bash
    kubectl get nodes
    ```

### **Part 2: Deploy Hyperswitch Using Helm**

1.  **Add the Hyperswitch Helm Repository**

    ```bash
    helm repo add hyperswitch https://juspay.github.io/hyperswitch-helm
    ```

    Update the repository to fetch the latest charts:

    ```bash
    helm repo update
    ```
2. **Prepare the Kubernetes Cluster**
   *   **Label the Node for Hyperswitch**:

       Replace `<node-name>` with the name of your node (use `kubectl get nodes` to find it):

       ```bash
       kubectl label nodes <node-name> node-type=generic-compute
       ```
   *   **Create a Namespace**:

       Create a dedicated namespace for Hyperswitch. Replace `<namespace>` with your desired namespace name:

       ```bash
       kubectl create namespace <namespace>
       ```
3.  **Install Hyperswitch**

    Deploy Hyperswitch using Helm. Replace `<release-name>` with your desired release name and `<namespace>` with the namespace you created:

    ```bash
    helm install <release-name> hyperswitch/hyperswitch-stack -n <namespace>
    ```
4. **Verify Installation**
   *   **Check Pod Status**:

       Ensure all pods are in the `Running` state:

       ```bash
       kubectl get pods -n <namespace>
       ```
   *   **Check Helm Release**:

       Verify the Helm release:

       ```bash
       helm list -n <namespace>
       ```

{% hint style="success" %}
That's it! Hyperswitch should be up and running on your Azure account 🎉 🎉
{% endhint %}

### **Accessing Services**

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

### **Uninstall Hyperswitch & Delete AKS Cluster**

To uninstall Hyperswitch:

```sh
helm uninstall <release-name> -n <namespace>
```

To delete the AKS cluster completely:

```sh
az aks delete --name <cluster-name> --resource-group <resource-group> --yes --no-wai
```

By replacing placeholders like `<resource-group-name>`, `<cluster-name>`, `<node-name>`, `<namespace>`, and `<release-name>` with your preferred names.

## Test a payment

#### Make a payment using our Demo App

Use the Hyperswitch Demo app and [make a payment with test card](https://opensource.hyperswitch.io/hyperswitch-open-source/test-a-payment).

Refer our [postman collection](https://www.postman.com/hyperswitch/workspace/hyperswitch/folder/25176183-0103918c-6611-459b-9faf-354dee8e4437) to try out REST APIs

### Explore Further

Once you are done with the test payment, you can explore more about these:

<table data-card-size="large" data-view="cards"><thead><tr><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><mark style="color:blue;"><strong>How to set up routing rules</strong></mark></td><td><a href="../../explore-hyperswitch/payment-flows-and-management/smart-router/">smart-router</a></td></tr><tr><td><mark style="color:blue;"><strong>How to integrate Hyperswitch with your app</strong></mark></td><td><a href="../../explore-hyperswitch/merchant-controls/integration-guide/">integration-guide</a></td></tr><tr><td><mark style="color:blue;"><strong>List of supported payment processors and payment methods</strong></mark></td><td><a href="https://hyperswitch.io/pm-list">https://hyperswitch.io/pm-list</a></td></tr><tr><td><mark style="color:blue;"><strong>AI Powered observability to reduce cost</strong></mark></td><td><a href="../../about-hyperswitch/payments-modules/ai-powered-cost-observability.md">ai-powered-cost-observability.md</a></td></tr></tbody></table>
