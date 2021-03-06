# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import CollectionOfAndroidManagedAppProtection
    from ._models_py3 import CollectionOfDefaultManagedAppProtection
    from ._models_py3 import CollectionOfDeviceCompliancePolicyState
    from ._models_py3 import CollectionOfDeviceConfigurationState
    from ._models_py3 import CollectionOfDeviceInstallState
    from ._models_py3 import CollectionOfDeviceInstallState0
    from ._models_py3 import CollectionOfDeviceManagementTroubleshootingEvent
    from ._models_py3 import CollectionOfIosManagedAppProtection
    from ._models_py3 import CollectionOfLinksOfManagedAppRegistration
    from ._models_py3 import CollectionOfLinksOfMobileAppCategory
    from ._models_py3 import CollectionOfManagedAppOperation
    from ._models_py3 import CollectionOfManagedAppPolicy
    from ._models_py3 import CollectionOfManagedAppPolicy0
    from ._models_py3 import CollectionOfManagedAppPolicy1
    from ._models_py3 import CollectionOfManagedAppRegistration
    from ._models_py3 import CollectionOfManagedAppRegistration0
    from ._models_py3 import CollectionOfManagedAppStatus
    from ._models_py3 import CollectionOfManagedDevice
    from ._models_py3 import CollectionOfManagedDeviceMobileAppConfiguration
    from ._models_py3 import CollectionOfManagedDeviceMobileAppConfigurationAssignment
    from ._models_py3 import CollectionOfManagedDeviceMobileAppConfigurationDeviceStatus
    from ._models_py3 import CollectionOfManagedDeviceMobileAppConfigurationUserStatus
    from ._models_py3 import CollectionOfManagedEBook
    from ._models_py3 import CollectionOfManagedEBookAssignment
    from ._models_py3 import CollectionOfManagedMobileApp
    from ._models_py3 import CollectionOfManagedMobileApp0
    from ._models_py3 import CollectionOfManagedMobileApp1
    from ._models_py3 import CollectionOfManagedMobileApp2
    from ._models_py3 import CollectionOfMdmWindowsInformationProtectionPolicy
    from ._models_py3 import CollectionOfMobileApp
    from ._models_py3 import CollectionOfMobileAppAssignment
    from ._models_py3 import CollectionOfMobileAppCategory
    from ._models_py3 import CollectionOfMobileAppCategory0
    from ._models_py3 import CollectionOfTargetedManagedAppConfiguration
    from ._models_py3 import CollectionOfTargetedManagedAppPolicyAssignment
    from ._models_py3 import CollectionOfUserInstallStateSummary
    from ._models_py3 import CollectionOfVppToken
    from ._models_py3 import CollectionOfWindowsInformationProtectionPolicy
    from ._models_py3 import MicrosoftGraphAndroidManagedAppProtection
    from ._models_py3 import MicrosoftGraphConfigurationManagerClientEnabledFeatures
    from ._models_py3 import MicrosoftGraphDefaultManagedAppProtection
    from ._models_py3 import MicrosoftGraphDeviceActionResult
    from ._models_py3 import MicrosoftGraphDeviceAppManagement
    from ._models_py3 import MicrosoftGraphDeviceCategory
    from ._models_py3 import MicrosoftGraphDeviceCompliancePolicySettingState
    from ._models_py3 import MicrosoftGraphDeviceCompliancePolicyState
    from ._models_py3 import MicrosoftGraphDeviceConfigurationSettingState
    from ._models_py3 import MicrosoftGraphDeviceConfigurationState
    from ._models_py3 import MicrosoftGraphDeviceHealthAttestationState
    from ._models_py3 import MicrosoftGraphDeviceInstallState
    from ._models_py3 import MicrosoftGraphDeviceManagementTroubleshootingEvent
    from ._models_py3 import MicrosoftGraphEBookInstallSummary
    from ._models_py3 import MicrosoftGraphEntity
    from ._models_py3 import MicrosoftGraphIosManagedAppProtection
    from ._models_py3 import MicrosoftGraphKeyValuePair
    from ._models_py3 import MicrosoftGraphManagedAppConfiguration
    from ._models_py3 import MicrosoftGraphManagedAppOperation
    from ._models_py3 import MicrosoftGraphManagedAppPolicy
    from ._models_py3 import MicrosoftGraphManagedAppPolicyDeploymentSummary
    from ._models_py3 import MicrosoftGraphManagedAppPolicyDeploymentSummaryPerApp
    from ._models_py3 import MicrosoftGraphManagedAppProtection
    from ._models_py3 import MicrosoftGraphManagedAppRegistration
    from ._models_py3 import MicrosoftGraphManagedAppStatus
    from ._models_py3 import MicrosoftGraphManagedDevice
    from ._models_py3 import MicrosoftGraphManagedDeviceMobileAppConfiguration
    from ._models_py3 import MicrosoftGraphManagedDeviceMobileAppConfigurationAssignment
    from ._models_py3 import MicrosoftGraphManagedDeviceMobileAppConfigurationDeviceStatus
    from ._models_py3 import MicrosoftGraphManagedDeviceMobileAppConfigurationDeviceSummary
    from ._models_py3 import MicrosoftGraphManagedDeviceMobileAppConfigurationUserStatus
    from ._models_py3 import MicrosoftGraphManagedDeviceMobileAppConfigurationUserSummary
    from ._models_py3 import MicrosoftGraphManagedEBook
    from ._models_py3 import MicrosoftGraphManagedEBookAssignment
    from ._models_py3 import MicrosoftGraphManagedMobileApp
    from ._models_py3 import MicrosoftGraphMdmWindowsInformationProtectionPolicy
    from ._models_py3 import MicrosoftGraphMimeContent
    from ._models_py3 import MicrosoftGraphMobileApp
    from ._models_py3 import MicrosoftGraphMobileAppAssignment
    from ._models_py3 import MicrosoftGraphMobileAppCategory
    from ._models_py3 import MicrosoftGraphProxiedDomain
    from ._models_py3 import MicrosoftGraphSettingSource
    from ._models_py3 import MicrosoftGraphTargetedManagedAppConfiguration
    from ._models_py3 import MicrosoftGraphTargetedManagedAppPolicyAssignment
    from ._models_py3 import MicrosoftGraphTargetedManagedAppProtection
    from ._models_py3 import MicrosoftGraphUserInstallStateSummary
    from ._models_py3 import MicrosoftGraphVppToken
    from ._models_py3 import MicrosoftGraphWindowsInformationProtection
    from ._models_py3 import MicrosoftGraphWindowsInformationProtectionApp
    from ._models_py3 import MicrosoftGraphWindowsInformationProtectionAppLockerFile
    from ._models_py3 import MicrosoftGraphWindowsInformationProtectionDataRecoveryCertificate
    from ._models_py3 import MicrosoftGraphWindowsInformationProtectionIpRangeCollection
    from ._models_py3 import MicrosoftGraphWindowsInformationProtectionPolicy
    from ._models_py3 import MicrosoftGraphWindowsInformationProtectionProxiedDomainCollection
    from ._models_py3 import MicrosoftGraphWindowsInformationProtectionResourceCollection
    from ._models_py3 import OdataError
    from ._models_py3 import OdataErrorDetail
    from ._models_py3 import OdataErrorMain
    from ._models_py3 import Paths12NzrcrDeviceappmanagementMobileappsMobileappIdMicrosoftGraphAssignPostRequestbodyContentApplicationJsonSchema
    from ._models_py3 import Paths14Nj8OcDeviceappmanagementManagedapppoliciesManagedapppolicyIdMicrosoftGraphTargetappsPostRequestbodyContentApplicationJsonSchema
    from ._models_py3 import Paths1Mv9GnvDeviceappmanagementManagedappregistrationsManagedappregistrationIdIntendedpoliciesManagedapppolicyIdMicrosoftGraphTargetappsPostRequestbodyContentApplicationJsonSchema
    from ._models_py3 import Paths1Pwcjs5DeviceappmanagementMobileappconfigurationsManageddevicemobileappconfigurationIdMicrosoftGraphAssignPostRequestbodyContentApplicationJsonSchema
    from ._models_py3 import PathsVf2Dh9DeviceappmanagementManagedappregistrationsManagedappregistrationIdAppliedpoliciesManagedapppolicyIdMicrosoftGraphTargetappsPostRequestbodyContentApplicationJsonSchema
    from ._models_py3 import PathsWfdti0DeviceappmanagementManagedebooksManagedebookIdMicrosoftGraphAssignPostRequestbodyContentApplicationJsonSchema
    from ._models_py3 import PathsXzr66BDeviceappmanagementTargetedmanagedappconfigurationsTargetedmanagedappconfigurationIdMicrosoftGraphTargetappsPostRequestbodyContentApplicationJsonSchema
    from ._models_py3 import PathsZxn05FDeviceappmanagementTargetedmanagedappconfigurationsTargetedmanagedappconfigurationIdMicrosoftGraphAssignPostRequestbodyContentApplicationJsonSchema
