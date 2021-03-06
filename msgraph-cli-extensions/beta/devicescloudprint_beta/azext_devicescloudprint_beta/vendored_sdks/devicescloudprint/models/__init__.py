# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import CollectionOfLinksOfPrintConnector
    from ._models_py3 import CollectionOfLinksOfPrinterShare
    from ._models_py3 import CollectionOfPrintConnector
    from ._models_py3 import CollectionOfPrintConnector0
    from ._models_py3 import CollectionOfPrintIdentity
    from ._models_py3 import CollectionOfPrintIdentity0
    from ._models_py3 import CollectionOfPrintIdentity1
    from ._models_py3 import CollectionOfPrintOperation
    from ._models_py3 import CollectionOfPrintService
    from ._models_py3 import CollectionOfPrintServiceEndpoint
    from ._models_py3 import CollectionOfPrintTask
    from ._models_py3 import CollectionOfPrintTaskDefinition
    from ._models_py3 import CollectionOfPrintTaskTrigger
    from ._models_py3 import CollectionOfPrintUserIdentity
    from ._models_py3 import CollectionOfPrintUserIdentity0
    from ._models_py3 import CollectionOfPrintUserIdentity1
    from ._models_py3 import CollectionOfPrinter
    from ._models_py3 import CollectionOfPrinterShare
    from ._models_py3 import CollectionOfPrinterShare0
    from ._models_py3 import CollectionOfPrinterShare1
    from ._models_py3 import CollectionOfReportRoot
    from ._models_py3 import MicrosoftGraphAppIdentity
    from ._models_py3 import MicrosoftGraphApplicationSignInDetailedSummary
    from ._models_py3 import MicrosoftGraphArchivedPrintJob
    from ._models_py3 import MicrosoftGraphCredentialUserRegistrationDetails
    from ._models_py3 import MicrosoftGraphDeviceHealth
    from ._models_py3 import MicrosoftGraphDirectoryObject
    from ._models_py3 import MicrosoftGraphEntity
    from ._models_py3 import MicrosoftGraphGroupPrintUsageSummary
    from ._models_py3 import MicrosoftGraphIdentity
    from ._models_py3 import MicrosoftGraphIntegerRange
    from ._models_py3 import MicrosoftGraphOverallPrintUsageSummary
    from ._models_py3 import MicrosoftGraphPrint
    from ._models_py3 import MicrosoftGraphPrintCertificateSigningRequest
    from ._models_py3 import MicrosoftGraphPrintConnector
    from ._models_py3 import MicrosoftGraphPrintDocument
    from ._models_py3 import MicrosoftGraphPrintIdentity
    from ._models_py3 import MicrosoftGraphPrintJob
    from ._models_py3 import MicrosoftGraphPrintJobConfiguration
    from ._models_py3 import MicrosoftGraphPrintJobStatus
    from ._models_py3 import MicrosoftGraphPrintMargin
    from ._models_py3 import MicrosoftGraphPrintOperation
    from ._models_py3 import MicrosoftGraphPrintOperationStatus
    from ._models_py3 import MicrosoftGraphPrintService
    from ._models_py3 import MicrosoftGraphPrintServiceEndpoint
    from ._models_py3 import MicrosoftGraphPrintSettings
    from ._models_py3 import MicrosoftGraphPrintTask
    from ._models_py3 import MicrosoftGraphPrintTaskDefinition
    from ._models_py3 import MicrosoftGraphPrintTaskStatus
    from ._models_py3 import MicrosoftGraphPrintTaskTrigger
    from ._models_py3 import MicrosoftGraphPrintUsageSummary
    from ._models_py3 import MicrosoftGraphPrintUsageSummaryByPrinter
    from ._models_py3 import MicrosoftGraphPrintUsageSummaryByUser
    from ._models_py3 import MicrosoftGraphPrintUserIdentity
    from ._models_py3 import MicrosoftGraphPrinter
    from ._models_py3 import MicrosoftGraphPrinterBase
    from ._models_py3 import MicrosoftGraphPrinterCapabilities
    from ._models_py3 import MicrosoftGraphPrinterDefaults
    from ._models_py3 import MicrosoftGraphPrinterDocumentConfiguration
    from ._models_py3 import MicrosoftGraphPrinterLocation
    from ._models_py3 import MicrosoftGraphPrinterShare
    from ._models_py3 import MicrosoftGraphPrinterStatus
    from ._models_py3 import MicrosoftGraphPrinterUsageSummary
    from ._models_py3 import MicrosoftGraphReportRoot
    from ._models_py3 import MicrosoftGraphSignInStatus
    from ._models_py3 import MicrosoftGraphUserCredentialUsageDetails
    from ._models_py3 import MicrosoftGraphUserIdentity
    from ._models_py3 import MicrosoftGraphUserPrintUsageSummary
    from ._models_py3 import OdataError
    from ._models_py3 import OdataErrorDetail
    from ._models_py3 import OdataErrorMain
    from ._models_py3 import Paths18VwyqhPrintPrintersMicrosoftGraphCreatePostRequestbodyContentApplicationJsonSchema
