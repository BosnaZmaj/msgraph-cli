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

from knack.help_files import helps


helps['users'] = """
    type: group
    short-summary: users
"""

helps['users delete'] = """
    type: command
    short-summary: "Delete entity from users"
"""

helps['users create-user'] = """
    type: command
    short-summary: "Add new entity to users"
"""

helps['users get-user'] = """
    type: command
    short-summary: "Get entity from users by key"
"""

helps['users list-user'] = """
    type: command
    short-summary: "Get entities from users"
"""

helps['users update-user'] = """
    type: command
    short-summary: "Update entity in users"
"""

helps['users'] = """
    type: group
    short-summary: users
"""

helps['users delete'] = """
    type: command
    short-summary: "Delete navigation property settings for users"
"""

helps['users create-extension'] = """
    type: command
    short-summary: "Create new navigation property to extensions for users"
"""

helps['users create-license-detail'] = """
    type: command
    short-summary: "Create new navigation property to licenseDetails for users"
    parameters:
      - name: --service-plans
        short-summary: "Information about the service plans assigned with the license. Read-only, Not nullable"
        long-summary: |
            Usage: --service-plans applies-to=XX provisioning-status=XX service-plan-id=XX service-plan-name=XX

            applies-to: The object the service plan can be assigned to. Possible values:'User' - service plan can be \
assigned to individual users.'Company' - service plan can be assigned to the entire tenant.
            provisioning-status: The provisioning status of the service plan. Possible values:'Success' - Service is \
fully provisioned.'Disabled' - Service has been disabled.'PendingInput' - Service is not yet provisioned; awaiting \
service confirmation.'PendingActivation' - Service is provisioned but requires explicit activation by administrator \
(for example, Intune_O365 service plan)'PendingProvisioning' - Microsoft has added a new service to the product SKU \
and it has not been activated in the tenant, yet.
            service-plan-id: The unique identifier of the service plan.
            service-plan-name: The name of the service plan.

            Multiple actions can be specified by using more than one --service-plans argument.
"""

helps['users create-photo'] = """
    type: command
    short-summary: "Create new navigation property to photos for users"
"""

helps['users create-ref-created-object'] = """
    type: command
    short-summary: "Create new navigation property ref to createdObjects for users"
"""

helps['users create-ref-direct-report'] = """
    type: command
    short-summary: "Create new navigation property ref to directReports for users"
"""

helps['users create-ref-member-of'] = """
    type: command
    short-summary: "Create new navigation property ref to memberOf for users"
"""

helps['users create-ref-oauth2-permission-grant'] = """
    type: command
    short-summary: "Create new navigation property ref to oauth2PermissionGrants for users"
"""

helps['users create-ref-owned-device'] = """
    type: command
    short-summary: "Create new navigation property ref to ownedDevices for users"
"""

helps['users create-ref-owned-object'] = """
    type: command
    short-summary: "Create new navigation property ref to ownedObjects for users"
"""

helps['users create-ref-registered-device'] = """
    type: command
    short-summary: "Create new navigation property ref to registeredDevices for users"
"""

helps['users create-ref-transitive-member-of'] = """
    type: command
    short-summary: "Create new navigation property ref to transitiveMemberOf for users"
"""

helps['users get-extension'] = """
    type: command
    short-summary: "Get extensions from users"
"""

helps['users get-license-detail'] = """
    type: command
    short-summary: "Get licenseDetails from users"
"""

helps['users get-manager'] = """
    type: command
    short-summary: "Get manager from users"
"""

helps['users get-outlook'] = """
    type: command
    short-summary: "Get outlook from users"
"""

helps['users get-photo'] = """
    type: command
    short-summary: "Get photo from users"
"""

helps['users get-ref-manager'] = """
    type: command
    short-summary: "Get ref of manager from users"
"""

helps['users get-setting'] = """
    type: command
    short-summary: "Get settings from users"
"""

helps['users list-created-object'] = """
    type: command
    short-summary: "Get createdObjects from users"
"""

helps['users list-direct-report'] = """
    type: command
    short-summary: "Get directReports from users"
"""

helps['users list-extension'] = """
    type: command
    short-summary: "Get extensions from users"
"""

helps['users list-license-detail'] = """
    type: command
    short-summary: "Get licenseDetails from users"
"""

helps['users list-member-of'] = """
    type: command
    short-summary: "Get memberOf from users"
"""

helps['users list-oauth2-permission-grant'] = """
    type: command
    short-summary: "Get oauth2PermissionGrants from users"
"""

helps['users list-owned-device'] = """
    type: command
    short-summary: "Get ownedDevices from users"
"""

helps['users list-owned-object'] = """
    type: command
    short-summary: "Get ownedObjects from users"
"""

helps['users list-photo'] = """
    type: command
    short-summary: "Get photos from users"
"""

helps['users list-ref-created-object'] = """
    type: command
    short-summary: "Get ref of createdObjects from users"
"""

