# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=line-too-long
# pylint: disable=too-many-statements
# pylint: disable=too-many-locals

from msgraph.cli.core.commands import CliCommandType


def load_command_table(self, _):

    from azext_identitydirectorymanagement_v1_0.generated._client_factory import cf_contact_org_contact
    identitydirectorymanagement_v1_0_contact_org_contact = CliCommandType(
        operations_tmpl='azext_identitydirectorymanagement_v1_0.vendored_sdks.identitydirectorymanagement.operations._c'
        'ontact_org_contact_operations#ContactOrgContactOperations.{}',
        client_factory=cf_contact_org_contact)
    with self.command_group('identitydirectorymanagement', identitydirectorymanagement_v1_0_contact_org_contact,
                            client_factory=cf_contact_org_contact) as g:
        g.custom_command('delete', 'identitydirectorymanagement_delete', confirmation=True)
        g.custom_command('create-org-contact', 'identitydirectorymanagement_create_org_contact')
        g.custom_command('get-org-contact', 'identitydirectorymanagement_get_org_contact')
        g.custom_command('list-org-contact', 'identitydirectorymanagement_list_org_contact')
        g.custom_command('update-org-contact', 'identitydirectorymanagement_update_org_contact')

    from azext_identitydirectorymanagement_v1_0.generated._client_factory import cf_contact
    identitydirectorymanagement_v1_0_contact = CliCommandType(
        operations_tmpl='azext_identitydirectorymanagement_v1_0.vendored_sdks.identitydirectorymanagement.operations._c'
        'ontact_operations#ContactOperations.{}',
        client_factory=cf_contact)
    with self.command_group('identitydirectorymanagement', identitydirectorymanagement_v1_0_contact,
                            client_factory=cf_contact) as g:
        g.custom_command('delete', 'identitydirectorymanagement_delete', confirmation=True)
        g.custom_command('check-member-group', 'identitydirectorymanagement_check_member_group')
        g.custom_command('check-member-object', 'identitydirectorymanagement_check_member_object')
        g.custom_command('create-ref-direct-report', 'identitydirectorymanagement_create_ref_direct_report')
        g.custom_command('create-ref-member-of', 'identitydirectorymanagement_create_ref_member_of')
        g.custom_command('create-ref-transitive-member-of', 'identitydirectorymanagement_create_ref_transitive_member_o'
                         'f')
        g.custom_command('delta', 'identitydirectorymanagement_delta')
        g.custom_command('get-available-extension-property', 'identitydirectorymanagement_get_available_extension_prope'
                         'rty')
        g.custom_command('get-by-id', 'identitydirectorymanagement_get_by_id')
        g.custom_command('get-manager', 'identitydirectorymanagement_get_manager')
        g.custom_command('get-member-group', 'identitydirectorymanagement_get_member_group')
        g.custom_command('get-member-object', 'identitydirectorymanagement_get_member_object')
        g.custom_command('get-ref-manager', 'identitydirectorymanagement_get_ref_manager')
        g.custom_command('list-direct-report', 'identitydirectorymanagement_list_direct_report')
        g.custom_command('list-member-of', 'identitydirectorymanagement_list_member_of')
        g.custom_command('list-ref-direct-report', 'identitydirectorymanagement_list_ref_direct_report')
        g.custom_command('list-ref-member-of', 'identitydirectorymanagement_list_ref_member_of')
        g.custom_command('list-ref-transitive-member-of', 'identitydirectorymanagement_list_ref_transitive_member_of')
        g.custom_command('list-transitive-member-of', 'identitydirectorymanagement_list_transitive_member_of')
        g.custom_command('restore', 'identitydirectorymanagement_restore')
        g.custom_command('set-ref-manager', 'identitydirectorymanagement_set_ref_manager')
        g.custom_command('validate-property', 'identitydirectorymanagement_validate_property')

    from azext_identitydirectorymanagement_v1_0.generated._client_factory import cf_contract_contract
    identitydirectorymanagement_v1_0_contract_contract = CliCommandType(
        operations_tmpl='azext_identitydirectorymanagement_v1_0.vendored_sdks.identitydirectorymanagement.operations._c'
        'ontract_contract_operations#ContractContractOperations.{}',
        client_factory=cf_contract_contract)
    with self.command_group('identitydirectorymanagement', identitydirectorymanagement_v1_0_contract_contract,
                            client_factory=cf_contract_contract) as g:
        g.custom_command('delete', 'identitydirectorymanagement_delete', confirmation=True)
        g.custom_command('create-contract', 'identitydirectorymanagement_create_contract')
        g.custom_command('get-contract', 'identitydirectorymanagement_get_contract')
        g.custom_command('list-contract', 'identitydirectorymanagement_list_contract')
        g.custom_command('update-contract', 'identitydirectorymanagement_update_contract')

    from azext_identitydirectorymanagement_v1_0.generated._client_factory import cf_contract
    identitydirectorymanagement_v1_0_contract = CliCommandType(
        operations_tmpl='azext_identitydirectorymanagement_v1_0.vendored_sdks.identitydirectorymanagement.operations._c'
        'ontract_operations#ContractOperations.{}',
        client_factory=cf_contract)
    with self.command_group('identitydirectorymanagement', identitydirectorymanagement_v1_0_contract,
                            client_factory=cf_contract) as g:
        g.custom_command('check-member-group', 'identitydirectorymanagement_check_member_group')
        g.custom_command('check-member-object', 'identitydirectorymanagement_check_member_object')
        g.custom_command('get-available-extension-property', 'identitydirectorymanagement_get_available_extension_prope'
                         'rty')
        g.custom_command('get-by-id', 'identitydirectorymanagement_get_by_id')
        g.custom_command('get-member-group', 'identitydirectorymanagement_get_member_group')
        g.custom_command('get-member-object', 'identitydirectorymanagement_get_member_object')
        g.custom_command('restore', 'identitydirectorymanagement_restore')
        g.custom_command('validate-property', 'identitydirectorymanagement_validate_property')

    from azext_identitydirectorymanagement_v1_0.generated._client_factory import cf_device_device
    identitydirectorymanagement_v1_0_device_device = CliCommandType(
        operations_tmpl='azext_identitydirectorymanagement_v1_0.vendored_sdks.identitydirectorymanagement.operations._d'
        'evice_device_operations#DeviceDeviceOperations.{}',
        client_factory=cf_device_device)
    with self.command_group('identitydirectorymanagement', identitydirectorymanagement_v1_0_device_device,
                            client_factory=cf_device_device) as g:
        g.custom_command('delete', 'identitydirectorymanagement_delete', confirmation=True)
        g.custom_command('create-device', 'identitydirectorymanagement_create_device')
        g.custom_command('get-device', 'identitydirectorymanagement_get_device')
        g.custom_command('list-device', 'identitydirectorymanagement_list_device')
        g.custom_command('update-device', 'identitydirectorymanagement_update_device')

    from azext_identitydirectorymanagement_v1_0.generated._client_factory import cf_device
    identitydirectorymanagement_v1_0_device = CliCommandType(
        operations_tmpl='azext_identitydirectorymanagement_v1_0.vendored_sdks.identitydirectorymanagement.operations._d'
        'evice_operations#DeviceOperations.{}',
        client_factory=cf_device)
    with self.command_group('identitydirectorymanagement', identitydirectorymanagement_v1_0_device,
                            client_factory=cf_device) as g:
        g.custom_command('delete', 'identitydirectorymanagement_delete', confirmation=True)
        g.custom_command('check-member-group', 'identitydirectorymanagement_check_member_group')
        g.custom_command('check-member-object', 'identitydirectorymanagement_check_member_object')
        g.custom_command('create-extension', 'identitydirectorymanagement_create_extension')
        g.custom_command('create-ref-member-of', 'identitydirectorymanagement_create_ref_member_of')
        g.custom_command('create-ref-registered-owner', 'identitydirectorymanagement_create_ref_registered_owner')
        g.custom_command('create-ref-registered-user', 'identitydirectorymanagement_create_ref_registered_user')
        g.custom_command('create-ref-transitive-member-of', 'identitydirectorymanagement_create_ref_transitive_member_o'
                         'f')
        g.custom_command('get-available-extension-property', 'identitydirectorymanagement_get_available_extension_prope'
                         'rty')
        g.custom_command('get-by-id', 'identitydirectorymanagement_get_by_id')
        g.custom_command('get-extension', 'identitydirectorymanagement_get_extension')
        g.custom_command('get-member-group', 'identitydirectorymanagement_get_member_group')
        g.custom_command('get-member-object', 'identitydirectorymanagement_get_member_object')
        g.custom_command('list-extension', 'identitydirectorymanagement_list_extension')
        g.custom_command('list-member-of', 'identitydirectorymanagement_list_member_of')
        g.custom_command('list-ref-member-of', 'identitydirectorymanagement_list_ref_member_of')
        g.custom_command('list-ref-registered-owner', 'identitydirectorymanagement_list_ref_registered_owner')
        g.custom_command('list-ref-registered-user', 'identitydirectorymanagement_list_ref_registered_user')
        g.custom_command('list-ref-transitive-member-of', 'identitydirectorymanagement_list_ref_transitive_member_of')
        g.custom_command('list-registered-owner', 'identitydirectorymanagement_list_registered_owner')
        g.custom_command('list-registered-user', 'identitydirectorymanagement_list_registered_user')
        g.custom_command('list-transitive-member-of', 'identitydirectorymanagement_list_transitive_member_of')
        g.custom_command('restore', 'identitydirectorymanagement_restore')
        g.custom_command('update-extension', 'identitydirectorymanagement_update_extension')
        g.custom_command('validate-property', 'identitydirectorymanagement_validate_property')

    from azext_identitydirectorymanagement_v1_0.generated._client_factory import cf_directory_directory
    identitydirectorymanagement_v1_0_directory_directory = CliCommandType(
        operations_tmpl='azext_identitydirectorymanagement_v1_0.vendored_sdks.identitydirectorymanagement.operations._d'
        'irectory_directory_operations#DirectoryDirectoryOperations.{}',
        client_factory=cf_directory_directory)
    with self.command_group('identitydirectorymanagement', identitydirectorymanagement_v1_0_directory_directory,
                            client_factory=cf_directory_directory) as g:
        g.custom_command('get-directory', 'identitydirectorymanagement_get_directory')
        g.custom_command('update-directory', 'identitydirectorymanagement_update_directory')

    from azext_identitydirectorymanagement_v1_0.generated._client_factory import cf_directory
    identitydirectorymanagement_v1_0_directory = CliCommandType(
        operations_tmpl='azext_identitydirectorymanagement_v1_0.vendored_sdks.identitydirectorymanagement.operations._d'
        'irectory_operations#DirectoryOperations.{}',
        client_factory=cf_directory)
    with self.command_group('identitydirectorymanagement', identitydirectorymanagement_v1_0_directory,
                            client_factory=cf_directory) as g:
        g.custom_command('delete', 'identitydirectorymanagement_delete', confirmation=True)
        g.custom_command('create-administrative-unit', 'identitydirectorymanagement_create_administrative_unit')
        g.custom_command('create-deleted-item', 'identitydirectorymanagement_create_deleted_item')
        g.custom_command('get-administrative-unit', 'identitydirectorymanagement_get_administrative_unit')
        g.custom_command('get-deleted-item', 'identitydirectorymanagement_get_deleted_item')
        g.custom_command('list-administrative-unit', 'identitydirectorymanagement_list_administrative_unit')
        g.custom_command('list-deleted-item', 'identitydirectorymanagement_list_deleted_item')
        g.custom_command('update-administrative-unit', 'identitydirectorymanagement_update_administrative_unit')
        g.custom_command('update-deleted-item', 'identitydirectorymanagement_update_deleted_item')

    from azext_identitydirectorymanagement_v1_0.generated._client_factory import cf_directory_administrative_unit
    identitydirectorymanagement_v1_0_directory_administrative_unit = CliCommandType(
        operations_tmpl='azext_identitydirectorymanagement_v1_0.vendored_sdks.identitydirectorymanagement.operations._d'
        'irectory_administrative_unit_operations#DirectoryAdministrativeUnitOperations.{}',
        client_factory=cf_directory_administrative_unit)
    with self.command_group('identitydirectorymanagement',
                            identitydirectorymanagement_v1_0_directory_administrative_unit,
                            client_factory=cf_directory_administrative_unit) as g:
        g.custom_command('delete', 'identitydirectorymanagement_delete', confirmation=True)
        g.custom_command('create-extension', 'identitydirectorymanagement_create_extension')
        g.custom_command('create-ref-member', 'identitydirectorymanagement_create_ref_member')
        g.custom_command('create-scoped-role-member', 'identitydirectorymanagement_create_scoped_role_member')
        g.custom_command('delta', 'identitydirectorymanagement_delta')
        g.custom_command('get-extension', 'identitydirectorymanagement_get_extension')
        g.custom_command('get-scoped-role-member', 'identitydirectorymanagement_get_scoped_role_member')
        g.custom_command('list-extension', 'identitydirectorymanagement_list_extension')
        g.custom_command('list-member', 'identitydirectorymanagement_list_member')
        g.custom_command('list-ref-member', 'identitydirectorymanagement_list_ref_member')
        g.custom_command('list-scoped-role-member', 'identitydirectorymanagement_list_scoped_role_member')
        g.custom_command('update-extension', 'identitydirectorymanagement_update_extension')
        g.custom_command('update-scoped-role-member', 'identitydirectorymanagement_update_scoped_role_member')

    from azext_identitydirectorymanagement_v1_0.generated._client_factory import cf_directory_role_directory_role
    identitydirectorymanagement_v1_0_directory_role_directory_role = CliCommandType(
        operations_tmpl='azext_identitydirectorymanagement_v1_0.vendored_sdks.identitydirectorymanagement.operations._d'
        'irectory_role_directory_role_operations#DirectoryRoleDirectoryRoleOperations.{}',
        client_factory=cf_directory_role_directory_role)
    with self.command_group('identitydirectorymanagement',
                            identitydirectorymanagement_v1_0_directory_role_directory_role,
                            client_factory=cf_directory_role_directory_role) as g:
        g.custom_command('delete', 'identitydirectorymanagement_delete', confirmation=True)
        g.custom_command('create-directory-role', 'identitydirectorymanagement_create_directory_role')
        g.custom_command('get-directory-role', 'identitydirectorymanagement_get_directory_role')
        g.custom_command('list-directory-role', 'identitydirectorymanagement_list_directory_role')
        g.custom_command('update-directory-role', 'identitydirectorymanagement_update_directory_role')

    from azext_identitydirectorymanagement_v1_0.generated._client_factory import cf_directory_role
    identitydirectorymanagement_v1_0_directory_role = CliCommandType(
        operations_tmpl='azext_identitydirectorymanagement_v1_0.vendored_sdks.identitydirectorymanagement.operations._d'
        'irectory_role_operations#DirectoryRoleOperations.{}',
        client_factory=cf_directory_role)
    with self.command_group('identitydirectorymanagement', identitydirectorymanagement_v1_0_directory_role,
                            client_factory=cf_directory_role) as g:
        g.custom_command('delete', 'identitydirectorymanagement_delete', confirmation=True)
        g.custom_command('check-member-group', 'identitydirectorymanagement_check_member_group')
        g.custom_command('check-member-object', 'identitydirectorymanagement_check_member_object')
        g.custom_command('create-ref-member', 'identitydirectorymanagement_create_ref_member')
        g.custom_command('create-scoped-member', 'identitydirectorymanagement_create_scoped_member')
        g.custom_command('delta', 'identitydirectorymanagement_delta')
        g.custom_command('get-available-extension-property', 'identitydirectorymanagement_get_available_extension_prope'
                         'rty')
        g.custom_command('get-by-id', 'identitydirectorymanagement_get_by_id')
        g.custom_command('get-member-group', 'identitydirectorymanagement_get_member_group')
        g.custom_command('get-member-object', 'identitydirectorymanagement_get_member_object')
        g.custom_command('get-scoped-member', 'identitydirectorymanagement_get_scoped_member')
        g.custom_command('list-member', 'identitydirectorymanagement_list_member')
        g.custom_command('list-ref-member', 'identitydirectorymanagement_list_ref_member')
        g.custom_command('list-scoped-member', 'identitydirectorymanagement_list_scoped_member')
        g.custom_command('restore', 'identitydirectorymanagement_restore')
        g.custom_command('update-scoped-member', 'identitydirectorymanagement_update_scoped_member')
        g.custom_command('validate-property', 'identitydirectorymanagement_validate_property')

    from azext_identitydirectorymanagement_v1_0.generated._client_factory import cf_directory_role_template_directory_role_template
    identitydirectorymanagement_v1_0_directory_role_template_directory_role_template = CliCommandType(
        operations_tmpl='azext_identitydirectorymanagement_v1_0.vendored_sdks.identitydirectorymanagement.operations._d'
        'irectory_role_template_directory_role_template_operations#DirectoryRoleTemplateDirectoryRoleTemplateOperations'
        '.{}',
        client_factory=cf_directory_role_template_directory_role_template)
    with self.command_group('identitydirectorymanagement',
                            identitydirectorymanagement_v1_0_directory_role_template_directory_role_template,
                            client_factory=cf_directory_role_template_directory_role_template) as g:
        g.custom_command('delete', 'identitydirectorymanagement_delete', confirmation=True)
        g.custom_command('create-directory-role-template',
                         'identitydirectorymanagement_create_directory_role_template')
        g.custom_command('get-directory-role-template', 'identitydirectorymanagement_get_directory_role_template')
        g.custom_command('list-directory-role-template', 'identitydirectorymanagement_list_directory_role_template')
        g.custom_command('update-directory-role-template',
                         'identitydirectorymanagement_update_directory_role_template')

    from azext_identitydirectorymanagement_v1_0.generated._client_factory import cf_directory_role_template
    identitydirectorymanagement_v1_0_directory_role_template = CliCommandType(
        operations_tmpl='azext_identitydirectorymanagement_v1_0.vendored_sdks.identitydirectorymanagement.operations._d'
        'irectory_role_template_operations#DirectoryRoleTemplateOperations.{}',
        client_factory=cf_directory_role_template)
    with self.command_group('identitydirectorymanagement', identitydirectorymanagement_v1_0_directory_role_template,
                            client_factory=cf_directory_role_template) as g:
        g.custom_command('check-member-group', 'identitydirectorymanagement_check_member_group')
        g.custom_command('check-member-object', 'identitydirectorymanagement_check_member_object')
        g.custom_command('get-available-extension-property', 'identitydirectorymanagement_get_available_extension_prope'
                         'rty')
        g.custom_command('get-by-id', 'identitydirectorymanagement_get_by_id')
        g.custom_command('get-member-group', 'identitydirectorymanagement_get_member_group')
        g.custom_command('get-member-object', 'identitydirectorymanagement_get_member_object')
        g.custom_command('restore', 'identitydirectorymanagement_restore')
        g.custom_command('validate-property', 'identitydirectorymanagement_validate_property')

    from azext_identitydirectorymanagement_v1_0.generated._client_factory import cf_domain_domain
    identitydirectorymanagement_v1_0_domain_domain = CliCommandType(
        operations_tmpl='azext_identitydirectorymanagement_v1_0.vendored_sdks.identitydirectorymanagement.operations._d'
        'omain_domain_operations#DomainDomainOperations.{}',
        client_factory=cf_domain_domain)
    with self.command_group('identitydirectorymanagement', identitydirectorymanagement_v1_0_domain_domain,
                            client_factory=cf_domain_domain) as g:
        g.custom_command('delete', 'identitydirectorymanagement_delete', confirmation=True)
        g.custom_command('create-domain', 'identitydirectorymanagement_create_domain')
        g.custom_command('get-domain', 'identitydirectorymanagement_get_domain')
        g.custom_command('list-domain', 'identitydirectorymanagement_list_domain')
        g.custom_command('update-domain', 'identitydirectorymanagement_update_domain')

    from azext_identitydirectorymanagement_v1_0.generated._client_factory import cf_domain
    identitydirectorymanagement_v1_0_domain = CliCommandType(
        operations_tmpl='azext_identitydirectorymanagement_v1_0.vendored_sdks.identitydirectorymanagement.operations._d'
        'omain_operations#DomainOperations.{}',
        client_factory=cf_domain)
    with self.command_group('identitydirectorymanagement', identitydirectorymanagement_v1_0_domain,
                            client_factory=cf_domain) as g:
        g.custom_command('delete', 'identitydirectorymanagement_delete', confirmation=True)
        g.custom_command('create-ref-domain-name-reference', 'identitydirectorymanagement_create_ref_domain_name_refere'
                         'nce')
        g.custom_command('create-service-configuration-record', 'identitydirectorymanagement_create_service_configurati'
                         'on_record')
        g.custom_command('create-verification-dns-record',
                         'identitydirectorymanagement_create_verification_dns_record')
        g.custom_command('force-delete', 'identitydirectorymanagement_force_delete')
        g.custom_command('get-service-configuration-record', 'identitydirectorymanagement_get_service_configuration_rec'
                         'ord')
        g.custom_command('get-verification-dns-record', 'identitydirectorymanagement_get_verification_dns_record')
        g.custom_command('list-domain-name-reference', 'identitydirectorymanagement_list_domain_name_reference')
        g.custom_command('list-ref-domain-name-reference',
                         'identitydirectorymanagement_list_ref_domain_name_reference')
        g.custom_command('list-service-configuration-record', 'identitydirectorymanagement_list_service_configuration_r'
                         'ecord')
        g.custom_command('list-verification-dns-record', 'identitydirectorymanagement_list_verification_dns_record')
        g.custom_command('update-service-configuration-record', 'identitydirectorymanagement_update_service_configurati'
                         'on_record')
        g.custom_command('update-verification-dns-record',
                         'identitydirectorymanagement_update_verification_dns_record')
        g.custom_command('verify', 'identitydirectorymanagement_verify')

    from azext_identitydirectorymanagement_v1_0.generated._client_factory import cf_organization_organization
    identitydirectorymanagement_v1_0_organization_organization = CliCommandType(
        operations_tmpl='azext_identitydirectorymanagement_v1_0.vendored_sdks.identitydirectorymanagement.operations._o'
        'rganization_organization_operations#OrganizationOrganizationOperations.{}',
        client_factory=cf_organization_organization)
    with self.command_group('identitydirectorymanagement', identitydirectorymanagement_v1_0_organization_organization,
                            client_factory=cf_organization_organization) as g:
        g.custom_command('delete', 'identitydirectorymanagement_delete', confirmation=True)
        g.custom_command('create-organization', 'identitydirectorymanagement_create_organization')
        g.custom_command('get-organization', 'identitydirectorymanagement_get_organization')
        g.custom_command('list-organization', 'identitydirectorymanagement_list_organization')
        g.custom_command('update-organization', 'identitydirectorymanagement_update_organization')

    from azext_identitydirectorymanagement_v1_0.generated._client_factory import cf_organization
    identitydirectorymanagement_v1_0_organization = CliCommandType(
        operations_tmpl='azext_identitydirectorymanagement_v1_0.vendored_sdks.identitydirectorymanagement.operations._o'
        'rganization_operations#OrganizationOperations.{}',
        client_factory=cf_organization)
    with self.command_group('identitydirectorymanagement', identitydirectorymanagement_v1_0_organization,
                            client_factory=cf_organization) as g:
        g.custom_command('delete', 'identitydirectorymanagement_delete', confirmation=True)
        g.custom_command('check-member-group', 'identitydirectorymanagement_check_member_group')
        g.custom_command('check-member-object', 'identitydirectorymanagement_check_member_object')
        g.custom_command('create-extension', 'identitydirectorymanagement_create_extension')
        g.custom_command('get-available-extension-property', 'identitydirectorymanagement_get_available_extension_prope'
                         'rty')
        g.custom_command('get-by-id', 'identitydirectorymanagement_get_by_id')
        g.custom_command('get-extension', 'identitydirectorymanagement_get_extension')
        g.custom_command('get-member-group', 'identitydirectorymanagement_get_member_group')
        g.custom_command('get-member-object', 'identitydirectorymanagement_get_member_object')
        g.custom_command('list-extension', 'identitydirectorymanagement_list_extension')
        g.custom_command('restore', 'identitydirectorymanagement_restore')
        g.custom_command('set-mobile-device-management-authority', 'identitydirectorymanagement_set_mobile_device_manag'
                         'ement_authority')
        g.custom_command('update-extension', 'identitydirectorymanagement_update_extension')
        g.custom_command('validate-property', 'identitydirectorymanagement_validate_property')

    from azext_identitydirectorymanagement_v1_0.generated._client_factory import cf_subscribed_sku_subscribed_sku
    identitydirectorymanagement_v1_0_subscribed_sku_subscribed_sku = CliCommandType(
        operations_tmpl='azext_identitydirectorymanagement_v1_0.vendored_sdks.identitydirectorymanagement.operations._s'
        'ubscribed_sku_subscribed_sku_operations#SubscribedSkuSubscribedSkuOperations.{}',
        client_factory=cf_subscribed_sku_subscribed_sku)
    with self.command_group('identitydirectorymanagement',
                            identitydirectorymanagement_v1_0_subscribed_sku_subscribed_sku,
                            client_factory=cf_subscribed_sku_subscribed_sku) as g:
        g.custom_command('delete', 'identitydirectorymanagement_delete', confirmation=True)
        g.custom_command('create-subscribed-sku', 'identitydirectorymanagement_create_subscribed_sku')
        g.custom_command('get-subscribed-sku', 'identitydirectorymanagement_get_subscribed_sku')
        g.custom_command('list-subscribed-sku', 'identitydirectorymanagement_list_subscribed_sku')
        g.custom_command('update-subscribed-sku', 'identitydirectorymanagement_update_subscribed_sku')

    from azext_identitydirectorymanagement_v1_0.generated._client_factory import cf_user
    identitydirectorymanagement_v1_0_user = CliCommandType(
        operations_tmpl='azext_identitydirectorymanagement_v1_0.vendored_sdks.identitydirectorymanagement.operations._u'
        'ser_operations#UserOperations.{}',
        client_factory=cf_user)
    with self.command_group('identitydirectorymanagement', identitydirectorymanagement_v1_0_user,
                            client_factory=cf_user) as g:
        g.custom_command('delete', 'identitydirectorymanagement_delete', confirmation=True)
        g.custom_command('create-scoped-role-member-of', 'identitydirectorymanagement_create_scoped_role_member_of')
        g.custom_command('get-scoped-role-member-of', 'identitydirectorymanagement_get_scoped_role_member_of')
        g.custom_command('list-scoped-role-member-of', 'identitydirectorymanagement_list_scoped_role_member_of')
        g.custom_command('update-scoped-role-member-of', 'identitydirectorymanagement_update_scoped_role_member_of')