except (SyntaxError, ImportError):
    from ._models import CollectionOfAndroidManagedAppProtection  # type: ignore
    from ._models import CollectionOfDefaultManagedAppProtection  # type: ignore
    from ._models import CollectionOfDeviceCompliancePolicyState  # type: ignore
    from ._models import CollectionOfDeviceConfigurationState  # type: ignore
    from ._models import CollectionOfDeviceInstallState  # type: ignore
    from ._models import CollectionOfDeviceInstallState0  # type: ignore
    from ._models import CollectionOfDeviceManagementTroubleshootingEvent  # type: ignore
    from ._models import CollectionOfIosManagedAppProtection  # type: ignore
    from ._models import CollectionOfLinksOfManagedAppRegistration  # type: ignore
    from ._models import CollectionOfLinksOfMobileAppCategory  # type: ignore
    from ._models import CollectionOfManagedAppOperation  # type: ignore
    from ._models import CollectionOfManagedAppPolicy  # type: ignore
    from ._models import CollectionOfManagedAppPolicy0  # type: ignore
    from ._models import CollectionOfManagedAppPolicy1  # type: ignore
    from ._models import CollectionOfManagedAppRegistration  # type: ignore
    from ._models import CollectionOfManagedAppRegistration0  # type: ignore
    from ._models import CollectionOfManagedAppStatus  # type: ignore
    from ._models import CollectionOfManagedDevice  # type: ignore
    from ._models import CollectionOfManagedDeviceMobileAppConfiguration  # type: ignore
    from ._models import CollectionOfManagedDeviceMobileAppConfigurationAssignment  # type: ignore
    from ._models import CollectionOfManagedDeviceMobileAppConfigurationDeviceStatus  # type: ignore
    from ._models import CollectionOfManagedDeviceMobileAppConfigurationUserStatus  # type: ignore
    from ._models import CollectionOfManagedEBook  # type: ignore
    from ._models import CollectionOfManagedEBookAssignment  # type: ignore
    from ._models import CollectionOfManagedMobileApp  # type: ignore
    from ._models import CollectionOfManagedMobileApp0  # type: ignore
    from ._models import CollectionOfManagedMobileApp1  # type: ignore
    from ._models import CollectionOfManagedMobileApp2  # type: ignore
    from ._models import CollectionOfMdmWindowsInformationProtectionPolicy  # type: ignore
    from ._models import CollectionOfMobileApp  # type: ignore
    from ._models import CollectionOfMobileAppAssignment  # type: ignore
    from ._models import CollectionOfMobileAppCategory  # type: ignore
    from ._models import CollectionOfMobileAppCategory0  # type: ignore
    from ._models import CollectionOfTargetedManagedAppConfiguration  # type: ignore
    from ._models import CollectionOfTargetedManagedAppPolicyAssignment  # type: ignore
    from ._models import CollectionOfUserInstallStateSummary  # type: ignore
    from ._models import CollectionOfVppToken  # type: ignore
    from ._models import CollectionOfWindowsInformationProtectionPolicy  # type: ignore
    from ._models import MicrosoftGraphAndroidManagedAppProtection  # type: ignore
    from ._models import MicrosoftGraphConfigurationManagerClientEnabledFeatures  # type: ignore
    from ._models import MicrosoftGraphDefaultManagedAppProtection  # type: ignore
    from ._models import MicrosoftGraphDeviceActionResult  # type: ignore
    from ._models import MicrosoftGraphDeviceAppManagement  # type: ignore
    from ._models import MicrosoftGraphDeviceCategory  # type: ignore
    from ._models import MicrosoftGraphDeviceCompliancePolicySettingState  # type: ignore
    from ._models import MicrosoftGraphDeviceCompliancePolicyState  # type: ignore
    from ._models import MicrosoftGraphDeviceConfigurationSettingState  # type: ignore
    from ._models import MicrosoftGraphDeviceConfigurationState  # type: ignore
    from ._models import MicrosoftGraphDeviceHealthAttestationState  # type: ignore
    from ._models import MicrosoftGraphDeviceInstallState  # type: ignore
    from ._models import MicrosoftGraphDeviceManagementTroubleshootingEvent  # type: ignore
    from ._models import MicrosoftGraphEBookInstallSummary  # type: ignore
    from ._models import MicrosoftGraphEntity  # type: ignore
    from ._models import MicrosoftGraphIosManagedAppProtection  # type: ignore
    from ._models import MicrosoftGraphKeyValuePair  # type: ignore
    from ._models import MicrosoftGraphManagedAppConfiguration  # type: ignore
    from ._models import MicrosoftGraphManagedAppOperation  # type: ignore
    from ._models import MicrosoftGraphManagedAppPolicy  # type: ignore
    from ._models import MicrosoftGraphManagedAppPolicyDeploymentSummary  # type: ignore
    from ._models import MicrosoftGraphManagedAppPolicyDeploymentSummaryPerApp  # type: ignore
    from ._models import MicrosoftGraphManagedAppProtection  # type: ignore
    from ._models import MicrosoftGraphManagedAppRegistration  # type: ignore
    from ._models import MicrosoftGraphManagedAppStatus  # type: ignore
    from ._models import MicrosoftGraphManagedDevice  # type: ignore
    from ._models import MicrosoftGraphManagedDeviceMobileAppConfiguration  # type: ignore
    from ._models import MicrosoftGraphManagedDeviceMobileAppConfigurationAssignment  # type: ignore
    from ._models import MicrosoftGraphManagedDeviceMobileAppConfigurationDeviceStatus  # type: ignore
    from ._models import MicrosoftGraphManagedDeviceMobileAppConfigurationDeviceSummary  # type: ignore
    from ._models import MicrosoftGraphManagedDeviceMobileAppConfigurationUserStatus  # type: ignore
    from ._models import MicrosoftGraphManagedDeviceMobileAppConfigurationUserSummary  # type: ignore
    from ._models import MicrosoftGraphManagedEBook  # type: ignore
    from ._models import MicrosoftGraphManagedEBookAssignment  # type: ignore
    from ._models import MicrosoftGraphManagedMobileApp  # type: ignore
    from ._models import MicrosoftGraphMdmWindowsInformationProtectionPolicy  # type: ignore
    from ._models import MicrosoftGraphMimeContent  # type: ignore
    from ._models import MicrosoftGraphMobileApp  # type: ignore
    from ._models import MicrosoftGraphMobileAppAssignment  # type: ignore
    from ._models import MicrosoftGraphMobileAppCategory  # type: ignore
    from ._models import MicrosoftGraphProxiedDomain  # type: ignore
    from ._models import MicrosoftGraphSettingSource  # type: ignore
    from ._models import MicrosoftGraphTargetedManagedAppConfiguration  # type: ignore
    from ._models import MicrosoftGraphTargetedManagedAppPolicyAssignment  # type: ignore
    from ._models import MicrosoftGraphTargetedManagedAppProtection  # type: ignore
    from ._models import MicrosoftGraphUserInstallStateSummary  # type: ignore
    from ._models import MicrosoftGraphVppToken  # type: ignore
    from ._models import MicrosoftGraphWindowsInformationProtection  # type: ignore
    from ._models import MicrosoftGraphWindowsInformationProtectionApp  # type: ignore
    from ._models import MicrosoftGraphWindowsInformationProtectionAppLockerFile  # type: ignore
    from ._models import MicrosoftGraphWindowsInformationProtectionDataRecoveryCertificate  # type: ignore
    from ._models import MicrosoftGraphWindowsInformationProtectionIpRangeCollection  # type: ignore
    from ._models import MicrosoftGraphWindowsInformationProtectionPolicy  # type: ignore
    from ._models import MicrosoftGraphWindowsInformationProtectionProxiedDomainCollection  # type: ignore
    from ._models import MicrosoftGraphWindowsInformationProtectionResourceCollection  # type: ignore
    from ._models import OdataError  # type: ignore
    from ._models import OdataErrorDetail  # type: ignore
    from ._models import OdataErrorMain  # type: ignore
    from ._models import Paths12NzrcrDeviceappmanagementMobileappsMobileappIdMicrosoftGraphAssignPostRequestbodyContentApplicationJsonSchema  # type: ignore
    from ._models import Paths14Nj8OcDeviceappmanagementManagedapppoliciesManagedapppolicyIdMicrosoftGraphTargetappsPostRequestbodyContentApplicationJsonSchema  # type: ignore
    from ._models import Paths1Mv9GnvDeviceappmanagementManagedappregistrationsManagedappregistrationIdIntendedpoliciesManagedapppolicyIdMicrosoftGraphTargetappsPostRequestbodyContentApplicationJsonSchema  # type: ignore
    from ._models import Paths1Pwcjs5DeviceappmanagementMobileappconfigurationsManageddevicemobileappconfigurationIdMicrosoftGraphAssignPostRequestbodyContentApplicationJsonSchema  # type: ignore
    from ._models import PathsVf2Dh9DeviceappmanagementManagedappregistrationsManagedappregistrationIdAppliedpoliciesManagedapppolicyIdMicrosoftGraphTargetappsPostRequestbodyContentApplicationJsonSchema  # type: ignore
    from ._models import PathsWfdti0DeviceappmanagementManagedebooksManagedebookIdMicrosoftGraphAssignPostRequestbodyContentApplicationJsonSchema  # type: ignore
    from ._models import PathsXzr66BDeviceappmanagementTargetedmanagedappconfigurationsTargetedmanagedappconfigurationIdMicrosoftGraphTargetappsPostRequestbodyContentApplicationJsonSchema  # type: ignore
    from ._models import PathsZxn05FDeviceappmanagementTargetedmanagedappconfigurationsTargetedmanagedappconfigurationIdMicrosoftGraphAssignPostRequestbodyContentApplicationJsonSchema  # type: ignore

