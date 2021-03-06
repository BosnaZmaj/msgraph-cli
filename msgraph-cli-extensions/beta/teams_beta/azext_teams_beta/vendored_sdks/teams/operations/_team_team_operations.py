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

class TeamTeamOperations(object):
    """TeamTeamOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~teams.models
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

    def list_team(
        self,
        orderby=None,  # type: Optional[List[Union[str, "models.Enum166"]]]
        select=None,  # type: Optional[List[Union[str, "models.Enum167"]]]
        expand=None,  # type: Optional[List[Union[str, "models.Enum168"]]]
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["models.CollectionOfTeam"]
        """Get entities from teams.

        Get entities from teams.

        :param orderby: Order items by property values.
        :type orderby: list[str or ~teams.models.Enum166]
        :param select: Select properties to be returned.
        :type select: list[str or ~teams.models.Enum167]
        :param expand: Expand related entities.
        :type expand: list[str or ~teams.models.Enum168]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either CollectionOfTeam or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~teams.models.CollectionOfTeam]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.CollectionOfTeam"]
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
                url = self.list_team.metadata['url']  # type: ignore
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
            deserialized = self._deserialize('CollectionOfTeam', pipeline_response)
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
    list_team.metadata = {'url': '/teams'}  # type: ignore

    def create_team(
        self,
        id=None,  # type: Optional[str]
        classification=None,  # type: Optional[str]
        created_date_time=None,  # type: Optional[datetime.datetime]
        description=None,  # type: Optional[str]
        display_name=None,  # type: Optional[str]
        fun_settings=None,  # type: Optional["models.MicrosoftGraphTeamFunSettings"]
        guest_settings=None,  # type: Optional["models.MicrosoftGraphTeamGuestSettings"]
        internal_id=None,  # type: Optional[str]
        is_archived=None,  # type: Optional[bool]
        is_membership_limited_to_owners=None,  # type: Optional[bool]
        member_settings=None,  # type: Optional["models.MicrosoftGraphTeamMemberSettings"]
        messaging_settings=None,  # type: Optional["models.MicrosoftGraphTeamMessagingSettings"]
        specialization=None,  # type: Optional[Union[str, "models.MicrosoftGraphTeamSpecialization"]]
        visibility=None,  # type: Optional[Union[str, "models.MicrosoftGraphTeamVisibilityType"]]
        web_url=None,  # type: Optional[str]
        channels=None,  # type: Optional[List["models.MicrosoftGraphChannel"]]
        group=None,  # type: Optional["models.MicrosoftGraphGroup"]
        installed_apps=None,  # type: Optional[List["models.MicrosoftGraphTeamsAppInstallation"]]
        members=None,  # type: Optional[List["models.MicrosoftGraphConversationMember"]]
        operations=None,  # type: Optional[List["models.MicrosoftGraphTeamsAsyncOperation"]]
        owners=None,  # type: Optional[List["models.MicrosoftGraphUser"]]
        photo=None,  # type: Optional["models.MicrosoftGraphProfilePhoto"]
        primary_channel=None,  # type: Optional["models.MicrosoftGraphChannel"]
        microsoft_graph_entity_id=None,  # type: Optional[str]
        id1=None,  # type: Optional[str]
        enabled=None,  # type: Optional[bool]
        offer_shift_requests_enabled=None,  # type: Optional[bool]
        open_shifts_enabled=None,  # type: Optional[bool]
        provision_status=None,  # type: Optional[Union[str, "models.MicrosoftGraphOperationStatus"]]
        provision_status_code=None,  # type: Optional[str]
        swap_shifts_requests_enabled=None,  # type: Optional[bool]
        time_clock_enabled=None,  # type: Optional[bool]
        time_off_requests_enabled=None,  # type: Optional[bool]
        time_zone=None,  # type: Optional[str]
        workforce_integration_ids=None,  # type: Optional[List[str]]
        offer_shift_requests=None,  # type: Optional[List["models.MicrosoftGraphOfferShiftRequest"]]
        open_shift_change_requests=None,  # type: Optional[List["models.MicrosoftGraphOpenShiftChangeRequest"]]
        open_shifts=None,  # type: Optional[List["models.MicrosoftGraphOpenShift"]]
        scheduling_groups=None,  # type: Optional[List["models.MicrosoftGraphSchedulingGroup"]]
        shifts=None,  # type: Optional[List["models.MicrosoftGraphShift"]]
        swap_shifts_change_requests=None,  # type: Optional[List["models.MicrosoftGraphSwapShiftsChangeRequest"]]
        time_cards=None,  # type: Optional[List["models.MicrosoftGraphTimeCard"]]
        time_off_reasons=None,  # type: Optional[List["models.MicrosoftGraphTimeOffReason"]]
        time_off_requests=None,  # type: Optional[List["models.MicrosoftGraphTimeOffRequest"]]
        times_off=None,  # type: Optional[List["models.MicrosoftGraphTimeOff"]]
        approved_location=None,  # type: Optional["models.MicrosoftGraphGeoCoordinates"]
        show_in_teams_search_and_suggestions=None,  # type: Optional[bool]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphTeam"
        """Add new entity to teams.

        Add new entity to teams.

        :param id: Read-only.
        :type id: str
        :param classification: An optional label. Typically describes the data or business sensitivity
         of the team. Must match one of a pre-configured set in the tenant's directory.
        :type classification: str
        :param created_date_time:
        :type created_date_time: ~datetime.datetime
        :param description: An optional description for the team.
        :type description: str
        :param display_name: The name of the team.
        :type display_name: str
        :param fun_settings: teamFunSettings.
        :type fun_settings: ~teams.models.MicrosoftGraphTeamFunSettings
        :param guest_settings: teamGuestSettings.
        :type guest_settings: ~teams.models.MicrosoftGraphTeamGuestSettings
        :param internal_id: A unique ID for the team that has been used in a few places such as the
         audit log/Office 365 Management Activity API.
        :type internal_id: str
        :param is_archived: Whether this team is in read-only mode.
        :type is_archived: bool
        :param is_membership_limited_to_owners:
        :type is_membership_limited_to_owners: bool
        :param member_settings: teamMemberSettings.
        :type member_settings: ~teams.models.MicrosoftGraphTeamMemberSettings
        :param messaging_settings: teamMessagingSettings.
        :type messaging_settings: ~teams.models.MicrosoftGraphTeamMessagingSettings
        :param specialization:
        :type specialization: str or ~teams.models.MicrosoftGraphTeamSpecialization
        :param visibility:
        :type visibility: str or ~teams.models.MicrosoftGraphTeamVisibilityType
        :param web_url: A hyperlink that will go to the team in the Microsoft Teams client. This is the
         URL that you get when you right-click a team in the Microsoft Teams client and select Get link
         to team. This URL should be treated as an opaque blob, and not parsed.
        :type web_url: str
        :param channels: The collection of channels & messages associated with the team.
        :type channels: list[~teams.models.MicrosoftGraphChannel]
        :param group: Represents an Azure Active Directory object. The directoryObject type is the base
         type for many other directory entity types.
        :type group: ~teams.models.MicrosoftGraphGroup
        :param installed_apps: The apps installed in this team.
        :type installed_apps: list[~teams.models.MicrosoftGraphTeamsAppInstallation]
        :param members: Members and owners of the team.
        :type members: list[~teams.models.MicrosoftGraphConversationMember]
        :param operations: The async operations that ran or are running on this team.
        :type operations: list[~teams.models.MicrosoftGraphTeamsAsyncOperation]
        :param owners:
        :type owners: list[~teams.models.MicrosoftGraphUser]
        :param photo: profilePhoto.
        :type photo: ~teams.models.MicrosoftGraphProfilePhoto
        :param primary_channel: channel.
        :type primary_channel: ~teams.models.MicrosoftGraphChannel
        :param microsoft_graph_entity_id: Read-only.
        :type microsoft_graph_entity_id: str
        :param id1: Read-only.
        :type id1: str
        :param enabled: Indicates whether the schedule is enabled for the team. Required.
        :type enabled: bool
        :param offer_shift_requests_enabled: Indicates whether offer shift requests are enabled for the
         schedule.
        :type offer_shift_requests_enabled: bool
        :param open_shifts_enabled: Indicates whether open shifts are enabled for the schedule.
        :type open_shifts_enabled: bool
        :param provision_status:
        :type provision_status: str or ~teams.models.MicrosoftGraphOperationStatus
        :param provision_status_code: Additional information about why schedule provisioning failed.
        :type provision_status_code: str
        :param swap_shifts_requests_enabled: Indicates whether swap shifts requests are enabled for the
         schedule.
        :type swap_shifts_requests_enabled: bool
        :param time_clock_enabled: Indicates whether time clock is enabled for the schedule.
        :type time_clock_enabled: bool
        :param time_off_requests_enabled: Indicates whether time off requests are enabled for the
         schedule.
        :type time_off_requests_enabled: bool
        :param time_zone: Indicates the time zone of the schedule team using tz database format.
         Required.
        :type time_zone: str
        :param workforce_integration_ids:
        :type workforce_integration_ids: list[str]
        :param offer_shift_requests:
        :type offer_shift_requests: list[~teams.models.MicrosoftGraphOfferShiftRequest]
        :param open_shift_change_requests:
        :type open_shift_change_requests: list[~teams.models.MicrosoftGraphOpenShiftChangeRequest]
        :param open_shifts:
        :type open_shifts: list[~teams.models.MicrosoftGraphOpenShift]
        :param scheduling_groups: The logical grouping of users in the schedule (usually by role).
        :type scheduling_groups: list[~teams.models.MicrosoftGraphSchedulingGroup]
        :param shifts: The shifts in the schedule.
        :type shifts: list[~teams.models.MicrosoftGraphShift]
        :param swap_shifts_change_requests:
        :type swap_shifts_change_requests: list[~teams.models.MicrosoftGraphSwapShiftsChangeRequest]
        :param time_cards:
        :type time_cards: list[~teams.models.MicrosoftGraphTimeCard]
        :param time_off_reasons: The set of reasons for a time off in the schedule.
        :type time_off_reasons: list[~teams.models.MicrosoftGraphTimeOffReason]
        :param time_off_requests:
        :type time_off_requests: list[~teams.models.MicrosoftGraphTimeOffRequest]
        :param times_off: The instances of times off in the schedule.
        :type times_off: list[~teams.models.MicrosoftGraphTimeOff]
        :param approved_location: geoCoordinates.
        :type approved_location: ~teams.models.MicrosoftGraphGeoCoordinates
        :param show_in_teams_search_and_suggestions:
        :type show_in_teams_search_and_suggestions: bool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphTeam, or the result of cls(response)
        :rtype: ~teams.models.MicrosoftGraphTeam
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphTeam"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.MicrosoftGraphTeam(id=id, classification=classification, created_date_time=created_date_time, description=description, display_name=display_name, fun_settings=fun_settings, guest_settings=guest_settings, internal_id=internal_id, is_archived=is_archived, is_membership_limited_to_owners=is_membership_limited_to_owners, member_settings=member_settings, messaging_settings=messaging_settings, specialization=specialization, visibility=visibility, web_url=web_url, channels=channels, group=group, installed_apps=installed_apps, members=members, operations=operations, owners=owners, photo=photo, primary_channel=primary_channel, id_template_id=microsoft_graph_entity_id, id_schedule_id=id1, enabled=enabled, offer_shift_requests_enabled=offer_shift_requests_enabled, open_shifts_enabled=open_shifts_enabled, provision_status=provision_status, provision_status_code=provision_status_code, swap_shifts_requests_enabled=swap_shifts_requests_enabled, time_clock_enabled=time_clock_enabled, time_off_requests_enabled=time_off_requests_enabled, time_zone=time_zone, workforce_integration_ids=workforce_integration_ids, offer_shift_requests=offer_shift_requests, open_shift_change_requests=open_shift_change_requests, open_shifts=open_shifts, scheduling_groups=scheduling_groups, shifts=shifts, swap_shifts_change_requests=swap_shifts_change_requests, time_cards=time_cards, time_off_reasons=time_off_reasons, time_off_requests=time_off_requests, times_off=times_off, approved_location=approved_location, show_in_teams_search_and_suggestions=show_in_teams_search_and_suggestions)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.create_team.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')
        header_parameters['Accept'] = 'application/json'

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'MicrosoftGraphTeam')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphTeam', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_team.metadata = {'url': '/teams'}  # type: ignore

    def get_team(
        self,
        team_id,  # type: str
        select=None,  # type: Optional[List[Union[str, "models.Enum169"]]]
        expand=None,  # type: Optional[List[Union[str, "models.Enum170"]]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphTeam"
        """Get entity from teams by key.

        Get entity from teams by key.

        :param team_id: key: id of team.
        :type team_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~teams.models.Enum169]
        :param expand: Expand related entities.
        :type expand: list[str or ~teams.models.Enum170]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphTeam, or the result of cls(response)
        :rtype: ~teams.models.MicrosoftGraphTeam
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphTeam"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_team.metadata['url']  # type: ignore
        path_format_arguments = {
            'team-id': self._serialize.url("team_id", team_id, 'str'),
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
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphTeam', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_team.metadata = {'url': '/teams/{team-id}'}  # type: ignore

    def update_team(
        self,
        team_id,  # type: str
        id=None,  # type: Optional[str]
        classification=None,  # type: Optional[str]
        created_date_time=None,  # type: Optional[datetime.datetime]
        description=None,  # type: Optional[str]
        display_name=None,  # type: Optional[str]
        fun_settings=None,  # type: Optional["models.MicrosoftGraphTeamFunSettings"]
        guest_settings=None,  # type: Optional["models.MicrosoftGraphTeamGuestSettings"]
        internal_id=None,  # type: Optional[str]
        is_archived=None,  # type: Optional[bool]
        is_membership_limited_to_owners=None,  # type: Optional[bool]
        member_settings=None,  # type: Optional["models.MicrosoftGraphTeamMemberSettings"]
        messaging_settings=None,  # type: Optional["models.MicrosoftGraphTeamMessagingSettings"]
        specialization=None,  # type: Optional[Union[str, "models.MicrosoftGraphTeamSpecialization"]]
        visibility=None,  # type: Optional[Union[str, "models.MicrosoftGraphTeamVisibilityType"]]
        web_url=None,  # type: Optional[str]
        channels=None,  # type: Optional[List["models.MicrosoftGraphChannel"]]
        group=None,  # type: Optional["models.MicrosoftGraphGroup"]
        installed_apps=None,  # type: Optional[List["models.MicrosoftGraphTeamsAppInstallation"]]
        members=None,  # type: Optional[List["models.MicrosoftGraphConversationMember"]]
        operations=None,  # type: Optional[List["models.MicrosoftGraphTeamsAsyncOperation"]]
        owners=None,  # type: Optional[List["models.MicrosoftGraphUser"]]
        photo=None,  # type: Optional["models.MicrosoftGraphProfilePhoto"]
        primary_channel=None,  # type: Optional["models.MicrosoftGraphChannel"]
        microsoft_graph_entity_id=None,  # type: Optional[str]
        id1=None,  # type: Optional[str]
        enabled=None,  # type: Optional[bool]
        offer_shift_requests_enabled=None,  # type: Optional[bool]
        open_shifts_enabled=None,  # type: Optional[bool]
        provision_status=None,  # type: Optional[Union[str, "models.MicrosoftGraphOperationStatus"]]
        provision_status_code=None,  # type: Optional[str]
        swap_shifts_requests_enabled=None,  # type: Optional[bool]
        time_clock_enabled=None,  # type: Optional[bool]
        time_off_requests_enabled=None,  # type: Optional[bool]
        time_zone=None,  # type: Optional[str]
        workforce_integration_ids=None,  # type: Optional[List[str]]
        offer_shift_requests=None,  # type: Optional[List["models.MicrosoftGraphOfferShiftRequest"]]
        open_shift_change_requests=None,  # type: Optional[List["models.MicrosoftGraphOpenShiftChangeRequest"]]
        open_shifts=None,  # type: Optional[List["models.MicrosoftGraphOpenShift"]]
        scheduling_groups=None,  # type: Optional[List["models.MicrosoftGraphSchedulingGroup"]]
        shifts=None,  # type: Optional[List["models.MicrosoftGraphShift"]]
        swap_shifts_change_requests=None,  # type: Optional[List["models.MicrosoftGraphSwapShiftsChangeRequest"]]
        time_cards=None,  # type: Optional[List["models.MicrosoftGraphTimeCard"]]
        time_off_reasons=None,  # type: Optional[List["models.MicrosoftGraphTimeOffReason"]]
        time_off_requests=None,  # type: Optional[List["models.MicrosoftGraphTimeOffRequest"]]
        times_off=None,  # type: Optional[List["models.MicrosoftGraphTimeOff"]]
        approved_location=None,  # type: Optional["models.MicrosoftGraphGeoCoordinates"]
        show_in_teams_search_and_suggestions=None,  # type: Optional[bool]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Update entity in teams.

        Update entity in teams.

        :param team_id: key: id of team.
        :type team_id: str
        :param id: Read-only.
        :type id: str
        :param classification: An optional label. Typically describes the data or business sensitivity
         of the team. Must match one of a pre-configured set in the tenant's directory.
        :type classification: str
        :param created_date_time:
        :type created_date_time: ~datetime.datetime
        :param description: An optional description for the team.
        :type description: str
        :param display_name: The name of the team.
        :type display_name: str
        :param fun_settings: teamFunSettings.
        :type fun_settings: ~teams.models.MicrosoftGraphTeamFunSettings
        :param guest_settings: teamGuestSettings.
        :type guest_settings: ~teams.models.MicrosoftGraphTeamGuestSettings
        :param internal_id: A unique ID for the team that has been used in a few places such as the
         audit log/Office 365 Management Activity API.
        :type internal_id: str
        :param is_archived: Whether this team is in read-only mode.
        :type is_archived: bool
        :param is_membership_limited_to_owners:
        :type is_membership_limited_to_owners: bool
        :param member_settings: teamMemberSettings.
        :type member_settings: ~teams.models.MicrosoftGraphTeamMemberSettings
        :param messaging_settings: teamMessagingSettings.
        :type messaging_settings: ~teams.models.MicrosoftGraphTeamMessagingSettings
        :param specialization:
        :type specialization: str or ~teams.models.MicrosoftGraphTeamSpecialization
        :param visibility:
        :type visibility: str or ~teams.models.MicrosoftGraphTeamVisibilityType
        :param web_url: A hyperlink that will go to the team in the Microsoft Teams client. This is the
         URL that you get when you right-click a team in the Microsoft Teams client and select Get link
         to team. This URL should be treated as an opaque blob, and not parsed.
        :type web_url: str
        :param channels: The collection of channels & messages associated with the team.
        :type channels: list[~teams.models.MicrosoftGraphChannel]
        :param group: Represents an Azure Active Directory object. The directoryObject type is the base
         type for many other directory entity types.
        :type group: ~teams.models.MicrosoftGraphGroup
        :param installed_apps: The apps installed in this team.
        :type installed_apps: list[~teams.models.MicrosoftGraphTeamsAppInstallation]
        :param members: Members and owners of the team.
        :type members: list[~teams.models.MicrosoftGraphConversationMember]
        :param operations: The async operations that ran or are running on this team.
        :type operations: list[~teams.models.MicrosoftGraphTeamsAsyncOperation]
        :param owners:
        :type owners: list[~teams.models.MicrosoftGraphUser]
        :param photo: profilePhoto.
        :type photo: ~teams.models.MicrosoftGraphProfilePhoto
        :param primary_channel: channel.
        :type primary_channel: ~teams.models.MicrosoftGraphChannel
        :param microsoft_graph_entity_id: Read-only.
        :type microsoft_graph_entity_id: str
        :param id1: Read-only.
        :type id1: str
        :param enabled: Indicates whether the schedule is enabled for the team. Required.
        :type enabled: bool
        :param offer_shift_requests_enabled: Indicates whether offer shift requests are enabled for the
         schedule.
        :type offer_shift_requests_enabled: bool
        :param open_shifts_enabled: Indicates whether open shifts are enabled for the schedule.
        :type open_shifts_enabled: bool
        :param provision_status:
        :type provision_status: str or ~teams.models.MicrosoftGraphOperationStatus
        :param provision_status_code: Additional information about why schedule provisioning failed.
        :type provision_status_code: str
        :param swap_shifts_requests_enabled: Indicates whether swap shifts requests are enabled for the
         schedule.
        :type swap_shifts_requests_enabled: bool
        :param time_clock_enabled: Indicates whether time clock is enabled for the schedule.
        :type time_clock_enabled: bool
        :param time_off_requests_enabled: Indicates whether time off requests are enabled for the
         schedule.
        :type time_off_requests_enabled: bool
        :param time_zone: Indicates the time zone of the schedule team using tz database format.
         Required.
        :type time_zone: str
        :param workforce_integration_ids:
        :type workforce_integration_ids: list[str]
        :param offer_shift_requests:
        :type offer_shift_requests: list[~teams.models.MicrosoftGraphOfferShiftRequest]
        :param open_shift_change_requests:
        :type open_shift_change_requests: list[~teams.models.MicrosoftGraphOpenShiftChangeRequest]
        :param open_shifts:
        :type open_shifts: list[~teams.models.MicrosoftGraphOpenShift]
        :param scheduling_groups: The logical grouping of users in the schedule (usually by role).
        :type scheduling_groups: list[~teams.models.MicrosoftGraphSchedulingGroup]
        :param shifts: The shifts in the schedule.
        :type shifts: list[~teams.models.MicrosoftGraphShift]
        :param swap_shifts_change_requests:
        :type swap_shifts_change_requests: list[~teams.models.MicrosoftGraphSwapShiftsChangeRequest]
        :param time_cards:
        :type time_cards: list[~teams.models.MicrosoftGraphTimeCard]
        :param time_off_reasons: The set of reasons for a time off in the schedule.
        :type time_off_reasons: list[~teams.models.MicrosoftGraphTimeOffReason]
        :param time_off_requests:
        :type time_off_requests: list[~teams.models.MicrosoftGraphTimeOffRequest]
        :param times_off: The instances of times off in the schedule.
        :type times_off: list[~teams.models.MicrosoftGraphTimeOff]
        :param approved_location: geoCoordinates.
        :type approved_location: ~teams.models.MicrosoftGraphGeoCoordinates
        :param show_in_teams_search_and_suggestions:
        :type show_in_teams_search_and_suggestions: bool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.MicrosoftGraphTeam(id=id, classification=classification, created_date_time=created_date_time, description=description, display_name=display_name, fun_settings=fun_settings, guest_settings=guest_settings, internal_id=internal_id, is_archived=is_archived, is_membership_limited_to_owners=is_membership_limited_to_owners, member_settings=member_settings, messaging_settings=messaging_settings, specialization=specialization, visibility=visibility, web_url=web_url, channels=channels, group=group, installed_apps=installed_apps, members=members, operations=operations, owners=owners, photo=photo, primary_channel=primary_channel, id_template_id=microsoft_graph_entity_id, id_schedule_id=id1, enabled=enabled, offer_shift_requests_enabled=offer_shift_requests_enabled, open_shifts_enabled=open_shifts_enabled, provision_status=provision_status, provision_status_code=provision_status_code, swap_shifts_requests_enabled=swap_shifts_requests_enabled, time_clock_enabled=time_clock_enabled, time_off_requests_enabled=time_off_requests_enabled, time_zone=time_zone, workforce_integration_ids=workforce_integration_ids, offer_shift_requests=offer_shift_requests, open_shift_change_requests=open_shift_change_requests, open_shifts=open_shifts, scheduling_groups=scheduling_groups, shifts=shifts, swap_shifts_change_requests=swap_shifts_change_requests, time_cards=time_cards, time_off_reasons=time_off_reasons, time_off_requests=time_off_requests, times_off=times_off, approved_location=approved_location, show_in_teams_search_and_suggestions=show_in_teams_search_and_suggestions)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.update_team.metadata['url']  # type: ignore
        path_format_arguments = {
            'team-id': self._serialize.url("team_id", team_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'MicrosoftGraphTeam')
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

    update_team.metadata = {'url': '/teams/{team-id}'}  # type: ignore

    def delete_team(
        self,
        team_id,  # type: str
        if_match=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Delete entity from teams.

        Delete entity from teams.

        :param team_id: key: id of team.
        :type team_id: str
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
        url = self.delete_team.metadata['url']  # type: ignore
        path_format_arguments = {
            'team-id': self._serialize.url("team_id", team_id, 'str'),
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
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete_team.metadata = {'url': '/teams/{team-id}'}  # type: ignore
