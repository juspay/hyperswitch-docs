---
description: Payment Links & Theme Customization Guide
---

# Payment Links & Theme Customization Guide

## **1. Understanding Style IDs**

Style IDs are design templates for your payment links, allowing you to create different themes for different purposes - separate looks for your premium brand, holiday sales, or regional markets.

**What you can customize in each theme:**
- Your brand's visual identity (colors, logos, backgrounds, button styles)
- Custom messaging and terms & conditions
- Display preferences (how forms behave)
- Language preferences (we support 19+ languages including English, Hebrew, Arabic, Japanese, German, Spanish, Chinese, and more!)

**How it works:** When creating a payment link, simply specify which style ID you want to use (via the `payment_link_config_id` parameter), and your customers will see that themed experience.

**Examples of Style IDs you might create:**
- `brand-default` - Your main brand theme
- `brand-premium` - Elevated experience for premium customers
- `holiday-2024` - Special theme for seasonal promotions

---

## **2. Smart Text Handling**

**The system works intelligently by default:**

Out of the box, the payment link automatically:
- Adapts text based on the purpose of the payment link (payment, authorization, or payment method storage)
- Changes button text to match the transaction type
- Translates everything into your customer's language automatically (across 19+ languages!)

**Important consideration when customizing text:**

If you decide to write your own custom text for terms and conditions, here's what changes:
- 💡 The system will use your exact text across all scenarios
- 🌍 Automatic translations stop working - you'll need to provide translations for each language you support
- 📝 Automatic text inference is lost since a single text is configured for all transaction types

**If you do customize text, here's a pro tip:**

Write in a way that works for any scenario your customers might encounter:

- ❌ **Don't say:** "By clicking Pay Now, you authorize..." (too specific - button might say something different!)
- ✅ **Instead say:** "By submitting your payment information, you authorize..."
- ✅ **Or even better:** "By completing this form, you authorize..."

**Universal example that works everywhere:**
```
"By submitting your payment information, you authorize [Your Business Name] to 
charge your payment method or store your payment details as applicable."
```

This works whether your customer is paying now, setting up a subscription, or just saving their card!

---

## **3. Choosing Your Approach**

You have two ways to set up your payment link themes:

**Option A: Keep It Simple**
- Use one universal theme with messaging that works for everything
- Easier to manage and maintain
- Consistent brand experience for all customers
- Recommended for streamlined operations

**Option B: Get Specific for Each Flow**
- Create different themes for different purposes:
  - `payment-flow-theme` - For regular purchases
  - `authorization-flow-theme` - For payment verification
  - `storage-flow-theme` - For saving payment methods
- Use precise messaging for each scenario (like "By clicking 'Pay Now'..." for actual payments)
- When creating a payment link, choose which theme fits that transaction
- **What to know:** More control and precision, but more themes to keep updated

**When specialized themes make sense:**
- You want different experiences for different flows (like a simpler look for quick payments vs detailed for subscriptions)
- You're optimizing conversion rates and want to test different approaches
- You have the resources to maintain multiple themes

---

## **4. Real-World Use Cases**

**Running multiple brands?**
Create a style ID for each brand (like `brand-a-default`, `brand-b-default`). When you create a payment link, just specify which brand's theme to use. Each brand keeps its own look and feel!

**Operating in different regions?**
Set up region-specific themes (`us-theme`, `eu-theme`, `apac-theme`) with appropriate languages, currency displays, and localized messaging. Route your customers to the right theme based on where they are.

**Planning a seasonal promotion?**
Create a special campaign theme (`holiday-2024`, `summer-sale`) that you can easily turn on for promotional periods and turn off when the campaign ends.

---

## **5. Handling Different Transaction Types**

**Zero-dollar authorizations (like verifying a card without charging):**

Use messaging that covers both charging AND just storing:
```
"By submitting your payment information, you authorize [Your Business Name] to 
charge your payment method or store your payment details as applicable."
```

This works whether you're charging now or just verifying the card!

**Saving payment methods for later:**
- Stick with universal language that focuses on permission
- Avoid mentioning specific amounts
- Focus on the authorization to store their credentials

**Setting up subscriptions:**
- Your messaging should cover both storing the payment method AND future charges
- Example: "...to charge your payment method or store your payment details as applicable"
- This way, customers understand they're authorizing both setup and future billing

---
