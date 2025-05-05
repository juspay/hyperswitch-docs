---
icon: badge-check
---

# Run Hyperswitch Locally Using Docker

{% embed url="https://youtu.be/6yJCvskbc80" %}

{% hint style="success" %}
This setup automatically runs all three components of Hyperswitch (Backend, Control Center, and SDK) on your machine at once using Docker.
{% endhint %}

## Setup using Docker

You can run Hyperswitch on your system using [Docker compose](https://docs.docker.com/get-docker/). We recommend using Docker Desktop for Windows and Mac OS. On Linux, you can install Docker Engine directly.

{% hint style="warning" %}
You can alternatively use [Podman](https://podman.io/) or [Orbstack](https://orbstack.dev/) (for macOS) instead of docker.
{% endhint %}

Once Docker is installed, launch the Docker desktop app, then use the following command at the command line.

```
git clone --depth 1 --branch latest https://github.com/juspay/hyperswitch
cd hyperswitch
scripts/setup.sh
```

The above command will:

* Check for prerequisites (Docker Compose/Podman)
* Set up necessary configurations (PostgreSQL, Redis)
* Let you select a setup option:
  * **Standard**: (Recommended) App server + Control Center + Web SDK
  * **Full**: Standard + Monitoring + Scheduler
  * **Standalone App Server**: Core services only App Server
* Start the selected services
* Provide link to access various components

If you're **looking to Contribute to Hyperswitch**, try [setting up a **development environment** using Docker Compose](https://github.com/juspay/hyperswitch/blob/main/docs/try_local_system.md#set-up-a-development-environment-using-docker-compose).&#x20;

{% hint style="info" %}
**Have Questions?**\
Join our [Slack Community](https://join.slack.com/t/hyperswitch-io/shared_invite/zt-2jqxmpsbm-WXUENx022HjNEy~Ark7Orw) to ask questions, share feedback, and collaborate.\
Prefer direct support? Use our [Contact Us](https://hyperswitch.io/contact-us) page to reach out.
{% endhint %}

## Next step:

{% content-ref url="../account-setup/" %}
[account-setup](../account-setup/)
{% endcontent-ref %}
