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
     symbols: CreateApiKeyRequest, MerchantConnectorCreate = crates/router/src/types/api/api_keys.rs; crates/api_models/src/admin.rs
     symbols: organization_create, merchant_account_create, profile_create, api_key_create, connector_create = crates/router/src/routes/admin.rs; crates/router/src/routes/profiles.rs; crates/router/src/routes/api_keys.rs
     symbols: PlatformOrgAdminAuth = crates/router/src/services/authentication.rs
     checked: 2026-09-22 -->

# Platform Organization

A Platform Organization is an organization whose platform merchant can create and manage merchant accounts programmatically. The backend represents organization type with `organization_type: "platform"` and merchant type with `merchant_account_type: "platform"`, `"connected"`, or `"standard"`.

The platform merchant is the control-plane merchant. A Connected merchant can be operated on behalf of through the platform authorization path. A Standard merchant remains operationally isolated and uses its own merchant API key for payment operations.

### Programmatic onboarding flow

The exact v1 sequence is:

1. Create or convert the organization. Create with `POST /organization`, or convert with `POST /organization/{id}/convert_to_platform`.
2. Generate the Platform API Key. Switch to the platform merchant in the dashboard and create an API key on the [API keys page](https://app.hyperswitch.io/dashboard/developer-api-keys). Every call below authenticates with this key, so generate it before continuing.
3. Create a connected merchant account with `POST /accounts`. Set the merchant-account request type to `connected` where the request schema provides it.
4. Create the merchant's Business Profile with `POST /account/{account_id}/business_profile`.
5. Create an API key for that merchant with `POST /api_keys/{merchant_id}`.
6. Create the merchant connector account for that profile with `POST /account/{merchant_id}/connectors`, putting the processor credentials in `connector_account_details`. The platform can send this with either the merchant's own API key or the Platform API Key.
7. Use the new merchant API key for the merchant's payment operations. For a Connected merchant, the platform authorization path can perform permitted operations on behalf of that merchant.

The Platform API Key is privileged but not universal. It authorizes creating and managing merchant accounts in the organization, and it can act on behalf of Connected merchants. It does not run payments for Standard merchants; those use their own merchant API key. The administrative routes accept it through `PlatformOrgAdminAuth`, which rejects the key unless it belongs to a platform merchant account and platform support is enabled in configuration.

For v2, the corresponding routes are `POST /v2/merchant-accounts`, `POST /v2/profiles`, `POST /v2/api-keys`, and `POST /v2/connector-accounts`. The v2 route uses the authenticated merchant context rather than putting the merchant ID in each of those paths. Check the versioned request schema before sending fields because v1 and v2 use different identifier placement and profile request shapes.

The profile remains the boundary for payment configuration. Processor credentials belong to the merchant connector account created for that profile, not to the platform organization or the merchant account.

### Resource boundaries

Connected merchants share the platform resource model only where the backend permits it. Standard merchants keep isolated customer and payment-method data. Both merchant types have their own merchant account and profiles. The classification is set by the merchant-account type and is not a dashboard label that changes the API scope.

### Dashboard profile identifier

The control center's payment-settings profile view shows `Profile ID` next to `Profile Name` and `Merchant ID`, with a copy control. Where that identifier goes depends on the API version: on v1 pass it as `profile_id` in the payment request body, and on v2 send it in the `X-Profile-Id` header, because the v2 `PaymentsRequest` has no `profile_id` field. In profile APIs it is the profile path parameter on both versions. See [Organization, Merchant Account, and Business Profile](hyperswitch-account-structure.md#choosing-the-level).

### Related pages

* [Organization, Merchant Account, and Business Profile](hyperswitch-account-structure.md)
* [Setting Up a Platform Organization](setting-up-platform-organization.md)
* [On-Behalf-of Operations](on-behalf-of-operations.md)
