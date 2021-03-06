# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


def cf_notes_beta_cl(cli_ctx, *_):
    from msgraph.cli.core.commands.client_factory import get_mgmt_service_client
    from ..vendored_sdks.notes import Notes
    return get_mgmt_service_client(cli_ctx,
                                   Notes,
                                   subscription_bound=False,
                                   base_url_bound=False)


def cf_group(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).group


def cf_group_onenote(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).group_onenote


def cf_group_onenote_notebook(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).group_onenote_notebook


def cf_group_onenote_notebook_section_group(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).group_onenote_notebook_section_group


def cf_group_onenote_notebook_section_group_section(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).group_onenote_notebook_section_group_section


def cf_group_onenote_notebook_section_group_section_page(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).group_onenote_notebook_section_group_section_page


def cf_group_onenote_notebook_section(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).group_onenote_notebook_section


def cf_group_onenote_notebook_section_page(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).group_onenote_notebook_section_page


def cf_group_onenote_notebook_section_parent_section_group(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).group_onenote_notebook_section_parent_section_group


def cf_group_onenote_page(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).group_onenote_page


def cf_group_onenote_page_parent_notebook(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).group_onenote_page_parent_notebook


def cf_group_onenote_page_parent_notebook_section_group(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).group_onenote_page_parent_notebook_section_group


def cf_group_onenote_page_parent_notebook_section_group_section(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).group_onenote_page_parent_notebook_section_group_section


def cf_group_onenote_parent_notebook_section_group_section_page(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).group_onenote_parent_notebook_section_group_section_page


def cf_group_onenote_page_parent_notebook_section(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).group_onenote_page_parent_notebook_section


def cf_group_onenote_parent_notebook_section_page(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).group_onenote_parent_notebook_section_page


def cf_group_onenote_page_parent_notebook_section_parent_section_group(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).group_onenote_page_parent_notebook_section_parent_section_group


def cf_group_onenote_page_parent_section(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).group_onenote_page_parent_section


def cf_group_onenote_parent_section_page(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).group_onenote_parent_section_page


def cf_group_onenote_page_parent_section_parent_notebook(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).group_onenote_page_parent_section_parent_notebook


def cf_group_onenote_page_parent_section_parent_notebook_section_group(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).group_onenote_page_parent_section_parent_notebook_section_group


def cf_group_onenote_page_parent_section_parent_section_group(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).group_onenote_page_parent_section_parent_section_group


def cf_group_onenote_page_parent_section_parent_section_group_parent_notebook(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).group_onenote_page_parent_section_parent_section_group_parent_notebook


def cf_group_onenote_section_group(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).group_onenote_section_group


def cf_group_onenote_section_group_parent_notebook(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).group_onenote_section_group_parent_notebook


def cf_group_onenote_section_group_parent_notebook_section(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).group_onenote_section_group_parent_notebook_section


def cf_group_onenote_section_group_parent_notebook_section_page(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).group_onenote_section_group_parent_notebook_section_page


def cf_group_onenote_section_group_section(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).group_onenote_section_group_section


def cf_group_onenote_section_group_section_page(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).group_onenote_section_group_section_page


def cf_group_onenote_section_group_section_page_parent_notebook(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).group_onenote_section_group_section_page_parent_notebook


def cf_group_onenote_section_group_section_parent_notebook(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).group_onenote_section_group_section_parent_notebook


def cf_group_onenote_section(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).group_onenote_section


def cf_group_onenote_section_page(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).group_onenote_section_page


def cf_group_onenote_section_page_parent_notebook(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).group_onenote_section_page_parent_notebook


def cf_group_onenote_section_page_parent_notebook_section_group(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).group_onenote_section_page_parent_notebook_section_group


def cf_group_onenote_section_parent_notebook(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).group_onenote_section_parent_notebook


def cf_group_onenote_section_parent_notebook_section_group(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).group_onenote_section_parent_notebook_section_group


