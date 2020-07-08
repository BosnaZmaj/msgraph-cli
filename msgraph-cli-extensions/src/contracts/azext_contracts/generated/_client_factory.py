# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


def cf_contracts_cl(cli_ctx, *_):
    from msgraph.cli.core.commands.client_factory import get_mgmt_service_client
    from ..vendored_sdks.contracts import IdentityContracts
    return get_mgmt_service_client(cli_ctx,
                                   IdentityContracts,
                                   subscription_bound=False,
                                   base_url_bound=False)


def cf_contract_contract(cli_ctx, *_):
    return cf_contracts_cl(cli_ctx).contract_contract


def cf_contract(cli_ctx, *_):
    return cf_contracts_cl(cli_ctx).contract
