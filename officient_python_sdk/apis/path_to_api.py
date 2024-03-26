import typing_extensions

from officient_python_sdk.paths import PathValues
from officient_python_sdk.apis.paths._1_0_people_list import Model10PeopleList
from officient_python_sdk.apis.paths._1_0_token import Model10Token
from officient_python_sdk.apis.paths._1_0_wages_person_id_current import Model10WagesPersonIdCurrent
from officient_python_sdk.apis.paths._1_0_people_selfservice_invite_link import Model10PeopleSelfserviceInviteLink
from officient_python_sdk.apis.paths._1_0_wages_person_id_history import Model10WagesPersonIdHistory
from officient_python_sdk.apis.paths._1_0_assets_list import Model10AssetsList
from officient_python_sdk.apis.paths._1_0_assets_asset_id_detail import Model10AssetsAssetIdDetail
from officient_python_sdk.apis.paths._1_0_fleet_vehicle_id_detail import Model10FleetVehicleIdDetail
from officient_python_sdk.apis.paths._1_0_fleet_list import Model10FleetList
from officient_python_sdk.apis.paths._1_0_contracts_list import Model10ContractsList
from officient_python_sdk.apis.paths._1_0_contracts_contract_id_detail import Model10ContractsContractIdDetail
from officient_python_sdk.apis.paths._1_0_contracts_contract_id_pdf import Model10ContractsContractIdPdf
from officient_python_sdk.apis.paths._1_0_calendar_person_id_year_month import Model10CalendarPersonIdYearMonth
from officient_python_sdk.apis.paths._1_0_teams_list import Model10TeamsList
from officient_python_sdk.apis.paths._1_0_people_add import Model10PeopleAdd
from officient_python_sdk.apis.paths._1_0_calendar_events_types_year import Model10CalendarEventsTypesYear
from officient_python_sdk.apis.paths._1_0_calendar_person_id_events_add import Model10CalendarPersonIdEventsAdd
from officient_python_sdk.apis.paths._1_0_calendar_person_id_events_event_id import Model10CalendarPersonIdEventsEventId
from officient_python_sdk.apis.paths._1_0_calendar_person_id_year_month_day_work import Model10CalendarPersonIdYearMonthDayWork
from officient_python_sdk.apis.paths._1_0_calendar_person_id_year_month_day_work_reset import Model10CalendarPersonIdYearMonthDayWorkReset
from officient_python_sdk.apis.paths._1_0_people_person_id_detail import Model10PeoplePersonIdDetail
from officient_python_sdk.apis.paths._1_0_documents_object_type_object_id_list import Model10DocumentsObjectTypeObjectIdList
from officient_python_sdk.apis.paths._1_0_documents_file_id_download import Model10DocumentsFileIdDownload
from officient_python_sdk.apis.paths._1_0_documents_object_type_object_id_add import Model10DocumentsObjectTypeObjectIdAdd
from officient_python_sdk.apis.paths._1_0_webhooks_add import Model10WebhooksAdd
from officient_python_sdk.apis.paths._1_0_webhooks_webhook_id import Model10WebhooksWebhookId
from officient_python_sdk.apis.paths._1_0_webhooks_list import Model10WebhooksList
from officient_python_sdk.apis.paths._1_0_account import Model10Account
from officient_python_sdk.apis.paths._1_0_contracts_add import Model10ContractsAdd
from officient_python_sdk.apis.paths._1_0_contracts_signature_request import Model10ContractsSignatureRequest
from officient_python_sdk.apis.paths._1_0_calendar_person_id_events_types_year_limits import Model10CalendarPersonIdEventsTypesYearLimits
from officient_python_sdk.apis.paths._1_0_calendar_person_id_events_types_year_limits_type_id_set import Model10CalendarPersonIdEventsTypesYearLimitsTypeIdSet
from officient_python_sdk.apis.paths._1_0_people_search import Model10PeopleSearch
from officient_python_sdk.apis.paths._1_0_calendar_person_id_year_work_bulk import Model10CalendarPersonIdYearWorkBulk
from officient_python_sdk.apis.paths._1_0_people_person_id_manager import Model10PeoplePersonIdManager
from officient_python_sdk.apis.paths._1_0_calendar_person_id_year_month_day_events_set import Model10CalendarPersonIdYearMonthDayEventsSet
from officient_python_sdk.apis.paths._1_0_calendar_person_id_year_month_day import Model10CalendarPersonIdYearMonthDay
from officient_python_sdk.apis.paths._1_0_people_person_id_role import Model10PeoplePersonIdRole
from officient_python_sdk.apis.paths._1_0_teams_team_id import Model10TeamsTeamId
from officient_python_sdk.apis.paths._1_0_teams_add import Model10TeamsAdd
from officient_python_sdk.apis.paths._1_0_assets_types_list import Model10AssetsTypesList
from officient_python_sdk.apis.paths._1_0_assets_types_add import Model10AssetsTypesAdd
from officient_python_sdk.apis.paths._1_0_assets_types_asset_type_id import Model10AssetsTypesAssetTypeId
from officient_python_sdk.apis.paths._1_0_assets_add import Model10AssetsAdd
from officient_python_sdk.apis.paths._1_0_assets_asset_id import Model10AssetsAssetId
from officient_python_sdk.apis.paths._1_0_fleet_add import Model10FleetAdd
from officient_python_sdk.apis.paths._1_0_fleet_vehicle_id import Model10FleetVehicleId
from officient_python_sdk.apis.paths._1_0_calendar_person_id_year import Model10CalendarPersonIdYear
from officient_python_sdk.apis.paths._1_0_calendar_requests_list import Model10CalendarRequestsList
from officient_python_sdk.apis.paths._1_0_calendar_requests_request_id_detail import Model10CalendarRequestsRequestIdDetail
from officient_python_sdk.apis.paths._1_0_custom_fields_custom_field_id_object_type_object_id import Model10CustomFieldsCustomFieldIdObjectTypeObjectId
from officient_python_sdk.apis.paths._1_0_custom_fields_list import Model10CustomFieldsList
from officient_python_sdk.apis.paths._1_0_people_person_id_photo import Model10PeoplePersonIdPhoto
from officient_python_sdk.apis.paths._1_0_documents_file_id import Model10DocumentsFileId
from officient_python_sdk.apis.paths._1_0_wages_one_off_components_person_id_options_list import Model10WagesOneOffComponentsPersonIdOptionsList
from officient_python_sdk.apis.paths._1_0_wages_one_off_components_person_id_year_month_list import Model10WagesOneOffComponentsPersonIdYearMonthList
from officient_python_sdk.apis.paths._1_0_wages_one_off_components_add import Model10WagesOneOffComponentsAdd
from officient_python_sdk.apis.paths._1_0_wages_one_off_components_granted_component_id import Model10WagesOneOffComponentsGrantedComponentId
from officient_python_sdk.apis.paths._1_0_performance_reviews_person_id_list import Model10PerformanceReviewsPersonIdList
from officient_python_sdk.apis.paths._1_0_legal_dimonas_person_id_list import Model10LegalDimonasPersonIdList
from officient_python_sdk.apis.paths._1_0_calendar_state_lock import Model10CalendarStateLock
from officient_python_sdk.apis.paths._1_0_budgets_budget_id import Model10BudgetsBudgetId
from officient_python_sdk.apis.paths._1_0_budgets_add import Model10BudgetsAdd
from officient_python_sdk.apis.paths._1_0_budgets_budget_id_items_item_id import Model10BudgetsBudgetIdItemsItemId
from officient_python_sdk.apis.paths._1_0_budgets_budget_id_items_add import Model10BudgetsBudgetIdItemsAdd
from officient_python_sdk.apis.paths._1_0_budgets_people_person_id_year_list import Model10BudgetsPeoplePersonIdYearList
from officient_python_sdk.apis.paths._1_0_budgets_people_person_id_budget_id_items_list import Model10BudgetsPeoplePersonIdBudgetIdItemsList
from officient_python_sdk.apis.paths._1_0_calendar_events_priorityschemes_year import Model10CalendarEventsPriorityschemesYear
from officient_python_sdk.apis.paths._1_0_calendar_person_id_priorityschemes_events_add import Model10CalendarPersonIdPriorityschemesEventsAdd
from officient_python_sdk.apis.paths._1_0_roles_person_id_history import Model10RolesPersonIdHistory
from officient_python_sdk.apis.paths._1_0_people_change_history import Model10PeopleChangeHistory
from officient_python_sdk.apis.paths._1_0_calendar_person_id_verzuim_year import Model10CalendarPersonIdVerzuimYear
from officient_python_sdk.apis.paths._1_0_people_person_id_custom_fields import Model10PeoplePersonIdCustomFields
from officient_python_sdk.apis.paths._1_0_people_person_id_weekly_schedule_current import Model10PeoplePersonIdWeeklyScheduleCurrent
from officient_python_sdk.apis.paths._1_0_expenses_list_year_month import Model10ExpensesListYearMonth
from officient_python_sdk.apis.paths._1_0_expenses_categories_list import Model10ExpensesCategoriesList
from officient_python_sdk.apis.paths._1_0_expenses_expense_id_detail import Model10ExpensesExpenseIdDetail
from officient_python_sdk.apis.paths._1_0_expenses_add import Model10ExpensesAdd
from officient_python_sdk.apis.paths._1_0_expenses_expense_id import Model10ExpensesExpenseId
from officient_python_sdk.apis.paths._1_0_expenses_categories_category_id import Model10ExpensesCategoriesCategoryId
from officient_python_sdk.apis.paths._1_0_expenses_expense_id_update_payout import Model10ExpensesExpenseIdUpdatePayout
from officient_python_sdk.apis.paths._1_0_expenses_categories_add import Model10ExpensesCategoriesAdd
from officient_python_sdk.apis.paths._1_0_expenses_categories_category_id_detail import Model10ExpensesCategoriesCategoryIdDetail
from officient_python_sdk.apis.paths._1_0_expenses_list_year import Model10ExpensesListYear
from officient_python_sdk.apis.paths._1_0_wages_functions_list import Model10WagesFunctionsList
from officient_python_sdk.apis.paths._1_0_wages_functions_detail_internal_code import Model10WagesFunctionsDetailInternalCode
from officient_python_sdk.apis.paths._1_0_wages_departments_list import Model10WagesDepartmentsList
from officient_python_sdk.apis.paths._1_0_wages_departments_detail_internal_code import Model10WagesDepartmentsDetailInternalCode
from officient_python_sdk.apis.paths._1_0_wages_cost_units_list import Model10WagesCostUnitsList
from officient_python_sdk.apis.paths._1_0_wages_cost_units_detail_internal_code import Model10WagesCostUnitsDetailInternalCode
from officient_python_sdk.apis.paths._1_0_wages_cost_centers_list import Model10WagesCostCentersList
from officient_python_sdk.apis.paths._1_0_wages_cost_centers_detail_internal_code import Model10WagesCostCentersDetailInternalCode

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues._1_0_PEOPLE_LIST: Model10PeopleList,
        PathValues._1_0_TOKEN: Model10Token,
        PathValues._1_0_WAGES_PERSON_ID_CURRENT: Model10WagesPersonIdCurrent,
        PathValues._1_0_PEOPLE_SELFSERVICE_INVITE_LINK: Model10PeopleSelfserviceInviteLink,
        PathValues._1_0_WAGES_PERSON_ID_HISTORY: Model10WagesPersonIdHistory,
        PathValues._1_0_ASSETS_LIST: Model10AssetsList,
        PathValues._1_0_ASSETS_ASSET_ID_DETAIL: Model10AssetsAssetIdDetail,
        PathValues._1_0_FLEET_VEHICLE_ID_DETAIL: Model10FleetVehicleIdDetail,
        PathValues._1_0_FLEET_LIST: Model10FleetList,
        PathValues._1_0_CONTRACTS_LIST: Model10ContractsList,
        PathValues._1_0_CONTRACTS_CONTRACT_ID_DETAIL: Model10ContractsContractIdDetail,
        PathValues._1_0_CONTRACTS_CONTRACT_ID_PDF: Model10ContractsContractIdPdf,
        PathValues._1_0_CALENDAR_PERSON_ID_YEAR_MONTH: Model10CalendarPersonIdYearMonth,
        PathValues._1_0_TEAMS_LIST: Model10TeamsList,
        PathValues._1_0_PEOPLE_ADD: Model10PeopleAdd,
        PathValues._1_0_CALENDAR_EVENTS_TYPES_YEAR: Model10CalendarEventsTypesYear,
        PathValues._1_0_CALENDAR_PERSON_ID_EVENTS_ADD: Model10CalendarPersonIdEventsAdd,
        PathValues._1_0_CALENDAR_PERSON_ID_EVENTS_EVENT_ID: Model10CalendarPersonIdEventsEventId,
        PathValues._1_0_CALENDAR_PERSON_ID_YEAR_MONTH_DAY_WORK: Model10CalendarPersonIdYearMonthDayWork,
        PathValues._1_0_CALENDAR_PERSON_ID_YEAR_MONTH_DAY_WORK_RESET: Model10CalendarPersonIdYearMonthDayWorkReset,
        PathValues._1_0_PEOPLE_PERSON_ID_DETAIL: Model10PeoplePersonIdDetail,
        PathValues._1_0_DOCUMENTS_OBJECT_TYPE_OBJECT_ID_LIST: Model10DocumentsObjectTypeObjectIdList,
        PathValues._1_0_DOCUMENTS_FILE_ID_DOWNLOAD: Model10DocumentsFileIdDownload,
        PathValues._1_0_DOCUMENTS_OBJECT_TYPE_OBJECT_ID_ADD: Model10DocumentsObjectTypeObjectIdAdd,
        PathValues._1_0_WEBHOOKS_ADD: Model10WebhooksAdd,
        PathValues._1_0_WEBHOOKS_WEBHOOK_ID: Model10WebhooksWebhookId,
        PathValues._1_0_WEBHOOKS_LIST: Model10WebhooksList,
        PathValues._1_0_ACCOUNT: Model10Account,
        PathValues._1_0_CONTRACTS_ADD: Model10ContractsAdd,
        PathValues._1_0_CONTRACTS_SIGNATURE_REQUEST: Model10ContractsSignatureRequest,
        PathValues._1_0_CALENDAR_PERSON_ID_EVENTS_TYPES_YEAR_LIMITS: Model10CalendarPersonIdEventsTypesYearLimits,
        PathValues._1_0_CALENDAR_PERSON_ID_EVENTS_TYPES_YEAR_LIMITS_TYPE_ID_SET: Model10CalendarPersonIdEventsTypesYearLimitsTypeIdSet,
        PathValues._1_0_PEOPLE_SEARCH: Model10PeopleSearch,
        PathValues._1_0_CALENDAR_PERSON_ID_YEAR_WORK_BULK: Model10CalendarPersonIdYearWorkBulk,
        PathValues._1_0_PEOPLE_PERSON_ID_MANAGER: Model10PeoplePersonIdManager,
        PathValues._1_0_CALENDAR_PERSON_ID_YEAR_MONTH_DAY_EVENTS_SET: Model10CalendarPersonIdYearMonthDayEventsSet,
        PathValues._1_0_CALENDAR_PERSON_ID_YEAR_MONTH_DAY: Model10CalendarPersonIdYearMonthDay,
        PathValues._1_0_PEOPLE_PERSON_ID_ROLE: Model10PeoplePersonIdRole,
        PathValues._1_0_TEAMS_TEAM_ID: Model10TeamsTeamId,
        PathValues._1_0_TEAMS_ADD: Model10TeamsAdd,
        PathValues._1_0_ASSETS_TYPES_LIST: Model10AssetsTypesList,
        PathValues._1_0_ASSETS_TYPES_ADD: Model10AssetsTypesAdd,
        PathValues._1_0_ASSETS_TYPES_ASSET_TYPE_ID: Model10AssetsTypesAssetTypeId,
        PathValues._1_0_ASSETS_ADD: Model10AssetsAdd,
        PathValues._1_0_ASSETS_ASSET_ID: Model10AssetsAssetId,
        PathValues._1_0_FLEET_ADD: Model10FleetAdd,
        PathValues._1_0_FLEET_VEHICLE_ID: Model10FleetVehicleId,
        PathValues._1_0_CALENDAR_PERSON_ID_YEAR: Model10CalendarPersonIdYear,
        PathValues._1_0_CALENDAR_REQUESTS_LIST: Model10CalendarRequestsList,
        PathValues._1_0_CALENDAR_REQUESTS_REQUEST_ID_DETAIL: Model10CalendarRequestsRequestIdDetail,
        PathValues._1_0_CUSTOM_FIELDS_CUSTOM_FIELD_ID_OBJECT_TYPE_OBJECT_ID: Model10CustomFieldsCustomFieldIdObjectTypeObjectId,
        PathValues._1_0_CUSTOM_FIELDS_LIST: Model10CustomFieldsList,
        PathValues._1_0_PEOPLE_PERSON_ID_PHOTO: Model10PeoplePersonIdPhoto,
        PathValues._1_0_DOCUMENTS_FILE_ID: Model10DocumentsFileId,
        PathValues._1_0_WAGES_ONE_OFF_COMPONENTS_PERSON_ID_OPTIONS_LIST: Model10WagesOneOffComponentsPersonIdOptionsList,
        PathValues._1_0_WAGES_ONE_OFF_COMPONENTS_PERSON_ID_YEAR_MONTH_LIST: Model10WagesOneOffComponentsPersonIdYearMonthList,
        PathValues._1_0_WAGES_ONE_OFF_COMPONENTS_ADD: Model10WagesOneOffComponentsAdd,
        PathValues._1_0_WAGES_ONE_OFF_COMPONENTS_GRANTED_COMPONENT_ID: Model10WagesOneOffComponentsGrantedComponentId,
        PathValues._1_0_PERFORMANCE_REVIEWS_PERSON_ID_LIST: Model10PerformanceReviewsPersonIdList,
        PathValues._1_0_LEGAL_DIMONAS_PERSON_ID_LIST: Model10LegalDimonasPersonIdList,
        PathValues._1_0_CALENDAR_STATE_LOCK: Model10CalendarStateLock,
        PathValues._1_0_BUDGETS_BUDGET_ID: Model10BudgetsBudgetId,
        PathValues._1_0_BUDGETS_ADD: Model10BudgetsAdd,
        PathValues._1_0_BUDGETS_BUDGET_ID_ITEMS_ITEM_ID: Model10BudgetsBudgetIdItemsItemId,
        PathValues._1_0_BUDGETS_BUDGET_ID_ITEMS_ADD: Model10BudgetsBudgetIdItemsAdd,
        PathValues._1_0_BUDGETS_PEOPLE_PERSON_ID_YEAR_LIST: Model10BudgetsPeoplePersonIdYearList,
        PathValues._1_0_BUDGETS_PEOPLE_PERSON_ID_BUDGET_ID_ITEMS_LIST: Model10BudgetsPeoplePersonIdBudgetIdItemsList,
        PathValues._1_0_CALENDAR_EVENTS_PRIORITYSCHEMES_YEAR: Model10CalendarEventsPriorityschemesYear,
        PathValues._1_0_CALENDAR_PERSON_ID_PRIORITYSCHEMES_EVENTS_ADD: Model10CalendarPersonIdPriorityschemesEventsAdd,
        PathValues._1_0_ROLES_PERSON_ID_HISTORY: Model10RolesPersonIdHistory,
        PathValues._1_0_PEOPLE_CHANGE_HISTORY: Model10PeopleChangeHistory,
        PathValues._1_0_CALENDAR_PERSON_ID_VERZUIM_YEAR: Model10CalendarPersonIdVerzuimYear,
        PathValues._1_0_PEOPLE_PERSON_ID_CUSTOM_FIELDS: Model10PeoplePersonIdCustomFields,
        PathValues._1_0_PEOPLE_PERSON_ID_WEEKLY_SCHEDULE_CURRENT: Model10PeoplePersonIdWeeklyScheduleCurrent,
        PathValues._1_0_EXPENSES_LIST_YEAR_MONTH: Model10ExpensesListYearMonth,
        PathValues._1_0_EXPENSES_CATEGORIES_LIST: Model10ExpensesCategoriesList,
        PathValues._1_0_EXPENSES_EXPENSE_ID_DETAIL: Model10ExpensesExpenseIdDetail,
        PathValues._1_0_EXPENSES_ADD: Model10ExpensesAdd,
        PathValues._1_0_EXPENSES_EXPENSE_ID: Model10ExpensesExpenseId,
        PathValues._1_0_EXPENSES_CATEGORIES_CATEGORY_ID: Model10ExpensesCategoriesCategoryId,
        PathValues._1_0_EXPENSES_EXPENSE_ID_UPDATE_PAYOUT: Model10ExpensesExpenseIdUpdatePayout,
        PathValues._1_0_EXPENSES_CATEGORIES_ADD: Model10ExpensesCategoriesAdd,
        PathValues._1_0_EXPENSES_CATEGORIES_CATEGORY_ID_DETAIL: Model10ExpensesCategoriesCategoryIdDetail,
        PathValues._1_0_EXPENSES_LIST_YEAR: Model10ExpensesListYear,
        PathValues._1_0_WAGES_FUNCTIONS_LIST: Model10WagesFunctionsList,
        PathValues._1_0_WAGES_FUNCTIONS_DETAIL_INTERNAL_CODE: Model10WagesFunctionsDetailInternalCode,
        PathValues._1_0_WAGES_DEPARTMENTS_LIST: Model10WagesDepartmentsList,
        PathValues._1_0_WAGES_DEPARTMENTS_DETAIL_INTERNAL_CODE: Model10WagesDepartmentsDetailInternalCode,
        PathValues._1_0_WAGES_COST_UNITS_LIST: Model10WagesCostUnitsList,
        PathValues._1_0_WAGES_COST_UNITS_DETAIL_INTERNAL_CODE: Model10WagesCostUnitsDetailInternalCode,
        PathValues._1_0_WAGES_COST_CENTERS_LIST: Model10WagesCostCentersList,
        PathValues._1_0_WAGES_COST_CENTERS_DETAIL_INTERNAL_CODE: Model10WagesCostCentersDetailInternalCode,
    }
)

