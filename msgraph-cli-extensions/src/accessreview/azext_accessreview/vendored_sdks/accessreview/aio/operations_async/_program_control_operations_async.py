# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar, Union
import warnings

from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class ProgramControlOperations:
    """ProgramControlOperations async operations.

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

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    async def get_program(
        self,
        program_control_id: str,
        select: Optional[List[Union[str, "models.Enum30"]]] = None,
        expand: Optional[List[Union[str, "models.Enum31"]]] = None,
        **kwargs
    ) -> "models.MicrosoftGraphProgram":
        """Get program from programControls.

        Get program from programControls.

        :param program_control_id: key: programControl-id of programControl.
        :type program_control_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~identity_access_review.models.Enum30]
        :param expand: Expand related entities.
        :type expand: list[str or ~identity_access_review.models.Enum31]
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
            'programControl-id': self._serialize.url("program_control_id", program_control_id, 'str'),
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
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphProgram', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_program.metadata = {'url': '/programControls/{programControl-id}/program'}  # type: ignore

    async def update_program(
        self,
        program_control_id: str,
        id: Optional[str] = None,
        display_name: Optional[str] = None,
        description: Optional[str] = None,
        controls: Optional[List["models.MicrosoftGraphProgramControl"]] = None,
        **kwargs
    ) -> None:
        """Update the navigation property program in programControls.

        Update the navigation property program in programControls.

        :param program_control_id: key: programControl-id of programControl.
        :type program_control_id: str
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
            'programControl-id': self._serialize.url("program_control_id", program_control_id, 'str'),
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

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    update_program.metadata = {'url': '/programControls/{programControl-id}/program'}  # type: ignore
