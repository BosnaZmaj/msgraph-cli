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

class ProgramProgramOperations(object):
    """ProgramProgramOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~identity_access_review.models
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

    def list_program(
        self,
        orderby=None,  # type: Optional[List[Union[str, "models.Enum35"]]]
        select=None,  # type: Optional[List[Union[str, "models.Enum36"]]]
        expand=None,  # type: Optional[List[Union[str, "models.Enum37"]]]
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["models.CollectionOfProgram"]
        """Get entities from programs.

        Get entities from programs.

        :param orderby: Order items by property values.
        :type orderby: list[str or ~identity_access_review.models.Enum35]
        :param select: Select properties to be returned.
        :type select: list[str or ~identity_access_review.models.Enum36]
        :param expand: Expand related entities.
        :type expand: list[str or ~identity_access_review.models.Enum37]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either CollectionOfProgram or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~identity_access_review.models.CollectionOfProgram]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.CollectionOfProgram"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = 'application/json'

            if not next_link:
                # Construct URL
                url = self.list_program.metadata['url']  # type: ignore
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
            deserialized = self._deserialize('CollectionOfProgram', pipeline_response)
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
    list_program.metadata = {'url': '/programs'}  # type: ignore

    def create_program(
        self,
        id=None,  # type: Optional[str]
        display_name=None,  # type: Optional[str]
        description=None,  # type: Optional[str]
        controls=None,  # type: Optional[List["models.MicrosoftGraphProgramControl"]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphProgram"
        """Add new entity to programs.

        Add new entity to programs.

        :param id: Read-only.
        :type id: str
        :param display_name:
        :type display_name: str
        :param description:
        :type description: str
        :param controls:
        :type controls: list[~identity_access_review.models.MicrosoftGraphProgramControl]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphProgram, or the result of cls(response)
        :rtype: ~identity_access_review.models.MicrosoftGraphProgram
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphProgram"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.MicrosoftGraphProgram(id=id, display_name=display_name, description=description, controls=controls)
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.create_program.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'MicrosoftGraphProgram')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphProgram', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_program.metadata = {'url': '/programs'}  # type: ignore

    def get_program(
        self,
        program_id,  # type: str
        select=None,  # type: Optional[List[Union[str, "models.Enum38"]]]
        expand=None,  # type: Optional[List[Union[str, "models.Enum39"]]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphProgram"
        """Get entity from programs by key.

        Get entity from programs by key.

        :param program_id: key: program-id of program.
        :type program_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~identity_access_review.models.Enum38]
        :param expand: Expand related entities.
        :type expand: list[str or ~identity_access_review.models.Enum39]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphProgram, or the result of cls(response)
        :rtype: ~identity_access_review.models.MicrosoftGraphProgram
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphProgram"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        # Construct URL
        url = self.get_program.metadata['url']  # type: ignore
        path_format_arguments = {
            'program-id': self._serialize.url("program_id", program_id, 'str'),
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

        deserialized = self._deserialize('MicrosoftGraphProgram', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_program.metadata = {'url': '/programs/{program-id}'}  # type: ignore

    def update_program(
        self,
        program_id,  # type: str
        id=None,  # type: Optional[str]
        display_name=None,  # type: Optional[str]
        description=None,  # type: Optional[str]
        controls=None,  # type: Optional[List["models.MicrosoftGraphProgramControl"]]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Update entity in programs.

        Update entity in programs.

        :param program_id: key: program-id of program.
        :type program_id: str
        :param id: Read-only.
        :type id: str
        :param display_name:
        :type display_name: str
        :param description:
        :type description: str
        :param controls:
        :type controls: list[~identity_access_review.models.MicrosoftGraphProgramControl]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.MicrosoftGraphProgram(id=id, display_name=display_name, description=description, controls=controls)
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.update_program.metadata['url']  # type: ignore
        path_format_arguments = {
            'program-id': self._serialize.url("program_id", program_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'MicrosoftGraphProgram')
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

    update_program.metadata = {'url': '/programs/{program-id}'}  # type: ignore

    def delete_program(
        self,
        program_id,  # type: str
        if_match=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Delete entity from programs.

        Delete entity from programs.

        :param program_id: key: program-id of program.
        :type program_id: str
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

        # Construct URL
        url = self.delete_program.metadata['url']  # type: ignore
        path_format_arguments = {
            'program-id': self._serialize.url("program_id", program_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if if_match is not None:
            header_parameters['If-Match'] = self._serialize.header("if_match", if_match, 'str')

        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete_program.metadata = {'url': '/programs/{program-id}'}  # type: ignore