path_to_api = PathToApi(
    {
        PathValues._1_0_PEOPLE_LIST: Model10PeopleList,
        PathValues._1_0_TOKEN: Model10Token,
        PathValues._1_0_WAGES_PERSON_ID_CURRENT: Model10WagesPersonIdCurrent,
        PathValues._1_0_PEOPLE_SELFSERVICE_INVITE_LINK: Model10PeopleSelfserviceInviteLink,
        PathValues._1_0_WAGES_PERSON_ID_HISTORY: Model10WagesPersonIdHistory,
        PathValues._1_0_ASSETS_LIST: Model10AssetsList,
        PathValues._1_0_ASSETS_ASSET_ID_DETAIL: Model10AssetsAssetIdDetail,
        PathValues._1_0_FLEET_VEHICLE_ID_DETAIL: Model10FleetVehicleIdDetail,
        PathValues._1_0_FLEET_LIST: Model10FleetList,
        PathValues._1_0_CONTRACTS_LIST: Model10ContractsList,
        PathValues._1_0_CONTRACTS_CONTRACT_ID_DETAIL: Model10ContractsContractIdDetail,
        PathValues._1_0_CONTRACTS_CONTRACT_ID_PDF: Model10ContractsContractIdPdf,
        PathValues._1_0_CALENDAR_PERSON_ID_YEAR_MONTH: Model10CalendarPersonIdYearMonth,
        PathValues._1_0_TEAMS_LIST: Model10TeamsList,
        PathValues._1_0_PEOPLE_ADD: Model10PeopleAdd,
        PathValues._1_0_CALENDAR_EVENTS_TYPES_YEAR: Model10CalendarEventsTypesYear,
        PathValues._1_0_CALENDAR_PERSON_ID_EVENTS_ADD: Model10CalendarPersonIdEventsAdd,
        PathValues._1_0_CALENDAR_PERSON_ID_EVENTS_EVENT_ID: Model10CalendarPersonIdEventsEventId,
        PathValues._1_0_CALENDAR_PERSON_ID_YEAR_MONTH_DAY_WORK: Model10CalendarPersonIdYearMonthDayWork,
        PathValues._1_0_CALENDAR_PERSON_ID_YEAR_MONTH_DAY_WORK_RESET: Model10CalendarPersonIdYearMonthDayWorkReset,
        PathValues._1_0_PEOPLE_PERSON_ID_DETAIL: Model10PeoplePersonIdDetail,
        PathValues._1_0_DOCUMENTS_OBJECT_TYPE_OBJECT_ID_LIST: Model10DocumentsObjectTypeObjectIdList,
        PathValues._1_0_DOCUMENTS_FILE_ID_DOWNLOAD: Model10DocumentsFileIdDownload,
        PathValues._1_0_DOCUMENTS_OBJECT_TYPE_OBJECT_ID_ADD: Model10DocumentsObjectTypeObjectIdAdd,
        PathValues._1_0_WEBHOOKS_ADD: Model10WebhooksAdd,
        PathValues._1_0_WEBHOOKS_WEBHOOK_ID: Model10WebhooksWebhookId,
        PathValues._1_0_WEBHOOKS_LIST: Model10WebhooksList,
        PathValues._1_0_ACCOUNT: Model10Account,
        PathValues._1_0_CONTRACTS_ADD: Model10ContractsAdd,
        PathValues._1_0_CONTRACTS_SIGNATURE_REQUEST: Model10ContractsSignatureRequest,
        PathValues._1_0_CALENDAR_PERSON_ID_EVENTS_TYPES_YEAR_LIMITS: Model10CalendarPersonIdEventsTypesYearLimits,
        PathValues._1_0_CALENDAR_PERSON_ID_EVENTS_TYPES_YEAR_LIMITS_TYPE_ID_SET: Model10CalendarPersonIdEventsTypesYearLimitsTypeIdSet,
        PathValues._1_0_PEOPLE_SEARCH: Model10PeopleSearch,
        PathValues._1_0_CALENDAR_PERSON_ID_YEAR_WORK_BULK: Model10CalendarPersonIdYearWorkBulk,
        PathValues._1_0_PEOPLE_PERSON_ID_MANAGER: Model10PeoplePersonIdManager,
        PathValues._1_0_CALENDAR_PERSON_ID_YEAR_MONTH_DAY_EVENTS_SET: Model10CalendarPersonIdYearMonthDayEventsSet,
        PathValues._1_0_CALENDAR_PERSON_ID_YEAR_MONTH_DAY: Model10CalendarPersonIdYearMonthDay,
        PathValues._1_0_PEOPLE_PERSON_ID_ROLE: Model10PeoplePersonIdRole,
        PathValues._1_0_TEAMS_TEAM_ID: Model10TeamsTeamId,
        PathValues._1_0_TEAMS_ADD: Model10TeamsAdd,
        PathValues._1_0_ASSETS_TYPES_LIST: Model10AssetsTypesList,
        PathValues._1_0_ASSETS_TYPES_ADD: Model10AssetsTypesAdd,
        PathValues._1_0_ASSETS_TYPES_ASSET_TYPE_ID: Model10AssetsTypesAssetTypeId,
        PathValues._1_0_ASSETS_ADD: Model10AssetsAdd,
        PathValues._1_0_ASSETS_ASSET_ID: Model10AssetsAssetId,
        PathValues._1_0_FLEET_ADD: Model10FleetAdd,
        PathValues._1_0_FLEET_VEHICLE_ID: Model10FleetVehicleId,
        PathValues._1_0_CALENDAR_PERSON_ID_YEAR: Model10CalendarPersonIdYear,
        PathValues._1_0_CALENDAR_REQUESTS_LIST: Model10CalendarRequestsList,
        PathValues._1_0_CALENDAR_REQUESTS_REQUEST_ID_DETAIL: Model10CalendarRequestsRequestIdDetail,
        PathValues._1_0_CUSTOM_FIELDS_CUSTOM_FIELD_ID_OBJECT_TYPE_OBJECT_ID: Model10CustomFieldsCustomFieldIdObjectTypeObjectId,
        PathValues._1_0_CUSTOM_FIELDS_LIST: Model10CustomFieldsList,
        PathValues._1_0_PEOPLE_PERSON_ID_PHOTO: Model10PeoplePersonIdPhoto,
        PathValues._1_0_DOCUMENTS_FILE_ID: Model10DocumentsFileId,
        PathValues._1_0_WAGES_ONE_OFF_COMPONENTS_PERSON_ID_OPTIONS_LIST: Model10WagesOneOffComponentsPersonIdOptionsList,
        PathValues._1_0_WAGES_ONE_OFF_COMPONENTS_PERSON_ID_YEAR_MONTH_LIST: Model10WagesOneOffComponentsPersonIdYearMonthList,
        PathValues._1_0_WAGES_ONE_OFF_COMPONENTS_ADD: Model10WagesOneOffComponentsAdd,
        PathValues._1_0_WAGES_ONE_OFF_COMPONENTS_GRANTED_COMPONENT_ID: Model10WagesOneOffComponentsGrantedComponentId,
        PathValues._1_0_PERFORMANCE_REVIEWS_PERSON_ID_LIST: Model10PerformanceReviewsPersonIdList,
        PathValues._1_0_LEGAL_DIMONAS_PERSON_ID_LIST: Model10LegalDimonasPersonIdList,
        PathValues._1_0_CALENDAR_STATE_LOCK: Model10CalendarStateLock,
        PathValues._1_0_BUDGETS_BUDGET_ID: Model10BudgetsBudgetId,
        PathValues._1_0_BUDGETS_ADD: Model10BudgetsAdd,
        PathValues._1_0_BUDGETS_BUDGET_ID_ITEMS_ITEM_ID: Model10BudgetsBudgetIdItemsItemId,
        PathValues._1_0_BUDGETS_BUDGET_ID_ITEMS_ADD: Model10BudgetsBudgetIdItemsAdd,
        PathValues._1_0_BUDGETS_PEOPLE_PERSON_ID_YEAR_LIST: Model10BudgetsPeoplePersonIdYearList,
        PathValues._1_0_BUDGETS_PEOPLE_PERSON_ID_BUDGET_ID_ITEMS_LIST: Model10BudgetsPeoplePersonIdBudgetIdItemsList,
        PathValues._1_0_CALENDAR_EVENTS_PRIORITYSCHEMES_YEAR: Model10CalendarEventsPriorityschemesYear,
        PathValues._1_0_CALENDAR_PERSON_ID_PRIORITYSCHEMES_EVENTS_ADD: Model10CalendarPersonIdPriorityschemesEventsAdd,
        PathValues._1_0_ROLES_PERSON_ID_HISTORY: Model10RolesPersonIdHistory,
        PathValues._1_0_PEOPLE_CHANGE_HISTORY: Model10PeopleChangeHistory,
        PathValues._1_0_CALENDAR_PERSON_ID_VERZUIM_YEAR: Model10CalendarPersonIdVerzuimYear,
        PathValues._1_0_PEOPLE_PERSON_ID_CUSTOM_FIELDS: Model10PeoplePersonIdCustomFields,
        PathValues._1_0_PEOPLE_PERSON_ID_WEEKLY_SCHEDULE_CURRENT: Model10PeoplePersonIdWeeklyScheduleCurrent,
        PathValues._1_0_EXPENSES_LIST_YEAR_MONTH: Model10ExpensesListYearMonth,
        PathValues._1_0_EXPENSES_CATEGORIES_LIST: Model10ExpensesCategoriesList,
        PathValues._1_0_EXPENSES_EXPENSE_ID_DETAIL: Model10ExpensesExpenseIdDetail,
        PathValues._1_0_EXPENSES_ADD: Model10ExpensesAdd,
        PathValues._1_0_EXPENSES_EXPENSE_ID: Model10ExpensesExpenseId,
        PathValues._1_0_EXPENSES_CATEGORIES_CATEGORY_ID: Model10ExpensesCategoriesCategoryId,
        PathValues._1_0_EXPENSES_EXPENSE_ID_UPDATE_PAYOUT: Model10ExpensesExpenseIdUpdatePayout,
        PathValues._1_0_EXPENSES_CATEGORIES_ADD: Model10ExpensesCategoriesAdd,
        PathValues._1_0_EXPENSES_CATEGORIES_CATEGORY_ID_DETAIL: Model10ExpensesCategoriesCategoryIdDetail,
        PathValues._1_0_EXPENSES_LIST_YEAR: Model10ExpensesListYear,
        PathValues._1_0_WAGES_FUNCTIONS_LIST: Model10WagesFunctionsList,
        PathValues._1_0_WAGES_FUNCTIONS_DETAIL_INTERNAL_CODE: Model10WagesFunctionsDetailInternalCode,
        PathValues._1_0_WAGES_DEPARTMENTS_LIST: Model10WagesDepartmentsList,
        PathValues._1_0_WAGES_DEPARTMENTS_DETAIL_INTERNAL_CODE: Model10WagesDepartmentsDetailInternalCode,
        PathValues._1_0_WAGES_COST_UNITS_LIST: Model10WagesCostUnitsList,
        PathValues._1_0_WAGES_COST_UNITS_DETAIL_INTERNAL_CODE: Model10WagesCostUnitsDetailInternalCode,
        PathValues._1_0_WAGES_COST_CENTERS_LIST: Model10WagesCostCentersList,
        PathValues._1_0_WAGES_COST_CENTERS_DETAIL_INTERNAL_CODE: Model10WagesCostCentersDetailInternalCode,
    }
)
