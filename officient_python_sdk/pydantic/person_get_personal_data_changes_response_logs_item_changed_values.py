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

from officient_python_sdk.pydantic.person_get_personal_data_changes_response_logs_item_changed_values_address_city import PersonGetPersonalDataChangesResponseLogsItemChangedValuesAddressCity
from officient_python_sdk.pydantic.person_get_personal_data_changes_response_logs_item_changed_values_address_country_code import PersonGetPersonalDataChangesResponseLogsItemChangedValuesAddressCountryCode
from officient_python_sdk.pydantic.person_get_personal_data_changes_response_logs_item_changed_values_address_line1 import PersonGetPersonalDataChangesResponseLogsItemChangedValuesAddressLine1
from officient_python_sdk.pydantic.person_get_personal_data_changes_response_logs_item_changed_values_address_zipcode import PersonGetPersonalDataChangesResponseLogsItemChangedValuesAddressZipcode

class PersonGetPersonalDataChangesResponseLogsItemChangedValues(BaseModel):
    address_country_code: typing.Optional[PersonGetPersonalDataChangesResponseLogsItemChangedValuesAddressCountryCode] = Field(None, alias='address_country_code')

    address_line_1: typing.Optional[PersonGetPersonalDataChangesResponseLogsItemChangedValuesAddressLine1] = Field(None, alias='address_line_1')

    address_zipcode: typing.Optional[PersonGetPersonalDataChangesResponseLogsItemChangedValuesAddressZipcode] = Field(None, alias='address_zipcode')

    address_city: typing.Optional[PersonGetPersonalDataChangesResponseLogsItemChangedValuesAddressCity] = Field(None, alias='address_city')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
