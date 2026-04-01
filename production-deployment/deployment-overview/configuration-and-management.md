# Configuration and Management

### Configuration Files 

In case you would like to use the configuration TOML files directly instead of using Helm Charts please refer to this [directory](https://github.com/juspay/hyperswitch/tree/main/config/deployments).

It contains the configs for deployments of Hyperswitch in the 3 different hosted environments:

* Integration Test
* Sandbox
* Production

### Setting Up ArgoCD for Enterprise GitOps & Drift Management

This section describes how to deploy **Argo CD** in a production Kubernetes environment to enable **GitOps-based deployment, configuration management, and drift detection.**

ArgoCD will act as the **deployment controller**, continuously reconciling Kubernetes resources with the configuration stored in Git.

The following prerequisites need to be in place:

* A Kubernetes cluster already exists
* Cluster access is configured (`kubectl` context)
* Helm is available

Infrastructure provisioning (networking, cluster, databases) should already be completed before this step.

#### 1. Deployment Architecture

#### 1.1 Deployment Model

ArgoCD should be deployed as a **platform service within the Kubernetes cluster**.

Recommended architecture:

* Deploy ArgoCD in a **dedicated namespace**
* Use **Helm-based installation**
* Run in **High Availability (HA) mode**
* Enable **SSO authentication**
* Enforce **RBAC**
* Enable **TLS**
* Enable **automated reconciliation and drift detection**

Production deployments should **not**:

* expose the ArgoCD UI over insecure HTTP
* rely on the default admin credentials
* grant unrestricted `cluster-admin` privileges to users

ArgoCD is a **platform-level component**, not application-specific. It will typically manage deployments for multiple services, including Hyperswitch.

#### 2. Installing ArgoCD (HA Setup)

ArgoCD will be installed using the official Helm chart.

#### 2.1 Create Namespace

```
kubectl create namespace argocd
```

This namespace will contain all ArgoCD components.

#### 2.2 Add Helm Repository

Add the official Helm repository:

```
helm repo add argo https://argoproj.github.io/argo-helm
helm repo update
```

#### 2.3 Create Enterprise Configuration (values.yaml)

Create a configuration file for the deployment.

Example: `argocd-values.yaml`

```yaml
global:
  domain: argocd.company.com

configs:
  params:
    server.insecure: false

  cm:
    exec.enabled: false
    timeout.reconciliation: 180s

  rbac:
    policy.default: role:readonly
    policy.csv: |
      p, role:platform-admin, applications, *, *, allow
      p, role:app-team, applications, get, */*, allow
      p, role:app-team, applications, sync, */*, allow
      g, platform-admins, role:platform-admin
      g, app-teams, role:app-team
```

#### Explanation of Important Settings

**Reconciliation interval**

```
timeout.reconciliation: 180s
```

ArgoCD checks for configuration drift approximately every 3 minutes.

**RBAC**

RBAC policies restrict who can:

* deploy applications
* trigger sync operations
* modify configurations

Organizations should integrate this with their identity provider groups.

#### 2.4 Enable High Availability

Production environments should run multiple replicas of core ArgoCD components.

```yaml
server:
  replicas: 3
  autoscaling:
    enabled: true
    minReplicas: 3
    maxReplicas: 6

controller:
  replicas: 3

repoServer:
  replicas: 3
```

#### Component Roles

| Component              | Purpose                |
| ---------------------- | ---------------------- |
| ArgoCD Server          | Web UI and API         |
| Application Controller | Reconciliation engine  |
| Repo Server            | Pulls Git repositories |

Running multiple replicas ensures availability if nodes fail.

#### 2.5 Redis Configuration

ArgoCD requires Redis for caching.

```yaml
redis:
  enabled: true
  ha:
    enabled: true
```

Important clarification:

This Redis instance is **only used internally by ArgoCD** and is **not related to Redis used by application workloads such as Hyperswitch**.

#### 2.6 Install ArgoCD

Deploy using Helm:

```
helm install argocd argo/argo-cd \
  --namespace argocd \
  -f argocd-values.yaml
```

#### Verify Installation

```
kubectl get pods -n argocd
```

Expected components:

```
argocd-server
argocd-repo-server
argocd-application-controller
redis
```

Replica counts may vary depending on HA configuration.

#### 3. Secure Exposure (Ingress + TLS)

ArgoCD must be exposed securely.

Most clusters use an ingress controller such as:

* NGINX Ingress Controller
* Traefik

#### 3.1 Install Ingress Controller (if not already present)

Example:

```
helm install ingress-nginx ingress-nginx/ingress-nginx
```

Your organization may already have an ingress controller deployed as part of the platform stack.

#### 3.2 Configure ArgoCD Ingress

Add to `values.yaml`:

```yaml
server:
  ingress:
    enabled: true
    ingressClassName: nginx
    hostname: argocd.company.com
    tls: true
```

#### TLS Options

TLS certificates may be provisioned using:

* internal certificate management systems
* Kubernetes certificate controllers
* external load balancer TLS termination

Minimum security requirements:

* TLS 1.2 or higher
* trusted certificate authority
* strong cipher suites

#### 4. Initial Login & Admin Hardening

Retrieve the initial admin password:

```
kubectl -n argocd get secret argocd-initial-admin-secret \
  -o jsonpath="{.data.password}" | base64 -d
```

Login:

```
argocd login argocd.company.com
```

Immediately perform the following actions:

* rotate the admin password
* configure SSO
* disable the admin user if SSO is enforced

#### Disable Admin User

After SSO is configured:

```yaml
configs:
  cm:
    admin.enabled: "false"
```

This prevents local credential-based access.

#### 5. SSO Integration

Most enterprises integrate ArgoCD with an identity provider using OIDC.

Example configuration:

```yaml
configs:
  cm:
    oidc.config: |
      name: Okta
      issuer: https://company.okta.com
      clientID: <client-id>
      clientSecret: $oidc.okta.clientSecret
      requestedScopes: ["openid", "profile", "email", "groups"]
```

Create the required secret:

```
kubectl create secret generic argocd-secret \
  -n argocd \
  --from-literal=oidc.okta.clientSecret=<secret>
```

Benefits:

* centralized identity management
* group-based RBAC
* removal of static credentials

#### 6. Connecting Git Repositories

ArgoCD must have read access to the configuration repository.

Two common approaches:

#### HTTPS

```
argocd repo add https://github.com/company/platform-config.git
```

#### SSH (preferred)

```
argocd repo add git@github.com:company/platform-config.git \
  --ssh-private-key-path ~/.ssh/id_rsa
```

Best practices:

* use read-only deploy keys
* restrict repository access to ArgoCD
* store SSH credentials as Kubernetes secrets

#### 7. Enabling Drift Detection & Self-Healing

Applications deployed via ArgoCD should enable automated reconciliation.

Example:

```yaml
spec:
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
    syncOptions:
      - CreateNamespace=true
```

Explanation:

| Setting         | Behavior                              |
| --------------- | ------------------------------------- |
| selfHeal        | Reverts manual changes in the cluster |
| prune           | Removes resources deleted from Git    |
| CreateNamespace | Automatically creates namespaces      |

Reconciliation typically occurs every few minutes.

#### 8. Creating Applications (App-of-Apps Pattern)

Large platforms often use the **App-of-Apps pattern**.

A root application deploys multiple platform components.

Example:

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: platform-root
  namespace: argocd
spec:
  source:
    repoURL: https://github.com/company/cluster-config.git
    path: apps
    targetRevision: main
  destination:
    server: https://kubernetes.default.svc
    namespace: argocd
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
```

Typical components deployed via the root app:

```
ingress controller
monitoring stack
logging stack
application workloads
Hyperswitch deployment
```

The exact platform services deployed depend on the organization.

#### 9. Deploying Hyperswitch via ArgoCD

Hyperswitch is typically deployed using the official Helm chart.

ArgoCD can manage Helm releases directly.

Example Hyperswitch application:

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: hyperswitch-prod
  namespace: argocd
spec:
  destination:
    namespace: hyperswitch-prod
    server: https://kubernetes.default.svc
  source:
    repoURL: https://github.com/juspay/hyperswitch-helm
    chart: hyperswitch-stack
    targetRevision: <chart-version>
    helm:
      valueFiles:
        - values-prod.yaml
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
```

Separate applications should exist for:

```
Hyperswitch production
Hyperswitch sandbox
Hyperswitch integration
```

Each environment should use its own namespace and configuration values.

#### 10. Managing Multiple Clusters

ArgoCD can manage multiple Kubernetes clusters.

Register cluster:

```
argocd cluster add <context-name>
```

Best practices vary depending on organizational architecture.

Common models:

**Single cluster per ArgoCD**

Simpler operations.

**Centralized ArgoCD controlling multiple clusters**

Better for large platform teams.

Production payment systems often isolate production clusters for security reasons.

#### 11. Secret Management

Application deployments such as Hyperswitch require sensitive configuration.

Examples:

* database credentials
* encryption keys
* payment connector credentials

Secrets should not be stored directly in Git.

Common approaches:

* external secret managers
* sealed secrets
* runtime secret injection

The chosen method depends on the organization's security architecture.

#### 12. Managing Terraform Alongside ArgoCD

ArgoCD manages **Kubernetes resources**, not infrastructure.

Infrastructure provisioning should be handled separately using tools such as **Terraform**.

Typical workflow:

<div align="left"><figure><img src="../../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure></div>

ArgoCD then deploys applications onto the resulting infrastructure.

#### 13. Enforcing No-Drift Policy

To maintain GitOps integrity:

Kubernetes clusters should restrict direct modification of resources.

Recommended controls:

* limit `kubectl` access
* audit cluster changes
* enforce policy validation
* monitor configuration drift

Cloud infrastructure should also restrict manual changes outside the infrastructure pipeline.

#### Summary

ArgoCD ensures:

* continuous reconciliation
* Git as the source of truth
* automated deployments
* drift detection and remediation<br>
