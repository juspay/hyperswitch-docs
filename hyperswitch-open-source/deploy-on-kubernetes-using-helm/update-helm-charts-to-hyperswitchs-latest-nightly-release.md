# Update Helm Charts to Hyperswitch's Latest Nightly Release

Update charts/incubator/hyperswitch-stack/values.yaml to point to the most recent nightly release for the router, consumer, producer and drainer.

```
services:
    router:
      version: nightly
      image: docker.juspay.io/juspaydotin/hyperswitch-router:nightly
      host: *router_host
    consumer:
      version: nightly
      image: docker.juspay.io/juspaydotin/hyperswitch-consumer:nightly
    producer:
      version: nightly
      image: docker.juspay.io/juspaydotin/hyperswitch-producer:nightly
    drainer:
      image: docker.juspay.io/juspaydotin/hyperswitch-drainer:nightly
      version: nightly
```

Manually update configs based on the output of git diff command. Add configs that are labelled as “+” and remove the ones that are labelled as “-” in the respective files 1,2 mentioned below.

1\. charts/incubator/hyperswitch-app/configs/router-sandbox.toml\
\
sandbox.toml contains sandbox/test environment configurations, including:

* Test/sandbox base URLs for payment connectors
* Bank configuration for redirect payment methods
* Payment method filters by country and currency
* Connector-specific test credentials and endpoints
* Dummy connector settings for testing

Run the below command to generate the differences and update the router-sandbox.toml file

```
git diff --unified=10 --ignore-space-change --ignore-space-at-eol <<current version in helm charts>> nightly config/deployments/sandbox.toml
```

2\. charts/incubator/hyperswitch-app/configs/misc.toml

env\_specific.toml contains environment-specific configurations and secrets, including:

* Database connection settings (master and replica)
* External service credentials (AWS, payment processors, etc.)
* API keys and encryption keys
* Service endpoints and authentication settings
* Feature flags and operational parameters
* Logging and monitoring configurations

Run the below command to generate the difference and update misc.toml file

```
git diff --unified=10 --ignore-space-change --ignore-space-at-eol <<current version in helm charts>> nightly config/deployments/env_specific.toml
```

\
