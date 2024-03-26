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


class ExpenseAddCategoryRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "name",
            "type",
        }
        
        class properties:
            name = schemas.StrSchema
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "total": "TOTAL",
                        "kilometer-allowance": "KILOMETERALLOWANCE",
                        "day-allowance": "DAYALLOWANCE",
                    }
                
                @schemas.classproperty
                def TOTAL(cls):
                    return cls("total")
                
                @schemas.classproperty
                def KILOMETERALLOWANCE(cls):
                    return cls("kilometer-allowance")
                
                @schemas.classproperty
                def DAYALLOWANCE(cls):
                    return cls("day-allowance")
            price_per_kilometer = schemas.Float32Schema
            price_per_day = schemas.Float32Schema
            __annotations__ = {
                "name": name,
                "type": type,
                "price-per-kilometer": price_per_kilometer,
                "price-per-day": price_per_day,
            }
    
    name: MetaOapg.properties.name
    type: MetaOapg.properties.type
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["price-per-kilometer"]) -> MetaOapg.properties.price_per_kilometer: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["price-per-day"]) -> MetaOapg.properties.price_per_day: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "type", "price-per-kilometer", "price-per-day", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["price-per-kilometer"]) -> typing.Union[MetaOapg.properties.price_per_kilometer, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["price-per-day"]) -> typing.Union[MetaOapg.properties.price_per_day, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "type", "price-per-kilometer", "price-per-day", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ExpenseAddCategoryRequest':
        return super().__new__(
            cls,
            *args,
            name=name,
            type=type,
            _configuration=_configuration,
            **kwargs,
        )