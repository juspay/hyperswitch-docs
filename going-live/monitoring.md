---
description: Visibility and control over your application
---

# 👀 Monitoring

{% hint style="info" %}
In this chapter, you will learn to setup logs and monitoring on your application. Hyperswitch relies on Promtail, Loki, OpenTelemetry and Grafana for its logs and metrics. In this guide, we will delve into these tools and assist you in setting them up efficiently.
{% endhint %}

***

In the world of application monitoring, two critical elements play pivotal roles&#x20;

<table><thead><tr><th width="108">Element</th><th>What is it</th><th>Why is it required</th></tr></thead><tbody><tr><td>Logs</td><td>Logs are a running diary of all the activities that happen inside the application</td><td>Useful for tracking, debugging, and auditing</td></tr><tr><td>Metrics</td><td>Metrics are like measuring sticks (like a counter) highlighting the performance of the different parts of the application</td><td>Used to assess, analyze, and track various aspects of a system/application providing data-driven insights </td></tr></tbody></table>

To effectively utilize both aspects, Hyperswitch relies on the following

* Promtail (for scraping logs)
* Grafana's Loki (for storing and viewing logs)
* OpenTelemetry collector (for application metrics)
* Cloudwatch (for system metrics)

This combination, along with Grafana for visualization, seamlessly integrates logs and metrics into intuitive, interactive dashboards.&#x20;

<figure><img src="../.gitbook/assets/Monitoring architecture (3).jpg" alt=""><figcaption></figcaption></figure>

***

## Logs with Grafana Loki and Promtail

### 1. What is Grafana Loki and Promtail?

