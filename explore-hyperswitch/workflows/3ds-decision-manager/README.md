---
icon: badge-check
---

# 3DS / Strong Customer Authentication

3D Secure (3DS) is an authentication protocol that adds an extra layer of protection to card transactions. It helps confirm that the person making the purchase is the legitimate cardholder, reducing the risk of fraud for both businesses and customers. When 3DS is triggered, the issuing bank may prompt the cardholder to authenticate using methods such as a password, a one-time code sent to their mobile device, or biometric verification. Many customers recognize this experience through familiar card network brands like Visa Secure, Mastercard Identity Check, or American Express SafeKey.

Strong Customer Authentication (SCA), introduced under PSD2 in the European Economic Area and reflected in similar regulations in the UK, India, Japan, and Australia, may require the use of 3DS for certain card payments. In other regions, 3DS remains optional but can still be used strategically to help reduce fraud.

<table data-view="cards"><thead><tr><th align="center"></th><th align="center"></th></tr></thead><tbody><tr><td align="center"><a href="authenticate-with-3d-secure-via-psp.md">Authenticate with 3D Secure via PSP</a></td><td align="center">Perform 3D Secure (3DS) via the PSP that is processing the transaction</td></tr><tr><td align="center"><a href="external-authentication-for-3ds.md">Standalone 3D Secure <br>(via Hyperswitch)</a></td><td align="center">Run 3D Secure (3DS) via any 3DS server (Juspay, Netcetra, 3DSecure.io) while processing the subsequent payment on a third party gateway </td></tr><tr><td align="center"><a href="import-3d-secure-results.md">Import 3D Secure results</a></td><td align="center">Process payments via Hyperswitch when 3DS Secure (3DS) runs outside Hyperswitch </td></tr><tr><td align="center"><a href="3ds-intelligence-engine/">3D secure Intelligence Engine</a></td><td align="center">Use Rules and SCA exemptions to reduce cardholder friction on eligible transactions</td></tr></tbody></table>
