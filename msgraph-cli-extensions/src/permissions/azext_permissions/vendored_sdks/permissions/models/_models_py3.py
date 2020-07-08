# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import datetime
from typing import List, Optional

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class CollectionOfResourceSpecificPermissionGrant(msrest.serialization.Model):
    """Collection of resourceSpecificPermissionGrant.

    :param value:
    :type value: list[~files_permissions.models.MicrosoftGraphResourceSpecificPermissionGrant]
    :param odata_next_link:
    :type odata_next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[MicrosoftGraphResourceSpecificPermissionGrant]'},
        'odata_next_link': {'key': '@odata\\.nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["MicrosoftGraphResourceSpecificPermissionGrant"]] = None,
        odata_next_link: Optional[str] = None,
        **kwargs
    ):
        super(CollectionOfResourceSpecificPermissionGrant, self).__init__(**kwargs)
        self.value = value
        self.odata_next_link = odata_next_link


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
        *,
        id: Optional[str] = None,
        **kwargs
    ):
        super(MicrosoftGraphEntity, self).__init__(**kwargs)
        self.id = id


class MicrosoftGraphDirectoryObject(MicrosoftGraphEntity):
    """Represents an Azure Active Directory object. The directoryObject type is the base type for many other directory entity types.

    :param id: Read-only.
    :type id: str
    :param deleted_date_time:
    :type deleted_date_time: ~datetime.datetime
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'deleted_date_time': {'key': 'deletedDateTime', 'type': 'iso-8601'},
    }

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        deleted_date_time: Optional[datetime.datetime] = None,
        **kwargs
    ):
        super(MicrosoftGraphDirectoryObject, self).__init__(id=id, **kwargs)
        self.deleted_date_time = deleted_date_time


class MicrosoftGraphResourceSpecificPermissionGrant(MicrosoftGraphDirectoryObject):
    """Represents an Azure Active Directory object. The directoryObject type is the base type for many other directory entity types.

    :param id: Read-only.
    :type id: str
    :param deleted_date_time:
    :type deleted_date_time: ~datetime.datetime
    :param client_id:
    :type client_id: str
    :param client_app_id:
    :type client_app_id: str
    :param resource_app_id:
    :type resource_app_id: str
    :param permission_type:
    :type permission_type: str
    :param permission:
    :type permission: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'deleted_date_time': {'key': 'deletedDateTime', 'type': 'iso-8601'},
        'client_id': {'key': 'clientId', 'type': 'str'},
        'client_app_id': {'key': 'clientAppId', 'type': 'str'},
        'resource_app_id': {'key': 'resourceAppId', 'type': 'str'},
        'permission_type': {'key': 'permissionType', 'type': 'str'},
        'permission': {'key': 'permission', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        deleted_date_time: Optional[datetime.datetime] = None,
        client_id: Optional[str] = None,
        client_app_id: Optional[str] = None,
        resource_app_id: Optional[str] = None,
        permission_type: Optional[str] = None,
        permission: Optional[str] = None,
        **kwargs
    ):
        super(MicrosoftGraphResourceSpecificPermissionGrant, self).__init__(id=id, deleted_date_time=deleted_date_time, **kwargs)
        self.client_id = client_id
        self.client_app_id = client_app_id
        self.resource_app_id = resource_app_id
        self.permission_type = permission_type
        self.permission = permission


class OdataError(msrest.serialization.Model):
    """OdataError.

    All required parameters must be populated in order to send to Azure.

    :param error: Required.
    :type error: ~files_permissions.models.OdataErrorMain
    """

    _validation = {
        'error': {'required': True},
    }

    _attribute_map = {
        'error': {'key': 'error', 'type': 'OdataErrorMain'},
    }

    def __init__(
        self,
        *,
        error: "OdataErrorMain",
        **kwargs
    ):
        super(OdataError, self).__init__(**kwargs)
        self.error = error


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
        *,
        code: str,
        message: str,
        target: Optional[str] = None,
        **kwargs
    ):
        super(OdataErrorDetail, self).__init__(**kwargs)
        self.code = code
        self.message = message
        self.target = target


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
    :type details: list[~files_permissions.models.OdataErrorDetail]
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
        *,
        code: str,
        message: str,
        target: Optional[str] = None,
        details: Optional[List["OdataErrorDetail"]] = None,
        innererror: Optional[object] = None,
        **kwargs
    ):
        super(OdataErrorMain, self).__init__(**kwargs)
        self.code = code
        self.message = message
        self.target = target
        self.details = details
        self.innererror = innererror
