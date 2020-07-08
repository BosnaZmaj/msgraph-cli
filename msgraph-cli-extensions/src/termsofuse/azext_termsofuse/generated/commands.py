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

    from azext_termsofuse.generated._client_factory import cf_agreement_acceptance_agreement_acceptance
    termsofuse_agreement_acceptance_agreement_acceptance = CliCommandType(
        operations_tmpl='azext_termsofuse.vendored_sdks.termsofuse.operations._agreement_acceptance_agreement_acceptanc'
        'e_operations#AgreementAcceptanceOperations.{}',
        client_factory=cf_agreement_acceptance_agreement_acceptance)
    with self.command_group('termsofuse agreement-acceptance-agreement-acceptance',
                            termsofuse_agreement_acceptance_agreement_acceptance,
                            client_factory=cf_agreement_acceptance_agreement_acceptance, is_experimental=True) as g:
        g.custom_command('update', 'termsofuse_agreement_acceptance_agreement_acceptance_update')
        g.custom_command('delete', 'termsofuse_agreement_acceptance_agreement_acceptance_delete')
        g.custom_command('create-agreement-acceptance', 'termsofuse_agreement_acceptance_agreement_acceptance_create_ag'
                         'reement_acceptance')
        g.custom_command('get-agreement-acceptance', 'termsofuse_agreement_acceptance_agreement_acceptance_get_agreemen'
                         't_acceptance')
        g.custom_command('list-agreement-acceptance', 'termsofuse_agreement_acceptance_agreement_acceptance_list_agreem'
                         'ent_acceptance')

    from azext_termsofuse.generated._client_factory import cf_agreement_agreement
    termsofuse_agreement_agreement = CliCommandType(
        operations_tmpl='azext_termsofuse.vendored_sdks.termsofuse.operations._agreement_agreement_operations#Agreement'
        'Operations.{}',
        client_factory=cf_agreement_agreement)
    with self.command_group('termsofuse agreement-agreement', termsofuse_agreement_agreement,
                            client_factory=cf_agreement_agreement, is_experimental=True) as g:
        g.custom_command('update', 'termsofuse_agreement_agreement_update')
        g.custom_command('delete', 'termsofuse_agreement_agreement_delete')
        g.custom_command('create-agreement', 'termsofuse_agreement_agreement_create_agreement')
        g.custom_command('get-agreement', 'termsofuse_agreement_agreement_get_agreement')
        g.custom_command('list-agreement', 'termsofuse_agreement_agreement_list_agreement')

    from azext_termsofuse.generated._client_factory import cf_agreement
    termsofuse_agreement = CliCommandType(
        operations_tmpl='azext_termsofuse.vendored_sdks.termsofuse.operations._agreement_operations#AgreementOperations'
        '.{}',
        client_factory=cf_agreement)
    with self.command_group('termsofuse agreement', termsofuse_agreement, client_factory=cf_agreement,
                            is_experimental=True) as g:
        g.custom_command('update', 'termsofuse_agreement_update')
        g.custom_command('create-file', 'termsofuse_agreement_create_file')
        g.custom_command('get-file', 'termsofuse_agreement_get_file')
        g.custom_command('list-file', 'termsofuse_agreement_list_file')

    from azext_termsofuse.generated._client_factory import cf_user
    termsofuse_user = CliCommandType(
        operations_tmpl='azext_termsofuse.vendored_sdks.termsofuse.operations._user_operations#UserOperations.{}',
        client_factory=cf_user)
    with self.command_group('termsofuse user', termsofuse_user, client_factory=cf_user, is_experimental=True) as g:
        g.custom_command('get-agreement-acceptance', 'termsofuse_user_get_agreement_acceptance')
        g.custom_command('list-agreement-acceptance', 'termsofuse_user_list_agreement_acceptance')
