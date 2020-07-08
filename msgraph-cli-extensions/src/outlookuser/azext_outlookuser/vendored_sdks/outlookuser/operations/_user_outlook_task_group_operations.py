# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Iterable, List, Optional, TypeVar, Union

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class UserOutlookTaskGroupOperations(object):
    """UserOutlookTaskGroupOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~users_outlook_user.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def list_task_folder(
        self,
        user_id,  # type: str
        outlook_task_group_id,  # type: str
        orderby=None,  # type: Optional[List[Union[str, "models.Enum44"]]]
        select=None,  # type: Optional[List[Union[str, "models.Enum45"]]]
        expand=None,  # type: Optional[List[Union[str, "models.Enum46"]]]
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["models.CollectionOfOutlookTaskFolder0"]
        """Get taskFolders from users.

        Get taskFolders from users.

        :param user_id: key: user-id of user.
        :type user_id: str
        :param outlook_task_group_id: key: outlookTaskGroup-id of outlookTaskGroup.
        :type outlook_task_group_id: str
        :param orderby: Order items by property values.
        :type orderby: list[str or ~users_outlook_user.models.Enum44]
        :param select: Select properties to be returned.
        :type select: list[str or ~users_outlook_user.models.Enum45]
        :param expand: Expand related entities.
        :type expand: list[str or ~users_outlook_user.models.Enum46]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either CollectionOfOutlookTaskFolder0 or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~users_outlook_user.models.CollectionOfOutlookTaskFolder0]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.CollectionOfOutlookTaskFolder0"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = 'application/json'

            if not next_link:
                # Construct URL
                url = self.list_task_folder.metadata['url']  # type: ignore
                path_format_arguments = {
                    'user-id': self._serialize.url("user_id", user_id, 'str'),
                    'outlookTaskGroup-id': self._serialize.url("outlook_task_group_id", outlook_task_group_id, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                if self._config.top is not None:
                    query_parameters['$top'] = self._serialize.query("self._config.top", self._config.top, 'int', minimum=0)
                if self._config.skip is not None:
                    query_parameters['$skip'] = self._serialize.query("self._config.skip", self._config.skip, 'int', minimum=0)
                if self._config.search is not None:
                    query_parameters['$search'] = self._serialize.query("self._config.search", self._config.search, 'str')
                if self._config.filter is not None:
                    query_parameters['$filter'] = self._serialize.query("self._config.filter", self._config.filter, 'str')
                if self._config.count is not None:
                    query_parameters['$count'] = self._serialize.query("self._config.count", self._config.count, 'bool')
                if orderby is not None:
                    query_parameters['$orderby'] = self._serialize.query("orderby", orderby, '[str]', div=',')
                if select is not None:
                    query_parameters['$select'] = self._serialize.query("select", select, '[str]', div=',')
                if expand is not None:
                    query_parameters['$expand'] = self._serialize.query("expand", expand, '[str]', div=',')

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize('CollectionOfOutlookTaskFolder0', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.odata_next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize(models.OdataError, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    list_task_folder.metadata = {'url': '/users/{user-id}/outlook/taskGroups/{outlookTaskGroup-id}/taskFolders'}  # type: ignore

    def create_task_folder(
        self,
        user_id,  # type: str
        outlook_task_group_id,  # type: str
        id=None,  # type: Optional[str]
        change_key=None,  # type: Optional[str]
        name=None,  # type: Optional[str]
        is_default_folder=None,  # type: Optional[bool]
        parent_group_key=None,  # type: Optional[str]
        tasks=None,  # type: Optional[List["models.MicrosoftGraphOutlookTask"]]
        single_value_extended_properties=None,  # type: Optional[List["models.MicrosoftGraphSingleValueLegacyExtendedProperty"]]
        multi_value_extended_properties=None,  # type: Optional[List["models.MicrosoftGraphMultiValueLegacyExtendedProperty"]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphOutlookTaskFolder"
        """Create new navigation property to taskFolders for users.

        Create new navigation property to taskFolders for users.

        :param user_id: key: user-id of user.
        :type user_id: str
        :param outlook_task_group_id: key: outlookTaskGroup-id of outlookTaskGroup.
        :type outlook_task_group_id: str
        :param id: Read-only.
        :type id: str
        :param change_key:
        :type change_key: str
        :param name:
        :type name: str
        :param is_default_folder:
        :type is_default_folder: bool
        :param parent_group_key:
        :type parent_group_key: str
        :param tasks:
        :type tasks: list[~users_outlook_user.models.MicrosoftGraphOutlookTask]
        :param single_value_extended_properties:
        :type single_value_extended_properties: list[~users_outlook_user.models.MicrosoftGraphSingleValueLegacyExtendedProperty]
        :param multi_value_extended_properties:
        :type multi_value_extended_properties: list[~users_outlook_user.models.MicrosoftGraphMultiValueLegacyExtendedProperty]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphOutlookTaskFolder, or the result of cls(response)
        :rtype: ~users_outlook_user.models.MicrosoftGraphOutlookTaskFolder
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphOutlookTaskFolder"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.MicrosoftGraphOutlookTaskFolder(id=id, change_key=change_key, name=name, is_default_folder=is_default_folder, parent_group_key=parent_group_key, tasks=tasks, single_value_extended_properties=single_value_extended_properties, multi_value_extended_properties=multi_value_extended_properties)
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.create_task_folder.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'outlookTaskGroup-id': self._serialize.url("outlook_task_group_id", outlook_task_group_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'MicrosoftGraphOutlookTaskFolder')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphOutlookTaskFolder', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_task_folder.metadata = {'url': '/users/{user-id}/outlook/taskGroups/{outlookTaskGroup-id}/taskFolders'}  # type: ignore

    def get_task_folder(
        self,
        user_id,  # type: str
        outlook_task_group_id,  # type: str
        outlook_task_folder_id,  # type: str
        select=None,  # type: Optional[List[Union[str, "models.Enum47"]]]
        expand=None,  # type: Optional[List[Union[str, "models.Enum48"]]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphOutlookTaskFolder"
        """Get taskFolders from users.

        Get taskFolders from users.

        :param user_id: key: user-id of user.
        :type user_id: str
        :param outlook_task_group_id: key: outlookTaskGroup-id of outlookTaskGroup.
        :type outlook_task_group_id: str
        :param outlook_task_folder_id: key: outlookTaskFolder-id of outlookTaskFolder.
        :type outlook_task_folder_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~users_outlook_user.models.Enum47]
        :param expand: Expand related entities.
        :type expand: list[str or ~users_outlook_user.models.Enum48]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphOutlookTaskFolder, or the result of cls(response)
        :rtype: ~users_outlook_user.models.MicrosoftGraphOutlookTaskFolder
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphOutlookTaskFolder"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        # Construct URL
        url = self.get_task_folder.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'outlookTaskGroup-id': self._serialize.url("outlook_task_group_id", outlook_task_group_id, 'str'),
            'outlookTaskFolder-id': self._serialize.url("outlook_task_folder_id", outlook_task_folder_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if select is not None:
            query_parameters['$select'] = self._serialize.query("select", select, '[str]', div=',')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query("expand", expand, '[str]', div=',')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphOutlookTaskFolder', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_task_folder.metadata = {'url': '/users/{user-id}/outlook/taskGroups/{outlookTaskGroup-id}/taskFolders/{outlookTaskFolder-id}'}  # type: ignore

    def update_task_folder(
        self,
        user_id,  # type: str
        outlook_task_group_id,  # type: str
        outlook_task_folder_id,  # type: str
        id=None,  # type: Optional[str]
        change_key=None,  # type: Optional[str]
        name=None,  # type: Optional[str]
        is_default_folder=None,  # type: Optional[bool]
        parent_group_key=None,  # type: Optional[str]
        tasks=None,  # type: Optional[List["models.MicrosoftGraphOutlookTask"]]
        single_value_extended_properties=None,  # type: Optional[List["models.MicrosoftGraphSingleValueLegacyExtendedProperty"]]
        multi_value_extended_properties=None,  # type: Optional[List["models.MicrosoftGraphMultiValueLegacyExtendedProperty"]]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Update the navigation property taskFolders in users.

        Update the navigation property taskFolders in users.

        :param user_id: key: user-id of user.
        :type user_id: str
        :param outlook_task_group_id: key: outlookTaskGroup-id of outlookTaskGroup.
        :type outlook_task_group_id: str
        :param outlook_task_folder_id: key: outlookTaskFolder-id of outlookTaskFolder.
        :type outlook_task_folder_id: str
        :param id: Read-only.
        :type id: str
        :param change_key:
        :type change_key: str
        :param name:
        :type name: str
        :param is_default_folder:
        :type is_default_folder: bool
        :param parent_group_key:
        :type parent_group_key: str
        :param tasks:
        :type tasks: list[~users_outlook_user.models.MicrosoftGraphOutlookTask]
        :param single_value_extended_properties:
        :type single_value_extended_properties: list[~users_outlook_user.models.MicrosoftGraphSingleValueLegacyExtendedProperty]
        :param multi_value_extended_properties:
        :type multi_value_extended_properties: list[~users_outlook_user.models.MicrosoftGraphMultiValueLegacyExtendedProperty]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.MicrosoftGraphOutlookTaskFolder(id=id, change_key=change_key, name=name, is_default_folder=is_default_folder, parent_group_key=parent_group_key, tasks=tasks, single_value_extended_properties=single_value_extended_properties, multi_value_extended_properties=multi_value_extended_properties)
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.update_task_folder.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'outlookTaskGroup-id': self._serialize.url("outlook_task_group_id", outlook_task_group_id, 'str'),
            'outlookTaskFolder-id': self._serialize.url("outlook_task_folder_id", outlook_task_folder_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'MicrosoftGraphOutlookTaskFolder')
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    update_task_folder.metadata = {'url': '/users/{user-id}/outlook/taskGroups/{outlookTaskGroup-id}/taskFolders/{outlookTaskFolder-id}'}  # type: ignore
