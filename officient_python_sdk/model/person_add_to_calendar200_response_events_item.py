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


class PersonAddToCalendar200ResponseEventsItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            date = schemas.StrSchema
            start_time_minutes = schemas.IntSchema
            duration_minutes = schemas.IntSchema
            __annotations__ = {
                "date": date,
                "start_time_minutes": start_time_minutes,
                "duration_minutes": duration_minutes,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date"]) -> MetaOapg.properties.date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["start_time_minutes"]) -> MetaOapg.properties.start_time_minutes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["duration_minutes"]) -> MetaOapg.properties.duration_minutes: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["date", "start_time_minutes", "duration_minutes", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date"]) -> typing.Union[MetaOapg.properties.date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["start_time_minutes"]) -> typing.Union[MetaOapg.properties.start_time_minutes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["duration_minutes"]) -> typing.Union[MetaOapg.properties.duration_minutes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["date", "start_time_minutes", "duration_minutes", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        date: typing.Union[MetaOapg.properties.date, str, schemas.Unset] = schemas.unset,
        start_time_minutes: typing.Union[MetaOapg.properties.start_time_minutes, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        duration_minutes: typing.Union[MetaOapg.properties.duration_minutes, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PersonAddToCalendar200ResponseEventsItem':
        return super().__new__(
            cls,
            *args,
            date=date,
            start_time_minutes=start_time_minutes,
            duration_minutes=duration_minutes,
            _configuration=_configuration,
            **kwargs,
        )