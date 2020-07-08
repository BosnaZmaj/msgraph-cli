# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import datetime
from typing import List, Optional, Union

from azure.core.exceptions import HttpResponseError
import msrest.serialization

from ._users_planner_enums import *


class CollectionOfPlannerBucket(msrest.serialization.Model):
    """Collection of plannerBucket.

    :param value:
    :type value: list[~users_planner.models.MicrosoftGraphPlannerBucket]
    :param odata_next_link:
    :type odata_next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[MicrosoftGraphPlannerBucket]'},
        'odata_next_link': {'key': '@odata\\.nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["MicrosoftGraphPlannerBucket"]] = None,
        odata_next_link: Optional[str] = None,
        **kwargs
    ):
        super(CollectionOfPlannerBucket, self).__init__(**kwargs)
        self.value = value
        self.odata_next_link = odata_next_link


class CollectionOfPlannerDelta(msrest.serialization.Model):
    """Collection of plannerDelta.

    :param value:
    :type value: list[~users_planner.models.MicrosoftGraphEntity]
    :param odata_next_link:
    :type odata_next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[MicrosoftGraphEntity]'},
        'odata_next_link': {'key': '@odata\\.nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["MicrosoftGraphEntity"]] = None,
        odata_next_link: Optional[str] = None,
        **kwargs
    ):
        super(CollectionOfPlannerDelta, self).__init__(**kwargs)
        self.value = value
        self.odata_next_link = odata_next_link


class CollectionOfPlannerPlan(msrest.serialization.Model):
    """Collection of plannerPlan.

    :param value:
    :type value: list[~users_planner.models.MicrosoftGraphPlannerPlan]
    :param odata_next_link:
    :type odata_next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[MicrosoftGraphPlannerPlan]'},
        'odata_next_link': {'key': '@odata\\.nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["MicrosoftGraphPlannerPlan"]] = None,
        odata_next_link: Optional[str] = None,
        **kwargs
    ):
        super(CollectionOfPlannerPlan, self).__init__(**kwargs)
        self.value = value
        self.odata_next_link = odata_next_link


class CollectionOfPlannerPlan0(msrest.serialization.Model):
    """Collection of plannerPlan.

    :param value:
    :type value: list[~users_planner.models.MicrosoftGraphPlannerPlan]
    :param odata_next_link:
    :type odata_next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[MicrosoftGraphPlannerPlan]'},
        'odata_next_link': {'key': '@odata\\.nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["MicrosoftGraphPlannerPlan"]] = None,
        odata_next_link: Optional[str] = None,
        **kwargs
    ):
        super(CollectionOfPlannerPlan0, self).__init__(**kwargs)
        self.value = value
        self.odata_next_link = odata_next_link


class CollectionOfPlannerPlan1(msrest.serialization.Model):
    """Collection of plannerPlan.

    :param value:
    :type value: list[~users_planner.models.MicrosoftGraphPlannerPlan]
    :param odata_next_link:
    :type odata_next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[MicrosoftGraphPlannerPlan]'},
        'odata_next_link': {'key': '@odata\\.nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["MicrosoftGraphPlannerPlan"]] = None,
        odata_next_link: Optional[str] = None,
        **kwargs
    ):
        super(CollectionOfPlannerPlan1, self).__init__(**kwargs)
        self.value = value
        self.odata_next_link = odata_next_link


class CollectionOfPlannerTask(msrest.serialization.Model):
    """Collection of plannerTask.

    :param value:
    :type value: list[~users_planner.models.MicrosoftGraphPlannerTask]
    :param odata_next_link:
    :type odata_next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[MicrosoftGraphPlannerTask]'},
        'odata_next_link': {'key': '@odata\\.nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["MicrosoftGraphPlannerTask"]] = None,
        odata_next_link: Optional[str] = None,
        **kwargs
    ):
        super(CollectionOfPlannerTask, self).__init__(**kwargs)
        self.value = value
        self.odata_next_link = odata_next_link


