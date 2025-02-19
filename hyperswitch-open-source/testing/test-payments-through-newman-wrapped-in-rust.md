---
description: >-
  Test payments through CLI version of Postman, Newman which resides in a Rust
  wrapper called as Rustman
icon: stethoscope
---

# Test payments through Newman wrapped in Rust

### Newman

To begin with, a fork of Newman needs to be installed by executing `npm install -g 'https://github.com/knutties/newman.git#feature/newman-dir'`

This Newman fork has built-in support exporting and importing a postman collection in the form directory unlike having a single large `.json` collection file.

<figure><img src="../../.gitbook/assets/image (147).png" alt="" width="375"><figcaption><p>The main feature of the newman fork, directory support</p></figcaption></figure>

To see the features that the fork of `newman` supports, click [_**here**_](https://github.com/knutties/newman/blob/feature/newman-dir/DIR_COMMANDS.md)

### Test Utils Usage

* Add the connector credentials to the `connector_auth.toml` / `auth.toml` by creating a copy of the `sample_auth.toml` from `router/tests/connectors/sample_auth.toml`
*   Export the auth file path as an environment variable:

    ```shell
    export CONNECTOR_AUTH_FILE_PATH=/path/to/connector_auth.toml
    ```

#### Supported Commands

Required fields:

* `--admin-api-key` -- Admin API Key of the environment. `test_admin` is the Admin API Key for running locally
* `--base-url` -- Base URL of the environment. `http://127.0.0.1:8080` / `http://localhost:8080` is the Base URL for running locally
* `--connector-name` -- Name of the connector that you wish to run. Example: `adyen`, `shift4`, `stripe`

Optional fields:

* `--delay` -- To add a delay between requests in milliseconds.
  * Maximum delay is 4294967295 milliseconds or 4294967.295 seconds or 71616 minutes or 1193.6 hours or 49.733 days
  * Example: `--delay 1000` (for 1 second delay)
* `--folder` -- To run individual folders in the collection
  * Use double quotes to specify folder name. If you wish to run multiple folders, separate them with a comma (`,`)
  * Example: `--folder "QuickStart"` or `--folder "Health check,QuickStart"`
  * If a specific folder needs to be run, automatically `QuickStart` folder will be executed first to avoid issues with account creation and setup.
* `--header` -- If you wish to add custom headers to the requests, you can pass them as a string
  * Example: `--header "key:value"`
  * If you want to pass multiple custom headers, you can pass multiple `--header` flags
    * Example: `--header "key1:value1" --header "key2:value2"`
* `--verbose` -- A boolean to print detailed logs (requests and responses)

**Note:** Passing `--verbose` will also print the connector as well as admin API keys in the logs. So, make sure you don't push the commands with `--verbose` to any public repository.

#### Running tests

*   Tests can be run with the following command:

    ```shell
    cargo run --package test_utils --bin test_utils -- --connector-name=<connector_name> --base-url=<base_url> --admin-api-key=<admin_api_key> \
    # optionally
    --folder "<folder_name_1>,<folder_name_2>,...<folder_name_n>" --verbose
    ```

**Note**: You can omit `--package test_utils` at the time of running the above command since it is optional.

The command `cargo run --package test_utils --bin test_utils -- --connector-name=<connector_name> --base-url=<base_url> --admin-api-key=<admin_api_key>`  will generate newman commands on the go and execute the collection.
