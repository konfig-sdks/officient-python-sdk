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

from officient_python_sdk.type.expense_list_by_category_detail_response_data_payroll_components import ExpenseListByCategoryDetailResponseDataPayrollComponents

class RequiredExpenseListByCategoryDetailResponseData(TypedDict):
    pass

class OptionalExpenseListByCategoryDetailResponseData(TypedDict, total=False):
    id: int

    name: str

    way_of_input: str

    price_per_kilometer: str

    deleted: int

    payroll_components: ExpenseListByCategoryDetailResponseDataPayrollComponents

class ExpenseListByCategoryDetailResponseData(RequiredExpenseListByCategoryDetailResponseData, OptionalExpenseListByCategoryDetailResponseData):
    pass
