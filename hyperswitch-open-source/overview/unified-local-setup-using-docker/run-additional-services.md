---
icon: arrows-to-circle
---

# Run Additional Services

The default behaviour for docker compose only runs the following services:

1. hyperswitch server
2. hyperswitch control center
3. hyperswitch web sdk
4. postgres
5. redis (standalone)

You can run the **scheduler, data and monitoring services** by specifying suitable profile names to the above Docker Compose command. To understand more about the hyperswitch architecture and the components involved, check out the [architecture document](https://github.com/juspay/hyperswitch/blob/main/docs/architecture.md).

*   To run the scheduler components (consumer and producer), you can specify `--profile scheduler`:

    ```bash
    docker compose --profile scheduler up -d
    ```
*   To run the monitoring services (Grafana, Promtail, Loki, Prometheus and Tempo), you can specify `--profile monitoring`:

    ```bash
    docker compose --profile monitoring up -d
    ```

    You can then access Grafana at `http://localhost:3000` and view application logs using the "Explore" tab, select Loki as the data source, and select the container to query logs from.
*   To run the data services (Clickhouse, Kafka and Opensearch) you can specify the `olap` profile

    ```bash
    docker compose --profile olap up -d
    ```

    You can read more about using the data services [here](https://github.com/juspay/hyperswitch/blob/main/crates/analytics/docs/README.md)
*   You can also specify multiple profile names by specifying the `--profile` flag multiple times. To run both the scheduler components and monitoring services, the Docker Compose command would be:

    ```bash
    docker compose --profile scheduler --profile monitoring up -d
    ```

Once the services have been confirmed to be up and running, you can proceed with [trying out our APIs](run-additional-services.md#try-out-our-apis).
