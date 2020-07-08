# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional, TYPE_CHECKING

from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

from ._configuration_async import IdentityAccessReviewConfiguration
from .operations_async import AccessReviewDecisionAccessReviewDecisionOperations
from .operations_async import AccessReviewAccessReviewOperations
from .operations_async import AccessReviewOperations
from .operations_async import BusinessFlowTemplateBusinessFlowTemplateOperations
from .operations_async import ProgramControlProgramControlOperations
from .operations_async import ProgramControlOperations
from .operations_async import ProgramControlTypeProgramControlTypeOperations
from .operations_async import ProgramProgramOperations
from .operations_async import ProgramOperations
from .. import models


class IdentityAccessReview(object):
    """IdentityAccessReview.

    :ivar access_review_decision_access_review_decision: AccessReviewDecisionAccessReviewDecisionOperations operations
    :vartype access_review_decision_access_review_decision: identity_access_review.aio.operations_async.AccessReviewDecisionAccessReviewDecisionOperations
    :ivar access_review_access_review: AccessReviewAccessReviewOperations operations
    :vartype access_review_access_review: identity_access_review.aio.operations_async.AccessReviewAccessReviewOperations
    :ivar access_review: AccessReviewOperations operations
    :vartype access_review: identity_access_review.aio.operations_async.AccessReviewOperations
    :ivar business_flow_template_business_flow_template: BusinessFlowTemplateBusinessFlowTemplateOperations operations
    :vartype business_flow_template_business_flow_template: identity_access_review.aio.operations_async.BusinessFlowTemplateBusinessFlowTemplateOperations
    :ivar program_control_program_control: ProgramControlProgramControlOperations operations
    :vartype program_control_program_control: identity_access_review.aio.operations_async.ProgramControlProgramControlOperations
    :ivar program_control: ProgramControlOperations operations
    :vartype program_control: identity_access_review.aio.operations_async.ProgramControlOperations
    :ivar program_control_type_program_control_type: ProgramControlTypeProgramControlTypeOperations operations
    :vartype program_control_type_program_control_type: identity_access_review.aio.operations_async.ProgramControlTypeProgramControlTypeOperations
    :ivar program_program: ProgramProgramOperations operations
    :vartype program_program: identity_access_review.aio.operations_async.ProgramProgramOperations
    :ivar program: ProgramOperations operations
    :vartype program: identity_access_review.aio.operations_async.ProgramOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param top: Show only the first n items.
    :type top: int
    :param skip: Skip the first n items.
    :type skip: int
    :param search: Search items by search phrases.
    :type search: str
    :param filter: Filter items by property values.
    :type filter: str
    :param count: Include count of items.
    :type count: bool
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = 'https://graph.microsoft.com/beta'
        self._config = IdentityAccessReviewConfiguration(credential, top, skip, search, filter, count, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.access_review_decision_access_review_decision = AccessReviewDecisionAccessReviewDecisionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.access_review_access_review = AccessReviewAccessReviewOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.access_review = AccessReviewOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.business_flow_template_business_flow_template = BusinessFlowTemplateBusinessFlowTemplateOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.program_control_program_control = ProgramControlProgramControlOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.program_control = ProgramControlOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.program_control_type_program_control_type = ProgramControlTypeProgramControlTypeOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.program_program = ProgramProgramOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.program = ProgramOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "IdentityAccessReview":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
