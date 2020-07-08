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

class GroupConversationThreadOperations(object):
    """GroupConversationThreadOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~groups_conversation.models
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

    def list_post(
        self,
        group_id,  # type: str
        conversation_id,  # type: str
        conversation_thread_id,  # type: str
        orderby=None,  # type: Optional[List[Union[str, "models.Enum12"]]]
        select=None,  # type: Optional[List[Union[str, "models.Enum13"]]]
        expand=None,  # type: Optional[List[Union[str, "models.Get10ItemsItem"]]]
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["models.CollectionOfPost"]
        """Get posts from groups.

        Get posts from groups.

        :param group_id: key: group-id of group.
        :type group_id: str
        :param conversation_id: key: conversation-id of conversation.
        :type conversation_id: str
        :param conversation_thread_id: key: conversationThread-id of conversationThread.
        :type conversation_thread_id: str
        :param orderby: Order items by property values.
        :type orderby: list[str or ~groups_conversation.models.Enum12]
        :param select: Select properties to be returned.
        :type select: list[str or ~groups_conversation.models.Enum13]
        :param expand: Expand related entities.
        :type expand: list[str or ~groups_conversation.models.Get10ItemsItem]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either CollectionOfPost or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~groups_conversation.models.CollectionOfPost]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.CollectionOfPost"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = 'application/json'

            if not next_link:
                # Construct URL
                url = self.list_post.metadata['url']  # type: ignore
                path_format_arguments = {
                    'group-id': self._serialize.url("group_id", group_id, 'str'),
                    'conversation-id': self._serialize.url("conversation_id", conversation_id, 'str'),
                    'conversationThread-id': self._serialize.url("conversation_thread_id", conversation_thread_id, 'str'),
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
            deserialized = self._deserialize('CollectionOfPost', pipeline_response)
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
    list_post.metadata = {'url': '/groups/{group-id}/conversations/{conversation-id}/threads/{conversationThread-id}/posts'}  # type: ignore

    def create_post(
        self,
        group_id,  # type: str
        conversation_id,  # type: str
        conversation_thread_id,  # type: str
        id=None,  # type: Optional[str]
        created_date_time=None,  # type: Optional[datetime.datetime]
        last_modified_date_time=None,  # type: Optional[datetime.datetime]
        change_key=None,  # type: Optional[str]
        categories=None,  # type: Optional[List[str]]
        body=None,  # type: Optional["models.MicrosoftGraphItemBody"]
        received_date_time=None,  # type: Optional[datetime.datetime]
        has_attachments=None,  # type: Optional[bool]
        microsoft_graph_post_conversation_thread_id_conversation_thread_id=None,  # type: Optional[str]
        new_participants=None,  # type: Optional[List["models.MicrosoftGraphRecipient"]]
        microsoft_graph_post_conversation_id=None,  # type: Optional[str]
        importance=None,  # type: Optional[Union[str, "models.MicrosoftGraphImportance"]]
        in_reply_to=None,  # type: Optional["models.MicrosoftGraphPost"]
        single_value_extended_properties=None,  # type: Optional[List["models.MicrosoftGraphSingleValueLegacyExtendedProperty"]]
        multi_value_extended_properties=None,  # type: Optional[List["models.MicrosoftGraphMultiValueLegacyExtendedProperty"]]
        extensions=None,  # type: Optional[List["models.MicrosoftGraphEntity"]]
        attachments=None,  # type: Optional[List["models.MicrosoftGraphAttachment"]]
        mentions=None,  # type: Optional[List["models.MicrosoftGraphMention"]]
        name=None,  # type: Optional[str]
        address=None,  # type: Optional[str]
        microsoft_graph_email_address_name=None,  # type: Optional[str]
        microsoft_graph_email_address=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphPost"
        """Create new navigation property to posts for groups.

        Create new navigation property to posts for groups.

        :param group_id: key: group-id of group.
        :type group_id: str
        :param conversation_id: key: conversation-id of conversation.
        :type conversation_id: str
        :param conversation_thread_id: key: conversationThread-id of conversationThread.
        :type conversation_thread_id: str
        :param id: Read-only.
        :type id: str
        :param created_date_time: The Timestamp type represents date and time information using ISO
         8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like
         this: '2014-01-01T00:00:00Z'.
        :type created_date_time: ~datetime.datetime
        :param last_modified_date_time: The Timestamp type represents date and time information using
         ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look
         like this: '2014-01-01T00:00:00Z'.
        :type last_modified_date_time: ~datetime.datetime
        :param change_key: Identifies the version of the item. Every time the item is changed,
         changeKey changes as well. This allows Exchange to apply changes to the correct version of the
         object. Read-only.
        :type change_key: str
        :param categories: The categories associated with the item.
        :type categories: list[str]
        :param body: itemBody.
        :type body: ~groups_conversation.models.MicrosoftGraphItemBody
        :param received_date_time: Specifies when the post was received. The DateTimeOffset type
         represents date and time information using ISO 8601 format and is always in UTC time. For
         example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'.
        :type received_date_time: ~datetime.datetime
        :param has_attachments: Indicates whether the post has at least one attachment. This is a
         default property.
        :type has_attachments: bool
        :param microsoft_graph_post_conversation_thread_id_conversation_thread_id: Unique ID of the
         conversation thread. Read-only.
        :type microsoft_graph_post_conversation_thread_id_conversation_thread_id: str
        :param new_participants: Conversation participants that were added to the thread as part of
         this post.
        :type new_participants: list[~groups_conversation.models.MicrosoftGraphRecipient]
        :param microsoft_graph_post_conversation_id: Unique ID of the conversation. Read-only.
        :type microsoft_graph_post_conversation_id: str
        :param importance: importance.
        :type importance: str or ~groups_conversation.models.MicrosoftGraphImportance
        :param in_reply_to: post.
        :type in_reply_to: ~groups_conversation.models.MicrosoftGraphPost
        :param single_value_extended_properties: The collection of single-value extended properties
         defined for the post. Read-only. Nullable.
        :type single_value_extended_properties: list[~groups_conversation.models.MicrosoftGraphSingleValueLegacyExtendedProperty]
        :param multi_value_extended_properties: The collection of multi-value extended properties
         defined for the post. Read-only. Nullable.
        :type multi_value_extended_properties: list[~groups_conversation.models.MicrosoftGraphMultiValueLegacyExtendedProperty]
        :param extensions: The collection of open extensions defined for the post. Read-only. Nullable.
        :type extensions: list[~groups_conversation.models.MicrosoftGraphEntity]
        :param attachments: Read-only. Nullable.
        :type attachments: list[~groups_conversation.models.MicrosoftGraphAttachment]
        :param mentions:
        :type mentions: list[~groups_conversation.models.MicrosoftGraphMention]
        :param name: The display name of the person or entity.
        :type name: str
        :param address: The email address of the person or entity.
        :type address: str
        :param microsoft_graph_email_address_name: The display name of the person or entity.
        :type microsoft_graph_email_address_name: str
        :param microsoft_graph_email_address: The email address of the person or entity.
        :type microsoft_graph_email_address: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphPost, or the result of cls(response)
        :rtype: ~groups_conversation.models.MicrosoftGraphPost
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphPost"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.MicrosoftGraphPost(id=id, created_date_time=created_date_time, last_modified_date_time=last_modified_date_time, change_key=change_key, categories=categories, body=body, received_date_time=received_date_time, has_attachments=has_attachments, conversation_thread_id=microsoft_graph_post_conversation_thread_id_conversation_thread_id, new_participants=new_participants, conversation_id=microsoft_graph_post_conversation_id, importance=importance, in_reply_to=in_reply_to, single_value_extended_properties=single_value_extended_properties, multi_value_extended_properties=multi_value_extended_properties, extensions=extensions, attachments=attachments, mentions=mentions, name_sender_email_address_name=name, address_sender_email_address=address, name_from_email_address_name=microsoft_graph_email_address_name, address_from_email_address=microsoft_graph_email_address)
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.create_post.metadata['url']  # type: ignore
        path_format_arguments = {
            'group-id': self._serialize.url("group_id", group_id, 'str'),
            'conversation-id': self._serialize.url("conversation_id", conversation_id, 'str'),
            'conversationThread-id': self._serialize.url("conversation_thread_id", conversation_thread_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'MicrosoftGraphPost')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphPost', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_post.metadata = {'url': '/groups/{group-id}/conversations/{conversation-id}/threads/{conversationThread-id}/posts'}  # type: ignore

    def get_post(
        self,
        group_id,  # type: str
        conversation_id,  # type: str
        conversation_thread_id,  # type: str
        post_id,  # type: str
        select=None,  # type: Optional[List[Union[str, "models.Enum15"]]]
        expand=None,  # type: Optional[List[Union[str, "models.Get5ItemsItem"]]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphPost"
        """Get posts from groups.

        Get posts from groups.

        :param group_id: key: group-id of group.
        :type group_id: str
        :param conversation_id: key: conversation-id of conversation.
        :type conversation_id: str
        :param conversation_thread_id: key: conversationThread-id of conversationThread.
        :type conversation_thread_id: str
        :param post_id: key: post-id of post.
        :type post_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~groups_conversation.models.Enum15]
        :param expand: Expand related entities.
        :type expand: list[str or ~groups_conversation.models.Get5ItemsItem]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphPost, or the result of cls(response)
        :rtype: ~groups_conversation.models.MicrosoftGraphPost
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphPost"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        # Construct URL
        url = self.get_post.metadata['url']  # type: ignore
        path_format_arguments = {
            'group-id': self._serialize.url("group_id", group_id, 'str'),
            'conversation-id': self._serialize.url("conversation_id", conversation_id, 'str'),
            'conversationThread-id': self._serialize.url("conversation_thread_id", conversation_thread_id, 'str'),
            'post-id': self._serialize.url("post_id", post_id, 'str'),
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

        deserialized = self._deserialize('MicrosoftGraphPost', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_post.metadata = {'url': '/groups/{group-id}/conversations/{conversation-id}/threads/{conversationThread-id}/posts/{post-id}'}  # type: ignore

    def update_post(
        self,
        group_id,  # type: str
        conversation_id,  # type: str
        conversation_thread_id,  # type: str
        post_id,  # type: str
        id=None,  # type: Optional[str]
        created_date_time=None,  # type: Optional[datetime.datetime]
        last_modified_date_time=None,  # type: Optional[datetime.datetime]
        change_key=None,  # type: Optional[str]
        categories=None,  # type: Optional[List[str]]
        body=None,  # type: Optional["models.MicrosoftGraphItemBody"]
        received_date_time=None,  # type: Optional[datetime.datetime]
        has_attachments=None,  # type: Optional[bool]
        microsoft_graph_post_conversation_thread_id_conversation_thread_id=None,  # type: Optional[str]
        new_participants=None,  # type: Optional[List["models.MicrosoftGraphRecipient"]]
        microsoft_graph_post_conversation_id=None,  # type: Optional[str]
        importance=None,  # type: Optional[Union[str, "models.MicrosoftGraphImportance"]]
        in_reply_to=None,  # type: Optional["models.MicrosoftGraphPost"]
        single_value_extended_properties=None,  # type: Optional[List["models.MicrosoftGraphSingleValueLegacyExtendedProperty"]]
        multi_value_extended_properties=None,  # type: Optional[List["models.MicrosoftGraphMultiValueLegacyExtendedProperty"]]
        extensions=None,  # type: Optional[List["models.MicrosoftGraphEntity"]]
        attachments=None,  # type: Optional[List["models.MicrosoftGraphAttachment"]]
        mentions=None,  # type: Optional[List["models.MicrosoftGraphMention"]]
        name=None,  # type: Optional[str]
        address=None,  # type: Optional[str]
        microsoft_graph_email_address_name=None,  # type: Optional[str]
        microsoft_graph_email_address=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Update the navigation property posts in groups.

        Update the navigation property posts in groups.

        :param group_id: key: group-id of group.
        :type group_id: str
        :param conversation_id: key: conversation-id of conversation.
        :type conversation_id: str
        :param conversation_thread_id: key: conversationThread-id of conversationThread.
        :type conversation_thread_id: str
        :param post_id: key: post-id of post.
        :type post_id: str
        :param id: Read-only.
        :type id: str
        :param created_date_time: The Timestamp type represents date and time information using ISO
         8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like
         this: '2014-01-01T00:00:00Z'.
        :type created_date_time: ~datetime.datetime
        :param last_modified_date_time: The Timestamp type represents date and time information using
         ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look
         like this: '2014-01-01T00:00:00Z'.
        :type last_modified_date_time: ~datetime.datetime
        :param change_key: Identifies the version of the item. Every time the item is changed,
         changeKey changes as well. This allows Exchange to apply changes to the correct version of the
         object. Read-only.
        :type change_key: str
        :param categories: The categories associated with the item.
        :type categories: list[str]
        :param body: itemBody.
        :type body: ~groups_conversation.models.MicrosoftGraphItemBody
        :param received_date_time: Specifies when the post was received. The DateTimeOffset type
         represents date and time information using ISO 8601 format and is always in UTC time. For
         example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'.
        :type received_date_time: ~datetime.datetime
        :param has_attachments: Indicates whether the post has at least one attachment. This is a
         default property.
        :type has_attachments: bool
        :param microsoft_graph_post_conversation_thread_id_conversation_thread_id: Unique ID of the
         conversation thread. Read-only.
        :type microsoft_graph_post_conversation_thread_id_conversation_thread_id: str
        :param new_participants: Conversation participants that were added to the thread as part of
         this post.
        :type new_participants: list[~groups_conversation.models.MicrosoftGraphRecipient]
        :param microsoft_graph_post_conversation_id: Unique ID of the conversation. Read-only.
        :type microsoft_graph_post_conversation_id: str
        :param importance: importance.
        :type importance: str or ~groups_conversation.models.MicrosoftGraphImportance
        :param in_reply_to: post.
        :type in_reply_to: ~groups_conversation.models.MicrosoftGraphPost
        :param single_value_extended_properties: The collection of single-value extended properties
         defined for the post. Read-only. Nullable.
        :type single_value_extended_properties: list[~groups_conversation.models.MicrosoftGraphSingleValueLegacyExtendedProperty]
        :param multi_value_extended_properties: The collection of multi-value extended properties
         defined for the post. Read-only. Nullable.
        :type multi_value_extended_properties: list[~groups_conversation.models.MicrosoftGraphMultiValueLegacyExtendedProperty]
        :param extensions: The collection of open extensions defined for the post. Read-only. Nullable.
        :type extensions: list[~groups_conversation.models.MicrosoftGraphEntity]
        :param attachments: Read-only. Nullable.
        :type attachments: list[~groups_conversation.models.MicrosoftGraphAttachment]
        :param mentions:
        :type mentions: list[~groups_conversation.models.MicrosoftGraphMention]
        :param name: The display name of the person or entity.
        :type name: str
        :param address: The email address of the person or entity.
        :type address: str
        :param microsoft_graph_email_address_name: The display name of the person or entity.
        :type microsoft_graph_email_address_name: str
        :param microsoft_graph_email_address: The email address of the person or entity.
        :type microsoft_graph_email_address: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.MicrosoftGraphPost(id=id, created_date_time=created_date_time, last_modified_date_time=last_modified_date_time, change_key=change_key, categories=categories, body=body, received_date_time=received_date_time, has_attachments=has_attachments, conversation_thread_id=microsoft_graph_post_conversation_thread_id_conversation_thread_id, new_participants=new_participants, conversation_id=microsoft_graph_post_conversation_id, importance=importance, in_reply_to=in_reply_to, single_value_extended_properties=single_value_extended_properties, multi_value_extended_properties=multi_value_extended_properties, extensions=extensions, attachments=attachments, mentions=mentions, name_sender_email_address_name=name, address_sender_email_address=address, name_from_email_address_name=microsoft_graph_email_address_name, address_from_email_address=microsoft_graph_email_address)
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.update_post.metadata['url']  # type: ignore
        path_format_arguments = {
            'group-id': self._serialize.url("group_id", group_id, 'str'),
            'conversation-id': self._serialize.url("conversation_id", conversation_id, 'str'),
            'conversationThread-id': self._serialize.url("conversation_thread_id", conversation_thread_id, 'str'),
            'post-id': self._serialize.url("post_id", post_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'MicrosoftGraphPost')
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

    update_post.metadata = {'url': '/groups/{group-id}/conversations/{conversation-id}/threads/{conversationThread-id}/posts/{post-id}'}  # type: ignore
