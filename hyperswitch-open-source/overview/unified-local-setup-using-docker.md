---
icon: badge-check
---

# Run Hyperswitch Locally Using Docker

{% embed url="https://youtu.be/6yJCvskbc80" %}

{% hint style="success" %}
This setup automatically runs all three components of Hyperswitch (Backend, Control Center, and SDK) on your machine at once using Docker.
{% endhint %}

## Setup using Docker

You can run Hyperswitch on your system using [Docker compose](https://docs.docker.com/get-docker/) after cloning this repository. We recommend using Docker Desktop for Windows and Mac OS. On Linux, you can install Docker Engine directly.

{% hint style="warning" %}
You can alternatively use [Orbstack](https://orbstack.dev/) or [Podman](https://podman.io/) instead of docker.
{% endhint %}

Once Docker is installed, launch the Docker app, then use the following command at the command line to clone the Hyperswitch repository.

```
git clone --depth 1 --branch latest https://github.com/juspay/hyperswitch
cd hyperswitch
docker compose up -d
# This script verifies the setup and provides links to the individual components.
scripts/docker_output.sh
```

{% hint style="warning" %}
If you face any issues during setup, please feel free to post in the #dev-support channel in our [Slack community](https://join.slack.com/t/hyperswitch-io/shared_invite/zt-2jqxmpsbm-WXUENx022HjNEy~Ark7Orw), and our team will respond as soon as possible.
{% endhint %}

If you're **looking to Contribute to Hyperswitch**, try [setting up a **development environment** using Docker Compose](https://github.com/juspay/hyperswitch/blob/main/docs/try_local_system.md#set-up-a-development-environment-using-docker-compose).&#x20;

## Next step:

{% content-ref url="../account-setup/" %}
[account-setup](../account-setup/)
{% endcontent-ref %}