class CollectionOfPlannerTask0(msrest.serialization.Model):
    """Collection of plannerTask.

    :param value:
    :type value: list[~users_planner.models.MicrosoftGraphPlannerTask]
    :param odata_next_link:
    :type odata_next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[MicrosoftGraphPlannerTask]'},
        'odata_next_link': {'key': '@odata\\.nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["MicrosoftGraphPlannerTask"]] = None,
        odata_next_link: Optional[str] = None,
        **kwargs
    ):
        super(CollectionOfPlannerTask0, self).__init__(**kwargs)
        self.value = value
        self.odata_next_link = odata_next_link


class CollectionOfPlannerTask1(msrest.serialization.Model):
    """Collection of plannerTask.

    :param value:
    :type value: list[~users_planner.models.MicrosoftGraphPlannerTask]
    :param odata_next_link:
    :type odata_next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[MicrosoftGraphPlannerTask]'},
        'odata_next_link': {'key': '@odata\\.nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["MicrosoftGraphPlannerTask"]] = None,
        odata_next_link: Optional[str] = None,
        **kwargs
    ):
        super(CollectionOfPlannerTask1, self).__init__(**kwargs)
        self.value = value
        self.odata_next_link = odata_next_link


class MicrosoftGraphEntity(msrest.serialization.Model):
    """entity.

    :param id: Read-only.
    :type id: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        **kwargs
    ):
        super(MicrosoftGraphEntity, self).__init__(**kwargs)
        self.id = id


class MicrosoftGraphIdentity(msrest.serialization.Model):
    """identity.

    :param id: Unique identifier for the identity.
    :type id: str
    :param display_name: The identity's display name. Note that this may not always be available or
     up to date. For example, if a user changes their display name, the API may show the new value
     in a future response, but the items associated with the user won't show up as having changed
     when using delta.
    :type display_name: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        display_name: Optional[str] = None,
        **kwargs
    ):
        super(MicrosoftGraphIdentity, self).__init__(**kwargs)
        self.id = id
        self.display_name = display_name


class MicrosoftGraphIdentitySet(msrest.serialization.Model):
    """identitySet.

    :param application: identity.
    :type application: ~users_planner.models.MicrosoftGraphIdentity
    :param device: identity.
    :type device: ~users_planner.models.MicrosoftGraphIdentity
    :param user: identity.
    :type user: ~users_planner.models.MicrosoftGraphIdentity
    """

    _attribute_map = {
        'application': {'key': 'application', 'type': 'MicrosoftGraphIdentity'},
        'device': {'key': 'device', 'type': 'MicrosoftGraphIdentity'},
        'user': {'key': 'user', 'type': 'MicrosoftGraphIdentity'},
    }

    def __init__(
        self,
        *,
        application: Optional["MicrosoftGraphIdentity"] = None,
        device: Optional["MicrosoftGraphIdentity"] = None,
        user: Optional["MicrosoftGraphIdentity"] = None,
        **kwargs
    ):
        super(MicrosoftGraphIdentitySet, self).__init__(**kwargs)
        self.application = application
        self.device = device
        self.user = user