except (SyntaxError, ImportError):
    from ._models import CollectionOfLinksOfPrintConnector  # type: ignore
    from ._models import CollectionOfLinksOfPrinterShare  # type: ignore
    from ._models import CollectionOfPrintConnector  # type: ignore
    from ._models import CollectionOfPrintConnector0  # type: ignore
    from ._models import CollectionOfPrintIdentity  # type: ignore
    from ._models import CollectionOfPrintIdentity0  # type: ignore
    from ._models import CollectionOfPrintIdentity1  # type: ignore
    from ._models import CollectionOfPrintOperation  # type: ignore
    from ._models import CollectionOfPrintService  # type: ignore
    from ._models import CollectionOfPrintServiceEndpoint  # type: ignore
    from ._models import CollectionOfPrintTask  # type: ignore
    from ._models import CollectionOfPrintTaskDefinition  # type: ignore
    from ._models import CollectionOfPrintTaskTrigger  # type: ignore
    from ._models import CollectionOfPrintUserIdentity  # type: ignore
    from ._models import CollectionOfPrintUserIdentity0  # type: ignore
    from ._models import CollectionOfPrintUserIdentity1  # type: ignore
    from ._models import CollectionOfPrinter  # type: ignore
    from ._models import CollectionOfPrinterShare  # type: ignore
    from ._models import CollectionOfPrinterShare0  # type: ignore
    from ._models import CollectionOfPrinterShare1  # type: ignore
    from ._models import CollectionOfReportRoot  # type: ignore
    from ._models import MicrosoftGraphAppIdentity  # type: ignore
    from ._models import MicrosoftGraphApplicationSignInDetailedSummary  # type: ignore
    from ._models import MicrosoftGraphArchivedPrintJob  # type: ignore
    from ._models import MicrosoftGraphCredentialUserRegistrationDetails  # type: ignore
    from ._models import MicrosoftGraphDeviceHealth  # type: ignore
    from ._models import MicrosoftGraphDirectoryObject  # type: ignore
    from ._models import MicrosoftGraphEntity  # type: ignore
    from ._models import MicrosoftGraphGroupPrintUsageSummary  # type: ignore
    from ._models import MicrosoftGraphIdentity  # type: ignore
    from ._models import MicrosoftGraphIntegerRange  # type: ignore
    from ._models import MicrosoftGraphOverallPrintUsageSummary  # type: ignore
    from ._models import MicrosoftGraphPrint  # type: ignore
    from ._models import MicrosoftGraphPrintCertificateSigningRequest  # type: ignore
    from ._models import MicrosoftGraphPrintConnector  # type: ignore
    from ._models import MicrosoftGraphPrintDocument  # type: ignore
    from ._models import MicrosoftGraphPrintIdentity  # type: ignore
    from ._models import MicrosoftGraphPrintJob  # type: ignore
    from ._models import MicrosoftGraphPrintJobConfiguration  # type: ignore
    from ._models import MicrosoftGraphPrintJobStatus  # type: ignore
    from ._models import MicrosoftGraphPrintMargin  # type: ignore
    from ._models import MicrosoftGraphPrintOperation  # type: ignore
    from ._models import MicrosoftGraphPrintOperationStatus  # type: ignore
    from ._models import MicrosoftGraphPrintService  # type: ignore
    from ._models import MicrosoftGraphPrintServiceEndpoint  # type: ignore
    from ._models import MicrosoftGraphPrintSettings  # type: ignore
    from ._models import MicrosoftGraphPrintTask  # type: ignore
    from ._models import MicrosoftGraphPrintTaskDefinition  # type: ignore
    from ._models import MicrosoftGraphPrintTaskStatus  # type: ignore
    from ._models import MicrosoftGraphPrintTaskTrigger  # type: ignore
    from ._models import MicrosoftGraphPrintUsageSummary  # type: ignore
    from ._models import MicrosoftGraphPrintUsageSummaryByPrinter  # type: ignore
    from ._models import MicrosoftGraphPrintUsageSummaryByUser  # type: ignore
    from ._models import MicrosoftGraphPrintUserIdentity  # type: ignore
    from ._models import MicrosoftGraphPrinter  # type: ignore
    from ._models import MicrosoftGraphPrinterBase  # type: ignore
    from ._models import MicrosoftGraphPrinterCapabilities  # type: ignore
    from ._models import MicrosoftGraphPrinterDefaults  # type: ignore
    from ._models import MicrosoftGraphPrinterDocumentConfiguration  # type: ignore
    from ._models import MicrosoftGraphPrinterLocation  # type: ignore
    from ._models import MicrosoftGraphPrinterShare  # type: ignore
    from ._models import MicrosoftGraphPrinterStatus  # type: ignore
    from ._models import MicrosoftGraphPrinterUsageSummary  # type: ignore
    from ._models import MicrosoftGraphReportRoot  # type: ignore
    from ._models import MicrosoftGraphSignInStatus  # type: ignore
    from ._models import MicrosoftGraphUserCredentialUsageDetails  # type: ignore
    from ._models import MicrosoftGraphUserIdentity  # type: ignore
    from ._models import MicrosoftGraphUserPrintUsageSummary  # type: ignore
    from ._models import OdataError  # type: ignore
    from ._models import OdataErrorDetail  # type: ignore
    from ._models import OdataErrorMain  # type: ignore
    from ._models import Paths18VwyqhPrintPrintersMicrosoftGraphCreatePostRequestbodyContentApplicationJsonSchema  # type: ignore

from ._devices_cloud_print_enums import (
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
    Get5ItemsItem,
    Get6ItemsItem,
    MicrosoftGraphFeatureType,
    MicrosoftGraphPrintColorConfiguration,
    MicrosoftGraphPrintColorMode,
    MicrosoftGraphPrintDuplexConfiguration,
    MicrosoftGraphPrintDuplexMode,
    MicrosoftGraphPrintEvent,
    MicrosoftGraphPrintFinishing,
    MicrosoftGraphPrintJobProcessingState,
    MicrosoftGraphPrintJobStateDetail,
    MicrosoftGraphPrintMediaType,
    MicrosoftGraphPrintMultipageLayout,
    MicrosoftGraphPrintOperationProcessingState,
    MicrosoftGraphPrintOrientation,
    MicrosoftGraphPrintPresentationDirection,
    MicrosoftGraphPrintQuality,
    MicrosoftGraphPrintScaling,
    MicrosoftGraphPrintTaskProcessingState,
    MicrosoftGraphPrinterFeedDirection,
    MicrosoftGraphPrinterFeedOrientation,
    MicrosoftGraphPrinterProcessingState,
    MicrosoftGraphPrinterProcessingStateDetail,
    MicrosoftGraphPrinterProcessingStateReason,
    MicrosoftGraphRegistrationAuthMethod,
    MicrosoftGraphUsageAuthMethod,
)

__all__ = [
    'CollectionOfLinksOfPrintConnector',
    'CollectionOfLinksOfPrinterShare',
    'CollectionOfPrintConnector',
    'CollectionOfPrintConnector0',
    'CollectionOfPrintIdentity',
    'CollectionOfPrintIdentity0',
    'CollectionOfPrintIdentity1',
    'CollectionOfPrintOperation',
    'CollectionOfPrintService',
    'CollectionOfPrintServiceEndpoint',
    'CollectionOfPrintTask',
    'CollectionOfPrintTaskDefinition',
    'CollectionOfPrintTaskTrigger',
    'CollectionOfPrintUserIdentity',
    'CollectionOfPrintUserIdentity0',
    'CollectionOfPrintUserIdentity1',
    'CollectionOfPrinter',
    'CollectionOfPrinterShare',
    'CollectionOfPrinterShare0',
    'CollectionOfPrinterShare1',
    'CollectionOfReportRoot',
    'MicrosoftGraphAppIdentity',
    'MicrosoftGraphApplicationSignInDetailedSummary',
    'MicrosoftGraphArchivedPrintJob',
    'MicrosoftGraphCredentialUserRegistrationDetails',
    'MicrosoftGraphDeviceHealth',
    'MicrosoftGraphDirectoryObject',
    'MicrosoftGraphEntity',
    'MicrosoftGraphGroupPrintUsageSummary',
    'MicrosoftGraphIdentity',
    'MicrosoftGraphIntegerRange',
    'MicrosoftGraphOverallPrintUsageSummary',
    'MicrosoftGraphPrint',
    'MicrosoftGraphPrintCertificateSigningRequest',
    'MicrosoftGraphPrintConnector',
    'MicrosoftGraphPrintDocument',
    'MicrosoftGraphPrintIdentity',
    'MicrosoftGraphPrintJob',
    'MicrosoftGraphPrintJobConfiguration',
    'MicrosoftGraphPrintJobStatus',
    'MicrosoftGraphPrintMargin',
    'MicrosoftGraphPrintOperation',
    'MicrosoftGraphPrintOperationStatus',
    'MicrosoftGraphPrintService',
    'MicrosoftGraphPrintServiceEndpoint',
    'MicrosoftGraphPrintSettings',
    'MicrosoftGraphPrintTask',
    'MicrosoftGraphPrintTaskDefinition',
    'MicrosoftGraphPrintTaskStatus',
    'MicrosoftGraphPrintTaskTrigger',
    'MicrosoftGraphPrintUsageSummary',
    'MicrosoftGraphPrintUsageSummaryByPrinter',
    'MicrosoftGraphPrintUsageSummaryByUser',
    'MicrosoftGraphPrintUserIdentity',
    'MicrosoftGraphPrinter',
    'MicrosoftGraphPrinterBase',
    'MicrosoftGraphPrinterCapabilities',
    'MicrosoftGraphPrinterDefaults',
    'MicrosoftGraphPrinterDocumentConfiguration',
    'MicrosoftGraphPrinterLocation',
    'MicrosoftGraphPrinterShare',
    'MicrosoftGraphPrinterStatus',
    'MicrosoftGraphPrinterUsageSummary',
    'MicrosoftGraphReportRoot',
    'MicrosoftGraphSignInStatus',
    'MicrosoftGraphUserCredentialUsageDetails',
    'MicrosoftGraphUserIdentity',
    'MicrosoftGraphUserPrintUsageSummary',
    'OdataError',
    'OdataErrorDetail',
    'OdataErrorMain',
    'Paths18VwyqhPrintPrintersMicrosoftGraphCreatePostRequestbodyContentApplicationJsonSchema',
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
    'Get5ItemsItem',
    'Get6ItemsItem',
    'MicrosoftGraphFeatureType',
    'MicrosoftGraphPrintColorConfiguration',
    'MicrosoftGraphPrintColorMode',
    'MicrosoftGraphPrintDuplexConfiguration',
    'MicrosoftGraphPrintDuplexMode',
    'MicrosoftGraphPrintEvent',
    'MicrosoftGraphPrintFinishing',
    'MicrosoftGraphPrintJobProcessingState',
    'MicrosoftGraphPrintJobStateDetail',
    'MicrosoftGraphPrintMediaType',
    'MicrosoftGraphPrintMultipageLayout',
    'MicrosoftGraphPrintOperationProcessingState',
    'MicrosoftGraphPrintOrientation',
    'MicrosoftGraphPrintPresentationDirection',
    'MicrosoftGraphPrintQuality',
    'MicrosoftGraphPrintScaling',
    'MicrosoftGraphPrintTaskProcessingState',
    'MicrosoftGraphPrinterFeedDirection',
    'MicrosoftGraphPrinterFeedOrientation',
    'MicrosoftGraphPrinterProcessingState',
    'MicrosoftGraphPrinterProcessingStateDetail',
    'MicrosoftGraphPrinterProcessingStateReason',
    'MicrosoftGraphRegistrationAuthMethod',
    'MicrosoftGraphUsageAuthMethod',
]
