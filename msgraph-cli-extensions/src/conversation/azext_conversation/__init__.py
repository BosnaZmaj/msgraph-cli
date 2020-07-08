# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msgraph.cli.core import AzCommandsLoader
from azext_conversation.generated._help import helps  # pylint: disable=unused-import
try:
    from azext_conversation.manual._help import helps  # pylint: disable=reimported
except ImportError:
    pass


class GroupsConversationCommandsLoader(AzCommandsLoader):

    def __init__(self, cli_ctx=None):
        from msgraph.cli.core.commands import CliCommandType
        from azext_conversation.generated._client_factory import cf_conversation_cl
        conversation_custom = CliCommandType(
            operations_tmpl='azext_conversation.custom#{}',
            client_factory=cf_conversation_cl)
        parent = super(GroupsConversationCommandsLoader, self)
        parent.__init__(cli_ctx=cli_ctx, custom_command_type=conversation_custom)

    def load_command_table(self, args):
        from azext_conversation.generated.commands import load_command_table
        load_command_table(self, args)
        try:
            from azext_conversation.manual.commands import load_command_table as load_command_table_manual
            load_command_table_manual(self, args)
        except ImportError:
            pass
        return self.command_table

    def load_arguments(self, command):
        from azext_conversation.generated._params import load_arguments
        load_arguments(self, command)
        try:
            from azext_conversation.manual._params import load_arguments as load_arguments_manual
            load_arguments_manual(self, command)
        except ImportError:
            pass


COMMAND_LOADER_CLS = GroupsConversationCommandsLoader
