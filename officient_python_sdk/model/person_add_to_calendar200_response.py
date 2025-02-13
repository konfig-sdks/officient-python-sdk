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


class PersonAddToCalendar200Response(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            ruleset_id = schemas.IntSchema
        
            @staticmethod
            def events() -> typing.Type['PersonAddToCalendar200ResponseEvents']:
                return PersonAddToCalendar200ResponseEvents
            __annotations__ = {
                "ruleset_id": ruleset_id,
                "events": events,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ruleset_id"]) -> MetaOapg.properties.ruleset_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["events"]) -> 'PersonAddToCalendar200ResponseEvents': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["ruleset_id", "events", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ruleset_id"]) -> typing.Union[MetaOapg.properties.ruleset_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["events"]) -> typing.Union['PersonAddToCalendar200ResponseEvents', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["ruleset_id", "events", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        ruleset_id: typing.Union[MetaOapg.properties.ruleset_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        events: typing.Union['PersonAddToCalendar200ResponseEvents', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PersonAddToCalendar200Response':
        return super().__new__(
            cls,
            *args,
            ruleset_id=ruleset_id,
            events=events,
            _configuration=_configuration,
            **kwargs,
        )

from officient_python_sdk.model.person_add_to_calendar200_response_events import PersonAddToCalendar200ResponseEvents
