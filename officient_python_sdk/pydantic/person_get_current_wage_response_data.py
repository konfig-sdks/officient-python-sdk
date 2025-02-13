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

from officient_python_sdk.pydantic.person_get_current_wage_response_data_custom_payroll_data import PersonGetCurrentWageResponseDataCustomPayrollData
from officient_python_sdk.pydantic.person_get_current_wage_response_data_estimated_monthly_cost import PersonGetCurrentWageResponseDataEstimatedMonthlyCost
from officient_python_sdk.pydantic.person_get_current_wage_response_data_multiple_week_schedule import PersonGetCurrentWageResponseDataMultipleWeekSchedule
from officient_python_sdk.pydantic.person_get_current_wage_response_data_weekly_time_engagement_minutes import PersonGetCurrentWageResponseDataWeeklyTimeEngagementMinutes

class PersonGetCurrentWageResponseData(BaseModel):
    id: typing.Optional[int] = Field(None, alias='id')

    start_date: typing.Optional[str] = Field(None, alias='start_date')

    end_date: typing.Optional[str] = Field(None, alias='end_date')

    estimated_monthly_total: typing.Optional[int] = Field(None, alias='estimated_monthly_total')

    currency: typing.Optional[str] = Field(None, alias='currency')

    type: typing.Optional[str] = Field(None, alias='type')

    rate: typing.Optional[int] = Field(None, alias='rate')

    created_at: typing.Optional[int] = Field(None, alias='created_at')

    updated_at: typing.Optional[int] = Field(None, alias='updated_at')

    registration_country_code: typing.Optional[str] = Field(None, alias='registration_country_code')

    estimated_monthly_cost: typing.Optional[PersonGetCurrentWageResponseDataEstimatedMonthlyCost] = Field(None, alias='estimated_monthly_cost')

    weekly_time_engagement_minutes: typing.Optional[PersonGetCurrentWageResponseDataWeeklyTimeEngagementMinutes] = Field(None, alias='weekly_time_engagement_minutes')

    custom_payroll_data: typing.Optional[PersonGetCurrentWageResponseDataCustomPayrollData] = Field(None, alias='custom_payroll_data')

    termination_reason: typing.Optional[str] = Field(None, alias='termination_reason')

    multiple_week_schedule: typing.Optional[PersonGetCurrentWageResponseDataMultipleWeekSchedule] = Field(None, alias='multiple_week_schedule')

    contract_index_number: typing.Optional[int] = Field(None, alias='contract_index_number')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