class MicrosoftGraphPlannerAssignedToTaskBoardTaskFormat(MicrosoftGraphEntity):
    """plannerAssignedToTaskBoardTaskFormat.

    :param id: Read-only.
    :type id: str
    :param unassigned_order_hint: Hint value used to order the task on the AssignedTo view of the
     Task Board when the task is not assigned to anyone, or if the orderHintsByAssignee dictionary
     does not provide an order hint for the user the task is assigned to. The format is defined as
     outlined here.
    :type unassigned_order_hint: str
    :param order_hints_by_assignee: Any object.
    :type order_hints_by_assignee: object
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'unassigned_order_hint': {'key': 'unassignedOrderHint', 'type': 'str'},
        'order_hints_by_assignee': {'key': 'orderHintsByAssignee', 'type': 'object'},
    }

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        unassigned_order_hint: Optional[str] = None,
        order_hints_by_assignee: Optional[object] = None,
        **kwargs
    ):
        super(MicrosoftGraphPlannerAssignedToTaskBoardTaskFormat, self).__init__(id=id, **kwargs)
        self.unassigned_order_hint = unassigned_order_hint
        self.order_hints_by_assignee = order_hints_by_assignee


class MicrosoftGraphPlannerBucket(MicrosoftGraphEntity):
    """plannerBucket.

    :param id: Read-only.
    :type id: str
    :param name: Name of the bucket.
    :type name: str
    :param plan_id: Plan ID to which the bucket belongs.
    :type plan_id: str
    :param order_hint: Hint used to order items of this type in a list view. The format is defined
     as outlined here.
    :type order_hint: str
    :param tasks: Read-only. Nullable. The collection of tasks in the bucket.
    :type tasks: list[~users_planner.models.MicrosoftGraphPlannerTask]
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'plan_id': {'key': 'planId', 'type': 'str'},
        'order_hint': {'key': 'orderHint', 'type': 'str'},
        'tasks': {'key': 'tasks', 'type': '[MicrosoftGraphPlannerTask]'},
    }

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        name: Optional[str] = None,
        plan_id: Optional[str] = None,
        order_hint: Optional[str] = None,
        tasks: Optional[List["MicrosoftGraphPlannerTask"]] = None,
        **kwargs
    ):
        super(MicrosoftGraphPlannerBucket, self).__init__(id=id, **kwargs)
        self.name = name
        self.plan_id = plan_id
        self.order_hint = order_hint
        self.tasks = tasks


class MicrosoftGraphPlannerBucketTaskBoardTaskFormat(MicrosoftGraphEntity):
    """plannerBucketTaskBoardTaskFormat.

    :param id: Read-only.
    :type id: str
    :param order_hint: Hint used to order tasks in the Bucket view of the Task Board. The format is
     defined as outlined here.
    :type order_hint: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'order_hint': {'key': 'orderHint', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        order_hint: Optional[str] = None,
        **kwargs
    ):
        super(MicrosoftGraphPlannerBucketTaskBoardTaskFormat, self).__init__(id=id, **kwargs)
        self.order_hint = order_hint


class MicrosoftGraphPlannerCategoryDescriptions(msrest.serialization.Model):
    """plannerCategoryDescriptions.

    :param category1: The label associated with Category 1.
    :type category1: str
    :param category2: The label associated with Category 2.
    :type category2: str
    :param category3: The label associated with Category 3.
    :type category3: str
    :param category4: The label associated with Category 4.
    :type category4: str
    :param category5: The label associated with Category 5.
    :type category5: str
    :param category6: The label associated with Category 6.
    :type category6: str
    """

    _attribute_map = {
        'category1': {'key': 'category1', 'type': 'str'},
        'category2': {'key': 'category2', 'type': 'str'},
        'category3': {'key': 'category3', 'type': 'str'},
        'category4': {'key': 'category4', 'type': 'str'},
        'category5': {'key': 'category5', 'type': 'str'},
        'category6': {'key': 'category6', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        category1: Optional[str] = None,
        category2: Optional[str] = None,
        category3: Optional[str] = None,
        category4: Optional[str] = None,
        category5: Optional[str] = None,
        category6: Optional[str] = None,
        **kwargs
    ):
        super(MicrosoftGraphPlannerCategoryDescriptions, self).__init__(**kwargs)
        self.category1 = category1
        self.category2 = category2
        self.category3 = category3
        self.category4 = category4
        self.category5 = category5
        self.category6 = category6


class MicrosoftGraphPlannerDelta(MicrosoftGraphEntity):
    """plannerDelta.

    :param id: Read-only.
    :type id: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        **kwargs
    ):
        super(MicrosoftGraphPlannerDelta, self).__init__(id=id, **kwargs)


