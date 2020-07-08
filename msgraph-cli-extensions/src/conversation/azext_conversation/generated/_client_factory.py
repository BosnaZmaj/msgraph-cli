# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


def cf_conversation_cl(cli_ctx, *_):
    from msgraph.cli.core.commands.client_factory import get_mgmt_service_client
    from ..vendored_sdks.conversation import GroupsConversation
    return get_mgmt_service_client(cli_ctx,
                                   GroupsConversation,
                                   subscription_bound=False,
                                   base_url_bound=False)


def cf_group(cli_ctx, *_):
    return cf_conversation_cl(cli_ctx).group


def cf_group_conversation(cli_ctx, *_):
    return cf_conversation_cl(cli_ctx).group_conversation


def cf_group_conversation_thread(cli_ctx, *_):
    return cf_conversation_cl(cli_ctx).group_conversation_thread


def cf_group_conversation_thread_post(cli_ctx, *_):
    return cf_conversation_cl(cli_ctx).group_conversation_thread_post
