---
description: Setup custom domains
---

# Setup Custom Domain

A custom domain name can be used for payment links. This is your own domain name which is configured at HyperSwitch side. For doing this, contact us and we will get it configured and give you a TLS certificate.

## How to setup custom domain within your cloud

* Identify your DNS provider

> First, determine which service is handling your DNS records. This will guide you to the correct platform where you can log in and set up the new records.

> Your DNS provider may be the same as your domain registrar, but it's possible they are different entities.

> If you're unsure about your DNS provider, you can search for your domain's nameservers using the following command, replacing "hyperswitch.com" with your own domain:

```shell
$ nslookup -querytype=NS hyperswitch.com
```

> You’ll see a list of name servers for your domain in the output.

* Create required DNS records

> In this segment, you'll generate the necessary DNS records to link your domain. Follow the following steps to enable the same

Step 1: Sign into your DNS provider

> DNS providers offer a control panel where you can log in to manage your DNS settings. Locate your provider’s control panel page and sign in.

Step 2: Locate the page to manage the DNS for your domain

> Now that you've successfully logged in, locate the section within your provider's control panel where you can manage the DNS records for your domain.

Step 3: Create CNAME record

> In your DNS control panel, create a new record that associates your chosen subdomain with 'hyperswitch payment link'. Your DNS provider will typically prompt you to specify the record type, name, value, and TTL (Time To Live) or expiration when adding a new record.

Enter the following values and save the new DNS record.

> \| FIELD | INSTRUCTIONS | DESCRIPTION | |----------|----------|----------| | Type | Select `CNAME` from the dropdown | What kind of DNS record this is. | | Name | if your custom domain is `paymentlink.xyz.com`, enter `paymentlink`| For CNAME records, this field is the first part of your subdomain (the part leading up to the first period).| | Value |Enter `sandbox.hyperswitch.io` | This is what the new subdomain record points to–in this case, Hyperswitch .Some providers may expect a trailing period (.) after the CNAME value. Make sure to verify that your CNAME value matches the format your provider expects. | | TTL/Expiry | Enter `300` | An expiration of 5 minutes (300 seconds) is OK. Your DNS provider might not allow you to change the TTL value. If this field is missing or you can’t change it, it’s safe to ignore this part of the configuration. |

Step 4: Create your TXT record

> Navigate to your DNS control panel and proceed to add a new TXT record.

> > This TXT record is essential for domain ownership verification. It's a necessary step to obtain TLS certificates for your domain, ensuring secure payment processing.

> Enter these values and save the new DNS record:

> \| FIELD | INSTRUCTIONS | DESCRIPTION | |----------|----------|----------| | Type | Select `TXT` from the dropdown | What kind of DNS record this is. | | Name | If your custom domain is `paymentlink.xyz.com`, enter \_acme-challenge.paymentlink| For TXT records, this field is the subdomain portion of your domain. | | Value | Copy the TXT value that is given by us and paste | This is a long, unique string used for domain verification | | TTL/Expiry | Enter `300` | An expiration of 5 minutes (300 seconds) is OK. Your DNS provider might not allow you to change the TTL value. If this field is missing or you can’t change it, it’s safe to ignore this part of the configuration.|

Step 5. Verify your CNAME record setup

> After you save your DNS record, verify that it has the correct values.

> > Please allow up to 10 minutes for your DNS provider to update its name servers. Replace "pay.xyz.com" with your custom domain in the command below, and then run it in your terminal:

```shell
$ nslookup -querytype=CNAME paymentlink.xyz.com
```

your should get a output like this

```shell
<your subdomain> 	canonical name = sandbox.hyperswitch.io.
```

Once you observe the output, proceed to the next step.

Step 6. Verify your TXT record

> After you save your DNS record, verify that it has the correct values.

> > Please allow up to 10 minutes for your DNS provider to update its nameservers. Replace pay.xyz.com with your custom domain in the following command and run it from your terminal:

```shell
$ nslookup -querytype=TXT _acme-challenge.paymentlink
```

your should get a output like this

```shell
_acme-challenge.<your domain>   text = "<your unique TXT record value>"
```

> If you don't observe your unique TXT record value in the output, please wait a little longer and then attempt running the command again.

> Upon completing this step, your DNS records will be configured.

* Now that you've established and verified your DNS records, Hyperswitch proceeds to verify the connection and provision your domain on our end. You will receive an email from us once the domain is ready for you to enable it.

## How to use Wallets like Apple Pay & Google Pay in Payment Links?

To enable wallet flows such as Apple Pay or Google Pay for payment links, domain validation from Apple or Google is required respectively to obtain session tokens. This validation can be facilitated by utilizing the custom domain feature available for payment links, which can be configured at the business profile level.

After you have setup custom domain in your cloud, you need to get respective Google pay, Apple pay certificate for your new domain, and register the same in our dashboard.
