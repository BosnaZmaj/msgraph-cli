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

class SiteOnenotePageParentSectionOperations(object):
    """SiteOnenotePageParentSectionOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~sites_one_note.models
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

    def list_page(
        self,
        site_id,  # type: str
        onenote_page_id,  # type: str
        orderby=None,  # type: Optional[List[Union[str, "models.Enum141"]]]
        select=None,  # type: Optional[List[Union[str, "models.Enum142"]]]
        expand=None,  # type: Optional[List[Union[str, "models.Enum143"]]]
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["models.CollectionOfOnenotePage4"]
        """Get pages from sites.

        Get pages from sites.

        :param site_id: key: site-id of site.
        :type site_id: str
        :param onenote_page_id: key: onenotePage-id of onenotePage.
        :type onenote_page_id: str
        :param orderby: Order items by property values.
        :type orderby: list[str or ~sites_one_note.models.Enum141]
        :param select: Select properties to be returned.
        :type select: list[str or ~sites_one_note.models.Enum142]
        :param expand: Expand related entities.
        :type expand: list[str or ~sites_one_note.models.Enum143]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either CollectionOfOnenotePage4 or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~sites_one_note.models.CollectionOfOnenotePage4]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.CollectionOfOnenotePage4"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = 'application/json'

            if not next_link:
                # Construct URL
                url = self.list_page.metadata['url']  # type: ignore
                path_format_arguments = {
                    'site-id': self._serialize.url("site_id", site_id, 'str'),
                    'onenotePage-id': self._serialize.url("onenote_page_id", onenote_page_id, 'str'),
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
            deserialized = self._deserialize('CollectionOfOnenotePage4', pipeline_response)
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
    list_page.metadata = {'url': '/sites/{site-id}/onenote/pages/{onenotePage-id}/parentSection/pages'}  # type: ignore

    def create_page(
        self,
        site_id,  # type: str
        onenote_page_id,  # type: str
        body,  # type: "models.MicrosoftGraphOnenotePage"
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphOnenotePage"
        """Create new navigation property to pages for sites.

        Create new navigation property to pages for sites.

        :param site_id: key: site-id of site.
        :type site_id: str
        :param onenote_page_id: key: onenotePage-id of onenotePage.
        :type onenote_page_id: str
        :param body: New navigation property.
        :type body: ~sites_one_note.models.MicrosoftGraphOnenotePage
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphOnenotePage, or the result of cls(response)
        :rtype: ~sites_one_note.models.MicrosoftGraphOnenotePage
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphOnenotePage"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.create_page.metadata['url']  # type: ignore
        path_format_arguments = {
            'site-id': self._serialize.url("site_id", site_id, 'str'),
            'onenotePage-id': self._serialize.url("onenote_page_id", onenote_page_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'MicrosoftGraphOnenotePage')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphOnenotePage', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_page.metadata = {'url': '/sites/{site-id}/onenote/pages/{onenotePage-id}/parentSection/pages'}  # type: ignore

    def get_page(
        self,
        site_id,  # type: str
        onenote_page_id,  # type: str
        onenote_page_id1,  # type: str
        select=None,  # type: Optional[List[Union[str, "models.Enum144"]]]
        expand=None,  # type: Optional[List[Union[str, "models.Enum145"]]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphOnenotePage"
        """Get pages from sites.

        Get pages from sites.

        :param site_id: key: site-id of site.
        :type site_id: str
        :param onenote_page_id: key: onenotePage-id of onenotePage.
        :type onenote_page_id: str
        :param onenote_page_id1: key: onenotePage-id of onenotePage.
        :type onenote_page_id1: str
        :param select: Select properties to be returned.
        :type select: list[str or ~sites_one_note.models.Enum144]
        :param expand: Expand related entities.
        :type expand: list[str or ~sites_one_note.models.Enum145]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphOnenotePage, or the result of cls(response)
        :rtype: ~sites_one_note.models.MicrosoftGraphOnenotePage
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphOnenotePage"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        # Construct URL
        url = self.get_page.metadata['url']  # type: ignore
        path_format_arguments = {
            'site-id': self._serialize.url("site_id", site_id, 'str'),
            'onenotePage-id': self._serialize.url("onenote_page_id", onenote_page_id, 'str'),
            'onenotePage-id1': self._serialize.url("onenote_page_id1", onenote_page_id1, 'str'),
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

        deserialized = self._deserialize('MicrosoftGraphOnenotePage', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_page.metadata = {'url': '/sites/{site-id}/onenote/pages/{onenotePage-id}/parentSection/pages/{onenotePage-id1}'}  # type: ignore

    def update_page(
        self,
        site_id,  # type: str
        onenote_page_id,  # type: str
        onenote_page_id1,  # type: str
        body,  # type: "models.MicrosoftGraphOnenotePage"
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Update the navigation property pages in sites.

        Update the navigation property pages in sites.

        :param site_id: key: site-id of site.
        :type site_id: str
        :param onenote_page_id: key: onenotePage-id of onenotePage.
        :type onenote_page_id: str
        :param onenote_page_id1: key: onenotePage-id of onenotePage.
        :type onenote_page_id1: str
        :param body: New navigation property values.
        :type body: ~sites_one_note.models.MicrosoftGraphOnenotePage
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.update_page.metadata['url']  # type: ignore
        path_format_arguments = {
            'site-id': self._serialize.url("site_id", site_id, 'str'),
            'onenotePage-id': self._serialize.url("onenote_page_id", onenote_page_id, 'str'),
            'onenotePage-id1': self._serialize.url("onenote_page_id1", onenote_page_id1, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'MicrosoftGraphOnenotePage')
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

    update_page.metadata = {'url': '/sites/{site-id}/onenote/pages/{onenotePage-id}/parentSection/pages/{onenotePage-id1}'}  # type: ignore

    def get_parent_notebook(
        self,
        site_id,  # type: str
        onenote_page_id,  # type: str
        select=None,  # type: Optional[List[Union[str, "models.Enum146"]]]
        expand=None,  # type: Optional[List[Union[str, "models.Enum147"]]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphNotebook"
        """Get parentNotebook from sites.

        Get parentNotebook from sites.

        :param site_id: key: site-id of site.
        :type site_id: str
        :param onenote_page_id: key: onenotePage-id of onenotePage.
        :type onenote_page_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~sites_one_note.models.Enum146]
        :param expand: Expand related entities.
        :type expand: list[str or ~sites_one_note.models.Enum147]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphNotebook, or the result of cls(response)
        :rtype: ~sites_one_note.models.MicrosoftGraphNotebook
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphNotebook"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        # Construct URL
        url = self.get_parent_notebook.metadata['url']  # type: ignore
        path_format_arguments = {
            'site-id': self._serialize.url("site_id", site_id, 'str'),
            'onenotePage-id': self._serialize.url("onenote_page_id", onenote_page_id, 'str'),
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

        deserialized = self._deserialize('MicrosoftGraphNotebook', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_parent_notebook.metadata = {'url': '/sites/{site-id}/onenote/pages/{onenotePage-id}/parentSection/parentNotebook'}  # type: ignore

    def update_parent_notebook(
        self,
        site_id,  # type: str
        onenote_page_id,  # type: str
        id=None,  # type: Optional[str]
        self_parameter=None,  # type: Optional[str]
        created_date_time=None,  # type: Optional[datetime.datetime]
        display_name=None,  # type: Optional[str]
        last_modified_date_time=None,  # type: Optional[datetime.datetime]
        application=None,  # type: Optional["models.MicrosoftGraphIdentity"]
        device=None,  # type: Optional["models.MicrosoftGraphIdentity"]
        user=None,  # type: Optional["models.MicrosoftGraphIdentity"]
        microsoft_graph_identity_application=None,  # type: Optional["models.MicrosoftGraphIdentity"]
        microsoft_graph_identity_device=None,  # type: Optional["models.MicrosoftGraphIdentity"]
        microsoft_graph_identity_user=None,  # type: Optional["models.MicrosoftGraphIdentity"]
        is_default=None,  # type: Optional[bool]
        user_role=None,  # type: Optional[Union[str, "models.MicrosoftGraphOnenoteUserRole"]]
        is_shared=None,  # type: Optional[bool]
        sections_url=None,  # type: Optional[str]
        section_groups_url=None,  # type: Optional[str]
        sections=None,  # type: Optional[List["models.MicrosoftGraphOnenoteSection"]]
        section_groups=None,  # type: Optional[List["models.MicrosoftGraphSectionGroup"]]
        one_note_client_url=None,  # type: Optional["models.MicrosoftGraphExternalLink"]
        one_note_web_url=None,  # type: Optional["models.MicrosoftGraphExternalLink"]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Update the navigation property parentNotebook in sites.

        Update the navigation property parentNotebook in sites.

        :param site_id: key: site-id of site.
        :type site_id: str
        :param onenote_page_id: key: onenotePage-id of onenotePage.
        :type onenote_page_id: str
        :param id: Read-only.
        :type id: str
        :param self_parameter: The endpoint where you can get details about the page. Read-only.
        :type self_parameter: str
        :param created_date_time: The date and time when the page was created. The timestamp represents
         date and time information using ISO 8601 format and is always in UTC time. For example,
         midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.
        :type created_date_time: ~datetime.datetime
        :param display_name: The name of the notebook.
        :type display_name: str
        :param last_modified_date_time: The date and time when the notebook was last modified. The
         timestamp represents date and time information using ISO 8601 format and is always in UTC time.
         For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-
         only.
        :type last_modified_date_time: ~datetime.datetime
        :param application: identity.
        :type application: ~sites_one_note.models.MicrosoftGraphIdentity
        :param device: identity.
        :type device: ~sites_one_note.models.MicrosoftGraphIdentity
        :param user: identity.
        :type user: ~sites_one_note.models.MicrosoftGraphIdentity
        :param microsoft_graph_identity_application: identity.
        :type microsoft_graph_identity_application: ~sites_one_note.models.MicrosoftGraphIdentity
        :param microsoft_graph_identity_device: identity.
        :type microsoft_graph_identity_device: ~sites_one_note.models.MicrosoftGraphIdentity
        :param microsoft_graph_identity_user: identity.
        :type microsoft_graph_identity_user: ~sites_one_note.models.MicrosoftGraphIdentity
        :param is_default: Indicates whether this is the user's default notebook. Read-only.
        :type is_default: bool
        :param user_role: onenoteUserRole.
        :type user_role: str or ~sites_one_note.models.MicrosoftGraphOnenoteUserRole
        :param is_shared: Indicates whether the notebook is shared. If true, the contents of the
         notebook can be seen by people other than the owner. Read-only.
        :type is_shared: bool
        :param sections_url: The URL for the sections navigation property, which returns all the
         sections in the notebook. Read-only.
        :type sections_url: str
        :param section_groups_url: The URL for the sectionGroups navigation property, which returns all
         the section groups in the notebook. Read-only.
        :type section_groups_url: str
        :param sections: The sections in the notebook. Read-only. Nullable.
        :type sections: list[~sites_one_note.models.MicrosoftGraphOnenoteSection]
        :param section_groups: The section groups in the notebook. Read-only. Nullable.
        :type section_groups: list[~sites_one_note.models.MicrosoftGraphSectionGroup]
        :param one_note_client_url: externalLink.
        :type one_note_client_url: ~sites_one_note.models.MicrosoftGraphExternalLink
        :param one_note_web_url: externalLink.
        :type one_note_web_url: ~sites_one_note.models.MicrosoftGraphExternalLink
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.MicrosoftGraphNotebook(id=id, self_property=self_parameter, created_date_time=created_date_time, display_name=display_name, last_modified_date_time=last_modified_date_time, application_last_modified_by_application=application, device_last_modified_by_device=device, user_last_modified_by_user=user, application_created_by_application=microsoft_graph_identity_application, device_created_by_device=microsoft_graph_identity_device, user_created_by_user=microsoft_graph_identity_user, is_default=is_default, user_role=user_role, is_shared=is_shared, sections_url=sections_url, section_groups_url=section_groups_url, sections=sections, section_groups=section_groups, one_note_client_url=one_note_client_url, one_note_web_url=one_note_web_url)
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.update_parent_notebook.metadata['url']  # type: ignore
        path_format_arguments = {
            'site-id': self._serialize.url("site_id", site_id, 'str'),
            'onenotePage-id': self._serialize.url("onenote_page_id", onenote_page_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'MicrosoftGraphNotebook')
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

    update_parent_notebook.metadata = {'url': '/sites/{site-id}/onenote/pages/{onenotePage-id}/parentSection/parentNotebook'}  # type: ignore

    def get_parent_section_group(
        self,
        site_id,  # type: str
        onenote_page_id,  # type: str
        select=None,  # type: Optional[List[Union[str, "models.Enum172"]]]
        expand=None,  # type: Optional[List[Union[str, "models.Enum173"]]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphSectionGroup"
        """Get parentSectionGroup from sites.

        Get parentSectionGroup from sites.

        :param site_id: key: site-id of site.
        :type site_id: str
        :param onenote_page_id: key: onenotePage-id of onenotePage.
        :type onenote_page_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~sites_one_note.models.Enum172]
        :param expand: Expand related entities.
        :type expand: list[str or ~sites_one_note.models.Enum173]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphSectionGroup, or the result of cls(response)
        :rtype: ~sites_one_note.models.MicrosoftGraphSectionGroup
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphSectionGroup"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        # Construct URL
        url = self.get_parent_section_group.metadata['url']  # type: ignore
        path_format_arguments = {
            'site-id': self._serialize.url("site_id", site_id, 'str'),
            'onenotePage-id': self._serialize.url("onenote_page_id", onenote_page_id, 'str'),
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

        deserialized = self._deserialize('MicrosoftGraphSectionGroup', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_parent_section_group.metadata = {'url': '/sites/{site-id}/onenote/pages/{onenotePage-id}/parentSection/parentSectionGroup'}  # type: ignore

    def update_parent_section_group(
        self,
        site_id,  # type: str
        onenote_page_id,  # type: str
        id=None,  # type: Optional[str]
        self_parameter=None,  # type: Optional[str]
        created_date_time=None,  # type: Optional[datetime.datetime]
        display_name=None,  # type: Optional[str]
        last_modified_date_time=None,  # type: Optional[datetime.datetime]
        application=None,  # type: Optional["models.MicrosoftGraphIdentity"]
        device=None,  # type: Optional["models.MicrosoftGraphIdentity"]
        user=None,  # type: Optional["models.MicrosoftGraphIdentity"]
        microsoft_graph_identity_application=None,  # type: Optional["models.MicrosoftGraphIdentity"]
        microsoft_graph_identity_device=None,  # type: Optional["models.MicrosoftGraphIdentity"]
        microsoft_graph_identity_user=None,  # type: Optional["models.MicrosoftGraphIdentity"]
        sections_url=None,  # type: Optional[str]
        section_groups_url=None,  # type: Optional[str]
        parent_notebook=None,  # type: Optional["models.MicrosoftGraphNotebook"]
        parent_section_group=None,  # type: Optional["models.MicrosoftGraphSectionGroup"]
        sections=None,  # type: Optional[List["models.MicrosoftGraphOnenoteSection"]]
        section_groups=None,  # type: Optional[List["models.MicrosoftGraphSectionGroup"]]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Update the navigation property parentSectionGroup in sites.

        Update the navigation property parentSectionGroup in sites.

        :param site_id: key: site-id of site.
        :type site_id: str
        :param onenote_page_id: key: onenotePage-id of onenotePage.
        :type onenote_page_id: str
        :param id: Read-only.
        :type id: str
        :param self_parameter: The endpoint where you can get details about the page. Read-only.
        :type self_parameter: str
        :param created_date_time: The date and time when the page was created. The timestamp represents
         date and time information using ISO 8601 format and is always in UTC time. For example,
         midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.
        :type created_date_time: ~datetime.datetime
        :param display_name: The name of the notebook.
        :type display_name: str
        :param last_modified_date_time: The date and time when the notebook was last modified. The
         timestamp represents date and time information using ISO 8601 format and is always in UTC time.
         For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-
         only.
        :type last_modified_date_time: ~datetime.datetime
        :param application: identity.
        :type application: ~sites_one_note.models.MicrosoftGraphIdentity
        :param device: identity.
        :type device: ~sites_one_note.models.MicrosoftGraphIdentity
        :param user: identity.
        :type user: ~sites_one_note.models.MicrosoftGraphIdentity
        :param microsoft_graph_identity_application: identity.
        :type microsoft_graph_identity_application: ~sites_one_note.models.MicrosoftGraphIdentity
        :param microsoft_graph_identity_device: identity.
        :type microsoft_graph_identity_device: ~sites_one_note.models.MicrosoftGraphIdentity
        :param microsoft_graph_identity_user: identity.
        :type microsoft_graph_identity_user: ~sites_one_note.models.MicrosoftGraphIdentity
        :param sections_url: The URL for the sections navigation property, which returns all the
         sections in the section group. Read-only.
        :type sections_url: str
        :param section_groups_url: The URL for the sectionGroups navigation property, which returns all
         the section groups in the section group. Read-only.
        :type section_groups_url: str
        :param parent_notebook: notebook.
        :type parent_notebook: ~sites_one_note.models.MicrosoftGraphNotebook
        :param parent_section_group: sectionGroup.
        :type parent_section_group: ~sites_one_note.models.MicrosoftGraphSectionGroup
        :param sections: The sections in the section group. Read-only. Nullable.
        :type sections: list[~sites_one_note.models.MicrosoftGraphOnenoteSection]
        :param section_groups: The section groups in the section. Read-only. Nullable.
        :type section_groups: list[~sites_one_note.models.MicrosoftGraphSectionGroup]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.MicrosoftGraphSectionGroup(id=id, self_property=self_parameter, created_date_time=created_date_time, display_name=display_name, last_modified_date_time=last_modified_date_time, application_last_modified_by_application=application, device_last_modified_by_device=device, user_last_modified_by_user=user, application_created_by_application=microsoft_graph_identity_application, device_created_by_device=microsoft_graph_identity_device, user_created_by_user=microsoft_graph_identity_user, sections_url=sections_url, section_groups_url=section_groups_url, parent_notebook=parent_notebook, parent_section_group=parent_section_group, sections=sections, section_groups=section_groups)
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.update_parent_section_group.metadata['url']  # type: ignore
        path_format_arguments = {
            'site-id': self._serialize.url("site_id", site_id, 'str'),
            'onenotePage-id': self._serialize.url("onenote_page_id", onenote_page_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'MicrosoftGraphSectionGroup')
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

    update_parent_section_group.metadata = {'url': '/sites/{site-id}/onenote/pages/{onenotePage-id}/parentSection/parentSectionGroup'}  # type: ignore
