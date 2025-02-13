# coding: utf-8

"""
    Officient API

    Officient offers an intuitive HRIS which helps manage all personnel administration through our HR platform & personalized employee self-services. Manage payroll, company assets, contracts, days off, fleet, performance reviews and all employee data in one HR system. HR deserves great software and we're here to provide it.  We support our customers in transforming HR towards paperless administration and automating tedious workforce management tasks in the process. Our goal? Transform HR from an administrative, processing role, to a controlling role which fuels HR strategy across the organization.

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from officient_python_sdk.paths._1_0_calendar_requests_request_id_detail.get import GetDetailById
from officient_python_sdk.paths._1_0_calendar_requests_list.get import ListRequests
from officient_python_sdk.apis.tags.calendar_request_api_raw import CalendarRequestApiRaw


class CalendarRequestApi(
    GetDetailById,
    ListRequests,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: CalendarRequestApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = CalendarRequestApiRaw(api_client)
