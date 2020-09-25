# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!  You can find all relevant documentation here: https://github.com/carbon3d/carbon3d-api   # noqa: E501

    The version of the OpenAPI document: 0.1.4
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import carbon3d
from carbon3d.models.part_measurement_response import PartMeasurementResponse  # noqa: E501
from carbon3d.rest import ApiException

class TestPartMeasurementResponse(unittest.TestCase):
    """PartMeasurementResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PartMeasurementResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = carbon3d.models.part_measurement_response.PartMeasurementResponse()  # noqa: E501
        if include_optional :
            return PartMeasurementResponse(
                limit = 56, 
                next_cursor = 'dXNlcjpXMDdRQ1JQQTQ=', 
                total_count = 56, 
                part_measurements = [
                    {"uuid":"c13fcaeb-b106-4126-9ca6-3ecbb0ba3124","printed_part_uuid":"75e4811b-0f54-4ce0-a93a-511668b08b49","part_measurement_template_uuid":"261bfc3a-1644-4b78-80be-264d3c85dc15","value":null,"category_value":"adhesion","zones":["A","B"],"measurement_result":"fail","notes":"Some notes","updated_at":"2020-03-28T12:25:00.000Z"}
                    ]
            )
        else :
            return PartMeasurementResponse(
        )

    def testPartMeasurementResponse(self):
        """Test PartMeasurementResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
