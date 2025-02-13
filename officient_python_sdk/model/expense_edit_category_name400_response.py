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


class ExpenseEditCategoryName400Response(
    schemas.ComposedSchema,
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        
        class one_of_0(
            schemas.DictSchema
        ):
        
        
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
            ) -> 'one_of_0':
                return super().__new__(
                    cls,
                    *args,
                    status_code=status_code,
                    reason_phrase=reason_phrase,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        
        class one_of_1(
            schemas.DictSchema
        ):
        
        
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
            ) -> 'one_of_1':
                return super().__new__(
                    cls,
                    *args,
                    status_code=status_code,
                    reason_phrase=reason_phrase,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        @classmethod
        @functools.lru_cache()
        def one_of(cls):
            # we need this here to make our import statements work
            # we must store _composed_schemas in here so the code is only run
            # when we invoke this method. If we kept this at the class
            # level we would get an error because the class level
            # code would be run when this module is imported, and these composed
            # classes don't exist yet because their module has not finished
            # loading
            return [
                cls.one_of_0,
                cls.one_of_1,
            ]


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ExpenseEditCategoryName400Response':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )
