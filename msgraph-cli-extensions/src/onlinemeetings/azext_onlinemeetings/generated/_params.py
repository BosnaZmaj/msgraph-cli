# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines
# pylint: disable=too-many-statements

from msgraph.cli.core.commands.parameters import (
    get_three_state_flag,
    get_enum_type
)
from msgraph.cli.core.commands.validators import validate_file_or_dict
from azext_onlinemeetings.action import (
    AddAudioConferencing,
    AddChatInfo,
    AddJoinInformation
)


def load_arguments(self, _):

    with self.argument_context('onlinemeetings update') as c:
        c.argument('user_id', help='key: user-id of user')
        c.argument('online_meeting_id', help='key: onlineMeeting-id of onlineMeeting')
        c.argument('id_', options_list=['--id'], help='Read-only.')
        c.argument('creation_date_time', help='The meeting creation time in UTC. Read-only.')
        c.argument('start_date_time', help='The meeting start time in UTC.')
        c.argument('end_date_time', help='The meeting end time in UTC.')
        c.argument('canceled_date_time', help='')
        c.argument('expiration_date_time', help='')
        c.argument('entry_exit_announcement', arg_type=get_three_state_flag(), help='')
        c.argument('join_url', help='')
        c.argument('subject', help='The subject of the online meeting.')
        c.argument('is_cancelled', arg_type=get_three_state_flag(), help='')
        c.argument('is_broadcast', arg_type=get_three_state_flag(), help='')
        c.argument('access_level', arg_type=get_enum_type(['everyone', 'invited', 'locked', 'sameEnterprise', ''
                   'sameEnterpriseAndFederated']), help='')
        c.argument('capabilities', nargs='*', help='')
        c.argument('audio_conferencing', action=AddAudioConferencing, nargs='*', help='audioConferencing')
        c.argument('chat_info', action=AddChatInfo, nargs='*', help='chatInfo')
        c.argument('video_teleconference_id', help='The video teleconferencing ID. Read-only.')
        c.argument('external_id', help='')
        c.argument('join_information', action=AddJoinInformation, nargs='*', help='itemBody')
        c.argument('participants_organizer', type=validate_file_or_dict, help='meetingParticipantInfo Expected value: '
                   'json-string/@json-file.')
        c.argument('participants_attendees', type=validate_file_or_dict, help=' Expected value: '
                   'json-string/@json-file.')
        c.argument('participants_producers', type=validate_file_or_dict, help=' Expected value: '
                   'json-string/@json-file.')
        c.argument('participants_contributors', type=validate_file_or_dict, help=' Expected value: '
                   'json-string/@json-file.')

    with self.argument_context('onlinemeetings create-online-meeting') as c:
        c.argument('user_id', help='key: user-id of user')
        c.argument('id_', options_list=['--id'], help='Read-only.')
        c.argument('creation_date_time', help='The meeting creation time in UTC. Read-only.')
        c.argument('start_date_time', help='The meeting start time in UTC.')
        c.argument('end_date_time', help='The meeting end time in UTC.')
        c.argument('canceled_date_time', help='')
        c.argument('expiration_date_time', help='')
        c.argument('entry_exit_announcement', arg_type=get_three_state_flag(), help='')
        c.argument('join_url', help='')
        c.argument('subject', help='The subject of the online meeting.')
        c.argument('is_cancelled', arg_type=get_three_state_flag(), help='')
        c.argument('is_broadcast', arg_type=get_three_state_flag(), help='')
        c.argument('access_level', arg_type=get_enum_type(['everyone', 'invited', 'locked', 'sameEnterprise', ''
                   'sameEnterpriseAndFederated']), help='')
        c.argument('capabilities', nargs='*', help='')
        c.argument('audio_conferencing', action=AddAudioConferencing, nargs='*', help='audioConferencing')
        c.argument('chat_info', action=AddChatInfo, nargs='*', help='chatInfo')
        c.argument('video_teleconference_id', help='The video teleconferencing ID. Read-only.')
        c.argument('external_id', help='')
        c.argument('join_information', action=AddJoinInformation, nargs='*', help='itemBody')
        c.argument('participants_organizer', type=validate_file_or_dict, help='meetingParticipantInfo Expected value: '
                   'json-string/@json-file.')
        c.argument('participants_attendees', type=validate_file_or_dict, help=' Expected value: '
                   'json-string/@json-file.')
        c.argument('participants_producers', type=validate_file_or_dict, help=' Expected value: '
                   'json-string/@json-file.')
        c.argument('participants_contributors', type=validate_file_or_dict, help=' Expected value: '
                   'json-string/@json-file.')

    with self.argument_context('onlinemeetings get-online-meeting') as c:
        c.argument('user_id', help='key: user-id of user')
        c.argument('online_meeting_id', help='key: onlineMeeting-id of onlineMeeting')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('onlinemeetings list-online-meeting') as c:
        c.argument('user_id', help='key: user-id of user')
        c.argument('orderby', nargs='*', help='Order items by property values')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')