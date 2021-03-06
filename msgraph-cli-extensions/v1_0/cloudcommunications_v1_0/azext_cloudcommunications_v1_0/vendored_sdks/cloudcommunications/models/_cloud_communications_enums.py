# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum, EnumMeta
from six import with_metaclass

class _CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(self, name):
        return super().__getitem__(name.upper())

    def __getattr__(cls, name):
        """Return the enum member matching `name`
        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.
        """
        try:
            return cls._member_map_[name.upper()]
        except KeyError:
            raise AttributeError(name)


class Get2ItemsItem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    AUDIO_CONFERENCING = "audioConferencing"
    CHAT_INFO = "chatInfo"
    CREATION_DATE_TIME = "creationDateTime"
    END_DATE_TIME = "endDateTime"
    EXTERNAL_ID = "externalId"
    JOIN_INFORMATION = "joinInformation"
    JOIN_WEB_URL = "joinWebUrl"
    PARTICIPANTS = "participants"
    START_DATE_TIME = "startDateTime"
    SUBJECT = "subject"
    VIDEO_TELECONFERENCE_ID = "videoTeleconferenceId"

class Get6ItemsItem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    AUDIO_CONFERENCING = "audioConferencing"
    AUDIO_CONFERENCING_DESC = "audioConferencing desc"
    CHAT_INFO = "chatInfo"
    CHAT_INFO_DESC = "chatInfo desc"
    CREATION_DATE_TIME = "creationDateTime"
    CREATION_DATE_TIME_DESC = "creationDateTime desc"
    END_DATE_TIME = "endDateTime"
    END_DATE_TIME_DESC = "endDateTime desc"
    EXTERNAL_ID = "externalId"
    EXTERNAL_ID_DESC = "externalId desc"
    JOIN_INFORMATION = "joinInformation"
    JOIN_INFORMATION_DESC = "joinInformation desc"
    JOIN_WEB_URL = "joinWebUrl"
    JOIN_WEB_URL_DESC = "joinWebUrl desc"
    PARTICIPANTS = "participants"
    PARTICIPANTS_DESC = "participants desc"
    START_DATE_TIME = "startDateTime"
    START_DATE_TIME_DESC = "startDateTime desc"
    SUBJECT = "subject"
    SUBJECT_DESC = "subject desc"
    VIDEO_TELECONFERENCE_ID = "videoTeleconferenceId"
    VIDEO_TELECONFERENCE_ID_DESC = "videoTeleconferenceId desc"

class Get7ItemsItem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    AUDIO_CONFERENCING = "audioConferencing"
    CHAT_INFO = "chatInfo"
    CREATION_DATE_TIME = "creationDateTime"
    END_DATE_TIME = "endDateTime"
    EXTERNAL_ID = "externalId"
    JOIN_INFORMATION = "joinInformation"
    JOIN_WEB_URL = "joinWebUrl"
    PARTICIPANTS = "participants"
    START_DATE_TIME = "startDateTime"
    SUBJECT = "subject"
    VIDEO_TELECONFERENCE_ID = "videoTeleconferenceId"

class MicrosoftGraphBodyType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    TEXT = "text"
    HTML = "html"
