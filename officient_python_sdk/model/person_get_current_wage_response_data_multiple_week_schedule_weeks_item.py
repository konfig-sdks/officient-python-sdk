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


class PersonGetCurrentWageResponseDataMultipleWeekScheduleWeeksItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            week_nr = schemas.IntSchema
        
            @staticmethod
            def weekly_time_engagement_minutes() -> typing.Type['PersonGetCurrentWageResponseDataMultipleWeekScheduleWeeksItemWeeklyTimeEngagementMinutes']:
                return PersonGetCurrentWageResponseDataMultipleWeekScheduleWeeksItemWeeklyTimeEngagementMinutes
            __annotations__ = {
                "week_nr": week_nr,
                "weekly_time_engagement_minutes": weekly_time_engagement_minutes,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["week_nr"]) -> MetaOapg.properties.week_nr: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["weekly_time_engagement_minutes"]) -> 'PersonGetCurrentWageResponseDataMultipleWeekScheduleWeeksItemWeeklyTimeEngagementMinutes': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["week_nr", "weekly_time_engagement_minutes", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["week_nr"]) -> typing.Union[MetaOapg.properties.week_nr, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["weekly_time_engagement_minutes"]) -> typing.Union['PersonGetCurrentWageResponseDataMultipleWeekScheduleWeeksItemWeeklyTimeEngagementMinutes', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["week_nr", "weekly_time_engagement_minutes", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        week_nr: typing.Union[MetaOapg.properties.week_nr, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        weekly_time_engagement_minutes: typing.Union['PersonGetCurrentWageResponseDataMultipleWeekScheduleWeeksItemWeeklyTimeEngagementMinutes', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PersonGetCurrentWageResponseDataMultipleWeekScheduleWeeksItem':
        return super().__new__(
            cls,
            *args,
            week_nr=week_nr,
            weekly_time_engagement_minutes=weekly_time_engagement_minutes,
            _configuration=_configuration,
            **kwargs,
        )

from officient_python_sdk.model.person_get_current_wage_response_data_multiple_week_schedule_weeks_item_weekly_time_engagement_minutes import PersonGetCurrentWageResponseDataMultipleWeekScheduleWeeksItemWeeklyTimeEngagementMinutes
