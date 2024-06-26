# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!   # noqa: E501

    The version of the OpenAPI document: 0.4.17
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import carbon3d
from carbon3d.models.part_measurement_template import PartMeasurementTemplate  # noqa: E501
from carbon3d.rest import ApiException

class TestPartMeasurementTemplate(unittest.TestCase):
    """PartMeasurementTemplate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PartMeasurementTemplate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = carbon3d.models.part_measurement_template.PartMeasurementTemplate()  # noqa: E501
        if include_optional :
            return PartMeasurementTemplate(
                uuid = '0', 
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                production_sop_name = '0', 
                production_sop_version = 1.337, 
                operation_name = '0', 
                measurement_name = '0', 
                zones = [
                    '0'
                    ], 
                zones_enabled = True, 
                required_level = 'required', 
                measurement_type = 'process', 
                units = '0', 
                min = 1.337, 
                max = 1.337, 
                measurement_classification = '0', 
                category_options = carbon3d.models.part_measurement_template_category_options.PartMeasurementTemplate_category_options(
                    fail = [
                        '0'
                        ], 
                    flag = [
                        '0'
                        ], 
                    pass = [
                        '0'
                        ], )
            )
        else :
            return PartMeasurementTemplate(
        )

    def testPartMeasurementTemplate(self):
        """Test PartMeasurementTemplate"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