from ._devices_corporate_management_enums import (
    Enum100,
    Enum101,
    Enum102,
    Enum103,
    Enum104,
    Enum105,
    Enum106,
    Enum107,
    Enum108,
    Enum109,
    Enum110,
    Enum111,
    Enum112,
    Enum113,
    Enum114,
    Enum115,
    Enum116,
    Enum117,
    Enum118,
    Enum119,
    Enum120,
    Enum121,
    Enum122,
    Enum123,
    Enum124,
    Enum125,
    Enum126,
    Enum127,
    Enum128,
    Enum129,
    Enum130,
    Enum131,
    Enum132,
    Enum133,
    Enum134,
    Enum135,
    Enum136,
    Enum137,
    Enum138,
    Enum139,
    Enum140,
    Enum141,
    Enum142,
    Enum143,
    Enum144,
    Enum145,
    Enum146,
    Enum147,
    Enum148,
    Enum149,
    Enum160,
    Enum161,
    Enum162,
    Enum163,
    Enum164,
    Enum165,
    Enum166,
    Enum167,
    Enum168,
    Enum21,
    Enum23,
    Enum24,
    Enum25,
    Enum26,
    Enum27,
    Enum28,
    Enum29,
    Enum30,
    Enum31,
    Enum32,
    Enum33,
    Enum34,
    Enum35,
    Enum36,
    Enum37,
    Enum38,
    Enum39,
    Enum40,
    Enum41,
    Enum42,
    Enum43,
    Enum44,
    Enum45,
    Enum46,
    Enum47,
    Enum48,
    Enum49,
    Enum50,
    Enum51,
    Enum52,
    Enum53,
    Enum54,
    Enum55,
    Enum56,
    Enum57,
    Enum58,
    Enum59,
    Enum60,
    Enum61,
    Enum62,
    Enum63,
    Enum64,
    Enum65,
    Enum66,
    Enum67,
    Enum68,
    Enum69,
    Enum70,
    Enum71,
    Enum72,
    Enum73,
    Enum74,
    Enum75,
    Enum76,
    Enum77,
    Enum78,
    Enum79,
    Enum80,
    Enum81,
    Enum82,
    Enum83,
    Enum84,
    Enum85,
    Enum86,
    Enum87,
    Enum88,
    Enum89,
    Enum90,
    Enum91,
    Enum92,
    Enum93,
    Enum94,
    Enum95,
    Enum96,
    Enum97,
    Enum98,
    Enum99,
    Get0ItemsItem,
    Get1ItemsItem,
    Get2ItemsItem,
    Get5ItemsItem,
    Get6ItemsItem,
    Get7ItemsItem,
    MicrosoftGraphActionState,
    MicrosoftGraphComplianceState,
    MicrosoftGraphComplianceStatus,
    MicrosoftGraphDeviceEnrollmentType,
    MicrosoftGraphDeviceManagementExchangeAccessState,
    MicrosoftGraphDeviceManagementExchangeAccessStateReason,
    MicrosoftGraphDeviceRegistrationState,
    MicrosoftGraphInstallIntent,
    MicrosoftGraphInstallState,
    MicrosoftGraphManagedAppClipboardSharingLevel,
    MicrosoftGraphManagedAppDataEncryptionType,
    MicrosoftGraphManagedAppDataStorageLocation,
    MicrosoftGraphManagedAppDataTransferLevel,
    MicrosoftGraphManagedAppFlaggedReason,
    MicrosoftGraphManagedAppPinCharacterSet,
    MicrosoftGraphManagedBrowserType,
    MicrosoftGraphManagedDeviceOwnerType,
    MicrosoftGraphManagedDevicePartnerReportedHealthState,
    MicrosoftGraphManagementAgentType,
    MicrosoftGraphMobileAppPublishingState,
    MicrosoftGraphPolicyPlatformType,
    MicrosoftGraphVppTokenAccountType,
    MicrosoftGraphVppTokenState,
    MicrosoftGraphVppTokenSyncStatus,
    MicrosoftGraphWindowsInformationProtectionEnforcementLevel,
    MicrosoftGraphWindowsInformationProtectionPinCharacterRequirements,
)

