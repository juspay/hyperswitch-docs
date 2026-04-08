# Table of contents


## PRISM


- [Product Overview](prism/README.md)
  - [Installation & Configuration](prism/getting-started/installation.md)
  - [First Payment](prism/getting-started/first-payment.md)
  - [Extend to More Flows](prism/getting-started/extend-to-more-flows.md)

- [Architecture Overview](prism/architecture/README.md)
  - [PCI Compliance](prism/architecture/compliance/compliance.md)
  - [Connector Settings and Overrides](prism/architecture/concepts/connector-settings-and-overrides.md)
  - [Services and Methods](prism/architecture/concepts/services-and-methods.md)
  - [Environment Settings](prism/architecture/concepts/environment-settings.md)
  - [Error Handling](prism/architecture/concepts/error-handling.md)
  - [Error Mapping](prism/architecture/concepts/error-mapping.md)
  - [ID and Object Modelling](prism/architecture/concepts/id-and-object-modelling.md)
  - [Modes of Usage](prism/architecture/concepts/modes-of-usage.md)
  - [Domain specific language](prism/architecture/concepts/specs-and-dsl.md)
  - [Integrity and Source Verification](prism/architecture/frameworks/integrity-and-source-verification.md)
  - [Money Struct](prism/architecture/frameworks/money-struct.md)
  - [Versioning](prism/architecture/versioning.md)

- [API Reference Overview](prism/api-reference/README.md)
    - [Payment Service Overview](prism/api-reference/services/payment-service/README.md)
    - [Authorize](prism/api-reference/services/payment-service/authorize.md)
    - [Capture](prism/api-reference/services/payment-service/capture.md)
    - [Void](prism/api-reference/services/payment-service/void.md)
    - [Refund](prism/api-reference/services/payment-service/refund.md)
    - [Get](prism/api-reference/services/payment-service/get.md)
    - [Reverse](prism/api-reference/services/payment-service/reverse.md)
    - [Setup Recurring](prism/api-reference/services/payment-service/setup-recurring.md)
    - [Incremental Authorization](prism/api-reference/services/payment-service/incremental-authorization.md)
    - [Verify Redirect Response](prism/api-reference/services/payment-service/verify-redirect-response.md)
  - [Recurring Payment Service Overview](prism/api-reference/services/recurring-payment-service/README.md)
    - [Charge](prism/api-reference/services/recurring-payment-service/charge.md)
    - [Revoke](prism/api-reference/services/recurring-payment-service/revoke.md)
  - [Refund Service Overview](prism/api-reference/services/refund-service/README.md)
    - [Get](prism/api-reference/services/refund-service/get.md)
  - [Dispute Service Overview](prism/api-reference/services/dispute-service/README.md)
    - [Accept](prism/api-reference/services/dispute-service/accept.md)
    - [Defend](prism/api-reference/services/dispute-service/defend.md)
    - [Get](prism/api-reference/services/dispute-service/get.md)
    - [Submit Evidence](prism/api-reference/services/dispute-service/submit-evidence.md)
  - [Event Service Overview](prism/api-reference/services/event-service/README.md)
    - [Handle](prism/api-reference/services/event-service/handle.md)
  - [Payment Method Service Overview](prism/api-reference/services/payment-method-service/README.md)
    - [Tokenize](prism/api-reference/services/payment-method-service/tokenize.md)
  - [Customer Service Overview](prism/api-reference/services/customer-service/README.md)
    - [Create](prism/api-reference/services/customer-service/create.md)
  - [Payment Method Authentication Service Overview](prism/api-reference/services/payment-method-authentication-service/README.md)
    - [Pre-authenticate](prism/api-reference/services/payment-method-authentication-service/pre-authenticate.md)
    - [Authenticate](prism/api-reference/services/payment-method-authentication-service/authenticate.md)
    - [Post-authenticate](prism/api-reference/services/payment-method-authentication-service/post-authenticate.md)
  - [Merchant Authentication Service Overview](prism/api-reference/services/merchant-authentication-service/README.md)
    - [Create Access Token](prism/api-reference/services/merchant-authentication-service/create-access-token.md)
    - [Create Session Token](prism/api-reference/services/merchant-authentication-service/create-session-token.md)
    - [Create SDK Session Token](prism/api-reference/services/merchant-authentication-service/create-sdk-session-token.md)
  - [Domain Schema](prism/api-reference/domain-schema/README.md)

## SDKs

### Java SDK
- [Java SDK Overview](prism/sdks/java/README.md)

