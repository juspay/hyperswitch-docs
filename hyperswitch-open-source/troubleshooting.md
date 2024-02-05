---
description: >-
  This guide explains how to troubleshoot the Hyperswitch setup and verify if
  all the components are up and running as expected
---

# ⚒ Troubleshooting

{% hint style="info" %}
The deep health check endpoint will be rolled out in the monthly stable version release planned for February 2024
{% endhint %}

## System Health Check

Hyperswitch provides a deep health check endpoint to check if the various components involved are up and running. To check the readiness of the application, you can run the following command.

```bash
curl http://localhost:8080/health/ready
```

The above command will check the Database connection, Redis connection, Hyperswitch Vault connection (if enabled), ability to send outgoing requests, and the health of analytical components. If the components are up and running with the correct configurations, you will get a success response as shown below

```json
{
    "database": true,
    "redis": true,
    "vault": true,
    "analytics": true,
    "outgoing_request": true
}
```

If there is an issue with one of the components, the API will return an error response which will indicate the reason for the failure. For example, if the app server is not able to connect with the database, the error response would be as follows

```json
{
    "error": {
        "type": "api",
        "message": "Database health check failed with error: Error while connecting to database",
        "code": "HE_00"
    }
}
```

Additionally you can add this as a Readiness Probe in your Kubernetes Deployment

```yaml
readinessProbe:
  httpGet:
    path: /health/ready
    port: 8080
  initialDelaySeconds: 5
  periodSeconds: 15
```

In case the app server does not start due to the failure of the readiness probe, you can check the logs through Kubernetes Logs using the below command

{% code fullWidth="false" %}
```bash
kubectl logs <your-pod-name> --tail 10 -n <your-namespace-name> -c <container-name>
```
{% endcode %}

