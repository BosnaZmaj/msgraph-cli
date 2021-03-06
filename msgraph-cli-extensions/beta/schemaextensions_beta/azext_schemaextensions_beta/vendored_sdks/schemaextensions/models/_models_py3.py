# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Dict, List, Optional

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class CollectionOfSchemaExtension(msrest.serialization.Model):
    """Collection of schemaExtension.

    :param additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :type additional_properties: dict[str, object]
    :param value:
    :type value: list[~schema_extensions.models.MicrosoftGraphSchemaExtension]
    :param odata_next_link:
    :type odata_next_link: str
    """

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'value': {'key': 'value', 'type': '[MicrosoftGraphSchemaExtension]'},
        'odata_next_link': {'key': '@odata\\.nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        additional_properties: Optional[Dict[str, object]] = None,
        value: Optional[List["MicrosoftGraphSchemaExtension"]] = None,
        odata_next_link: Optional[str] = None,
        **kwargs
    ):
        super(CollectionOfSchemaExtension, self).__init__(**kwargs)
        self.additional_properties = additional_properties
        self.value = value
        self.odata_next_link = odata_next_link


class MicrosoftGraphEntity(msrest.serialization.Model):
    """entity.

    :param additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :type additional_properties: dict[str, object]
    :param id: Read-only.
    :type id: str
    """

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'id': {'key': 'id', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        additional_properties: Optional[Dict[str, object]] = None,
        id: Optional[str] = None,
        **kwargs
    ):
        super(MicrosoftGraphEntity, self).__init__(**kwargs)
        self.additional_properties = additional_properties
        self.id = id


class MicrosoftGraphExtensionSchemaProperty(msrest.serialization.Model):
    """extensionSchemaProperty.

    :param additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :type additional_properties: dict[str, object]
    :param name: The name of the strongly-typed property defined as part of a schema extension.
    :type name: str
    :param type: The type of the property that is defined as part of a schema extension.  Allowed
     values are Binary, Boolean, DateTime, Integer or String.  See the table below for more details.
    :type type: str
    """

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        additional_properties: Optional[Dict[str, object]] = None,
        name: Optional[str] = None,
        type: Optional[str] = None,
        **kwargs
    ):
        super(MicrosoftGraphExtensionSchemaProperty, self).__init__(**kwargs)
        self.additional_properties = additional_properties
        self.name = name
        self.type = type


class MicrosoftGraphSchemaExtension(MicrosoftGraphEntity):
    """schemaExtension.

    :param id: Read-only.
    :type id: str
    :param additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :type additional_properties: dict[str, object]
    :param description: Description for the schema extension.
    :type description: str
    :param owner: The appId of the application that is the owner of the schema extension. This
     property can be supplied on creation, to set the owner.  If not supplied, then the calling
     application's appId will be set as the owner. In either case, the signed-in user must be the
     owner of the application. Once set, this property is read-only and cannot be changed.
    :type owner: str
    :param properties: The collection of property names and types that make up the schema extension
     definition.
    :type properties: list[~schema_extensions.models.MicrosoftGraphExtensionSchemaProperty]
    :param status: The lifecycle state of the schema extension. Possible states are InDevelopment,
     Available, and Deprecated. Automatically set to InDevelopment on creation. Schema extensions
     provides more information on the possible state transitions and behaviors.
    :type status: str
    :param target_types: Set of Microsoft Graph types (that can support extensions) that the schema
     extension can be applied to. Select from contact, device, event, group, message, organization,
     post, or user.
    :type target_types: list[str]
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'additional_properties': {'key': '', 'type': '{object}'},
        'description': {'key': 'description', 'type': 'str'},
        'owner': {'key': 'owner', 'type': 'str'},
        'properties': {'key': 'properties', 'type': '[MicrosoftGraphExtensionSchemaProperty]'},
        'status': {'key': 'status', 'type': 'str'},
        'target_types': {'key': 'targetTypes', 'type': '[str]'},
    }

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        additional_properties: Optional[Dict[str, object]] = None,
        description: Optional[str] = None,
        owner: Optional[str] = None,
        properties: Optional[List["MicrosoftGraphExtensionSchemaProperty"]] = None,
        status: Optional[str] = None,
        target_types: Optional[List[str]] = None,
        **kwargs
    ):
        super(MicrosoftGraphSchemaExtension, self).__init__(id=id, **kwargs)
        self.additional_properties = additional_properties
        self.description = description
        self.owner = owner
        self.properties = properties
        self.status = status
        self.target_types = target_types


class OdataError(msrest.serialization.Model):
    """OdataError.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :type additional_properties: dict[str, object]
    :param error: Required.
    :type error: ~schema_extensions.models.OdataErrorMain
    """

    _validation = {
        'error': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'error': {'key': 'error', 'type': 'OdataErrorMain'},
    }

    def __init__(
        self,
        *,
        error: "OdataErrorMain",
        additional_properties: Optional[Dict[str, object]] = None,
        **kwargs
    ):
        super(OdataError, self).__init__(**kwargs)
        self.additional_properties = additional_properties
        self.error = error


class OdataErrorDetail(msrest.serialization.Model):
    """OdataErrorDetail.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :type additional_properties: dict[str, object]
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
        'additional_properties': {'key': '', 'type': '{object}'},
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        code: str,
        message: str,
        additional_properties: Optional[Dict[str, object]] = None,
        target: Optional[str] = None,
        **kwargs
    ):
        super(OdataErrorDetail, self).__init__(**kwargs)
        self.additional_properties = additional_properties
        self.code = code
        self.message = message
        self.target = target


class OdataErrorMain(msrest.serialization.Model):
    """OdataErrorMain.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :type additional_properties: dict[str, object]
    :param code: Required.
    :type code: str
    :param message: Required.
    :type message: str
    :param target:
    :type target: str
    :param details:
    :type details: list[~schema_extensions.models.OdataErrorDetail]
    :param innererror: The structure of this object is service-specific.
    :type innererror: dict[str, object]
    """

    _validation = {
        'code': {'required': True},
        'message': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'details': {'key': 'details', 'type': '[OdataErrorDetail]'},
        'innererror': {'key': 'innererror', 'type': '{object}'},
    }

    def __init__(
        self,
        *,
        code: str,
        message: str,
        additional_properties: Optional[Dict[str, object]] = None,
        target: Optional[str] = None,
        details: Optional[List["OdataErrorDetail"]] = None,
        innererror: Optional[Dict[str, object]] = None,
        **kwargs
    ):
        super(OdataErrorMain, self).__init__(**kwargs)
        self.additional_properties = additional_properties
        self.code = code
        self.message = message
        self.target = target
        self.details = details
        self.innererror = innererror
