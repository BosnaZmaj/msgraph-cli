# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


def cf_accessreview_cl(cli_ctx, *_):
    from msgraph.cli.core.commands.client_factory import get_mgmt_service_client
    from ..vendored_sdks.accessreview import IdentityAccessReview
    return get_mgmt_service_client(cli_ctx,
                                   IdentityAccessReview,
                                   subscription_bound=False,
                                   base_url_bound=False)


def cf_access_review_decision_access_review_decision(cli_ctx, *_):
    return cf_accessreview_cl(cli_ctx).access_review_decision_access_review_decision


def cf_access_review_access_review(cli_ctx, *_):
    return cf_accessreview_cl(cli_ctx).access_review_access_review


def cf_access_review(cli_ctx, *_):
    return cf_accessreview_cl(cli_ctx).access_review


def cf_business_flow_template_business_flow_template(cli_ctx, *_):
    return cf_accessreview_cl(cli_ctx).business_flow_template_business_flow_template


def cf_program_control_program_control(cli_ctx, *_):
    return cf_accessreview_cl(cli_ctx).program_control_program_control


def cf_program_control(cli_ctx, *_):
    return cf_accessreview_cl(cli_ctx).program_control


def cf_program_control_type_program_control_type(cli_ctx, *_):
    return cf_accessreview_cl(cli_ctx).program_control_type_program_control_type


def cf_program_program(cli_ctx, *_):
    return cf_accessreview_cl(cli_ctx).program_program


def cf_program(cli_ctx, *_):
    return cf_accessreview_cl(cli_ctx).program
