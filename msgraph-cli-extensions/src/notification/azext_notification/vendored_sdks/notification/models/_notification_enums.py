# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum

class Get2ItemsItem(str, Enum):

    id = "id"
    target_host_name = "targetHostName"
    expiration_date_time = "expirationDateTime"
    payload = "payload"
    display_time_to_live = "displayTimeToLive"
    priority = "priority"
    group_name = "groupName"
    target_policy = "targetPolicy"

class Get6ItemsItem(str, Enum):

    id = "id"
    id_desc = "id desc"
    target_host_name = "targetHostName"
    target_host_name_desc = "targetHostName desc"
    expiration_date_time = "expirationDateTime"
    expiration_date_time_desc = "expirationDateTime desc"
    payload = "payload"
    payload_desc = "payload desc"
    display_time_to_live = "displayTimeToLive"
    display_time_to_live_desc = "displayTimeToLive desc"
    priority = "priority"
    priority_desc = "priority desc"
    group_name = "groupName"
    group_name_desc = "groupName desc"
    target_policy = "targetPolicy"
    target_policy_desc = "targetPolicy desc"

class Get7ItemsItem(str, Enum):

    id = "id"
    target_host_name = "targetHostName"
    expiration_date_time = "expirationDateTime"
    payload = "payload"
    display_time_to_live = "displayTimeToLive"
    priority = "priority"
    group_name = "groupName"
    target_policy = "targetPolicy"

class MicrosoftGraphPriority(str, Enum):
    """priority
    """

    none = "None"
    high = "High"
    low = "Low"
