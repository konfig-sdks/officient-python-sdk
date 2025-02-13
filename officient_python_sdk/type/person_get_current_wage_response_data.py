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

from officient_python_sdk.type.person_get_current_wage_response_data_custom_payroll_data import PersonGetCurrentWageResponseDataCustomPayrollData
from officient_python_sdk.type.person_get_current_wage_response_data_estimated_monthly_cost import PersonGetCurrentWageResponseDataEstimatedMonthlyCost
from officient_python_sdk.type.person_get_current_wage_response_data_multiple_week_schedule import PersonGetCurrentWageResponseDataMultipleWeekSchedule
from officient_python_sdk.type.person_get_current_wage_response_data_weekly_time_engagement_minutes import PersonGetCurrentWageResponseDataWeeklyTimeEngagementMinutes

class RequiredPersonGetCurrentWageResponseData(TypedDict):
    pass

class OptionalPersonGetCurrentWageResponseData(TypedDict, total=False):
    id: int

    start_date: str

    end_date: str

    estimated_monthly_total: int

    currency: str

    type: str

    rate: int

    created_at: int

    updated_at: int

    registration_country_code: str

    estimated_monthly_cost: PersonGetCurrentWageResponseDataEstimatedMonthlyCost

    weekly_time_engagement_minutes: PersonGetCurrentWageResponseDataWeeklyTimeEngagementMinutes

    custom_payroll_data: PersonGetCurrentWageResponseDataCustomPayrollData

    termination_reason: str

    multiple_week_schedule: PersonGetCurrentWageResponseDataMultipleWeekSchedule

    contract_index_number: int

class PersonGetCurrentWageResponseData(RequiredPersonGetCurrentWageResponseData, OptionalPersonGetCurrentWageResponseData):
    pass
