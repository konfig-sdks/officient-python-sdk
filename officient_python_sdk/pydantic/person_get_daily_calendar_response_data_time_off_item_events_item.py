# coding: utf-8

"""
    Officient API

    Officient offers an intuitive HRIS which helps manage all personnel administration through our HR platform & personalized employee self-services. Manage payroll, company assets, contracts, days off, fleet, performance reviews and all employee data in one HR system. HR deserves great software and we're here to provide it.  We support our customers in transforming HR towards paperless administration and automating tedious workforce management tasks in the process. Our goal? Transform HR from an administrative, processing role, to a controlling role which fuels HR strategy across the organization.

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel, ConfigDict


class PersonGetDailyCalendarResponseDataTimeOffItemEventsItem(BaseModel):
    id: typing.Optional[int] = Field(None, alias='id')

    name: typing.Optional[str] = Field(None, alias='name')

    event_type: typing.Optional[str] = Field(None, alias='event_type')

    custom_day_off_type_id: typing.Optional[str] = Field(None, alias='custom_day_off_type_id')

    date: typing.Optional[str] = Field(None, alias='date')

    duration_minutes: typing.Optional[int] = Field(None, alias='duration_minutes')

    start_time_minutes: typing.Optional[int] = Field(None, alias='start_time_minutes')

    type: typing.Optional[str] = Field(None, alias='type')

    working: typing.Optional[int] = Field(None, alias='working')

    status: typing.Optional[str] = Field(None, alias='status')

    color: typing.Optional[str] = Field(None, alias='color')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )