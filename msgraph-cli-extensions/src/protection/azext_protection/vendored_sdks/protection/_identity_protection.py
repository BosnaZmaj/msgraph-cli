# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING

from azure.mgmt.core import ARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

    from azure.core.credentials import TokenCredential

from ._configuration import IdentityProtectionConfiguration
from .operations import AnonymouIpRiskEventAnonymouIpRiskEventOperations
from .operations import IdentityRiskEventIdentityRiskEventOperations
from .operations import IdentityRiskEventOperations
from .operations import ImpossibleTravelRiskEventImpossibleTravelRiskEventOperations
from .operations import LeakedCredentialsRiskEventLeakedCredentialsRiskEventOperations
from .operations import MalwareRiskEventMalwareRiskEventOperations
from .operations import RiskDetectionRiskDetectionOperations
from .operations import RiskyUserRiskyUserOperations
from .operations import RiskyUserOperations
from .operations import SuspiciouIpRiskEventSuspiciouIpRiskEventOperations
from .operations import UnfamiliarLocationRiskEventUnfamiliarLocationRiskEventOperations
from . import models


class IdentityProtection(object):
    """IdentityProtection.

    :ivar anonymou_ip_risk_event_anonymou_ip_risk_event: AnonymouIpRiskEventAnonymouIpRiskEventOperations operations
    :vartype anonymou_ip_risk_event_anonymou_ip_risk_event: identity_protection.operations.AnonymouIpRiskEventAnonymouIpRiskEventOperations
    :ivar identity_risk_event_identity_risk_event: IdentityRiskEventIdentityRiskEventOperations operations
    :vartype identity_risk_event_identity_risk_event: identity_protection.operations.IdentityRiskEventIdentityRiskEventOperations
    :ivar identity_risk_event: IdentityRiskEventOperations operations
    :vartype identity_risk_event: identity_protection.operations.IdentityRiskEventOperations
    :ivar impossible_travel_risk_event_impossible_travel_risk_event: ImpossibleTravelRiskEventImpossibleTravelRiskEventOperations operations
    :vartype impossible_travel_risk_event_impossible_travel_risk_event: identity_protection.operations.ImpossibleTravelRiskEventImpossibleTravelRiskEventOperations
    :ivar leaked_credentials_risk_event_leaked_credentials_risk_event: LeakedCredentialsRiskEventLeakedCredentialsRiskEventOperations operations
    :vartype leaked_credentials_risk_event_leaked_credentials_risk_event: identity_protection.operations.LeakedCredentialsRiskEventLeakedCredentialsRiskEventOperations
    :ivar malware_risk_event_malware_risk_event: MalwareRiskEventMalwareRiskEventOperations operations
    :vartype malware_risk_event_malware_risk_event: identity_protection.operations.MalwareRiskEventMalwareRiskEventOperations
    :ivar risk_detection_risk_detection: RiskDetectionRiskDetectionOperations operations
    :vartype risk_detection_risk_detection: identity_protection.operations.RiskDetectionRiskDetectionOperations
    :ivar risky_user_risky_user: RiskyUserRiskyUserOperations operations
    :vartype risky_user_risky_user: identity_protection.operations.RiskyUserRiskyUserOperations
    :ivar risky_user: RiskyUserOperations operations
    :vartype risky_user: identity_protection.operations.RiskyUserOperations
    :ivar suspiciou_ip_risk_event_suspiciou_ip_risk_event: SuspiciouIpRiskEventSuspiciouIpRiskEventOperations operations
    :vartype suspiciou_ip_risk_event_suspiciou_ip_risk_event: identity_protection.operations.SuspiciouIpRiskEventSuspiciouIpRiskEventOperations
    :ivar unfamiliar_location_risk_event_unfamiliar_location_risk_event: UnfamiliarLocationRiskEventUnfamiliarLocationRiskEventOperations operations
    :vartype unfamiliar_location_risk_event_unfamiliar_location_risk_event: identity_protection.operations.UnfamiliarLocationRiskEventUnfamiliarLocationRiskEventOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
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
        credential,  # type: "TokenCredential"
        top=None,  # type: Optional[int]
        skip=None,  # type: Optional[int]
        search=None,  # type: Optional[str]
        filter=None,  # type: Optional[str]
        count=None,  # type: Optional[bool]
        base_url=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        if not base_url:
            base_url = 'https://graph.microsoft.com/beta'
        self._config = IdentityProtectionConfiguration(credential, top, skip, search, filter, count, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.anonymou_ip_risk_event_anonymou_ip_risk_event = AnonymouIpRiskEventAnonymouIpRiskEventOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.identity_risk_event_identity_risk_event = IdentityRiskEventIdentityRiskEventOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.identity_risk_event = IdentityRiskEventOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.impossible_travel_risk_event_impossible_travel_risk_event = ImpossibleTravelRiskEventImpossibleTravelRiskEventOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.leaked_credentials_risk_event_leaked_credentials_risk_event = LeakedCredentialsRiskEventLeakedCredentialsRiskEventOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.malware_risk_event_malware_risk_event = MalwareRiskEventMalwareRiskEventOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.risk_detection_risk_detection = RiskDetectionRiskDetectionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.risky_user_risky_user = RiskyUserRiskyUserOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.risky_user = RiskyUserOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.suspiciou_ip_risk_event_suspiciou_ip_risk_event = SuspiciouIpRiskEventSuspiciouIpRiskEventOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.unfamiliar_location_risk_event_unfamiliar_location_risk_event = UnfamiliarLocationRiskEventUnfamiliarLocationRiskEventOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> IdentityProtection
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
