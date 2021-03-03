# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!  You can find all relevant documentation here: https://github.com/carbon3d/carbon3d-api   # noqa: E501

    The version of the OpenAPI document: 0.2.8
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import carbon3d
from carbon3d.models.print_order_request import PrintOrderRequest  # noqa: E501
from carbon3d.rest import ApiException

class TestPrintOrderRequest(unittest.TestCase):
    """PrintOrderRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PrintOrderRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = carbon3d.models.print_order_request.PrintOrderRequest()  # noqa: E501
        if include_optional :
            return PrintOrderRequest(
                build_uuid = '0', 
                total_copies = 56, 
                route_to = [
                    '0'
                    ], 
                print_order_number = '0', 
                print_order_tags = {
                    'key' : '0'
                    }, 
                notes = '0'
            )
        else :
            return PrintOrderRequest(
                build_uuid = '0',
                total_copies = 56,
                route_to = [
                    '0'
                    ],
        )

    def testPrintOrderRequest(self):
        """Test PrintOrderRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
