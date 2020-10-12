# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum, EnumMeta
from six import with_metaclass

class _CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(self, name):
        return super().__getitem__(name.upper())

    def __getattr__(cls, name):
        """Return the enum member matching `name`
        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.
        """
        try:
            return cls._member_map_[name.upper()]
        except KeyError:
            raise AttributeError(name)


class Enum10(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DELETED_DATE_TIME = "deletedDateTime"
    DESCRIPTION = "description"
    DISPLAY_NAME = "displayName"
    DEFINITION = "definition"
    IS_ORGANIZATION_DEFAULT = "isOrganizationDefault"
    APPLIES_TO = "appliesTo"

class Enum11(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    APPLIES_TO = "appliesTo"

class Enum12(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DELETED_DATE_TIME = "deletedDateTime"
    DELETED_DATE_TIME_DESC = "deletedDateTime desc"
    DESCRIPTION = "description"
    DESCRIPTION_DESC = "description desc"
    DISPLAY_NAME = "displayName"
    DISPLAY_NAME_DESC = "displayName desc"
    DEFINITION = "definition"
    DEFINITION_DESC = "definition desc"
    IS_ORGANIZATION_DEFAULT = "isOrganizationDefault"
    IS_ORGANIZATION_DEFAULT_DESC = "isOrganizationDefault desc"

class Enum13(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DELETED_DATE_TIME = "deletedDateTime"
    DELETED_DATE_TIME_DESC = "deletedDateTime desc"

class Enum14(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DELETED_DATE_TIME = "deletedDateTime"

class Enum15(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DELETED_DATE_TIME = "deletedDateTime"
    DELETED_DATE_TIME_DESC = "deletedDateTime desc"

class Enum16(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DELETED_DATE_TIME = "deletedDateTime"
    DELETED_DATE_TIME_DESC = "deletedDateTime desc"
    DESCRIPTION = "description"
    DESCRIPTION_DESC = "description desc"
    DISPLAY_NAME = "displayName"
    DISPLAY_NAME_DESC = "displayName desc"
    DEFINITION = "definition"
    DEFINITION_DESC = "definition desc"
    IS_ORGANIZATION_DEFAULT = "isOrganizationDefault"
    IS_ORGANIZATION_DEFAULT_DESC = "isOrganizationDefault desc"

class Enum17(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DELETED_DATE_TIME = "deletedDateTime"
    DESCRIPTION = "description"
    DISPLAY_NAME = "displayName"
    DEFINITION = "definition"
    IS_ORGANIZATION_DEFAULT = "isOrganizationDefault"
    APPLIES_TO = "appliesTo"

class Enum18(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    APPLIES_TO = "appliesTo"

class Enum19(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DELETED_DATE_TIME = "deletedDateTime"
    DELETED_DATE_TIME_DESC = "deletedDateTime desc"
    DESCRIPTION = "description"
    DESCRIPTION_DESC = "description desc"
    DISPLAY_NAME = "displayName"
    DISPLAY_NAME_DESC = "displayName desc"
    DEFINITION = "definition"
    DEFINITION_DESC = "definition desc"
    IS_ORGANIZATION_DEFAULT = "isOrganizationDefault"
    IS_ORGANIZATION_DEFAULT_DESC = "isOrganizationDefault desc"

class Enum20(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DELETED_DATE_TIME = "deletedDateTime"
    DELETED_DATE_TIME_DESC = "deletedDateTime desc"
    DESCRIPTION = "description"
    DESCRIPTION_DESC = "description desc"
    DISPLAY_NAME = "displayName"
    DISPLAY_NAME_DESC = "displayName desc"
    DEFINITION = "definition"
    DEFINITION_DESC = "definition desc"
    IS_ORGANIZATION_DEFAULT = "isOrganizationDefault"
    IS_ORGANIZATION_DEFAULT_DESC = "isOrganizationDefault desc"

class Enum21(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DELETED_DATE_TIME = "deletedDateTime"
    DESCRIPTION = "description"
    DISPLAY_NAME = "displayName"
    DEFINITION = "definition"
    IS_ORGANIZATION_DEFAULT = "isOrganizationDefault"
    APPLIES_TO = "appliesTo"

class Enum22(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    APPLIES_TO = "appliesTo"

class Enum23(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DELETED_DATE_TIME = "deletedDateTime"
    DELETED_DATE_TIME_DESC = "deletedDateTime desc"
    DESCRIPTION = "description"
    DESCRIPTION_DESC = "description desc"
    DISPLAY_NAME = "displayName"
    DISPLAY_NAME_DESC = "displayName desc"
    DEFINITION = "definition"
    DEFINITION_DESC = "definition desc"
    IS_ORGANIZATION_DEFAULT = "isOrganizationDefault"
    IS_ORGANIZATION_DEFAULT_DESC = "isOrganizationDefault desc"

class Enum24(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DELETED_DATE_TIME = "deletedDateTime"
    DELETED_DATE_TIME_DESC = "deletedDateTime desc"
    APP_ROLE_ID = "appRoleId"
    APP_ROLE_ID_DESC = "appRoleId desc"
    CREATED_DATE_TIME = "createdDateTime"
    CREATED_DATE_TIME_DESC = "createdDateTime desc"
    PRINCIPAL_DISPLAY_NAME = "principalDisplayName"
    PRINCIPAL_DISPLAY_NAME_DESC = "principalDisplayName desc"
    PRINCIPAL_ID = "principalId"
    PRINCIPAL_ID_DESC = "principalId desc"
    PRINCIPAL_TYPE = "principalType"
    PRINCIPAL_TYPE_DESC = "principalType desc"
    RESOURCE_DISPLAY_NAME = "resourceDisplayName"
    RESOURCE_DISPLAY_NAME_DESC = "resourceDisplayName desc"
    RESOURCE_ID = "resourceId"
    RESOURCE_ID_DESC = "resourceId desc"

class Enum25(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DELETED_DATE_TIME = "deletedDateTime"
    APP_ROLE_ID = "appRoleId"
    CREATED_DATE_TIME = "createdDateTime"
    PRINCIPAL_DISPLAY_NAME = "principalDisplayName"
    PRINCIPAL_ID = "principalId"
    PRINCIPAL_TYPE = "principalType"
    RESOURCE_DISPLAY_NAME = "resourceDisplayName"
    RESOURCE_ID = "resourceId"

class Enum26(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DELETED_DATE_TIME = "deletedDateTime"
    APP_ROLE_ID = "appRoleId"
    CREATED_DATE_TIME = "createdDateTime"
    PRINCIPAL_DISPLAY_NAME = "principalDisplayName"
    PRINCIPAL_ID = "principalId"
    PRINCIPAL_TYPE = "principalType"
    RESOURCE_DISPLAY_NAME = "resourceDisplayName"
    RESOURCE_ID = "resourceId"

class Enum27(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DELETED_DATE_TIME = "deletedDateTime"
    DELETED_DATE_TIME_DESC = "deletedDateTime desc"
    ACCOUNT_ENABLED = "accountEnabled"
    ACCOUNT_ENABLED_DESC = "accountEnabled desc"
    ADD_INS = "addIns"
    ADD_INS_DESC = "addIns desc"
    ALTERNATIVE_NAMES = "alternativeNames"
    ALTERNATIVE_NAMES_DESC = "alternativeNames desc"
    APP_DESCRIPTION = "appDescription"
    APP_DESCRIPTION_DESC = "appDescription desc"
    APP_DISPLAY_NAME = "appDisplayName"
    APP_DISPLAY_NAME_DESC = "appDisplayName desc"
    APP_ID = "appId"
    APP_ID_DESC = "appId desc"
    APPLICATION_TEMPLATE_ID = "applicationTemplateId"
    APPLICATION_TEMPLATE_ID_DESC = "applicationTemplateId desc"
    APP_OWNER_ORGANIZATION_ID = "appOwnerOrganizationId"
    APP_OWNER_ORGANIZATION_ID_DESC = "appOwnerOrganizationId desc"
    APP_ROLE_ASSIGNMENT_REQUIRED = "appRoleAssignmentRequired"
    APP_ROLE_ASSIGNMENT_REQUIRED_DESC = "appRoleAssignmentRequired desc"
    APP_ROLES = "appRoles"
    APP_ROLES_DESC = "appRoles desc"
    DESCRIPTION = "description"
    DESCRIPTION_DESC = "description desc"
    DISPLAY_NAME = "displayName"
    DISPLAY_NAME_DESC = "displayName desc"
    HOMEPAGE = "homepage"
    HOMEPAGE_DESC = "homepage desc"
    INFO = "info"
    INFO_DESC = "info desc"
    KEY_CREDENTIALS = "keyCredentials"
    KEY_CREDENTIALS_DESC = "keyCredentials desc"
    LOGIN_URL = "loginUrl"
    LOGIN_URL_DESC = "loginUrl desc"
    LOGOUT_URL = "logoutUrl"
    LOGOUT_URL_DESC = "logoutUrl desc"
    NOTES = "notes"
    NOTES_DESC = "notes desc"
    NOTIFICATION_EMAIL_ADDRESSES = "notificationEmailAddresses"
    NOTIFICATION_EMAIL_ADDRESSES_DESC = "notificationEmailAddresses desc"
    OAUTH2_PERMISSION_SCOPES = "oauth2PermissionScopes"
    OAUTH2_PERMISSION_SCOPES_DESC = "oauth2PermissionScopes desc"
    PASSWORD_CREDENTIALS = "passwordCredentials"
    PASSWORD_CREDENTIALS_DESC = "passwordCredentials desc"
    PREFERRED_SINGLE_SIGN_ON_MODE = "preferredSingleSignOnMode"
    PREFERRED_SINGLE_SIGN_ON_MODE_DESC = "preferredSingleSignOnMode desc"
    PREFERRED_TOKEN_SIGNING_KEY_THUMBPRINT = "preferredTokenSigningKeyThumbprint"
    PREFERRED_TOKEN_SIGNING_KEY_THUMBPRINT_DESC = "preferredTokenSigningKeyThumbprint desc"
    REPLY_URLS = "replyUrls"
    REPLY_URLS_DESC = "replyUrls desc"
    SAML_SINGLE_SIGN_ON_SETTINGS = "samlSingleSignOnSettings"
    SAML_SINGLE_SIGN_ON_SETTINGS_DESC = "samlSingleSignOnSettings desc"
    SERVICE_PRINCIPAL_NAMES = "servicePrincipalNames"
    SERVICE_PRINCIPAL_NAMES_DESC = "servicePrincipalNames desc"
    SERVICE_PRINCIPAL_TYPE = "servicePrincipalType"
    SERVICE_PRINCIPAL_TYPE_DESC = "servicePrincipalType desc"
    TAGS = "tags"
    TAGS_DESC = "tags desc"
    TOKEN_ENCRYPTION_KEY_ID = "tokenEncryptionKeyId"
    TOKEN_ENCRYPTION_KEY_ID_DESC = "tokenEncryptionKeyId desc"

class Enum28(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DELETED_DATE_TIME = "deletedDateTime"
    ACCOUNT_ENABLED = "accountEnabled"
    ADD_INS = "addIns"
    ALTERNATIVE_NAMES = "alternativeNames"
    APP_DESCRIPTION = "appDescription"
    APP_DISPLAY_NAME = "appDisplayName"
    APP_ID = "appId"
    APPLICATION_TEMPLATE_ID = "applicationTemplateId"
    APP_OWNER_ORGANIZATION_ID = "appOwnerOrganizationId"
    APP_ROLE_ASSIGNMENT_REQUIRED = "appRoleAssignmentRequired"
    APP_ROLES = "appRoles"
    DESCRIPTION = "description"
    DISPLAY_NAME = "displayName"
    HOMEPAGE = "homepage"
    INFO = "info"
    KEY_CREDENTIALS = "keyCredentials"
    LOGIN_URL = "loginUrl"
    LOGOUT_URL = "logoutUrl"
    NOTES = "notes"
    NOTIFICATION_EMAIL_ADDRESSES = "notificationEmailAddresses"
    OAUTH2_PERMISSION_SCOPES = "oauth2PermissionScopes"
    PASSWORD_CREDENTIALS = "passwordCredentials"
    PREFERRED_SINGLE_SIGN_ON_MODE = "preferredSingleSignOnMode"
    PREFERRED_TOKEN_SIGNING_KEY_THUMBPRINT = "preferredTokenSigningKeyThumbprint"
    REPLY_URLS = "replyUrls"
    SAML_SINGLE_SIGN_ON_SETTINGS = "samlSingleSignOnSettings"
    SERVICE_PRINCIPAL_NAMES = "servicePrincipalNames"
    SERVICE_PRINCIPAL_TYPE = "servicePrincipalType"
    TAGS = "tags"
    TOKEN_ENCRYPTION_KEY_ID = "tokenEncryptionKeyId"
    APP_ROLE_ASSIGNED_TO = "appRoleAssignedTo"
    APP_ROLE_ASSIGNMENTS = "appRoleAssignments"
    CLAIMS_MAPPING_POLICIES = "claimsMappingPolicies"
    CREATED_OBJECTS = "createdObjects"
    ENDPOINTS = "endpoints"
    HOME_REALM_DISCOVERY_POLICIES = "homeRealmDiscoveryPolicies"
    MEMBER_OF = "memberOf"
    OAUTH2_PERMISSION_GRANTS = "oauth2PermissionGrants"
    OWNED_OBJECTS = "ownedObjects"
    OWNERS = "owners"
    TOKEN_ISSUANCE_POLICIES = "tokenIssuancePolicies"
    TOKEN_LIFETIME_POLICIES = "tokenLifetimePolicies"
    TRANSITIVE_MEMBER_OF = "transitiveMemberOf"

class Enum29(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    APP_ROLE_ASSIGNED_TO = "appRoleAssignedTo"
    APP_ROLE_ASSIGNMENTS = "appRoleAssignments"
    CLAIMS_MAPPING_POLICIES = "claimsMappingPolicies"
    CREATED_OBJECTS = "createdObjects"
    ENDPOINTS = "endpoints"
    HOME_REALM_DISCOVERY_POLICIES = "homeRealmDiscoveryPolicies"
    MEMBER_OF = "memberOf"
    OAUTH2_PERMISSION_GRANTS = "oauth2PermissionGrants"
    OWNED_OBJECTS = "ownedObjects"
    OWNERS = "owners"
    TOKEN_ISSUANCE_POLICIES = "tokenIssuancePolicies"
    TOKEN_LIFETIME_POLICIES = "tokenLifetimePolicies"
    TRANSITIVE_MEMBER_OF = "transitiveMemberOf"

class Enum30(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DELETED_DATE_TIME = "deletedDateTime"
    ACCOUNT_ENABLED = "accountEnabled"
    ADD_INS = "addIns"
    ALTERNATIVE_NAMES = "alternativeNames"
    APP_DESCRIPTION = "appDescription"
    APP_DISPLAY_NAME = "appDisplayName"
    APP_ID = "appId"
    APPLICATION_TEMPLATE_ID = "applicationTemplateId"
    APP_OWNER_ORGANIZATION_ID = "appOwnerOrganizationId"
    APP_ROLE_ASSIGNMENT_REQUIRED = "appRoleAssignmentRequired"
    APP_ROLES = "appRoles"
    DESCRIPTION = "description"
    DISPLAY_NAME = "displayName"
    HOMEPAGE = "homepage"
    INFO = "info"
    KEY_CREDENTIALS = "keyCredentials"
    LOGIN_URL = "loginUrl"
    LOGOUT_URL = "logoutUrl"
    NOTES = "notes"
    NOTIFICATION_EMAIL_ADDRESSES = "notificationEmailAddresses"
    OAUTH2_PERMISSION_SCOPES = "oauth2PermissionScopes"
    PASSWORD_CREDENTIALS = "passwordCredentials"
    PREFERRED_SINGLE_SIGN_ON_MODE = "preferredSingleSignOnMode"
    PREFERRED_TOKEN_SIGNING_KEY_THUMBPRINT = "preferredTokenSigningKeyThumbprint"
    REPLY_URLS = "replyUrls"
    SAML_SINGLE_SIGN_ON_SETTINGS = "samlSingleSignOnSettings"
    SERVICE_PRINCIPAL_NAMES = "servicePrincipalNames"
    SERVICE_PRINCIPAL_TYPE = "servicePrincipalType"
    TAGS = "tags"
    TOKEN_ENCRYPTION_KEY_ID = "tokenEncryptionKeyId"
    APP_ROLE_ASSIGNED_TO = "appRoleAssignedTo"
    APP_ROLE_ASSIGNMENTS = "appRoleAssignments"
    CLAIMS_MAPPING_POLICIES = "claimsMappingPolicies"
    CREATED_OBJECTS = "createdObjects"
    ENDPOINTS = "endpoints"
    HOME_REALM_DISCOVERY_POLICIES = "homeRealmDiscoveryPolicies"
    MEMBER_OF = "memberOf"
    OAUTH2_PERMISSION_GRANTS = "oauth2PermissionGrants"
    OWNED_OBJECTS = "ownedObjects"
    OWNERS = "owners"
    TOKEN_ISSUANCE_POLICIES = "tokenIssuancePolicies"
    TOKEN_LIFETIME_POLICIES = "tokenLifetimePolicies"
    TRANSITIVE_MEMBER_OF = "transitiveMemberOf"

class Enum31(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    APP_ROLE_ASSIGNED_TO = "appRoleAssignedTo"
    APP_ROLE_ASSIGNMENTS = "appRoleAssignments"
    CLAIMS_MAPPING_POLICIES = "claimsMappingPolicies"
    CREATED_OBJECTS = "createdObjects"
    ENDPOINTS = "endpoints"
    HOME_REALM_DISCOVERY_POLICIES = "homeRealmDiscoveryPolicies"
    MEMBER_OF = "memberOf"
    OAUTH2_PERMISSION_GRANTS = "oauth2PermissionGrants"
    OWNED_OBJECTS = "ownedObjects"
    OWNERS = "owners"
    TOKEN_ISSUANCE_POLICIES = "tokenIssuancePolicies"
    TOKEN_LIFETIME_POLICIES = "tokenLifetimePolicies"
    TRANSITIVE_MEMBER_OF = "transitiveMemberOf"

class Enum32(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DELETED_DATE_TIME = "deletedDateTime"
    DELETED_DATE_TIME_DESC = "deletedDateTime desc"
    APP_ROLE_ID = "appRoleId"
    APP_ROLE_ID_DESC = "appRoleId desc"
    CREATED_DATE_TIME = "createdDateTime"
    CREATED_DATE_TIME_DESC = "createdDateTime desc"
    PRINCIPAL_DISPLAY_NAME = "principalDisplayName"
    PRINCIPAL_DISPLAY_NAME_DESC = "principalDisplayName desc"
    PRINCIPAL_ID = "principalId"
    PRINCIPAL_ID_DESC = "principalId desc"
    PRINCIPAL_TYPE = "principalType"
    PRINCIPAL_TYPE_DESC = "principalType desc"
    RESOURCE_DISPLAY_NAME = "resourceDisplayName"
    RESOURCE_DISPLAY_NAME_DESC = "resourceDisplayName desc"
    RESOURCE_ID = "resourceId"
    RESOURCE_ID_DESC = "resourceId desc"

class Enum33(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DELETED_DATE_TIME = "deletedDateTime"
    APP_ROLE_ID = "appRoleId"
    CREATED_DATE_TIME = "createdDateTime"
    PRINCIPAL_DISPLAY_NAME = "principalDisplayName"
    PRINCIPAL_ID = "principalId"
    PRINCIPAL_TYPE = "principalType"
    RESOURCE_DISPLAY_NAME = "resourceDisplayName"
    RESOURCE_ID = "resourceId"

class Enum34(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DELETED_DATE_TIME = "deletedDateTime"
    APP_ROLE_ID = "appRoleId"
    CREATED_DATE_TIME = "createdDateTime"
    PRINCIPAL_DISPLAY_NAME = "principalDisplayName"
    PRINCIPAL_ID = "principalId"
    PRINCIPAL_TYPE = "principalType"
    RESOURCE_DISPLAY_NAME = "resourceDisplayName"
    RESOURCE_ID = "resourceId"

class Enum35(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DELETED_DATE_TIME = "deletedDateTime"
    DELETED_DATE_TIME_DESC = "deletedDateTime desc"
    APP_ROLE_ID = "appRoleId"
    APP_ROLE_ID_DESC = "appRoleId desc"
    CREATED_DATE_TIME = "createdDateTime"
    CREATED_DATE_TIME_DESC = "createdDateTime desc"
    PRINCIPAL_DISPLAY_NAME = "principalDisplayName"
    PRINCIPAL_DISPLAY_NAME_DESC = "principalDisplayName desc"
    PRINCIPAL_ID = "principalId"
    PRINCIPAL_ID_DESC = "principalId desc"
    PRINCIPAL_TYPE = "principalType"
    PRINCIPAL_TYPE_DESC = "principalType desc"
    RESOURCE_DISPLAY_NAME = "resourceDisplayName"
    RESOURCE_DISPLAY_NAME_DESC = "resourceDisplayName desc"
    RESOURCE_ID = "resourceId"
    RESOURCE_ID_DESC = "resourceId desc"

class Enum36(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DELETED_DATE_TIME = "deletedDateTime"
    APP_ROLE_ID = "appRoleId"
    CREATED_DATE_TIME = "createdDateTime"
    PRINCIPAL_DISPLAY_NAME = "principalDisplayName"
    PRINCIPAL_ID = "principalId"
    PRINCIPAL_TYPE = "principalType"
    RESOURCE_DISPLAY_NAME = "resourceDisplayName"
    RESOURCE_ID = "resourceId"

class Enum37(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DELETED_DATE_TIME = "deletedDateTime"
    APP_ROLE_ID = "appRoleId"
    CREATED_DATE_TIME = "createdDateTime"
    PRINCIPAL_DISPLAY_NAME = "principalDisplayName"
    PRINCIPAL_ID = "principalId"
    PRINCIPAL_TYPE = "principalType"
    RESOURCE_DISPLAY_NAME = "resourceDisplayName"
    RESOURCE_ID = "resourceId"

class Enum38(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DELETED_DATE_TIME = "deletedDateTime"
    DELETED_DATE_TIME_DESC = "deletedDateTime desc"
    DESCRIPTION = "description"
    DESCRIPTION_DESC = "description desc"
    DISPLAY_NAME = "displayName"
    DISPLAY_NAME_DESC = "displayName desc"
    DEFINITION = "definition"
    DEFINITION_DESC = "definition desc"
    IS_ORGANIZATION_DEFAULT = "isOrganizationDefault"
    IS_ORGANIZATION_DEFAULT_DESC = "isOrganizationDefault desc"

class Enum39(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DELETED_DATE_TIME = "deletedDateTime"
    DESCRIPTION = "description"
    DISPLAY_NAME = "displayName"
    DEFINITION = "definition"
    IS_ORGANIZATION_DEFAULT = "isOrganizationDefault"
    APPLIES_TO = "appliesTo"

class Enum40(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    APPLIES_TO = "appliesTo"

class Enum41(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DELETED_DATE_TIME = "deletedDateTime"
    DELETED_DATE_TIME_DESC = "deletedDateTime desc"
    DESCRIPTION = "description"
    DESCRIPTION_DESC = "description desc"
    DISPLAY_NAME = "displayName"
    DISPLAY_NAME_DESC = "displayName desc"
    DEFINITION = "definition"
    DEFINITION_DESC = "definition desc"
    IS_ORGANIZATION_DEFAULT = "isOrganizationDefault"
    IS_ORGANIZATION_DEFAULT_DESC = "isOrganizationDefault desc"

class Enum42(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DELETED_DATE_TIME = "deletedDateTime"
    DELETED_DATE_TIME_DESC = "deletedDateTime desc"

class Enum43(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DELETED_DATE_TIME = "deletedDateTime"

class Enum44(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DELETED_DATE_TIME = "deletedDateTime"
    DELETED_DATE_TIME_DESC = "deletedDateTime desc"

class Enum45(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DELETED_DATE_TIME = "deletedDateTime"
    DELETED_DATE_TIME_DESC = "deletedDateTime desc"
    CAPABILITY = "capability"
    CAPABILITY_DESC = "capability desc"
    PROVIDER_ID = "providerId"
    PROVIDER_ID_DESC = "providerId desc"
    PROVIDER_NAME = "providerName"
    PROVIDER_NAME_DESC = "providerName desc"
    PROVIDER_RESOURCE_ID = "providerResourceId"
    PROVIDER_RESOURCE_ID_DESC = "providerResourceId desc"
    URI = "uri"
    URI_DESC = "uri desc"

class Enum46(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DELETED_DATE_TIME = "deletedDateTime"
    CAPABILITY = "capability"
    PROVIDER_ID = "providerId"
    PROVIDER_NAME = "providerName"
    PROVIDER_RESOURCE_ID = "providerResourceId"
    URI = "uri"

class Enum47(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DELETED_DATE_TIME = "deletedDateTime"
    CAPABILITY = "capability"
    PROVIDER_ID = "providerId"
    PROVIDER_NAME = "providerName"
    PROVIDER_RESOURCE_ID = "providerResourceId"
    URI = "uri"

class Enum48(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DELETED_DATE_TIME = "deletedDateTime"
    DELETED_DATE_TIME_DESC = "deletedDateTime desc"
    DESCRIPTION = "description"
    DESCRIPTION_DESC = "description desc"
    DISPLAY_NAME = "displayName"
    DISPLAY_NAME_DESC = "displayName desc"
    DEFINITION = "definition"
    DEFINITION_DESC = "definition desc"
    IS_ORGANIZATION_DEFAULT = "isOrganizationDefault"
    IS_ORGANIZATION_DEFAULT_DESC = "isOrganizationDefault desc"

class Enum49(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DELETED_DATE_TIME = "deletedDateTime"
    DESCRIPTION = "description"
    DISPLAY_NAME = "displayName"
    DEFINITION = "definition"
    IS_ORGANIZATION_DEFAULT = "isOrganizationDefault"
    APPLIES_TO = "appliesTo"

class Enum5(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DELETED_DATE_TIME = "deletedDateTime"

class Enum50(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    APPLIES_TO = "appliesTo"

class Enum51(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DELETED_DATE_TIME = "deletedDateTime"
    DELETED_DATE_TIME_DESC = "deletedDateTime desc"
    DESCRIPTION = "description"
    DESCRIPTION_DESC = "description desc"
    DISPLAY_NAME = "displayName"
    DISPLAY_NAME_DESC = "displayName desc"
    DEFINITION = "definition"
    DEFINITION_DESC = "definition desc"
    IS_ORGANIZATION_DEFAULT = "isOrganizationDefault"
    IS_ORGANIZATION_DEFAULT_DESC = "isOrganizationDefault desc"

class Enum52(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DELETED_DATE_TIME = "deletedDateTime"
    DELETED_DATE_TIME_DESC = "deletedDateTime desc"

class Enum53(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DELETED_DATE_TIME = "deletedDateTime"

class Enum54(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DELETED_DATE_TIME = "deletedDateTime"
    DELETED_DATE_TIME_DESC = "deletedDateTime desc"

class Enum55(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    CLIENT_ID = "clientId"
    CLIENT_ID_DESC = "clientId desc"
    CONSENT_TYPE = "consentType"
    CONSENT_TYPE_DESC = "consentType desc"
    PRINCIPAL_ID = "principalId"
    PRINCIPAL_ID_DESC = "principalId desc"
    RESOURCE_ID = "resourceId"
    RESOURCE_ID_DESC = "resourceId desc"
    SCOPE = "scope"
    SCOPE_DESC = "scope desc"

class Enum56(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    CLIENT_ID = "clientId"
    CONSENT_TYPE = "consentType"
    PRINCIPAL_ID = "principalId"
    RESOURCE_ID = "resourceId"
    SCOPE = "scope"

class Enum57(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    CLIENT_ID = "clientId"
    CLIENT_ID_DESC = "clientId desc"
    CONSENT_TYPE = "consentType"
    CONSENT_TYPE_DESC = "consentType desc"
    PRINCIPAL_ID = "principalId"
    PRINCIPAL_ID_DESC = "principalId desc"
    RESOURCE_ID = "resourceId"
    RESOURCE_ID_DESC = "resourceId desc"
    SCOPE = "scope"
    SCOPE_DESC = "scope desc"

class Enum58(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DELETED_DATE_TIME = "deletedDateTime"
    DELETED_DATE_TIME_DESC = "deletedDateTime desc"

class Enum59(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DELETED_DATE_TIME = "deletedDateTime"

class Enum6(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DELETED_DATE_TIME = "deletedDateTime"
    DELETED_DATE_TIME_DESC = "deletedDateTime desc"
    APP_DISPLAY_NAME = "appDisplayName"
    APP_DISPLAY_NAME_DESC = "appDisplayName desc"
    DATA_TYPE = "dataType"
    DATA_TYPE_DESC = "dataType desc"
    IS_SYNCED_FROM_ON_PREMISES = "isSyncedFromOnPremises"
    IS_SYNCED_FROM_ON_PREMISES_DESC = "isSyncedFromOnPremises desc"
    NAME = "name"
    NAME_DESC = "name desc"
    TARGET_OBJECTS = "targetObjects"
    TARGET_OBJECTS_DESC = "targetObjects desc"

class Enum60(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DELETED_DATE_TIME = "deletedDateTime"
    DELETED_DATE_TIME_DESC = "deletedDateTime desc"

class Enum61(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DELETED_DATE_TIME = "deletedDateTime"
    DELETED_DATE_TIME_DESC = "deletedDateTime desc"

class Enum62(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DELETED_DATE_TIME = "deletedDateTime"

class Enum63(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DELETED_DATE_TIME = "deletedDateTime"
    DELETED_DATE_TIME_DESC = "deletedDateTime desc"

class Enum64(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DELETED_DATE_TIME = "deletedDateTime"
    DELETED_DATE_TIME_DESC = "deletedDateTime desc"
    DESCRIPTION = "description"
    DESCRIPTION_DESC = "description desc"
    DISPLAY_NAME = "displayName"
    DISPLAY_NAME_DESC = "displayName desc"
    DEFINITION = "definition"
    DEFINITION_DESC = "definition desc"
    IS_ORGANIZATION_DEFAULT = "isOrganizationDefault"
    IS_ORGANIZATION_DEFAULT_DESC = "isOrganizationDefault desc"

class Enum65(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DELETED_DATE_TIME = "deletedDateTime"
    DESCRIPTION = "description"
    DISPLAY_NAME = "displayName"
    DEFINITION = "definition"
    IS_ORGANIZATION_DEFAULT = "isOrganizationDefault"
    APPLIES_TO = "appliesTo"

class Enum66(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    APPLIES_TO = "appliesTo"

class Enum67(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DELETED_DATE_TIME = "deletedDateTime"
    DELETED_DATE_TIME_DESC = "deletedDateTime desc"
    DESCRIPTION = "description"
    DESCRIPTION_DESC = "description desc"
    DISPLAY_NAME = "displayName"
    DISPLAY_NAME_DESC = "displayName desc"
    DEFINITION = "definition"
    DEFINITION_DESC = "definition desc"
    IS_ORGANIZATION_DEFAULT = "isOrganizationDefault"
    IS_ORGANIZATION_DEFAULT_DESC = "isOrganizationDefault desc"

class Enum68(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DELETED_DATE_TIME = "deletedDateTime"
    DELETED_DATE_TIME_DESC = "deletedDateTime desc"
    DESCRIPTION = "description"
    DESCRIPTION_DESC = "description desc"
    DISPLAY_NAME = "displayName"
    DISPLAY_NAME_DESC = "displayName desc"
    DEFINITION = "definition"
    DEFINITION_DESC = "definition desc"
    IS_ORGANIZATION_DEFAULT = "isOrganizationDefault"
    IS_ORGANIZATION_DEFAULT_DESC = "isOrganizationDefault desc"

class Enum69(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DELETED_DATE_TIME = "deletedDateTime"
    DESCRIPTION = "description"
    DISPLAY_NAME = "displayName"
    DEFINITION = "definition"
    IS_ORGANIZATION_DEFAULT = "isOrganizationDefault"
    APPLIES_TO = "appliesTo"

class Enum7(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DELETED_DATE_TIME = "deletedDateTime"
    APP_DISPLAY_NAME = "appDisplayName"
    DATA_TYPE = "dataType"
    IS_SYNCED_FROM_ON_PREMISES = "isSyncedFromOnPremises"
    NAME = "name"
    TARGET_OBJECTS = "targetObjects"

class Enum70(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    APPLIES_TO = "appliesTo"

class Enum71(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DELETED_DATE_TIME = "deletedDateTime"
    DELETED_DATE_TIME_DESC = "deletedDateTime desc"
    DESCRIPTION = "description"
    DESCRIPTION_DESC = "description desc"
    DISPLAY_NAME = "displayName"
    DISPLAY_NAME_DESC = "displayName desc"
    DEFINITION = "definition"
    DEFINITION_DESC = "definition desc"
    IS_ORGANIZATION_DEFAULT = "isOrganizationDefault"
    IS_ORGANIZATION_DEFAULT_DESC = "isOrganizationDefault desc"

class Enum72(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DELETED_DATE_TIME = "deletedDateTime"
    DELETED_DATE_TIME_DESC = "deletedDateTime desc"

class Enum73(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DELETED_DATE_TIME = "deletedDateTime"

class Enum74(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DELETED_DATE_TIME = "deletedDateTime"
    DELETED_DATE_TIME_DESC = "deletedDateTime desc"

class Enum75(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DELETED_DATE_TIME = "deletedDateTime"
    DELETED_DATE_TIME_DESC = "deletedDateTime desc"
    APP_ROLE_ID = "appRoleId"
    APP_ROLE_ID_DESC = "appRoleId desc"
    CREATED_DATE_TIME = "createdDateTime"
    CREATED_DATE_TIME_DESC = "createdDateTime desc"
    PRINCIPAL_DISPLAY_NAME = "principalDisplayName"
    PRINCIPAL_DISPLAY_NAME_DESC = "principalDisplayName desc"
    PRINCIPAL_ID = "principalId"
    PRINCIPAL_ID_DESC = "principalId desc"
    PRINCIPAL_TYPE = "principalType"
    PRINCIPAL_TYPE_DESC = "principalType desc"
    RESOURCE_DISPLAY_NAME = "resourceDisplayName"
    RESOURCE_DISPLAY_NAME_DESC = "resourceDisplayName desc"
    RESOURCE_ID = "resourceId"
    RESOURCE_ID_DESC = "resourceId desc"

class Enum76(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DELETED_DATE_TIME = "deletedDateTime"
    APP_ROLE_ID = "appRoleId"
    CREATED_DATE_TIME = "createdDateTime"
    PRINCIPAL_DISPLAY_NAME = "principalDisplayName"
    PRINCIPAL_ID = "principalId"
    PRINCIPAL_TYPE = "principalType"
    RESOURCE_DISPLAY_NAME = "resourceDisplayName"
    RESOURCE_ID = "resourceId"

class Enum77(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DELETED_DATE_TIME = "deletedDateTime"
    APP_ROLE_ID = "appRoleId"
    CREATED_DATE_TIME = "createdDateTime"
    PRINCIPAL_DISPLAY_NAME = "principalDisplayName"
    PRINCIPAL_ID = "principalId"
    PRINCIPAL_TYPE = "principalType"
    RESOURCE_DISPLAY_NAME = "resourceDisplayName"
    RESOURCE_ID = "resourceId"

class Enum8(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DELETED_DATE_TIME = "deletedDateTime"
    APP_DISPLAY_NAME = "appDisplayName"
    DATA_TYPE = "dataType"
    IS_SYNCED_FROM_ON_PREMISES = "isSyncedFromOnPremises"
    NAME = "name"
    TARGET_OBJECTS = "targetObjects"

class Enum9(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DELETED_DATE_TIME = "deletedDateTime"
    DELETED_DATE_TIME_DESC = "deletedDateTime desc"
    DESCRIPTION = "description"
    DESCRIPTION_DESC = "description desc"
    DISPLAY_NAME = "displayName"
    DISPLAY_NAME_DESC = "displayName desc"
    DEFINITION = "definition"
    DEFINITION_DESC = "definition desc"
    IS_ORGANIZATION_DEFAULT = "isOrganizationDefault"
    IS_ORGANIZATION_DEFAULT_DESC = "isOrganizationDefault desc"

class Get1ItemsItem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DELETED_DATE_TIME = "deletedDateTime"
    ADD_INS = "addIns"
    API = "api"
    APP_ID = "appId"
    APPLICATION_TEMPLATE_ID = "applicationTemplateId"
    APP_ROLES = "appRoles"
    CREATED_DATE_TIME = "createdDateTime"
    DESCRIPTION = "description"
    DISPLAY_NAME = "displayName"
    GROUP_MEMBERSHIP_CLAIMS = "groupMembershipClaims"
    IDENTIFIER_URIS = "identifierUris"
    INFO = "info"
    IS_DEVICE_ONLY_AUTH_SUPPORTED = "isDeviceOnlyAuthSupported"
    IS_FALLBACK_PUBLIC_CLIENT = "isFallbackPublicClient"
    KEY_CREDENTIALS = "keyCredentials"
    LOGO = "logo"
    NOTES = "notes"
    OAUTH2_REQUIRE_POST_RESPONSE = "oauth2RequirePostResponse"
    OPTIONAL_CLAIMS = "optionalClaims"
    PARENTAL_CONTROL_SETTINGS = "parentalControlSettings"
    PASSWORD_CREDENTIALS = "passwordCredentials"
    PUBLIC_CLIENT = "publicClient"
    PUBLISHER_DOMAIN = "publisherDomain"
    REQUIRED_RESOURCE_ACCESS = "requiredResourceAccess"
    SIGN_IN_AUDIENCE = "signInAudience"
    TAGS = "tags"
    TOKEN_ENCRYPTION_KEY_ID = "tokenEncryptionKeyId"
    WEB = "web"
    CREATED_ON_BEHALF_OF = "createdOnBehalfOf"
    EXTENSION_PROPERTIES = "extensionProperties"
    HOME_REALM_DISCOVERY_POLICIES = "homeRealmDiscoveryPolicies"
    OWNERS = "owners"
    TOKEN_ISSUANCE_POLICIES = "tokenIssuancePolicies"
    TOKEN_LIFETIME_POLICIES = "tokenLifetimePolicies"

class Get2ItemsItem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    CREATED_ON_BEHALF_OF = "createdOnBehalfOf"
    EXTENSION_PROPERTIES = "extensionProperties"
    HOME_REALM_DISCOVERY_POLICIES = "homeRealmDiscoveryPolicies"
    OWNERS = "owners"
    TOKEN_ISSUANCE_POLICIES = "tokenIssuancePolicies"
    TOKEN_LIFETIME_POLICIES = "tokenLifetimePolicies"

class Get5ItemsItem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DELETED_DATE_TIME = "deletedDateTime"
    DELETED_DATE_TIME_DESC = "deletedDateTime desc"
    ADD_INS = "addIns"
    ADD_INS_DESC = "addIns desc"
    API = "api"
    API_DESC = "api desc"
    APP_ID = "appId"
    APP_ID_DESC = "appId desc"
    APPLICATION_TEMPLATE_ID = "applicationTemplateId"
    APPLICATION_TEMPLATE_ID_DESC = "applicationTemplateId desc"
    APP_ROLES = "appRoles"
    APP_ROLES_DESC = "appRoles desc"
    CREATED_DATE_TIME = "createdDateTime"
    CREATED_DATE_TIME_DESC = "createdDateTime desc"
    DESCRIPTION = "description"
    DESCRIPTION_DESC = "description desc"
    DISPLAY_NAME = "displayName"
    DISPLAY_NAME_DESC = "displayName desc"
    GROUP_MEMBERSHIP_CLAIMS = "groupMembershipClaims"
    GROUP_MEMBERSHIP_CLAIMS_DESC = "groupMembershipClaims desc"
    IDENTIFIER_URIS = "identifierUris"
    IDENTIFIER_URIS_DESC = "identifierUris desc"
    INFO = "info"
    INFO_DESC = "info desc"
    IS_DEVICE_ONLY_AUTH_SUPPORTED = "isDeviceOnlyAuthSupported"
    IS_DEVICE_ONLY_AUTH_SUPPORTED_DESC = "isDeviceOnlyAuthSupported desc"
    IS_FALLBACK_PUBLIC_CLIENT = "isFallbackPublicClient"
    IS_FALLBACK_PUBLIC_CLIENT_DESC = "isFallbackPublicClient desc"
    KEY_CREDENTIALS = "keyCredentials"
    KEY_CREDENTIALS_DESC = "keyCredentials desc"
    LOGO = "logo"
    LOGO_DESC = "logo desc"
    NOTES = "notes"
    NOTES_DESC = "notes desc"
    OAUTH2_REQUIRE_POST_RESPONSE = "oauth2RequirePostResponse"
    OAUTH2_REQUIRE_POST_RESPONSE_DESC = "oauth2RequirePostResponse desc"
    OPTIONAL_CLAIMS = "optionalClaims"
    OPTIONAL_CLAIMS_DESC = "optionalClaims desc"
    PARENTAL_CONTROL_SETTINGS = "parentalControlSettings"
    PARENTAL_CONTROL_SETTINGS_DESC = "parentalControlSettings desc"
    PASSWORD_CREDENTIALS = "passwordCredentials"
    PASSWORD_CREDENTIALS_DESC = "passwordCredentials desc"
    PUBLIC_CLIENT = "publicClient"
    PUBLIC_CLIENT_DESC = "publicClient desc"
    PUBLISHER_DOMAIN = "publisherDomain"
    PUBLISHER_DOMAIN_DESC = "publisherDomain desc"
    REQUIRED_RESOURCE_ACCESS = "requiredResourceAccess"
    REQUIRED_RESOURCE_ACCESS_DESC = "requiredResourceAccess desc"
    SIGN_IN_AUDIENCE = "signInAudience"
    SIGN_IN_AUDIENCE_DESC = "signInAudience desc"
    TAGS = "tags"
    TAGS_DESC = "tags desc"
    TOKEN_ENCRYPTION_KEY_ID = "tokenEncryptionKeyId"
    TOKEN_ENCRYPTION_KEY_ID_DESC = "tokenEncryptionKeyId desc"
    WEB = "web"
    WEB_DESC = "web desc"

class Get6ItemsItem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DELETED_DATE_TIME = "deletedDateTime"
    ADD_INS = "addIns"
    API = "api"
    APP_ID = "appId"
    APPLICATION_TEMPLATE_ID = "applicationTemplateId"
    APP_ROLES = "appRoles"
    CREATED_DATE_TIME = "createdDateTime"
    DESCRIPTION = "description"
    DISPLAY_NAME = "displayName"
    GROUP_MEMBERSHIP_CLAIMS = "groupMembershipClaims"
    IDENTIFIER_URIS = "identifierUris"
    INFO = "info"
    IS_DEVICE_ONLY_AUTH_SUPPORTED = "isDeviceOnlyAuthSupported"
    IS_FALLBACK_PUBLIC_CLIENT = "isFallbackPublicClient"
    KEY_CREDENTIALS = "keyCredentials"
    LOGO = "logo"
    NOTES = "notes"
    OAUTH2_REQUIRE_POST_RESPONSE = "oauth2RequirePostResponse"
    OPTIONAL_CLAIMS = "optionalClaims"
    PARENTAL_CONTROL_SETTINGS = "parentalControlSettings"
    PASSWORD_CREDENTIALS = "passwordCredentials"
    PUBLIC_CLIENT = "publicClient"
    PUBLISHER_DOMAIN = "publisherDomain"
    REQUIRED_RESOURCE_ACCESS = "requiredResourceAccess"
    SIGN_IN_AUDIENCE = "signInAudience"
    TAGS = "tags"
    TOKEN_ENCRYPTION_KEY_ID = "tokenEncryptionKeyId"
    WEB = "web"
    CREATED_ON_BEHALF_OF = "createdOnBehalfOf"
    EXTENSION_PROPERTIES = "extensionProperties"
    HOME_REALM_DISCOVERY_POLICIES = "homeRealmDiscoveryPolicies"
    OWNERS = "owners"
    TOKEN_ISSUANCE_POLICIES = "tokenIssuancePolicies"
    TOKEN_LIFETIME_POLICIES = "tokenLifetimePolicies"

class Get7ItemsItem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    CREATED_ON_BEHALF_OF = "createdOnBehalfOf"
    EXTENSION_PROPERTIES = "extensionProperties"
    HOME_REALM_DISCOVERY_POLICIES = "homeRealmDiscoveryPolicies"
    OWNERS = "owners"
    TOKEN_ISSUANCE_POLICIES = "tokenIssuancePolicies"
    TOKEN_LIFETIME_POLICIES = "tokenLifetimePolicies"