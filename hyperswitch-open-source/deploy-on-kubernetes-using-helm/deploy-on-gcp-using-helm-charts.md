# Deploy on GCP Using Helm Charts

## Part 1: Setting Up a Kubernetes Cluster on GCP

#### Step 1: Set Up GCP Account and Enable Kubernetes Engine API

1. **Sign In to Google Cloud Console**:
   * Go to the Google Cloud Console.
2. **Create a Project**:
   * Click **Create Project**, provide a project name, and click **Create**.
   * If using an existing project, note the project ID for later use.
3. **Enable Kubernetes Engine API**:
   * Navigate to **APIs & Services > Library**.
   * Search for **Kubernetes Engine API** and click **Enable**.

#### Step 2: Install Required Tools

1.  **Google Cloud CLI (`gcloud`)**

    The Google Cloud Command-Line Interface (CLI) is a cross-platform tool that allows you to manage GCP resources. To install `gcloud`, please refer to the official Google[ Cloud SDK installation guide](https://cloud.google.com/sdk/docs/install).
2. **kubectl**\
   `kubectl` is the command-line tool for interacting with Kubernetes clusters. To install `kubectl`, please refer to the [Kubernetes documentation](https://pwittrock.github.io/docs/tasks/tools/install-kubectl/).
3.  **Helm**

    Helm is a package manager for Kubernetes applications. To install Helm, please refer to the [official Helm documentation](https://helm.sh/docs/intro/install/#through-package-managers).

#### Step 3: Create a Kubernetes Cluster

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
           --num-nodes 1 \
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

#### Step 1: Add and Update the Hyperswitch Helm Repository

1.  Add the Hyperswitch Helm repository:

    ```bash
    helm repo add hyperswitch https://juspay.github.io/hyperswitch-helm
    ```
2.  Update Helm repository to fetch the latest charts:

    ```bash
    helm repo update
    ```

#### Step 2: Prepare the Kubernetes Cluster

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
       kubectl create namespace <namespace>
       ```

#### Step 3: Install Hyperswitch

1. Deploy Hyperswitch using Helm. Replace `<release-name>` with your desired release name and `<namespace>` with the namespace you created:

```bash
helm install <release-name> hyperswitch/hyperswitch-stack -n <namespace>
```

2. Verify the Deployment:

*   Check the status of all deployed pods:

    ```bash
    kubectl get pods -n <namespace>
    ```
* Ensure all pods are in the `Running` state.

{% hint style="success" %}
That's it! Hyperswitch should be up and running on your GCP account 🎉 🎉
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

*   **View Pod Logs:**\
    To check logs for a specific pod in Google Kubernetes Engine (GKE):

    ```sh
    kubectl logs <pod-name> -n <namespace>
    ```
*   **View Events:**\
    To list events in the namespace sorted by creation time:

    ```sh
    kubectl get events -n <namespace> --sort-by='.metadata.creationTimestamp'
    ```
*   **Deploy Hyperswitch Helm Chart on GKE:**\
    If deploying for the first time or reinstalling, run:

    ```sh
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

### **Uninstall Hyperswitch & Delete GKE Cluster**

To uninstall Hyperswitch:

```sh
helm uninstall <release-name> -n <namespace>
```

To delete the GKE cluster completely:

```sh
gcloud container clusters delete <cluster-name> --region <region> --project <project-id> --quiet
```

### Test a payment

Use the Hyperswitch Control Center and [make a payment with test card](https://opensource.hyperswitch.io/hyperswitch-open-source/test-a-payment).

Refer our [postman collection](https://www.postman.com/hyperswitch/workspace/hyperswitch/folder/25176183-0103918c-6611-459b-9faf-354dee8e4437) to try out REST APIs.