* **Grafana Loki:** Grafana Loki is a standout in log aggregation. It draws inspiration from Prometheus and is designed to be horizontally scalable and highly available, with a focus on multi-tenancy. Unlike traditional logging systems, Loki doesn't index the content of logs but concentrates on a set of labels associated with each log stream. This approach not only keeps costs in check but also ensures swift access to logs during queries. Refer [here](https://grafana.com/docs/loki/latest/get-started/) for more details regarding Loki.
* **Promtail:** Promtail serves as the agent that powers Loki by collecting logs. Tailored specifically for Loki, Promtail runs on each Kubernetes node and utilizes the same service discovery mechanisms as Prometheus. Before sending logs to Loki, Promtail labels, transforms, and filters them to ensure that only relevant data reaches Loki. This data processing streamlines the logging process. Additionally, Loki boasts its own query language, LogQL, which is compatible with its command-line interface and Grafana. Integration capabilities with Prometheus's Alert Manager further solidify Loki's position as a pivotal tool in modern logging. To know more about Promtail refer [here](https://grafana.com/docs/loki/latest/send-data/promtail/).

### 2. Installing Loki and Promtail

By following these installation steps, you can set up Grafana Loki and Promtail effectively, enabling comprehensive logging capabilities for your application monitoring needs.

**Step 1: Install helm**

{% tabs %}
{% tab title="MacOs" %}
If you're using MacOS and don't have Helm installed, you can easily install it using the following command with Homebrew:

```
brew install helm
```
{% endtab %}

{% tab title="Debian/Ubuntu Linux" %}


To install Helm on Debian/Ubuntu Linux, follow these steps:

a. Download and add Helm's GPG key to your keyring:

```
curl https://baltocdn.com/helm/signing.asc | gpg --dearmor | sudo tee /usr/share/keyrings/helm.gpg > /dev/null
```

b. Install the 'apt-transport-https' package, which is necessary for secure package downloads:

```
sudo apt-get install apt-transport-https --yes
```

c. Add Helm's repository to your package sources:

```
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/helm.gpg] https://baltocdn.com/helm/stable/debian/ all main" | sudo tee /etc/apt/sources.list.d/helm-stable-debian.list
```

d. Update the package list:

```
sudo apt-get update
```

e. Finally, install Helm:

```
sudo apt-get install helm --yes
```
{% endtab %}
{% endtabs %}

**Step 2: Install Loki**

Once Helm is installed, you can proceed with the installation of Loki. Loki can be installed in various modes, and [here](https://grafana.com/docs/loki/latest/setup/install/helm/install-scalable/), we provide a setup guide for installing Loki in a scalable monolithic mode.

Make sure you install grafana/loki in a specific kubernetes namespace that you desire using command

```bash
helm install --namespace your-namespace --values values.yaml loki grafana/loki
```

**Step 3: Install Promtail**

To set up the endpoint for Loki's gateway, which Promtail will use to transmit logs, we need to specify it in the Promtail chart's configuration values. In our specific scenario, the designated endpoint is "loki.grafana-loki.svc.cluster.local." Let's proceed by incorporating this endpoint into the Promtail chart values.

1. First, let's obtain the basic values for the Grafana Promtail chart and store them in a file named "promtail-overrides.yaml" by running the following command

```bash
helm show values grafana/promtail > promtail-overrides.yaml
```

2. Next, open the `promtail-overrides.yaml` file and locate the section that specifies the Loki clients' URL. Replace the existing URL:

```yaml
clients:
  - url: http://loki-gateway/loki/api/v1/push
```

with the new endpoint:

```yaml
clients:
  - url: http://loki.grafana-loki.svc.cluster.local/loki/api/v1/push
```

3. With the endpoint correctly updated in the configuration, we are now ready to deploy Promtail. Execute the following command and patiently wait for all pods to reach a "Ready" state:

```bash
helm upgrade --install --values promtail-overrides.yaml promtail grafana/promtail -n grafana-loki
```

By following these steps, you will configure Promtail to utilize the specified "loki.grafana-loki.svc.cluster.local" endpoint for log transmission to Loki, ensuring seamless integration into your monitoring environment.

## Grafana for Visibility

### 1.  Installing Grafana

You can proceed with the installation of the Helm chart for Grafana using the following commands:

```bash
# Add the Grafana Helm chart repository
helm repo add grafana https://grafana.github.io/helm-charts

# Update the Helm repositories
helm repo update

# Install Grafana using Helm, specifying the namespace and creating it if necessary
helm install grafana grafana/grafana --namespace your_namespace --create-namespace
```

It's worth noting that in a standard installation, the Grafana service is of type ClusterIP. However, if you are using MetalLB as a network load balancer in your cluster and have configured the service type as LoadBalancer, you can disregard this information. We will address port-forwarding for the service at a later stage.

### 2.  Configuring Data Source in Grafana

To configure Grafana's data sources and dashboard, follow these steps:

1.  Port-forward Grafana to access it locally:

    <pre class="language-bash"><code class="lang-bash"><strong>kubectl port-forward service/grafana 8080:80 -n grafana
    </strong></code></pre>

    You can also choose to expose Grafana differently, such as assigning it an external IP via a Load Balancer or setting up an Ingress route depending on your preference.
2.  Obtain the login credentials:

    By default, the Grafana username is "admin." However, you'll need to retrieve the password. First, list all the Secrets in your namespace:

    ```bash
    kubectl get secrets -n your_namespace
    ```

    Locate the secret containing the password. To extract and decode it, use the following command:

    ```bash
    kubectl get secret grafana_secret_name -n your_namespace -o jsonpath="{.data.admin-password}" | base64 --decode ; echo
    ```

    This will provide you with the password required to log in.
3. Log in to Grafana using the obtained credentials.
4. Add Grafana Loki as a data source:
   * Access the Grafana interface via http://localhost:8080/ or the respective URL if you have exposed it differently.
   * Navigate to the Data Sources section in the Grafana UI.
   * Click on "Add data source."
   * Configure the data source with the following details:
     * Name: Choose a descriptive name for the data source.
     * Type: Select "Loki" from the list of available data sources.
     * HTTP URL: Use the endpoint of the Grafana Loki gateway service. In your case, it appears to be: http://loki-loki-distributed-gateway.grafana-loki.svc.cluster.local.
   * Test the data source to ensure it's working correctly.
   * Save the data source configuration.

Now you have successfully configured Grafana's data source with Grafana Loki, and you can proceed to create dashboards and visualize your data. Similarly, you can configure Prometheus for metrics.

### 3.  Web client logs

Logging from the payment checkout web client is crucial for tracking and monitoring the flow of payments. It provides a transparent record of events, errors, and user interactions, aiding developers and support teams in identifying issues, debugging, and ensuring the security and reliability of payment processes. Well-implemented logging enhances traceability and facilitates a more efficient resolution of potential problems in the payment checkout experience.

Logs are sent to the server via non-blocking Beacon API requests. This means that even if the logging endpoint configured is incorrect, it would not affect the core payment functionalities. You can find more about the structure of logging request payload in the `beaconApiCall` function in the `OrcaLogger.res` file.

If you want to collect logs, you can do so by setting up an endpoint on your server to receive, process and persist logs.

In `webpack.common.js`, you would have to enable the logging flag, and configure the logging endpoint and log level.

```javascipt
let logEndpoint =
  sdkEnv === "prod"
    ? "<YOUR_PRODUCTION_LOGGING_ENDPOINT>"
    : "<YOUR_SANDBOX_LOGGING_ENDPOINT>";

// Set this to true to enable logging
let enableLogging = true;

// Choose from DEBUG, INFO, WARNING, ERROR, SILENT
let loggingLevel = "DEBUG";
```

<figure><img src="../.gitbook/assets/Screenshot 2023-11-24 at 5.00.03 PM.png" alt=""><figcaption><p>Understanding Logging Levels</p></figcaption></figure>
