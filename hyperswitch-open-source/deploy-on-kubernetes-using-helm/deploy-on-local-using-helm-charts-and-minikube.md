---
description: >-
  A step-by-step guide to deploying Hyperswitch locally using Helm and Minikube,
  with setup, access, cleanup, and troubleshooting instructions.
---

# Deploy on Local using Helm Charts and Minikube

## **Part 1: Setting Up a Local Kubernetes Cluster with Minikube/OrbStack**

### Option 1: Setting Up a Local Kubernetes Cluster with Minikube

#### **Step 1: Install Required Tools** <a href="#id-5nsuvyw3aien" id="id-5nsuvyw3aien"></a>

**a. kubectl**

kubectl is the CLI for interacting with Kubernetes clusters.\
To install it, refer to the official guide:[ Install kubectl](https://kubernetes.io/docs/tasks/tools/)

**b. Minikube**

Minikube is a local Kubernetes cluster for development/testing.\
Install Minikube following the official documentation:[ Install Minikube](https://minikube.sigs.k8s.io/docs/start/)

**c. Helm**

Helm is a package manager for Kubernetes applications.\
Install Helm using the instructions here:[ Install Helm](https://helm.sh/docs/intro/install/)

#### **Step 2: Start Minikube** <a href="#v4ghhsu6urci" id="v4ghhsu6urci"></a>

Start a Minikube cluster with sufficient resources:

```bash
minikube start --cpus=4 --memory=7900 --driver=docker
```

You can also use `--driver=virtualbox` or `--driver=hyperkit` depending on your system.

Verify the cluster is running:

```bash
kubectl get nodes
```

### Option 2: Setting Up a Local Kubernetes Cluster using OrbStack (Only for macOS)

**Step 1: Install Required Tools**

```
brew install helm
```

```
brew install orbstack  # Download the OrbStack application
```

**Step 2: Set Up Kubernetes in OrbStack**

1. Open the OrbStack application.
2. Navigate to the Pods section.
3. Enable Kubernetes from the settings.

## **Part 2: Deploy Hyperswitch on Kubernetes Using Helm** <a href="#jqgk5qw5bkgo" id="jqgk5qw5bkgo"></a>

#### **Step 1: Add and Update the Hyperswitch Helm Repository** <a href="#id-75zpwj4wb8db" id="id-75zpwj4wb8db"></a>

```bash
helm repo add hyperswitch https://juspay.github.io/hyperswitch-helm
helm repo update
```

#### **Step 2: Install Hyperswitch** <a href="#id-4ckek6lepkr2" id="id-4ckek6lepkr2"></a>

Install the Helm chart and create the namespace:

```
helm install hypers-v1 hyperswitch/hyperswitch-stack -n hyperswitch --create-namespace
```

Check the status of the pods:

```bash
kubectl get pods -n hyperswitch
```

{% hint style="success" %}
That's it! Hyperswitch should be up and running on your Minikube Cluster🎉 🎉
{% endhint %}

#### **Step 3: Accessing Services** <a href="#id-6pkposi9l5fl" id="id-6pkposi9l5fl"></a>

Expose services locally using port forwarding:

```bash
kubectl port-forward service/hyperswitch-server 8080:80 -n hyperswitch > /dev/null 2>&1 & \
kubectl port-forward service/hyperswitch-control-center 9000:80 -n hyperswitch > /dev/null 2>&1 & \
kubectl port-forward service/hyperswitch-web 9050:9050 -n hyperswitch > /dev/null 2>&1 & \
kubectl port-forward service/hypers-v1-grafana 3000:80 -n hyperswitch > /dev/null 2>&1 & \
kubectl port-forward service/hypers-v1-vector 3103:3103 -n hyperswitch > /dev/null 2>&1 & \
kubectl port-forward service/mailhog 8025:8025 -n hyperswitch > /dev/null 2>&1 &
```

Access services at:

* App server:[ http://localhost:8080](http://localhost:8080/)
* Control center:[ http://localhost:9000](http://localhost:9000/)
* Hyperswitch Web:[ http://localhost:9050/HyperLoader.js](http://localhost:9050/HyperLoader.js)
* Grafana:[ http://localhost:3000](http://localhost:3000/)
* Vector:[ http://localhost:3103](http://localhost:3103/)
* Mailhog:[ http://localhost:8025](http://localhost:8025/)

### **Cleanup** <a href="#id-13mcbknndl2h" id="id-13mcbknndl2h"></a>

To uninstall Hyperswitch and clean up the namespace:

```
helm uninstall hypers-v1 -n hyperswitch
kubectl delete namespace hyperswitch
```

### **Troubleshooting** <a href="#ywgi5rvuean2" id="ywgi5rvuean2"></a>

#### **View Pod Logs** <a href="#id-7wtmzixwrfeq" id="id-7wtmzixwrfeq"></a>

```bash
kubectl logs <pod-name> -n hyperswitch
```

#### **View Events** <a href="#ptykemgnnwf0" id="ptykemgnnwf0"></a>

```bash
kubectl get events -n hyperswitch --sort-by='.metadata.creationTimestamp'
```
