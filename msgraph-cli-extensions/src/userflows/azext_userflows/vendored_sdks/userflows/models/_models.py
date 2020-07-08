# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class CollectionOfIdentityUserFlow(msrest.serialization.Model):
    """Collection of identityUserFlow.

    :param value:
    :type value: list[~identity_user_flows.models.MicrosoftGraphIdentityUserFlow]
    :param odata_next_link:
    :type odata_next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[MicrosoftGraphIdentityUserFlow]'},
        'odata_next_link': {'key': '@odata\\.nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(CollectionOfIdentityUserFlow, self).__init__(**kwargs)
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


class MicrosoftGraphIdentityUserFlow(MicrosoftGraphEntity):
    """identityUserFlow.

    :param id: Read-only.
    :type id: str
    :param user_flow_type: userFlowType. Possible values include: "signUp", "signIn",
     "signUpOrSignIn", "passwordReset", "profileUpdate", "resourceOwner", "unknownFutureValue".
    :type user_flow_type: str or ~identity_user_flows.models.MicrosoftGraphUserFlowType
    :param user_flow_type_version:
    :type user_flow_type_version: float
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'user_flow_type': {'key': 'userFlowType', 'type': 'str'},
        'user_flow_type_version': {'key': 'userFlowTypeVersion', 'type': 'float'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(MicrosoftGraphIdentityUserFlow, self).__init__(**kwargs)
        self.user_flow_type = kwargs.get('user_flow_type', None)
        self.user_flow_type_version = kwargs.get('user_flow_type_version', None)


class OdataError(msrest.serialization.Model):
    """OdataError.

    All required parameters must be populated in order to send to Azure.

    :param error: Required.
    :type error: ~identity_user_flows.models.OdataErrorMain
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
    :type details: list[~identity_user_flows.models.OdataErrorDetail]
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
