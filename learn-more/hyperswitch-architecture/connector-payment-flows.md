---
description: >-
  This page outlines the various payment flows you may come across while
  building a connector.
---

# Connector Payment Flows

### Pre-processing

This refers to the two-step payment flow where preprocessing steps are executed before the main authorization call. If your connector does not use tokenization or does not require customer or access token flows, implement the pre-processing pattern described below. It's important to note that different connectors implement preprocessing differently. For example, Airwallex creates payment intents during preprocessing as one of the steps while Nuvei performs 3DS enrollment checks as a step. The preprocessing call does make a separate (second) call for the authorize flow. The preprocessing and authorization are implemented as distinct, sequential operations in Hyperswitch's payment processing pipeline.

The preprocessing steps are executed first:

* **Preprocessing Execution**: The system creates a preprocessing connector integration and executes it
* **Data Transformation**: Converts the authorize request data to preprocessing request data
* **Connector Processing**: Executes the preprocessing step through the connector
* **Response Handling**: Processes the preprocessing response and updates the router data accordingly

Then, the system proceeds to build the actual authorization request:

* **First Call | Preprocessing**: The system creates a preprocessing connector integration and executes it
* **Response Processing**: The preprocessing response updates the router data
* **Second Call | Authorization**: After preprocessing completes, the system proceeds with the actual authorization flow

**When to Use This Flow** Use this pattern if:

* The connector issues temporary session credentials.
* You need to make a discovery or configuration call before authorization.
* No prior customer setup or vaulting is needed.

**Example Diagram**

<figure><img src="../../.gitbook/assets/Slide 16_9 - 130.jpg" alt=""><figcaption></figcaption></figure>

## Authorization Flow

This flow represents the core payment authorization logic executed once all prerequisite steps are complete. For example, after the pre-processing stage finishes, the authorization flow runs. At this point, the sequence below is evaluated, after which the authorization logic determines the next steps and uses the necessary tokens to construct the request:

* **Access Token Addition**: Adds access tokens if required by the connector
* **Session Token Addition**: Handles session tokens for wallet payments
* **Payment Method Tokenization**: Tokenizes payment methods if needed
* **Preprocessing Steps**: Executes preprocessing logic
* **Connector Customer Creation**: Creates customer records at the connector level

#### **Decision Logic**

The flow includes intelligent decision-making capabilities:

* **Authentication Type Decision**: Automatically steps up Google Pay transactions to 3DS when risk indicators are present
* **Proceed Decision**: Determines whether to proceed with authorization based on preprocessing responses (e.g., skips authorization if redirection is required)

**Example Diagram**

<figure><img src="../../.gitbook/assets/Slide 16_9 - 129.jpg" alt=""><figcaption></figcaption></figure>
