---
description: Upgrade Hyperswitch using GitOps practices to deploy new versions with minimal downtime
---

# Upgrade Hyperswitch

### GitOps-Based Deployment using ArgoCD (App-of-Apps Pattern)

Using a GitOps orchestration platform such as **Argo CD** allows Hyperswitch deployments to be managed declaratively via Git.

Benefits include:

* Version-controlled deployments
* Automated reconciliation and drift detection
* Reproducible environments
* Simplified rollbacks
* Centralized multi-cluster management

Instead of manually executing Helm commands such as:

```
helm upgrade --install hyperswitch ...
```

the desired deployment state is defined in Git and continuously reconciled by ArgoCD.

This guide uses ArgoCD, but similar GitOps tools can be used.

#### Target Architecture

A **blue/green cluster upgrade model** is recommended.

This strategy involves provisioning a **parallel environment (green)** where the upgraded version of Hyperswitch is deployed and validated before production traffic is switched over.&#x20;

The **existing environment (blue)** continues serving live traffic during this process, allowing controlled cutover and providing a straightforward rollback mechanism if any issues arise after the upgrade.

During upgrade:

| Cluster           | Role                                           |
| ----------------- | ---------------------------------------------- |
| hyperswitch-v1    | current production cluster                     |
| hyperswitch-v2    | upgraded cluster                               |
| ArgoCD            | GitOps deployment controller                   |
| Git repository    | system source of truth                         |
| external services | shared Postgres, Redis, secrets, observability |

Stateful infrastructure such as databases should **not be recreated during cluster upgrades**.

#### ArgoCD App-of-Apps Pattern

The diagram illustrates how Hyperswitch deployments are managed using the **App-of-Apps pattern in Argo CD**.

<figure><img src="../../.gitbook/assets/image (8).png" alt="" width="161"><figcaption></figcaption></figure>

In this model, **a single “Root Application” manages multiple child applications**, allowing complex systems to be deployed and maintained in a structured and scalable way.

1. **Git Repository** All deployment configurations are stored in a Git repository. This includes the ArgoCD application definitions and Helm chart references that describe the desired state of the system.
2. **ArgoCD** ArgoCD continuously monitors the Git repository and ensures that the Kubernetes cluster matches the configuration defined in Git. Any changes committed to the repository are automatically synchronized to the cluster.
3. **Root Application (App-of-Apps)** The Root Application acts as the **entry point for the deployment**. Instead of directly deploying services, it references multiple child applications. This structure is known as the **App-of-Apps pattern**, where one parent application manages a collection of related applications.
4. **Environment Applications** The Root Application deploys **environment-level applications** (for example: Dev, Staging, Production). Each environment application contains configuration specific to that environment.
5. **Helm Applications** Each environment application then deploys individual **Helm-based applications**, which package and deploy specific components of the system.
6. **Hyperswitch + Platform Components** These Helm applications ultimately deploy **Hyperswitch services and supporting platform components** into the Kubernetes cluster.

Using the App-of-Apps pattern allows teams to manage large deployments in a **modular, hierarchical structure**, making it easier to organize environments, promote changes across stages, and maintain consistency across clusters.

#### 1. Prepare the GitOps Repository Structure

The **App-of-Apps pattern** organizes deployments hierarchically.

Example repository layout:

```
infra-gitops/

applications/
  root-app.yaml

environments/
  production/
    hyperswitch-v1.yaml
    hyperswitch-v2.yaml

apps/
  hyperswitch/
    application.yaml
    values-prod.yaml

  platform/
    ingress.yaml
    cert-manager.yaml
    monitoring.yaml
```

Structure overview:

| Directory    | Purpose                         |
| ------------ | ------------------------------- |
| applications | root ArgoCD application         |
| environments | cluster-specific deployments    |
| apps         | application Helm configurations |

This structure enables **environment isolation and reusable application definitions**.

#### 2. Provision the New Kubernetes Cluster

Provision a new cluster for the upgraded deployment.

Supported platforms include:

* managed Kubernetes services
* self-managed Kubernetes clusters
* on-prem Kubernetes environments

Verify cluster connectivity:

```
kubectl get nodes
```

Recommended cluster baseline:

| Requirement            | Recommendation                        |
| ---------------------- | ------------------------------------- |
| autoscaling            | enabled                               |
| node pools             | separate system and application pools |
| ingress controller     | installed                             |
| certificate management | enabled                               |
| RBAC                   | enabled                               |
| network policies       | recommended                           |

#### 3. Install ArgoCD

Install ArgoCD on a **management cluster** or a designated platform cluster.

Installation example:

