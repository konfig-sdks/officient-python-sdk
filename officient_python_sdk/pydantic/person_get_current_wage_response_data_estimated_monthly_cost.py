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

from officient_python_sdk.pydantic.person_get_current_wage_response_data_estimated_monthly_cost_base_components import PersonGetCurrentWageResponseDataEstimatedMonthlyCostBaseComponents
from officient_python_sdk.pydantic.person_get_current_wage_response_data_estimated_monthly_cost_custom_components import PersonGetCurrentWageResponseDataEstimatedMonthlyCostCustomComponents

class PersonGetCurrentWageResponseDataEstimatedMonthlyCost(BaseModel):
    base_components: typing.Optional[PersonGetCurrentWageResponseDataEstimatedMonthlyCostBaseComponents] = Field(None, alias='base_components')

    custom_components: typing.Optional[PersonGetCurrentWageResponseDataEstimatedMonthlyCostCustomComponents] = Field(None, alias='custom_components')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )