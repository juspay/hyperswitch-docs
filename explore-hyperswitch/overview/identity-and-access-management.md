---
icon: id-card-clip
---

# Identity and Access Management

Identity and Access Management (IAM) in Hyperswitch is designed to provide a secure, user-friendly, and well-regulated environment. By implementing best practices for authentication and access control, Hyperswitch ensures data confidentiality, operational efficiency, and compliance with global standards.

### Authentication Methodology for Hyperswitch APIs

**1. Admin Services Authentication**

Administrative services require robust, multi-layered authentication. Access is limited to specific personnel within the Hyperswitch team via an additional API key to maintain backend security.

**2. Merchant Authentication**

Merchants accessing Hyperswitch APIs benefit from strong authentication mechanisms to safeguard their accounts and transactions. For detailed guidance on merchant authentication, refer to the API documentation​​.

**3. Vault Authentication**

The Hyperswitch Vault employs a distributed key management approach. Key custodians must collaborate to initiate the application, ensuring no single individual can independently alter or access the vault. This design prevents unauthorized tampering and enhances the overall security framework​​.

### Identity and Access Management in AWS

**1. User Authentication**

Hyperswitch employs Multi-Factor Authentication (MFA) in conjunction with network and device whitelisting to ensure secure user access.

**2. Access Controls and Role-Based Access Control (RBAC)**

* **Granular Permissions:** Administrative roles are clearly defined with specific permissions, ensuring users only access functionalities necessary for their roles.
* **Distributed Access Model:** Hyperswitch employs a distributed model where no individual has complete control over administrative operations.
* **Principle of Least Privilege:** Permissions are restricted to essential tasks to mitigate unauthorized access risks.

### Benefits of Hyperswitch IAM

1. **Enhanced Security:** Multi-layered authentication, key management, and RBAC reduce vulnerabilities.
2. **Operational Efficiency:** Clear role definitions and access models ensure streamlined workflows.
3. **Compliance Assurance:** Meets global regulatory requirements, including PCI DSS and ISO 27001 standards​​.
4. **User Trust:** By minimizing risks and safeguarding data, Hyperswitch fosters confidence among merchants and partners.