```
kubectl create namespace argocd

kubectl apply -n argocd \
-f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

Verify installation:

```
kubectl get pods -n argocd
```

Access the UI:

```
kubectl port-forward svc/argocd-server -n argocd 8080:443
```

Production deployments should expose ArgoCD through:

* secure ingress
* TLS certificates
* SSO authentication

#### 4. Register Clusters in ArgoCD

Register target clusters so ArgoCD can deploy applications.

```
argocd cluster add <cluster-context>
```

Example clusters:

| Cluster        | Purpose            |
| -------------- | ------------------ |
| hyperswitch-v1 | current production |
| hyperswitch-v2 | upgrade deployment |

ArgoCD can then deploy applications to multiple clusters.

#### 5. Deploy the Root Application (App-of-Apps)

The **root application** manages all other applications.

Example:

`applications/root-app.yaml`

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: hyperswitch-root
spec:
  project: default

  source:
    repoURL: https://github.com/your-org/infra-gitops
    targetRevision: main
    path: environments/production

  destination:
    server: https://kubernetes.default.svc
    namespace: argocd

  syncPolicy:
    automated:
      prune: true
      selfHeal: true
```

Apply:

```
kubectl apply -f applications/root-app.yaml
```

ArgoCD will now automatically deploy all applications defined in the repository.

#### 6. Define Cluster Applications

Environment files define which applications are deployed to each cluster.

Example:

`environments/production/hyperswitch-v2.yaml`

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: hyperswitch-v2
spec:
  project: default

  source:
    repoURL: https://github.com/your-org/infra-gitops
    targetRevision: main
    path: apps/hyperswitch

  destination:
    server: https://kubernetes.default.svc
    namespace: hyperswitch
```

Each environment can deploy different versions or configurations.

#### 7. Deploy Hyperswitch via Helm

The Hyperswitch application definition references the Helm chart.

Example:

`apps/hyperswitch/application.yaml`

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: hyperswitch
spec:
  project: default

  source:
    repoURL: https://github.com/juspay/hyperswitch
    chart: hyperswitch-stack
    targetRevision: <chart-version>

    helm:
      valueFiles:
        - values-prod.yaml

  destination:
    server: https://kubernetes.default.svc
    namespace: hyperswitch

  syncPolicy:
    automated:
      prune: true
      selfHeal: true
```

ArgoCD will automatically:

* pull the Helm chart
* apply configuration
* maintain cluster state

#### 8. Plan Database Migration

Database schema changes must be handled carefully.

Disable automatic migrations during upgrade:

```yaml
hyperswitch-app:
  migrations:
    enabled: false
```

Recommended process:

1. Deploy new Hyperswitch version.
2. Ensure application pods are not receiving production traffic.
3. Create database backup or snapshot.
4. Run migration job.
5. Validate schema changes.
6. scale application replicas.

Example:

```
kubectl scale deployment hyperswitch --replicas=3
```

#### 9. Gradually Shift Traffic

Traffic should be migrated progressively to the new cluster.

Traffic management options:

| Method                  | Description               |
| ----------------------- | ------------------------- |
| DNS weighted routing    | gradual traffic shift     |
| load balancer weighting | layer-7 traffic routing   |
| service mesh            | advanced routing policies |

Example rollout plan:

| Stage      | v1  | v2   |
| ---------- | --- | ---- |
| initial    | 95% | 5%   |
| validation | 75% | 25%  |
| ramp-up    | 50% | 50%  |
| final      | 0%  | 100% |

#### 10. Validate System Health

Monitor the deployment during rollout.

Key metrics include:

| Metric               | Description                  |
| -------------------- | ---------------------------- |
| payment success rate | transaction reliability      |
| API error rate       | service failures             |
| database connections | connection pool usage        |
| Redis latency        | cache performance            |
| CPU and memory       | resource utilization         |
| webhook delivery     | downstream system processing |

Observability dashboards should be available before rollout.

#### 11. Decommission the Previous Cluster

After the rollout stabilizes:

1. confirm that all traffic flows to the new cluster.
2. monitor system stability.
3. retain the old cluster for a rollback window.
4. decommission the cluster once the upgrade is confirmed.

Typical retention window: **24–72 hours**.

#### Rollback Strategy

#### Traffic rollback

Redirect traffic back to the previous cluster.

#### Application rollback

Update the Git configuration to the previous version:

```
targetRevision: <previous-chart-version>
```

Commit the change and ArgoCD will automatically synchronize.

#### Enterprise Best Practices

| Area                  | Recommendation                       |
| --------------------- | ------------------------------------ |
| Secrets Management    | Use centralized secret management    |
| Deployment Approvals  | Require pull request review          |
| Observability         | Integrate logs, metrics, and tracing |
| Environment Promotion | Dev → Staging → Production pipeline  |
| Disaster Recovery     | Maintain database backup strategy    |
