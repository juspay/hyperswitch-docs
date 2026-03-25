---
icon: shield-check
description: Implement security controls and compliance measures to protect sensitive payment data and meet PCI DSS
---

# Security and Compliance

## Data Protection & Encryption

Data protection and encryption are critical for a Juspay Hyperswitch production installation to safeguard sensitive information and comply with GDPR and PCI DSS requirements.

It is recommended to ensure that:

- Database storage layer encryption at rest is enabled to secure cardholder data
- TLS 1.2 or higher is enforced for all data in transit
- Data residency requirements of the country of payment processing is adhered to

### Encryption at Rest

All storage layers containing sensitive or transactional data should enforce **encryption at rest**.

Recommended controls include:

- Database storage layer encryption enabled for all persistent data stores
- Encryption applied to backups and database snapshots
- Encryption enabled for object storage used for logs, analytics, or archival data

These measures ensure that stored data remains protected even if underlying storage media is compromised.

### Encryption in Transit

All service-to-service and external communications must enforce secure transport protocols.

Recommended baseline requirements:

- **TLS 1.2 or higher** must be enforced for all data in transit
- Internal service communication should use **secure service endpoints** or **service mesh encryption** where available
- TLS certificates should be issued and rotated automatically using certificate management tools

This ensures confidentiality and integrity of data transmitted between services and external systems.

## Card Vault Isolation

The **Juspay Hyperswitch Card Vault** must be deployed in a **separate compute environment and storage layer** to isolate sensitive cardholder data and encryption keys from the main application infrastructure.

Recommended controls include:

- Separate infrastructure instances
- Dedicated storage volumes
- Independent encryption key management
- Restricted operational access

### Key Custodian Model

Operational access to encryption keys should follow a **key custodian model**, where access to sensitive cryptographic material is restricted to designated security personnel.

This ensures compliance with common payment security frameworks and reduces the risk of unauthorized key access.

## Monitoring & Security Alerts

Continuous monitoring and real-time alerting are critical for detecting unauthorized activity and maintaining operational visibility.

### Centralized Logging and SIEM Integration

Production environments should integrate with a **Security Information and Event Management (SIEM)** platform or centralized logging system to collect and analyze security-relevant events.

Recommended capabilities include:

- Aggregation of application logs, system logs, and infrastructure logs
- Correlation of events across services
- Detection of suspicious activity patterns

### Real-Time Security Alerts

Real-time alerting should be configured for security-sensitive events, including:

- Unauthorized access attempts
- Repeated authentication failures
- Privilege escalation attempts
- Unexpected data access patterns
- Configuration changes affecting security controls

Alerts should integrate with incident management or on-call systems to ensure timely response.

### Log Integrity and Audit Protection

Logs and audit trails must be protected against tampering to ensure reliable forensic investigation.

Recommended practices include:

- Regular **integrity verification** of log data
- Write-once or immutable storage for audit logs
- Restricted access controls for log storage systems

These safeguards help preserve the reliability of security and operational audit records.

### File Integrity Monitoring (FIM)

File Integrity Monitoring should be enabled for critical system components.

FIM solutions track changes to important system files and configuration artifacts, allowing operators to detect unauthorized modifications.

Recommended monitoring targets include:

- System binaries
- Application configuration files
- Security policies
- Authentication and authorization configurations

Unexpected file changes should trigger alerts for security review.

## Access Control & User Management

It is recommended to ensure the following in the merchant's Juspay Hyperswitch production setup:

- Role Based Access Control or least privilege access is enforced for all system users
- MFA is enabled for all administrative access
- Strict access control for production data—only authorized personnel have access

## Penetration Testing Automation

Frequent penetration testing is critical for PCI DSS compliance applications due to its role in identifying vulnerabilities, preventing breaches, and ensuring continuous security.

PCI DSS requires annual penetration tests for all systems in the Cardholder Data Environment (CDE).

To maintain rigor in conducting more frequent penetration tests, it is recommended to automate the penetration test on a weekly basis using tools like Qualys or Nessus to perform scheduled network and application scans, ensuring continuous monitoring.

## Incident Response & Disaster Recovery

To minimize operational disruption and ensure regulatory compliance it is recommended to ensure the below:

- Incident response plans are documented and tested periodically
- Data backup and recovery processes are in place and tested regularly
- Failover and redundancy mechanisms are in place for high availability

## PCI Compliance Audit

Businesses subject to PCI-DSS must annually demonstrate compliance with the regulation. PCI-DSS lays out two ways of doing so:

- **Self-Assessment Questionnaire (SAQ):** This is an audit or assessment which can be completed by a business without an independent third-party Qualified Security Assessor (QSA) or an Internal Security Assessor (ISA). The person responsible for the payment infrastructure fills out the SAQ. This could be the stakeholder who is the closest to your payment infrastructure - your DevOps Manager, or Information Security Officer, or CTO.
- **Report on Compliance (ROC):** An independent third-party QSA or ISA certified by the PCI-SSC will have to perform the audit and share the findings.

Depending on the number of card transactions your business processes, you could be subject to different levels of PCI compliance.

<figure><img src="../.gitbook/assets/unknown (1).png" alt=""><figcaption></figcaption></figure>

Source: [Mastercard guidelines](https://www.mastercard.us/en-us/business/overview/safety-and-security/security-recommendations/site-data-protection-PCI/merchants-need-to-know.html), [Visa Guidelines](https://www.visa.co.in/support/small-business/security-compliance.html), [PCI SSC document library](https://www.pcisecuritystandards.org/document_library/?category=pcidss&hsCtaTracking=8aa4514c-37d0-40bc-b864-ed4c4aebb5de%7C8d5a5e5f-7860-4a8c-97cc-d91f17654660).

For PCI DSS Level 1 compliance the merchant shall engage with a [Third party QSA approved by the PCI council](https://www.pcisecuritystandards.org/assessors_and_solutions/qualified_security_assessors/). The PCI compliance certification shall be done annually, and to produce the SAQ and ROC artefacts.

Comparatively PCI Level 2, Level 3 and Level 4 may be completed with a self assessment.
