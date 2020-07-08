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

class SuspiciouIpRiskEventSuspiciouIpRiskEventOperations(object):
    """SuspiciouIpRiskEventSuspiciouIpRiskEventOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~identity_protection.models
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

    def list_suspiciou_ip_risk_event(
        self,
        orderby=None,  # type: Optional[List[Union[str, "models.Enum152"]]]
        select=None,  # type: Optional[List[Union[str, "models.Enum153"]]]
        expand=None,  # type: Optional[List[Union[str, "models.Enum154"]]]
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["models.CollectionOfSuspiciousIpRiskEvent"]
        """Get entities from suspiciousIpRiskEvents.

        Get entities from suspiciousIpRiskEvents.

        :param orderby: Order items by property values.
        :type orderby: list[str or ~identity_protection.models.Enum152]
        :param select: Select properties to be returned.
        :type select: list[str or ~identity_protection.models.Enum153]
        :param expand: Expand related entities.
        :type expand: list[str or ~identity_protection.models.Enum154]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either CollectionOfSuspiciousIpRiskEvent or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~identity_protection.models.CollectionOfSuspiciousIpRiskEvent]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.CollectionOfSuspiciousIpRiskEvent"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = 'application/json'

            if not next_link:
                # Construct URL
                url = self.list_suspiciou_ip_risk_event.metadata['url']  # type: ignore
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
            deserialized = self._deserialize('CollectionOfSuspiciousIpRiskEvent', pipeline_response)
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
    list_suspiciou_ip_risk_event.metadata = {'url': '/suspiciousIpRiskEvents'}  # type: ignore

    def create_suspiciou_ip_risk_event(
        self,
        id=None,  # type: Optional[str]
        user_display_name=None,  # type: Optional[str]
        user_principal_name=None,  # type: Optional[str]
        risk_event_date_time=None,  # type: Optional[datetime.datetime]
        risk_event_type=None,  # type: Optional[str]
        risk_level=None,  # type: Optional[Union[str, "models.MicrosoftGraphRiskLevel"]]
        risk_event_status=None,  # type: Optional[Union[str, "models.MicrosoftGraphRiskEventStatus"]]
        closed_date_time=None,  # type: Optional[datetime.datetime]
        created_date_time=None,  # type: Optional[datetime.datetime]
        user_id=None,  # type: Optional[str]
        impacted_user=None,  # type: Optional["models.MicrosoftGraphUser"]
        ip_address=None,  # type: Optional[str]
        city=None,  # type: Optional[str]
        state=None,  # type: Optional[str]
        country_or_region=None,  # type: Optional[str]
        geo_coordinates=None,  # type: Optional["models.MicrosoftGraphGeoCoordinates"]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphLocatedRiskEvent"
        """Add new entity to suspiciousIpRiskEvents.

        Add new entity to suspiciousIpRiskEvents.

        :param id: Read-only.
        :type id: str
        :param user_display_name:
        :type user_display_name: str
        :param user_principal_name:
        :type user_principal_name: str
        :param risk_event_date_time:
        :type risk_event_date_time: ~datetime.datetime
        :param risk_event_type:
        :type risk_event_type: str
        :param risk_level: riskLevel.
        :type risk_level: str or ~identity_protection.models.MicrosoftGraphRiskLevel
        :param risk_event_status: riskEventStatus.
        :type risk_event_status: str or ~identity_protection.models.MicrosoftGraphRiskEventStatus
        :param closed_date_time:
        :type closed_date_time: ~datetime.datetime
        :param created_date_time:
        :type created_date_time: ~datetime.datetime
        :param user_id:
        :type user_id: str
        :param impacted_user: Represents an Azure Active Directory user object.
        :type impacted_user: ~identity_protection.models.MicrosoftGraphUser
        :param ip_address:
        :type ip_address: str
        :param city: Provides the city where the sign-in originated. This is calculated using
         latitude/longitude information from the sign-in activity.
        :type city: str
        :param state: Provides the State where the sign-in originated. This is calculated using
         latitude/longitude information from the sign-in activity.
        :type state: str
        :param country_or_region: Provides the country code info (2 letter code) where the sign-in
         originated.  This is calculated using latitude/longitude information from the sign-in activity.
        :type country_or_region: str
        :param geo_coordinates: geoCoordinates.
        :type geo_coordinates: ~identity_protection.models.MicrosoftGraphGeoCoordinates
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphLocatedRiskEvent, or the result of cls(response)
        :rtype: ~identity_protection.models.MicrosoftGraphLocatedRiskEvent
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphLocatedRiskEvent"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.MicrosoftGraphLocatedRiskEvent(id=id, user_display_name=user_display_name, user_principal_name=user_principal_name, risk_event_date_time=risk_event_date_time, risk_event_type=risk_event_type, risk_level=risk_level, risk_event_status=risk_event_status, closed_date_time=closed_date_time, created_date_time=created_date_time, user_id=user_id, impacted_user=impacted_user, ip_address=ip_address, city=city, state=state, country_or_region=country_or_region, geo_coordinates=geo_coordinates)
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.create_suspiciou_ip_risk_event.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'MicrosoftGraphLocatedRiskEvent')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphLocatedRiskEvent', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_suspiciou_ip_risk_event.metadata = {'url': '/suspiciousIpRiskEvents'}  # type: ignore

    def get_suspiciou_ip_risk_event(
        self,
        suspicious_ip_risk_event_id,  # type: str
        select=None,  # type: Optional[List[Union[str, "models.Enum155"]]]
        expand=None,  # type: Optional[List[Union[str, "models.Enum156"]]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphLocatedRiskEvent"
        """Get entity from suspiciousIpRiskEvents by key.

        Get entity from suspiciousIpRiskEvents by key.

        :param suspicious_ip_risk_event_id: key: suspiciousIpRiskEvent-id of suspiciousIpRiskEvent.
        :type suspicious_ip_risk_event_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~identity_protection.models.Enum155]
        :param expand: Expand related entities.
        :type expand: list[str or ~identity_protection.models.Enum156]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphLocatedRiskEvent, or the result of cls(response)
        :rtype: ~identity_protection.models.MicrosoftGraphLocatedRiskEvent
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphLocatedRiskEvent"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        # Construct URL
        url = self.get_suspiciou_ip_risk_event.metadata['url']  # type: ignore
        path_format_arguments = {
            'suspiciousIpRiskEvent-id': self._serialize.url("suspicious_ip_risk_event_id", suspicious_ip_risk_event_id, 'str'),
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

        deserialized = self._deserialize('MicrosoftGraphLocatedRiskEvent', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_suspiciou_ip_risk_event.metadata = {'url': '/suspiciousIpRiskEvents/{suspiciousIpRiskEvent-id}'}  # type: ignore

    def update_suspiciou_ip_risk_event(
        self,
        suspicious_ip_risk_event_id,  # type: str
        id=None,  # type: Optional[str]
        user_display_name=None,  # type: Optional[str]
        user_principal_name=None,  # type: Optional[str]
        risk_event_date_time=None,  # type: Optional[datetime.datetime]
        risk_event_type=None,  # type: Optional[str]
        risk_level=None,  # type: Optional[Union[str, "models.MicrosoftGraphRiskLevel"]]
        risk_event_status=None,  # type: Optional[Union[str, "models.MicrosoftGraphRiskEventStatus"]]
        closed_date_time=None,  # type: Optional[datetime.datetime]
        created_date_time=None,  # type: Optional[datetime.datetime]
        user_id=None,  # type: Optional[str]
        impacted_user=None,  # type: Optional["models.MicrosoftGraphUser"]
        ip_address=None,  # type: Optional[str]
        city=None,  # type: Optional[str]
        state=None,  # type: Optional[str]
        country_or_region=None,  # type: Optional[str]
        geo_coordinates=None,  # type: Optional["models.MicrosoftGraphGeoCoordinates"]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Update entity in suspiciousIpRiskEvents.

        Update entity in suspiciousIpRiskEvents.

        :param suspicious_ip_risk_event_id: key: suspiciousIpRiskEvent-id of suspiciousIpRiskEvent.
        :type suspicious_ip_risk_event_id: str
        :param id: Read-only.
        :type id: str
        :param user_display_name:
        :type user_display_name: str
        :param user_principal_name:
        :type user_principal_name: str
        :param risk_event_date_time:
        :type risk_event_date_time: ~datetime.datetime
        :param risk_event_type:
        :type risk_event_type: str
        :param risk_level: riskLevel.
        :type risk_level: str or ~identity_protection.models.MicrosoftGraphRiskLevel
        :param risk_event_status: riskEventStatus.
        :type risk_event_status: str or ~identity_protection.models.MicrosoftGraphRiskEventStatus
        :param closed_date_time:
        :type closed_date_time: ~datetime.datetime
        :param created_date_time:
        :type created_date_time: ~datetime.datetime
        :param user_id:
        :type user_id: str
        :param impacted_user: Represents an Azure Active Directory user object.
        :type impacted_user: ~identity_protection.models.MicrosoftGraphUser
        :param ip_address:
        :type ip_address: str
        :param city: Provides the city where the sign-in originated. This is calculated using
         latitude/longitude information from the sign-in activity.
        :type city: str
        :param state: Provides the State where the sign-in originated. This is calculated using
         latitude/longitude information from the sign-in activity.
        :type state: str
        :param country_or_region: Provides the country code info (2 letter code) where the sign-in
         originated.  This is calculated using latitude/longitude information from the sign-in activity.
        :type country_or_region: str
        :param geo_coordinates: geoCoordinates.
        :type geo_coordinates: ~identity_protection.models.MicrosoftGraphGeoCoordinates
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.MicrosoftGraphLocatedRiskEvent(id=id, user_display_name=user_display_name, user_principal_name=user_principal_name, risk_event_date_time=risk_event_date_time, risk_event_type=risk_event_type, risk_level=risk_level, risk_event_status=risk_event_status, closed_date_time=closed_date_time, created_date_time=created_date_time, user_id=user_id, impacted_user=impacted_user, ip_address=ip_address, city=city, state=state, country_or_region=country_or_region, geo_coordinates=geo_coordinates)
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.update_suspiciou_ip_risk_event.metadata['url']  # type: ignore
        path_format_arguments = {
            'suspiciousIpRiskEvent-id': self._serialize.url("suspicious_ip_risk_event_id", suspicious_ip_risk_event_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'MicrosoftGraphLocatedRiskEvent')
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

    update_suspiciou_ip_risk_event.metadata = {'url': '/suspiciousIpRiskEvents/{suspiciousIpRiskEvent-id}'}  # type: ignore

    def delete_suspiciou_ip_risk_event(
        self,
        suspicious_ip_risk_event_id,  # type: str
        if_match=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Delete entity from suspiciousIpRiskEvents.

        Delete entity from suspiciousIpRiskEvents.

        :param suspicious_ip_risk_event_id: key: suspiciousIpRiskEvent-id of suspiciousIpRiskEvent.
        :type suspicious_ip_risk_event_id: str
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
        url = self.delete_suspiciou_ip_risk_event.metadata['url']  # type: ignore
        path_format_arguments = {
            'suspiciousIpRiskEvent-id': self._serialize.url("suspicious_ip_risk_event_id", suspicious_ip_risk_event_id, 'str'),
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

    delete_suspiciou_ip_risk_event.metadata = {'url': '/suspiciousIpRiskEvents/{suspiciousIpRiskEvent-id}'}  # type: ignore
