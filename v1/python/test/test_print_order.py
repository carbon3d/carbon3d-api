# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!  You can find all relevant documentation here: https://github.com/carbon3d/carbon3d-api   # noqa: E501

    The version of the OpenAPI document: 0.2.2
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import carbon3d
from carbon3d.models.print_order import PrintOrder  # noqa: E501
from carbon3d.rest import ApiException

class TestPrintOrder(unittest.TestCase):
    """PrintOrder unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PrintOrder
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = carbon3d.models.print_order.PrintOrder()  # noqa: E501
        if include_optional :
            return PrintOrder(
                uuid = '0', 
                build_uuid = '0', 
                total_copies = 56, 
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                print_order_number = '0', 
                print_order_tags = {
                    'key' : '0'
                    }, 
                notes = '0', 
                routed_to = {
                    'key' : carbon3d.models.print_order_routed_to.PrintOrder_routed_to(
                        copies_queued = 56, 
                        copies_printed = 56, )
                    }
            )
        else :
            return PrintOrder(
        )

    def testPrintOrder(self):
        """Test PrintOrder"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
