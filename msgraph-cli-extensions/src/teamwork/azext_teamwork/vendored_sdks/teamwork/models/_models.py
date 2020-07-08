# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class CollectionOfTeamsAppInstallation(msrest.serialization.Model):
    """Collection of teamsAppInstallation.

    :param value:
    :type value: list[~teams_teamwork.models.MicrosoftGraphTeamsAppInstallation]
    :param odata_next_link:
    :type odata_next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[MicrosoftGraphTeamsAppInstallation]'},
        'odata_next_link': {'key': '@odata\\.nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(CollectionOfTeamsAppInstallation, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.odata_next_link = kwargs.get('odata_next_link', None)


class MicrosoftGraphEntity(msrest.serialization.Model):
    """entity.

    :param id: Read-only.
    :type id: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(MicrosoftGraphEntity, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)


class MicrosoftGraphTeamsApp(MicrosoftGraphEntity):
    """teamsApp.

    :param id: Read-only.
    :type id: str
    :param external_id: The ID of the catalog provided by the app developer in the Microsoft Teams
     zip app package.
    :type external_id: str
    :param name:
    :type name: str
    :param display_name: The name of the catalog app provided by the app developer in the Microsoft
     Teams zip app package.
    :type display_name: str
    :param distribution_method: teamsAppDistributionMethod. Possible values include: "store",
     "organization", "sideloaded", "unknownFutureValue".
    :type distribution_method: str or
     ~teams_teamwork.models.MicrosoftGraphTeamsAppDistributionMethod
    :param app_definitions: The details for each version of the app.
    :type app_definitions: list[~teams_teamwork.models.MicrosoftGraphTeamsAppDefinition]
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'external_id': {'key': 'externalId', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'distribution_method': {'key': 'distributionMethod', 'type': 'str'},
        'app_definitions': {'key': 'appDefinitions', 'type': '[MicrosoftGraphTeamsAppDefinition]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(MicrosoftGraphTeamsApp, self).__init__(**kwargs)
        self.external_id = kwargs.get('external_id', None)
        self.name = kwargs.get('name', None)
        self.display_name = kwargs.get('display_name', None)
        self.distribution_method = kwargs.get('distribution_method', None)
        self.app_definitions = kwargs.get('app_definitions', None)


class MicrosoftGraphTeamsAppDefinition(MicrosoftGraphEntity):
    """teamsAppDefinition.

    :param id: Read-only.
    :type id: str
    :param teams_app_id: The id from the Teams App manifest.
    :type teams_app_id: str
    :param display_name: The name of the app provided by the app developer.
    :type display_name: str
    :param version: The version number of the application.
    :type version: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'teams_app_id': {'key': 'teamsAppId', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(MicrosoftGraphTeamsAppDefinition, self).__init__(**kwargs)
        self.teams_app_id = kwargs.get('teams_app_id', None)
        self.display_name = kwargs.get('display_name', None)
        self.version = kwargs.get('version', None)


class MicrosoftGraphTeamsAppInstallation(MicrosoftGraphEntity):
    """teamsAppInstallation.

    :param id: Read-only.
    :type id: str
    :param teams_app_definition: teamsAppDefinition.
    :type teams_app_definition: ~teams_teamwork.models.MicrosoftGraphTeamsAppDefinition
    :param id_teams_app_id: Read-only.
    :type id_teams_app_id: str
    :param external_id: The ID of the catalog provided by the app developer in the Microsoft Teams
     zip app package.
    :type external_id: str
    :param name:
    :type name: str
    :param display_name: The name of the catalog app provided by the app developer in the Microsoft
     Teams zip app package.
    :type display_name: str
    :param distribution_method: teamsAppDistributionMethod. Possible values include: "store",
     "organization", "sideloaded", "unknownFutureValue".
    :type distribution_method: str or
     ~teams_teamwork.models.MicrosoftGraphTeamsAppDistributionMethod
    :param app_definitions: The details for each version of the app.
    :type app_definitions: list[~teams_teamwork.models.MicrosoftGraphTeamsAppDefinition]
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'teams_app_definition': {'key': 'teamsAppDefinition', 'type': 'MicrosoftGraphTeamsAppDefinition'},
        'id_teams_app_id': {'key': 'teamsApp.id', 'type': 'str'},
        'external_id': {'key': 'teamsApp.externalId', 'type': 'str'},
        'name': {'key': 'teamsApp.name', 'type': 'str'},
        'display_name': {'key': 'teamsApp.displayName', 'type': 'str'},
        'distribution_method': {'key': 'teamsApp.distributionMethod', 'type': 'str'},
        'app_definitions': {'key': 'teamsApp.appDefinitions', 'type': '[MicrosoftGraphTeamsAppDefinition]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(MicrosoftGraphTeamsAppInstallation, self).__init__(**kwargs)
        self.teams_app_definition = kwargs.get('teams_app_definition', None)
        self.id_teams_app_id = kwargs.get('id_teams_app_id', None)
        self.external_id = kwargs.get('external_id', None)
        self.name = kwargs.get('name', None)
        self.display_name = kwargs.get('display_name', None)
        self.distribution_method = kwargs.get('distribution_method', None)
        self.app_definitions = kwargs.get('app_definitions', None)


class MicrosoftGraphUserTeamwork(MicrosoftGraphEntity):
    """userTeamwork.

    :param id: Read-only.
    :type id: str
    :param installed_apps:
    :type installed_apps: list[~teams_teamwork.models.MicrosoftGraphTeamsAppInstallation]
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'installed_apps': {'key': 'installedApps', 'type': '[MicrosoftGraphTeamsAppInstallation]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(MicrosoftGraphUserTeamwork, self).__init__(**kwargs)
        self.installed_apps = kwargs.get('installed_apps', None)


class OdataError(msrest.serialization.Model):
    """OdataError.

    All required parameters must be populated in order to send to Azure.

    :param error: Required.
    :type error: ~teams_teamwork.models.OdataErrorMain
    """

    _validation = {
        'error': {'required': True},
    }

    _attribute_map = {
        'error': {'key': 'error', 'type': 'OdataErrorMain'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OdataError, self).__init__(**kwargs)
        self.error = kwargs['error']


class OdataErrorDetail(msrest.serialization.Model):
    """OdataErrorDetail.

    All required parameters must be populated in order to send to Azure.

    :param code: Required.
    :type code: str
    :param message: Required.
    :type message: str
    :param target:
    :type target: str
    """

    _validation = {
        'code': {'required': True},
        'message': {'required': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OdataErrorDetail, self).__init__(**kwargs)
        self.code = kwargs['code']
        self.message = kwargs['message']
        self.target = kwargs.get('target', None)


class OdataErrorMain(msrest.serialization.Model):
    """OdataErrorMain.

    All required parameters must be populated in order to send to Azure.

    :param code: Required.
    :type code: str
    :param message: Required.
    :type message: str
    :param target:
    :type target: str
    :param details:
    :type details: list[~teams_teamwork.models.OdataErrorDetail]
    :param innererror: The structure of this object is service-specific.
    :type innererror: object
    """

    _validation = {
        'code': {'required': True},
        'message': {'required': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'details': {'key': 'details', 'type': '[OdataErrorDetail]'},
        'innererror': {'key': 'innererror', 'type': 'object'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OdataErrorMain, self).__init__(**kwargs)
        self.code = kwargs['code']
        self.message = kwargs['message']
        self.target = kwargs.get('target', None)
        self.details = kwargs.get('details', None)
        self.innererror = kwargs.get('innererror', None)
