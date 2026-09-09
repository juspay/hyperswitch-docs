---
description: >-
  Describes production grade infrastructure provisioning using Terraform on AWS
  cloud
icon: aws
---

# On AWS using Terraform

This guide provisions a production-shaped Hyperswitch stack entirely on AWS, using Terraform modules from [`hyperswitch-suite`](https://github.com/juspay/hyperswitch-suite) composed with a [Terragrunt Stack](https://terragrunt.gruntwork.io/docs/features/stacks/).

***

### Architecture at a glance

<table><thead><tr><th width="229.1875">Layer</th><th>AWS component</th></tr></thead><tbody><tr><td>Networking</td><td>VPC, Subnets, Route53, Cloudfront, Proxies, NAT etc.</td></tr><tr><td>Storage</td><td>RDS, Elasticache, s3</td></tr><tr><td>Compute</td><td>EC2, EKS cluster </td></tr><tr><td>Managed resources</td><td>KMS, Cloudwatch, WAF, IAM, etc.</td></tr></tbody></table>

The Terraform stack provision the AWS infrastructure. Argo CD then deploys the required applications on top of that infrastructure

### Prerequisites

Install and authenticate, from official sources:

* [`terraform`](https://developer.hashicorp.com/terraform/install)
* [`terragrunt`](https://docs.terragrunt.com/getting-started/install/)&#x20;
* [`aws-cli`](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)&#x20;

***

### Step 1 — Define the Infra stack using Terragrunt/Terraform

[`hyperswitch-suite`](https://github.com/juspay/hyperswitch-suite/blob/main/terraform/aws/live/terragrunt.stack.hcl) repo ships a reference stack at [`terraform/aws/catalog/stacks/dev/terragrunt.stack.hcl`](https://github.com/juspay/hyperswitch-suite/blob/main/terraform/aws/live/terragrunt.stack.hcl). Reading that file is recommended.

_Save the file in the following path of your repository `terraform/aws/live`:_

```
mkdir -p terraform/aws/live
curl -o terraform/aws/live/terragrunt.stack.hcl \
  https://raw.githubusercontent.com/juspay/hyperswitch-suite/main/terraform/aws/live/terragrunt.stack.hcl
```

Your file should look like below and please update the values in that file as per the requirement, which would have been done in finalizing stack blueprint,&#x20;

<pre class="language-hcl"><code class="lang-hcl">stack "prod" {
  source = "git::https://github.com/juspay/hyperswitch-suite.git//terraform/aws/catalog/stacks/dev?ref=stack/aws/catalog-v0.1.0"
  path   = "prod/eu-central-1"

  no_dot_terragrunt_stack = true

  values = {
    env          = "prod"
    region       = "eu-central-1"
    region_code  = "<a data-footnote-ref href="#user-content-fn-1">euc1</a>"
    project_name = "hyperswitch"
    account_id   = "000000000000" 
    state_bucket = "hyperswitch-tfstate-prod"

    vpc_cidr_prefix = "10.30"
    base_domain     = "example.com" # REPLACE_ME

    admin_role_arn     = "arn:aws:iam::000000000000:role/REPLACE_ME"
    admin_access_cidrs = []

    ami_id = "ami-000000000"

    virtual_hosts_domains = {
      api = ["api.example.com"]  REPLACE_ME
    }

    istio_host_domains = {
      prod = "istio.internal.prod.euc1.example.com"
    }

    db_instance_class            = "db.r6g.xlarge"
    db_engine_version            = "17.9"
    cache_node_type              = "cache.m6g.xlarge"
    eks_version                  = "1.35"
    eks_instance_types           = ["m6i.xlarge"]
    eks_ami_id                   = null
    system_nodes_desired_size    = 2
    generic_compute_desired_size = 3
    generic_compute_min_size     = 3
  }
}
</code></pre>

***

### Step 2 — Generate & Bootstrap

The following step generates terragrunt section required for the stack setup

```bash
# generate terragrunt modules
cd terraform/aws/live
terragrunt stack generate

#To check the dependencies
cd prod/eu-central-1
terragrunt list --tree --dag --dependencies

# BootStrap
cd vpc-network && terragrunt backend bootstrap && cd ..
```

Check the directory, you should be seeing all the modules required for the hyperswitch-stack in that folder.

***

### Step 3 — Plan & Apply

Since modules are dependent on other modules, we need to run terragrunt in phases, below are the phases in the order one has to apply. Please skip items based on the requirement.

Reply `yes` only when the plan shows creates and nothing else.

```bash
# Phase 1
terragrunt run --all --queue-include-dir=vpc-network plan
terragrunt run --all --queue-include-dir=vpc-network apply

# Phase 2
terragrunt run --all \
  --queue-include-dir=application-stack/eks-01 \
  --queue-include-dir=database \
  --queue-include-dir=efs \
  --queue-include-dir=elasticache \
  --queue-include-dir=jump-host \
  --queue-include-dir=locker \
  --queue-include-dir=route53 \
  --queue-include-dir=squid-proxy \
  plan
# ...same flags, apply

# Phase 3
terragrunt run --all \
  --queue-include-dir=application-stack/apps/alb-controller \
  --queue-include-dir=application-stack/apps/external-secrets \
  --queue-include-dir=application-stack/apps/grafana \
  --queue-include-dir=application-stack/apps/hyperswitch \
  --queue-include-dir=application-stack/apps/istio \
  --queue-include-dir=application-stack/apps/loki \
  --queue-include-dir=application-stack/apps/otel \
  --queue-include-dir=application-stack/apps/ratelimiter \
  --queue-include-dir=application-stack/apps/vector-dr \
  --queue-include-dir=application-stack/eks-resources \
  --queue-include-dir=application-stack/utils-load-balancer \
  --queue-include-dir=acm \
  plan
# ...same flags, apply

# Phase 4
terragrunt run --all \
  --queue-include-dir=application-stack/apps/decision-engine \
  --queue-include-dir=application-stack/apps/superposition \
  --queue-include-dir=envoy-proxy \
  plan
# ...same flags, apply

# Phase 5
terragrunt run --all --queue-include-dir=security-rules plan
terragrunt run --all --queue-include-dir=security-rules apply
```

***

### Step 4 — Create the logical databases and its users

We have 4 applications, which needs database of its own. Generate every password with `openssl rand -base64 32`&#x20;

1. hyperswitch-app (the OLTP Router)
2. superposition&#x20;
3. decision-engine
4. locker (the card vault)

Lets go one by one.&#x20;

#### Hyperswitch App&#x20;

Fetch host from `terragrunt output --working-dir database`  and login into the database and create user.

```
 psql -h host -d postgres -U postgres # get the password from the AWS secrets. AWS would have created and stored it in AWS Secret store
```

```sql
-- Create database
CREATE DATABASE hyperswitch;

-- Create user
CREATE USER hyperswitch_app WITH PASSWORD 'password'; # generate a password and replace here. 

-- Grant connect + basic access
GRANT CONNECT ON DATABASE hyperswitch TO hyperswitch_app;

\c hyperswitch

GRANT USAGE, CREATE ON SCHEMA public TO hyperswitch_app;

-- Auto-apply privileges to FUTURE tables/sequences/types created by the DB owner (or whoever runs the ALTER)
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL PRIVILEGES ON TABLES TO hyperswitch_app;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL PRIVILEGES ON SEQUENCES TO hyperswitch_app;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT USAGE ON TYPES TO hyperswitch_app;
```

**Database Schema Creation**

```bash
git clone --depth 1 --branch v1.126.0 https://github.com/juspay/hyperswitch.git
cd hyperswitch
cargo install diesel_cli --no-default-features --features postgres
diesel migration run \
  --database-url "postgresql://<username>:<password>@<host>:<port>/<database>?sslmode=require"
```

#### Superposition&#x20;

Fetch host from `terragrunt output --working-dir application-stack/apps/superposition`  and login into the database and create user.

```
  psql -h host -d postgres -U postgres # get the password from the AWS secrets. AWS would have created and stored it in AWS Secret store
```

```sql
-- Create database
CREATE DATABASE superposition;

-- Create user
CREATE USER superposition_app WITH PASSWORD 'password'; # generate a password and replace here. 

-- Grant connect + basic access
GRANT CONNECT ON DATABASE superposition TO superposition_app;

\c superposition

GRANT USAGE, CREATE ON SCHEMA public TO superposition_app;

-- Auto-apply privileges to FUTURE tables/sequences/types created by the DB owner (or whoever runs the ALTER)
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL PRIVILEGES ON TABLES TO superposition_app;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL PRIVILEGES ON SEQUENCES TO superposition_app;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT USAGE ON TYPES TO superposition_app;
```

**Database Schema Creation**

```bash
git clone --depth 1 --branch v1.126.0 https://github.com/juspay/hyperswitch.git # Skip this, if already done
cd hyperswitch # Skip this, if already done

DATABASE_URL="<host>:<port>" \
  scripts/seed_superposition.sh
```

#### Decision Engine&#x20;

Fetch host from `terragrunt output --working-dir application-stack/apps/decision-engine`  and login into the database and create user.

```
psql -h host -d postgres -U postgres # get the password from the AWS secrets. AWS would have created and stored it in AWS Secret store
```

```sql
-- Create database
CREATE DATABASE decision_engine;

-- Create user
CREATE USER decision_engine_app WITH PASSWORD 'password'; # generate a password and replace here. 

-- Grant connect + basic access
GRANT CONNECT ON DATABASE decision_engine TO decision_engine_app;

\c decision_engine

GRANT USAGE, CREATE ON SCHEMA public TO decision_engine_app;

-- Auto-apply privileges to FUTURE tables/sequences/types created by the DB owner (or whoever runs the ALTER)
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL PRIVILEGES ON TABLES TO decision_engine_app;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL PRIVILEGES ON SEQUENCES TO decision_engine_app;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT USAGE ON TYPES TO decision_engine_app;
```

**Database Schema Creation**

```bash
git clone --depth 1 --branch v1.126.0 https://github.com/juspay/decision-engine.git # Skip this, if already done
cd decision-engine

cargo install diesel_cli --no-default-features --features postgres
diesel migration run \
  --database-url "postgresql://<username>:<password>@<host>:<port>/<database>?sslmode=require"
```

#### Locker

Fetch host from `terragrunt output --working-dir application-stack/locker`  and login into the database and create user.

```
psql -h host -d postgres -U postgres # get the password from the AWS secrets. AWS would have created and stored it in AWS Secret store
```

```sql
-- Create database
CREATE DATABASE locker;

-- Create user
CREATE USER locker_app WITH PASSWORD 'password'; # generate a password and replace here. 

-- Grant connect + basic access
GRANT CONNECT ON DATABASE locker TO locker_app;

\c locker

GRANT USAGE, CREATE ON SCHEMA public TO locker_app;

-- Auto-apply privileges to FUTURE tables/sequences/types created by the DB owner (or whoever runs the ALTER)
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL PRIVILEGES ON TABLES TO locker_app;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL PRIVILEGES ON SEQUENCES TO locker_app;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT USAGE ON TYPES TO locker_app;
```

**Database Schema Creation**

```bash
git clone --depth 1 https://github.com/juspay/hyperswitch-card-vault.git
cd hyperswitch-card-vault
diesel migration run \
  --database-url "postgres://locker:<generated-password>@<locker-endpoint>:5432/locker?sslmode=require"
```

***

### Step 5 — Create secrets

Create following secrets in AWS secret manager and update the KMS encrypted [sensitive data](https://github.com/juspay/hyperswitch-helm/blob/feature/secrets-reference-and-chart-readmes/SECRETS.md) of respective application over there

| App              | Secret Path/ARN          |
| ---------------- | ------------------------ |
| hyperswitch-app  | `prod/hyperswitch`       |
| recon            | `prod/hyperswitch-recon` |
| revenue-recovery | `prod/revenue-recovery`  |

***

### Step 6 - Validation

```
terragrunt run --all plan -- -detailed-exitcode
```

Output decides the validation. Exit code `0` = no changes, `1` = error, `2` = changes

{% hint style="info" %}
Post validation of successful infrastructure provision, continue with the [Application installation](../deploy-kubernetes-applications-using-argo-cd.md).
{% endhint %}



[^1]: 
