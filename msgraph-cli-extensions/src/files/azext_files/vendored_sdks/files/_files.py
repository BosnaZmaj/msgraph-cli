# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING

from azure.mgmt.core import ARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

    from azure.core.credentials import TokenCredential

from ._configuration import FilesConfiguration
from .operations import DriveDriveOperations
from .operations import DriveOperations
from .operations import DriveListOperations
from .operations import DriveListContentTypeOperations
from .operations import DriveListItemOperations
from .operations import DriveListItemVersionOperations
from .operations import GroupOperations
from .operations import ShareSharedDriveItemOperations
from .operations import ShareOperations
from .operations import ShareListOperations
from .operations import ShareListContentTypeOperations
from .operations import ShareListItemOperations
from .operations import ShareListItemVersionOperations
from .operations import ShareListItemOperations
from .operations import ShareListItemVersionOperations
from .operations import SharePermissionOperations
from .operations import UserOperations
from . import models


class Files(object):
    """Files.

    :ivar drive_drive: DriveDriveOperations operations
    :vartype drive_drive: files.operations.DriveDriveOperations
    :ivar drive: DriveOperations operations
    :vartype drive: files.operations.DriveOperations
    :ivar drive_list: DriveListOperations operations
    :vartype drive_list: files.operations.DriveListOperations
    :ivar drive_list_content_type: DriveListContentTypeOperations operations
    :vartype drive_list_content_type: files.operations.DriveListContentTypeOperations
    :ivar drive_list_item: DriveListItemOperations operations
    :vartype drive_list_item: files.operations.DriveListItemOperations
    :ivar drive_list_item_version: DriveListItemVersionOperations operations
    :vartype drive_list_item_version: files.operations.DriveListItemVersionOperations
    :ivar group: GroupOperations operations
    :vartype group: files.operations.GroupOperations
    :ivar share_shared_drive_item: ShareSharedDriveItemOperations operations
    :vartype share_shared_drive_item: files.operations.ShareSharedDriveItemOperations
    :ivar share: ShareOperations operations
    :vartype share: files.operations.ShareOperations
    :ivar share_list: ShareListOperations operations
    :vartype share_list: files.operations.ShareListOperations
    :ivar share_list_content_type: ShareListContentTypeOperations operations
    :vartype share_list_content_type: files.operations.ShareListContentTypeOperations
    :ivar share_list_item: ShareListItemOperations operations
    :vartype share_list_item: files.operations.ShareListItemOperations
    :ivar share_list_item_version: ShareListItemVersionOperations operations
    :vartype share_list_item_version: files.operations.ShareListItemVersionOperations
    :ivar share_list_item: ShareListItemOperations operations
    :vartype share_list_item: files.operations.ShareListItemOperations
    :ivar share_list_item_version: ShareListItemVersionOperations operations
    :vartype share_list_item_version: files.operations.ShareListItemVersionOperations
    :ivar share_permission: SharePermissionOperations operations
    :vartype share_permission: files.operations.SharePermissionOperations
    :ivar user: UserOperations operations
    :vartype user: files.operations.UserOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
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
        credential,  # type: "TokenCredential"
        top=None,  # type: Optional[int]
        skip=None,  # type: Optional[int]
        search=None,  # type: Optional[str]
        filter=None,  # type: Optional[str]
        count=None,  # type: Optional[bool]
        base_url=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        if not base_url:
            base_url = 'https://graph.microsoft.com/v1.0'
        self._config = FilesConfiguration(credential, top, skip, search, filter, count, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.drive_drive = DriveDriveOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.drive = DriveOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.drive_list = DriveListOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.drive_list_content_type = DriveListContentTypeOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.drive_list_item = DriveListItemOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.drive_list_item_version = DriveListItemVersionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.group = GroupOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.share_shared_drive_item = ShareSharedDriveItemOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.share = ShareOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.share_list = ShareListOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.share_list_content_type = ShareListContentTypeOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.share_list_item = ShareListItemOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.share_list_item_version = ShareListItemVersionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.share_list_item = ShareListItemOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.share_list_item_version = ShareListItemVersionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.share_permission = SharePermissionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user = UserOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> Files
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)