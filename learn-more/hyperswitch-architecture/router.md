# Router

{% hint style="info" %}
Know about the architecture and the components involved
{% endhint %}

The router service is written in rust to enforce type safety and to maintain superior performance. The router is designed with a hexagonal architecture, to allow independent pieces to be managed separately.

## Core API Layer

* The HTTP requests hit the Core API Layer.&#x20;
* Based on the API endpoint/group, appropriate authentication mechanisms are invoked and the request is authenticated.
* The incoming data payload is validated. This includes validating the the payload data itself along with validating data against the merchant config etc. For example, a refund should be only against a successful payment.
* The valid incoming data is then stored. If the API action is complete, then successful response is returned. If the API action includes connector calls, then the status from the connector module determines the successful/failure response.&#x20;
* In case of failure response from connector, appropriate status mapping takes place to unify the user interface.

## Connectors

Connectors are external services that hyperswitch can interact with. It could be payments processors, fraud and risk management services, tokenization services etc.

* The API request type, API data, and merchant config determines one or more connectors to be called by hyperswitch.
* Connector module consists of code logic to build the necessary request data to talk to the selected services and understand the response from such services.&#x20;
* Connector can also handle cases where some requests and services may require multiple API calls for a single API action.&#x20;

## Asynchronous jobs Scheduler

Some API actions may run for long time and API response cannot be delayed for such actions to complete. In such cases, the router will return success response with intermediate state like processing. For example, payment processor may not return a success response, and hyperswitch needs to check for the status after sometime.

The required action is then queued for the scheduler to execute asynchronously. The scheduler determines the jobs to be run based on the scheduled time, executes them, and updates the router storage. It also triggers any other action required in the router, like a webhook call to the server.
