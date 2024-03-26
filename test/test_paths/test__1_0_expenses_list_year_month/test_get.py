# coding: utf-8

"""
    Officient API

    Officient offers an intuitive HRIS which helps manage all personnel administration through our HR platform & personalized employee self-services. Manage payroll, company assets, contracts, days off, fleet, performance reviews and all employee data in one HR system. HR deserves great software and we're here to provide it.  We support our customers in transforming HR towards paperless administration and automating tedious workforce management tasks in the process. Our goal? Transform HR from an administrative, processing role, to a controlling role which fuels HR strategy across the organization.

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

import unittest
from unittest.mock import patch

import urllib3

import officient_python_sdk
from officient_python_sdk.paths._1_0_expenses_list_year_month import get
from officient_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestModel10ExpensesListYearMonth(ApiTestMixin, unittest.TestCase):
    """
    Model10ExpensesListYearMonth unit test stubs
        List expenses by month
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
