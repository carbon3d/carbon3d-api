# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!  You can find all relevant documentation here: https://github.com/carbon3d/carbon3d-api   # noqa: E501

    The version of the OpenAPI document: 0.0.8
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import carbon3d
from carbon3d.models.part_order import PartOrder  # noqa: E501
from carbon3d.rest import ApiException

class TestPartOrder(unittest.TestCase):
    """PartOrder unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PartOrder
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = carbon3d.models.part_order.PartOrder()  # noqa: E501
        if include_optional :
            return PartOrder(
                uuid = '0', 
                status = 'open', 
                part_order_number = '0', 
                due_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                route_to = [
                    '0'
                    ], 
                printed_parts = [
                    carbon3d.models.printed_part_ref.PrintedPartRef(
                        uuid = '0', 
                        part_uuid = '0', 
                        status = 'waiting', )
                    ], 
                flushed_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else :
            return PartOrder(
                uuid = '0',
                due_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                printed_parts = [
                    carbon3d.models.printed_part_ref.PrintedPartRef(
                        uuid = '0', 
                        part_uuid = '0', 
                        status = 'waiting', )
                    ],
        )

    def testPartOrder(self):
        """Test PartOrder"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