class MicrosoftGraphPlannerPlan(MicrosoftGraphEntity):
    """plannerPlan.

    :param id: Read-only.
    :type id: str
    :param created_date_time: Read-only. Date and time at which the plan is created. The Timestamp
     type represents date and time information using ISO 8601 format and is always in UTC time. For
     example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'.
    :type created_date_time: ~datetime.datetime
    :param owner: ID of the Group that owns the plan. A valid group must exist before this field
     can be set. After it is set, this property can’t be updated.
    :type owner: str
    :param title: Required. Title of the plan.
    :type title: str
    :param contexts: Any object.
    :type contexts: object
    :param tasks: Read-only. Nullable. Collection of tasks in the plan.
    :type tasks: list[~users_planner.models.MicrosoftGraphPlannerTask]
    :param buckets: Read-only. Nullable. Collection of buckets in the plan.
    :type buckets: list[~users_planner.models.MicrosoftGraphPlannerBucket]
    :param id_details_id: Read-only.
    :type id_details_id: str
    :param shared_with: Any object.
    :type shared_with: object
    :param category_descriptions: plannerCategoryDescriptions.
    :type category_descriptions: ~users_planner.models.MicrosoftGraphPlannerCategoryDescriptions
    :param context_details: Any object.
    :type context_details: object
    :param application: identity.
    :type application: ~users_planner.models.MicrosoftGraphIdentity
    :param device: identity.
    :type device: ~users_planner.models.MicrosoftGraphIdentity
    :param user: identity.
    :type user: ~users_planner.models.MicrosoftGraphIdentity
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'created_date_time': {'key': 'createdDateTime', 'type': 'iso-8601'},
        'owner': {'key': 'owner', 'type': 'str'},
        'title': {'key': 'title', 'type': 'str'},
        'contexts': {'key': 'contexts', 'type': 'object'},
        'tasks': {'key': 'tasks', 'type': '[MicrosoftGraphPlannerTask]'},
        'buckets': {'key': 'buckets', 'type': '[MicrosoftGraphPlannerBucket]'},
        'id_details_id': {'key': 'details.id', 'type': 'str'},
        'shared_with': {'key': 'details.sharedWith', 'type': 'object'},
        'category_descriptions': {'key': 'details.categoryDescriptions', 'type': 'MicrosoftGraphPlannerCategoryDescriptions'},
        'context_details': {'key': 'details.contextDetails', 'type': 'object'},
        'application': {'key': 'createdBy.application', 'type': 'MicrosoftGraphIdentity'},
        'device': {'key': 'createdBy.device', 'type': 'MicrosoftGraphIdentity'},
        'user': {'key': 'createdBy.user', 'type': 'MicrosoftGraphIdentity'},
    }

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        created_date_time: Optional[datetime.datetime] = None,
        owner: Optional[str] = None,
        title: Optional[str] = None,
        contexts: Optional[object] = None,
        tasks: Optional[List["MicrosoftGraphPlannerTask"]] = None,
        buckets: Optional[List["MicrosoftGraphPlannerBucket"]] = None,
        id_details_id: Optional[str] = None,
        shared_with: Optional[object] = None,
        category_descriptions: Optional["MicrosoftGraphPlannerCategoryDescriptions"] = None,
        context_details: Optional[object] = None,
        application: Optional["MicrosoftGraphIdentity"] = None,
        device: Optional["MicrosoftGraphIdentity"] = None,
        user: Optional["MicrosoftGraphIdentity"] = None,
        **kwargs
    ):
        super(MicrosoftGraphPlannerPlan, self).__init__(id=id, **kwargs)
        self.created_date_time = created_date_time
        self.owner = owner
        self.title = title
        self.contexts = contexts
        self.tasks = tasks
        self.buckets = buckets
        self.id_details_id = id_details_id
        self.shared_with = shared_with
        self.category_descriptions = category_descriptions
        self.context_details = context_details
        self.application = application
        self.device = device
        self.user = user


class MicrosoftGraphPlannerPlanDetails(MicrosoftGraphEntity):
    """plannerPlanDetails.

    :param id: Read-only.
    :type id: str
    :param shared_with: Any object.
    :type shared_with: object
    :param category_descriptions: plannerCategoryDescriptions.
    :type category_descriptions: ~users_planner.models.MicrosoftGraphPlannerCategoryDescriptions
    :param context_details: Any object.
    :type context_details: object
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'shared_with': {'key': 'sharedWith', 'type': 'object'},
        'category_descriptions': {'key': 'categoryDescriptions', 'type': 'MicrosoftGraphPlannerCategoryDescriptions'},
        'context_details': {'key': 'contextDetails', 'type': 'object'},
    }

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        shared_with: Optional[object] = None,
        category_descriptions: Optional["MicrosoftGraphPlannerCategoryDescriptions"] = None,
        context_details: Optional[object] = None,
        **kwargs
    ):
        super(MicrosoftGraphPlannerPlanDetails, self).__init__(id=id, **kwargs)
        self.shared_with = shared_with
        self.category_descriptions = category_descriptions
        self.context_details = context_details


