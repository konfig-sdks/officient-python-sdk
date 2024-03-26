<div align="left">

[![Visit Officient](./header.png)](https://officient.io)

# Officient<a id="officient"></a>

Officient offers an intuitive HRIS which helps manage all personnel administration through our HR platform & personalized employee self-services. Manage payroll, company assets, contracts, days off, fleet, performance reviews and all employee data in one HR system. HR deserves great software and we're here to provide it.

We support our customers in transforming HR towards paperless administration and automating tedious workforce management tasks in the process. Our goal? Transform HR from an administrative, processing role, to a controlling role which fuels HR strategy across the organization.


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`officient.account.get_information`](#officientaccountget_information)
  * [`officient.asset.add_custom_type`](#officientassetadd_custom_type)
  * [`officient.asset.create_new_asset`](#officientassetcreate_new_asset)
  * [`officient.asset.get_custom_types_list`](#officientassetget_custom_types_list)
  * [`officient.asset.get_detail`](#officientassetget_detail)
  * [`officient.asset.list_assets`](#officientassetlist_assets)
  * [`officient.asset.remove`](#officientassetremove)
  * [`officient.asset.remove_custom_type`](#officientassetremove_custom_type)
  * [`officient.asset.update_asset`](#officientassetupdate_asset)
  * [`officient.authentication.get_access_token`](#officientauthenticationget_access_token)
  * [`officient.budget.add_budget_item`](#officientbudgetadd_budget_item)
  * [`officient.budget.add_item`](#officientbudgetadd_item)
  * [`officient.budget.delete_budget_by_id`](#officientbudgetdelete_budget_by_id)
  * [`officient.budget.remove_item`](#officientbudgetremove_item)
  * [`officient.budget.update_budget_item`](#officientbudgetupdate_budget_item)
  * [`officient.calendar_request.get_detail_by_id`](#officientcalendar_requestget_detail_by_id)
  * [`officient.calendar_request.list_requests`](#officientcalendar_requestlist_requests)
  * [`officient.calendar_state.unlock_month_processed`](#officientcalendar_stateunlock_month_processed)
  * [`officient.component.grant_one_off_wage`](#officientcomponentgrant_one_off_wage)
  * [`officient.component.remove_one_off_wage`](#officientcomponentremove_one_off_wage)
  * [`officient.contract.create_new_contract`](#officientcontractcreate_new_contract)
  * [`officient.contract.get_all`](#officientcontractget_all)
  * [`officient.contract.get_detail`](#officientcontractget_detail)
  * [`officient.contract.get_pdf_link`](#officientcontractget_pdf_link)
  * [`officient.contract.request_signature`](#officientcontractrequest_signature)
  * [`officient.cost_center.detail_get`](#officientcost_centerdetail_get)
  * [`officient.cost_center.get_list`](#officientcost_centerget_list)
  * [`officient.cost_unit.get_functions_detail`](#officientcost_unitget_functions_detail)
  * [`officient.cost_unit.list_functions`](#officientcost_unitlist_functions)
  * [`officient.custom_event_type.get_list`](#officientcustom_event_typeget_list)
  * [`officient.custom_field.edit_value_for_object`](#officientcustom_fieldedit_value_for_object)
  * [`officient.custom_field.list_fields`](#officientcustom_fieldlist_fields)
  * [`officient.department.get_all_departments`](#officientdepartmentget_all_departments)
  * [`officient.department.get_detail`](#officientdepartmentget_detail)
  * [`officient.document.get_download_url`](#officientdocumentget_download_url)
  * [`officient.document.list_related`](#officientdocumentlist_related)
  * [`officient.document.remove`](#officientdocumentremove)
  * [`officient.document.upload_document`](#officientdocumentupload_document)
  * [`officient.expense.add_category`](#officientexpenseadd_category)
  * [`officient.expense.add_expense_with_category`](#officientexpenseadd_expense_with_category)
  * [`officient.expense.delete_by_id`](#officientexpensedelete_by_id)
  * [`officient.expense.delete_category`](#officientexpensedelete_category)
  * [`officient.expense.edit_category_name`](#officientexpenseedit_category_name)
  * [`officient.expense.get_detail`](#officientexpenseget_detail)
  * [`officient.expense.list_by_category_detail`](#officientexpenselist_by_category_detail)
  * [`officient.expense.list_by_month`](#officientexpenselist_by_month)
  * [`officient.expense.list_by_year`](#officientexpenselist_by_year)
  * [`officient.expense.list_categories`](#officientexpenselist_categories)
  * [`officient.expense.set_payout_method_and_status`](#officientexpenseset_payout_method_and_status)
  * [`officient.expense.update_details`](#officientexpenseupdate_details)
  * [`officient.function.get_all_functions`](#officientfunctionget_all_functions)
  * [`officient.function.get_details`](#officientfunctionget_details)
  * [`officient.invitation.generate_secret_url`](#officientinvitationgenerate_secret_url)
  * [`officient.person.add_new`](#officientpersonadd_new)
  * [`officient.person.add_to_calendar`](#officientpersonadd_to_calendar)
  * [`officient.person.add_to_calendar_0`](#officientpersonadd_to_calendar_0)
  * [`officient.person.edit_detail`](#officientpersonedit_detail)
  * [`officient.person.get_budgets_by_year`](#officientpersonget_budgets_by_year)
  * [`officient.person.get_current_wage`](#officientpersonget_current_wage)
  * [`officient.person.get_current_weekly_schedule`](#officientpersonget_current_weekly_schedule)
  * [`officient.person.get_custom_fields`](#officientpersonget_custom_fields)
  * [`officient.person.get_daily_calendar`](#officientpersonget_daily_calendar)
  * [`officient.person.get_detail`](#officientpersonget_detail)
  * [`officient.person.get_event_type_limits`](#officientpersonget_event_type_limits)
  * [`officient.person.get_manager_details`](#officientpersonget_manager_details)
  * [`officient.person.get_monthly_calendar`](#officientpersonget_monthly_calendar)
  * [`officient.person.get_one_off_wage_components_by_month`](#officientpersonget_one_off_wage_components_by_month)
  * [`officient.person.get_performance_reviews_by_person`](#officientpersonget_performance_reviews_by_person)
  * [`officient.person.get_personal_data_changes`](#officientpersonget_personal_data_changes)
  * [`officient.person.get_verzuim_periods`](#officientpersonget_verzuim_periods)
  * [`officient.person.get_wage_history`](#officientpersonget_wage_history)
  * [`officient.person.get_yearly_calendar`](#officientpersonget_yearly_calendar)
  * [`officient.person.list_available_components`](#officientpersonlist_available_components)
  * [`officient.person.list_budget_items`](#officientpersonlist_budget_items)
  * [`officient.person.list_dimonas_by_person`](#officientpersonlist_dimonas_by_person)
  * [`officient.person.list_people`](#officientpersonlist_people)
  * [`officient.person.overwrite_event`](#officientpersonoverwrite_event)
  * [`officient.person.remove_event`](#officientpersonremove_event)
  * [`officient.person.reset_time_worked`](#officientpersonreset_time_worked)
  * [`officient.person.search_by_criteria`](#officientpersonsearch_by_criteria)
  * [`officient.person.set_function_description`](#officientpersonset_function_description)
  * [`officient.person.update_bulk_time_worked`](#officientpersonupdate_bulk_time_worked)
  * [`officient.person.update_event_type_limit`](#officientpersonupdate_event_type_limit)
  * [`officient.person.update_manager`](#officientpersonupdate_manager)
  * [`officient.person.update_time_worked`](#officientpersonupdate_time_worked)
  * [`officient.person.upload_avatar`](#officientpersonupload_avatar)
  * [`officient.person.view_role_history`](#officientpersonview_role_history)
  * [`officient.priority_scheme.list_active_priority_schemes_by_year`](#officientpriority_schemelist_active_priority_schemes_by_year)
  * [`officient.team.create_new_team`](#officientteamcreate_new_team)
  * [`officient.team.edit_information`](#officientteamedit_information)
  * [`officient.team.get_all_teams`](#officientteamget_all_teams)
  * [`officient.vehicle.create_new`](#officientvehiclecreate_new)
  * [`officient.vehicle.edit_details`](#officientvehicleedit_details)
  * [`officient.vehicle.get_all_vehicles`](#officientvehicleget_all_vehicles)
  * [`officient.vehicle.get_detail`](#officientvehicleget_detail)
  * [`officient.webhook.get_active_notifications`](#officientwebhookget_active_notifications)
  * [`officient.webhook.subscribe_notification`](#officientwebhooksubscribe_notification)
  * [`officient.webhook.unsubscribe_notification`](#officientwebhookunsubscribe_notification)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Officient&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from officient_python_sdk import Officient, ApiException

officient = Officient()

try:
    # Your account
    get_information_response = officient.account.get_information()
    print(get_information_response)
except ApiException as e:
    print("Exception when calling AccountApi.get_information: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from officient_python_sdk import Officient, ApiException

officient = Officient()


async def main():
    try:
        # Your account
        get_information_response = await officient.account.aget_information()
        print(get_information_response)
    except ApiException as e:
        print("Exception when calling AccountApi.get_information: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from officient_python_sdk import Officient, ApiException

officient = Officient()

try:
    # Your account
    get_information_response = officient.account.raw.get_information()
    pprint(get_information_response.body)
    pprint(get_information_response.body["data"])
    pprint(get_information_response.headers)
    pprint(get_information_response.status)
    pprint(get_information_response.round_trip_time)
except ApiException as e:
    print("Exception when calling AccountApi.get_information: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `officient.account.get_information`<a id="officientaccountget_information"></a>

This API will reveal information about your own account

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_information_response = officient.account.get_information()
```

#### 🔄 Return<a id="🔄-return"></a>

[`AccountGetInformationResponse`](./officient_python_sdk/pydantic/account_get_information_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/account` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.asset.add_custom_type`<a id="officientassetadd_custom_type"></a>

Add custom asset type

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_custom_type_response = officient.asset.add_custom_type()
```

#### 🔄 Return<a id="🔄-return"></a>

[`AssetAddCustomTypeResponse`](./officient_python_sdk/pydantic/asset_add_custom_type_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/assets/types/add` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.asset.create_new_asset`<a id="officientassetcreate_new_asset"></a>

Add asset

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_asset_response = officient.asset.create_new_asset()
```

#### 🔄 Return<a id="🔄-return"></a>

[`AssetCreateNewAssetResponse`](./officient_python_sdk/pydantic/asset_create_new_asset_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/assets/add` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.asset.get_custom_types_list`<a id="officientassetget_custom_types_list"></a>

List custom asset types

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_custom_types_list_response = officient.asset.get_custom_types_list()
```

#### 🔄 Return<a id="🔄-return"></a>

[`AssetGetCustomTypesListResponse`](./officient_python_sdk/pydantic/asset_get_custom_types_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/assets/types/list` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.asset.get_detail`<a id="officientassetget_detail"></a>

Get details about one asset

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_detail_response = officient.asset.get_detail(
    asset_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### asset_id: `int`<a id="asset_id-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`AssetGetDetailResponse`](./officient_python_sdk/pydantic/asset_get_detail_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/assets/{asset_id}/detail` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.asset.list_assets`<a id="officientassetlist_assets"></a>

List all assets

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_assets_response = officient.asset.list_assets(
    page=0,
    person_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page: `int`<a id="page-int"></a>

Controls pagination (0, 1, 2, ..) to view all results. 30 items per page.

##### person_id: `int`<a id="person_id-int"></a>

view only assets that belong to a specific person

#### 🔄 Return<a id="🔄-return"></a>

[`AssetListAssetsResponse`](./officient_python_sdk/pydantic/asset_list_assets_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/assets/list` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.asset.remove`<a id="officientassetremove"></a>

Delete asset

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_response = officient.asset.remove(
    asset_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### asset_id: `int`<a id="asset_id-int"></a>

The id of the asset that will be deleted

#### 🔄 Return<a id="🔄-return"></a>

[`AssetRemoveResponse`](./officient_python_sdk/pydantic/asset_remove_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/assets/{asset_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.asset.remove_custom_type`<a id="officientassetremove_custom_type"></a>

Delete custom asset type

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_custom_type_response = officient.asset.remove_custom_type(
    asset_type_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### asset_type_id: `int`<a id="asset_type_id-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`AssetRemoveCustomTypeResponse`](./officient_python_sdk/pydantic/asset_remove_custom_type_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/assets/types/{asset_type_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.asset.update_asset`<a id="officientassetupdate_asset"></a>

Edit asset

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_asset_response = officient.asset.update_asset(
    asset_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### asset_id: `int`<a id="asset_id-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`AssetUpdateAssetResponse`](./officient_python_sdk/pydantic/asset_update_asset_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/assets/{asset_id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.authentication.get_access_token`<a id="officientauthenticationget_access_token"></a>

Get access token

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_access_token_response = officient.authentication.get_access_token(
    code="string_example",
    client_id="string_example",
    client_secret="string_example",
    grant_type="string_example",
    refresh_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### code: `str`<a id="code-str"></a>

Authorization code in case of 3 legged oauth flow

##### client_id: `str`<a id="client_id-str"></a>

client_id of your app. Can be found under 'my apps'

##### client_secret: `str`<a id="client_secret-str"></a>

client secret of your app. Can be found under 'my apps'

##### grant_type: `str`<a id="grant_type-str"></a>

should always be either authorization_code or refresh_token

##### refresh_token: `str`<a id="refresh_token-str"></a>

optional

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AuthenticationGetAccessTokenRequest`](./officient_python_sdk/type/authentication_get_access_token_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AuthenticationGetAccessTokenResponse`](./officient_python_sdk/pydantic/authentication_get_access_token_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/token` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.budget.add_budget_item`<a id="officientbudgetadd_budget_item"></a>

Add budget

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_budget_item_response = officient.budget.add_budget_item(
    budget_type="string_example",
    maximum=1,
    year=1,
    employee_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### budget_type: `str`<a id="budget_type-str"></a>

The type of budget.

##### maximum: `int`<a id="maximum-int"></a>

The maximum amount that will be set for the budget.

##### year: `int`<a id="year-int"></a>

The year for which the budget will created.

##### employee_id: `int`<a id="employee_id-int"></a>

The id of the employee for which the budget will be created.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BudgetAddBudgetItemRequest`](./officient_python_sdk/type/budget_add_budget_item_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`BudgetAddBudgetItemResponse`](./officient_python_sdk/pydantic/budget_add_budget_item_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/budgets/add` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.budget.add_item`<a id="officientbudgetadd_item"></a>

Add budget item

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_item_response = officient.budget.add_item(
    budget_id=1,
    item_name="string_example",
    cost=3.14,
    employee_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### budget_id: `int`<a id="budget_id-int"></a>

##### item_name: `str`<a id="item_name-str"></a>

##### cost: `Union[int, float]`<a id="cost-unionint-float"></a>

##### employee_id: `int`<a id="employee_id-int"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BudgetAddItemRequest`](./officient_python_sdk/type/budget_add_item_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`BudgetAddItemResponse`](./officient_python_sdk/pydantic/budget_add_item_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/budgets/{budget_id}/items/add` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.budget.delete_budget_by_id`<a id="officientbudgetdelete_budget_by_id"></a>

Delete budget

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_budget_by_id_response = officient.budget.delete_budget_by_id(
    budget_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### budget_id: `int`<a id="budget_id-int"></a>

The id of the budget that will be deleted

#### 🔄 Return<a id="🔄-return"></a>

[`BudgetDeleteBudgetByIdResponse`](./officient_python_sdk/pydantic/budget_delete_budget_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/budgets/{budget_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.budget.remove_item`<a id="officientbudgetremove_item"></a>

Delete budget item

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_item_response = officient.budget.remove_item(
    budget_id=1,
    item_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### budget_id: `int`<a id="budget_id-int"></a>

##### item_id: `int`<a id="item_id-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`BudgetRemoveItemResponse`](./officient_python_sdk/pydantic/budget_remove_item_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/budgets/{budget_id}/items/{item_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.budget.update_budget_item`<a id="officientbudgetupdate_budget_item"></a>

Edit budget

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_budget_item_response = officient.budget.update_budget_item(
    budget_id=1,
    maximum=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### budget_id: `int`<a id="budget_id-int"></a>

The id of the budget that will be edited.

##### maximum: `int`<a id="maximum-int"></a>

The new maximum amount for the budget.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BudgetUpdateBudgetItemRequest`](./officient_python_sdk/type/budget_update_budget_item_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`BudgetUpdateBudgetItemResponse`](./officient_python_sdk/pydantic/budget_update_budget_item_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/budgets/{budget_id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.calendar_request.get_detail_by_id`<a id="officientcalendar_requestget_detail_by_id"></a>

Calendar request detail

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_detail_by_id_response = officient.calendar_request.get_detail_by_id(
    request_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### request_id: `int`<a id="request_id-int"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/calendar/requests/{request_id}/detail` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.calendar_request.list_requests`<a id="officientcalendar_requestlist_requests"></a>

List calendar requests

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_requests_response = officient.calendar_request.list_requests(
    page="0",
    status="all",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page: `str`<a id="page-str"></a>

##### status: `str`<a id="status-str"></a>

Can be either \"all\", \"pending\" or \"closed\"

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/calendar/requests/list` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.calendar_state.unlock_month_processed`<a id="officientcalendar_stateunlock_month_processed"></a>

Unlock the calendar for a month that has already been processed by your payroll provider. This is usually done to add corrections.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
unlock_month_processed_response = officient.calendar_state.unlock_month_processed(
    disable_lock=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### disable_lock: `bool`<a id="disable_lock-bool"></a>

By disabling the lock, the calendar will become unlocked.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CalendarStateUnlockMonthProcessedRequest`](./officient_python_sdk/type/calendar_state_unlock_month_processed_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CalendarStateUnlockMonthProcessedResponse`](./officient_python_sdk/pydantic/calendar_state_unlock_month_processed_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/calendar/state/lock` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.component.grant_one_off_wage`<a id="officientcomponentgrant_one_off_wage"></a>

Grants a one-off wage components for a specific person, in a specific month

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
grant_one_off_wage_response = officient.component.grant_one_off_wage()
```

#### 🔄 Return<a id="🔄-return"></a>

[`ComponentGrantOneOffWageResponse`](./officient_python_sdk/pydantic/component_grant_one_off_wage_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/wages/one_off/components/add` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.component.remove_one_off_wage`<a id="officientcomponentremove_one_off_wage"></a>

Removes a one-off wage component for a specific person in a specific month, by id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_one_off_wage_response = officient.component.remove_one_off_wage()
```

#### 🔄 Return<a id="🔄-return"></a>

[`ComponentRemoveOneOffWageResponse`](./officient_python_sdk/pydantic/component_remove_one_off_wage_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/wages/one_off/components/{granted_component_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.contract.create_new_contract`<a id="officientcontractcreate_new_contract"></a>

Add contract

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_contract_response = officient.contract.create_new_contract()
```

#### 🔄 Return<a id="🔄-return"></a>

[`ContractCreateNewContractResponse`](./officient_python_sdk/pydantic/contract_create_new_contract_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/contracts/add` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.contract.get_all`<a id="officientcontractget_all"></a>

Get a list of all contracts

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = officient.contract.get_all(
    page=0,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page: `int`<a id="page-int"></a>

Controls pagination (0, 1, 2, ..) to view all results. 30 items per page.

#### 🔄 Return<a id="🔄-return"></a>

[`ContractGetAllResponse`](./officient_python_sdk/pydantic/contract_get_all_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/contracts/list` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.contract.get_detail`<a id="officientcontractget_detail"></a>

Get details about one contract

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_detail_response = officient.contract.get_detail(
    contract_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### contract_id: `int`<a id="contract_id-int"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/contracts/{contract_id}/detail` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.contract.get_pdf_link`<a id="officientcontractget_pdf_link"></a>

Get a PDF download link for any contract

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_pdf_link_response = officient.contract.get_pdf_link(
    contract_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### contract_id: `int`<a id="contract_id-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ContractGetPdfLinkResponse`](./officient_python_sdk/pydantic/contract_get_pdf_link_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/contracts/{contract_id}/pdf` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.contract.request_signature`<a id="officientcontractrequest_signature"></a>

This API sends out an email invite requesting to sign a contract

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
request_signature_response = officient.contract.request_signature()
```

#### 🔄 Return<a id="🔄-return"></a>

[`ContractRequestSignatureResponse`](./officient_python_sdk/pydantic/contract_request_signature_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/contracts/signature/request` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.cost_center.detail_get`<a id="officientcost_centerdetail_get"></a>

Get the details of all functions or that of a single one

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
detail_get_response = officient.cost_center.detail_get(
    internal_code="internal_code_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### internal_code: `str`<a id="internal_code-str"></a>

The internal code / GUID of the function you would like to receive information on

#### 🔄 Return<a id="🔄-return"></a>

[`CostCenterDetailGetResponse`](./officient_python_sdk/pydantic/cost_center_detail_get_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/wages/cost_centers/detail/{internal_code}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.cost_center.get_list`<a id="officientcost_centerget_list"></a>

Get the details of all functions or that of a single one

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_list_response = officient.cost_center.get_list()
```

#### 🔄 Return<a id="🔄-return"></a>

[`CostCenterGetListResponse`](./officient_python_sdk/pydantic/cost_center_get_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/wages/cost_centers/list` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.cost_unit.get_functions_detail`<a id="officientcost_unitget_functions_detail"></a>

Get the details of all functions or that of a single one

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_functions_detail_response = officient.cost_unit.get_functions_detail(
    internal_code="internal_code_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### internal_code: `str`<a id="internal_code-str"></a>

The internal code / GUID of the function you would like to receive information on

#### 🔄 Return<a id="🔄-return"></a>

[`CostUnitGetFunctionsDetailResponse`](./officient_python_sdk/pydantic/cost_unit_get_functions_detail_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/wages/cost_units/detail/{internal_code}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.cost_unit.list_functions`<a id="officientcost_unitlist_functions"></a>

Get the details of all functions or that of a single one

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_functions_response = officient.cost_unit.list_functions()
```

#### 🔄 Return<a id="🔄-return"></a>

[`CostUnitListFunctionsResponse`](./officient_python_sdk/pydantic/cost_unit_list_functions_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/wages/cost_units/list` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.custom_event_type.get_list`<a id="officientcustom_event_typeget_list"></a>

fetch a list of custom event types including time off types, overtime types,..

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_list_response = officient.custom_event_type.get_list(
    year=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### year: `int`<a id="year-int"></a>

the year you want custom event type to be returned for

#### 🔄 Return<a id="🔄-return"></a>

[`CustomEventTypeGetListResponse`](./officient_python_sdk/pydantic/custom_event_type_get_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/calendar/events/types/{year}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.custom_field.edit_value_for_object`<a id="officientcustom_fieldedit_value_for_object"></a>

Update the custom field value for a specific object (either a person, car, asset, contract,..)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
edit_value_for_object_response = officient.custom_field.edit_value_for_object(
    custom_field_id=1,
    object_type="object_type_example",
    object_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### custom_field_id: `int`<a id="custom_field_id-int"></a>

Id of the custom field

##### object_type: `str`<a id="object_type-str"></a>

type of object to be edited. It can be: employee, asset, car, contract, software_license, training_participant, training

##### object_id: `int`<a id="object_id-int"></a>

ID of the object to be edited

#### 🔄 Return<a id="🔄-return"></a>

[`CustomFieldEditValueForObjectResponse`](./officient_python_sdk/pydantic/custom_field_edit_value_for_object_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/custom_fields/{custom_field_id}/{object_type}/{object_id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.custom_field.list_fields`<a id="officientcustom_fieldlist_fields"></a>

List all custom fields in a given account

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_fields_response = officient.custom_field.list_fields()
```

#### 🔄 Return<a id="🔄-return"></a>

[`CustomFieldListFieldsResponse`](./officient_python_sdk/pydantic/custom_field_list_fields_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/custom_fields/list` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.department.get_all_departments`<a id="officientdepartmentget_all_departments"></a>

Get the details of all functions or that of a single one

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_departments_response = officient.department.get_all_departments()
```

#### 🔄 Return<a id="🔄-return"></a>

[`DepartmentGetAllDepartmentsResponse`](./officient_python_sdk/pydantic/department_get_all_departments_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/wages/departments/list` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.department.get_detail`<a id="officientdepartmentget_detail"></a>

Get the details of all functions or that of a single one

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_detail_response = officient.department.get_detail(
    internal_code="internal_code_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### internal_code: `str`<a id="internal_code-str"></a>

The internal code / GUID of the function you would like to receive information on

#### 🔄 Return<a id="🔄-return"></a>

[`DepartmentGetDetailResponse`](./officient_python_sdk/pydantic/department_get_detail_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/wages/departments/detail/{internal_code}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.document.get_download_url`<a id="officientdocumentget_download_url"></a>

This API call returns a download url for a document

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_download_url_response = officient.document.get_download_url(
    file_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### file_id: `int`<a id="file_id-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`DocumentGetDownloadUrlResponse`](./officient_python_sdk/pydantic/document_get_download_url_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/documents/{file_id}/download` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.document.list_related`<a id="officientdocumentlist_related"></a>

This API call lists up all documents related to a specific object

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_related_response = officient.document.list_related(
    object_type="object_type_example",
    object_id=1,
    page=0,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### object_type: `str`<a id="object_type-str"></a>

pick one: employee, asset, car

##### object_id: `int`<a id="object_id-int"></a>

##### page: `int`<a id="page-int"></a>

Controls pagination (0, 1, 2, ..) to view all results. 30 items per page.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/documents/{object_type}/{object_id}/list` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.document.remove`<a id="officientdocumentremove"></a>

Delete document

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_response = officient.document.remove(
    file_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### file_id: `int`<a id="file_id-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`DocumentRemoveResponse`](./officient_python_sdk/pydantic/document_remove_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/documents/{file_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.document.upload_document`<a id="officientdocumentupload_document"></a>

Upload document

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
upload_document_response = officient.document.upload_document(
    object_type="object_type_example",
    object_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### object_type: `str`<a id="object_type-str"></a>

pick one: employee, asset, car

##### object_id: `int`<a id="object_id-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`DocumentUploadDocumentResponse`](./officient_python_sdk/pydantic/document_upload_document_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/documents/{object_type}/{object_id}/add` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.expense.add_category`<a id="officientexpenseadd_category"></a>

The api end-point to add an expense nd an optional category id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_category_response = officient.expense.add_category(
    name="string_example",
    type="total",
    price_per_kilometer=3.14,
    price_per_day=3.14,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

##### type: `str`<a id="type-str"></a>

##### price_per_kilometer: `Union[int, float]`<a id="price_per_kilometer-unionint-float"></a>

##### price_per_day: `Union[int, float]`<a id="price_per_day-unionint-float"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ExpenseAddCategoryRequest`](./officient_python_sdk/type/expense_add_category_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ExpenseAddCategoryResponse`](./officient_python_sdk/pydantic/expense_add_category_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/expenses/categories/add` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.expense.add_expense_with_category`<a id="officientexpenseadd_expense_with_category"></a>

The api end-point to add an expense nd an optional category id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_expense_with_category_response = officient.expense.add_expense_with_category(
    description="string_example",
    employee_id=1,
    category_id=0,
    amount=3.14,
    extra_information="string_example",
    date="string_example",
    filename="string_example",
    file_base64="string_example",
    dates=["string_example"],
    distance=0,
    ride="single",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### description: `str`<a id="description-str"></a>

This is the title for the expense

##### employee_id: `int`<a id="employee_id-int"></a>

##### category_id: `int`<a id="category_id-int"></a>

For some integrations this is required not to be 0 which is the default category id

##### amount: `Union[int, float]`<a id="amount-unionint-float"></a>

this is the price of the expense, this is only required when using a total amount category

##### extra_information: `str`<a id="extra_information-str"></a>

##### date: `str`<a id="date-str"></a>

this is the day the expense has incurred on and is required when it is a total amount category

##### filename: `str`<a id="filename-str"></a>

this is required when you want to add an expense with a total amount category

##### file_base64: `str`<a id="file_base64-str"></a>

this is required when you want to add an expense with a total amount category

##### dates: [`ExpenseAddExpenseWithCategoryRequestDates`](./officient_python_sdk/type/expense_add_expense_with_category_request_dates.py)<a id="dates-expenseaddexpensewithcategoryrequestdatesofficient_python_sdktypeexpense_add_expense_with_category_request_datespy"></a>

##### distance: `int`<a id="distance-int"></a>

this is required when you want to update to a killometer allowance expense category. This is equal to the total amount of kilometers that has been done

##### ride: `str`<a id="ride-str"></a>

this is the value if it's an outward or a round journey when using kilometer allowances, this defaults to single

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ExpenseAddExpenseWithCategoryRequest`](./officient_python_sdk/type/expense_add_expense_with_category_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ExpenseAddExpenseWithCategoryResponse`](./officient_python_sdk/pydantic/expense_add_expense_with_category_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/expenses/add` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.expense.delete_by_id`<a id="officientexpensedelete_by_id"></a>

Delete expense

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_by_id_response = officient.expense.delete_by_id(
    expense_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### expense_id: `int`<a id="expense_id-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ExpenseDeleteByIdResponse`](./officient_python_sdk/pydantic/expense_delete_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/expenses/{expense_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.expense.delete_category`<a id="officientexpensedelete_category"></a>

Delete expense category

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_category_response = officient.expense.delete_category(
    category_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### category_id: `int`<a id="category_id-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ExpenseDeleteCategoryResponse`](./officient_python_sdk/pydantic/expense_delete_category_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/expenses/categories/{category_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.expense.edit_category_name`<a id="officientexpenseedit_category_name"></a>

Edit expense category name

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
edit_category_name_response = officient.expense.edit_category_name(
    name="string_example",
    category_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

##### category_id: `int`<a id="category_id-int"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ExpenseEditCategoryNameRequest`](./officient_python_sdk/type/expense_edit_category_name_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ExpenseEditCategoryNameResponse`](./officient_python_sdk/pydantic/expense_edit_category_name_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/expenses/categories/{category_id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.expense.get_detail`<a id="officientexpenseget_detail"></a>

List all expenses

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_detail_response = officient.expense.get_detail(
    expense_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### expense_id: `int`<a id="expense_id-int"></a>

the specific id we want to see the details about

#### 🔄 Return<a id="🔄-return"></a>

[`ExpenseGetDetailResponse`](./officient_python_sdk/pydantic/expense_get_detail_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/expenses/{expense_id}/detail` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.expense.list_by_category_detail`<a id="officientexpenselist_by_category_detail"></a>

List all expenses

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_by_category_detail_response = officient.expense.list_by_category_detail(
    category_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### category_id: `int`<a id="category_id-int"></a>

the specific id we want to see the details about

#### 🔄 Return<a id="🔄-return"></a>

[`ExpenseListByCategoryDetailResponse`](./officient_python_sdk/pydantic/expense_list_by_category_detail_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/expenses/categories/{category_id}/detail` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.expense.list_by_month`<a id="officientexpenselist_by_month"></a>

List all expenses

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_by_month_response = officient.expense.list_by_month(
    year="year_example",
    month="month_example",
    page="0",
    include_deleted=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### year: `str`<a id="year-str"></a>

the specific year we want to filter

##### month: `str`<a id="month-str"></a>

the specific month we want to filter this is optional

##### page: `str`<a id="page-str"></a>

optional to filter pages

##### include_deleted: `int`<a id="include_deleted-int"></a>

this is so you can exclude any deleted expense, by default we show them (0 - 1)

#### 🔄 Return<a id="🔄-return"></a>

[`ExpenseListByMonthResponse`](./officient_python_sdk/pydantic/expense_list_by_month_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/expenses/list/{year}/{month}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.expense.list_by_year`<a id="officientexpenselist_by_year"></a>

List all expenses

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_by_year_response = officient.expense.list_by_year(
    year="year_example",
    month="month_example",
    page="0",
    include_deleted=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### year: `str`<a id="year-str"></a>

the specific year we want to filter

##### month: `str`<a id="month-str"></a>

the specific month we want to filter this is optional

##### page: `str`<a id="page-str"></a>

optional to filter pages

##### include_deleted: `int`<a id="include_deleted-int"></a>

this is so you can exclude any deleted expense, by default we show them (0 - 1)

#### 🔄 Return<a id="🔄-return"></a>

[`ExpenseListByYearResponse`](./officient_python_sdk/pydantic/expense_list_by_year_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/expenses/list/{year}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.expense.list_categories`<a id="officientexpenselist_categories"></a>

List all expenses

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_categories_response = officient.expense.list_categories()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/expenses/categories/list` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.expense.set_payout_method_and_status`<a id="officientexpenseset_payout_method_and_status"></a>

Set payout method and status

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
set_payout_method_and_status_response = officient.expense.set_payout_method_and_status(
    new_payout_method="UNDECIDED",
    expense_id=1,
    payout_other_reason="string_example",
    payout_status="PAID_OUT",
    period="string_example",
    year="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### new_payout_method: `str`<a id="new_payout_method-str"></a>

##### expense_id: `int`<a id="expense_id-int"></a>

##### payout_other_reason: `str`<a id="payout_other_reason-str"></a>

##### payout_status: `str`<a id="payout_status-str"></a>

This field is required when the \\\"new\\\"payout_method\\\" is either PAYOUT_ACCOUNTING, PAYOUT_OTHER or PAYOUT_MANUALLY

##### period: `str`<a id="period-str"></a>

##### year: `str`<a id="year-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ExpenseSetPayoutMethodAndStatusRequest`](./officient_python_sdk/type/expense_set_payout_method_and_status_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ExpenseSetPayoutMethodAndStatusResponse`](./officient_python_sdk/pydantic/expense_set_payout_method_and_status_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/expenses/{expense_id}/updatePayout` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.expense.update_details`<a id="officientexpenseupdate_details"></a>

Edit expense

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_details_response = officient.expense.update_details(
    category_id=0,
    expense_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### category_id: `int`<a id="category_id-int"></a>

For some integrations this is required not to be 0 which is the default category id

##### expense_id: `int`<a id="expense_id-int"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ExpenseUpdateDetailsRequest`](./officient_python_sdk/type/expense_update_details_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ExpenseUpdateDetailsResponse`](./officient_python_sdk/pydantic/expense_update_details_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/expenses/{expense_id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.function.get_all_functions`<a id="officientfunctionget_all_functions"></a>

Get the details of all functions or that of a single one

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_functions_response = officient.function.get_all_functions()
```

#### 🔄 Return<a id="🔄-return"></a>

[`FunctionGetAllFunctionsResponse`](./officient_python_sdk/pydantic/function_get_all_functions_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/wages/functions/list` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.function.get_details`<a id="officientfunctionget_details"></a>

Get the details of all functions or that of a single one

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_details_response = officient.function.get_details(
    internal_code="internal_code_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### internal_code: `str`<a id="internal_code-str"></a>

The internal code / GUID of the function you would like to receive information on

#### 🔄 Return<a id="🔄-return"></a>

[`FunctionGetDetailsResponse`](./officient_python_sdk/pydantic/function_get_details_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/wages/functions/detail/{internal_code}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.invitation.generate_secret_url`<a id="officientinvitationgenerate_secret_url"></a>

Generate a secret URL that brings a person straight to the HR self-service platform.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
generate_secret_url_response = officient.invitation.generate_secret_url(
    person_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### person_id: `str`<a id="person_id-str"></a>

Officient will generate a selfservice invite link for this person

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`InvitationGenerateSecretUrlRequest`](./officient_python_sdk/type/invitation_generate_secret_url_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`InvitationGenerateSecretUrlResponse`](./officient_python_sdk/pydantic/invitation_generate_secret_url_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/people/selfservice/invite_link` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.person.add_new`<a id="officientpersonadd_new"></a>

Add a new person to Officient

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_new_response = officient.person.add_new()
```

#### 🔄 Return<a id="🔄-return"></a>

[`PersonAddNewResponse`](./officient_python_sdk/pydantic/person_add_new_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/people/add` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.person.add_to_calendar`<a id="officientpersonadd_to_calendar"></a>

Add new events to a calender (eg a day off, overtime,..)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_to_calendar_response = officient.person.add_to_calendar(
    person_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### person_id: `int`<a id="person_id-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PersonAddToCalendarResponse`](./officient_python_sdk/pydantic/person_add_to_calendar_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/calendar/{person_id}/events/add` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.person.add_to_calendar_0`<a id="officientpersonadd_to_calendar_0"></a>

Adds events to a person's calendar based on a priority scheme of event types

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_to_calendar_0_response = officient.person.add_to_calendar_0(
    person_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### person_id: `int`<a id="person_id-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PersonAddToCalendar200Response`](./officient_python_sdk/pydantic/person_add_to_calendar200_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/calendar/{person_id}/priorityschemes/events/add` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.person.edit_detail`<a id="officientpersonedit_detail"></a>

Edit person

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
edit_detail_response = officient.person.edit_detail(
    person_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### person_id: `int`<a id="person_id-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PersonEditDetailResponse`](./officient_python_sdk/pydantic/person_edit_detail_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/people/{person_id}/detail` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.person.get_budgets_by_year`<a id="officientpersonget_budgets_by_year"></a>

Fetches a list of budgets for a given person and year.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_budgets_by_year_response = officient.person.get_budgets_by_year(
    person_id=1,
    year=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### person_id: `int`<a id="person_id-int"></a>

##### year: `int`<a id="year-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PersonGetBudgetsByYearResponse`](./officient_python_sdk/pydantic/person_get_budgets_by_year_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/budgets/people/{person_id}/{year}/list` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.person.get_current_wage`<a id="officientpersonget_current_wage"></a>

Get the current wage details for one person

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_current_wage_response = officient.person.get_current_wage(
    person_id="person_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### person_id: `str`<a id="person_id-str"></a>

The person you would like to receive wage information on

#### 🔄 Return<a id="🔄-return"></a>

[`PersonGetCurrentWageResponse`](./officient_python_sdk/pydantic/person_get_current_wage_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/wages/{person_id}/current` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.person.get_current_weekly_schedule`<a id="officientpersonget_current_weekly_schedule"></a>

Weekly schedule

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_current_weekly_schedule_response = officient.person.get_current_weekly_schedule(
    person_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### person_id: `int`<a id="person_id-int"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/people/{person_id}/weekly_schedule/current` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.person.get_custom_fields`<a id="officientpersonget_custom_fields"></a>

Person custom fields

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_custom_fields_response = officient.person.get_custom_fields(
    person_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### person_id: `int`<a id="person_id-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PersonGetCustomFieldsResponse`](./officient_python_sdk/pydantic/person_get_custom_fields_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/people/{person_id}/custom_fields` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.person.get_daily_calendar`<a id="officientpersonget_daily_calendar"></a>

List the time off, overtime & scheduled time for a single person for a single day

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_daily_calendar_response = officient.person.get_daily_calendar(
    person_id=1,
    year=1,
    month=1,
    day=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### person_id: `int`<a id="person_id-int"></a>

The person you would like to receive calender information on

##### year: `int`<a id="year-int"></a>

##### month: `int`<a id="month-int"></a>

##### day: `int`<a id="day-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PersonGetDailyCalendarResponse`](./officient_python_sdk/pydantic/person_get_daily_calendar_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/calendar/{person_id}/{year}/{month}/{day}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.person.get_detail`<a id="officientpersonget_detail"></a>

Person detail

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_detail_response = officient.person.get_detail(
    person_id="person_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### person_id: `str`<a id="person_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PersonGetDetailResponse`](./officient_python_sdk/pydantic/person_get_detail_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/people/{person_id}/detail` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.person.get_event_type_limits`<a id="officientpersonget_event_type_limits"></a>

This API can tell how many days off a certain person has in a certain year

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_event_type_limits_response = officient.person.get_event_type_limits(
    person_id=1,
    year=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### person_id: `int`<a id="person_id-int"></a>

##### year: `int`<a id="year-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PersonGetEventTypeLimitsResponse`](./officient_python_sdk/pydantic/person_get_event_type_limits_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/calendar/{person_id}/events/types/{year}/limits` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.person.get_manager_details`<a id="officientpersonget_manager_details"></a>

Person manager

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_manager_details_response = officient.person.get_manager_details(
    person_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### person_id: `int`<a id="person_id-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PersonGetManagerDetailsResponse`](./officient_python_sdk/pydantic/person_get_manager_details_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/people/{person_id}/manager` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.person.get_monthly_calendar`<a id="officientpersonget_monthly_calendar"></a>

List the time off, overtime & scheduled time for a single person for an entire month

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_monthly_calendar_response = officient.person.get_monthly_calendar(
    person_id=1,
    year=1,
    month=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### person_id: `int`<a id="person_id-int"></a>

The person you would like to receive calender information on

##### year: `int`<a id="year-int"></a>

##### month: `int`<a id="month-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PersonGetMonthlyCalendarResponse`](./officient_python_sdk/pydantic/person_get_monthly_calendar_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/calendar/{person_id}/{year}/{month}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.person.get_one_off_wage_components_by_month`<a id="officientpersonget_one_off_wage_components_by_month"></a>

Fetches the one-off wage components that are granted to a person on a specific month

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_one_off_wage_components_by_month_response = (
    officient.person.get_one_off_wage_components_by_month(
        person_id=1,
        year=1,
        month=1,
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### person_id: `int`<a id="person_id-int"></a>

##### year: `int`<a id="year-int"></a>

##### month: `int`<a id="month-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PersonGetOneOffWageComponentsByMonthResponse`](./officient_python_sdk/pydantic/person_get_one_off_wage_components_by_month_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/wages/one_off/components/{person_id}/{year}/{month}/list` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.person.get_performance_reviews_by_person`<a id="officientpersonget_performance_reviews_by_person"></a>

show metadata for performance reviews by person. No content (notes,..) are exposed

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_performance_reviews_by_person_response = (
    officient.person.get_performance_reviews_by_person(
        page=0,
        person_id=1,
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page: `int`<a id="page-int"></a>

Controls pagination (0, 1, 2, ..) to view all results. 30 items per page.

##### person_id: `int`<a id="person_id-int"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/performance_reviews/{person_id}/list` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.person.get_personal_data_changes`<a id="officientpersonget_personal_data_changes"></a>

Get the latest delta of changes to personal data

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_personal_data_changes_response = officient.person.get_personal_data_changes(
    since_timestamp="1970-01-01T00:00:00.00Z",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### since_timestamp: `datetime`<a id="since_timestamp-datetime"></a>

Defaults to 1 week ago

#### 🔄 Return<a id="🔄-return"></a>

[`PersonGetPersonalDataChangesResponse`](./officient_python_sdk/pydantic/person_get_personal_data_changes_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/people/change_history` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.person.get_verzuim_periods`<a id="officientpersonget_verzuim_periods"></a>

List verzuim periods

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_verzuim_periods_response = officient.person.get_verzuim_periods(
    person_id=1,
    year=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### person_id: `int`<a id="person_id-int"></a>

##### year: `int`<a id="year-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PersonGetVerzuimPeriodsResponse`](./officient_python_sdk/pydantic/person_get_verzuim_periods_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/calendar/{person_id}/verzuim/{year}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.person.get_wage_history`<a id="officientpersonget_wage_history"></a>

Get the entire wage history for one person

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_wage_history_response = officient.person.get_wage_history(
    person_id="person_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### person_id: `str`<a id="person_id-str"></a>

The person you need the wage history for

#### 🔄 Return<a id="🔄-return"></a>

[`PersonGetWageHistoryResponse`](./officient_python_sdk/pydantic/person_get_wage_history_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/wages/{person_id}/history` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.person.get_yearly_calendar`<a id="officientpersonget_yearly_calendar"></a>

List the time off, overtime & scheduled time for a single person for an entire year

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_yearly_calendar_response = officient.person.get_yearly_calendar(
    person_id=1,
    year=1,
    filter="all",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### person_id: `int`<a id="person_id-int"></a>

The person you would like to receive calender information on

##### year: `int`<a id="year-int"></a>

##### filter: `str`<a id="filter-str"></a>

can be either 'all' or 'days_with_events' to return only days containing events

#### 🔄 Return<a id="🔄-return"></a>

[`PersonGetYearlyCalendarResponse`](./officient_python_sdk/pydantic/person_get_yearly_calendar_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/calendar/{person_id}/{year}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.person.list_available_components`<a id="officientpersonlist_available_components"></a>

Fetches a list of available one-off wage components (eg bonus, expense compensation,..) for a specific person.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_available_components_response = officient.person.list_available_components()
```

#### 🔄 Return<a id="🔄-return"></a>

[`PersonListAvailableComponentsResponse`](./officient_python_sdk/pydantic/person_list_available_components_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/wages/one_off/components/{person_id}/options/list` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.person.list_budget_items`<a id="officientpersonlist_budget_items"></a>

Lists the items that are in a given budget.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_budget_items_response = officient.person.list_budget_items(
    person_id=1,
    budget_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### person_id: `int`<a id="person_id-int"></a>

##### budget_id: `int`<a id="budget_id-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PersonListBudgetItemsResponse`](./officient_python_sdk/pydantic/person_list_budget_items_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/budgets/people/{person_id}/{budget_id}/items/list` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.person.list_dimonas_by_person`<a id="officientpersonlist_dimonas_by_person"></a>

Belgium only: this API allows you to list all historical DIMONA information for one person

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_dimonas_by_person_response = officient.person.list_dimonas_by_person(
    person_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### person_id: `int`<a id="person_id-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PersonListDimonasByPersonResponse`](./officient_python_sdk/pydantic/person_list_dimonas_by_person_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/legal/dimonas/{person_id}/list` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.person.list_people`<a id="officientpersonlist_people"></a>

List people

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_people_response = officient.person.list_people(
    page=0,
    include_archived=0,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page: `int`<a id="page-int"></a>

Controls pagination (0, 1, 2, ..) to view all results. 30 items per page.

##### include_archived: `int`<a id="include_archived-int"></a>

Include archived people in response

#### 🔄 Return<a id="🔄-return"></a>

[`PersonListPeopleResponse`](./officient_python_sdk/pydantic/person_list_people_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/people/list` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.person.overwrite_event`<a id="officientpersonoverwrite_event"></a>

Create a new event or overwrite an existing one in a personal calender (eg a day off, overtime,..)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
overwrite_event_response = officient.person.overwrite_event(
    person_id="person_id_example",
    year="year_example",
    month="month_example",
    day="day_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### person_id: `str`<a id="person_id-str"></a>

##### year: `str`<a id="year-str"></a>

##### month: `str`<a id="month-str"></a>

##### day: `str`<a id="day-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PersonOverwriteEventResponse`](./officient_python_sdk/pydantic/person_overwrite_event_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/calendar/{person_id}/{year}/{month}/{day}/events/set` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.person.remove_event`<a id="officientpersonremove_event"></a>

Remove an event from the calender, such as a day off

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_event_response = officient.person.remove_event(
    person_id=1,
    event_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### person_id: `int`<a id="person_id-int"></a>

##### event_id: `int`<a id="event_id-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PersonRemoveEventResponse`](./officient_python_sdk/pydantic/person_remove_event_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/calendar/{person_id}/events/{event_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.person.reset_time_worked`<a id="officientpersonreset_time_worked"></a>

reset the time worked on a given day to the regular work schedule for one person

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
reset_time_worked_response = officient.person.reset_time_worked(
    person_id=1,
    year=1,
    month=1,
    day=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### person_id: `int`<a id="person_id-int"></a>

##### year: `int`<a id="year-int"></a>

##### month: `int`<a id="month-int"></a>

##### day: `int`<a id="day-int"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/calendar/{person_id}/{year}/{month}/{day}/work/reset` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.person.search_by_criteria`<a id="officientpersonsearch_by_criteria"></a>

search people by name, email or national number

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
search_by_criteria_response = officient.person.search_by_criteria(
    name="string_example",
    email="string_example",
    national_number="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

eg John Doe

##### email: `str`<a id="email-str"></a>

eg john@doe.net

##### national_number: `str`<a id="national_number-str"></a>

eg 82146126684

#### 🔄 Return<a id="🔄-return"></a>

[`PersonSearchByCriteriaResponse`](./officient_python_sdk/pydantic/person_search_by_criteria_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/people/search` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.person.set_function_description`<a id="officientpersonset_function_description"></a>

Set the function description for each person

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
set_function_description_response = officient.person.set_function_description(
    person_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### person_id: `int`<a id="person_id-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PersonSetFunctionDescriptionResponse`](./officient_python_sdk/pydantic/person_set_function_description_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/people/{person_id}/role` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.person.update_bulk_time_worked`<a id="officientpersonupdate_bulk_time_worked"></a>

Overwrite the amount of time worked for a set of days in bulk (eg for timetracking software integrations)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_bulk_time_worked_response = officient.person.update_bulk_time_worked(
    person_id=1,
    year=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### person_id: `int`<a id="person_id-int"></a>

##### year: `int`<a id="year-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PersonUpdateBulkTimeWorkedResponse`](./officient_python_sdk/pydantic/person_update_bulk_time_worked_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/calendar/{person_id}/{year}/work/bulk` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.person.update_event_type_limit`<a id="officientpersonupdate_event_type_limit"></a>

This API can update the limitations for a specific event type

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_event_type_limit_response = officient.person.update_event_type_limit(
    person_id=1,
    year=1,
    type_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### person_id: `int`<a id="person_id-int"></a>

##### year: `int`<a id="year-int"></a>

##### type_id: `int`<a id="type_id-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PersonUpdateEventTypeLimitResponse`](./officient_python_sdk/pydantic/person_update_event_type_limit_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/calendar/{person_id}/events/types/{year}/limits/{type_id}/set` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.person.update_manager`<a id="officientpersonupdate_manager"></a>

Who reports to who?

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_manager_response = officient.person.update_manager(
    person_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### person_id: `int`<a id="person_id-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PersonUpdateManagerResponse`](./officient_python_sdk/pydantic/person_update_manager_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/people/{person_id}/manager` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.person.update_time_worked`<a id="officientpersonupdate_time_worked"></a>

Overwrite the amount of time worked on a certain day (eg for timetracking software integrations)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_time_worked_response = officient.person.update_time_worked(
    person_id=1,
    year=1,
    month=1,
    day=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### person_id: `int`<a id="person_id-int"></a>

##### year: `int`<a id="year-int"></a>

##### month: `int`<a id="month-int"></a>

##### day: `int`<a id="day-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PersonUpdateTimeWorkedResponse`](./officient_python_sdk/pydantic/person_update_time_worked_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/calendar/{person_id}/{year}/{month}/{day}/work` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.person.upload_avatar`<a id="officientpersonupload_avatar"></a>

upload a photo of this person

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
upload_avatar_response = officient.person.upload_avatar(
    person_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### person_id: `int`<a id="person_id-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PersonUploadAvatarResponse`](./officient_python_sdk/pydantic/person_upload_avatar_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/people/{person_id}/photo` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.person.view_role_history`<a id="officientpersonview_role_history"></a>

View the role history for one person

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
view_role_history_response = officient.person.view_role_history(
    person_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### person_id: `int`<a id="person_id-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PersonViewRoleHistoryResponse`](./officient_python_sdk/pydantic/person_view_role_history_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/roles/{person_id}/history` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.priority_scheme.list_active_priority_schemes_by_year`<a id="officientpriority_schemelist_active_priority_schemes_by_year"></a>

lists the active priority schemes for a specific year

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_active_priority_schemes_by_year_response = (
    officient.priority_scheme.list_active_priority_schemes_by_year(
        year=1,
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### year: `int`<a id="year-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PrioritySchemeListActivePrioritySchemesByYearResponse`](./officient_python_sdk/pydantic/priority_scheme_list_active_priority_schemes_by_year_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/calendar/events/priorityschemes/{year}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.team.create_new_team`<a id="officientteamcreate_new_team"></a>

Add team

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_team_response = officient.team.create_new_team()
```

#### 🔄 Return<a id="🔄-return"></a>

[`TeamCreateNewTeamResponse`](./officient_python_sdk/pydantic/team_create_new_team_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/teams/add` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.team.edit_information`<a id="officientteamedit_information"></a>

Edit team

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
edit_information_response = officient.team.edit_information(
    team_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### team_id: `int`<a id="team_id-int"></a>

The ID of the team you'd like to update

#### 🔄 Return<a id="🔄-return"></a>

[`TeamEditInformationResponse`](./officient_python_sdk/pydantic/team_edit_information_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/teams/{team_id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.team.get_all_teams`<a id="officientteamget_all_teams"></a>

List all teams

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_teams_response = officient.team.get_all_teams()
```

#### 🔄 Return<a id="🔄-return"></a>

[`TeamGetAllTeamsResponse`](./officient_python_sdk/pydantic/team_get_all_teams_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/teams/list` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.vehicle.create_new`<a id="officientvehiclecreate_new"></a>

Add vehicle

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_response = officient.vehicle.create_new()
```

#### 🔄 Return<a id="🔄-return"></a>

[`VehicleCreateNewResponse`](./officient_python_sdk/pydantic/vehicle_create_new_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/fleet/add` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.vehicle.edit_details`<a id="officientvehicleedit_details"></a>

Edit vehicle

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
edit_details_response = officient.vehicle.edit_details(
    vehicle_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### vehicle_id: `int`<a id="vehicle_id-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`VehicleEditDetailsResponse`](./officient_python_sdk/pydantic/vehicle_edit_details_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/fleet/{vehicle_id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.vehicle.get_all_vehicles`<a id="officientvehicleget_all_vehicles"></a>

Get a list of all vehicles in the fleet

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_vehicles_response = officient.vehicle.get_all_vehicles(
    page=0,
    person_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page: `int`<a id="page-int"></a>

Controls pagination (0, 1, 2, ..) to view all results. 30 items per page.

##### person_id: `int`<a id="person_id-int"></a>

view only vehicles that belong to a specific person

#### 🔄 Return<a id="🔄-return"></a>

[`VehicleGetAllVehiclesResponse`](./officient_python_sdk/pydantic/vehicle_get_all_vehicles_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/fleet/list` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.vehicle.get_detail`<a id="officientvehicleget_detail"></a>

Get details about one vehicle in the fleet

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_detail_response = officient.vehicle.get_detail(
    vehicle_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### vehicle_id: `int`<a id="vehicle_id-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`VehicleGetDetailResponse`](./officient_python_sdk/pydantic/vehicle_get_detail_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/fleet/{vehicle_id}/detail` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.webhook.get_active_notifications`<a id="officientwebhookget_active_notifications"></a>

View currently active notifications

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_active_notifications_response = officient.webhook.get_active_notifications()
```

#### 🔄 Return<a id="🔄-return"></a>

[`WebhookGetActiveNotificationsResponse`](./officient_python_sdk/pydantic/webhook_get_active_notifications_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/webhooks/list` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.webhook.subscribe_notification`<a id="officientwebhooksubscribe_notification"></a>

use this API to subscribe to notifications

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
subscribe_notification_response = officient.webhook.subscribe_notification()
```

#### 🔄 Return<a id="🔄-return"></a>

[`WebhookSubscribeNotificationResponse`](./officient_python_sdk/pydantic/webhook_subscribe_notification_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/webhooks/add` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `officient.webhook.unsubscribe_notification`<a id="officientwebhookunsubscribe_notification"></a>

Use this API to unsubscribe from notifcations

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
unsubscribe_notification_response = officient.webhook.unsubscribe_notification(
    webhook_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webhook_id: `int`<a id="webhook_id-int"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/1.0/webhooks/{webhook_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
