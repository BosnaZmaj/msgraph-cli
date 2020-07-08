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

class UserTeamworkOperations(object):
    """UserTeamworkOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~teams_teamwork.models
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

    def list_installed_app(
        self,
        user_id,  # type: str
        orderby=None,  # type: Optional[List[Union[str, "models.Get6ItemsItem"]]]
        select=None,  # type: Optional[List[Union[str, "models.Get7ItemsItem"]]]
        expand=None,  # type: Optional[List[Union[str, "models.Get8ItemsItem"]]]
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["models.CollectionOfTeamsAppInstallation"]
        """Get installedApps from users.

        Get installedApps from users.

        :param user_id: key: user-id of user.
        :type user_id: str
        :param orderby: Order items by property values.
        :type orderby: list[str or ~teams_teamwork.models.Get6ItemsItem]
        :param select: Select properties to be returned.
        :type select: list[str or ~teams_teamwork.models.Get7ItemsItem]
        :param expand: Expand related entities.
        :type expand: list[str or ~teams_teamwork.models.Get8ItemsItem]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either CollectionOfTeamsAppInstallation or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~teams_teamwork.models.CollectionOfTeamsAppInstallation]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.CollectionOfTeamsAppInstallation"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = 'application/json'

            if not next_link:
                # Construct URL
                url = self.list_installed_app.metadata['url']  # type: ignore
                path_format_arguments = {
                    'user-id': self._serialize.url("user_id", user_id, 'str'),
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
            deserialized = self._deserialize('CollectionOfTeamsAppInstallation', pipeline_response)
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
    list_installed_app.metadata = {'url': '/users/{user-id}/teamwork/installedApps'}  # type: ignore

    def create_installed_app(
        self,
        user_id,  # type: str
        id=None,  # type: Optional[str]
        teams_app_definition=None,  # type: Optional["models.MicrosoftGraphTeamsAppDefinition"]
        microsoft_graph_entity_id=None,  # type: Optional[str]
        external_id=None,  # type: Optional[str]
        name=None,  # type: Optional[str]
        display_name=None,  # type: Optional[str]
        distribution_method=None,  # type: Optional[Union[str, "models.MicrosoftGraphTeamsAppDistributionMethod"]]
        app_definitions=None,  # type: Optional[List["models.MicrosoftGraphTeamsAppDefinition"]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphTeamsAppInstallation"
        """Create new navigation property to installedApps for users.

        Create new navigation property to installedApps for users.

        :param user_id: key: user-id of user.
        :type user_id: str
        :param id: Read-only.
        :type id: str
        :param teams_app_definition: teamsAppDefinition.
        :type teams_app_definition: ~teams_teamwork.models.MicrosoftGraphTeamsAppDefinition
        :param microsoft_graph_entity_id: Read-only.
        :type microsoft_graph_entity_id: str
        :param external_id: The ID of the catalog provided by the app developer in the Microsoft Teams
         zip app package.
        :type external_id: str
        :param name:
        :type name: str
        :param display_name: The name of the catalog app provided by the app developer in the Microsoft
         Teams zip app package.
        :type display_name: str
        :param distribution_method: teamsAppDistributionMethod.
        :type distribution_method: str or ~teams_teamwork.models.MicrosoftGraphTeamsAppDistributionMethod
        :param app_definitions: The details for each version of the app.
        :type app_definitions: list[~teams_teamwork.models.MicrosoftGraphTeamsAppDefinition]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphTeamsAppInstallation, or the result of cls(response)
        :rtype: ~teams_teamwork.models.MicrosoftGraphTeamsAppInstallation
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphTeamsAppInstallation"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.MicrosoftGraphTeamsAppInstallation(id=id, teams_app_definition=teams_app_definition, id_teams_app_id=microsoft_graph_entity_id, external_id=external_id, name=name, display_name=display_name, distribution_method=distribution_method, app_definitions=app_definitions)
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.create_installed_app.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'MicrosoftGraphTeamsAppInstallation')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphTeamsAppInstallation', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_installed_app.metadata = {'url': '/users/{user-id}/teamwork/installedApps'}  # type: ignore

    def get_installed_app(
        self,
        user_id,  # type: str
        teams_app_installation_id,  # type: str
        select=None,  # type: Optional[List[Union[str, "models.Enum6"]]]
        expand=None,  # type: Optional[List[Union[str, "models.Get3ItemsItem"]]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphTeamsAppInstallation"
        """Get installedApps from users.

        Get installedApps from users.

        :param user_id: key: user-id of user.
        :type user_id: str
        :param teams_app_installation_id: key: teamsAppInstallation-id of teamsAppInstallation.
        :type teams_app_installation_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~teams_teamwork.models.Enum6]
        :param expand: Expand related entities.
        :type expand: list[str or ~teams_teamwork.models.Get3ItemsItem]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphTeamsAppInstallation, or the result of cls(response)
        :rtype: ~teams_teamwork.models.MicrosoftGraphTeamsAppInstallation
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphTeamsAppInstallation"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        # Construct URL
        url = self.get_installed_app.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'teamsAppInstallation-id': self._serialize.url("teams_app_installation_id", teams_app_installation_id, 'str'),
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

        deserialized = self._deserialize('MicrosoftGraphTeamsAppInstallation', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_installed_app.metadata = {'url': '/users/{user-id}/teamwork/installedApps/{teamsAppInstallation-id}'}  # type: ignore

    def update_installed_app(
        self,
        user_id,  # type: str
        teams_app_installation_id,  # type: str
        id=None,  # type: Optional[str]
        teams_app_definition=None,  # type: Optional["models.MicrosoftGraphTeamsAppDefinition"]
        microsoft_graph_entity_id=None,  # type: Optional[str]
        external_id=None,  # type: Optional[str]
        name=None,  # type: Optional[str]
        display_name=None,  # type: Optional[str]
        distribution_method=None,  # type: Optional[Union[str, "models.MicrosoftGraphTeamsAppDistributionMethod"]]
        app_definitions=None,  # type: Optional[List["models.MicrosoftGraphTeamsAppDefinition"]]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Update the navigation property installedApps in users.

        Update the navigation property installedApps in users.

        :param user_id: key: user-id of user.
        :type user_id: str
        :param teams_app_installation_id: key: teamsAppInstallation-id of teamsAppInstallation.
        :type teams_app_installation_id: str
        :param id: Read-only.
        :type id: str
        :param teams_app_definition: teamsAppDefinition.
        :type teams_app_definition: ~teams_teamwork.models.MicrosoftGraphTeamsAppDefinition
        :param microsoft_graph_entity_id: Read-only.
        :type microsoft_graph_entity_id: str
        :param external_id: The ID of the catalog provided by the app developer in the Microsoft Teams
         zip app package.
        :type external_id: str
        :param name:
        :type name: str
        :param display_name: The name of the catalog app provided by the app developer in the Microsoft
         Teams zip app package.
        :type display_name: str
        :param distribution_method: teamsAppDistributionMethod.
        :type distribution_method: str or ~teams_teamwork.models.MicrosoftGraphTeamsAppDistributionMethod
        :param app_definitions: The details for each version of the app.
        :type app_definitions: list[~teams_teamwork.models.MicrosoftGraphTeamsAppDefinition]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.MicrosoftGraphTeamsAppInstallation(id=id, teams_app_definition=teams_app_definition, id_teams_app_id=microsoft_graph_entity_id, external_id=external_id, name=name, display_name=display_name, distribution_method=distribution_method, app_definitions=app_definitions)
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.update_installed_app.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'teamsAppInstallation-id': self._serialize.url("teams_app_installation_id", teams_app_installation_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'MicrosoftGraphTeamsAppInstallation')
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

    update_installed_app.metadata = {'url': '/users/{user-id}/teamwork/installedApps/{teamsAppInstallation-id}'}  # type: ignore
