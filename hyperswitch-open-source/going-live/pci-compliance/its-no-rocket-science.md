---
description: Demystifying PCI compliance and it's requirements
---

# 🍰 It's no rocket science

{% hint style="info" %}
In this chapter, we will look at the levels of PCI compliance, key requirements and we will understand why it is not as complex as it seems to be to obtain PCI compliance.
{% endhint %}

{% embed url="https://youtu.be/dBl3vNX3zXE" %}

Businesses subject to PCI-DSS must annually demonstrate compliance with the regulation. And PCI-DSS lays out two ways of doing so:

1. **Self-Assessment Questionnaire (SAQ):** This is an audit or assessment which can be completed by a business without a independent third-party Qualified Security Assessor (QSA) or an Internal Security Assessor (ISA). The person responsible for the payment infrastructure fills out the SAQ. This could be the stakeholder who is the closest to your payment infrastructure - your Dev Ops Manager, or Information Security Officer, or CTO.&#x20;
2. **Report on Compliance (ROC):** An independent third-party QSA or ISA certified by the PCI-SSC will have to perform the audit and share the findings.

{% hint style="success" %}
Companies that fall into PCI DSS Levels 2-4 are only required to complete a Self-Assessment Questionnaire (SAQ) and submit to the respective payment processor or acquirer. And that would be all !!
{% endhint %}

## Level of PCI compliance

Depending on the number of transactions your business processes, you could be subject to different levels of PCI compliance.

<table><thead><tr><th width="186">Parameter</th><th width="144">PCI Level 1</th><th width="142">PCI Level 2</th><th width="138">PCI Level 3</th><th>PCI Level 4</th></tr></thead><tbody><tr><td>Number of card transactions</td><td>Over 6 million</td><td>6 million to 1 million</td><td>1 million to 20,000</td><td>Less than 20,000</td></tr><tr><td>Compliance Report</td><td>Report on Compliance (ROC)</td><td>Self Assessment Questionnaire (SAQ)</td><td>Self Assessment Questionnaire (SAQ)</td><td>Self Assessment Questionnaire (SAQ)</td></tr><tr><td>Assessment type</td><td>Independent QSA or ISA</td><td>Self assessment</td><td>Self assessment</td><td>Self assessment</td></tr><tr><td>Quarterly network scan by approve QSA</td><td>Applicable</td><td>Applicable</td><td>Applicable</td><td>Applicable</td></tr></tbody></table>

_Sources:_ [_Mastercard guidelines_](https://www.mastercard.us/en-us/business/overview/safety-and-security/security-recommendations/site-data-protection-PCI/merchants-need-to-know.html)_,_ [_Visa Guidelines_](https://www.visa.co.in/support/small-business/security-compliance.html)_,_ [_PCI SSC document library_](https://www.pcisecuritystandards.org/document\_library/?category=pcidss\&hsCtaTracking=8aa4514c-37d0-40bc-b864-ed4c4aebb5de%7C8d5a5e5f-7860-4a8c-97cc-d91f17654660)_._&#x20;

## About PCI Requirements and Controls

In general PCI compliance is consolidated into 12 Requirements and 224 controls.

<table><thead><tr><th width="558">Requirements</th><th>Number of Controls</th></tr></thead><tbody><tr><td><strong>Requirement 1:</strong> Install and maintain a firewall configuration to protect cardholder data</td><td>20</td></tr><tr><td><strong>Requirement 2:</strong> Do not use vendor-supplied defaults for system passwords and other security parameters</td><td>12</td></tr><tr><td><strong>Requirement 3:</strong> Protect stored cardholder data</td><td>20</td></tr><tr><td><strong>Requirement 4:</strong> Encrypt transmission of cardholder data across open, public networks</td><td>4</td></tr><tr><td><strong>Requirement 5:</strong> Use and regularly update anti-virus software or programs</td><td>6</td></tr><tr><td><strong>Requirement 6:</strong> Develop and maintain secure systems and applications</td><td>28</td></tr><tr><td><strong>Requirement 7:</strong> Restrict access to cardholder data by business need to know</td><td>8</td></tr><tr><td><strong>Requirement 8:</strong> Assign a unique ID to each person with computer access</td><td>22</td></tr><tr><td><strong>Requirement 9:</strong> Restrict physical access to cardholder data</td><td>22</td></tr><tr><td><strong>Requirement 10:</strong> Track and monitor all access to network resources and cardholder data</td><td>28</td></tr><tr><td><strong>Requirement 11:</strong> Regularly test security systems and processes</td><td>16</td></tr><tr><td><strong>Requirement 12:</strong> Maintain a policy that addresses information security for all personnel</td><td>38</td></tr><tr><td><strong>Total</strong></td><td>224</td></tr></tbody></table>

## Simplifying your PCI compliance

### Self assess your business for PCI compliance

If you are an online business processing less than 6 million card transactions a month, all that you will have to do is a self assessment of PCI compliance as per [SAQ D](https://listings.pcisecuritystandards.org/documents/SAQ\_D\_v3\_Merchant.pdf).

### Requirement 9

Lets assume all your software systems are cloud native and do not depend upon on-premise servers. In such case your staff will not be able to physically access any cardholder data and hence your business is exempted from Requirement 9.

That is one PCI Requirement less for your business and 22 controls automatically exempted.

### Requirement 3

If you choose not to store card holder data on your servers, you will be exmepted from Requirement 3.

So eventually you are left with 10 PCI Requirements and 182 controls to comply with.&#x20;

{% hint style="info" %}
This is the reason behind our recommendation of installing a simple setup without the card vault, if your business processes less than 6 million card transactions
{% endhint %}

## Next step:

{% content-ref url="completing-the-saq.md" %}
[completing-the-saq.md](completing-the-saq.md)
{% endcontent-ref %}
