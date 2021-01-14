# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!  You can find all relevant documentation here: https://github.com/carbon3d/carbon3d-api   # noqa: E501

    The version of the OpenAPI document: 0.2.4
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import carbon3d
from carbon3d.models.part_measurement_template_response import PartMeasurementTemplateResponse  # noqa: E501
from carbon3d.rest import ApiException

class TestPartMeasurementTemplateResponse(unittest.TestCase):
    """PartMeasurementTemplateResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PartMeasurementTemplateResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = carbon3d.models.part_measurement_template_response.PartMeasurementTemplateResponse()  # noqa: E501
        if include_optional :
            return PartMeasurementTemplateResponse(
                limit = 56, 
                next_cursor = 'dXNlcjpXMDdRQ1JQQTQ=', 
                total_count = 56, 
                part_measurement_templates = [
                    {"uuid":"c13fcaeb-b106-4126-9ca6-3ecbb0ba3124","updated_at":"2020-03-28T12:25:00.000Z","production_sop_name":"Helmet Pad Size 56","production_sop_version":5,"operation_name":"WASH","measurement_name":"Visual Inspection","zones":["A","B","C","D"],"zones_enabled":true,"required_level":"required_for_failure","measurement_type":"category","measurement_classification":"visual","units":null,"min":null,"max":null,"category_options":{"fail":["Adhesion","Fringing","Tear"],"flag":[],"pass":["Pass"]}}
                    ]
            )
        else :
            return PartMeasurementTemplateResponse(
        )

    def testPartMeasurementTemplateResponse(self):
        """Test PartMeasurementTemplateResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