class MicrosoftGraphPlannerProgressTaskBoardTaskFormat(MicrosoftGraphEntity):
    """plannerProgressTaskBoardTaskFormat.

    :param id: Read-only.
    :type id: str
    :param order_hint: Hint value used to order the task on the Progress view of the Task Board.
     The format is defined as outlined here.
    :type order_hint: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'order_hint': {'key': 'orderHint', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        order_hint: Optional[str] = None,
        **kwargs
    ):
        super(MicrosoftGraphPlannerProgressTaskBoardTaskFormat, self).__init__(id=id, **kwargs)
        self.order_hint = order_hint


class MicrosoftGraphPlannerTask(MicrosoftGraphEntity):
    """plannerTask.

    :param id: Read-only.
    :type id: str
    :param created_by: identitySet.
    :type created_by: ~users_planner.models.MicrosoftGraphIdentitySet
    :param plan_id: Plan ID to which the task belongs.
    :type plan_id: str
    :param bucket_id: Bucket ID to which the task belongs. The bucket needs to be in the plan that
     the task is in. It is 28 characters long and case-sensitive. Format validation is done on the
     service.
    :type bucket_id: str
    :param title: Title of the task.
    :type title: str
    :param order_hint: Hint used to order items of this type in a list view. The format is defined
     as outlined here.
    :type order_hint: str
    :param assignee_priority: Hint used to order items of this type in a list view. The format is
     defined as outlined here.
    :type assignee_priority: str
    :param percent_complete: Percentage of task completion. When set to 100, the task is considered
     completed.
    :type percent_complete: int
    :param priority:
    :type priority: int
    :param start_date_time: Date and time at which the task starts. The Timestamp type represents
     date and time information using ISO 8601 format and is always in UTC time. For example,
     midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'.
    :type start_date_time: ~datetime.datetime
    :param created_date_time: Read-only. Date and time at which the task is created. The Timestamp
     type represents date and time information using ISO 8601 format and is always in UTC time. For
     example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'.
    :type created_date_time: ~datetime.datetime
    :param due_date_time: Date and time at which the task is due. The Timestamp type represents
     date and time information using ISO 8601 format and is always in UTC time. For example,
     midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'.
    :type due_date_time: ~datetime.datetime
    :param has_description: Read-only. Value is true if the details object of the task has a non-
     empty description and false otherwise.
    :type has_description: bool
    :param preview_type: plannerPreviewType. Possible values include: "automatic", "noPreview",
     "checklist", "description", "reference".
    :type preview_type: str or ~users_planner.models.MicrosoftGraphPlannerPreviewType
    :param completed_date_time: Read-only. Date and time at which the 'percentComplete' of the task
     is set to '100'. The Timestamp type represents date and time information using ISO 8601 format
     and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this:
     '2014-01-01T00:00:00Z'.
    :type completed_date_time: ~datetime.datetime
    :param completed_by: identitySet.
    :type completed_by: ~users_planner.models.MicrosoftGraphIdentitySet
    :param reference_count: Number of external references that exist on the task.
    :type reference_count: int
    :param checklist_item_count: Number of checklist items that are present on the task.
    :type checklist_item_count: int
    :param active_checklist_item_count: Number of checklist items with value set to false,
     representing incomplete items.
    :type active_checklist_item_count: int
    :param applied_categories: Any object.
    :type applied_categories: object
    :param assignments: Any object.
    :type assignments: object
    :param conversation_thread_id: Thread ID of the conversation on the task. This is the ID of the
     conversation thread object created in the group.
    :type conversation_thread_id: str
    :param details: plannerTaskDetails.
    :type details: ~users_planner.models.MicrosoftGraphPlannerTaskDetails
    :param assigned_to_task_board_format: plannerAssignedToTaskBoardTaskFormat.
    :type assigned_to_task_board_format:
     ~users_planner.models.MicrosoftGraphPlannerAssignedToTaskBoardTaskFormat
    :param progress_task_board_format: plannerProgressTaskBoardTaskFormat.
    :type progress_task_board_format:
     ~users_planner.models.MicrosoftGraphPlannerProgressTaskBoardTaskFormat
    :param bucket_task_board_format: plannerBucketTaskBoardTaskFormat.
    :type bucket_task_board_format:
     ~users_planner.models.MicrosoftGraphPlannerBucketTaskBoardTaskFormat
    """

    _validation = {
        'percent_complete': {'maximum': 2147483647, 'minimum': -2147483648},
        'priority': {'maximum': 2147483647, 'minimum': -2147483648},
        'reference_count': {'maximum': 2147483647, 'minimum': -2147483648},
        'checklist_item_count': {'maximum': 2147483647, 'minimum': -2147483648},
        'active_checklist_item_count': {'maximum': 2147483647, 'minimum': -2147483648},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'created_by': {'key': 'createdBy', 'type': 'MicrosoftGraphIdentitySet'},
        'plan_id': {'key': 'planId', 'type': 'str'},
        'bucket_id': {'key': 'bucketId', 'type': 'str'},
        'title': {'key': 'title', 'type': 'str'},
        'order_hint': {'key': 'orderHint', 'type': 'str'},
        'assignee_priority': {'key': 'assigneePriority', 'type': 'str'},
        'percent_complete': {'key': 'percentComplete', 'type': 'int'},
        'priority': {'key': 'priority', 'type': 'int'},
        'start_date_time': {'key': 'startDateTime', 'type': 'iso-8601'},
        'created_date_time': {'key': 'createdDateTime', 'type': 'iso-8601'},
        'due_date_time': {'key': 'dueDateTime', 'type': 'iso-8601'},
        'has_description': {'key': 'hasDescription', 'type': 'bool'},
        'preview_type': {'key': 'previewType', 'type': 'str'},
        'completed_date_time': {'key': 'completedDateTime', 'type': 'iso-8601'},
        'completed_by': {'key': 'completedBy', 'type': 'MicrosoftGraphIdentitySet'},
        'reference_count': {'key': 'referenceCount', 'type': 'int'},
        'checklist_item_count': {'key': 'checklistItemCount', 'type': 'int'},
        'active_checklist_item_count': {'key': 'activeChecklistItemCount', 'type': 'int'},
        'applied_categories': {'key': 'appliedCategories', 'type': 'object'},
        'assignments': {'key': 'assignments', 'type': 'object'},
        'conversation_thread_id': {'key': 'conversationThreadId', 'type': 'str'},
        'details': {'key': 'details', 'type': 'MicrosoftGraphPlannerTaskDetails'},
        'assigned_to_task_board_format': {'key': 'assignedToTaskBoardFormat', 'type': 'MicrosoftGraphPlannerAssignedToTaskBoardTaskFormat'},
        'progress_task_board_format': {'key': 'progressTaskBoardFormat', 'type': 'MicrosoftGraphPlannerProgressTaskBoardTaskFormat'},
        'bucket_task_board_format': {'key': 'bucketTaskBoardFormat', 'type': 'MicrosoftGraphPlannerBucketTaskBoardTaskFormat'},
    }

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        created_by: Optional["MicrosoftGraphIdentitySet"] = None,
        plan_id: Optional[str] = None,
        bucket_id: Optional[str] = None,
        title: Optional[str] = None,
        order_hint: Optional[str] = None,
        assignee_priority: Optional[str] = None,
        percent_complete: Optional[int] = None,
        priority: Optional[int] = None,
        start_date_time: Optional[datetime.datetime] = None,
        created_date_time: Optional[datetime.datetime] = None,
        due_date_time: Optional[datetime.datetime] = None,
        has_description: Optional[bool] = None,
        preview_type: Optional[Union[str, "MicrosoftGraphPlannerPreviewType"]] = None,
        completed_date_time: Optional[datetime.datetime] = None,
        completed_by: Optional["MicrosoftGraphIdentitySet"] = None,
        reference_count: Optional[int] = None,
        checklist_item_count: Optional[int] = None,
        active_checklist_item_count: Optional[int] = None,
        applied_categories: Optional[object] = None,
        assignments: Optional[object] = None,
        conversation_thread_id: Optional[str] = None,
        details: Optional["MicrosoftGraphPlannerTaskDetails"] = None,
        assigned_to_task_board_format: Optional["MicrosoftGraphPlannerAssignedToTaskBoardTaskFormat"] = None,
        progress_task_board_format: Optional["MicrosoftGraphPlannerProgressTaskBoardTaskFormat"] = None,
        bucket_task_board_format: Optional["MicrosoftGraphPlannerBucketTaskBoardTaskFormat"] = None,
        **kwargs
    ):
        super(MicrosoftGraphPlannerTask, self).__init__(id=id, **kwargs)
        self.created_by = created_by
        self.plan_id = plan_id
        self.bucket_id = bucket_id
        self.title = title
        self.order_hint = order_hint
        self.assignee_priority = assignee_priority
        self.percent_complete = percent_complete
        self.priority = priority
        self.start_date_time = start_date_time
        self.created_date_time = created_date_time
        self.due_date_time = due_date_time
        self.has_description = has_description
        self.preview_type = preview_type
        self.completed_date_time = completed_date_time
        self.completed_by = completed_by
        self.reference_count = reference_count
        self.checklist_item_count = checklist_item_count
        self.active_checklist_item_count = active_checklist_item_count
        self.applied_categories = applied_categories
        self.assignments = assignments
        self.conversation_thread_id = conversation_thread_id
        self.details = details
        self.assigned_to_task_board_format = assigned_to_task_board_format
        self.progress_task_board_format = progress_task_board_format
        self.bucket_task_board_format = bucket_task_board_format


class MicrosoftGraphPlannerTaskDetails(MicrosoftGraphEntity):
    """plannerTaskDetails.

    :param id: Read-only.
    :type id: str
    :param description: Description of the task.
    :type description: str
    :param preview_type: plannerPreviewType. Possible values include: "automatic", "noPreview",
     "checklist", "description", "reference".
    :type preview_type: str or ~users_planner.models.MicrosoftGraphPlannerPreviewType
    :param references: Any object.
    :type references: object
    :param checklist: Any object.
    :type checklist: object
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'preview_type': {'key': 'previewType', 'type': 'str'},
        'references': {'key': 'references', 'type': 'object'},
        'checklist': {'key': 'checklist', 'type': 'object'},
    }

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        description: Optional[str] = None,
        preview_type: Optional[Union[str, "MicrosoftGraphPlannerPreviewType"]] = None,
        references: Optional[object] = None,
        checklist: Optional[object] = None,
        **kwargs
    ):
        super(MicrosoftGraphPlannerTaskDetails, self).__init__(id=id, **kwargs)
        self.description = description
        self.preview_type = preview_type
        self.references = references
        self.checklist = checklist


