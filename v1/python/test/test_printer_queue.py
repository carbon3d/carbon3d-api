# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!  You can find all relevant documentation here: https://github.com/carbon3d/carbon3d-api   # noqa: E501

    The version of the OpenAPI document: 0.3.3
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import carbon3d
from carbon3d.models.printer_queue import PrinterQueue  # noqa: E501
from carbon3d.rest import ApiException

class TestPrinterQueue(unittest.TestCase):
    """PrinterQueue unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PrinterQueue
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = carbon3d.models.printer_queue.PrinterQueue()  # noqa: E501
        if include_optional :
            return PrinterQueue(
                printer_serial = '0', 
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                print_uuids = ["edb4304f-1323-5d3d-9a87-2a0febc91948","abc4303f-9a87-5d3d-1323-2a0febc12345"]
            )
        else :
            return PrinterQueue(
        )

    def testPrinterQueue(self):
        """Test PrinterQueue"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()