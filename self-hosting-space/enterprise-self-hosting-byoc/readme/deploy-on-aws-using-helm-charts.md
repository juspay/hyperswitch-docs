# Deploy on AWS using Helm Charts

### Step 0: IAM Role Setup

All three IAM roles must be created before the EKS cluster is provisioned.

#### 0.1 Create Cluster IAM Role

Navigate to IAM Console > Roles > Create Role:

* Trusted Entity: AWS Service
* Use case: EKS — Cluster

**Policies to Attach**

| Policy Name                        | Purpose                                                                                                  |
| ---------------------------------- | -------------------------------------------------------------------------------------------------------- |
| AmazonEKSClusterPolicy             | Core EKS cluster management — grants the control plane permission to manage AWS resources on your behalf |
| AmazonEKSVPCResourceController     | Required for Security Groups for Pods; allows cluster to manage ENIs and IPs                             |
| AmazonEC2ContainerRegistryReadOnly | Allows the cluster to pull container images from ECR                                                     |
| AmazonEKS\_CNI\_Policy             | Enables VPC CNI networking for pod IP allocation                                                         |
| ElasticLoadBalancingFullAccess     | Required only if the AWS Load Balancer Controller add-on is installed                                    |

***

#### 0.2 Create Node IAM Role

Navigate to IAM Console > Roles > Create Role:

* Trusted Entity: AWS Service
* Use case: EC2

**Policies to Attach**

| Policy Name                        | Purpose                                                                             |
| ---------------------------------- | ----------------------------------------------------------------------------------- |
| AmazonEKSWorkerNodePolicy          | Allows EC2 nodes to register with the EKS cluster and perform node-level operations |
| AmazonEKS\_CNI\_Policy             | Enables the VPC CNI plugin to configure pod networking on nodes                     |
| AmazonEC2ContainerRegistryReadOnly | Allows nodes to pull container images from ECR                                      |

***

#### 0.3 Create EBS CSI Driver IAM Role (Pod Identity Role)

Navigate to IAM Console > Roles > Create Role:

* Trusted Entity Type: Custom trust policy:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "pods.eks.amazonaws.com"
      },
      "Action": [
        "sts:AssumeRole",
        "sts:TagSession"
      ]
    }
  ]
}
```

* Policies to Attach: AmazonEBSCSIDriverPolicy
* Role Name: AmazonEKSPodIdentityAmazonEBSCSIDriverRole

***

### Step 1: Create an EKS Cluster

#### 1.1 Create VPC Subnets (if not using an existing VPC)

Go to VPC Dashboard > Subnets > Create subnet:

* VPC: Choose your existing VPC (or create a new one first under VPC > Create VPC)
* Subnets: Create at least 2 subnets in different Availability Zones (AZs).
* CIDR Block Example:
* Subnet 1 (us-east-1a): 10.0.1.0/24
* Subnet 2 (us-east-1b): 10.0.2.0/24
* These CIDR blocks allow 256 IP addresses each, which is sufficient for many small to medium workloads.
* Ensure each subnet has Auto-assign public IPv4 address enabled (under subnet settings).<br>

{% hint style="info" %}
Tip: Choose AZs from the same region (e.g., us-east-1a, us-east-1b). This helps with high availability and proper node distribution.
{% endhint %}

#### 1.2 Create EKS Cluster

Navigate to EKS > Clusters > Add cluster > Create:

* Cluster Name: (e.g., hypers-cluster)
* Disable EKS Auto Mode
* Cluster Authentication Mode: EKS API and ConfigMap (Recommended)
* Cluster Endpoint Access: Public and Private

#### 1.3 Add Cluster Add-ons (during creation):

Enable the following:

* CoreDNS
* Kube-proxy
* Amazon VPC CNI
* Amazon EKS Pod Identity Agent
* Amazon EBS CSI Driver
* When selecting this, choose the IAM role AmazonEKSPodIdentityAmazonEBSCSIDriverRole created earlier
* External DNS (if required)

***

### Step 2: Create and Configure Node Group

#### 2.1 Navigate to Cluster > Compute > Add Node Group

* Name: hypers-node-group
* Select the Node IAM Role created earlier<br>

#### 2.2 Configure Node Group:

* Minimum Nodes: 4 (important to avoid Helm deadlocks)
* Instance Types: Select appropriate instance (e.g., t3.medium or higher)
* Subnets: Select the 2 subnets across different AZs created earlier

Wait for the node group to be fully created and active before proceeding.

***

### Step 3: Configure CLI Environment

#### 3.1 Set AWS Credentials

```
export AWS_ACCESS_KEY_ID=<Your_Access_Key_ID>
export AWS_SECRET_ACCESS_KEY=<Your_Secret_Access_Key>
export AWS_SESSION_TOKEN="<Your_AWS_SESSION_TOKEN>" # If using temporary credentials
```

#### 3.2 Connect kubectl to EKS Cluster

```
aws eks update-kubeconfig --name <cluster_name> --region <region_name>
```

#### 3.3 Apply Default Storage Class

Create a file storageclass.yaml with the following:

```
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: gp3
  annotations:
    storageclass.kubernetes.io/is-default-class: "true"
provisioner: ebs.csi.aws.com
parameters:
  type: gp3
reclaimPolicy: Delete
allowVolumeExpansion: true
volumeBindingMode: WaitForFirstConsumer
```

Apply the file:

```
kubectl apply -f storageclass.yaml
```

***

### Step 4: Install Hyperswitch via Helm

#### 4.1 Add Hyperswitch Helm Repo

```
helm repo add hyperswitch  https://juspay.github.io/hyperswitch-helm
helm repo update 
```

#### 4.2 Install the Hyperswitch Stack

```
helm install hypers-v1 hyperswitch/hyperswitch-stack -n hyperswitch --create-namespace
```

***

### Step 5: Access Hyperswitch Services

Use the commands from the **Step 4.2 (from above)** for port-forwarding to access the services.&#x20;

### Step 6: Cleanup and Uninstallation

To uninstall Hyperswitch and remove the namespace:

helm uninstall hypers-v1 -n hyperswitch

kubectl delete namespace hyperswitch

***

### Notes

* Ensure all IAM roles are correctly attached and selected during EKS cluster and addon setup.
* Having fewer than 4 nodes may cause timeout or deployment issues with Helm.
* You can view logs, pods, and service states using kubectl get pods -n hyperswitch, kubectl logs, and similar commands for debugging.

***

You are now ready to deploy and manage the Hyperswitch stack on AWS EKS using Helm via the AWS Console!
