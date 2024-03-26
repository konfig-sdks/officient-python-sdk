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


class PersonSearchByCriteriaResponse(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['PersonSearchByCriteriaResponseItem']:
            return PersonSearchByCriteriaResponseItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['PersonSearchByCriteriaResponseItem'], typing.List['PersonSearchByCriteriaResponseItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'PersonSearchByCriteriaResponse':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'PersonSearchByCriteriaResponseItem':
        return super().__getitem__(i)

from officient_python_sdk.model.person_search_by_criteria_response_item import PersonSearchByCriteriaResponseItem
