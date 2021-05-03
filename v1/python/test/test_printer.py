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
from carbon3d.models.printer import Printer  # noqa: E501
from carbon3d.rest import ApiException

class TestPrinter(unittest.TestCase):
    """Printer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Printer
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = carbon3d.models.printer.Printer()  # noqa: E501
        if include_optional :
            return Printer(
                name = '0', 
                serial = '0', 
                hw_type = '0', 
                url = '0', 
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                status = carbon3d.models.printer_status.Printer_status(
                    alerts = [
                        '0'
                        ], 
                    printer_state = '0', 
                    software_version = '0', ), 
                prints = carbon3d.models.printer_prints.Printer_prints(
                    last = carbon3d.models.print_ref.PrintRef(
                        name = '0', 
                        print_id = '0', 
                        build_uuid = '0', 
                        finished_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        remaining_sec = 56, ), 
                    current = carbon3d.models.print_ref.PrintRef(
                        name = '0', 
                        print_id = '0', 
                        build_uuid = '0', 
                        finished_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        remaining_sec = 56, ), 
                    next = carbon3d.models.print_ref.PrintRef(
                        name = '0', 
                        print_id = '0', 
                        build_uuid = '0', 
                        finished_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        remaining_sec = 56, ), 
                    queue_length = 56, )
            )
        else :
            return Printer(
                name = '0',
                serial = '0',
                hw_type = '0',
                url = '0',
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                status = carbon3d.models.printer_status.Printer_status(
                    alerts = [
                        '0'
                        ], 
                    printer_state = '0', 
                    software_version = '0', ),
                prints = carbon3d.models.printer_prints.Printer_prints(
                    last = carbon3d.models.print_ref.PrintRef(
                        name = '0', 
                        print_id = '0', 
                        build_uuid = '0', 
                        finished_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        remaining_sec = 56, ), 
                    current = carbon3d.models.print_ref.PrintRef(
                        name = '0', 
                        print_id = '0', 
                        build_uuid = '0', 
                        finished_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        remaining_sec = 56, ), 
                    next = carbon3d.models.print_ref.PrintRef(
                        name = '0', 
                        print_id = '0', 
                        build_uuid = '0', 
                        finished_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        remaining_sec = 56, ), 
                    queue_length = 56, ),
        )

    def testPrinter(self):
        """Test Printer"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
