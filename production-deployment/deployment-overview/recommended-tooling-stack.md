---
description: Configure Recommended Tooling Stack to start processing payments quickly
---

# Recommended Tooling Stack

The recommended tooling stack for production deployments is:

* **Terraform** — Infrastructure provisioning and management (Infrastructure as Code)
* **Kubernetes** — Container orchestration platform
* **Helm** — Kubernetes package manager for application deployment
* **ArgoCD** — GitOps-based continuous delivery system for Kubernetes

Together, these tools form a layered deployment architecture:

| Layer                       | Tool       | Responsibility                                        |
| --------------------------- | ---------- | ----------------------------------------------------- |
| Infrastructure provisioning | Terraform  | Creates cloud infrastructure                          |
| Container orchestration     | Kubernetes | Runs and scales application workloads                 |
| Application packaging       | Helm       | Defines how the application is deployed on Kubernetes |
| Continuous delivery         | ArgoCD     | Automatically deploys Helm configurations from Git    |

This architecture enables reproducible deployments, automated rollouts, and reliable production operations.

## Terraform

Terraform is recommended as the **Infrastructure-as-Code (IaC)** tool used to provision and manage cloud infrastructure in a consistent, version-controlled, and repeatable manner.

Infrastructure is defined using declarative configuration files that describe the desired infrastructure state. Terraform then compares this configuration with the current infrastructure and performs the necessary actions to reconcile the two.

Terraform can be used with any major cloud provider including AWS, Google Cloud, and Azure.

#### How Terraform Works

Terraform operates in three key stages:

1. **Define Infrastructure** Infrastructure components are declared in configuration files.
2. **Plan Changes** Terraform generates an execution plan showing what resources will be created, modified, or deleted.
3. **Apply Changes** Terraform executes the plan and provisions the infrastructure.

This workflow allows infrastructure changes to be reviewed and approved before deployment.

#### Terraform allows merchants to

* Define infrastructure declaratively using code
* Version-control infrastructure changes
* Review infrastructure updates via pull requests
* Maintain environment parity across Dev, Staging, and Production
* Reduce configuration drift across environments

#### Terraform can provision foundational infrastructure components such as

* Virtual Private Cloud (VPC) and networking
* Subnets
* Internet Gateways and NAT Gateways
* Security Groups and Network Policies
* Kubernetes clusters (EKS / GKE / AKS or self-managed clusters)
* Managed databases (Postgres, Cloud SQL, etc.)
* Cache layers (Redis / ElastiCache)

{% hint style="info" %}
**Note:** Terraform state should be stored remotely (for example, S3 with DynamoDB locking or equivalent mechanisms) to support team-based workflows and prevent state corruption.
{% endhint %}

## Kubernetes

Kubernetes is recommended as the **container orchestration platform** used to run and scale containerized workloads in production environments.

Applications such as Hyperswitch are packaged as **containers** (Docker images). Kubernetes manages how these containers are deployed, scaled, restarted, and networked across multiple machines (nodes).

Kubernetes provides several built-in capabilities that are critical for production systems:

* Automatic workload scheduling across nodes
* Horizontal scaling of application replicas
* Self-healing for failed containers
* Service discovery and internal networking
* Rolling updates with zero downtime

#### Deployment Models

Kubernetes can be deployed in one of two models:

**Managed Kubernetes Services (Recommended)** Examples include:

* AWS Elastic Kubernetes Service (EKS)
* Google Kubernetes Engine (GKE)
* Azure Kubernetes Service (AKS)

Managed services reduce operational overhead by handling cluster management, control plane operations, and upgrades.

### Self-Managed Kubernetes Clusters

Organizations with strong internal platform engineering capabilities may choose to operate their own clusters. However, this approach increases operational complexity and maintenance responsibilities.

{% hint style="info" %}
**Note:** Managed Kubernetes services are strongly recommended for production deployments.
{% endhint %}

## Helm

Helm is the **package manager for Kubernetes**, similar to how package managers are used in traditional software environments.

Instead of manually creating many Kubernetes configuration files, Helm allows applications to be packaged into reusable templates called **Helm Charts**.

A Helm chart defines:

* Kubernetes deployments
* services
* configuration values
* secrets
* networking resources

Helm templates allow these resources to be configured using environment-specific values.

#### How Helm Works

A Helm deployment typically consists of:

1. **Chart:** A package containing all Kubernetes resource templates for the application.
2. **Values File (values.yaml):** A configuration file that customizes the deployment for a specific environment.
3. **Release:** An instance of a chart deployed to a Kubernetes cluster.

Using Helm, applications can be deployed, upgraded, or rolled back with a single command.

This makes Helm a powerful mechanism for managing complex Kubernetes applications like Hyperswitch.

{% hint style="info" %}
#### Note on Alternative Installation Methods

Juspay Hyperswitch developer documentation also provides alternative installation methods:

* Docker Compose installation
* AWS Cloud Development Kit (CDK) installation
* Installation from source

These methods are intended primarily for **developer environments or sandbox deployments**, and are not recommended for production installations.
{% endhint %}

Using Helm charts significantly simplifies installation and lifecycle management of Hyperswitch in production environments.

However, some supporting infrastructure components may still require manual installation or separate management. These may include:

* Firewall configuration
* Ingress controllers
* Inbound and outbound proxies
* Load balancers
* Monitoring services
* Remote monitoring infrastructure
* Load testing services
* Card Vault setup and lifecycle management

Detailed instructions for these components are provided in the subsequent sections.

## ArgoCD

ArgoCD is recommended as the **GitOps-based continuous delivery system** used to manage Kubernetes deployments declaratively.

In a GitOps model, the desired state of the system is stored in a Git repository. ArgoCD continuously monitors the repository and automatically applies changes to the Kubernetes cluster to match the defined configuration.

This eliminates the need for manual deployment commands and ensures that the cluster state always matches what is defined in Git.

#### How ArgoCD Works

The typical GitOps workflow is:

1. Application configuration (Helm charts and values) is stored in Git.
2. ArgoCD continuously monitors the repository.
3. When changes are committed to Git, ArgoCD automatically synchronizes the Kubernetes cluster.
4. If configuration drift occurs, ArgoCD detects it and restores the expected state.

#### ArgoCD enables

* Git as the single source of truth for cluster state
* Automated synchronization between Git and Kubernetes
* Drift detection and automatic reconciliation
* Controlled and auditable application rollouts
* Multi-environment promotion workflows (Dev → Staging → Production)
* Rollback to previously known-good versions

This GitOps model improves operational reliability and enables safer production deployments.

## Summary

Collectively, this tooling stack enables a robust, scalable, and production-grade infrastructure foundation for deploying and operating Hyperswitch in enterprise environments.

The responsibilities of each layer are clearly separated:

* **Terraform** provisions the underlying infrastructure.
* **Kubernetes** manages containerized workloads.
* **Helm** packages and deploys application resources.
* **ArgoCD** automates deployment and ensures configuration consistency through GitOps workflows.

This architecture provides repeatable infrastructure provisioning, automated deployments, and reliable lifecycle management for production payment systems.<br>
