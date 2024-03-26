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


class PersonListAvailableComponentsResponseAvailableTypesItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            description = schemas.StrSchema
            id = schemas.IntSchema
            groupname = schemas.StrSchema
            code = schemas.StrSchema
            linked_payroll_provider = schemas.StrSchema
            input_type = schemas.StrSchema
            default_value_hint = schemas.AnyTypeSchema
            __annotations__ = {
                "description": description,
                "id": id,
                "groupname": groupname,
                "code": code,
                "linked_payroll_provider": linked_payroll_provider,
                "input_type": input_type,
                "default_value_hint": default_value_hint,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["groupname"]) -> MetaOapg.properties.groupname: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["code"]) -> MetaOapg.properties.code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["linked_payroll_provider"]) -> MetaOapg.properties.linked_payroll_provider: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["input_type"]) -> MetaOapg.properties.input_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["default_value_hint"]) -> MetaOapg.properties.default_value_hint: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "id", "groupname", "code", "linked_payroll_provider", "input_type", "default_value_hint", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["groupname"]) -> typing.Union[MetaOapg.properties.groupname, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["code"]) -> typing.Union[MetaOapg.properties.code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["linked_payroll_provider"]) -> typing.Union[MetaOapg.properties.linked_payroll_provider, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["input_type"]) -> typing.Union[MetaOapg.properties.input_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["default_value_hint"]) -> typing.Union[MetaOapg.properties.default_value_hint, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "id", "groupname", "code", "linked_payroll_provider", "input_type", "default_value_hint", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        groupname: typing.Union[MetaOapg.properties.groupname, str, schemas.Unset] = schemas.unset,
        code: typing.Union[MetaOapg.properties.code, str, schemas.Unset] = schemas.unset,
        linked_payroll_provider: typing.Union[MetaOapg.properties.linked_payroll_provider, str, schemas.Unset] = schemas.unset,
        input_type: typing.Union[MetaOapg.properties.input_type, str, schemas.Unset] = schemas.unset,
        default_value_hint: typing.Union[MetaOapg.properties.default_value_hint, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PersonListAvailableComponentsResponseAvailableTypesItem':
        return super().__new__(
            cls,
            *args,
            description=description,
            id=id,
            groupname=groupname,
            code=code,
            linked_payroll_provider=linked_payroll_provider,
            input_type=input_type,
            default_value_hint=default_value_hint,
            _configuration=_configuration,
            **kwargs,
        )