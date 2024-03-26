# coding: utf-8

"""
    Officient API

    Officient offers an intuitive HRIS which helps manage all personnel administration through our HR platform & personalized employee self-services. Manage payroll, company assets, contracts, days off, fleet, performance reviews and all employee data in one HR system. HR deserves great software and we're here to provide it.  We support our customers in transforming HR towards paperless administration and automating tedious workforce management tasks in the process. Our goal? Transform HR from an administrative, processing role, to a controlling role which fuels HR strategy across the organization.

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

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


class ExpenseListByMonth400Response(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            status_code = schemas.IntSchema
            reason_phrase = schemas.StrSchema
            __annotations__ = {
                "status_code": status_code,
                "reason_phrase": reason_phrase,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status_code"]) -> MetaOapg.properties.status_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reason_phrase"]) -> MetaOapg.properties.reason_phrase: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["status_code", "reason_phrase", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status_code"]) -> typing.Union[MetaOapg.properties.status_code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reason_phrase"]) -> typing.Union[MetaOapg.properties.reason_phrase, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["status_code", "reason_phrase", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        status_code: typing.Union[MetaOapg.properties.status_code, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        reason_phrase: typing.Union[MetaOapg.properties.reason_phrase, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ExpenseListByMonth400Response':
        return super().__new__(
            cls,
            *args,
            status_code=status_code,
            reason_phrase=reason_phrase,
            _configuration=_configuration,
            **kwargs,
        )