#### Payment Service
- [Payment Service Overview](prism/sdks/java/payment-service/README.md)
- [Create Order](prism/sdks/java/payment-service/create-order.md)
- [Authorize](prism/sdks/java/payment-service/authorize.md)
- [Capture](prism/sdks/java/payment-service/capture.md)
- [Void](prism/sdks/java/payment-service/void.md)
- [Refund](prism/sdks/java/payment-service/refund.md)
- [Get](prism/sdks/java/payment-service/get.md)
- [Reverse](prism/sdks/java/payment-service/reverse.md)
- [Setup Recurring](prism/sdks/java/payment-service/setup-recurring.md)
- [Incremental Authorization](prism/sdks/java/payment-service/incremental-authorization.md)
- [Verify Redirect Response](prism/sdks/java/payment-service/verify-redirect-response.md)

#### Recurring Payment Service
- [Recurring Payment Service Overview](prism/sdks/java/recurring-payment-service/README.md)
- [Charge](prism/sdks/java/recurring-payment-service/charge.md)
- [Revoke](prism/sdks/java/recurring-payment-service/revoke.md)

#### Refund Service
- [Refund Service Overview](prism/sdks/java/refund-service/README.md)
- [Get](prism/sdks/java/refund-service/get.md)

#### Dispute Service
- [Dispute Service Overview](prism/sdks/java/dispute-service/README.md)
- [Accept](prism/sdks/java/dispute-service/accept.md)
- [Defend](prism/sdks/java/dispute-service/defend.md)
- [Get](prism/sdks/java/dispute-service/get.md)
- [Submit Evidence](prism/sdks/java/dispute-service/submit-evidence.md)

#### Event Service
- [Event Service Overview](prism/sdks/java/event-service/README.md)
- [Handle](prism/sdks/java/event-service/handle.md)

#### Payment Method Service
- [Payment Method Service Overview](prism/sdks/java/payment-method-service/README.md)
- [Tokenize](prism/sdks/java/payment-method-service/tokenize.md)

#### Customer Service
- [Customer Service Overview](prism/sdks/java/customer-service/README.md)
- [Create](prism/sdks/java/customer-service/create.md)

#### Payment Method Authentication Service
- [Payment Method Authentication Service Overview](prism/sdks/java/payment-method-authentication-service/README.md)
- [Pre-authenticate](prism/sdks/java/payment-method-authentication-service/pre-authenticate.md)
- [Authenticate](prism/sdks/java/payment-method-authentication-service/authenticate.md)
- [Post-authenticate](prism/sdks/java/payment-method-authentication-service/post-authenticate.md)

#### Merchant Authentication Service
- [Merchant Authentication Service Overview](prism/sdks/java/merchant-authentication-service/README.md)
- [Create Access Token](prism/sdks/java/merchant-authentication-service/create-access-token.md)
- [Create Session Token](prism/sdks/java/merchant-authentication-service/create-session-token.md)
- [Create SDK Session Token](prism/sdks/java/merchant-authentication-service/create-sdk-session-token.md)

#### Payout Service
- [Payout Service Overview](prism/sdks/java/payout-service/README.md)

### Node.js SDK
- [Node.js SDK Overview](prism/sdks/node/README.md)

#### Payment Service
- [Payment Service Overview](prism/sdks/node/payment-service/README.md)
- [Authorize](prism/sdks/node/payment-service/authorize.md)
- [Capture](prism/sdks/node/payment-service/capture.md)
- [Void](prism/sdks/node/payment-service/void.md)
- [Refund](prism/sdks/node/payment-service/refund.md)
- [Get](prism/sdks/node/payment-service/get.md)
- [Reverse](prism/sdks/node/payment-service/reverse.md)
- [Setup Recurring](prism/sdks/node/payment-service/setup-recurring.md)
- [Incremental Authorization](prism/sdks/node/payment-service/incremental-authorization.md)
- [Verify Redirect Response](prism/sdks/node/payment-service/verify-redirect-response.md)

#### Recurring Payment Service
- [Recurring Payment Service Overview](prism/sdks/node/recurring-payment-service/README.md)
- [Charge](prism/sdks/node/recurring-payment-service/charge.md)
- [Revoke](prism/sdks/node/recurring-payment-service/revoke.md)

#### Refund Service
- [Refund Service Overview](prism/sdks/node/refund-service/README.md)
- [Get](prism/sdks/node/refund-service/get.md)

#### Dispute Service
- [Dispute Service Overview](prism/sdks/node/dispute-service/README.md)
- [Accept](prism/sdks/node/dispute-service/accept.md)
- [Defend](prism/sdks/node/dispute-service/defend.md)
- [Get](prism/sdks/node/dispute-service/get.md)
- [Submit Evidence](prism/sdks/node/dispute-service/submit-evidence.md)

