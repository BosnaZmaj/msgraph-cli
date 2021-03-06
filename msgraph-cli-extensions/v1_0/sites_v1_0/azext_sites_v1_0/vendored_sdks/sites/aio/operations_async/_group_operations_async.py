# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import datetime
from typing import Any, AsyncIterable, Callable, Dict, Generic, List, Optional, TypeVar, Union
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class GroupOperations:
    """GroupOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~sites.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def list_site(
        self,
        group_id: str,
        orderby: Optional[List[Union[str, "models.Get6ItemsItem"]]] = None,
        select: Optional[List[Union[str, "models.Get7ItemsItem"]]] = None,
        expand: Optional[List[Union[str, "models.Get8ItemsItem"]]] = None,
        **kwargs
    ) -> AsyncIterable["models.CollectionOfSite"]:
        """Get sites from groups.

        Get sites from groups.

        :param group_id: key: id of group.
        :type group_id: str
        :param orderby: Order items by property values.
        :type orderby: list[str or ~sites.models.Get6ItemsItem]
        :param select: Select properties to be returned.
        :type select: list[str or ~sites.models.Get7ItemsItem]
        :param expand: Expand related entities.
        :type expand: list[str or ~sites.models.Get8ItemsItem]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either CollectionOfSite or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~sites.models.CollectionOfSite]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.CollectionOfSite"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')
            header_parameters['Accept'] = 'application/json'

            if not next_link:
                # Construct URL
                url = self.list_site.metadata['url']  # type: ignore
                path_format_arguments = {
                    'group-id': self._serialize.url("group_id", group_id, 'str'),
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

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('CollectionOfSite', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.odata_next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize(models.OdataError, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    list_site.metadata = {'url': '/groups/{group-id}/sites'}  # type: ignore

    async def create_site(
        self,
        group_id: str,
        id: Optional[str] = None,
        created_date_time: Optional[datetime.datetime] = None,
        description: Optional[str] = None,
        e_tag: Optional[str] = None,
        last_modified_date_time: Optional[datetime.datetime] = None,
        name: Optional[str] = None,
        web_url: Optional[str] = None,
        created_by_user: Optional["models.MicrosoftGraphUser"] = None,
        last_modified_by_user: Optional["models.MicrosoftGraphUser"] = None,
        drive_id: Optional[str] = None,
        drive_type: Optional[str] = None,
        microsoft_graph_item_reference_id: Optional[str] = None,
        microsoft_graph_item_reference_name: Optional[str] = None,
        path: Optional[str] = None,
        share_id: Optional[str] = None,
        sharepoint_ids: Optional["models.MicrosoftGraphSharepointIds"] = None,
        site_id: Optional[str] = None,
        application: Optional["models.MicrosoftGraphIdentity"] = None,
        device: Optional["models.MicrosoftGraphIdentity"] = None,
        user: Optional["models.MicrosoftGraphIdentity"] = None,
        microsoft_graph_identity_application: Optional["models.MicrosoftGraphIdentity"] = None,
        microsoft_graph_identity_device: Optional["models.MicrosoftGraphIdentity"] = None,
        microsoft_graph_identity_user: Optional["models.MicrosoftGraphIdentity"] = None,
        display_name: Optional[str] = None,
        root: Optional[Dict[str, object]] = None,
        microsoft_graph_sharepoint_ids: Optional["models.MicrosoftGraphSharepointIds"] = None,
        analytics: Optional["models.MicrosoftGraphItemAnalytics"] = None,
        columns: Optional[List["models.MicrosoftGraphColumnDefinition"]] = None,
        content_types: Optional[List["models.MicrosoftGraphContentType"]] = None,
        drive: Optional["models.MicrosoftGraphDrive"] = None,
        drives: Optional[List["models.MicrosoftGraphDrive"]] = None,
        items: Optional[List["models.MicrosoftGraphBaseItem"]] = None,
        lists: Optional[List["models.MicrosoftGraphList"]] = None,
        sites: Optional[List["models.MicrosoftGraphSite"]] = None,
        microsoft_graph_entity_id: Optional[str] = None,
        notebooks: Optional[List["models.MicrosoftGraphNotebook"]] = None,
        operations: Optional[List["models.MicrosoftGraphOnenoteOperation"]] = None,
        pages: Optional[List["models.MicrosoftGraphOnenotePage"]] = None,
        resources: Optional[List["models.MicrosoftGraphOnenoteResource"]] = None,
        section_groups: Optional[List["models.MicrosoftGraphSectionGroup"]] = None,
        sections: Optional[List["models.MicrosoftGraphOnenoteSection"]] = None,
        data_location_code: Optional[str] = None,
        hostname: Optional[str] = None,
        microsoft_graph_root: Optional[Dict[str, object]] = None,
        code: Optional[str] = None,
        details: Optional[List["models.MicrosoftGraphPublicErrorDetail"]] = None,
        inner_error: Optional["models.MicrosoftGraphPublicInnerError"] = None,
        message: Optional[str] = None,
        target: Optional[str] = None,
        **kwargs
    ) -> "models.MicrosoftGraphSite":
        """Create new navigation property to sites for groups.

        Create new navigation property to sites for groups.

        :param group_id: key: id of group.
        :type group_id: str
        :param id: Read-only.
        :type id: str
        :param created_date_time: Date and time of item creation. Read-only.
        :type created_date_time: ~datetime.datetime
        :param description: Provides a user-visible description of the item. Optional.
        :type description: str
        :param e_tag: ETag for the item. Read-only.
        :type e_tag: str
        :param last_modified_date_time: Date and time the item was last modified. Read-only.
        :type last_modified_date_time: ~datetime.datetime
        :param name: The name of the item. Read-write.
        :type name: str
        :param web_url: URL that displays the resource in the browser. Read-only.
        :type web_url: str
        :param created_by_user: Represents an Azure Active Directory user object.
        :type created_by_user: ~sites.models.MicrosoftGraphUser
        :param last_modified_by_user: Represents an Azure Active Directory user object.
        :type last_modified_by_user: ~sites.models.MicrosoftGraphUser
        :param drive_id: Unique identifier of the drive instance that contains the item. Read-only.
        :type drive_id: str
        :param drive_type: Identifies the type of drive. See [drive][] resource for values.
        :type drive_type: str
        :param microsoft_graph_item_reference_id: Unique identifier of the item in the drive. Read-
         only.
        :type microsoft_graph_item_reference_id: str
        :param microsoft_graph_item_reference_name: The name of the item being referenced. Read-only.
        :type microsoft_graph_item_reference_name: str
        :param path: Path that can be used to navigate to the item. Read-only.
        :type path: str
        :param share_id: A unique identifier for a shared resource that can be accessed via the
         [Shares][] API.
        :type share_id: str
        :param sharepoint_ids: sharepointIds.
        :type sharepoint_ids: ~sites.models.MicrosoftGraphSharepointIds
        :param site_id:
        :type site_id: str
        :param application: identity.
        :type application: ~sites.models.MicrosoftGraphIdentity
        :param device: identity.
        :type device: ~sites.models.MicrosoftGraphIdentity
        :param user: identity.
        :type user: ~sites.models.MicrosoftGraphIdentity
        :param microsoft_graph_identity_application: identity.
        :type microsoft_graph_identity_application: ~sites.models.MicrosoftGraphIdentity
        :param microsoft_graph_identity_device: identity.
        :type microsoft_graph_identity_device: ~sites.models.MicrosoftGraphIdentity
        :param microsoft_graph_identity_user: identity.
        :type microsoft_graph_identity_user: ~sites.models.MicrosoftGraphIdentity
        :param display_name: The full title for the site. Read-only.
        :type display_name: str
        :param root: root.
        :type root: dict[str, object]
        :param microsoft_graph_sharepoint_ids: sharepointIds.
        :type microsoft_graph_sharepoint_ids: ~sites.models.MicrosoftGraphSharepointIds
        :param analytics: itemAnalytics.
        :type analytics: ~sites.models.MicrosoftGraphItemAnalytics
        :param columns: The collection of column definitions reusable across lists under this site.
        :type columns: list[~sites.models.MicrosoftGraphColumnDefinition]
        :param content_types: The collection of content types defined for this site.
        :type content_types: list[~sites.models.MicrosoftGraphContentType]
        :param drive: drive.
        :type drive: ~sites.models.MicrosoftGraphDrive
        :param drives: The collection of drives (document libraries) under this site.
        :type drives: list[~sites.models.MicrosoftGraphDrive]
        :param items: Used to address any item contained in this site. This collection cannot be
         enumerated.
        :type items: list[~sites.models.MicrosoftGraphBaseItem]
        :param lists: The collection of lists under this site.
        :type lists: list[~sites.models.MicrosoftGraphList]
        :param sites: The collection of the sub-sites under this site.
        :type sites: list[~sites.models.MicrosoftGraphSite]
        :param microsoft_graph_entity_id: Read-only.
        :type microsoft_graph_entity_id: str
        :param notebooks: The collection of OneNote notebooks that are owned by the user or group.
         Read-only. Nullable.
        :type notebooks: list[~sites.models.MicrosoftGraphNotebook]
        :param operations: The status of OneNote operations. Getting an operations collection is not
         supported, but you can get the status of long-running operations if the Operation-Location
         header is returned in the response. Read-only. Nullable.
        :type operations: list[~sites.models.MicrosoftGraphOnenoteOperation]
        :param pages: The pages in all OneNote notebooks that are owned by the user or group.  Read-
         only. Nullable.
        :type pages: list[~sites.models.MicrosoftGraphOnenotePage]
        :param resources: The image and other file resources in OneNote pages. Getting a resources
         collection is not supported, but you can get the binary content of a specific resource. Read-
         only. Nullable.
        :type resources: list[~sites.models.MicrosoftGraphOnenoteResource]
        :param section_groups: The section groups in all OneNote notebooks that are owned by the user
         or group.  Read-only. Nullable.
        :type section_groups: list[~sites.models.MicrosoftGraphSectionGroup]
        :param sections: The sections in all OneNote notebooks that are owned by the user or group.
         Read-only. Nullable.
        :type sections: list[~sites.models.MicrosoftGraphOnenoteSection]
        :param data_location_code: The geographic region code for where this site collection resides.
         Read-only.
        :type data_location_code: str
        :param hostname: The hostname for the site collection. Read-only.
        :type hostname: str
        :param microsoft_graph_root: root.
        :type microsoft_graph_root: dict[str, object]
        :param code:
        :type code: str
        :param details:
        :type details: list[~sites.models.MicrosoftGraphPublicErrorDetail]
        :param inner_error: publicInnerError.
        :type inner_error: ~sites.models.MicrosoftGraphPublicInnerError
        :param message:
        :type message: str
        :param target:
        :type target: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphSite, or the result of cls(response)
        :rtype: ~sites.models.MicrosoftGraphSite
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphSite"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.MicrosoftGraphSite(id=id, created_date_time=created_date_time, description=description, e_tag=e_tag, last_modified_date_time=last_modified_date_time, name=name, web_url=web_url, created_by_user=created_by_user, last_modified_by_user=last_modified_by_user, drive_id=drive_id, drive_type=drive_type, id_parent_reference_id=microsoft_graph_item_reference_id, name_parent_reference_name=microsoft_graph_item_reference_name, path=path, share_id=share_id, sharepoint_ids=sharepoint_ids, site_id=site_id, application_last_modified_by_application=application, device_last_modified_by_device=device, user_last_modified_by_user=user, application_created_by_application=microsoft_graph_identity_application, device_created_by_device=microsoft_graph_identity_device, user_created_by_user=microsoft_graph_identity_user, display_name=display_name, root=root, sharepoint_ids=microsoft_graph_sharepoint_ids, analytics=analytics, columns=columns, content_types=content_types, drive=drive, drives=drives, items=items, lists=lists, sites=sites, id_onenote_id=microsoft_graph_entity_id, notebooks=notebooks, operations=operations, pages=pages, resources=resources, section_groups=section_groups, sections=sections, data_location_code=data_location_code, hostname=hostname, root_site_collection_root=microsoft_graph_root, code=code, details=details, inner_error=inner_error, message=message, target=target)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.create_site.metadata['url']  # type: ignore
        path_format_arguments = {
            'group-id': self._serialize.url("group_id", group_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')
        header_parameters['Accept'] = 'application/json'

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'MicrosoftGraphSite')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphSite', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_site.metadata = {'url': '/groups/{group-id}/sites'}  # type: ignore

    async def get_site(
        self,
        group_id: str,
        site_id: str,
        select: Optional[List[Union[str, "models.Get2ItemsItem"]]] = None,
        expand: Optional[List[Union[str, "models.Get3ItemsItem"]]] = None,
        **kwargs
    ) -> "models.MicrosoftGraphSite":
        """Get sites from groups.

        Get sites from groups.

        :param group_id: key: id of group.
        :type group_id: str
        :param site_id: key: id of site.
        :type site_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~sites.models.Get2ItemsItem]
        :param expand: Expand related entities.
        :type expand: list[str or ~sites.models.Get3ItemsItem]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphSite, or the result of cls(response)
        :rtype: ~sites.models.MicrosoftGraphSite
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphSite"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_site.metadata['url']  # type: ignore
        path_format_arguments = {
            'group-id': self._serialize.url("group_id", group_id, 'str'),
            'site-id': self._serialize.url("site_id", site_id, 'str'),
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
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')
        header_parameters['Accept'] = 'application/json'

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphSite', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_site.metadata = {'url': '/groups/{group-id}/sites/{site-id}'}  # type: ignore

    async def update_site(
        self,
        group_id: str,
        site_id: str,
        id: Optional[str] = None,
        created_date_time: Optional[datetime.datetime] = None,
        description: Optional[str] = None,
        e_tag: Optional[str] = None,
        last_modified_date_time: Optional[datetime.datetime] = None,
        name: Optional[str] = None,
        web_url: Optional[str] = None,
        created_by_user: Optional["models.MicrosoftGraphUser"] = None,
        last_modified_by_user: Optional["models.MicrosoftGraphUser"] = None,
        drive_id: Optional[str] = None,
        drive_type: Optional[str] = None,
        microsoft_graph_item_reference_id: Optional[str] = None,
        microsoft_graph_item_reference_name: Optional[str] = None,
        path: Optional[str] = None,
        share_id: Optional[str] = None,
        sharepoint_ids: Optional["models.MicrosoftGraphSharepointIds"] = None,
        microsoft_graph_item_reference_site_id: Optional[str] = None,
        application: Optional["models.MicrosoftGraphIdentity"] = None,
        device: Optional["models.MicrosoftGraphIdentity"] = None,
        user: Optional["models.MicrosoftGraphIdentity"] = None,
        microsoft_graph_identity_application: Optional["models.MicrosoftGraphIdentity"] = None,
        microsoft_graph_identity_device: Optional["models.MicrosoftGraphIdentity"] = None,
        microsoft_graph_identity_user: Optional["models.MicrosoftGraphIdentity"] = None,
        display_name: Optional[str] = None,
        root: Optional[Dict[str, object]] = None,
        microsoft_graph_sharepoint_ids: Optional["models.MicrosoftGraphSharepointIds"] = None,
        analytics: Optional["models.MicrosoftGraphItemAnalytics"] = None,
        columns: Optional[List["models.MicrosoftGraphColumnDefinition"]] = None,
        content_types: Optional[List["models.MicrosoftGraphContentType"]] = None,
        drive: Optional["models.MicrosoftGraphDrive"] = None,
        drives: Optional[List["models.MicrosoftGraphDrive"]] = None,
        items: Optional[List["models.MicrosoftGraphBaseItem"]] = None,
        lists: Optional[List["models.MicrosoftGraphList"]] = None,
        sites: Optional[List["models.MicrosoftGraphSite"]] = None,
        microsoft_graph_entity_id: Optional[str] = None,
        notebooks: Optional[List["models.MicrosoftGraphNotebook"]] = None,
        operations: Optional[List["models.MicrosoftGraphOnenoteOperation"]] = None,
        pages: Optional[List["models.MicrosoftGraphOnenotePage"]] = None,
        resources: Optional[List["models.MicrosoftGraphOnenoteResource"]] = None,
        section_groups: Optional[List["models.MicrosoftGraphSectionGroup"]] = None,
        sections: Optional[List["models.MicrosoftGraphOnenoteSection"]] = None,
        data_location_code: Optional[str] = None,
        hostname: Optional[str] = None,
        microsoft_graph_root: Optional[Dict[str, object]] = None,
        code: Optional[str] = None,
        details: Optional[List["models.MicrosoftGraphPublicErrorDetail"]] = None,
        inner_error: Optional["models.MicrosoftGraphPublicInnerError"] = None,
        message: Optional[str] = None,
        target: Optional[str] = None,
        **kwargs
    ) -> None:
        """Update the navigation property sites in groups.

        Update the navigation property sites in groups.

        :param group_id: key: id of group.
        :type group_id: str
        :param site_id: key: id of site.
        :type site_id: str
        :param id: Read-only.
        :type id: str
        :param created_date_time: Date and time of item creation. Read-only.
        :type created_date_time: ~datetime.datetime
        :param description: Provides a user-visible description of the item. Optional.
        :type description: str
        :param e_tag: ETag for the item. Read-only.
        :type e_tag: str
        :param last_modified_date_time: Date and time the item was last modified. Read-only.
        :type last_modified_date_time: ~datetime.datetime
        :param name: The name of the item. Read-write.
        :type name: str
        :param web_url: URL that displays the resource in the browser. Read-only.
        :type web_url: str
        :param created_by_user: Represents an Azure Active Directory user object.
        :type created_by_user: ~sites.models.MicrosoftGraphUser
        :param last_modified_by_user: Represents an Azure Active Directory user object.
        :type last_modified_by_user: ~sites.models.MicrosoftGraphUser
        :param drive_id: Unique identifier of the drive instance that contains the item. Read-only.
        :type drive_id: str
        :param drive_type: Identifies the type of drive. See [drive][] resource for values.
        :type drive_type: str
        :param microsoft_graph_item_reference_id: Unique identifier of the item in the drive. Read-
         only.
        :type microsoft_graph_item_reference_id: str
        :param microsoft_graph_item_reference_name: The name of the item being referenced. Read-only.
        :type microsoft_graph_item_reference_name: str
        :param path: Path that can be used to navigate to the item. Read-only.
        :type path: str
        :param share_id: A unique identifier for a shared resource that can be accessed via the
         [Shares][] API.
        :type share_id: str
        :param sharepoint_ids: sharepointIds.
        :type sharepoint_ids: ~sites.models.MicrosoftGraphSharepointIds
        :param microsoft_graph_item_reference_site_id:
        :type microsoft_graph_item_reference_site_id: str
        :param application: identity.
        :type application: ~sites.models.MicrosoftGraphIdentity
        :param device: identity.
        :type device: ~sites.models.MicrosoftGraphIdentity
        :param user: identity.
        :type user: ~sites.models.MicrosoftGraphIdentity
        :param microsoft_graph_identity_application: identity.
        :type microsoft_graph_identity_application: ~sites.models.MicrosoftGraphIdentity
        :param microsoft_graph_identity_device: identity.
        :type microsoft_graph_identity_device: ~sites.models.MicrosoftGraphIdentity
        :param microsoft_graph_identity_user: identity.
        :type microsoft_graph_identity_user: ~sites.models.MicrosoftGraphIdentity
        :param display_name: The full title for the site. Read-only.
        :type display_name: str
        :param root: root.
        :type root: dict[str, object]
        :param microsoft_graph_sharepoint_ids: sharepointIds.
        :type microsoft_graph_sharepoint_ids: ~sites.models.MicrosoftGraphSharepointIds
        :param analytics: itemAnalytics.
        :type analytics: ~sites.models.MicrosoftGraphItemAnalytics
        :param columns: The collection of column definitions reusable across lists under this site.
        :type columns: list[~sites.models.MicrosoftGraphColumnDefinition]
        :param content_types: The collection of content types defined for this site.
        :type content_types: list[~sites.models.MicrosoftGraphContentType]
        :param drive: drive.
        :type drive: ~sites.models.MicrosoftGraphDrive
        :param drives: The collection of drives (document libraries) under this site.
        :type drives: list[~sites.models.MicrosoftGraphDrive]
        :param items: Used to address any item contained in this site. This collection cannot be
         enumerated.
        :type items: list[~sites.models.MicrosoftGraphBaseItem]
        :param lists: The collection of lists under this site.
        :type lists: list[~sites.models.MicrosoftGraphList]
        :param sites: The collection of the sub-sites under this site.
        :type sites: list[~sites.models.MicrosoftGraphSite]
        :param microsoft_graph_entity_id: Read-only.
        :type microsoft_graph_entity_id: str
        :param notebooks: The collection of OneNote notebooks that are owned by the user or group.
         Read-only. Nullable.
        :type notebooks: list[~sites.models.MicrosoftGraphNotebook]
        :param operations: The status of OneNote operations. Getting an operations collection is not
         supported, but you can get the status of long-running operations if the Operation-Location
         header is returned in the response. Read-only. Nullable.
        :type operations: list[~sites.models.MicrosoftGraphOnenoteOperation]
        :param pages: The pages in all OneNote notebooks that are owned by the user or group.  Read-
         only. Nullable.
        :type pages: list[~sites.models.MicrosoftGraphOnenotePage]
        :param resources: The image and other file resources in OneNote pages. Getting a resources
         collection is not supported, but you can get the binary content of a specific resource. Read-
         only. Nullable.
        :type resources: list[~sites.models.MicrosoftGraphOnenoteResource]
        :param section_groups: The section groups in all OneNote notebooks that are owned by the user
         or group.  Read-only. Nullable.
        :type section_groups: list[~sites.models.MicrosoftGraphSectionGroup]
        :param sections: The sections in all OneNote notebooks that are owned by the user or group.
         Read-only. Nullable.
        :type sections: list[~sites.models.MicrosoftGraphOnenoteSection]
        :param data_location_code: The geographic region code for where this site collection resides.
         Read-only.
        :type data_location_code: str
        :param hostname: The hostname for the site collection. Read-only.
        :type hostname: str
        :param microsoft_graph_root: root.
        :type microsoft_graph_root: dict[str, object]
        :param code:
        :type code: str
        :param details:
        :type details: list[~sites.models.MicrosoftGraphPublicErrorDetail]
        :param inner_error: publicInnerError.
        :type inner_error: ~sites.models.MicrosoftGraphPublicInnerError
        :param message:
        :type message: str
        :param target:
        :type target: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.MicrosoftGraphSite(id=id, created_date_time=created_date_time, description=description, e_tag=e_tag, last_modified_date_time=last_modified_date_time, name=name, web_url=web_url, created_by_user=created_by_user, last_modified_by_user=last_modified_by_user, drive_id=drive_id, drive_type=drive_type, id_parent_reference_id=microsoft_graph_item_reference_id, name_parent_reference_name=microsoft_graph_item_reference_name, path=path, share_id=share_id, sharepoint_ids=sharepoint_ids, site_id=microsoft_graph_item_reference_site_id, application_last_modified_by_application=application, device_last_modified_by_device=device, user_last_modified_by_user=user, application_created_by_application=microsoft_graph_identity_application, device_created_by_device=microsoft_graph_identity_device, user_created_by_user=microsoft_graph_identity_user, display_name=display_name, root=root, sharepoint_ids=microsoft_graph_sharepoint_ids, analytics=analytics, columns=columns, content_types=content_types, drive=drive, drives=drives, items=items, lists=lists, sites=sites, id_onenote_id=microsoft_graph_entity_id, notebooks=notebooks, operations=operations, pages=pages, resources=resources, section_groups=section_groups, sections=sections, data_location_code=data_location_code, hostname=hostname, root_site_collection_root=microsoft_graph_root, code=code, details=details, inner_error=inner_error, message=message, target=target)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.update_site.metadata['url']  # type: ignore
        path_format_arguments = {
            'group-id': self._serialize.url("group_id", group_id, 'str'),
            'site-id': self._serialize.url("site_id", site_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'MicrosoftGraphSite')
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    update_site.metadata = {'url': '/groups/{group-id}/sites/{site-id}'}  # type: ignore

    async def delete_site(
        self,
        group_id: str,
        site_id: str,
        if_match: Optional[str] = None,
        **kwargs
    ) -> None:
        """Delete navigation property sites for groups.

        Delete navigation property sites for groups.

        :param group_id: key: id of group.
        :type group_id: str
        :param site_id: key: id of site.
        :type site_id: str
        :param if_match: ETag.
        :type if_match: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.delete_site.metadata['url']  # type: ignore
        path_format_arguments = {
            'group-id': self._serialize.url("group_id", group_id, 'str'),
            'site-id': self._serialize.url("site_id", site_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if if_match is not None:
            header_parameters['If-Match'] = self._serialize.header("if_match", if_match, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete_site.metadata = {'url': '/groups/{group-id}/sites/{site-id}'}  # type: ignore
