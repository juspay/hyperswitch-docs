---
description: >-
  Reference table of client error codes returned by the SDK for graceful error
  handling in your web application.
icon: ban
metaLinks:
  alternates:
    - error-codes.md
---

# Error Codes

The following table lists client error codes that the Juspay Hyperswitch SDK returns to your website for graceful handling.

| Error Type               | Error Message                                   |
| ------------------------ | ----------------------------------------------- |
| invalid\_request\_error  | Invalid api key                                 |
| invalid\_request\_error  | Invalid value for < parameter\_name >           |
| invalid\_request\_error  | Missing required parameter: < parameter\_name > |
| invalid\_request\_error  | Invalid client secret                           |
| invalid\_request\_error  | Invalid promise                                 |
| processing\_error        | Payment failed with the payment processor       |
| internal\_server\_error  | Server is unavailable                           |
| object\_not\_found       | Payment does not exist                          |
| confirm\_payment\_failed | An unknown error occurred                       |
