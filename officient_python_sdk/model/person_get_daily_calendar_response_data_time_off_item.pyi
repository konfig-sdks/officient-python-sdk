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


class PersonGetDailyCalendarResponseDataTimeOffItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            date = schemas.StrSchema
            scheduled_minutes = schemas.IntSchema
        
            @staticmethod
            def events() -> typing.Type['PersonGetDailyCalendarResponseDataTimeOffItemEvents']:
                return PersonGetDailyCalendarResponseDataTimeOffItemEvents
            __annotations__ = {
                "date": date,
                "scheduled_minutes": scheduled_minutes,
                "events": events,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date"]) -> MetaOapg.properties.date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scheduled_minutes"]) -> MetaOapg.properties.scheduled_minutes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["events"]) -> 'PersonGetDailyCalendarResponseDataTimeOffItemEvents': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["date", "scheduled_minutes", "events", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date"]) -> typing.Union[MetaOapg.properties.date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scheduled_minutes"]) -> typing.Union[MetaOapg.properties.scheduled_minutes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["events"]) -> typing.Union['PersonGetDailyCalendarResponseDataTimeOffItemEvents', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["date", "scheduled_minutes", "events", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        date: typing.Union[MetaOapg.properties.date, str, schemas.Unset] = schemas.unset,
        scheduled_minutes: typing.Union[MetaOapg.properties.scheduled_minutes, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        events: typing.Union['PersonGetDailyCalendarResponseDataTimeOffItemEvents', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PersonGetDailyCalendarResponseDataTimeOffItem':
        return super().__new__(
            cls,
            *args,
            date=date,
            scheduled_minutes=scheduled_minutes,
            events=events,
            _configuration=_configuration,
            **kwargs,
        )

from officient_python_sdk.model.person_get_daily_calendar_response_data_time_off_item_events import PersonGetDailyCalendarResponseDataTimeOffItemEvents
