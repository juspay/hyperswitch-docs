---
description: Stay up to date with minimal maintenance effort!
---

# ♻️ Updates

{% hint style="info" %}
This chapter covers everything you need to know about handling maintenance and updates for your application.
{% endhint %}

***

## Hyperswitch version updates

Hyperswitch requires minimal maintenance effort, and updating to newer versions is quite simple

* Hyperswitch adheres to a **monthly release schedule**, with versions undergoing thorough internal testing before being deemed stable
* Stay informed about updates by checking our [GitHub releases](https://github.com/juspay/hyperswitch/releases) page
* Hyperswitch follows semantic versioning for all releases

{% hint style="success" %}
**Our releases ensure backward compatibility** between the three components - the App Server, Web Client and Control Center

In case of any release which defers backward compatibility, prior announcement will be made along with the expected action
{% endhint %}

### Updating the application

Often, when you are upgrading to a latest version of Hyperswitch, you would also need to take care of two aspects

<details>

<summary>Database Schema Additions</summary>

***

**Why is this required?**

This is required due to any schema additions/ deletions required due to the new features

***

**How to update the schema?**

* The SQL commands for database schema changes would be included in the `up.sql` files included in sub-directories of the `migrations` directory in the repository
* You can easily obtain the commands to be run with a command like the one below

{% code overflow="wrap" fullWidth="false" %}
```bash
$ git diff --name-only <CURRENT_VERSION>..<NEW_VERSION> migrations/**/up.sql | sort | xargs cat
```
{% endcode %}

* You can log in to the database console and run the SQL commands obtained

</details>

<details>

<summary>Configuration Updates (ENVs)</summary>

***

**Why is this required?**

* Environment variables typically store configuration data such as API endpoints, database connection details, security credentials, feature toggles, and application settings
* Managing them in each new release is essential to accommodate changes, adapt to evolving requirements, maintain security, and ensure the application functions are as intended

***

**How to update the environment variables?**

* Hyperswitch allows specifying application configuration variables from two sources a TOML file and environment variables, with environment variables having higher priority
* Except for some values such as database connection information that must be provided, if a configuration variable has not been specified in either source, the application uses default values specified in code
* To ease the management of application configuration variables, the suggested approach would be to specify values that would depend on the deployment environment such as database and Redis URLs and some secrets values (such as admin API key, master encryption key, etc.) via environment variables, and specifying domain related configuration variables (such as payment methods enabled for a specific connector, base URLs used for accessing connectors, etc.) via the TOML file
* This way, you can just copy over the [`development.toml`](https://github.com/juspay/hyperswitch/blob/main/config/development.toml) file from the repository for ensuring that the application configuration variables are up-to-date

</details>

### Web Client Updates

Hyperswitch Web client is periodically updated for new features and bug fixes.&#x20;

* Please note that the web client adheres strictly to semantic versioning for consistent releases.
* Please follow the [Changelog](https://github.com/juspay/hyperswitch-web/blob/main/CHANGELOG.md) to get the latest updates. You can pull the latest changes to get new features or build new features and contribute to the `hyperswitch-web` repo for others to use.
* For ensuring backward compatibility, please ensure that the major version of the web client is the same as that of the app server's major release version.

## Request Features or Report Bugs

You can reach out to us about new features or report bugs on GitHub:

1. You can [request for a new feature](https://github.com/juspay/hyperswitch/issues/new?assignees=\&labels=C-feature%2CS-awaiting-triage\&projects=\&template=feature\_request.yml\&title=%5BFEATURE%5D+) if it hasn't been requested already on [our issue tracker](https://github.com/juspay/hyperswitch/issues?q=is%3Aissue+is%3Aopen).
2. You can [report a bug](https://github.com/juspay/hyperswitch/issues/new?assignees=\&labels=C-bug%2CS-awaiting-triage\&projects=\&template=bug\_report.yml\&title=%5BBUG%5D+) if there isn't hasn't been reported already on [our issue tracker](https://github.com/juspay/hyperswitch/issues?q=is%3Aissue+is%3Aopen).
3. You can [open a GitHub discussion](https://github.com/juspay/hyperswitch/discussions/new/choose), or reach out to us on our [Discord server](https://discord.gg/wJZ7DVW8mm) or [Slack workspace](https://join.slack.com/t/hyperswitch-io/shared\_invite/zt-1k6cz4lee-SAJzhz6bjmpp4jZCDOtOIg) for any general help or queries that you may have.

{% hint style="danger" %}
Steps for updating and maintaining the Control Centre would be updated in this chapter soon!
{% endhint %}
