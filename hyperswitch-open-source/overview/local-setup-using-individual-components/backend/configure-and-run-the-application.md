---
description: Configure and run the Hyperswitch server application locally to start processing payments through your self-hosted infrastructure
icon: panel-ews
---

# Configure and Run the Application

## Configure the application

The application configuration files are present under the [`config`](https://github.com/juspay/hyperswitch/blob/main/config) directory.

The configuration file read varies with the environment:

* Development: [`config/development.toml`](https://github.com/juspay/hyperswitch/blob/main/config/development.toml)
* Sandbox: `config/sandbox.toml`
* Production: `config/production.toml`

Refer to [`config.example.toml`](https://github.com/juspay/hyperswitch/blob/main/config/config.example.toml) for all the available configuration options. Refer to [`development.toml`](https://github.com/juspay/hyperswitch/blob/main/config/development.toml) for the recommended defaults for local development.

Update the [`development.toml`](https://github.com/juspay/hyperswitch/blob/main/config/development.toml) file if different database credentials are used as compared to the sample ones included in this guide.

After configuring the application, proceed with [running the application](configure-and-run-the-application.md#run-the-application).

### Run the application

1. Compile and run the application using `cargo`:

   ```bash
   cargo run
   ```

   If you are using `nix`, you can compile and run the application using `nix`:

   ```bash
   nix run
   ```

2. Verify that the server is up and running by hitting the health endpoint:

   ```bash
   curl --head --request GET 'http://localhost:8080/health'
   ```

   If the command returned a `200 OK` status code, proceed with trying out the APIs.

{% content-ref url="try-out-apis.md" %}
[try-out-apis.md](try-out-apis.md)
{% endcontent-ref %}
