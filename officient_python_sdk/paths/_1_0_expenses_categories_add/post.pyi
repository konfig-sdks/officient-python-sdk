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

from officient_python_sdk.model.expense_add_category_response import ExpenseAddCategoryResponse as ExpenseAddCategoryResponseSchema
from officient_python_sdk.model.expense_add_category_request import ExpenseAddCategoryRequest as ExpenseAddCategoryRequestSchema
from officient_python_sdk.model.expense_add_category400_response import ExpenseAddCategory400Response as ExpenseAddCategory400ResponseSchema

from officient_python_sdk.type.expense_add_category_request import ExpenseAddCategoryRequest
from officient_python_sdk.type.expense_add_category400_response import ExpenseAddCategory400Response
from officient_python_sdk.type.expense_add_category_response import ExpenseAddCategoryResponse

from ...api_client import Dictionary
from officient_python_sdk.pydantic.expense_add_category_response import ExpenseAddCategoryResponse as ExpenseAddCategoryResponsePydantic
from officient_python_sdk.pydantic.expense_add_category400_response import ExpenseAddCategory400Response as ExpenseAddCategory400ResponsePydantic
from officient_python_sdk.pydantic.expense_add_category_request import ExpenseAddCategoryRequest as ExpenseAddCategoryRequestPydantic

# body param
SchemaForRequestBodyApplicationJson = ExpenseAddCategoryRequestSchema


request_body_expense_add_category_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
SchemaFor200ResponseBodyApplicationJson = ExpenseAddCategoryResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: ExpenseAddCategoryResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: ExpenseAddCategoryResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationJson = ExpenseAddCategory400ResponseSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: ExpenseAddCategory400Response


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: ExpenseAddCategory400Response


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _add_category_mapped_args(
        self,
        name: str,
        type: str,
        price_per_kilometer: typing.Optional[typing.Union[int, float]] = None,
        price_per_day: typing.Optional[typing.Union[int, float]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if name is not None:
            _body["name"] = name
        if type is not None:
            _body["type"] = type
        if price_per_kilometer is not None:
            _body["price-per-kilometer"] = price_per_kilometer
        if price_per_day is not None:
            _body["price-per-day"] = price_per_day
        args.body = _body
        return args

    async def _aadd_category_oapg(
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
        Add expense category
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
            path_template='/1.0/expenses/categories/add',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_expense_add_category_request.serialize(body, content_type)
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


    def _add_category_oapg(
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
        Add expense category
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
            path_template='/1.0/expenses/categories/add',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_expense_add_category_request.serialize(body, content_type)
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


class AddCategoryRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aadd_category(
        self,
        name: str,
        type: str,
        price_per_kilometer: typing.Optional[typing.Union[int, float]] = None,
        price_per_day: typing.Optional[typing.Union[int, float]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._add_category_mapped_args(
            name=name,
            type=type,
            price_per_kilometer=price_per_kilometer,
            price_per_day=price_per_day,
        )
        return await self._aadd_category_oapg(
            body=args.body,
            **kwargs,
        )
    
    def add_category(
        self,
        name: str,
        type: str,
        price_per_kilometer: typing.Optional[typing.Union[int, float]] = None,
        price_per_day: typing.Optional[typing.Union[int, float]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._add_category_mapped_args(
            name=name,
            type=type,
            price_per_kilometer=price_per_kilometer,
            price_per_day=price_per_day,
        )
        return self._add_category_oapg(
            body=args.body,
        )

class AddCategory(BaseApi):

    async def aadd_category(
        self,
        name: str,
        type: str,
        price_per_kilometer: typing.Optional[typing.Union[int, float]] = None,
        price_per_day: typing.Optional[typing.Union[int, float]] = None,
        validate: bool = False,
        **kwargs,
    ) -> ExpenseAddCategoryResponsePydantic:
        raw_response = await self.raw.aadd_category(
            name=name,
            type=type,
            price_per_kilometer=price_per_kilometer,
            price_per_day=price_per_day,
            **kwargs,
        )
        if validate:
            return ExpenseAddCategoryResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ExpenseAddCategoryResponsePydantic, raw_response.body)
    
    
    def add_category(
        self,
        name: str,
        type: str,
        price_per_kilometer: typing.Optional[typing.Union[int, float]] = None,
        price_per_day: typing.Optional[typing.Union[int, float]] = None,
        validate: bool = False,
    ) -> ExpenseAddCategoryResponsePydantic:
        raw_response = self.raw.add_category(
            name=name,
            type=type,
            price_per_kilometer=price_per_kilometer,
            price_per_day=price_per_day,
        )
        if validate:
            return ExpenseAddCategoryResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ExpenseAddCategoryResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        name: str,
        type: str,
        price_per_kilometer: typing.Optional[typing.Union[int, float]] = None,
        price_per_day: typing.Optional[typing.Union[int, float]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._add_category_mapped_args(
            name=name,
            type=type,
            price_per_kilometer=price_per_kilometer,
            price_per_day=price_per_day,
        )
        return await self._aadd_category_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        name: str,
        type: str,
        price_per_kilometer: typing.Optional[typing.Union[int, float]] = None,
        price_per_day: typing.Optional[typing.Union[int, float]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._add_category_mapped_args(
            name=name,
            type=type,
            price_per_kilometer=price_per_kilometer,
            price_per_day=price_per_day,
        )
        return self._add_category_oapg(
            body=args.body,
        )

