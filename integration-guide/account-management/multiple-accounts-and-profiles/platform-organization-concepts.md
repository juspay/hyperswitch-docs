---
description: Conceptual reference for Platform Organizations, Platform Merchants, and Connected and Standard merchants.
icon: sitemap
metaLinks:
  alternates:
    - platform-organization-concepts.md
---

<!-- truth manifest; hyperswitch 502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5; control-center 2c18b1da385bc79cfa9b4da6204bf869cfc50f42; spec api-reference/v1/openapi_spec_v1.json@502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5
     symbols: OrganizationType, MerchantAccountType, MerchantAccountRequestType = crates/common_enums/src/enums/accounts.rs
     symbols: OrganizationCreateRequest, OrganizationResponse, ConvertOrganizationToPlatformRequest = crates/api_models/src/organization.rs
     symbols: MerchantAccountCreate = crates/api_models/src/admin.rs
     symbols: ProfileCreate = crates/api_models/src/admin.rs
     symbols: CreateApiKeyRequest = crates/router/src/types/api/api_keys.rs
     symbols: organization_create, merchant_account_create, profile_create, api_key_create = crates/router/src/routes/admin.rs; crates/router/src/routes/profiles.rs; crates/router/src/routes/api_keys.rs
     checked: 2026-09-22 -->

# Platform Organization

A Platform Organization is an organization whose platform merchant can create and manage merchant accounts programmatically. The backend represents organization type with `organization_type: "platform"` and merchant type with `merchant_account_type: "platform"`, `"connected"`, or `"standard"`.

The platform merchant is the control-plane merchant. A Connected merchant can be operated on behalf of through the platform authorization path. A Standard merchant remains operationally isolated and uses its own merchant API key for payment operations.

### Programmatic onboarding flow

The exact v1 sequence is:

1. Create or convert the organization. Create with `POST /organization`, or convert with `POST /organization/{id}/convert_to_platform`.
2. Create a connected merchant account with `POST /accounts`. Set the merchant-account request type to `connected` where the request schema provides it.
3. Create the merchant's Business Profile with `POST /account/{account_id}/business_profile`.
4. Create an API key for that merchant with `POST /api_keys/{merchant_id}`.
5. Use the new merchant API key for the merchant's payment operations. For a Connected merchant, the platform authorization path can perform permitted operations on behalf of that merchant.

For v2, the corresponding routes are `POST /v2/merchant-accounts`, `POST /v2/profiles`, and `POST /v2/api-keys`. The v2 route uses the authenticated merchant context rather than putting the merchant ID in each of those paths. Check the versioned request schema before sending fields because v1 and v2 use different identifier placement and profile request shapes.

The profile remains the boundary for payment configuration. Processor credentials belong to the merchant connector account created for that profile, not to the platform organization or the merchant account.

### Resource boundaries

Connected merchants share the platform resource model only where the backend permits it. Standard merchants keep isolated customer and payment-method data. Both merchant types have their own merchant account and profiles. The classification is set by the merchant-account type and is not a dashboard label that changes the API scope.

### Dashboard profile identifier

The control center's payment-settings profile view shows `Profile ID` next to `Profile Name` and `Merchant ID`, with a copy control. This is the identifier to pass as `profile_id` in a payment request or as the profile path parameter in profile APIs.

### Related pages

* [Organization, Merchant, and Profile](hyperswitch-account-structure.md)
* [Setting Up a Platform Organization](setting-up-platform-organization.md)
* [On-Behalf-of Operations](on-behalf-of-operations.md)
