---
icon: credit-card
---

# Co-badged Cards

Co-badged cards are credit or debit cards issued by banks that integrate two or more payment networks. These cards carry the logos of both a local network (e.g., MADA, CB, Dankort, eftpos) and a global network (e.g., Visa, Mastercard).&#x20;

Customers benefit from the global scope, security, and consumer protection of international networks while enjoying local perks, such as better discounts and lower fees. Co-badged cards enhance payment flexibility, especially in markets with strong local payment networks.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXf95RQ8eKXXo3IQI0TuK5Rcn_kiRM4u0VNdukMAFxleLIODje5FLFkO-SO2dK6EPtkNfhy8VYvFTt-NxGRB3RapqCqjyKs5mpFdYOZwsJELpUIGiDK9Kj4GXiId_macNX6_KntcIpzlBiV436h6q2Lo6xsT?key=cqdjEpZuvzmudtMKqZ5fuw" alt=""><figcaption></figcaption></figure>

## What’s in it for Your Business:

* **Increased Payment Flexibility**: Merchants can offer customers the ability to select their preferred network, optimizing the payment experience and accommodating different payment preferences.
* **Better Dispute Resolution**: In many cases, for high-value items, global networks like Visa and Mastercard provide better consumer protection and dispute resolution. Customers can choose these for international transactions, while using local networks for domestic purchases.
* **Compliance with Global Standards**: Co-badged cards support local regulations, such as Article 8 of the [Interchange Fee Regulation](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32015R0751) (IFR) issued by the European Union, ensuring full compliance while maintaining flexibility for merchants outside the EEA.
* **Cost Optimization**: The platform's debit routing engine automatically selects the most cost-effective network based on real-time data and merchant preferences.

## How to enable support for Co-badged cards with Hyperswitch?

Co-badged card support is **automatically enabled** when you configure multiple card networks in your business profile. The system will:

1. Automatically detect co-badged cards during payment processing
2. Apply intelligent routing based on your configured preferences
3. Maintain compliance with applicable regulations
4. Provide detailed network information in payment responses

No additional configuration is required beyond selecting the card networks you support during payment processor setup.

### FAQs

#### Are co-badged cards the same as co-branded cards?&#x20;

No. Co-badged cards feature multiple networks (e.g., Visa and Cartes Bancaires), allowing customers to choose the network for transactions. Co-branded cards are a partnership between a merchant and a network, offering perks specific to the merchant’s store.

#### Can the merchant choose the network for co-badged cards?&#x20;

In the IFR, Article 8 mandates that customers must be free to choose their network. In non-EEA regions, merchants can set default network preferences or automatically route transactions based on cost and success rates.

#### What if the merchant doesn’t support one of the networks on the co-badged card?&#x20;

Merchants can choose not to support one of the networks, and in such cases, transactions will be routed through the supported network.

{% content-ref url="tokenization-and-saved-cards/mandates-and-recurring-payments.md" %}
[mandates-and-recurring-payments.md](tokenization-and-saved-cards/mandates-and-recurring-payments.md)
{% endcontent-ref %}
