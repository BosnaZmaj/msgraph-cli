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

class PrintPrintOperations:
    """PrintPrintOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~devices_cloud_print.models
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

    async def get_print(
        self,
        select: Optional[List[Union[str, "models.Get0ItemsItem"]]] = None,
        expand: Optional[List[Union[str, "models.Get1ItemsItem"]]] = None,
        **kwargs
    ) -> "models.MicrosoftGraphPrint":
        """Get print.

        Get print.

        :param select: Select properties to be returned.
        :type select: list[str or ~devices_cloud_print.models.Get0ItemsItem]
        :param expand: Expand related entities.
        :type expand: list[str or ~devices_cloud_print.models.Get1ItemsItem]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphPrint, or the result of cls(response)
        :rtype: ~devices_cloud_print.models.MicrosoftGraphPrint
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphPrint"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_print.metadata['url']  # type: ignore

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

        deserialized = self._deserialize('MicrosoftGraphPrint', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_print.metadata = {'url': '/print'}  # type: ignore

    async def update_print(
        self,
        connectors: Optional[List["models.MicrosoftGraphPrintConnector"]] = None,
        operations: Optional[List["models.MicrosoftGraphPrintOperation"]] = None,
        printers: Optional[List["models.MicrosoftGraphPrinter"]] = None,
        printer_shares: Optional[List["models.MicrosoftGraphPrinterShare"]] = None,
        reports: Optional[List["models.MicrosoftGraphReportRoot"]] = None,
        services: Optional[List["models.MicrosoftGraphPrintService"]] = None,
        shares: Optional[List["models.MicrosoftGraphPrinterShare"]] = None,
        task_definitions: Optional[List["models.MicrosoftGraphPrintTaskDefinition"]] = None,
        document_conversion_enabled: Optional[bool] = None,
        **kwargs
    ) -> None:
        """Update print.

        Update print.

        :param connectors:
        :type connectors: list[~devices_cloud_print.models.MicrosoftGraphPrintConnector]
        :param operations:
        :type operations: list[~devices_cloud_print.models.MicrosoftGraphPrintOperation]
        :param printers:
        :type printers: list[~devices_cloud_print.models.MicrosoftGraphPrinter]
        :param printer_shares:
        :type printer_shares: list[~devices_cloud_print.models.MicrosoftGraphPrinterShare]
        :param reports:
        :type reports: list[~devices_cloud_print.models.MicrosoftGraphReportRoot]
        :param services:
        :type services: list[~devices_cloud_print.models.MicrosoftGraphPrintService]
        :param shares:
        :type shares: list[~devices_cloud_print.models.MicrosoftGraphPrinterShare]
        :param task_definitions:
        :type task_definitions: list[~devices_cloud_print.models.MicrosoftGraphPrintTaskDefinition]
        :param document_conversion_enabled:
        :type document_conversion_enabled: bool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.MicrosoftGraphPrint(connectors=connectors, operations=operations, printers=printers, printer_shares=printer_shares, reports=reports, services=services, shares=shares, task_definitions=task_definitions, document_conversion_enabled=document_conversion_enabled)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.update_print.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'MicrosoftGraphPrint')
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

    update_print.metadata = {'url': '/print'}  # type: ignore