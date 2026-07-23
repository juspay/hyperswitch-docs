---
description: >-
  Reference table of client error codes returned by the SDK for graceful error
  handling in your web application.
icon: laptop-slash
layout:
  width: wide
---

# Error Codes

{% hint style="info" icon="circle-exclamation" %}
The following table lists client error codes that the Juspay Hyperswitch SDK returns to your website for graceful handling.
{% endhint %}

| Error Type               | Error Message                                   |
| ------------------------ | ----------------------------------------------- |
| `invalid_request_error`  | Invalid api key                                 |
| `invalid_request_error`  | Invalid value for < parameter\_name >           |
| `invalid_request_error`  | Missing required parameter: < parameter\_name > |
| `invalid_request_error`  | Invalid client secret                           |
| `invalid_request_error`  | Invalid promise                                 |
| `processing_error`       | Payment failed with the payment processor       |
| `internal_server_error`  | Server is unavailable                           |
| `object_not_found`       | Payment does not exist                          |
| `confirm_payment_failed` | An unknown error occurred                       |
