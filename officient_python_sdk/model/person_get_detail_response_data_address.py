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


class PersonGetDetailResponseDataAddress(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            line_1 = schemas.StrSchema
            line_2 = schemas.StrSchema
            zipcode = schemas.StrSchema
            city = schemas.StrSchema
            state = schemas.StrSchema
            country_code = schemas.StrSchema
            date_last_changed = schemas.StrSchema
            __annotations__ = {
                "line_1": line_1,
                "line_2": line_2,
                "zipcode": zipcode,
                "city": city,
                "state": state,
                "country_code": country_code,
                "date_last_changed": date_last_changed,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["line_1"]) -> MetaOapg.properties.line_1: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["line_2"]) -> MetaOapg.properties.line_2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["zipcode"]) -> MetaOapg.properties.zipcode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["city"]) -> MetaOapg.properties.city: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["state"]) -> MetaOapg.properties.state: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["country_code"]) -> MetaOapg.properties.country_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date_last_changed"]) -> MetaOapg.properties.date_last_changed: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["line_1", "line_2", "zipcode", "city", "state", "country_code", "date_last_changed", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["line_1"]) -> typing.Union[MetaOapg.properties.line_1, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["line_2"]) -> typing.Union[MetaOapg.properties.line_2, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["zipcode"]) -> typing.Union[MetaOapg.properties.zipcode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["city"]) -> typing.Union[MetaOapg.properties.city, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["state"]) -> typing.Union[MetaOapg.properties.state, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["country_code"]) -> typing.Union[MetaOapg.properties.country_code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date_last_changed"]) -> typing.Union[MetaOapg.properties.date_last_changed, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["line_1", "line_2", "zipcode", "city", "state", "country_code", "date_last_changed", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        line_1: typing.Union[MetaOapg.properties.line_1, str, schemas.Unset] = schemas.unset,
        line_2: typing.Union[MetaOapg.properties.line_2, str, schemas.Unset] = schemas.unset,
        zipcode: typing.Union[MetaOapg.properties.zipcode, str, schemas.Unset] = schemas.unset,
        city: typing.Union[MetaOapg.properties.city, str, schemas.Unset] = schemas.unset,
        state: typing.Union[MetaOapg.properties.state, str, schemas.Unset] = schemas.unset,
        country_code: typing.Union[MetaOapg.properties.country_code, str, schemas.Unset] = schemas.unset,
        date_last_changed: typing.Union[MetaOapg.properties.date_last_changed, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PersonGetDetailResponseDataAddress':
        return super().__new__(
            cls,
            *args,
            line_1=line_1,
            line_2=line_2,
            zipcode=zipcode,
            city=city,
            state=state,
            country_code=country_code,
            date_last_changed=date_last_changed,
            _configuration=_configuration,
            **kwargs,
        )
