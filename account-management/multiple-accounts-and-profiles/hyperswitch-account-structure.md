---
icon: people-roof
---

# Organization, Merchant and Profile Setup

Adapting the right account structure while setting up Hyperswitch for your business is one of the most crucial steps. Hyperswitch allows you to choose different account structures based on your business needs-

* Whether you are a business with multiple product lines and business units within each line, or a marketplace with multiple sub-merchants, each having multiple business units.
* Whether you want to accept payments at the business level, business unit level, or allow your sub-merchants to accept payments on their own.

You can manage it all via Hyperswitch.

This is enabled by Hyperswitch’s three-level user hierarchy: **Organization, Merchant Account, and Profile**, enabling businesses to configure and optimize payment flows while maintaining visibility across all merchants, sub-merchants, and business units.

<figure><img src="../../../.gitbook/assets/Screenshot 2024-10-21 at 5.59.19 PM.png" alt="" width="563"><figcaption></figcaption></figure>

Once a user signs up on the Hyperswitch Control Centre, they need to create an organization. By default, one merchant account and one profile are created for the organization, and the user is assigned the role of organization Admin. They can further invite team members on the basis of the applicable roles.

## Features Useful for Your Business:

*   **Multiple Merchant Accounts:** Organization admins can create and manage multiple merchant accounts under one organization for different business lines or sub-merchants, with each merchant account having its own API keys.

    <figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXfkpJiCObIbDBPVtIEGznJLWwbGChBFpdKt3HR3MhNEArehioKVZi5AXTAsPyxqba-Xo3FNQ2ySdc3XoU7sk6khd51MGJILUqwmpT1anTTnfxrem9zfj1XZ4j0A3IVEbbX6pQWsjNDcTwSx8A3YlAztohQ?key=KjIGF7_A-nGwRp3B4LA6NQ" alt=""><figcaption></figcaption></figure>
*   **Multiple Profiles under each Merchant:** A merchant account can set up multiple profiles for each individual business unit. Profiles are the most granular levels in Hyperswitch, and every payment via Hyperswitch is mandatorily and exclusively tagged with a profile.

    <figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXf-aR3KdLup56nCK71gZeOJMZ4o4AqE1lcN4iZ0C1MyqmstN2Hns4C_nudITry6ic4hA36P8qquQmCdK98z8Mxd7PQysxYhtfFFcRBkY3w_Pq0e2lttOMq4iLNGK-veOfvxccjGeupzEoV_H5rDb4CkismV?key=KjIGF7_A-nGwRp3B4LA6NQ" alt=""><figcaption></figcaption></figure>
* **Easy Checkout for Return Customers:** Hyperswitch allows an organization to store customer cards while enabling sub-merchants to access them, and for payments handled by a merchant, only the cards relevant to that merchant are visible.&#x20;
  * Additionally, payments can be tokenized (both network and PSP) at the sub-merchant level, ensuring that sub-merchants or platforms don't need to worry about PCI compliance.
  * Hyperswitch also enables organizations to accept payments on behalf of their sub-merchant using one of profiles of sub-merchant, without allowing the organization to access the connector credentials used with the profile.
*   **Routing & Connectors Configuration:** If a business has connector credentials for each of its business units, they can configure them to  their respective profiles and set up routing rules for each profile.&#x20;

    * If the merchant wants to accept payments at the merchant level with its own set of connector credentials, it can create another profile and configure its connectors with that profile.

    <figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXcivUqB263o28dMqZCfxKiWkNnJUJOnbIi9Ri4L3qhOXwf6BF3wXnVwNCIISlqXM4Kwx363sB09zrDKJEYMJ8T6CsV-d2kvvc7WAxLulChyGxYtduwgra4H7MttVWjHV6iI8YhhB8E0hf69HiRGV9lZ2wTw?key=KjIGF7_A-nGwRp3B4LA6NQ" alt=""><figcaption><p>Kindly note the Profile name and Routing name to identify the difference</p></figcaption></figure>

    <figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXeNBK4CDEvBeUV-Bo6lRKHzVCDKFSHnPWW-NaXjifjXFww3ADzbILjX-YoCGpErEL8UpgJA0Rq4ID0hAgf1WT3asLnlXG8Cse9paisbmUa63vnT8QxPq-wVD-qs8e5vVi1OW1WqYKPKalJ5HeJ6RPQh4bg?key=KjIGF7_A-nGwRp3B4LA6NQ" alt=""><figcaption><p>Kindly note the Profile name and Routing name to identify the difference</p></figcaption></figure>
*   **Exhaustive Data Visibility:** Payment lists, analytics, and teams are segregated at the profile, merchant, and organization levels. Hyperswitch allows top-down access to data; each level can access the payments data of the levels below it by switching into their levels, not vice versa.&#x20;

    * Each level can get an aggregated view of the payment transactions of all the sub-levels beneath it. Also, Using the global search within
    * Hyperswitch Control Centre, you can search for any data across any merchant account or profile of which the user is a part.&#x20;

    <figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXdQ2NY5E8lHbH2_QvXzepO-6TissIdWWhV9pZRNPZeMKh2GgynWaNKWtbJnJNRYppn_buAMYqqfMkz9VvupvfkFVee_cbS5oY6Z0Mbx0Vvgri6Jw7T-shuBQouJ4BKY2o_nPvKG159LdfPhAOEfb2My0ekN?key=KjIGF7_A-nGwRp3B4LA6NQ" alt=""><figcaption></figcaption></figure>

{% content-ref url="./" %}
[.](./)
{% endcontent-ref %}
