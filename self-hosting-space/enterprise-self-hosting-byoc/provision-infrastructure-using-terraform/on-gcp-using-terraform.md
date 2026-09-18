---
description: >-
  Describes production grade infrastructure provisioning using Terraform on GCP
  cloud
icon: google
---

# On GCP using Terraform

This guide provisions a production-shaped Hyperswitch stack entirely on GCP, using Terraform modules composed with a Terragrunt Stack.

### Architecture at a glance

<table><thead><tr><th width="191.609375">Layer</th><th>AWS component</th></tr></thead><tbody><tr><td>Networking</td><td>VPC, Subnets, Cloud DNS, Cloud CDN, Proxies, NAT etc.,</td></tr><tr><td>Storage</td><td>AlloyDB, Memory Store, GCS</td></tr><tr><td>Compute</td><td>VM, GKE</td></tr><tr><td>Managed Resources</td><td>Cloud Monitoring, Armor, Cloud IAM, etc.,</td></tr></tbody></table>

The Terraform stack provision the GCP _infrastructure_. Argo CD then deploys the required _applications_ on top of that infrastructure

### Prerequisites

Install and authenticate, from official sources:

* [`terraform`](https://developer.hashicorp.com/terraform/install)
* [`terragrunt`](https://docs.terragrunt.com/getting-started/install/)&#x20;
* [`gcloud` CLI](https://docs.cloud.google.com/sdk/docs/install-sdk)&#x20;

### Step 1 — Define the Infra stack using Terragrunt/Terraform

Save the stack definition in the following path of your repository `terraform/gcp/live`:

bash

```bash
mkdir -p terraform/gcp/live
curl -o terraform/gcp/live/terragrunt.stack.hcl \
  https://raw.githubusercontent.com/juspay/hyperswitch-suite/refs/heads/main/terraform/gcp/live/terragrunt.stack.hcl
```

Your file should look like below — update the values as per your finalized stack blueprint,which would have been done in finalising stack blueprint,

```hcl
stack "prod" {
  source = "git::https://github.com/juspay/hyperswitch-suite.git//terraform/gcp/catalog/stacks/dev?ref=stack/gcp/catalog-v0.1.0"
  path   = "prod/europe-west3"

  no_dot_terragrunt_stack = true

  values = {
    # -------------------------------------------------------------------------
    # Identity and state
    # -------------------------------------------------------------------------
    env        = "prod"
    region     = "europe-west3"
    project_id = "REPLACE_ME-gcp-project"

    # Terragrunt creates this bucket on the first unit's `init`. Must be
    # globally unique; set skip_bucket_creation = true to use one that is
    # managed elsewhere.
    state_bucket = "REPLACE_ME-dev-europe-west3-tfstate"

    # -------------------------------------------------------------------------
    # Networking
    # -------------------------------------------------------------------------
    vpc_cidr_prefix                   = "10.2"
    gke_pods_secondary_range_cidr     = "10.100.0.0/16"
    gke_services_secondary_range_cidr = "10.101.0.0/20"

    # Office / VPN CIDRs allowed to reach the GKE control plane. REQUIRED —
    # left empty, the gke unit falls back to an allow-all placeholder that is
    # not safe to apply.
    vpn_cidr_blocks = [] # REPLACE_ME

    # -------------------------------------------------------------------------
    # DNS
    # -------------------------------------------------------------------------
    domains = {
      api     = "api.dev.example.com"     # REPLACE_ME
      grafana = "grafana.dev.example.com" # REPLACE_ME
    }

    # -------------------------------------------------------------------------
    # Custom GCE images — edge proxies
    # -------------------------------------------------------------------------
    # Pre-baked images built from terraform/gcp/packer/{envoy-proxy,squid-proxy}.
    # Image names only; the units expand them to a full projects/<id>/global/
    # images/<name> path against project_id above.
    custom_images = {
      envoy = "REPLACE_ME-envoy"
      squid = "REPLACE_ME-squid"
    }

    # -------------------------------------------------------------------------
    # Cluster sizing
    # -------------------------------------------------------------------------
    machine_types = {
      gke_system_pool     = "e2-standard-4"
      gke_generic_compute = "e2-standard-4"
      bastion             = "e2-small"
    }

    # Group(s) or user(s) granted IAP SSH to the bastion host.
    bastion_iap_members = ["group:REPLACE_ME@example.com"]

    # -------------------------------------------------------------------------
    # Data services — every key optional; omit the block for unit defaults
    # -------------------------------------------------------------------------
    # Defaults are dev-shaped. Production wants availability_type = "REGIONAL"
    # plus at least one read pool.
    alloydb = {
      availability_type   = "ZONAL"
      cpu_count           = 2
      read_pool_instances = {}
      deletion_protection = false
    }

    valkey = {
      shard_count                 = 1
      replica_count               = 1
      node_type                   = "SHARED_CORE_NANO"
      deletion_protection_enabled = false
    }

    # The card vault's own AlloyDB cluster, separate from the shared one above
    # so card data stays in its own PCI-DSS scope. Production wants
    # availability_type = "REGIONAL" and deletion_protection left true.
    locker = {
      availability_type    = "ZONAL"
      cpu_count            = 2
      deletion_protection  = false
      kms_protection_level = "SOFTWARE"
    }

    # -------------------------------------------------------------------------
    # Application
    # -------------------------------------------------------------------------
    # Secret Manager secret ID holding SMTP credentials — GCP has no SES
    # equivalent, so hyperswitch takes one directly. null disables outbound
    # mail wiring.
    smtp_secret_id = null
  }
}
```

***

### Step 2 — Generate & Bootstrap

The following step generates the terragrunt units required for the stack setup:

bash

```bash
# generate terragrunt modules
cd terraform/gcp/live
terragrunt stack generate

# To check the dependencies
cd prod/europe-west3
terragrunt list --tree --dag --dependencies

# BootStrap (provisions the GCS state bucket from your remote_state block)
# Run from any upstream directory containing the relevant terragrunt.hcl (e.g. vpc-network)
cd vpc-network && terragrunt backend bootstrap && cd ..
```

Check the directory — you should see all the modules required for the hyperswitch stack in that folder.

***

### Step 3 — Plan & Apply

Since modules are dependent on other modules, run terragrunt in phases, in the order below. Skip items based on your requirement.

Reply `yes` only when the plan shows creates and nothing else.

bash

```bash
# Phase 1
terragrunt run --all \
  --queue-include-dir=application-stack/apps/gateway-controller \
  --queue-include-dir=artifact-registry \
  --queue-include-dir=vpc-network \
  plan
# ...same flags, applyy

# Phase 2
terragrunt run --all \
  --queue-include-dir=alloydb \
  --queue-include-dir=application-stack/gke \
  --queue-include-dir=bastion-host \
  --queue-include-dir=envoy-proxy \
  --queue-include-dir=firewall-rules \
  --queue-include-dir=memorystore-valkey \
  --queue-include-dir=squid-proxy \
  plan
# ...same flags, apply

# Phase 3
terragrunt run --all \
  --queue-include-dir=application-stack/apps/argocd \
  --queue-include-dir=application-stack/apps/external-secrets-operator \
  --queue-include-dir=application-stack/apps/grafana \
  --queue-include-dir=application-stack/apps/hyperswitch \
  --queue-include-dir=application-stack/apps/istio \
  --queue-include-dir=application-stack/apps/loki \
  --queue-include-dir=application-stack/apps/superposition \
  --queue-include-dir=application-stack/apps/vector \
  --queue-include-dir=locker \
  plan
# ...same flags, apply

# Phase 4
terragrunt run --all --queue-include-dir=security-rules plan
terragrunt run --all --queue-include-dir=security-rules apply
```

***

### Step 4 — Create the logical databases and their users

We have 4 applications, each needing its own database. Generate every password with `openssl rand -base64 32`:

* hyperswitch-app
* superposition
* decision-engine
* locker

#### Hyperswitch App

Fetch the Cloud SQL connection host from `terragrunt output --working-dir alloydb`, then connect. Get the `postgres` password from Secret Manager (Cloud SQL auto-generates and stores it there if you provisioned it that way, or set it explicitly in the module).

bash

```bash
psql -h <host> -d postgres -U postgres
```

sql

```sql
-- Create database
CREATE DATABASE hyperswitch;

-- Create user
CREATE USER hyperswitch_app WITH PASSWORD 'password'; -- generate a password and replace here

-- Grant connect + basic access
GRANT CONNECT ON DATABASE hyperswitch TO hyperswitch_app;

\c hyperswitch

GRANT USAGE, CREATE ON SCHEMA public TO hyperswitch_app;

-- Auto-apply privileges to FUTURE tables/sequences/types
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL PRIVILEGES ON TABLES TO hyperswitch_app;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL PRIVILEGES ON SEQUENCES TO hyperswitch_app;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT USAGE ON TYPES TO hyperswitch_app;
```

**Database Schema Creation**

bash

```bash
git clone --depth 1 --branch v1.126.0 https://github.com/juspay/hyperswitch.git
cd hyperswitch
cargo install diesel_cli --no-default-features --features postgres
diesel migration run \
  --database-url "postgresql://<username>:<password>@<host>:<port>/<database>?sslmode=require"
```

> Cloud SQL note: for private-IP-only instances you'll typically connect via the Cloud SQL Auth Proxy or from within the VPC (e.g. the jump host) rather than a public endpoint — adjust `<host>` accordingly.

#### Superposition

Fetch host from `terragrunt output --working-dir application-stack/apps/superposition`, then connect (same `psql` pattern as above).

sql

```sql
CREATE DATABASE superposition;
CREATE USER superposition_app WITH PASSWORD 'password'; -- generate a password and replace here
GRANT CONNECT ON DATABASE superposition TO superposition_app;

\c superposition

GRANT USAGE, CREATE ON SCHEMA public TO superposition_app;

ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL PRIVILEGES ON TABLES TO superposition_app;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL PRIVILEGES ON SEQUENCES TO superposition_app;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT USAGE ON TYPES TO superposition_app;
```

**Database Schema Creation**

bash

```bash
git clone --depth 1 --branch v1.126.0 https://github.com/juspay/hyperswitch.git # Skip if already done
cd hyperswitch # Skip if already done

DATABASE_URL="<host>:<port>" \
  scripts/seed_superposition.sh
```

#### Locker

Fetch host from `terragrunt output --working-dir application-stack/locker`, then connect.

sql

```sql
CREATE DATABASE locker;
CREATE USER locker_app WITH PASSWORD 'password'; -- generate a password and replace here
GRANT CONNECT ON DATABASE locker TO locker_app;

\c locker

GRANT USAGE, CREATE ON SCHEMA public TO locker_app;

ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL PRIVILEGES ON TABLES TO locker_app;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL PRIVILEGES ON SEQUENCES TO locker_app;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT USAGE ON TYPES TO locker_app;
```

**Database Schema Creation**

bash

```bash
git clone --depth 1 https://github.com/juspay/hyperswitch-card-vault.git
cd hyperswitch-card-vault
diesel migration run \
  --database-url "postgres://locker:<generated-password>@<locker-endpoint>:5432/locker?sslmode=require"
```

***

### Step 5 — Create secrets

Create the following secrets in **Secret Manager** and update the KMS-encrypted (Cloud KMS) sensitive data of each respective application there.

| App              | Secret Path/ARN          |
| ---------------- | ------------------------ |
| hyperswitch-app  | `prod_hyperswitch`       |
| recon            | `prod_hyperswitch-recon` |
| revenue-recovery | `prod_revenue-recovery`  |

***

### Step 6 — Validation

```bash
terragrunt run --all plan -- -detailed-exitcode
```

Output decides the validation. Exit code `0` = no changes, `1` = error, `2` = changes pending.

***

{% hint style="info" %}
Post validation of successful infrastructure provision, continue with the [Application installation](../deploy-kubernetes-applications-using-argo-cd.md).​
{% endhint %}

