# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from officient_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    PERSON = "Person"
    EXPENSE = "Expense"
    ASSET = "Asset"
    BUDGET = "Budget"
    CONTRACT = "Contract"
    VEHICLE = "Vehicle"
    DOCUMENT = "Document"
    TEAM = "Team"
    WEBHOOK = "Webhook"
    CUSTOM_FIELD = "CustomField"
    FUNCTION = "Function"
    COST_UNIT = "CostUnit"
    CALENDAR_REQUEST = "CalendarRequest"
    DEPARTMENT = "Department"
    COST_CENTER = "CostCenter"
    COMPONENT = "Component"
    AUTHENTICATION = "Authentication"
    ACCOUNT = "Account"
    CALENDAR_STATE = "CalendarState"
    CUSTOM_EVENT_TYPE = "CustomEventType"
    INVITATION = "Invitation"
    PRIORITY_SCHEME = "PriorityScheme"
