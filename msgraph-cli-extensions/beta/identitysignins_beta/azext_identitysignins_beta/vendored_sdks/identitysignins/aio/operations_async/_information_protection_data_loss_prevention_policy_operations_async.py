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

class InformationProtectionDataLossPreventionPolicyOperations:
    """InformationProtectionDataLossPreventionPolicyOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~identity_sign_ins.models
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

    async def evaluate(
        self,
        target: Optional[str] = None,
        author: Optional[str] = None,
        access_scope: Optional[Union[str, "models.MicrosoftGraphAccessScope"]] = None,
        current_label: Optional["models.MicrosoftGraphCurrentLabel"] = None,
        discovered_sensitive_types: Optional[List["models.MicrosoftGraphDiscoveredSensitiveType"]] = None,
        **kwargs
    ) -> "models.MicrosoftGraphDlpEvaluatePoliciesJobResponse":
        """Invoke action evaluate.

        Invoke action evaluate.

        :param target:
        :type target: str
        :param author:
        :type author: str
        :param access_scope:
        :type access_scope: str or ~identity_sign_ins.models.MicrosoftGraphAccessScope
        :param current_label: currentLabel.
        :type current_label: ~identity_sign_ins.models.MicrosoftGraphCurrentLabel
        :param discovered_sensitive_types:
        :type discovered_sensitive_types: list[~identity_sign_ins.models.MicrosoftGraphDiscoveredSensitiveType]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphDlpEvaluatePoliciesJobResponse, or the result of cls(response)
        :rtype: ~identity_sign_ins.models.MicrosoftGraphDlpEvaluatePoliciesJobResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphDlpEvaluatePoliciesJobResponse"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.Paths1JhdydfInformationprotectionDatalosspreventionpoliciesMicrosoftGraphEvaluatePostRequestbodyContentApplicationJsonSchema(target=target, author=author, access_scope=access_scope, current_label=current_label, discovered_sensitive_types=discovered_sensitive_types)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.evaluate.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')
        header_parameters['Accept'] = 'application/json'

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'Paths1JhdydfInformationprotectionDatalosspreventionpoliciesMicrosoftGraphEvaluatePostRequestbodyContentApplicationJsonSchema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphDlpEvaluatePoliciesJobResponse', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    evaluate.metadata = {'url': '/informationProtection/dataLossPreventionPolicies/microsoft.graph.evaluate'}  # type: ignore
