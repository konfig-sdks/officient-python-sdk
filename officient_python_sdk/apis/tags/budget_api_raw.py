# coding: utf-8

"""
    Officient API

    Officient offers an intuitive HRIS which helps manage all personnel administration through our HR platform & personalized employee self-services. Manage payroll, company assets, contracts, days off, fleet, performance reviews and all employee data in one HR system. HR deserves great software and we're here to provide it.  We support our customers in transforming HR towards paperless administration and automating tedious workforce management tasks in the process. Our goal? Transform HR from an administrative, processing role, to a controlling role which fuels HR strategy across the organization.

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from officient_python_sdk.paths._1_0_budgets_add.post import AddBudgetItemRaw
from officient_python_sdk.paths._1_0_budgets_budget_id_items_add.post import AddItemRaw
from officient_python_sdk.paths._1_0_budgets_budget_id.delete import DeleteBudgetByIdRaw
from officient_python_sdk.paths._1_0_budgets_budget_id_items_item_id.delete import RemoveItemRaw
from officient_python_sdk.paths._1_0_budgets_budget_id.patch import UpdateBudgetItemRaw


class BudgetApiRaw(
    AddBudgetItemRaw,
    AddItemRaw,
    DeleteBudgetByIdRaw,
    RemoveItemRaw,
    UpdateBudgetItemRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
