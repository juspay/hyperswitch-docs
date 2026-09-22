---
description: >-
  Understand the Organization, Merchant Account, and Business Profile hierarchy.
icon: people-roof
metaLinks:
  alternates:
    - hyperswitch-account-structure.md
---

<!-- truth manifest; hyperswitch 502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5; control-center 2c18b1da385bc79cfa9b4da6204bf869cfc50f42; spec api-reference/v1/openapi_spec_v1.json@502bfe8ddbe6a9a9619dc4e0b88900a780c2aac5
     symbols: OrganizationId, OrganizationResponse = crates/api_models/src/organization.rs
     symbols: MerchantAccountCreate, MerchantAccountResponse = crates/api_models/src/admin.rs
     symbols: ProfileCreate, ProfileUpdate, ProfileResponse = crates/api_models/src/admin.rs
     symbols: MerchantConnectorCreate, MerchantConnectorResponse = crates/api_models/src/admin.rs
     symbols: PaymentsRequest.profile_id = crates/api_models/src/payments.rs
     symbols: get_profile_id_from_business_details = crates/router/src/core/utils.rs
     symbols: profile_update = crates/router/src/routes/profiles.rs; crates/router/src/routes/app.rs
     symbols: BusinessProfileInterfaceTypesV1.profileEntity_v1, profileEntityRequestType_v1 = control-center/src/Interface/BusinessProfileInterface/BusinessProfileInterfaceTypes/BusinessProfileInterfaceTypesV1.res
     symbols: ProfileInfoHeader = control-center/src/screens/Developer/PaymentSettings/PaymentSettingsProfileInfo.res
     checked: 2026-09-22 -->

# Organization, Merchant Account, and Business Profile

Hyperswitch separates organization ownership, merchant authentication, and payment configuration.

* An **Organization** is identified by an `organization_id`. It owns merchant accounts and can be standard or platform type.
* A **Merchant Account** is identified by a `merchant_id`. It belongs to an organization and is the scope for merchant API keys.
* A **Business Profile** is identified by a `profile_id`. It belongs to a merchant account and stores payment configuration, including return URL, webhook details, routing-related settings, and profile-level feature settings.
* A **merchant_connector_account** is identified by a connector-account ID and belongs to a profile. Its connector account details are where processor credentials are stored. Do not put processor credentials on the organization or merchant account.

The backend models this relationship in `OrganizationResponse.organization_id`, `MerchantAccountResponse.merchant_id`, `ProfileResponse.profile_id`, and `MerchantConnectorResponse.profile_id`. The connector create request carries `connector_account_details` on `MerchantConnectorCreate`.

### Choosing the level

Use multiple merchant accounts when each business needs separate merchant API keys. Use multiple profiles when one merchant account needs separate payment configuration while retaining one merchant API-key scope.

A profile is selected for a payment in the API request with `profile_id`. On v1, the field is optional in `PaymentsRequest`. The handler calls `get_profile_id_from_business_details`: it first uses the request `profile_id`, then the merchant account's `default_profile`, and only then resolves the legacy `business_country` plus `business_label` pair. If none is available, the handler returns a missing-field error. Therefore, when the account has one profile and that profile is the account's `default_profile`, omitting `profile_id` works through the default-profile branch. This is handler behavior, not a property of the Rust field declaration. On v2, the create flow requires `profile_id`.

### Edit a Business Profile

You can update a profile with the API or from the dashboard.

#### API

For v1, send `POST /account/{account_id}/business_profile/{profile_id}`. For v2, send `PUT /v2/profiles/{profile_id}`. The route registrations bind these methods to `profile_update`.

The request can update the profile name, return URL, webhook details, authentication connector details, shipping-detail collection settings, retry and routing settings, metadata, and other fields defined by the versioned `ProfileUpdate` struct. To update the profile webhook URL, include the `webhook_details` object with its `webhook_url` member. The v1 and v2 request names differ for some shipping fields, so copy the fields from the API version you are calling.

Example v1 shape:

```json
{
  "webhook_details": {
    "webhook_url": "https://example.com/hyperswitch-webhooks"
  }
}
```

The profile update handler validates `webhook_details` before calling the update operation. The endpoint is not the merchant-account update endpoint.

#### Dashboard

Open the active profile's settings and edit the available profile configuration. The control center fetches a profile with the business-profile endpoint and sends the edited profile through the version-specific update method. Its request model includes `profile_name`, `return_url`, `webhook_details`, authentication connector details, shipping collection options, retry settings, metadata, and version-specific feature flags. The profile page displays the `Profile ID` beside `Profile Name` and `Merchant ID`.

Profile IDs are also available in the dashboard's developer payment settings view. Look for the `Profile ID` field and use its copy control.

### Route out

* KV mode and Redis retention, plus the drainer configuration, are self-hosting concerns. See [Operations](../../control-center/operations.md) and the self-hosting operations documentation.
* For the complete field list for `POST /payments`, use the [Payments Create API reference](https://api-reference.hyperswitch.io/v1/payments/payments--create). The list is generated from the `PaymentsRequest` schema and must be kept with the API reference rather than duplicated here.

If you need programmatic merchant onboarding, continue to [Platform Organization](platform-organization-concepts.md).
