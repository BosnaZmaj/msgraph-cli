# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-statements
# pylint: disable=too-many-locals

from msgraph.cli.core.commands import CliCommandType


def load_command_table(self, _):

    from azext_onlinemeetings.generated._client_factory import cf_user
    onlinemeetings_user = CliCommandType(
        operations_tmpl='azext_onlinemeetings.vendored_sdks.onlinemeetings.operations._user_operations#UserOperations.{'
        '}',
        client_factory=cf_user)
    with self.command_group('onlinemeetings user', onlinemeetings_user, client_factory=cf_user,
                            is_experimental=True) as g:
        g.custom_command('update', 'onlinemeetings_user_update')
        g.custom_command('create-online-meeting', 'onlinemeetings_user_create_online_meeting')
        g.custom_command('get-online-meeting', 'onlinemeetings_user_get_online_meeting')
        g.custom_command('list-online-meeting', 'onlinemeetings_user_list_online_meeting')
