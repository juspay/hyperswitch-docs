---
description: Learn to configure Cybersource to enhance your payment processing capabilities.
---
# CyberSource

<!--
This file is auto-generated. Do not edit by hand.
Source: data/field_probe/cybersource.json
Regenerate: python3 scripts/generate-connector-docs.py cybersource
-->

## Implemented Flows

| Flow (Service.RPC) | Category | gRPC Request Message |
|--------------------|----------|----------------------|
| [PaymentService.Authorize](#paymentserviceauthorize) | Payments | `PaymentServiceAuthorizeRequest` |
| [PaymentService.Capture](#paymentservicecapture) | Payments | `PaymentServiceCaptureRequest` |
| [PaymentService.Get](#paymentserviceget) | Payments | `PaymentServiceGetRequest` |
| [RecurringPaymentService.Charge](#recurringpaymentservicecharge) | Mandates | `RecurringPaymentServiceChargeRequest` |
| [PaymentService.Refund](#paymentservicerefund) | Payments | `PaymentServiceRefundRequest` |
| [PaymentService.SetupRecurring](#paymentservicesetuprecurring) | Payments | `PaymentServiceSetupRecurringRequest` |
| [PaymentService.Void](#paymentservicevoid) | Payments | `PaymentServiceVoidRequest` |

## Flow Details

### Payments

#### PaymentService.Authorize

Authorize a payment amount on a payment method. This reserves funds without capturing them, essential for verifying availability before finalizing.

| | Message |
|---|---|---------|
| Request | `PaymentServiceAuthorizeRequest` |
| Response | `PaymentServiceAuthorizeResponse` |

##### Request Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `payment_method_data` | `PaymentMethodData` | ✅ | Payment method details (card, wallet, bank transfer, etc.) |
| `connector_auth` | `ConnectorAuth` | ✅ | Authentication credentials specific to the connector |
| `capture_method` | `CaptureMethod` | ✅ | When to capture funds (Automatic, Manual, Scheduled) |

##### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `status` | `Status` | Current payment status (Succeeded, Failed, Pending, Cancelled) |
| `connector_transaction_id` | `String` | Transaction identifier from the connector |
| `payment_method_data` | `PaymentMethodData` | Payment method details used/returned |

#### PaymentService.Capture

Capture funds from a previously authorized payment. This completes the transaction and transfers funds to your account.

| | Message |
|---|---------|
| Request | `PaymentServiceCaptureRequest` |
| Response | `PaymentServiceCaptureResponse` |

##### Request Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `connector_transaction_id` | `String` | ✅ | The transaction ID from the original authorization |
| `amount` | `Amount` | ✅ | Amount to capture (can be partial) |

##### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `status` | `Status` | Current capture status |
| `connector_capture_id` | `String` | Capture identifier from the connector |

#### PaymentService.Get

Retrieve the current status and details of a payment.

| | Message |
|---|---------|
| Request | `PaymentServiceGetRequest` |
| Response | `PaymentServiceGetResponse` |

##### Request Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `connector_transaction_id` | `String` | ✅ | Transaction ID from the connector |

##### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `status` | `Status` | Current payment status |
| `amount` | `Amount` | Payment amount details |
| `payment_method_data` | `PaymentMethodData` | Payment method information |

#### PaymentService.Refund

Return funds to a customer for a completed payment (full or partial).

| | Message |
|---|---------|
| Request | `PaymentServiceRefundRequest` |
| Response | `PaymentServiceRefundResponse` |

##### Request Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `connector_transaction_id` | `String` | ✅ | Original transaction ID |
| `amount` | `Amount` | ✅ | Refund amount (can be partial) |
| `reason` | `String` | | Reason for refund |

##### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `status` | `Status` | Refund status |
| `connector_refund_id` | `String` | Refund identifier from connector |

#### PaymentService.SetupRecurring

Create a mandate/recurring payment authorization for future charges without customer intervention.

| | Message |
|---|---------|
| Request | `PaymentServiceSetupRecurringRequest` |
| Response | `PaymentServiceSetupRecurringResponse` |

##### Request Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `payment_method_data` | `PaymentMethodData` | ✅ | Payment method to store |
| `connector_auth` | `ConnectorAuth` | ✅ | Authentication credentials |
| `mandate_type` | `MandateType` | ✅ | Single-use or multi-use mandate |

##### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `status` | `Status` | Setup status |
| `mandate_id` | `String` | Mandate identifier for future charges |

#### PaymentService.Void

Cancel an authorized payment that hasn't been captured yet.

| | Message |
|---|---------|
| Request | `PaymentServiceVoidRequest` |
| Response | `PaymentServiceVoidResponse` |

##### Request Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `connector_transaction_id` | `String` | ✅ | Transaction ID to void |
| `reason` | `String` | | Reason for voiding |

##### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `status` | `Status` | Void status |

### Mandates

#### RecurringPaymentService.Charge

Charge a stored payment method using an existing mandate.

| | Message |
|---|---------|
| Request | `RecurringPaymentServiceChargeRequest` |
| Response | `RecurringPaymentServiceChargeResponse` |

##### Request Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `mandate_id` | `String` | ✅ | Mandate ID from setup |
| `amount` | `Amount` | ✅ | Amount to charge |
| `connector_auth` | `ConnectorAuth` | ✅ | Authentication credentials |

##### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `status` | `Status` | Charge status |
| `connector_transaction_id` | `String` | New transaction ID |

## Authentication

Cybersource requires specific authentication credentials:

```json
{
  "api_key": "your_api_key",
  "api_secret": "your_api_secret",
  "merchant_id": "your_merchant_id"
}
```

## Configuration

```rust
use connector_service::ConnectorConfig;

let config = ConnectorConfig {
    connector: Connector::Cybersource,
    auth: CybersourceAuth {
        api_key: "key".to_string(),
        api_secret: "secret".to_string(),
        merchant_id: "merchant".to_string(),
    },
    sandbox: false,
};
```

## Error Handling

Cybersource uses standard HTTP status codes and returns detailed error messages:

| Status Code | Meaning |
|-------------|---------|
| 200 | Success |
| 400 | Bad Request - Invalid parameters |
| 401 | Unauthorized - Authentication failed |
| 402 | Payment Required - Transaction declined |
| 404 | Not Found - Resource doesn't exist |
| 500 | Server Error - Cybersource internal error |

## Webhooks

Cybersource supports webhooks for real-time event notifications:

| Event Type | Description |
|------------|-------------|
| `payment.authorize` | Authorization completed |
| `payment.capture` | Capture completed |
| `payment.refund` | Refund processed |
| `payment.void` | Payment voided |

Configure webhook endpoints in your Cybersource merchant dashboard.

## Testing

### Sandbox Environment

Use Cybersource's sandbox environment for testing:

```rust
let config = ConnectorConfig {
    sandbox: true,
    // ... other config
};
```

### Test Cards

| Card Number | Type | Result |
|-------------|------|--------|
| 4111111111111111 | Visa | Success |
| 4000000000000002 | Visa | Decline |
| 5555555555554444 | Mastercard | Success |

## Additional Resources

- [Cybersource API Documentation](https://developer.cybersource.com/)
- [Cybersource Testing Guide](https://developer.cybersource.com/hello-world/testing-guide.html)
- [Connector Service SDK](/connector-service/sdks/)

## Support

For issues or questions:
- [GitHub Issues](https://github.com/juspay/hyperswitch/issues)
- [Discord Community](https://discord.gg/hyperswitch)
