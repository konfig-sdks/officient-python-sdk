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


class PersonGetMonthlyCalendarResponseData(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def time_off() -> typing.Type['PersonGetMonthlyCalendarResponseDataTimeOff']:
                return PersonGetMonthlyCalendarResponseDataTimeOff
        
            @staticmethod
            def company_days_off() -> typing.Type['PersonGetMonthlyCalendarResponseDataCompanyDaysOff']:
                return PersonGetMonthlyCalendarResponseDataCompanyDaysOff
            __annotations__ = {
                "time_off": time_off,
                "company_days_off": company_days_off,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["time_off"]) -> 'PersonGetMonthlyCalendarResponseDataTimeOff': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["company_days_off"]) -> 'PersonGetMonthlyCalendarResponseDataCompanyDaysOff': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["time_off", "company_days_off", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["time_off"]) -> typing.Union['PersonGetMonthlyCalendarResponseDataTimeOff', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["company_days_off"]) -> typing.Union['PersonGetMonthlyCalendarResponseDataCompanyDaysOff', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["time_off", "company_days_off", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        time_off: typing.Union['PersonGetMonthlyCalendarResponseDataTimeOff', schemas.Unset] = schemas.unset,
        company_days_off: typing.Union['PersonGetMonthlyCalendarResponseDataCompanyDaysOff', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PersonGetMonthlyCalendarResponseData':
        return super().__new__(
            cls,
            *args,
            time_off=time_off,
            company_days_off=company_days_off,
            _configuration=_configuration,
            **kwargs,
        )

from officient_python_sdk.model.person_get_monthly_calendar_response_data_company_days_off import PersonGetMonthlyCalendarResponseDataCompanyDaysOff
from officient_python_sdk.model.person_get_monthly_calendar_response_data_time_off import PersonGetMonthlyCalendarResponseDataTimeOff
