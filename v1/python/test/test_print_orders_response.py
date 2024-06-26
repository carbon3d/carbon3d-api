# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!   # noqa: E501

    The version of the OpenAPI document: 0.4.17
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import carbon3d
from carbon3d.models.print_orders_response import PrintOrdersResponse  # noqa: E501
from carbon3d.rest import ApiException

class TestPrintOrdersResponse(unittest.TestCase):
    """PrintOrdersResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PrintOrdersResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = carbon3d.models.print_orders_response.PrintOrdersResponse()  # noqa: E501
        if include_optional :
            return PrintOrdersResponse(
                limit = 56, 
                next_cursor = 'dXNlcjpXMDdRQ1JQQTQ=', 
                total_count = 56, 
                print_orders = [
                    {"uuid":"c13fcaeb-b106-4126-9ca6-3ecbb0ba3124","build_uuid":"75e4811b-0f54-4ce0-a93a-511668b08b49","total_copies":100,"print_order_number":"WO_12345","created_at":"2020-03-28T12:25:00.000Z","route_to":["1G0001","3N00QP","9N0000","9B9ZZ9"],"print_order_tags":{"validation":"true","experiment":"ABC"},"notes":"Some notes"}
                    ]
            )
        else :
            return PrintOrdersResponse(
        )

    def testPrintOrdersResponse(self):
        """Test PrintOrdersResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
