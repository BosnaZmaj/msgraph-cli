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

    from azext_cloudcommunications_v1_0.generated._client_factory import cf_user
    cloudcommunications_v1_0_user = CliCommandType(
        operations_tmpl='azext_cloudcommunications_v1_0.vendored_sdks.cloudcommunications.operations._user_operations#U'
        'serOperations.{}',
        client_factory=cf_user)
    with self.command_group('cloudcommunications', cloudcommunications_v1_0_user, client_factory=cf_user) as g:
        g.custom_command('delete', 'cloudcommunications_delete', confirmation=True)
        g.custom_command('create-online-meeting', 'cloudcommunications_create_online_meeting')
        g.custom_command('get-online-meeting', 'cloudcommunications_get_online_meeting')
        g.custom_command('list-online-meeting', 'cloudcommunications_list_online_meeting')
        g.custom_command('update-online-meeting', 'cloudcommunications_update_online_meeting')
