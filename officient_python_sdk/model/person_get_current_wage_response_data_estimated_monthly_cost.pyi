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


class PersonGetCurrentWageResponseDataEstimatedMonthlyCost(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def base_components() -> typing.Type['PersonGetCurrentWageResponseDataEstimatedMonthlyCostBaseComponents']:
                return PersonGetCurrentWageResponseDataEstimatedMonthlyCostBaseComponents
        
            @staticmethod
            def custom_components() -> typing.Type['PersonGetCurrentWageResponseDataEstimatedMonthlyCostCustomComponents']:
                return PersonGetCurrentWageResponseDataEstimatedMonthlyCostCustomComponents
            __annotations__ = {
                "base_components": base_components,
                "custom_components": custom_components,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["base_components"]) -> 'PersonGetCurrentWageResponseDataEstimatedMonthlyCostBaseComponents': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["custom_components"]) -> 'PersonGetCurrentWageResponseDataEstimatedMonthlyCostCustomComponents': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["base_components", "custom_components", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["base_components"]) -> typing.Union['PersonGetCurrentWageResponseDataEstimatedMonthlyCostBaseComponents', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["custom_components"]) -> typing.Union['PersonGetCurrentWageResponseDataEstimatedMonthlyCostCustomComponents', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["base_components", "custom_components", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        base_components: typing.Union['PersonGetCurrentWageResponseDataEstimatedMonthlyCostBaseComponents', schemas.Unset] = schemas.unset,
        custom_components: typing.Union['PersonGetCurrentWageResponseDataEstimatedMonthlyCostCustomComponents', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PersonGetCurrentWageResponseDataEstimatedMonthlyCost':
        return super().__new__(
            cls,
            *args,
            base_components=base_components,
            custom_components=custom_components,
            _configuration=_configuration,
            **kwargs,
        )

from officient_python_sdk.model.person_get_current_wage_response_data_estimated_monthly_cost_base_components import PersonGetCurrentWageResponseDataEstimatedMonthlyCostBaseComponents
from officient_python_sdk.model.person_get_current_wage_response_data_estimated_monthly_cost_custom_components import PersonGetCurrentWageResponseDataEstimatedMonthlyCostCustomComponents