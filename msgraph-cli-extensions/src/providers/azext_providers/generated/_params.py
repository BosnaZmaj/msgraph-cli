# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines
# pylint: disable=too-many-statements



def load_arguments(self, _):

    with self.argument_context('providers identity-provider-identity-provider update') as c:
        c.argument('identity_provider_id', help='key: identityProvider-id of identityProvider')
        c.argument('id_', options_list=['--id'], help='Read-only.')
        c.argument('type_', options_list=['--type'], help='')
        c.argument('name', help='')
        c.argument('client_id', help='')
        c.argument('client_secret', help='')

    with self.argument_context('providers identity-provider-identity-provider delete') as c:
        c.argument('identity_provider_id', help='key: identityProvider-id of identityProvider')
        c.argument('if_match', help='ETag')

    with self.argument_context('providers identity-provider-identity-provider create-identity-provider') as c:
        c.argument('id_', options_list=['--id'], help='Read-only.')
        c.argument('type_', options_list=['--type'], help='')
        c.argument('name', help='')
        c.argument('client_id', help='')
        c.argument('client_secret', help='')

    with self.argument_context('providers identity-provider-identity-provider get-identity-provider') as c:
        c.argument('identity_provider_id', help='key: identityProvider-id of identityProvider')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')

    with self.argument_context('providers identity-provider-identity-provider list-identity-provider') as c:
        c.argument('orderby', nargs='*', help='Order items by property values')
        c.argument('select', nargs='*', help='Select properties to be returned')
        c.argument('expand', nargs='*', help='Expand related entities')
