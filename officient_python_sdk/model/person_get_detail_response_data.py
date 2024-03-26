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


class PersonGetDetailResponseData(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            id = schemas.IntSchema
            deleted = schemas.IntSchema
            name = schemas.StrSchema
            first_name = schemas.StrSchema
            last_name = schemas.StrSchema
            created_at = schemas.IntSchema
            preferred_language_code = schemas.StrSchema
            email = schemas.StrSchema
            personal_email = schemas.StrSchema
            national_number = schemas.StrSchema
            social_security_nr = schemas.StrSchema
            birthdate = schemas.StrSchema
            birthplace = schemas.StrSchema
            avatar = schemas.StrSchema
            linked_payroll_provider = schemas.StrSchema
            linked_payroll_employee_id = schemas.StrSchema
            linked_payroll_employee_number = schemas.StrSchema
            dependent_adults_below_65 = schemas.IntSchema
            dependent_children = schemas.IntSchema
            dependent_adults_above_65 = schemas.IntSchema
            dependent_disabled_children = schemas.IntSchema
            dependent_disabled_adults_below_65 = schemas.IntSchema
            dependent_disabled_adults_above_65 = schemas.IntSchema
            spouse_has_income = schemas.BoolSchema
            phone = schemas.StrSchema
            civil_state = schemas.StrSchema
            nationality_country_code = schemas.StrSchema
            gender = schemas.StrSchema
            bank_account_iban = schemas.StrSchema
            bank_account_bic = schemas.StrSchema
        
            @staticmethod
            def emergency_contact() -> typing.Type['PersonGetDetailResponseDataEmergencyContact']:
                return PersonGetDetailResponseDataEmergencyContact
        
            @staticmethod
            def address() -> typing.Type['PersonGetDetailResponseDataAddress']:
                return PersonGetDetailResponseDataAddress
        
            @staticmethod
            def team() -> typing.Type['PersonGetDetailResponseDataTeam']:
                return PersonGetDetailResponseDataTeam
        
            @staticmethod
            def employment() -> typing.Type['PersonGetDetailResponseDataEmployment']:
                return PersonGetDetailResponseDataEmployment
        
            @staticmethod
            def current_role() -> typing.Type['PersonGetDetailResponseDataCurrentRole']:
                return PersonGetDetailResponseDataCurrentRole
        
            @staticmethod
            def current_reports_to() -> typing.Type['PersonGetDetailResponseDataCurrentReportsTo']:
                return PersonGetDetailResponseDataCurrentReportsTo
        
            @staticmethod
            def custom_fields() -> typing.Type['PersonGetDetailResponseDataCustomFields']:
                return PersonGetDetailResponseDataCustomFields
        
            @staticmethod
            def name_parts() -> typing.Type['PersonGetDetailResponseDataNameParts']:
                return PersonGetDetailResponseDataNameParts
            __annotations__ = {
                "id": id,
                "deleted": deleted,
                "name": name,
                "first_name": first_name,
                "last_name": last_name,
                "created_at": created_at,
                "preferred_language_code": preferred_language_code,
                "email": email,
                "personal_email": personal_email,
                "national_number": national_number,
                "social_security_nr": social_security_nr,
                "birthdate": birthdate,
                "birthplace": birthplace,
                "avatar": avatar,
                "linked_payroll_provider": linked_payroll_provider,
                "linked_payroll_employee_id": linked_payroll_employee_id,
                "linked_payroll_employee_number": linked_payroll_employee_number,
                "dependent_adults_below_65": dependent_adults_below_65,
                "dependent_children": dependent_children,
                "dependent_adults_above_65": dependent_adults_above_65,
                "dependent_disabled_children": dependent_disabled_children,
                "dependent_disabled_adults_below_65": dependent_disabled_adults_below_65,
                "dependent_disabled_adults_above_65": dependent_disabled_adults_above_65,
                "spouse_has_income": spouse_has_income,
                "phone": phone,
                "civil_state": civil_state,
                "nationality_country_code": nationality_country_code,
                "gender": gender,
                "bank_account_iban": bank_account_iban,
                "bank_account_bic": bank_account_bic,
                "emergency_contact": emergency_contact,
                "address": address,
                "team": team,
                "employment": employment,
                "current_role": current_role,
                "current_reports_to": current_reports_to,
                "custom_fields": custom_fields,
                "name_parts": name_parts,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deleted"]) -> MetaOapg.properties.deleted: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["first_name"]) -> MetaOapg.properties.first_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_name"]) -> MetaOapg.properties.last_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["preferred_language_code"]) -> MetaOapg.properties.preferred_language_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["personal_email"]) -> MetaOapg.properties.personal_email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["national_number"]) -> MetaOapg.properties.national_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["social_security_nr"]) -> MetaOapg.properties.social_security_nr: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["birthdate"]) -> MetaOapg.properties.birthdate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["birthplace"]) -> MetaOapg.properties.birthplace: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["avatar"]) -> MetaOapg.properties.avatar: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["linked_payroll_provider"]) -> MetaOapg.properties.linked_payroll_provider: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["linked_payroll_employee_id"]) -> MetaOapg.properties.linked_payroll_employee_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["linked_payroll_employee_number"]) -> MetaOapg.properties.linked_payroll_employee_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dependent_adults_below_65"]) -> MetaOapg.properties.dependent_adults_below_65: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dependent_children"]) -> MetaOapg.properties.dependent_children: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dependent_adults_above_65"]) -> MetaOapg.properties.dependent_adults_above_65: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dependent_disabled_children"]) -> MetaOapg.properties.dependent_disabled_children: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dependent_disabled_adults_below_65"]) -> MetaOapg.properties.dependent_disabled_adults_below_65: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dependent_disabled_adults_above_65"]) -> MetaOapg.properties.dependent_disabled_adults_above_65: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["spouse_has_income"]) -> MetaOapg.properties.spouse_has_income: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phone"]) -> MetaOapg.properties.phone: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["civil_state"]) -> MetaOapg.properties.civil_state: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nationality_country_code"]) -> MetaOapg.properties.nationality_country_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gender"]) -> MetaOapg.properties.gender: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bank_account_iban"]) -> MetaOapg.properties.bank_account_iban: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bank_account_bic"]) -> MetaOapg.properties.bank_account_bic: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["emergency_contact"]) -> 'PersonGetDetailResponseDataEmergencyContact': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address"]) -> 'PersonGetDetailResponseDataAddress': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["team"]) -> 'PersonGetDetailResponseDataTeam': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employment"]) -> 'PersonGetDetailResponseDataEmployment': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["current_role"]) -> 'PersonGetDetailResponseDataCurrentRole': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["current_reports_to"]) -> 'PersonGetDetailResponseDataCurrentReportsTo': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["custom_fields"]) -> 'PersonGetDetailResponseDataCustomFields': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name_parts"]) -> 'PersonGetDetailResponseDataNameParts': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "deleted", "name", "first_name", "last_name", "created_at", "preferred_language_code", "email", "personal_email", "national_number", "social_security_nr", "birthdate", "birthplace", "avatar", "linked_payroll_provider", "linked_payroll_employee_id", "linked_payroll_employee_number", "dependent_adults_below_65", "dependent_children", "dependent_adults_above_65", "dependent_disabled_children", "dependent_disabled_adults_below_65", "dependent_disabled_adults_above_65", "spouse_has_income", "phone", "civil_state", "nationality_country_code", "gender", "bank_account_iban", "bank_account_bic", "emergency_contact", "address", "team", "employment", "current_role", "current_reports_to", "custom_fields", "name_parts", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deleted"]) -> typing.Union[MetaOapg.properties.deleted, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["first_name"]) -> typing.Union[MetaOapg.properties.first_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_name"]) -> typing.Union[MetaOapg.properties.last_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> typing.Union[MetaOapg.properties.created_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["preferred_language_code"]) -> typing.Union[MetaOapg.properties.preferred_language_code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> typing.Union[MetaOapg.properties.email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["personal_email"]) -> typing.Union[MetaOapg.properties.personal_email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["national_number"]) -> typing.Union[MetaOapg.properties.national_number, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["social_security_nr"]) -> typing.Union[MetaOapg.properties.social_security_nr, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["birthdate"]) -> typing.Union[MetaOapg.properties.birthdate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["birthplace"]) -> typing.Union[MetaOapg.properties.birthplace, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["avatar"]) -> typing.Union[MetaOapg.properties.avatar, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["linked_payroll_provider"]) -> typing.Union[MetaOapg.properties.linked_payroll_provider, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["linked_payroll_employee_id"]) -> typing.Union[MetaOapg.properties.linked_payroll_employee_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["linked_payroll_employee_number"]) -> typing.Union[MetaOapg.properties.linked_payroll_employee_number, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dependent_adults_below_65"]) -> typing.Union[MetaOapg.properties.dependent_adults_below_65, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dependent_children"]) -> typing.Union[MetaOapg.properties.dependent_children, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dependent_adults_above_65"]) -> typing.Union[MetaOapg.properties.dependent_adults_above_65, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dependent_disabled_children"]) -> typing.Union[MetaOapg.properties.dependent_disabled_children, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dependent_disabled_adults_below_65"]) -> typing.Union[MetaOapg.properties.dependent_disabled_adults_below_65, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dependent_disabled_adults_above_65"]) -> typing.Union[MetaOapg.properties.dependent_disabled_adults_above_65, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["spouse_has_income"]) -> typing.Union[MetaOapg.properties.spouse_has_income, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phone"]) -> typing.Union[MetaOapg.properties.phone, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["civil_state"]) -> typing.Union[MetaOapg.properties.civil_state, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nationality_country_code"]) -> typing.Union[MetaOapg.properties.nationality_country_code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gender"]) -> typing.Union[MetaOapg.properties.gender, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bank_account_iban"]) -> typing.Union[MetaOapg.properties.bank_account_iban, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bank_account_bic"]) -> typing.Union[MetaOapg.properties.bank_account_bic, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["emergency_contact"]) -> typing.Union['PersonGetDetailResponseDataEmergencyContact', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address"]) -> typing.Union['PersonGetDetailResponseDataAddress', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["team"]) -> typing.Union['PersonGetDetailResponseDataTeam', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employment"]) -> typing.Union['PersonGetDetailResponseDataEmployment', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["current_role"]) -> typing.Union['PersonGetDetailResponseDataCurrentRole', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["current_reports_to"]) -> typing.Union['PersonGetDetailResponseDataCurrentReportsTo', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["custom_fields"]) -> typing.Union['PersonGetDetailResponseDataCustomFields', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name_parts"]) -> typing.Union['PersonGetDetailResponseDataNameParts', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "deleted", "name", "first_name", "last_name", "created_at", "preferred_language_code", "email", "personal_email", "national_number", "social_security_nr", "birthdate", "birthplace", "avatar", "linked_payroll_provider", "linked_payroll_employee_id", "linked_payroll_employee_number", "dependent_adults_below_65", "dependent_children", "dependent_adults_above_65", "dependent_disabled_children", "dependent_disabled_adults_below_65", "dependent_disabled_adults_above_65", "spouse_has_income", "phone", "civil_state", "nationality_country_code", "gender", "bank_account_iban", "bank_account_bic", "emergency_contact", "address", "team", "employment", "current_role", "current_reports_to", "custom_fields", "name_parts", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        deleted: typing.Union[MetaOapg.properties.deleted, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        first_name: typing.Union[MetaOapg.properties.first_name, str, schemas.Unset] = schemas.unset,
        last_name: typing.Union[MetaOapg.properties.last_name, str, schemas.Unset] = schemas.unset,
        created_at: typing.Union[MetaOapg.properties.created_at, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        preferred_language_code: typing.Union[MetaOapg.properties.preferred_language_code, str, schemas.Unset] = schemas.unset,
        email: typing.Union[MetaOapg.properties.email, str, schemas.Unset] = schemas.unset,
        personal_email: typing.Union[MetaOapg.properties.personal_email, str, schemas.Unset] = schemas.unset,
        national_number: typing.Union[MetaOapg.properties.national_number, str, schemas.Unset] = schemas.unset,
        social_security_nr: typing.Union[MetaOapg.properties.social_security_nr, str, schemas.Unset] = schemas.unset,
        birthdate: typing.Union[MetaOapg.properties.birthdate, str, schemas.Unset] = schemas.unset,
        birthplace: typing.Union[MetaOapg.properties.birthplace, str, schemas.Unset] = schemas.unset,
        avatar: typing.Union[MetaOapg.properties.avatar, str, schemas.Unset] = schemas.unset,
        linked_payroll_provider: typing.Union[MetaOapg.properties.linked_payroll_provider, str, schemas.Unset] = schemas.unset,
        linked_payroll_employee_id: typing.Union[MetaOapg.properties.linked_payroll_employee_id, str, schemas.Unset] = schemas.unset,
        linked_payroll_employee_number: typing.Union[MetaOapg.properties.linked_payroll_employee_number, str, schemas.Unset] = schemas.unset,
        dependent_adults_below_65: typing.Union[MetaOapg.properties.dependent_adults_below_65, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        dependent_children: typing.Union[MetaOapg.properties.dependent_children, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        dependent_adults_above_65: typing.Union[MetaOapg.properties.dependent_adults_above_65, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        dependent_disabled_children: typing.Union[MetaOapg.properties.dependent_disabled_children, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        dependent_disabled_adults_below_65: typing.Union[MetaOapg.properties.dependent_disabled_adults_below_65, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        dependent_disabled_adults_above_65: typing.Union[MetaOapg.properties.dependent_disabled_adults_above_65, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        spouse_has_income: typing.Union[MetaOapg.properties.spouse_has_income, bool, schemas.Unset] = schemas.unset,
        phone: typing.Union[MetaOapg.properties.phone, str, schemas.Unset] = schemas.unset,
        civil_state: typing.Union[MetaOapg.properties.civil_state, str, schemas.Unset] = schemas.unset,
        nationality_country_code: typing.Union[MetaOapg.properties.nationality_country_code, str, schemas.Unset] = schemas.unset,
        gender: typing.Union[MetaOapg.properties.gender, str, schemas.Unset] = schemas.unset,
        bank_account_iban: typing.Union[MetaOapg.properties.bank_account_iban, str, schemas.Unset] = schemas.unset,
        bank_account_bic: typing.Union[MetaOapg.properties.bank_account_bic, str, schemas.Unset] = schemas.unset,
        emergency_contact: typing.Union['PersonGetDetailResponseDataEmergencyContact', schemas.Unset] = schemas.unset,
        address: typing.Union['PersonGetDetailResponseDataAddress', schemas.Unset] = schemas.unset,
        team: typing.Union['PersonGetDetailResponseDataTeam', schemas.Unset] = schemas.unset,
        employment: typing.Union['PersonGetDetailResponseDataEmployment', schemas.Unset] = schemas.unset,
        current_role: typing.Union['PersonGetDetailResponseDataCurrentRole', schemas.Unset] = schemas.unset,
        current_reports_to: typing.Union['PersonGetDetailResponseDataCurrentReportsTo', schemas.Unset] = schemas.unset,
        custom_fields: typing.Union['PersonGetDetailResponseDataCustomFields', schemas.Unset] = schemas.unset,
        name_parts: typing.Union['PersonGetDetailResponseDataNameParts', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PersonGetDetailResponseData':
        return super().__new__(
            cls,
            *args,
            id=id,
            deleted=deleted,
            name=name,
            first_name=first_name,
            last_name=last_name,
            created_at=created_at,
            preferred_language_code=preferred_language_code,
            email=email,
            personal_email=personal_email,
            national_number=national_number,
            social_security_nr=social_security_nr,
            birthdate=birthdate,
            birthplace=birthplace,
            avatar=avatar,
            linked_payroll_provider=linked_payroll_provider,
            linked_payroll_employee_id=linked_payroll_employee_id,
            linked_payroll_employee_number=linked_payroll_employee_number,
            dependent_adults_below_65=dependent_adults_below_65,
            dependent_children=dependent_children,
            dependent_adults_above_65=dependent_adults_above_65,
            dependent_disabled_children=dependent_disabled_children,
            dependent_disabled_adults_below_65=dependent_disabled_adults_below_65,
            dependent_disabled_adults_above_65=dependent_disabled_adults_above_65,
            spouse_has_income=spouse_has_income,
            phone=phone,
            civil_state=civil_state,
            nationality_country_code=nationality_country_code,
            gender=gender,
            bank_account_iban=bank_account_iban,
            bank_account_bic=bank_account_bic,
            emergency_contact=emergency_contact,
            address=address,
            team=team,
            employment=employment,
            current_role=current_role,
            current_reports_to=current_reports_to,
            custom_fields=custom_fields,
            name_parts=name_parts,
            _configuration=_configuration,
            **kwargs,
        )

from officient_python_sdk.model.person_get_detail_response_data_address import PersonGetDetailResponseDataAddress
from officient_python_sdk.model.person_get_detail_response_data_current_reports_to import PersonGetDetailResponseDataCurrentReportsTo
from officient_python_sdk.model.person_get_detail_response_data_current_role import PersonGetDetailResponseDataCurrentRole
from officient_python_sdk.model.person_get_detail_response_data_custom_fields import PersonGetDetailResponseDataCustomFields
from officient_python_sdk.model.person_get_detail_response_data_emergency_contact import PersonGetDetailResponseDataEmergencyContact
from officient_python_sdk.model.person_get_detail_response_data_employment import PersonGetDetailResponseDataEmployment
from officient_python_sdk.model.person_get_detail_response_data_name_parts import PersonGetDetailResponseDataNameParts
from officient_python_sdk.model.person_get_detail_response_data_team import PersonGetDetailResponseDataTeam