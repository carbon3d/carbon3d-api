# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!  You can find all relevant documentation here: https://github.com/carbon3d/carbon3d-api   # noqa: E501

    The version of the OpenAPI document: 0.1.2
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import carbon3d
from carbon3d.models.part_measurement import PartMeasurement  # noqa: E501
from carbon3d.rest import ApiException

class TestPartMeasurement(unittest.TestCase):
    """PartMeasurement unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PartMeasurement
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = carbon3d.models.part_measurement.PartMeasurement()  # noqa: E501
        if include_optional :
            return PartMeasurement(
                uuid = '0', 
                printed_part_uuid = '0', 
                part_measurement_template_uuid = '0', 
                value = 1.337, 
                category_value = '0', 
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                measurement_result = 'pass', 
                zones = [
                    '0'
                    ], 
                notes = '0'
            )
        else :
            return PartMeasurement(
        )

    def testPartMeasurement(self):
        """Test PartMeasurement"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
