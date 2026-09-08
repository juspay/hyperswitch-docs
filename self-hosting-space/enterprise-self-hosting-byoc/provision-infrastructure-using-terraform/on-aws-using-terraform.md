---
description: >-
  Describes the infrastructure provisioning using Terraform on AWS cloud for
  Hyperswitch.
icon: aws
---

# On AWS using Terraform

This guide provisions a production-validateed Hyperswitch stack entirely on AWS, using Terraform modules from [`hyperswitch-suite`](https://github.com/juspay/hyperswitch-suite) composed with a [Terragrunt Stack](https://terragrunt.gruntwork.io/docs/features/stacks/).

***

### Architecture at a glance

| Layer            | AWS component                               | Terraform unit                                 |
| ---------------- | ------------------------------------------- | ---------------------------------------------- |
| Network          | VPC, subnets, NAT                           | `vpc-network` (prerequisite, not covered here) |
| DNS              | Route 53 public zone                        | `dns` (prerequisite, not covered here)         |
| Database         | RDS for PostgreSQL                          | `rds`                                          |
| Compute          | EKS cluster                                 | `eks`                                          |
| Cache            | ElastiCache (Valkey/Redis)                  | `valkey`                                       |
| IAM / KMS        | Workload identity, encryption keys          | `application-resources`                        |
| Cluster plumbing | RBAC, storage classes, autoscaler           | `eks-resources`                                |
| Edge / CDN       | CloudFront for the SDK + Control Center     | `cloudfront`                                   |
| GitOps           | Argo CD, ingress, External Secrets Operator | management-stack bootstrap (Step 7)            |
| Secrets          | AWS Secrets Manager → synced into cluster   | ESO (Step 8)                                   |

The Terraform units in the table (excluding VPC/DNS) provision the _infrastructure_. Argo CD then deploys the _application workloads_ (router, control center, web SDK, card vault, key manager) on top of that infrastructure — see Step 9.

***

### Step 0 — Prerequisites

Install and authenticate, from official sources:

* `kubectl`
* `terraform`
* `terragrunt` (stacks require a recent version — check the [Terragrunt release notes](https://github.com/gruntwork-io/terragrunt/releases) against what `hyperswitch-suite` targets)
* `yq`
* `git`
* `openssl`
* AWS CLI, authenticated with credentials that can create VPC, RDS, EKS, ElastiCache, IAM, KMS, and CloudFront resources

**Pin a module tag now.** Everything below references `?ref=<module-tag>` — pick a released tag (not `main`) from the [hyperswitch-suite releases](https://github.com/juspay/hyperswitch-suite/releases) or [CHANGELOG](https://github.com/juspay/hyperswitch-suite/blob/main/CHANGELOG.md), and use that same tag everywhere in this guide. Module directory names and inputs can change between releases, so confirm the paths in Step 2 against the `terraform/aws/modules` tree at that tag before you generate anything.

**VPC and DNS.** This guide assumes an existing VPC and a public Route 53 hosted zone. If you don't have these yet, add the `vpc-network` and `dns` units from the suite _before_ the units in Step 2 — everything else is unchanged. Skipping this step is the most common reason `terragrunt plan` fails with subnet/zone lookup errors in Step 4.

***

### Step 1 — Define the stack

Refer from [https://github.com/juspay/hyperswitch-suite/blob/main/terraform/aws/catalog/stacks/dev/terragrunt.stack.hcl](https://github.com/juspay/hyperswitch-suite/blob/main/terraform/aws/catalog/stacks/dev/terragrunt.stack.hcl)&#x20;

```hcl
stack "dev" {
  source = "../catalog/stacks/dev"
  path   = "dev/eu-central-1"

  no_dot_terragrunt_stack = true

  values = {
    env          = "dev"
    region       = "eu-central-1"
    region_code  = "euc1"
    project_name = "hyperswitch"
    account_id   = "000000000000" # REPLACE_ME
    state_bucket = "hyperswitch-tfstate-dev"

    # Networking
    vpc_cidr_prefix = "10.10"

    # DNS / TLS
    base_domain = "dev.example.com" # REPLACE_ME

    # Access
    admin_role_arn     = "arn:aws:iam::000000000000:role/REPLACE_ME" # REPLACE_ME
    admin_access_cidrs = []

    # Proxies / bastion — shared AMI placeholder; use a real per-role AMI id.
    ami_id = "ami-REPLACE_ME"

    # Envoy ingress domains: map of virtual-host-group => [domains]
    virtual_hosts_domains = {
      api = [""]
    }

    # Istio host domains (map keys are arbitrary; module reads the values)
    istio_host_domains = {
      dev = "" # REPLACE_ME
    }

    # Sizing
    db_instance_class            = ""
    db_engine_version            = ""
    cache_node_type              = ""
    eks_version                  = "1.35"
    eks_instance_types           = [""]
    eks_ami_id                   = null
    system_nodes_desired_size    = 1
    generic_compute_desired_size = 2
    generic_compute_min_size     = 1
  }
}
```

Fill in `<module-tag>` (from Step 0) everywhere. What each unit does:

* **rds** — PostgreSQL instance backing the router, OLAP, Superposition (config), and locker (card vault) schemas.
* **eks** — the Kubernetes cluster the app workloads run on.
* **valkey** — Redis-compatible cache used for locking, idempotency, and session state.
* **application-resources** — IAM roles/policies (IRSA or Pod Identity) and KMS keys the application pods assume at runtime.
* **eks-resources** — in-cluster plumbing: RBAC bindings, `StorageClass`es, and the cluster autoscaler.
* **cloudfront** — CDN in front of the web SDK and Control Center static assets.

***

### Step 2 — Generate and plan

```bash
cd terraform/aws/live/aws/live
terragrunt stack generate
terragrunt plan
```

**Read the plan.** This is the only review gate before real AWS resources exist. Check specifically for:

* No unintended destroys or replacements (`-/+`) if this is a re-run.
* Instance sizes and multi-AZ settings match your environment (don't provision `prod` sizing defaults into a `staging` account, or vice versa).
* The RDS and ElastiCache resources land in private subnets, not public ones.

***

### Step 4 — Apply

```bash
terragrunt apply
```

Reply `yes` only when the plan shows creates and nothing else (`N added, 0 changed, 0 destroyed`). Terragrunt applies units in dependency order, parallelizing where the stack graph allows it.

***

### Step 5 — Create the database users and run table queries

Connect to the new RDS instance and create one login per service, each scoped to its own schema — don't share a superuser credential across services.

```sql
CREATE DATABASE hyperswitch OWNER router;
CREATE DATABASE superposition OWNER superposition;
CREATE DATABASE locker OWNER locker;

CREATE USER router WITH PASSWORD '<generated-password>';
CREATE USER superposition WITH PASSWORD '<generated-password>';
CREATE USER locker WITH PASSWORD '<generated-password>';

GRANT CONNECT ON DATABASE hyperswitch TO router, superposition TO superposition, locker TO locker;

-- Then, per service, create and scope its own schema, e.g. for router:
CREATE SCHEMA router AUTHORIZATION router;
GRANT USAGE, CREATE ON SCHEMA router TO router;
ALTER DEFAULT PRIVILEGES IN SCHEMA router GRANT ALL ON TABLES TO router;
```

Run the following migrations on the hyperswitch database:

```bash
git clone https://github.com/juspay/hyperswitch.git && cd hyperswitch
diesel migration run \
  --database-url "postgres://postgres:<master-password>@<rds-endpoint>:5432/hyperswitch?sslmode=require"
```

Generate passwords with `openssl rand -base64 32` (or your org's secret generator) — don't hand-type them.

***

### Step 6 — Bootstrap the management stack

This installs the cluster-wide plumbing Argo CD needs before it can deploy anything: an ingress controller, the External Secrets Operator (ESO), and Argo CD itself.

**Status:** the install script referenced for this step is not yet published in `juspay/hyperswitch-suite` — it currently lives in an internal repo, and needs to move before this step can be a one-liner. Until it lands, bootstrap manually:

<pre><code>curl -fSL https://raw.githubusercontent.com/juspay/hyperswitch-suite/refs/heads/main/scripts/install-argocd.sh | bash
<strong>kubectl create namespace argocd
</strong>kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
</code></pre>

Then apply the ingress controller and ESO of your choice (e.g. `ingress-nginx` and `external-secrets` via their official Helm charts), and apply the app definitions at `management-<env>/apps/*.yaml` from your environment path once those exist.

_(Docs team: once `install.sh` moves to `hyperswitch-suite` and the script URL is confirmed, replace this block with the one-liner and a screenshot of the interactive component-selection prompt.)_

***

### Step 7 — Populate secrets

Everything the application needs at runtime is read from AWS Secrets Manager by ESO — nothing sensitive is committed to Git.

**1. Database credentials.** Store each password from Step 5 at the path your `ExternalSecret` resources reference, e.g.:

```
hyperswitch/<env>/db/router
hyperswitch/<env>/db/superposition
hyperswitch/<env>/db/locker
```

**2. Card Vault keys.** The locker needs a master key and a JWE keypair:

```bash
openssl rand -hex 32 > vault-master-key.txt
openssl genrsa -out jwe-private.pem 2048
openssl rsa -in jwe-private.pem -pubout -out jwe-public.pem
```

Store all three at `hyperswitch/<env>/vault/*`, then delete the local files.

**3. Key-manager mTLS certs.** Generate via the suite's `gen_certs.sh` (confirm its path at your pinned tag) and store the resulting cert/key pair at `hyperswitch/<env>/key-manager/*`.

**4. Reference from Helm values** using `valueFrom.secretKeyRef` (populated by ESO), e.g.:

```yaml
env:
  - name: DATABASE_PASSWORD
    valueFrom:
      secretKeyRef:
        name: router-db-credentials
        key: password
```

***

### Step 9 — Verify the install

* `kubectl get pods -A` — all pods `Running`/`Ready`, no `CrashLoopBackOff`.
* Hit the Control Center URL behind CloudFront and confirm login works.
* Send a test payment through the router API to confirm the full path (router → DB → cache → locker) is wired correctly.