def cf_group_onenote_section_parent_section_group(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).group_onenote_section_parent_section_group


def cf_group_onenote_section_parent_section_group_parent_notebook(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).group_onenote_section_parent_section_group_parent_notebook


def cf_site(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).site


def cf_site_onenote(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).site_onenote


def cf_site_onenote_notebook(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).site_onenote_notebook


def cf_site_onenote_notebook_section_group(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).site_onenote_notebook_section_group


def cf_site_onenote_notebook_section_group_section(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).site_onenote_notebook_section_group_section


def cf_site_onenote_notebook_section_group_section_page(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).site_onenote_notebook_section_group_section_page


def cf_site_onenote_notebook_section(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).site_onenote_notebook_section


def cf_site_onenote_notebook_section_page(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).site_onenote_notebook_section_page


def cf_site_onenote_notebook_section_parent_section_group(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).site_onenote_notebook_section_parent_section_group


def cf_site_onenote_page(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).site_onenote_page


def cf_site_onenote_page_parent_notebook(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).site_onenote_page_parent_notebook


def cf_site_onenote_page_parent_notebook_section_group(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).site_onenote_page_parent_notebook_section_group


def cf_site_onenote_page_parent_notebook_section_group_section(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).site_onenote_page_parent_notebook_section_group_section


def cf_site_onenote_parent_notebook_section_group_section_page(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).site_onenote_parent_notebook_section_group_section_page


def cf_site_onenote_page_parent_notebook_section(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).site_onenote_page_parent_notebook_section


def cf_site_onenote_parent_notebook_section_page(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).site_onenote_parent_notebook_section_page


def cf_site_onenote_page_parent_notebook_section_parent_section_group(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).site_onenote_page_parent_notebook_section_parent_section_group


def cf_site_onenote_page_parent_section(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).site_onenote_page_parent_section


def cf_site_onenote_parent_section_page(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).site_onenote_parent_section_page


def cf_site_onenote_page_parent_section_parent_notebook(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).site_onenote_page_parent_section_parent_notebook


def cf_site_onenote_page_parent_section_parent_notebook_section_group(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).site_onenote_page_parent_section_parent_notebook_section_group


def cf_site_onenote_page_parent_section_parent_section_group(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).site_onenote_page_parent_section_parent_section_group


def cf_site_onenote_page_parent_section_parent_section_group_parent_notebook(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).site_onenote_page_parent_section_parent_section_group_parent_notebook


def cf_site_onenote_section_group(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).site_onenote_section_group


def cf_site_onenote_section_group_parent_notebook(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).site_onenote_section_group_parent_notebook


def cf_site_onenote_section_group_parent_notebook_section(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).site_onenote_section_group_parent_notebook_section


def cf_site_onenote_section_group_parent_notebook_section_page(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).site_onenote_section_group_parent_notebook_section_page


def cf_site_onenote_section_group_section(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).site_onenote_section_group_section


def cf_site_onenote_section_group_section_page(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).site_onenote_section_group_section_page


def cf_site_onenote_section_group_section_page_parent_notebook(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).site_onenote_section_group_section_page_parent_notebook


def cf_site_onenote_section_group_section_parent_notebook(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).site_onenote_section_group_section_parent_notebook


def cf_site_onenote_section(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).site_onenote_section


def cf_site_onenote_section_page(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).site_onenote_section_page


def cf_site_onenote_section_page_parent_notebook(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).site_onenote_section_page_parent_notebook


def cf_site_onenote_section_page_parent_notebook_section_group(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).site_onenote_section_page_parent_notebook_section_group


def cf_site_onenote_section_parent_notebook(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).site_onenote_section_parent_notebook


def cf_site_onenote_section_parent_notebook_section_group(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).site_onenote_section_parent_notebook_section_group


def cf_site_onenote_section_parent_section_group(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).site_onenote_section_parent_section_group


