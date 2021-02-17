# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!  You can find all relevant documentation here: https://github.com/carbon3d/carbon3d-api   # noqa: E501

    The version of the OpenAPI document: 0.2.7
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import carbon3d
from carbon3d.models.printers_response import PrintersResponse  # noqa: E501
from carbon3d.rest import ApiException

class TestPrintersResponse(unittest.TestCase):
    """PrintersResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PrintersResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = carbon3d.models.printers_response.PrintersResponse()  # noqa: E501
        if include_optional :
            return PrintersResponse(
                limit = 56, 
                offset = 56, 
                total_count = 56, 
                printers = [
                    {"name":"L9001","serial":"3P01CM","hw_type":"L1","url":"https://l9001.customer.print.carbon3d.com","updated_at":"2020-03-28T12:25:00.000Z","status":{"alerts":["oxygen shortage"],"printer_state":"PRINTING","software_version":"123.0-785.85"},"prints":{"last":{"name":"great_file.stl","build_uuid":"1cf34076-417e-489f-8863-3438facd4808-10","print_id":"JN007KA","finished_at":"2020-01-18T12:25:00.000Z"},"current":{"name":"greater_file.stl","print_id":"JN008KA","build_uuid":"3ff34076-417e-489f-8863-3438facd4808-99","started_at":"2020-01-18T14:25:00.000Z","remaining_sec":523},"next":{"name":"future_file.stl","build_uuid":"66634076-417e-489f-8863-3438facd4808-09"},"queue_length":2}}
                    ]
            )
        else :
            return PrintersResponse(
                limit = 56,
                offset = 56,
                total_count = 56,
                printers = [
                    {"name":"L9001","serial":"3P01CM","hw_type":"L1","url":"https://l9001.customer.print.carbon3d.com","updated_at":"2020-03-28T12:25:00.000Z","status":{"alerts":["oxygen shortage"],"printer_state":"PRINTING","software_version":"123.0-785.85"},"prints":{"last":{"name":"great_file.stl","build_uuid":"1cf34076-417e-489f-8863-3438facd4808-10","print_id":"JN007KA","finished_at":"2020-01-18T12:25:00.000Z"},"current":{"name":"greater_file.stl","print_id":"JN008KA","build_uuid":"3ff34076-417e-489f-8863-3438facd4808-99","started_at":"2020-01-18T14:25:00.000Z","remaining_sec":523},"next":{"name":"future_file.stl","build_uuid":"66634076-417e-489f-8863-3438facd4808-09"},"queue_length":2}}
                    ],
        )

    def testPrintersResponse(self):
        """Test PrintersResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
