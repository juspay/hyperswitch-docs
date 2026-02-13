---
icon: at
---

# SMTP Server Integration

Previously, **Hyperswitch** relied solely on **AWS SES** for sending emails during signup and login flows. As we grew, many merchants requested support for **other email service providers** to better align with their existing infrastructure.

Thus we upgraded Hyperswitch's email service to allow pluggable support for **any SMTP-compliant email service provider**, offering merchants greater flexibility.

### Configuration

The configuration can be found in the following file:

```
hyperswitch/config/docker_compose.toml
```

For SMTP-based email sending, update the `[email.smtp]` section as shown:

```toml
# Configuration for smtp, applicable when the active email client is SMTP
[email.smtp]
host = "mailhog"          # SMTP host (e.g., smtp.gmail.com)
port = 1025               # SMTP port (e.g., 25, 587)
timeout = 10              # Timeout for SMTP connection in seconds
connection = "plaintext"  # Supported values: "plaintext", "starttls"
```

#### Details

* **host**: SMTP server hostname used to send emails.\
  &#xNAN;_&#x45;xample_: `"smtp.gmail.com"` or `"mailhog"` for local testing
* **port**: Port on which the SMTP server is listening.\
  &#xNAN;_&#x45;xample_: `587` (for STARTTLS), `25`, or `1025` (for MailHog)
* **timeout**: Maximum time (in seconds) to wait while connecting to the SMTP server.\
  &#xNAN;_&#x45;xample_: `10`
* **connection**: Type of SMTP connection.\
  &#xNAN;_&#x45;xample_: `"starttls"` (recommended) or `"plaintext"` (insecure; for development only)

### How does it work?

The email client is designed to work with standard SMTP servers by implementing the `EmailClient` trait for an internal `SmtpServer` struct.

**Key Points of the Implementation**

* **Config Validation:** Ensures required fields like `host`, and credentials (if provided) are not empty.
* **Connection Modes:** Supports both `StartTls` (recommended) and `Plaintext` (insecure) connections.
* **Dynamic Client Creation:** A new SMTP client is created every time an email is sent. This allows for up-to-date configuration without persistent connections.
* **Secure Credential Handling:** Username and password are wrapped in secure types to protect sensitive data.
* **Email Formatting:** Converts plain strings into `lettre::Message` objects with proper headers and HTML content type.
* **Error Handling:** Provides granular error types to indicate issues during email construction, parsing, or sending.

This modular design ensures that merchants can plug in their preferred SMTP service provider without changing application logic.

{% hint style="info" %}
If you face any issues, feel free to reach out to us on [Slack](https://inviter.co/hyperswitch-slack)
{% endhint %}