class MicrosoftGraphPlannerUser(MicrosoftGraphEntity):
    """plannerUser.

    :param id: Read-only.
    :type id: str
    :param favorite_plan_references: Any object.
    :type favorite_plan_references: object
    :param recent_plan_references: Any object.
    :type recent_plan_references: object
    :param tasks: Read-only. Nullable. Returns the plannerPlans shared with the user.
    :type tasks: list[~users_planner.models.MicrosoftGraphPlannerTask]
    :param plans: Read-only. Nullable. Returns the plannerTasks assigned to the user.
    :type plans: list[~users_planner.models.MicrosoftGraphPlannerPlan]
    :param favorite_plans:
    :type favorite_plans: list[~users_planner.models.MicrosoftGraphPlannerPlan]
    :param recent_plans:
    :type recent_plans: list[~users_planner.models.MicrosoftGraphPlannerPlan]
    :param all:
    :type all: list[~users_planner.models.MicrosoftGraphEntity]
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'favorite_plan_references': {'key': 'favoritePlanReferences', 'type': 'object'},
        'recent_plan_references': {'key': 'recentPlanReferences', 'type': 'object'},
        'tasks': {'key': 'tasks', 'type': '[MicrosoftGraphPlannerTask]'},
        'plans': {'key': 'plans', 'type': '[MicrosoftGraphPlannerPlan]'},
        'favorite_plans': {'key': 'favoritePlans', 'type': '[MicrosoftGraphPlannerPlan]'},
        'recent_plans': {'key': 'recentPlans', 'type': '[MicrosoftGraphPlannerPlan]'},
        'all': {'key': 'all', 'type': '[MicrosoftGraphEntity]'},
    }

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        favorite_plan_references: Optional[object] = None,
        recent_plan_references: Optional[object] = None,
        tasks: Optional[List["MicrosoftGraphPlannerTask"]] = None,
        plans: Optional[List["MicrosoftGraphPlannerPlan"]] = None,
        favorite_plans: Optional[List["MicrosoftGraphPlannerPlan"]] = None,
        recent_plans: Optional[List["MicrosoftGraphPlannerPlan"]] = None,
        all: Optional[List["MicrosoftGraphEntity"]] = None,
        **kwargs
    ):
        super(MicrosoftGraphPlannerUser, self).__init__(id=id, **kwargs)
        self.favorite_plan_references = favorite_plan_references
        self.recent_plan_references = recent_plan_references
        self.tasks = tasks
        self.plans = plans
        self.favorite_plans = favorite_plans
        self.recent_plans = recent_plans
        self.all = all


class OdataError(msrest.serialization.Model):
    """OdataError.

    All required parameters must be populated in order to send to Azure.

    :param error: Required.
    :type error: ~users_planner.models.OdataErrorMain
    """

    _validation = {
        'error': {'required': True},
    }

    _attribute_map = {
        'error': {'key': 'error', 'type': 'OdataErrorMain'},
    }

    def __init__(
        self,
        *,
        error: "OdataErrorMain",
        **kwargs
    ):
        super(OdataError, self).__init__(**kwargs)
        self.error = error


class OdataErrorDetail(msrest.serialization.Model):
    """OdataErrorDetail.

    All required parameters must be populated in order to send to Azure.

    :param code: Required.
    :type code: str
    :param message: Required.
    :type message: str
    :param target:
    :type target: str
    """

    _validation = {
        'code': {'required': True},
        'message': {'required': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        code: str,
        message: str,
        target: Optional[str] = None,
        **kwargs
    ):
        super(OdataErrorDetail, self).__init__(**kwargs)
        self.code = code
        self.message = message
        self.target = target


class OdataErrorMain(msrest.serialization.Model):
    """OdataErrorMain.

    All required parameters must be populated in order to send to Azure.

    :param code: Required.
    :type code: str
    :param message: Required.
    :type message: str
    :param target:
    :type target: str
    :param details:
    :type details: list[~users_planner.models.OdataErrorDetail]
    :param innererror: The structure of this object is service-specific.
    :type innererror: object
    """

    _validation = {
        'code': {'required': True},
        'message': {'required': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'details': {'key': 'details', 'type': '[OdataErrorDetail]'},
        'innererror': {'key': 'innererror', 'type': 'object'},
    }

    def __init__(
        self,
        *,
        code: str,
        message: str,
        target: Optional[str] = None,
        details: Optional[List["OdataErrorDetail"]] = None,
        innererror: Optional[object] = None,
        **kwargs
    ):
        super(OdataErrorMain, self).__init__(**kwargs)
        self.code = code
        self.message = message
        self.target = target
        self.details = details
        self.innererror = innererror
