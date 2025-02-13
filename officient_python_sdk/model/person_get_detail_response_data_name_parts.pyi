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


class PersonGetDetailResponseDataNameParts(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            initials = schemas.StrSchema
            insertion = schemas.StrSchema
            last_name_composition = schemas.StrSchema
            insertion_partner = schemas.StrSchema
            last_name_partner = schemas.StrSchema
            __annotations__ = {
                "initials": initials,
                "insertion": insertion,
                "last_name_composition": last_name_composition,
                "insertion_partner": insertion_partner,
                "last_name_partner": last_name_partner,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["initials"]) -> MetaOapg.properties.initials: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["insertion"]) -> MetaOapg.properties.insertion: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_name_composition"]) -> MetaOapg.properties.last_name_composition: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["insertion_partner"]) -> MetaOapg.properties.insertion_partner: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_name_partner"]) -> MetaOapg.properties.last_name_partner: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["initials", "insertion", "last_name_composition", "insertion_partner", "last_name_partner", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["initials"]) -> typing.Union[MetaOapg.properties.initials, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["insertion"]) -> typing.Union[MetaOapg.properties.insertion, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_name_composition"]) -> typing.Union[MetaOapg.properties.last_name_composition, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["insertion_partner"]) -> typing.Union[MetaOapg.properties.insertion_partner, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_name_partner"]) -> typing.Union[MetaOapg.properties.last_name_partner, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["initials", "insertion", "last_name_composition", "insertion_partner", "last_name_partner", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        initials: typing.Union[MetaOapg.properties.initials, str, schemas.Unset] = schemas.unset,
        insertion: typing.Union[MetaOapg.properties.insertion, str, schemas.Unset] = schemas.unset,
        last_name_composition: typing.Union[MetaOapg.properties.last_name_composition, str, schemas.Unset] = schemas.unset,
        insertion_partner: typing.Union[MetaOapg.properties.insertion_partner, str, schemas.Unset] = schemas.unset,
        last_name_partner: typing.Union[MetaOapg.properties.last_name_partner, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PersonGetDetailResponseDataNameParts':
        return super().__new__(
            cls,
            *args,
            initials=initials,
            insertion=insertion,
            last_name_composition=last_name_composition,
            insertion_partner=insertion_partner,
            last_name_partner=last_name_partner,
            _configuration=_configuration,
            **kwargs,
        )
