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

    from azext_user.generated._client_factory import cf_user_user
    user_user_user = CliCommandType(
        operations_tmpl='azext_user.vendored_sdks.user.operations._user_user_operations#UserOperations.{}',
        client_factory=cf_user_user)
    with self.command_group('user user-user', user_user_user, client_factory=cf_user_user, is_experimental=True) as g:
        g.custom_command('update', 'user_user_user_update')
        g.custom_command('delete', 'user_user_user_delete')
        g.custom_command('create-user', 'user_user_user_create_user')
        g.custom_command('get-user', 'user_user_user_get_user')
        g.custom_command('list-user', 'user_user_user_list_user')

    from azext_user.generated._client_factory import cf_user
    user_user = CliCommandType(
        operations_tmpl='azext_user.vendored_sdks.user.operations._user_operations#UserOperations.{}',
        client_factory=cf_user)
    with self.command_group('user user', user_user, client_factory=cf_user, is_experimental=True) as g:
        g.custom_command('update', 'user_user_update')
        g.custom_command('get-presence', 'user_user_get_presence')
