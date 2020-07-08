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


def onlinemeetings_user_update(client,
                               user_id,
                               online_meeting_id,
                               id_=None,
                               creation_date_time=None,
                               start_date_time=None,
                               end_date_time=None,
                               canceled_date_time=None,
                               expiration_date_time=None,
                               entry_exit_announcement=None,
                               join_url=None,
                               subject=None,
                               is_cancelled=None,
                               is_broadcast=None,
                               access_level=None,
                               capabilities=None,
                               audio_conferencing=None,
                               chat_info=None,
                               video_teleconference_id=None,
                               external_id=None,
                               join_information=None,
                               participants_organizer=None,
                               participants_attendees=None,
                               participants_producers=None,
                               participants_contributors=None):
    return client.update_online_meeting(user_id=user_id,
                                        online_meeting_id=online_meeting_id,
                                        id=id_,
                                        creation_date_time=creation_date_time,
                                        start_date_time=start_date_time,
                                        end_date_time=end_date_time,
                                        canceled_date_time=canceled_date_time,
                                        expiration_date_time=expiration_date_time,
                                        entry_exit_announcement=entry_exit_announcement,
                                        join_url=join_url,
                                        subject=subject,
                                        is_cancelled=is_cancelled,
                                        is_broadcast=is_broadcast,
                                        access_level=access_level,
                                        capabilities=capabilities,
                                        audio_conferencing=audio_conferencing,
                                        chat_info=chat_info,
                                        video_teleconference_id=video_teleconference_id,
                                        external_id=external_id,
                                        join_information=join_information,
                                        organizer=participants_organizer,
                                        attendees=participants_attendees,
                                        producers=participants_producers,
                                        contributors=participants_contributors)


def onlinemeetings_user_create_online_meeting(client,
                                              user_id,
                                              id_=None,
                                              creation_date_time=None,
                                              start_date_time=None,
                                              end_date_time=None,
                                              canceled_date_time=None,
                                              expiration_date_time=None,
                                              entry_exit_announcement=None,
                                              join_url=None,
                                              subject=None,
                                              is_cancelled=None,
                                              is_broadcast=None,
                                              access_level=None,
                                              capabilities=None,
                                              audio_conferencing=None,
                                              chat_info=None,
                                              video_teleconference_id=None,
                                              external_id=None,
                                              join_information=None,
                                              participants_organizer=None,
                                              participants_attendees=None,
                                              participants_producers=None,
                                              participants_contributors=None):
    return client.create_online_meeting(user_id=user_id,
                                        id=id_,
                                        creation_date_time=creation_date_time,
                                        start_date_time=start_date_time,
                                        end_date_time=end_date_time,
                                        canceled_date_time=canceled_date_time,
                                        expiration_date_time=expiration_date_time,
                                        entry_exit_announcement=entry_exit_announcement,
                                        join_url=join_url,
                                        subject=subject,
                                        is_cancelled=is_cancelled,
                                        is_broadcast=is_broadcast,
                                        access_level=access_level,
                                        capabilities=capabilities,
                                        audio_conferencing=audio_conferencing,
                                        chat_info=chat_info,
                                        video_teleconference_id=video_teleconference_id,
                                        external_id=external_id,
                                        join_information=join_information,
                                        organizer=participants_organizer,
                                        attendees=participants_attendees,
                                        producers=participants_producers,
                                        contributors=participants_contributors)


def onlinemeetings_user_get_online_meeting(client,
                                           user_id,
                                           online_meeting_id,
                                           select=None,
                                           expand=None):
    return client.get_online_meeting(user_id=user_id,
                                     online_meeting_id=online_meeting_id,
                                     select=select,
                                     expand=expand)


def onlinemeetings_user_list_online_meeting(client,
                                            user_id,
                                            orderby=None,
                                            select=None,
                                            expand=None):
    return client.list_online_meeting(user_id=user_id,
                                      orderby=orderby,
                                      select=select,
                                      expand=expand)
