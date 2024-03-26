import typing_extensions

from officient_python_sdk.apis.tags import TagValues
from officient_python_sdk.apis.tags.person_api import PersonApi
from officient_python_sdk.apis.tags.expense_api import ExpenseApi
from officient_python_sdk.apis.tags.asset_api import AssetApi
from officient_python_sdk.apis.tags.budget_api import BudgetApi
from officient_python_sdk.apis.tags.contract_api import ContractApi
from officient_python_sdk.apis.tags.vehicle_api import VehicleApi
from officient_python_sdk.apis.tags.document_api import DocumentApi
from officient_python_sdk.apis.tags.team_api import TeamApi
from officient_python_sdk.apis.tags.webhook_api import WebhookApi
from officient_python_sdk.apis.tags.custom_field_api import CustomFieldApi
from officient_python_sdk.apis.tags.function_api import FunctionApi
from officient_python_sdk.apis.tags.cost_unit_api import CostUnitApi
from officient_python_sdk.apis.tags.calendar_request_api import CalendarRequestApi
from officient_python_sdk.apis.tags.department_api import DepartmentApi
from officient_python_sdk.apis.tags.cost_center_api import CostCenterApi
from officient_python_sdk.apis.tags.component_api import ComponentApi
from officient_python_sdk.apis.tags.authentication_api import AuthenticationApi
from officient_python_sdk.apis.tags.account_api import AccountApi
from officient_python_sdk.apis.tags.calendar_state_api import CalendarStateApi
from officient_python_sdk.apis.tags.custom_event_type_api import CustomEventTypeApi
from officient_python_sdk.apis.tags.invitation_api import InvitationApi
from officient_python_sdk.apis.tags.priority_scheme_api import PrioritySchemeApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.PERSON: PersonApi,
        TagValues.EXPENSE: ExpenseApi,
        TagValues.ASSET: AssetApi,
        TagValues.BUDGET: BudgetApi,
        TagValues.CONTRACT: ContractApi,
        TagValues.VEHICLE: VehicleApi,
        TagValues.DOCUMENT: DocumentApi,
        TagValues.TEAM: TeamApi,
        TagValues.WEBHOOK: WebhookApi,
        TagValues.CUSTOM_FIELD: CustomFieldApi,
        TagValues.FUNCTION: FunctionApi,
        TagValues.COST_UNIT: CostUnitApi,
        TagValues.CALENDAR_REQUEST: CalendarRequestApi,
        TagValues.DEPARTMENT: DepartmentApi,
        TagValues.COST_CENTER: CostCenterApi,
        TagValues.COMPONENT: ComponentApi,
        TagValues.AUTHENTICATION: AuthenticationApi,
        TagValues.ACCOUNT: AccountApi,
        TagValues.CALENDAR_STATE: CalendarStateApi,
        TagValues.CUSTOM_EVENT_TYPE: CustomEventTypeApi,
        TagValues.INVITATION: InvitationApi,
        TagValues.PRIORITY_SCHEME: PrioritySchemeApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.PERSON: PersonApi,
        TagValues.EXPENSE: ExpenseApi,
        TagValues.ASSET: AssetApi,
        TagValues.BUDGET: BudgetApi,
        TagValues.CONTRACT: ContractApi,
        TagValues.VEHICLE: VehicleApi,
        TagValues.DOCUMENT: DocumentApi,
        TagValues.TEAM: TeamApi,
        TagValues.WEBHOOK: WebhookApi,
        TagValues.CUSTOM_FIELD: CustomFieldApi,
        TagValues.FUNCTION: FunctionApi,
        TagValues.COST_UNIT: CostUnitApi,
        TagValues.CALENDAR_REQUEST: CalendarRequestApi,
        TagValues.DEPARTMENT: DepartmentApi,
        TagValues.COST_CENTER: CostCenterApi,
        TagValues.COMPONENT: ComponentApi,
        TagValues.AUTHENTICATION: AuthenticationApi,
        TagValues.ACCOUNT: AccountApi,
        TagValues.CALENDAR_STATE: CalendarStateApi,
        TagValues.CUSTOM_EVENT_TYPE: CustomEventTypeApi,
        TagValues.INVITATION: InvitationApi,
        TagValues.PRIORITY_SCHEME: PrioritySchemeApi,
    }
)
