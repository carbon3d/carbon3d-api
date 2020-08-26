# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!  You can find all relevant documentation here: https://github.com/carbon3d/carbon3d-api   # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import carbon3d
from carbon3d.models.printed_parts_response import PrintedPartsResponse  # noqa: E501
from carbon3d.rest import ApiException

class TestPrintedPartsResponse(unittest.TestCase):
    """PrintedPartsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PrintedPartsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = carbon3d.models.printed_parts_response.PrintedPartsResponse()  # noqa: E501
        if include_optional :
            return PrintedPartsResponse(
                limit = 56, 
                offset = 56, 
                total_count = 56, 
                parts = [
                    {"build_uuid":"d938c229-a14d-4314-8a00-f2d2717c43d0","model_uuid":"26ee9a9b-0a23-4146-93de-27afea4acd65","part_number":"101000-01","part_order_number":"","part_order_uuid":"7eacc87e-e4ee-4911-b317-039717dd9a76","part_uuid":"4133bbe6-4858-4f18-ad6f-95ef6ea08b31","print_id":"KT310GVA","print_order_number":"WO-123","print_order_uuid":"657208d6-d796-4623-8981-d7aa66932a69","serial_number":"KT310GVA-1","status":"complete","tags":{"part_number":{"size":"large","color":"red"},"part":{"customization_id":"123456"},"printed_part":{}},"uuid":"cc49c64d-c3cf-45f8-943b-c8693f28c146"}
                    ]
            )
        else :
            return PrintedPartsResponse(
        )

    def testPrintedPartsResponse(self):
        """Test PrintedPartsResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
