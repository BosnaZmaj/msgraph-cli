# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional, TYPE_CHECKING

from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

from ._configuration_async import DevicesCorporateManagementConfiguration
from .operations_async import DeviceAppManagementDeviceAppManagementOperations
from .operations_async import DeviceAppManagementOperations
from .operations_async import DeviceAppManagementAndroidManagedAppProtectionOperations
from .operations_async import DeviceAppManagementDefaultManagedAppProtectionOperations
from .operations_async import DeviceAppManagementIoManagedAppProtectionOperations
from .operations_async import DeviceAppManagementManagedAppPolicyOperations
from .operations_async import DeviceAppManagementManagedAppRegistrationOperations
from .operations_async import DeviceAppManagementManagedAppRegistrationAppliedPolicyOperations
from .operations_async import DeviceAppManagementManagedAppRegistrationIntendedPolicyOperations
from .operations_async import DeviceAppManagementManagedEBookOperations
from .operations_async import DeviceAppManagementManagedEBookUserStateSummaryOperations
from .operations_async import DeviceAppManagementMobileAppConfigurationOperations
from .operations_async import DeviceAppManagementMobileAppOperations
from .operations_async import DeviceAppManagementTargetedManagedAppConfigurationOperations
from .operations_async import DeviceAppManagementVppTokenOperations
from .operations_async import UserOperations
from .operations_async import UserManagedDeviceOperations
from .. import models


class DevicesCorporateManagement(object):
    """DevicesCorporateManagement.

    :ivar device_app_management_device_app_management: DeviceAppManagementDeviceAppManagementOperations operations
    :vartype device_app_management_device_app_management: devices_corporate_management.aio.operations_async.DeviceAppManagementDeviceAppManagementOperations
    :ivar device_app_management: DeviceAppManagementOperations operations
    :vartype device_app_management: devices_corporate_management.aio.operations_async.DeviceAppManagementOperations
    :ivar device_app_management_android_managed_app_protection: DeviceAppManagementAndroidManagedAppProtectionOperations operations
    :vartype device_app_management_android_managed_app_protection: devices_corporate_management.aio.operations_async.DeviceAppManagementAndroidManagedAppProtectionOperations
    :ivar device_app_management_default_managed_app_protection: DeviceAppManagementDefaultManagedAppProtectionOperations operations
    :vartype device_app_management_default_managed_app_protection: devices_corporate_management.aio.operations_async.DeviceAppManagementDefaultManagedAppProtectionOperations
    :ivar device_app_management_io_managed_app_protection: DeviceAppManagementIoManagedAppProtectionOperations operations
    :vartype device_app_management_io_managed_app_protection: devices_corporate_management.aio.operations_async.DeviceAppManagementIoManagedAppProtectionOperations
    :ivar device_app_management_managed_app_policy: DeviceAppManagementManagedAppPolicyOperations operations
    :vartype device_app_management_managed_app_policy: devices_corporate_management.aio.operations_async.DeviceAppManagementManagedAppPolicyOperations
    :ivar device_app_management_managed_app_registration: DeviceAppManagementManagedAppRegistrationOperations operations
    :vartype device_app_management_managed_app_registration: devices_corporate_management.aio.operations_async.DeviceAppManagementManagedAppRegistrationOperations
    :ivar device_app_management_managed_app_registration_applied_policy: DeviceAppManagementManagedAppRegistrationAppliedPolicyOperations operations
    :vartype device_app_management_managed_app_registration_applied_policy: devices_corporate_management.aio.operations_async.DeviceAppManagementManagedAppRegistrationAppliedPolicyOperations
    :ivar device_app_management_managed_app_registration_intended_policy: DeviceAppManagementManagedAppRegistrationIntendedPolicyOperations operations
    :vartype device_app_management_managed_app_registration_intended_policy: devices_corporate_management.aio.operations_async.DeviceAppManagementManagedAppRegistrationIntendedPolicyOperations
    :ivar device_app_management_managed_ebook: DeviceAppManagementManagedEBookOperations operations
    :vartype device_app_management_managed_ebook: devices_corporate_management.aio.operations_async.DeviceAppManagementManagedEBookOperations
    :ivar device_app_management_managed_ebook_user_state_summary: DeviceAppManagementManagedEBookUserStateSummaryOperations operations
    :vartype device_app_management_managed_ebook_user_state_summary: devices_corporate_management.aio.operations_async.DeviceAppManagementManagedEBookUserStateSummaryOperations
    :ivar device_app_management_mobile_app_configuration: DeviceAppManagementMobileAppConfigurationOperations operations
    :vartype device_app_management_mobile_app_configuration: devices_corporate_management.aio.operations_async.DeviceAppManagementMobileAppConfigurationOperations
    :ivar device_app_management_mobile_app: DeviceAppManagementMobileAppOperations operations
    :vartype device_app_management_mobile_app: devices_corporate_management.aio.operations_async.DeviceAppManagementMobileAppOperations
    :ivar device_app_management_targeted_managed_app_configuration: DeviceAppManagementTargetedManagedAppConfigurationOperations operations
    :vartype device_app_management_targeted_managed_app_configuration: devices_corporate_management.aio.operations_async.DeviceAppManagementTargetedManagedAppConfigurationOperations
    :ivar device_app_management_vpp_token: DeviceAppManagementVppTokenOperations operations
    :vartype device_app_management_vpp_token: devices_corporate_management.aio.operations_async.DeviceAppManagementVppTokenOperations
    :ivar user: UserOperations operations
    :vartype user: devices_corporate_management.aio.operations_async.UserOperations
    :ivar user_managed_device: UserManagedDeviceOperations operations
    :vartype user_managed_device: devices_corporate_management.aio.operations_async.UserManagedDeviceOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param top: Show only the first n items.
    :type top: int
    :param skip: Skip the first n items.
    :type skip: int
    :param search: Search items by search phrases.
    :type search: str
    :param filter: Filter items by property values.
    :type filter: str
    :param count: Include count of items.
    :type count: bool
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = 'https://graph.microsoft.com/v1.0'
        self._config = DevicesCorporateManagementConfiguration(credential, top, skip, search, filter, count, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.device_app_management_device_app_management = DeviceAppManagementDeviceAppManagementOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.device_app_management = DeviceAppManagementOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.device_app_management_android_managed_app_protection = DeviceAppManagementAndroidManagedAppProtectionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.device_app_management_default_managed_app_protection = DeviceAppManagementDefaultManagedAppProtectionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.device_app_management_io_managed_app_protection = DeviceAppManagementIoManagedAppProtectionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.device_app_management_managed_app_policy = DeviceAppManagementManagedAppPolicyOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.device_app_management_managed_app_registration = DeviceAppManagementManagedAppRegistrationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.device_app_management_managed_app_registration_applied_policy = DeviceAppManagementManagedAppRegistrationAppliedPolicyOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.device_app_management_managed_app_registration_intended_policy = DeviceAppManagementManagedAppRegistrationIntendedPolicyOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.device_app_management_managed_ebook = DeviceAppManagementManagedEBookOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.device_app_management_managed_ebook_user_state_summary = DeviceAppManagementManagedEBookUserStateSummaryOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.device_app_management_mobile_app_configuration = DeviceAppManagementMobileAppConfigurationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.device_app_management_mobile_app = DeviceAppManagementMobileAppOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.device_app_management_targeted_managed_app_configuration = DeviceAppManagementTargetedManagedAppConfigurationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.device_app_management_vpp_token = DeviceAppManagementVppTokenOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user = UserOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_managed_device = UserManagedDeviceOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "DevicesCorporateManagement":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)