helps['users list-ref-direct-report'] = """
    type: command
    short-summary: "Get ref of directReports from users"
"""

helps['users list-ref-member-of'] = """
    type: command
    short-summary: "Get ref of memberOf from users"
"""

helps['users list-ref-oauth2-permission-grant'] = """
    type: command
    short-summary: "Get ref of oauth2PermissionGrants from users"
"""

helps['users list-ref-owned-device'] = """
    type: command
    short-summary: "Get ref of ownedDevices from users"
"""

helps['users list-ref-owned-object'] = """
    type: command
    short-summary: "Get ref of ownedObjects from users"
"""

helps['users list-ref-registered-device'] = """
    type: command
    short-summary: "Get ref of registeredDevices from users"
"""

helps['users list-ref-transitive-member-of'] = """
    type: command
    short-summary: "Get ref of transitiveMemberOf from users"
"""

helps['users list-registered-device'] = """
    type: command
    short-summary: "Get registeredDevices from users"
"""

helps['users list-transitive-member-of'] = """
    type: command
    short-summary: "Get transitiveMemberOf from users"
"""

helps['users set-ref-manager'] = """
    type: command
    short-summary: "Update the ref of navigation property manager in users"
"""

helps['users update-extension'] = """
    type: command
    short-summary: "Update the navigation property extensions in users"
"""

helps['users update-license-detail'] = """
    type: command
    short-summary: "Update the navigation property licenseDetails in users"
    parameters:
      - name: --service-plans
        short-summary: "Information about the service plans assigned with the license. Read-only, Not nullable"
        long-summary: |
            Usage: --service-plans applies-to=XX provisioning-status=XX service-plan-id=XX service-plan-name=XX

            applies-to: The object the service plan can be assigned to. Possible values:'User' - service plan can be \
assigned to individual users.'Company' - service plan can be assigned to the entire tenant.
            provisioning-status: The provisioning status of the service plan. Possible values:'Success' - Service is \
fully provisioned.'Disabled' - Service has been disabled.'PendingInput' - Service is not yet provisioned; awaiting \
service confirmation.'PendingActivation' - Service is provisioned but requires explicit activation by administrator \
(for example, Intune_O365 service plan)'PendingProvisioning' - Microsoft has added a new service to the product SKU \
and it has not been activated in the tenant, yet.
            service-plan-id: The unique identifier of the service plan.
            service-plan-name: The name of the service plan.

            Multiple actions can be specified by using more than one --service-plans argument.
"""

helps['users update-outlook'] = """
    type: command
    short-summary: "Update the navigation property outlook in users"
    parameters:
      - name: --master-categories
        short-summary: "A list of categories defined for the user."
        long-summary: |
            Usage: --master-categories color=XX display-name=XX id=XX

            display-name: A unique name that identifies a category in the user's mailbox. After a category is created, \
the name cannot be changed. Read-only.
            id: Read-only.

            Multiple actions can be specified by using more than one --master-categories argument.
"""

helps['users update-photo'] = """
    type: command
    short-summary: "Update the navigation property photo in users"
"""

helps['users update-setting'] = """
    type: command
    short-summary: "Update the navigation property settings in users"
    parameters:
      - name: --shift-preferences-last-modified-by-application
        short-summary: "identity"
        long-summary: |
            Usage: --shift-preferences-last-modified-by-application display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --shift-preferences-last-modified-by-device
        short-summary: "identity"
        long-summary: |
            Usage: --shift-preferences-last-modified-by-device display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --shift-preferences-last-modified-by-user
        short-summary: "identity"
        long-summary: |
            Usage: --shift-preferences-last-modified-by-user display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
"""

helps['users'] = """
    type: group
    short-summary: users
"""

helps['users delete'] = """
    type: command
    short-summary: "Delete navigation property masterCategories for users"
"""

helps['users create-master-category'] = """
    type: command
    short-summary: "Create new navigation property to masterCategories for users"
"""

helps['users get-master-category'] = """
    type: command
    short-summary: "Get masterCategories from users"
"""

helps['users list-master-category'] = """
    type: command
    short-summary: "Get masterCategories from users"
"""

helps['users update-master-category'] = """
    type: command
    short-summary: "Update the navigation property masterCategories in users"
"""

helps['users'] = """
    type: group
    short-summary: users
"""

helps['users delete'] = """
    type: command
    short-summary: "Delete navigation property shiftPreferences for users"
"""

helps['users get-shift-preference'] = """
    type: command
    short-summary: "Get shiftPreferences from users"
"""

helps['users update-shift-preference'] = """
    type: command
    short-summary: "Update the navigation property shiftPreferences in users"
    parameters:
      - name: --last-modified-by-application
        short-summary: "identity"
        long-summary: |
            Usage: --last-modified-by-application display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --last-modified-by-device
        short-summary: "identity"
        long-summary: |
            Usage: --last-modified-by-device display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --last-modified-by-user
        short-summary: "identity"
        long-summary: |
            Usage: --last-modified-by-user display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
"""