# Configuring and Running the Application

## Configure the application

The application configuration files are present under the [`config`](https://github.com/juspay/hyperswitch/blob/main/config) directory.

The configuration file read varies with the environment:

* Development: [`config/development.toml`](https://github.com/juspay/hyperswitch/blob/main/config/development.toml)
* Sandbox: `config/sandbox.toml`
* Production: `config/production.toml`

Refer to [`config.example.toml`](https://github.com/juspay/hyperswitch/blob/main/config/config.example.toml) for all the available configuration options. Refer to [`development.toml`](https://github.com/juspay/hyperswitch/blob/main/config/development.toml) for the recommended defaults for local development.

Ensure to update the [`development.toml`](https://github.com/juspay/hyperswitch/blob/main/config/development.toml) file if you opted to use different database credentials as compared to the sample ones included in this guide.

Once you're done with configuring the application, proceed with [running the application](configuring-and-running-the-application.md#run-the-application).

### Run the application

1.  Compile and run the application using `cargo`:

    ```bash
    cargo run
    ```

    If you are using `nix`, you can compile and run the application using `nix`:

    ```bash
    nix run
    ```
2.  Verify that the server is up and running by hitting the health endpoint:

    ```bash
    curl --head --request GET 'http://localhost:8080/health'
    ```

    If the command returned a `200 OK` status code, proceed with trying out our APIs.

{% content-ref url="try-out-apis.md" %}
[try-out-apis.md](try-out-apis.md)
{% endcontent-ref %}
