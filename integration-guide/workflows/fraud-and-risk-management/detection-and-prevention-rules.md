---
description: >-
  Card testing guard designed to identify suspicious patterns of failed
  transactions and prevent further abuse.
icon: hexagon-minus
---

# Detection and Prevention Rules

### Card <> IP Blocking for Profile

Condition: If a single IP address is used to make X number of unsuccessful payment attempts for a specific profile, the combination of Card <> IP will be blocked for that profile for a specified duration.

Purpose: Fraudsters often use a single IP address while testing multiple stolen card details. By blocking the IP-card combination after multiple failed attempts, we prevent repeated attacks from the same source.

### Card Blocking for Guest Users for Profile

Condition: If a single card is used for X number of unsuccessful payment attempts, then guest user payments for that card will be blocked for that profile for a particular duration.

Purpose: Guest checkouts are frequently targeted for card testing since they do not require user authentication. By restricting guest transactions for a card that has exceeded the failure threshold, we prevent further misuse while allowing logged-in customers to continue using the card.

### Customer ID Blocking for Merchant

Condition: If a single Customer ID reaches X number of unsuccessful payment attempts, that customer ID will be blocked from making any further payments for a specified duration.

Purpose: In cases where fraudsters have access to customer accounts, they might repeatedly test different cards under the same user ID. Blocking the customer ID upon exceeding the failed attempt threshold prevents further fraudulent actions.

### IP-Only Blocking for Profile

Condition: If a single IP address reaches X number of unsuccessful payment attempts (regardless of card number or customer ID), that IP will be blocked for that profile for a specified duration.

Purpose: In guest checkout flows where customer\_id is absent, fraudsters can rotate card numbers from the same IP to bypass Card IP Blocking and Guest User Card Blocking. IP-Only Blocking catches this by tracking all failed attempts from a single IP, preventing card testing attacks even when different cards are used.

Note: This check is applied to all payment attempts, not just guest checkouts.

#### Configurable Parameters

The following parameters can be configured to suit different merchant requirements:

* Threshold of Unsuccessful Payment Attempts: The number of failed transactions allowed before triggering a block.
* Blocking Duration: The period for which a card, IP, or customer ID is blocked.

Rule Enablement per Merchant: Merchants can decide whether they want each rule to be enabled or disabled.
