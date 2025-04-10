---
icon: badge-check
---

# Run Hyperswitch Locally Using Docker

{% embed url="https://youtu.be/6yJCvskbc80" %}

{% hint style="danger" %}
This setup automatically runs all three components of Hyperswitch (Backend, Control Center, and SDK) on your machine at once using Docker.
{% endhint %}

## Setup using Docker

If you don't already have Docker, you can [download](https://docs.docker.com/get-docker/) it from the official Docker website. \
Once Docker is installed, launch the Docker app, then use the following commands at the command line to clone the Hyperswitch repository.

{% hint style="danger" %}
You can alternatively use [Orbstack](https://orbstack.dev/) or [Podman](https://podman.io/) instead of docker.
{% endhint %}

```
git clone --depth 1 --branch latest https://github.com/juspay/hyperswitch
```

Once the repository is cloned, switch to the project directory.

```
cd hyperswitch
```

Now, we'll start all services using Docker Compose. This will pull Hyperswitch Docker images and then start the server. Wait for the `migration_runner` container to finish running migrations (approximately 2 minutes) before proceeding further.

```
docker compose up -d
```

Congratulations! You've now setup Hyperswitch in your local machine. In order to verify that the server is up and running hit the health endpoint.

```
curl --head --request GET 'http://localhost:8080/health'
```

The expected response here is `200 OK` status code. This indicates that the server and all of its dependent services such as the database and Redis are functioning correctly.

**Access the Control Centre in your browser at** [**http://localhost:9000**](http://localhost:9000/)

{% hint style="warning" %}
If you face any issues during setup, please feel free to post in the #dev-support channel in our [Slack community](https://join.slack.com/t/hyperswitch-io/shared_invite/zt-2jqxmpsbm-WXUENx022HjNEy~Ark7Orw), and our team will respond as soon as possible.
{% endhint %}

If you're **looking to Contribute to Hyperswitch**, try [setting up a **development environment** using Docker Compose](https://github.com/juspay/hyperswitch/blob/main/docs/try_local_system.md#set-up-a-development-environment-using-docker-compose).&#x20;

## Next step:

{% content-ref url="../../account-setup/" %}
[account-setup](../../account-setup/)
{% endcontent-ref %}
