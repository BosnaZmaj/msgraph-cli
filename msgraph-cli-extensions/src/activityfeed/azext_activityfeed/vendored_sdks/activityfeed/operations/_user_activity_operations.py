# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import datetime
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

class UserActivityOperations(object):
    """UserActivityOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~users_activity_feed.models
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

    def list_history_item(
        self,
        user_id,  # type: str
        user_activity_id,  # type: str
        orderby=None,  # type: Optional[List[Union[str, "models.Enum6"]]]
        select=None,  # type: Optional[List[Union[str, "models.Enum7"]]]
        expand=None,  # type: Optional[List[Union[str, "models.Get9ItemsItem"]]]
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["models.CollectionOfActivityHistoryItem"]
        """Get historyItems from users.

        Get historyItems from users.

        :param user_id: key: user-id of user.
        :type user_id: str
        :param user_activity_id: key: userActivity-id of userActivity.
        :type user_activity_id: str
        :param orderby: Order items by property values.
        :type orderby: list[str or ~users_activity_feed.models.Enum6]
        :param select: Select properties to be returned.
        :type select: list[str or ~users_activity_feed.models.Enum7]
        :param expand: Expand related entities.
        :type expand: list[str or ~users_activity_feed.models.Get9ItemsItem]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either CollectionOfActivityHistoryItem or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~users_activity_feed.models.CollectionOfActivityHistoryItem]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.CollectionOfActivityHistoryItem"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = 'application/json'

            if not next_link:
                # Construct URL
                url = self.list_history_item.metadata['url']  # type: ignore
                path_format_arguments = {
                    'user-id': self._serialize.url("user_id", user_id, 'str'),
                    'userActivity-id': self._serialize.url("user_activity_id", user_activity_id, 'str'),
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
            deserialized = self._deserialize('CollectionOfActivityHistoryItem', pipeline_response)
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
    list_history_item.metadata = {'url': '/users/{user-id}/activities/{userActivity-id}/historyItems'}  # type: ignore

    def create_history_item(
        self,
        user_id,  # type: str
        user_activity_id,  # type: str
        id=None,  # type: Optional[str]
        status=None,  # type: Optional[Union[str, "models.MicrosoftGraphStatus"]]
        active_duration_seconds=None,  # type: Optional[int]
        created_date_time=None,  # type: Optional[datetime.datetime]
        last_active_date_time=None,  # type: Optional[datetime.datetime]
        last_modified_date_time=None,  # type: Optional[datetime.datetime]
        expiration_date_time=None,  # type: Optional[datetime.datetime]
        started_date_time=None,  # type: Optional[datetime.datetime]
        user_timezone=None,  # type: Optional[str]
        activity=None,  # type: Optional["models.MicrosoftGraphUserActivity"]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphActivityHistoryItem"
        """Create new navigation property to historyItems for users.

        Create new navigation property to historyItems for users.

        :param user_id: key: user-id of user.
        :type user_id: str
        :param user_activity_id: key: userActivity-id of userActivity.
        :type user_activity_id: str
        :param id: Read-only.
        :type id: str
        :param status: status.
        :type status: str or ~users_activity_feed.models.MicrosoftGraphStatus
        :param active_duration_seconds: Optional. The duration of active user engagement. if not
         supplied, this is calculated from the startedDateTime and lastActiveDateTime.
        :type active_duration_seconds: int
        :param created_date_time: Set by the server. DateTime in UTC when the object was created on the
         server.
        :type created_date_time: ~datetime.datetime
        :param last_active_date_time: Optional. UTC DateTime when the historyItem (activity session)
         was last understood as active or finished - if null, historyItem status should be Ongoing.
        :type last_active_date_time: ~datetime.datetime
        :param last_modified_date_time: Set by the server. DateTime in UTC when the object was modified
         on the server.
        :type last_modified_date_time: ~datetime.datetime
        :param expiration_date_time: Optional. UTC DateTime when the historyItem will undergo hard-
         delete. Can be set by the client.
        :type expiration_date_time: ~datetime.datetime
        :param started_date_time: Required. UTC DateTime when the historyItem (activity session) was
         started. Required for timeline history.
        :type started_date_time: ~datetime.datetime
        :param user_timezone: Optional. The timezone in which the user's device used to generate the
         activity was located at activity creation time. Values supplied as Olson IDs in order to
         support cross-platform representation.
        :type user_timezone: str
        :param activity: userActivity.
        :type activity: ~users_activity_feed.models.MicrosoftGraphUserActivity
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphActivityHistoryItem, or the result of cls(response)
        :rtype: ~users_activity_feed.models.MicrosoftGraphActivityHistoryItem
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphActivityHistoryItem"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.MicrosoftGraphActivityHistoryItem(id=id, status=status, active_duration_seconds=active_duration_seconds, created_date_time=created_date_time, last_active_date_time=last_active_date_time, last_modified_date_time=last_modified_date_time, expiration_date_time=expiration_date_time, started_date_time=started_date_time, user_timezone=user_timezone, activity=activity)
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.create_history_item.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'userActivity-id': self._serialize.url("user_activity_id", user_activity_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'MicrosoftGraphActivityHistoryItem')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphActivityHistoryItem', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_history_item.metadata = {'url': '/users/{user-id}/activities/{userActivity-id}/historyItems'}  # type: ignore

    def get_history_item(
        self,
        user_id,  # type: str
        user_activity_id,  # type: str
        activity_history_item_id,  # type: str
        select=None,  # type: Optional[List[Union[str, "models.Enum9"]]]
        expand=None,  # type: Optional[List[Union[str, "models.Get4ItemsItem"]]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphActivityHistoryItem"
        """Get historyItems from users.

        Get historyItems from users.

        :param user_id: key: user-id of user.
        :type user_id: str
        :param user_activity_id: key: userActivity-id of userActivity.
        :type user_activity_id: str
        :param activity_history_item_id: key: activityHistoryItem-id of activityHistoryItem.
        :type activity_history_item_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~users_activity_feed.models.Enum9]
        :param expand: Expand related entities.
        :type expand: list[str or ~users_activity_feed.models.Get4ItemsItem]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphActivityHistoryItem, or the result of cls(response)
        :rtype: ~users_activity_feed.models.MicrosoftGraphActivityHistoryItem
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphActivityHistoryItem"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        # Construct URL
        url = self.get_history_item.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'userActivity-id': self._serialize.url("user_activity_id", user_activity_id, 'str'),
            'activityHistoryItem-id': self._serialize.url("activity_history_item_id", activity_history_item_id, 'str'),
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

        deserialized = self._deserialize('MicrosoftGraphActivityHistoryItem', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_history_item.metadata = {'url': '/users/{user-id}/activities/{userActivity-id}/historyItems/{activityHistoryItem-id}'}  # type: ignore

    def update_history_item(
        self,
        user_id,  # type: str
        user_activity_id,  # type: str
        activity_history_item_id,  # type: str
        id=None,  # type: Optional[str]
        status=None,  # type: Optional[Union[str, "models.MicrosoftGraphStatus"]]
        active_duration_seconds=None,  # type: Optional[int]
        created_date_time=None,  # type: Optional[datetime.datetime]
        last_active_date_time=None,  # type: Optional[datetime.datetime]
        last_modified_date_time=None,  # type: Optional[datetime.datetime]
        expiration_date_time=None,  # type: Optional[datetime.datetime]
        started_date_time=None,  # type: Optional[datetime.datetime]
        user_timezone=None,  # type: Optional[str]
        activity=None,  # type: Optional["models.MicrosoftGraphUserActivity"]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Update the navigation property historyItems in users.

        Update the navigation property historyItems in users.

        :param user_id: key: user-id of user.
        :type user_id: str
        :param user_activity_id: key: userActivity-id of userActivity.
        :type user_activity_id: str
        :param activity_history_item_id: key: activityHistoryItem-id of activityHistoryItem.
        :type activity_history_item_id: str
        :param id: Read-only.
        :type id: str
        :param status: status.
        :type status: str or ~users_activity_feed.models.MicrosoftGraphStatus
        :param active_duration_seconds: Optional. The duration of active user engagement. if not
         supplied, this is calculated from the startedDateTime and lastActiveDateTime.
        :type active_duration_seconds: int
        :param created_date_time: Set by the server. DateTime in UTC when the object was created on the
         server.
        :type created_date_time: ~datetime.datetime
        :param last_active_date_time: Optional. UTC DateTime when the historyItem (activity session)
         was last understood as active or finished - if null, historyItem status should be Ongoing.
        :type last_active_date_time: ~datetime.datetime
        :param last_modified_date_time: Set by the server. DateTime in UTC when the object was modified
         on the server.
        :type last_modified_date_time: ~datetime.datetime
        :param expiration_date_time: Optional. UTC DateTime when the historyItem will undergo hard-
         delete. Can be set by the client.
        :type expiration_date_time: ~datetime.datetime
        :param started_date_time: Required. UTC DateTime when the historyItem (activity session) was
         started. Required for timeline history.
        :type started_date_time: ~datetime.datetime
        :param user_timezone: Optional. The timezone in which the user's device used to generate the
         activity was located at activity creation time. Values supplied as Olson IDs in order to
         support cross-platform representation.
        :type user_timezone: str
        :param activity: userActivity.
        :type activity: ~users_activity_feed.models.MicrosoftGraphUserActivity
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.MicrosoftGraphActivityHistoryItem(id=id, status=status, active_duration_seconds=active_duration_seconds, created_date_time=created_date_time, last_active_date_time=last_active_date_time, last_modified_date_time=last_modified_date_time, expiration_date_time=expiration_date_time, started_date_time=started_date_time, user_timezone=user_timezone, activity=activity)
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.update_history_item.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'userActivity-id': self._serialize.url("user_activity_id", user_activity_id, 'str'),
            'activityHistoryItem-id': self._serialize.url("activity_history_item_id", activity_history_item_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'MicrosoftGraphActivityHistoryItem')
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

    update_history_item.metadata = {'url': '/users/{user-id}/activities/{userActivity-id}/historyItems/{activityHistoryItem-id}'}  # type: ignore
