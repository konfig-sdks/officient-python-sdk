operation_parameter_map = {
    '/1.0/account-GET': {
        'parameters': [
        ]
    },
    '/1.0/assets/types/add-POST': {
        'parameters': [
        ]
    },
    '/1.0/assets/add-POST': {
        'parameters': [
        ]
    },
    '/1.0/assets/types/list-GET': {
        'parameters': [
        ]
    },
    '/1.0/assets/{asset_id}/detail-GET': {
        'parameters': [
            {
                'name': 'asset_id'
            },
        ]
    },
    '/1.0/assets/list-GET': {
        'parameters': [
            {
                'name': 'page'
            },
            {
                'name': 'person_id'
            },
        ]
    },
    '/1.0/assets/{asset_id}-DELETE': {
        'parameters': [
            {
                'name': 'asset_id'
            },
        ]
    },
    '/1.0/assets/types/{asset_type_id}-DELETE': {
        'parameters': [
            {
                'name': 'asset_type_id'
            },
        ]
    },
    '/1.0/assets/{asset_id}-PATCH': {
        'parameters': [
            {
                'name': 'asset_id'
            },
        ]
    },
    '/1.0/token-POST': {
        'parameters': [
            {
                'name': 'code'
            },
            {
                'name': 'client_id'
            },
            {
                'name': 'client_secret'
            },
            {
                'name': 'grant_type'
            },
            {
                'name': 'refresh_token'
            },
        ]
    },
    '/1.0/budgets/add-POST': {
        'parameters': [
            {
                'name': 'budget_type'
            },
            {
                'name': 'maximum'
            },
            {
                'name': 'year'
            },
            {
                'name': 'employee_id'
            },
        ]
    },
    '/1.0/budgets/{budget_id}/items/add-POST': {
        'parameters': [
            {
                'name': 'budget_id'
            },
            {
                'name': 'item_name'
            },
            {
                'name': 'cost'
            },
            {
                'name': 'employee_id'
            },
        ]
    },
    '/1.0/budgets/{budget_id}-DELETE': {
        'parameters': [
            {
                'name': 'budget_id'
            },
        ]
    },
    '/1.0/budgets/{budget_id}/items/{item_id}-DELETE': {
        'parameters': [
            {
                'name': 'budget_id'
            },
            {
                'name': 'item_id'
            },
        ]
    },
    '/1.0/budgets/{budget_id}-PATCH': {
        'parameters': [
            {
                'name': 'budget_id'
            },
            {
                'name': 'maximum'
            },
        ]
    },
    '/1.0/calendar/requests/{request_id}/detail-GET': {
        'parameters': [
            {
                'name': 'request_id'
            },
        ]
    },
    '/1.0/calendar/requests/list-GET': {
        'parameters': [
            {
                'name': 'page'
            },
            {
                'name': 'status'
            },
        ]
    },
    '/1.0/calendar/state/lock-POST': {
        'parameters': [
            {
                'name': 'disable_lock'
            },
        ]
    },
    '/1.0/wages/one_off/components/add-POST': {
        'parameters': [
        ]
    },
    '/1.0/wages/one_off/components/{granted_component_id}-DELETE': {
        'parameters': [
        ]
    },
    '/1.0/contracts/add-POST': {
        'parameters': [
        ]
    },
    '/1.0/contracts/list-GET': {
        'parameters': [
            {
                'name': 'page'
            },
        ]
    },
    '/1.0/contracts/{contract_id}/detail-GET': {
        'parameters': [
            {
                'name': 'contract_id'
            },
        ]
    },
    '/1.0/contracts/{contract_id}/pdf-GET': {
        'parameters': [
            {
                'name': 'contract_id'
            },
        ]
    },
    '/1.0/contracts/signature/request-POST': {
        'parameters': [
        ]
    },
    '/1.0/wages/cost_centers/detail/{internal_code}-GET': {
        'parameters': [
            {
                'name': 'internal_code'
            },
        ]
    },
    '/1.0/wages/cost_centers/list-GET': {
        'parameters': [
        ]
    },
    '/1.0/wages/cost_units/detail/{internal_code}-GET': {
        'parameters': [
            {
                'name': 'internal_code'
            },
        ]
    },
    '/1.0/wages/cost_units/list-GET': {
        'parameters': [
        ]
    },
    '/1.0/calendar/events/types/{year}-GET': {
        'parameters': [
            {
                'name': 'year'
            },
        ]
    },
    '/1.0/custom_fields/{custom_field_id}/{object_type}/{object_id}-PATCH': {
        'parameters': [
            {
                'name': 'custom_field_id'
            },
            {
                'name': 'object_type'
            },
            {
                'name': 'object_id'
            },
        ]
    },
    '/1.0/custom_fields/list-GET': {
        'parameters': [
        ]
    },
    '/1.0/wages/departments/list-GET': {
        'parameters': [
        ]
    },
    '/1.0/wages/departments/detail/{internal_code}-GET': {
        'parameters': [
            {
                'name': 'internal_code'
            },
        ]
    },
    '/1.0/documents/{file_id}/download-GET': {
        'parameters': [
            {
                'name': 'file_id'
            },
        ]
    },
    '/1.0/documents/{object_type}/{object_id}/list-GET': {
        'parameters': [
            {
                'name': 'object_type'
            },
            {
                'name': 'object_id'
            },
            {
                'name': 'page'
            },
        ]
    },
    '/1.0/documents/{file_id}-DELETE': {
        'parameters': [
            {
                'name': 'file_id'
            },
        ]
    },
    '/1.0/documents/{object_type}/{object_id}/add-POST': {
        'parameters': [
            {
                'name': 'object_type'
            },
            {
                'name': 'object_id'
            },
        ]
    },
    '/1.0/expenses/categories/add-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'type'
            },
            {
                'name': 'price-per-kilometer'
            },
            {
                'name': 'price-per-day'
            },
        ]
    },
    '/1.0/expenses/add-POST': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'employee_id'
            },
            {
                'name': 'category_id'
            },
            {
                'name': 'amount'
            },
            {
                'name': 'extra_information'
            },
            {
                'name': 'date'
            },
            {
                'name': 'filename'
            },
            {
                'name': 'file_base64'
            },
            {
                'name': 'dates'
            },
            {
                'name': 'distance'
            },
            {
                'name': 'ride'
            },
        ]
    },
    '/1.0/expenses/{expense_id}-DELETE': {
        'parameters': [
            {
                'name': 'expense_id'
            },
        ]
    },
    '/1.0/expenses/categories/{category_id}-DELETE': {
        'parameters': [
            {
                'name': 'category_id'
            },
        ]
    },
    '/1.0/expenses/categories/{category_id}-PATCH': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'category_id'
            },
        ]
    },
    '/1.0/expenses/{expense_id}/detail-GET': {
        'parameters': [
            {
                'name': 'expense id'
            },
        ]
    },
    '/1.0/expenses/categories/{category_id}/detail-GET': {
        'parameters': [
            {
                'name': 'category_id'
            },
        ]
    },
    '/1.0/expenses/list/{year}/{month}-GET': {
        'parameters': [
            {
                'name': 'year'
            },
            {
                'name': 'month'
            },
            {
                'name': 'page'
            },
            {
                'name': 'include_deleted'
            },
        ]
    },
    '/1.0/expenses/list/{year}-GET': {
        'parameters': [
            {
                'name': 'year'
            },
            {
                'name': 'month'
            },
            {
                'name': 'page'
            },
            {
                'name': 'include_deleted'
            },
        ]
    },
    '/1.0/expenses/categories/list-GET': {
        'parameters': [
        ]
    },
    '/1.0/expenses/{expense_id}/updatePayout-POST': {
        'parameters': [
            {
                'name': 'new_payout_method'
            },
            {
                'name': 'expense_id'
            },
            {
                'name': 'payout_other_reason'
            },
            {
                'name': 'payout_status'
            },
            {
                'name': 'period'
            },
            {
                'name': 'year'
            },
        ]
    },
    '/1.0/expenses/{expense_id}-PATCH': {
        'parameters': [
            {
                'name': 'category_id'
            },
            {
                'name': 'expense_id'
            },
        ]
    },
    '/1.0/wages/functions/list-GET': {
        'parameters': [
        ]
    },
    '/1.0/wages/functions/detail/{internal_code}-GET': {
        'parameters': [
            {
                'name': 'internal_code'
            },
        ]
    },
    '/1.0/people/selfservice/invite_link-POST': {
        'parameters': [
            {
                'name': 'person_id'
            },
        ]
    },
    '/1.0/people/add-POST': {
        'parameters': [
        ]
    },
    '/1.0/calendar/{person_id}/events/add-POST': {
        'parameters': [
            {
                'name': 'person_id'
            },
        ]
    },
    '/1.0/calendar/{person_id}/priorityschemes/events/add-POST': {
        'parameters': [
            {
                'name': 'person_id'
            },
        ]
    },
    '/1.0/people/{person_id}/detail-PATCH': {
        'parameters': [
            {
                'name': 'person_id'
            },
        ]
    },
    '/1.0/budgets/people/{person_id}/{year}/list-GET': {
        'parameters': [
            {
                'name': 'person_id'
            },
            {
                'name': 'year'
            },
        ]
    },
    '/1.0/wages/{person_id}/current-GET': {
        'parameters': [
            {
                'name': 'person_id'
            },
        ]
    },
    '/1.0/people/{person_id}/weekly_schedule/current-GET': {
        'parameters': [
            {
                'name': 'person_id'
            },
        ]
    },
    '/1.0/people/{person_id}/custom_fields-GET': {
        'parameters': [
            {
                'name': 'person_id'
            },
        ]
    },
    '/1.0/calendar/{person_id}/{year}/{month}/{day}-GET': {
        'parameters': [
            {
                'name': 'person_id'
            },
            {
                'name': 'year'
            },
            {
                'name': 'month'
            },
            {
                'name': 'day'
            },
        ]
    },
    '/1.0/people/{person_id}/detail-GET': {
        'parameters': [
            {
                'name': 'person_id'
            },
        ]
    },
    '/1.0/calendar/{person_id}/events/types/{year}/limits-GET': {
        'parameters': [
            {
                'name': 'person_id'
            },
            {
                'name': 'year'
            },
        ]
    },
    '/1.0/people/{person_id}/manager-GET': {
        'parameters': [
            {
                'name': 'person_id'
            },
        ]
    },
    '/1.0/calendar/{person_id}/{year}/{month}-GET': {
        'parameters': [
            {
                'name': 'person_id'
            },
            {
                'name': 'year'
            },
            {
                'name': 'month'
            },
        ]
    },
    '/1.0/wages/one_off/components/{person_id}/{year}/{month}/list-GET': {
        'parameters': [
            {
                'name': 'person_id'
            },
            {
                'name': 'year'
            },
            {
                'name': 'month'
            },
        ]
    },
    '/1.0/performance_reviews/{person_id}/list-GET': {
        'parameters': [
            {
                'name': 'page'
            },
            {
                'name': 'person_id'
            },
        ]
    },
    '/1.0/people/change_history-GET': {
        'parameters': [
            {
                'name': 'since_timestamp'
            },
        ]
    },
    '/1.0/calendar/{person_id}/verzuim/{year}-GET': {
        'parameters': [
            {
                'name': 'person_id'
            },
            {
                'name': 'year'
            },
        ]
    },
    '/1.0/wages/{person_id}/history-GET': {
        'parameters': [
            {
                'name': 'person_id'
            },
        ]
    },
    '/1.0/calendar/{person_id}/{year}-GET': {
        'parameters': [
            {
                'name': 'person_id'
            },
            {
                'name': 'year'
            },
            {
                'name': 'filter'
            },
        ]
    },
    '/1.0/wages/one_off/components/{person_id}/options/list-GET': {
        'parameters': [
        ]
    },
    '/1.0/budgets/people/{person_id}/{budget_id}/items/list-GET': {
        'parameters': [
            {
                'name': 'person_id'
            },
            {
                'name': 'budget_id'
            },
        ]
    },
    '/1.0/legal/dimonas/{person_id}/list-GET': {
        'parameters': [
            {
                'name': 'person_id'
            },
        ]
    },
    '/1.0/people/list-GET': {
        'parameters': [
            {
                'name': 'page'
            },
            {
                'name': 'include_archived'
            },
        ]
    },
    '/1.0/calendar/{person_id}/{year}/{month}/{day}/events/set-PUT': {
        'parameters': [
            {
                'name': 'person_id'
            },
            {
                'name': 'year'
            },
            {
                'name': 'month'
            },
            {
                'name': 'day'
            },
        ]
    },
    '/1.0/calendar/{person_id}/events/{event_id}-DELETE': {
        'parameters': [
            {
                'name': 'person_id'
            },
            {
                'name': 'event_id'
            },
        ]
    },
    '/1.0/calendar/{person_id}/{year}/{month}/{day}/work/reset-POST': {
        'parameters': [
            {
                'name': 'person_id'
            },
            {
                'name': 'year'
            },
            {
                'name': 'month'
            },
            {
                'name': 'day'
            },
        ]
    },
    '/1.0/people/search-GET': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'email'
            },
            {
                'name': 'national_number'
            },
        ]
    },
    '/1.0/people/{person_id}/role-PUT': {
        'parameters': [
            {
                'name': 'person_id'
            },
        ]
    },
    '/1.0/calendar/{person_id}/{year}/work/bulk-PATCH': {
        'parameters': [
            {
                'name': 'person_id'
            },
            {
                'name': 'year'
            },
        ]
    },
    '/1.0/calendar/{person_id}/events/types/{year}/limits/{type_id}/set-POST': {
        'parameters': [
            {
                'name': 'person_id'
            },
            {
                'name': 'year'
            },
            {
                'name': 'type_id'
            },
        ]
    },
    '/1.0/people/{person_id}/manager-PUT': {
        'parameters': [
            {
                'name': 'person_id'
            },
        ]
    },
    '/1.0/calendar/{person_id}/{year}/{month}/{day}/work-PATCH': {
        'parameters': [
            {
                'name': 'person_id'
            },
            {
                'name': 'year'
            },
            {
                'name': 'month'
            },
            {
                'name': 'day'
            },
        ]
    },
    '/1.0/people/{person_id}/photo-PUT': {
        'parameters': [
            {
                'name': 'person_id'
            },
        ]
    },
    '/1.0/roles/{person_id}/history-GET': {
        'parameters': [
            {
                'name': 'person_id'
            },
        ]
    },
    '/1.0/calendar/events/priorityschemes/{year}-GET': {
        'parameters': [
            {
                'name': 'year'
            },
        ]
    },
    '/1.0/teams/add-POST': {
        'parameters': [
        ]
    },
    '/1.0/teams/{team_id}-PATCH': {
        'parameters': [
            {
                'name': 'team_id'
            },
        ]
    },
    '/1.0/teams/list-GET': {
        'parameters': [
        ]
    },
    '/1.0/fleet/add-POST': {
        'parameters': [
        ]
    },
    '/1.0/fleet/{vehicle_id}-PATCH': {
        'parameters': [
            {
                'name': 'vehicle_id'
            },
        ]
    },
    '/1.0/fleet/list-GET': {
        'parameters': [
            {
                'name': 'page'
            },
            {
                'name': 'person_id'
            },
        ]
    },
    '/1.0/fleet/{vehicle_id}/detail-GET': {
        'parameters': [
            {
                'name': 'vehicle_id'
            },
        ]
    },
    '/1.0/webhooks/list-GET': {
        'parameters': [
        ]
    },
    '/1.0/webhooks/add-POST': {
        'parameters': [
        ]
    },
    '/1.0/webhooks/{webhook_id}-DELETE': {
        'parameters': [
            {
                'name': 'webhook_id'
            },
        ]
    },
};