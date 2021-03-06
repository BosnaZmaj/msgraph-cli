# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import datetime
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar, Union

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class FinancialCompanyPurchaseInvoicePurchaseInvoiceLineOperations(object):
    """FinancialCompanyPurchaseInvoicePurchaseInvoiceLineOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~financials.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def get_account(
        self,
        company_id,  # type: str
        purchase_invoice_id,  # type: str
        purchase_invoice_line_id,  # type: str
        select=None,  # type: Optional[List[Union[str, "models.Enum157"]]]
        expand=None,  # type: Optional[List[str]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphAccount"
        """Get account from financials.

        Get account from financials.

        :param company_id: key: id of company.
        :type company_id: str
        :param purchase_invoice_id: key: id of purchaseInvoice.
        :type purchase_invoice_id: str
        :param purchase_invoice_line_id: key: id of purchaseInvoiceLine.
        :type purchase_invoice_line_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~financials.models.Enum157]
        :param expand: Expand related entities.
        :type expand: list[str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphAccount, or the result of cls(response)
        :rtype: ~financials.models.MicrosoftGraphAccount
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphAccount"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_account.metadata['url']  # type: ignore
        path_format_arguments = {
            'company-id': self._serialize.url("company_id", company_id, 'str'),
            'purchaseInvoice-id': self._serialize.url("purchase_invoice_id", purchase_invoice_id, 'str'),
            'purchaseInvoiceLine-id': self._serialize.url("purchase_invoice_line_id", purchase_invoice_line_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if select is not None:
            query_parameters['$select'] = self._serialize.query("select", select, '[str]', div=',')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query("expand", expand, '[str]', div=',')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')
        header_parameters['Accept'] = 'application/json'

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphAccount', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_account.metadata = {'url': '/financials/companies/{company-id}/purchaseInvoices/{purchaseInvoice-id}/purchaseInvoiceLines/{purchaseInvoiceLine-id}/account'}  # type: ignore

    def update_account(
        self,
        company_id,  # type: str
        purchase_invoice_id,  # type: str
        purchase_invoice_line_id,  # type: str
        id=None,  # type: Optional[str]
        blocked=None,  # type: Optional[bool]
        category=None,  # type: Optional[str]
        display_name=None,  # type: Optional[str]
        last_modified_date_time=None,  # type: Optional[datetime.datetime]
        number=None,  # type: Optional[str]
        sub_category=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Update the navigation property account in financials.

        Update the navigation property account in financials.

        :param company_id: key: id of company.
        :type company_id: str
        :param purchase_invoice_id: key: id of purchaseInvoice.
        :type purchase_invoice_id: str
        :param purchase_invoice_line_id: key: id of purchaseInvoiceLine.
        :type purchase_invoice_line_id: str
        :param id: Read-only.
        :type id: str
        :param blocked:
        :type blocked: bool
        :param category:
        :type category: str
        :param display_name:
        :type display_name: str
        :param last_modified_date_time:
        :type last_modified_date_time: ~datetime.datetime
        :param number:
        :type number: str
        :param sub_category:
        :type sub_category: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.MicrosoftGraphAccount(id=id, blocked=blocked, category=category, display_name=display_name, last_modified_date_time=last_modified_date_time, number=number, sub_category=sub_category)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.update_account.metadata['url']  # type: ignore
        path_format_arguments = {
            'company-id': self._serialize.url("company_id", company_id, 'str'),
            'purchaseInvoice-id': self._serialize.url("purchase_invoice_id", purchase_invoice_id, 'str'),
            'purchaseInvoiceLine-id': self._serialize.url("purchase_invoice_line_id", purchase_invoice_line_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'MicrosoftGraphAccount')
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    update_account.metadata = {'url': '/financials/companies/{company-id}/purchaseInvoices/{purchaseInvoice-id}/purchaseInvoiceLines/{purchaseInvoiceLine-id}/account'}  # type: ignore

    def delete_account(
        self,
        company_id,  # type: str
        purchase_invoice_id,  # type: str
        purchase_invoice_line_id,  # type: str
        if_match=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Delete navigation property account for financials.

        Delete navigation property account for financials.

        :param company_id: key: id of company.
        :type company_id: str
        :param purchase_invoice_id: key: id of purchaseInvoice.
        :type purchase_invoice_id: str
        :param purchase_invoice_line_id: key: id of purchaseInvoiceLine.
        :type purchase_invoice_line_id: str
        :param if_match: ETag.
        :type if_match: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.delete_account.metadata['url']  # type: ignore
        path_format_arguments = {
            'company-id': self._serialize.url("company_id", company_id, 'str'),
            'purchaseInvoice-id': self._serialize.url("purchase_invoice_id", purchase_invoice_id, 'str'),
            'purchaseInvoiceLine-id': self._serialize.url("purchase_invoice_line_id", purchase_invoice_line_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if if_match is not None:
            header_parameters['If-Match'] = self._serialize.header("if_match", if_match, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete_account.metadata = {'url': '/financials/companies/{company-id}/purchaseInvoices/{purchaseInvoice-id}/purchaseInvoiceLines/{purchaseInvoiceLine-id}/account'}  # type: ignore

    def get_item(
        self,
        company_id,  # type: str
        purchase_invoice_id,  # type: str
        purchase_invoice_line_id,  # type: str
        select=None,  # type: Optional[List[Union[str, "models.Enum158"]]]
        expand=None,  # type: Optional[List[Union[str, "models.Enum159"]]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphItem"
        """Get item from financials.

        Get item from financials.

        :param company_id: key: id of company.
        :type company_id: str
        :param purchase_invoice_id: key: id of purchaseInvoice.
        :type purchase_invoice_id: str
        :param purchase_invoice_line_id: key: id of purchaseInvoiceLine.
        :type purchase_invoice_line_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~financials.models.Enum158]
        :param expand: Expand related entities.
        :type expand: list[str or ~financials.models.Enum159]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphItem, or the result of cls(response)
        :rtype: ~financials.models.MicrosoftGraphItem
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphItem"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_item.metadata['url']  # type: ignore
        path_format_arguments = {
            'company-id': self._serialize.url("company_id", company_id, 'str'),
            'purchaseInvoice-id': self._serialize.url("purchase_invoice_id", purchase_invoice_id, 'str'),
            'purchaseInvoiceLine-id': self._serialize.url("purchase_invoice_line_id", purchase_invoice_line_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if select is not None:
            query_parameters['$select'] = self._serialize.query("select", select, '[str]', div=',')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query("expand", expand, '[str]', div=',')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')
        header_parameters['Accept'] = 'application/json'

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphItem', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_item.metadata = {'url': '/financials/companies/{company-id}/purchaseInvoices/{purchaseInvoice-id}/purchaseInvoiceLines/{purchaseInvoiceLine-id}/item'}  # type: ignore

    def update_item(
        self,
        company_id,  # type: str
        purchase_invoice_id,  # type: str
        purchase_invoice_line_id,  # type: str
        id=None,  # type: Optional[str]
        base_unit_of_measure_id=None,  # type: Optional[str]
        blocked=None,  # type: Optional[bool]
        display_name=None,  # type: Optional[str]
        gtin=None,  # type: Optional[str]
        inventory=None,  # type: Optional[float]
        item_category_code=None,  # type: Optional[str]
        item_category_id=None,  # type: Optional[str]
        last_modified_date_time=None,  # type: Optional[datetime.datetime]
        number=None,  # type: Optional[str]
        price_includes_tax=None,  # type: Optional[bool]
        tax_group_code=None,  # type: Optional[str]
        tax_group_id=None,  # type: Optional[str]
        type=None,  # type: Optional[str]
        unit_cost=None,  # type: Optional[float]
        unit_price=None,  # type: Optional[float]
        item_category=None,  # type: Optional["models.MicrosoftGraphItemCategory"]
        picture=None,  # type: Optional[List["models.MicrosoftGraphPicture"]]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Update the navigation property item in financials.

        Update the navigation property item in financials.

        :param company_id: key: id of company.
        :type company_id: str
        :param purchase_invoice_id: key: id of purchaseInvoice.
        :type purchase_invoice_id: str
        :param purchase_invoice_line_id: key: id of purchaseInvoiceLine.
        :type purchase_invoice_line_id: str
        :param id: Read-only.
        :type id: str
        :param base_unit_of_measure_id:
        :type base_unit_of_measure_id: str
        :param blocked:
        :type blocked: bool
        :param display_name:
        :type display_name: str
        :param gtin:
        :type gtin: str
        :param inventory:
        :type inventory: float
        :param item_category_code:
        :type item_category_code: str
        :param item_category_id:
        :type item_category_id: str
        :param last_modified_date_time:
        :type last_modified_date_time: ~datetime.datetime
        :param number:
        :type number: str
        :param price_includes_tax:
        :type price_includes_tax: bool
        :param tax_group_code:
        :type tax_group_code: str
        :param tax_group_id:
        :type tax_group_id: str
        :param type:
        :type type: str
        :param unit_cost:
        :type unit_cost: float
        :param unit_price:
        :type unit_price: float
        :param item_category: itemCategory.
        :type item_category: ~financials.models.MicrosoftGraphItemCategory
        :param picture:
        :type picture: list[~financials.models.MicrosoftGraphPicture]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.MicrosoftGraphItem(id=id, base_unit_of_measure_id=base_unit_of_measure_id, blocked=blocked, display_name=display_name, gtin=gtin, inventory=inventory, item_category_code=item_category_code, item_category_id=item_category_id, last_modified_date_time=last_modified_date_time, number=number, price_includes_tax=price_includes_tax, tax_group_code=tax_group_code, tax_group_id=tax_group_id, type=type, unit_cost=unit_cost, unit_price=unit_price, item_category=item_category, picture=picture)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.update_item.metadata['url']  # type: ignore
        path_format_arguments = {
            'company-id': self._serialize.url("company_id", company_id, 'str'),
            'purchaseInvoice-id': self._serialize.url("purchase_invoice_id", purchase_invoice_id, 'str'),
            'purchaseInvoiceLine-id': self._serialize.url("purchase_invoice_line_id", purchase_invoice_line_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'MicrosoftGraphItem')
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    update_item.metadata = {'url': '/financials/companies/{company-id}/purchaseInvoices/{purchaseInvoice-id}/purchaseInvoiceLines/{purchaseInvoiceLine-id}/item'}  # type: ignore

    def delete_item(
        self,
        company_id,  # type: str
        purchase_invoice_id,  # type: str
        purchase_invoice_line_id,  # type: str
        if_match=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Delete navigation property item for financials.

        Delete navigation property item for financials.

        :param company_id: key: id of company.
        :type company_id: str
        :param purchase_invoice_id: key: id of purchaseInvoice.
        :type purchase_invoice_id: str
        :param purchase_invoice_line_id: key: id of purchaseInvoiceLine.
        :type purchase_invoice_line_id: str
        :param if_match: ETag.
        :type if_match: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.delete_item.metadata['url']  # type: ignore
        path_format_arguments = {
            'company-id': self._serialize.url("company_id", company_id, 'str'),
            'purchaseInvoice-id': self._serialize.url("purchase_invoice_id", purchase_invoice_id, 'str'),
            'purchaseInvoiceLine-id': self._serialize.url("purchase_invoice_line_id", purchase_invoice_line_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if if_match is not None:
            header_parameters['If-Match'] = self._serialize.header("if_match", if_match, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete_item.metadata = {'url': '/financials/companies/{company-id}/purchaseInvoices/{purchaseInvoice-id}/purchaseInvoiceLines/{purchaseInvoiceLine-id}/item'}  # type: ignore
