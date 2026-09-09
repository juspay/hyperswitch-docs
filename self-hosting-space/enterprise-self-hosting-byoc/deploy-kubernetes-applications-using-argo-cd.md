---
description: >-
  Install Argo CD on your Kubernetes cluster and use it to deploy Hyperswitch
  and its applications from your own Git repository.
icon: kubernetes
---

# Deploy Kubernetes applications using Argo CD

Terraform builds the infrastructure. Argo CD deploys the applications that run on it.

The steps are the same on any Kubernetes cluster on any cloud provider — be it EKS, GKE, or one you manage yourself. Provision your infrastructure first using the Terraform page for your cloud using the previous section.

***

## What Argo CD deploys

Hyperswitch ships as one umbrella Helm chart, `hyperswitch-stack`. Argo CD deploys that single chart, and every Hyperswitch component comes up as a subchart of it. You control all of them from one values file.

1. **hyperswitch-app** (OLAP router, OLTP router and scheduler)
2. **superposition**
3. **hyperswitch-control-center**&#x20;
4. **hyperswitch-ucs**
5. **decision-engine**&#x20;
6. **istio**

***

### Prerequisites

* [kubectl](https://kubernetes.io/docs/tasks/tools/)
* [helm](https://helm.sh/docs/intro/install/)
* [yq](https://github.com/mikefarah/yq#install)
* [argocd CLI](https://argo-cd.readthedocs.io/en/stable/cli_installation/)
* [git](https://git-scm.com/downloads)
* A Git repository you can push to, reachable from the cluster. It can be private.

***

### Step 1 — Create your configuration repository

The following generator asks a few questions and writes out a ready-to-push configuration repository.

```bash
curl -fsSL https://raw.githubusercontent.com/juspay/hyperswitch-suite/main/scripts/self-host/bootstrap.sh \
  | bash -s -- --ref main --target-dir ./hyperswitch-config
```

Two answers matter most: the **Git URL** Argo CD will fetch (if this is wrong, nothing syncs) and the **chart version**. Your answers are saved to `hyperswitch-bootstrap.conf` — edit that file and rerun with `--force` to change them.

What you get:

```
hyperswitch-config/
├── argocd/
│   ├── argo-apps.yaml                              # root app-of-apps
│   ├── bootstrap/argocd.yaml                       # Argo CD manages itself
│   ├── projects/hyperswitch.yaml                   # what the application may do
│   └── apps/hyperswitch/hyperswitch-stack.yaml     # the Hyperswitch application
├── infra-configurations/
│   └── hyperswitch-stack/values.yaml               # <- you edit this
├── deployment-configs/
│   └── hyperswitch-stack/values-dep.yaml           # <- and this
├── install-argocd.sh                               # cluster bootstrap script
└── SELF_HOST.md                                    # your generated runbook
```

The values files are layered: `infra-configurations/` holds anything tied to your infrastructure (database, cache, domains, ingress), and `deployment-configs/` is applied after it for application overrides (environment variables, feature flags, connector settings).

_`Update the values according to your requriements`_

***

### Step 2 — Push the changes

Argo CD can only read what is pushed.

```bash
cd hyperswitch-config
git add -A
git commit -m "hyperswitch self-host configuration"
git remote add origin https://github.com/<your-org>/<your-config-repo>.git # Only if it is a new repo
git push -u origin main
```

***

### Step 3 — Install Argo CD & other required applications

Run `install-argocd.sh` from the root of the repository you generated in Step 1.&#x20;

```bash
cd hyperswitch-config
./install-argocd.sh
```

Answer the question as per your requirements.

***

### Step 4 — Connect Argo CD to your repository

Only if your repository is private:

```bash
argocd repo add https://github.com/<your-org>/<your-config-repo>.git \
  --username <user> --password <personal-access-token>
```

***

### Step 5 — Sync

It reads the chart, version, namespace and values from your own `argocd/` files, and asks before each step. Answer `skip` for anything already installed.

Get the admin password, port forward and open the UI:

```bash
kubectl -n argocd get secret argocd-initial-admin-secret \
  -o jsonpath='{.data.password}' | base64 -d

kubectl port-forward svc/argocd-server -n argocd 8080:443
```

Log in at `https://localhost:8080` as `admin`.&#x20;

Sync all the applications we brought up.

### Step 6 — Verify

```bash
kubectl get pods -n argocd     
kubectl get pods -n hyperswitch
```

Then check the router. `/health` says the process is up; `/health/ready` is the deep health check and covers the database, Redis and the other dependencies:

```bash
curl https://api.example.com/health
curl https://api.example.com/health/ready
```

You are now ready to log in to your Control Center and create your first merchant account.