#### Event Service
- [Event Service Overview](prism/sdks/node/event-service/README.md)
- [Handle](prism/sdks/node/event-service/handle.md)

#### Payment Method Service
- [Payment Method Service Overview](prism/sdks/node/payment-method-service/README.md)
- [Tokenize](prism/sdks/node/payment-method-service/tokenize.md)

#### Customer Service
- [Customer Service Overview](prism/sdks/node/customer-service/README.md)
- [Create](prism/sdks/node/customer-service/create.md)

#### Payment Method Authentication Service
- [Payment Method Authentication Service Overview](prism/sdks/node/payment-method-authentication-service/README.md)
- [Pre-authenticate](prism/sdks/node/payment-method-authentication-service/pre-authenticate.md)
- [Authenticate](prism/sdks/node/payment-method-authentication-service/authenticate.md)
- [Post-authenticate](prism/sdks/node/payment-method-authentication-service/post-authenticate.md)

#### Merchant Authentication Service
- [Merchant Authentication Service Overview](prism/sdks/node/merchant-authentication-service/README.md)
- [Create Access Token](prism/sdks/node/merchant-authentication-service/create-access-token.md)
- [Create Session Token](prism/sdks/node/merchant-authentication-service/create-session-token.md)
- [Create SDK Session Token](prism/sdks/node/merchant-authentication-service/create-sdk-session-token.md)

#### Payout Service
- [Payout Service Overview](prism/sdks/node/payout-service/README.md)

### Python SDK
- [Python SDK Overview](prism/sdks/python/README.md)

#### Payment Service
- [Payment Service Overview](prism/sdks/python/payment-service/README.md)
- [Create Order](prism/sdks/python/payment-service/create-order.md)
- [Authorize](prism/sdks/python/payment-service/authorize.md)
- [Capture](prism/sdks/python/payment-service/capture.md)
- [Void](prism/sdks/python/payment-service/void.md)
- [Refund](prism/sdks/python/payment-service/refund.md)
- [Get](prism/sdks/python/payment-service/get.md)
- [Reverse](prism/sdks/python/payment-service/reverse.md)
- [Setup Recurring](prism/sdks/python/payment-service/setup-recurring.md)
- [Incremental Authorization](prism/sdks/python/payment-service/incremental-authorization.md)
- [Verify Redirect Response](prism/sdks/python/payment-service/verify-redirect-response.md)

#### Recurring Payment Service
- [Recurring Payment Service Overview](prism/sdks/python/recurring-payment-service/README.md)
- [Charge](prism/sdks/python/recurring-payment-service/charge.md)
- [Revoke](prism/sdks/python/recurring-payment-service/revoke.md)

#### Refund Service
- [Refund Service Overview](prism/sdks/python/refund-service/README.md)
- [Get](prism/sdks/python/refund-service/get.md)

#### Dispute Service
- [Dispute Service Overview](prism/sdks/python/dispute-service/README.md)
- [Accept](prism/sdks/python/dispute-service/accept.md)
- [Defend](prism/sdks/python/dispute-service/defend.md)
- [Get](prism/sdks/python/dispute-service/get.md)
- [Submit Evidence](prism/sdks/python/dispute-service/submit-evidence.md)

#### Event Service
- [Event Service Overview](prism/sdks/python/event-service/README.md)
- [Handle](prism/sdks/python/event-service/handle.md)

#### Payment Method Service
- [Payment Method Service Overview](prism/sdks/python/payment-method-service/README.md)
- [Tokenize](prism/sdks/python/payment-method-service/tokenize.md)

#### Customer Service
- [Customer Service Overview](prism/sdks/python/customer-service/README.md)
- [Create](prism/sdks/python/customer-service/create.md)

#### Payment Method Authentication Service
- [Payment Method Authentication Service Overview](prism/sdks/python/payment-method-authentication-service/README.md)
- [Pre-authenticate](prism/sdks/python/payment-method-authentication-service/pre-authenticate.md)
- [Authenticate](prism/sdks/python/payment-method-authentication-service/authenticate.md)
- [Post-authenticate](prism/sdks/python/payment-method-authentication-service/post-authenticate.md)

#### Merchant Authentication Service
- [Merchant Authentication Service Overview](prism/sdks/python/merchant-authentication-service/README.md)
- [Create Access Token](prism/sdks/python/merchant-authentication-service/create-access-token.md)
- [Create Session Token](prism/sdks/python/merchant-authentication-service/create-session-token.md)
- [Create SDK Session Token](prism/sdks/python/merchant-authentication-service/create-sdk-session-token.md)

#### Payout Service
- [Payout Service Overview](prism/sdks/python/payout-service/README.md)