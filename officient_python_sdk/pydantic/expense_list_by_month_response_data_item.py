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


class ExpenseListByMonthResponseDataItem(BaseModel):
    title: typing.Optional[str] = Field(None, alias='title')

    description: typing.Optional[str] = Field(None, alias='description')

    id: typing.Optional[int] = Field(None, alias='id')

    employee_id: typing.Optional[int] = Field(None, alias='employee_id')

    date: typing.Optional[str] = Field(None, alias='date')

    time_created: typing.Optional[int] = Field(None, alias='time_created')

    status: typing.Optional[str] = Field(None, alias='status')

    price: typing.Optional[str] = Field(None, alias='price')

    payout_method: typing.Optional[str] = Field(None, alias='payout_method')

    payout_period: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='payout_period')

    payout_period_frequency: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='payout_period_frequency')

    payout_year: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='payout_year')

    expense_category_id: typing.Optional[int] = Field(None, alias='expense_category_id')

    price_per_kilometer: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='price_per_kilometer')

    distance: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='distance')

    metadata: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='metadata')

    dates: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='dates')

    date_approved: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='date_approved')

    payout_other_reason: typing.Optional[str] = Field(None, alias='payout_other_reason')

    payout_status: typing.Optional[str] = Field(None, alias='payout_status')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
