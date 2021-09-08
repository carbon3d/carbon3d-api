# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!  You can find all relevant documentation here: https://github.com/carbon3d/carbon3d-api   # noqa: E501

    The version of the OpenAPI document: 0.3.4
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import carbon3d
from carbon3d.models.printed_part import PrintedPart  # noqa: E501
from carbon3d.rest import ApiException

class TestPrintedPart(unittest.TestCase):
    """PrintedPart unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PrintedPart
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = carbon3d.models.printed_part.PrintedPart()  # noqa: E501
        if include_optional :
            return PrintedPart(
                uuid = '0', 
                part_uuid = '0', 
                model_uuid = '0', 
                part_number = '0', 
                build_uuid = '0', 
                part_order_uuid = '0', 
                part_order_number = '0', 
                print_order_uuid = '0', 
                print_order_number = '0', 
                print_id = '0', 
                print_uuid = '0', 
                serial_number = '0', 
                tags = carbon3d.models.printed_part_tags.PrintedPart_tags(
                    part_number = {
                        'key' : '0'
                        }, 
                    part = {
                        'key' : '0'
                        }, 
                    printed_part = {
                        'key' : '0'
                        }, ), 
                status = 'waiting', 
                error = '0'
            )
        else :
            return PrintedPart(
                uuid = '0',
                part_uuid = '0',
                status = 'waiting',
        )

    def testPrintedPart(self):
        """Test PrintedPart"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
