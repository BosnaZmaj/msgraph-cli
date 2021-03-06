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

    from azext_personalcontacts_beta.generated._client_factory import cf_user
    personalcontacts_beta_user = CliCommandType(
        operations_tmpl='azext_personalcontacts_beta.vendored_sdks.personalcontacts.operations._user_operations#UserOpe'
        'rations.{}',
        client_factory=cf_user)
    with self.command_group('personalcontacts', personalcontacts_beta_user, client_factory=cf_user) as g:
        g.custom_command('delete', 'personalcontacts_delete', confirmation=True)
        g.custom_command('create-contact', 'personalcontacts_create_contact')
        g.custom_command('create-contact-folder', 'personalcontacts_create_contact_folder')
        g.custom_command('get-contact', 'personalcontacts_get_contact')
        g.custom_command('get-contact-folder', 'personalcontacts_get_contact_folder')
        g.custom_command('list-contact', 'personalcontacts_list_contact')
        g.custom_command('list-contact-folder', 'personalcontacts_list_contact_folder')
        g.custom_command('update-contact', 'personalcontacts_update_contact')
        g.custom_command('update-contact-folder', 'personalcontacts_update_contact_folder')

    from azext_personalcontacts_beta.generated._client_factory import cf_user_contact_folder
    personalcontacts_beta_user_contact_folder = CliCommandType(
        operations_tmpl='azext_personalcontacts_beta.vendored_sdks.personalcontacts.operations._user_contact_folder_ope'
        'rations#UserContactFolderOperations.{}',
        client_factory=cf_user_contact_folder)
    with self.command_group('personalcontacts', personalcontacts_beta_user_contact_folder,
                            client_factory=cf_user_contact_folder) as g:
        g.custom_command('delete', 'personalcontacts_delete', confirmation=True)
        g.custom_command('create-child-folder', 'personalcontacts_create_child_folder')
        g.custom_command('create-contact', 'personalcontacts_create_contact')
        g.custom_command('create-multi-value-extended-property', 'personalcontacts_create_multi_value_extended_property'
                         '')
        g.custom_command('create-single-value-extended-property', 'personalcontacts_create_single_value_extended_proper'
                         'ty')
        g.custom_command('get-child-folder', 'personalcontacts_get_child_folder')
        g.custom_command('get-contact', 'personalcontacts_get_contact')
        g.custom_command('get-multi-value-extended-property', 'personalcontacts_get_multi_value_extended_property')
        g.custom_command('get-single-value-extended-property', 'personalcontacts_get_single_value_extended_property')
        g.custom_command('list-child-folder', 'personalcontacts_list_child_folder')
        g.custom_command('list-contact', 'personalcontacts_list_contact')
        g.custom_command('list-multi-value-extended-property', 'personalcontacts_list_multi_value_extended_property')
        g.custom_command('list-single-value-extended-property',
                         'personalcontacts_list_single_value_extended_property')
        g.custom_command('update-child-folder', 'personalcontacts_update_child_folder')
        g.custom_command('update-contact', 'personalcontacts_update_contact')
        g.custom_command('update-multi-value-extended-property', 'personalcontacts_update_multi_value_extended_property'
                         '')
        g.custom_command('update-single-value-extended-property', 'personalcontacts_update_single_value_extended_proper'
                         'ty')

    from azext_personalcontacts_beta.generated._client_factory import cf_user_contact_folder_contact
    personalcontacts_beta_user_contact_folder_contact = CliCommandType(
        operations_tmpl='azext_personalcontacts_beta.vendored_sdks.personalcontacts.operations._user_contact_folder_con'
        'tact_operations#UserContactFolderContactOperations.{}',
        client_factory=cf_user_contact_folder_contact)
    with self.command_group('personalcontacts', personalcontacts_beta_user_contact_folder_contact,
                            client_factory=cf_user_contact_folder_contact) as g:
        g.custom_command('delete', 'personalcontacts_delete', confirmation=True)
        g.custom_command('create-extension', 'personalcontacts_create_extension')
        g.custom_command('create-multi-value-extended-property', 'personalcontacts_create_multi_value_extended_property'
                         '')
        g.custom_command('create-single-value-extended-property', 'personalcontacts_create_single_value_extended_proper'
                         'ty')
        g.custom_command('get-extension', 'personalcontacts_get_extension')
        g.custom_command('get-multi-value-extended-property', 'personalcontacts_get_multi_value_extended_property')
        g.custom_command('get-photo', 'personalcontacts_get_photo')
        g.custom_command('get-photo-content', 'personalcontacts_get_photo_content')
        g.custom_command('get-single-value-extended-property', 'personalcontacts_get_single_value_extended_property')
        g.custom_command('list-extension', 'personalcontacts_list_extension')
        g.custom_command('list-multi-value-extended-property', 'personalcontacts_list_multi_value_extended_property')
        g.custom_command('list-single-value-extended-property',
                         'personalcontacts_list_single_value_extended_property')
        g.custom_command('set-photo-content', 'personalcontacts_set_photo_content')
        g.custom_command('update-extension', 'personalcontacts_update_extension')
        g.custom_command('update-multi-value-extended-property', 'personalcontacts_update_multi_value_extended_property'
                         '')
        g.custom_command('update-photo', 'personalcontacts_update_photo')
        g.custom_command('update-single-value-extended-property', 'personalcontacts_update_single_value_extended_proper'
                         'ty')

    from azext_personalcontacts_beta.generated._client_factory import cf_user_contact
    personalcontacts_beta_user_contact = CliCommandType(
        operations_tmpl='azext_personalcontacts_beta.vendored_sdks.personalcontacts.operations._user_contact_operations'
        '#UserContactOperations.{}',
        client_factory=cf_user_contact)
    with self.command_group('personalcontacts', personalcontacts_beta_user_contact,
                            client_factory=cf_user_contact) as g:
        g.custom_command('delete', 'personalcontacts_delete', confirmation=True)
        g.custom_command('create-extension', 'personalcontacts_create_extension')
        g.custom_command('create-multi-value-extended-property', 'personalcontacts_create_multi_value_extended_property'
                         '')
        g.custom_command('create-single-value-extended-property', 'personalcontacts_create_single_value_extended_proper'
                         'ty')
        g.custom_command('get-extension', 'personalcontacts_get_extension')
        g.custom_command('get-multi-value-extended-property', 'personalcontacts_get_multi_value_extended_property')
        g.custom_command('get-photo', 'personalcontacts_get_photo')
        g.custom_command('get-photo-content', 'personalcontacts_get_photo_content')
        g.custom_command('get-single-value-extended-property', 'personalcontacts_get_single_value_extended_property')
        g.custom_command('list-extension', 'personalcontacts_list_extension')
        g.custom_command('list-multi-value-extended-property', 'personalcontacts_list_multi_value_extended_property')
        g.custom_command('list-single-value-extended-property',
                         'personalcontacts_list_single_value_extended_property')
        g.custom_command('set-photo-content', 'personalcontacts_set_photo_content')
        g.custom_command('update-extension', 'personalcontacts_update_extension')
        g.custom_command('update-multi-value-extended-property', 'personalcontacts_update_multi_value_extended_property'
                         '')
        g.custom_command('update-photo', 'personalcontacts_update_photo')
        g.custom_command('update-single-value-extended-property', 'personalcontacts_update_single_value_extended_proper'
                         'ty')
