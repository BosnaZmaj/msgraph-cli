# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

from msgraph.cli.core import AzCommandsLoader
from msgraph.cli.core.commands import CliCommandType
from msgraph.command_modules.profile._exception_handler import profile_exception_handler
import msgraph.command_modules.profile._help


class ProfileCommandsLoader(AzCommandsLoader):
    """Provides profile commands to msgraph-cli
    """
    def __init__(self, cli_ctx, **kwargs):
        super().__init__(cli_ctx, **kwargs)

    def load_command_table(self, args):
        # operations_tmpl is the file that contains the implementation of the command
        command_type = CliCommandType(operations_tmpl='msgraph.command_modules.profile.custom#{}',
                                      exception_handler=profile_exception_handler)
        with self.command_group('cloud', command_type) as group:
            group.command('select', 'select_cloud')
            group.command('add', 'add_cloud')
            group.command('show-current', 'current_cloud')
            group.command('update', 'update_cloud')
            group.command('delete', 'delete_cloud')

        with self.command_group('graph-version', command_type) as group:
            group.command('select', 'select_version')
            group.command('show-current', 'show_version')

        return self.command_table


COMMAND_LOADER_CLS = ProfileCommandsLoader