__all__ = [
    'CollectionOfAndroidManagedAppProtection',
    'CollectionOfDefaultManagedAppProtection',
    'CollectionOfDeviceCompliancePolicyState',
    'CollectionOfDeviceConfigurationState',
    'CollectionOfDeviceInstallState',
    'CollectionOfDeviceInstallState0',
    'CollectionOfDeviceManagementTroubleshootingEvent',
    'CollectionOfIosManagedAppProtection',
    'CollectionOfLinksOfManagedAppRegistration',
    'CollectionOfLinksOfMobileAppCategory',
    'CollectionOfManagedAppOperation',
    'CollectionOfManagedAppPolicy',
    'CollectionOfManagedAppPolicy0',
    'CollectionOfManagedAppPolicy1',
    'CollectionOfManagedAppRegistration',
    'CollectionOfManagedAppRegistration0',
    'CollectionOfManagedAppStatus',
    'CollectionOfManagedDevice',
    'CollectionOfManagedDeviceMobileAppConfiguration',
    'CollectionOfManagedDeviceMobileAppConfigurationAssignment',
    'CollectionOfManagedDeviceMobileAppConfigurationDeviceStatus',
    'CollectionOfManagedDeviceMobileAppConfigurationUserStatus',
    'CollectionOfManagedEBook',
    'CollectionOfManagedEBookAssignment',
    'CollectionOfManagedMobileApp',
    'CollectionOfManagedMobileApp0',
    'CollectionOfManagedMobileApp1',
    'CollectionOfManagedMobileApp2',
    'CollectionOfMdmWindowsInformationProtectionPolicy',
    'CollectionOfMobileApp',
    'CollectionOfMobileAppAssignment',
    'CollectionOfMobileAppCategory',
    'CollectionOfMobileAppCategory0',
    'CollectionOfTargetedManagedAppConfiguration',
    'CollectionOfTargetedManagedAppPolicyAssignment',
    'CollectionOfUserInstallStateSummary',
    'CollectionOfVppToken',
    'CollectionOfWindowsInformationProtectionPolicy',
    'MicrosoftGraphAndroidManagedAppProtection',
    'MicrosoftGraphConfigurationManagerClientEnabledFeatures',
    'MicrosoftGraphDefaultManagedAppProtection',
    'MicrosoftGraphDeviceActionResult',
    'MicrosoftGraphDeviceAppManagement',
    'MicrosoftGraphDeviceCategory',
    'MicrosoftGraphDeviceCompliancePolicySettingState',
    'MicrosoftGraphDeviceCompliancePolicyState',
    'MicrosoftGraphDeviceConfigurationSettingState',
    'MicrosoftGraphDeviceConfigurationState',
    'MicrosoftGraphDeviceHealthAttestationState',
    'MicrosoftGraphDeviceInstallState',
    'MicrosoftGraphDeviceManagementTroubleshootingEvent',
    'MicrosoftGraphEBookInstallSummary',
    'MicrosoftGraphEntity',
    'MicrosoftGraphIosManagedAppProtection',
    'MicrosoftGraphKeyValuePair',
    'MicrosoftGraphManagedAppConfiguration',
    'MicrosoftGraphManagedAppOperation',
    'MicrosoftGraphManagedAppPolicy',
    'MicrosoftGraphManagedAppPolicyDeploymentSummary',
    'MicrosoftGraphManagedAppPolicyDeploymentSummaryPerApp',
    'MicrosoftGraphManagedAppProtection',
    'MicrosoftGraphManagedAppRegistration',
    'MicrosoftGraphManagedAppStatus',
    'MicrosoftGraphManagedDevice',
    'MicrosoftGraphManagedDeviceMobileAppConfiguration',
    'MicrosoftGraphManagedDeviceMobileAppConfigurationAssignment',
    'MicrosoftGraphManagedDeviceMobileAppConfigurationDeviceStatus',
    'MicrosoftGraphManagedDeviceMobileAppConfigurationDeviceSummary',
    'MicrosoftGraphManagedDeviceMobileAppConfigurationUserStatus',
    'MicrosoftGraphManagedDeviceMobileAppConfigurationUserSummary',
    'MicrosoftGraphManagedEBook',
    'MicrosoftGraphManagedEBookAssignment',
    'MicrosoftGraphManagedMobileApp',
    'MicrosoftGraphMdmWindowsInformationProtectionPolicy',
    'MicrosoftGraphMimeContent',
    'MicrosoftGraphMobileApp',
    'MicrosoftGraphMobileAppAssignment',
    'MicrosoftGraphMobileAppCategory',
    'MicrosoftGraphProxiedDomain',
    'MicrosoftGraphSettingSource',
    'MicrosoftGraphTargetedManagedAppConfiguration',
    'MicrosoftGraphTargetedManagedAppPolicyAssignment',
    'MicrosoftGraphTargetedManagedAppProtection',
    'MicrosoftGraphUserInstallStateSummary',
    'MicrosoftGraphVppToken',
    'MicrosoftGraphWindowsInformationProtection',
    'MicrosoftGraphWindowsInformationProtectionApp',
    'MicrosoftGraphWindowsInformationProtectionAppLockerFile',
    'MicrosoftGraphWindowsInformationProtectionDataRecoveryCertificate',
    'MicrosoftGraphWindowsInformationProtectionIpRangeCollection',
    'MicrosoftGraphWindowsInformationProtectionPolicy',
    'MicrosoftGraphWindowsInformationProtectionProxiedDomainCollection',
    'MicrosoftGraphWindowsInformationProtectionResourceCollection',
    'OdataError',
    'OdataErrorDetail',
    'OdataErrorMain',
    'Paths12NzrcrDeviceappmanagementMobileappsMobileappIdMicrosoftGraphAssignPostRequestbodyContentApplicationJsonSchema',
    'Paths14Nj8OcDeviceappmanagementManagedapppoliciesManagedapppolicyIdMicrosoftGraphTargetappsPostRequestbodyContentApplicationJsonSchema',
    'Paths1Mv9GnvDeviceappmanagementManagedappregistrationsManagedappregistrationIdIntendedpoliciesManagedapppolicyIdMicrosoftGraphTargetappsPostRequestbodyContentApplicationJsonSchema',
    'Paths1Pwcjs5DeviceappmanagementMobileappconfigurationsManageddevicemobileappconfigurationIdMicrosoftGraphAssignPostRequestbodyContentApplicationJsonSchema',
    'PathsVf2Dh9DeviceappmanagementManagedappregistrationsManagedappregistrationIdAppliedpoliciesManagedapppolicyIdMicrosoftGraphTargetappsPostRequestbodyContentApplicationJsonSchema',
    'PathsWfdti0DeviceappmanagementManagedebooksManagedebookIdMicrosoftGraphAssignPostRequestbodyContentApplicationJsonSchema',
    'PathsXzr66BDeviceappmanagementTargetedmanagedappconfigurationsTargetedmanagedappconfigurationIdMicrosoftGraphTargetappsPostRequestbodyContentApplicationJsonSchema',
    'PathsZxn05FDeviceappmanagementTargetedmanagedappconfigurationsTargetedmanagedappconfigurationIdMicrosoftGraphAssignPostRequestbodyContentApplicationJsonSchema',
    'Enum100',
    'Enum101',
    'Enum102',
    'Enum103',
    'Enum104',
    'Enum105',
    'Enum106',
    'Enum107',
    'Enum108',
    'Enum109',
    'Enum110',
    'Enum111',
    'Enum112',
    'Enum113',
    'Enum114',
    'Enum115',
    'Enum116',
    'Enum117',
    'Enum118',
    'Enum119',
    'Enum120',
    'Enum121',
    'Enum122',
    'Enum123',
    'Enum124',
    'Enum125',
    'Enum126',
    'Enum127',
    'Enum128',
    'Enum129',
    'Enum130',
    'Enum131',
    'Enum132',
    'Enum133',
    'Enum134',
    'Enum135',
    'Enum136',
    'Enum137',
    'Enum138',
    'Enum139',
    'Enum140',
    'Enum141',
    'Enum142',
    'Enum143',
    'Enum144',
    'Enum145',
    'Enum146',
    'Enum147',
    'Enum148',
    'Enum149',
    'Enum160',
    'Enum161',
    'Enum162',
    'Enum163',
    'Enum164',
    'Enum165',
    'Enum166',
    'Enum167',
    'Enum168',
    'Enum21',
    'Enum23',
    'Enum24',
    'Enum25',
    'Enum26',
    'Enum27',
    'Enum28',
    'Enum29',
    'Enum30',
    'Enum31',
    'Enum32',
    'Enum33',
    'Enum34',
    'Enum35',
    'Enum36',
    'Enum37',
    'Enum38',
    'Enum39',
    'Enum40',
    'Enum41',
    'Enum42',
    'Enum43',
    'Enum44',
    'Enum45',
    'Enum46',
    'Enum47',
    'Enum48',
    'Enum49',
    'Enum50',
    'Enum51',
    'Enum52',
    'Enum53',
    'Enum54',
    'Enum55',
    'Enum56',
    'Enum57',
    'Enum58',
    'Enum59',
    'Enum60',
    'Enum61',
    'Enum62',
    'Enum63',
    'Enum64',
    'Enum65',
    'Enum66',
    'Enum67',
    'Enum68',
    'Enum69',
    'Enum70',
    'Enum71',
    'Enum72',
    'Enum73',
    'Enum74',
    'Enum75',
    'Enum76',
    'Enum77',
    'Enum78',
    'Enum79',
    'Enum80',
    'Enum81',
    'Enum82',
    'Enum83',
    'Enum84',
    'Enum85',
    'Enum86',
    'Enum87',
    'Enum88',
    'Enum89',
    'Enum90',
    'Enum91',
    'Enum92',
    'Enum93',
    'Enum94',
    'Enum95',
    'Enum96',
    'Enum97',
    'Enum98',
    'Enum99',
    'Get0ItemsItem',
    'Get1ItemsItem',
    'Get2ItemsItem',
    'Get5ItemsItem',
    'Get6ItemsItem',
    'Get7ItemsItem',
    'MicrosoftGraphActionState',
    'MicrosoftGraphComplianceState',
    'MicrosoftGraphComplianceStatus',
    'MicrosoftGraphDeviceEnrollmentType',
    'MicrosoftGraphDeviceManagementExchangeAccessState',
    'MicrosoftGraphDeviceManagementExchangeAccessStateReason',
    'MicrosoftGraphDeviceRegistrationState',
    'MicrosoftGraphInstallIntent',
    'MicrosoftGraphInstallState',
    'MicrosoftGraphManagedAppClipboardSharingLevel',
    'MicrosoftGraphManagedAppDataEncryptionType',
    'MicrosoftGraphManagedAppDataStorageLocation',
    'MicrosoftGraphManagedAppDataTransferLevel',
    'MicrosoftGraphManagedAppFlaggedReason',
    'MicrosoftGraphManagedAppPinCharacterSet',
    'MicrosoftGraphManagedBrowserType',
    'MicrosoftGraphManagedDeviceOwnerType',
    'MicrosoftGraphManagedDevicePartnerReportedHealthState',
    'MicrosoftGraphManagementAgentType',
    'MicrosoftGraphMobileAppPublishingState',
    'MicrosoftGraphPolicyPlatformType',
    'MicrosoftGraphVppTokenAccountType',
    'MicrosoftGraphVppTokenState',
    'MicrosoftGraphVppTokenSyncStatus',
    'MicrosoftGraphWindowsInformationProtectionEnforcementLevel',
    'MicrosoftGraphWindowsInformationProtectionPinCharacterRequirements',
]