def cf_site_onenote_section_parent_section_group_parent_notebook(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).site_onenote_section_parent_section_group_parent_notebook


def cf_user(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).user


def cf_user_onenote(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).user_onenote


def cf_user_onenote_notebook(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).user_onenote_notebook


def cf_user_onenote_notebook_section_group(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).user_onenote_notebook_section_group


def cf_user_onenote_notebook_section_group_section(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).user_onenote_notebook_section_group_section


def cf_user_onenote_notebook_section_group_section_page(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).user_onenote_notebook_section_group_section_page


def cf_user_onenote_notebook_section(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).user_onenote_notebook_section


def cf_user_onenote_notebook_section_page(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).user_onenote_notebook_section_page


def cf_user_onenote_notebook_section_parent_section_group(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).user_onenote_notebook_section_parent_section_group


def cf_user_onenote_page(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).user_onenote_page


def cf_user_onenote_page_parent_notebook(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).user_onenote_page_parent_notebook


def cf_user_onenote_page_parent_notebook_section_group(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).user_onenote_page_parent_notebook_section_group


def cf_user_onenote_page_parent_notebook_section_group_section(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).user_onenote_page_parent_notebook_section_group_section


def cf_user_onenote_parent_notebook_section_group_section_page(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).user_onenote_parent_notebook_section_group_section_page


def cf_user_onenote_page_parent_notebook_section(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).user_onenote_page_parent_notebook_section


def cf_user_onenote_parent_notebook_section_page(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).user_onenote_parent_notebook_section_page


def cf_user_onenote_page_parent_notebook_section_parent_section_group(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).user_onenote_page_parent_notebook_section_parent_section_group


def cf_user_onenote_page_parent_section(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).user_onenote_page_parent_section


def cf_user_onenote_parent_section_page(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).user_onenote_parent_section_page


def cf_user_onenote_page_parent_section_parent_notebook(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).user_onenote_page_parent_section_parent_notebook


def cf_user_onenote_page_parent_section_parent_notebook_section_group(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).user_onenote_page_parent_section_parent_notebook_section_group


def cf_user_onenote_page_parent_section_parent_section_group(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).user_onenote_page_parent_section_parent_section_group


def cf_user_onenote_page_parent_section_parent_section_group_parent_notebook(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).user_onenote_page_parent_section_parent_section_group_parent_notebook


def cf_user_onenote_section_group(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).user_onenote_section_group


def cf_user_onenote_section_group_parent_notebook(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).user_onenote_section_group_parent_notebook


def cf_user_onenote_section_group_parent_notebook_section(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).user_onenote_section_group_parent_notebook_section


def cf_user_onenote_section_group_parent_notebook_section_page(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).user_onenote_section_group_parent_notebook_section_page


def cf_user_onenote_section_group_section(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).user_onenote_section_group_section


def cf_user_onenote_section_group_section_page(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).user_onenote_section_group_section_page


def cf_user_onenote_section_group_section_page_parent_notebook(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).user_onenote_section_group_section_page_parent_notebook


def cf_user_onenote_section_group_section_parent_notebook(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).user_onenote_section_group_section_parent_notebook


def cf_user_onenote_section(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).user_onenote_section


def cf_user_onenote_section_page(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).user_onenote_section_page


def cf_user_onenote_section_page_parent_notebook(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).user_onenote_section_page_parent_notebook


def cf_user_onenote_section_page_parent_notebook_section_group(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).user_onenote_section_page_parent_notebook_section_group


def cf_user_onenote_section_parent_notebook(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).user_onenote_section_parent_notebook


def cf_user_onenote_section_parent_notebook_section_group(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).user_onenote_section_parent_notebook_section_group


def cf_user_onenote_section_parent_section_group(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).user_onenote_section_parent_section_group


def cf_user_onenote_section_parent_section_group_parent_notebook(cli_ctx, *_):
    return cf_notes_beta_cl(cli_ctx).user_onenote_section_parent_section_group_parent_notebook
