# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!  You can find all relevant documentation here: https://github.com/carbon3d/carbon3d-api   # noqa: E501

    The version of the OpenAPI document: 0.3.0
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import carbon3d
from carbon3d.models.part_genealogy_print_info import PartGenealogyPrintInfo  # noqa: E501
from carbon3d.rest import ApiException

class TestPartGenealogyPrintInfo(unittest.TestCase):
    """PartGenealogyPrintInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PartGenealogyPrintInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = carbon3d.models.part_genealogy_print_info.PartGenealogyPrintInfo()  # noqa: E501
        if include_optional :
            return PartGenealogyPrintInfo(
                queued_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                print_uuid = '0', 
                printer_serial = '0', 
                platform_serial = '0', 
                cassette_serial = '0', 
                resin_lot_number = '0', 
                started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                finished_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                error = '0'
            )
        else :
            return PartGenealogyPrintInfo(
        )

    def testPartGenealogyPrintInfo(self):
        """Test PartGenealogyPrintInfo"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
