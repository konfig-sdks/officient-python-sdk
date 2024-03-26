# coding: utf-8

"""
    Officient API

    Officient offers an intuitive HRIS which helps manage all personnel administration through our HR platform & personalized employee self-services. Manage payroll, company assets, contracts, days off, fleet, performance reviews and all employee data in one HR system. HR deserves great software and we're here to provide it.  We support our customers in transforming HR towards paperless administration and automating tedious workforce management tasks in the process. Our goal? Transform HR from an administrative, processing role, to a controlling role which fuels HR strategy across the organization.

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from officient_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from officient_python_sdk.api_response import AsyncGeneratorResponse
from officient_python_sdk import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from officient_python_sdk import schemas  # noqa: F401

from officient_python_sdk.model.budget_add_budget_item_response import BudgetAddBudgetItemResponse as BudgetAddBudgetItemResponseSchema
from officient_python_sdk.model.budget_add_budget_item_request import BudgetAddBudgetItemRequest as BudgetAddBudgetItemRequestSchema

from officient_python_sdk.type.budget_add_budget_item_response import BudgetAddBudgetItemResponse
from officient_python_sdk.type.budget_add_budget_item_request import BudgetAddBudgetItemRequest

from ...api_client import Dictionary
from officient_python_sdk.pydantic.budget_add_budget_item_request import BudgetAddBudgetItemRequest as BudgetAddBudgetItemRequestPydantic
from officient_python_sdk.pydantic.budget_add_budget_item_response import BudgetAddBudgetItemResponse as BudgetAddBudgetItemResponsePydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = BudgetAddBudgetItemRequestSchema


request_body_budget_add_budget_item_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
SchemaFor200ResponseBodyApplicationJson = BudgetAddBudgetItemResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: BudgetAddBudgetItemResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: BudgetAddBudgetItemResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationJson = schemas.DictSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _add_budget_item_mapped_args(
        self,
        budget_type: typing.Optional[str] = None,
        maximum: typing.Optional[int] = None,
        year: typing.Optional[int] = None,
        employee_id: typing.Optional[int] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if budget_type is not None:
            _body["budget_type"] = budget_type
        if maximum is not None:
            _body["maximum"] = maximum
        if year is not None:
            _body["year"] = year
        if employee_id is not None:
            _body["employee_id"] = employee_id
        args.body = _body
        return args

    async def _aadd_budget_item_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Add budget
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/1.0/budgets/add',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_budget_add_budget_item_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _add_budget_item_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Add budget
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/1.0/budgets/add',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_budget_add_budget_item_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class AddBudgetItemRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aadd_budget_item(
        self,
        budget_type: typing.Optional[str] = None,
        maximum: typing.Optional[int] = None,
        year: typing.Optional[int] = None,
        employee_id: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._add_budget_item_mapped_args(
            budget_type=budget_type,
            maximum=maximum,
            year=year,
            employee_id=employee_id,
        )
        return await self._aadd_budget_item_oapg(
            body=args.body,
            **kwargs,
        )
    
    def add_budget_item(
        self,
        budget_type: typing.Optional[str] = None,
        maximum: typing.Optional[int] = None,
        year: typing.Optional[int] = None,
        employee_id: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._add_budget_item_mapped_args(
            budget_type=budget_type,
            maximum=maximum,
            year=year,
            employee_id=employee_id,
        )
        return self._add_budget_item_oapg(
            body=args.body,
        )

class AddBudgetItem(BaseApi):

    async def aadd_budget_item(
        self,
        budget_type: typing.Optional[str] = None,
        maximum: typing.Optional[int] = None,
        year: typing.Optional[int] = None,
        employee_id: typing.Optional[int] = None,
        validate: bool = False,
        **kwargs,
    ) -> BudgetAddBudgetItemResponsePydantic:
        raw_response = await self.raw.aadd_budget_item(
            budget_type=budget_type,
            maximum=maximum,
            year=year,
            employee_id=employee_id,
            **kwargs,
        )
        if validate:
            return BudgetAddBudgetItemResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(BudgetAddBudgetItemResponsePydantic, raw_response.body)
    
    
    def add_budget_item(
        self,
        budget_type: typing.Optional[str] = None,
        maximum: typing.Optional[int] = None,
        year: typing.Optional[int] = None,
        employee_id: typing.Optional[int] = None,
        validate: bool = False,
    ) -> BudgetAddBudgetItemResponsePydantic:
        raw_response = self.raw.add_budget_item(
            budget_type=budget_type,
            maximum=maximum,
            year=year,
            employee_id=employee_id,
        )
        if validate:
            return BudgetAddBudgetItemResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(BudgetAddBudgetItemResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        budget_type: typing.Optional[str] = None,
        maximum: typing.Optional[int] = None,
        year: typing.Optional[int] = None,
        employee_id: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._add_budget_item_mapped_args(
            budget_type=budget_type,
            maximum=maximum,
            year=year,
            employee_id=employee_id,
        )
        return await self._aadd_budget_item_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        budget_type: typing.Optional[str] = None,
        maximum: typing.Optional[int] = None,
        year: typing.Optional[int] = None,
        employee_id: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._add_budget_item_mapped_args(
            budget_type=budget_type,
            maximum=maximum,
            year=year,
            employee_id=employee_id,
        )
        return self._add_budget_item_oapg(
            body=args.body,
        )

