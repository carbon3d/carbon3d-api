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
from carbon3d.models.model_print import ModelPrint  # noqa: E501
from carbon3d.rest import ApiException

class TestModelPrint(unittest.TestCase):
    """ModelPrint unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ModelPrint
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = carbon3d.models.model_print.ModelPrint()  # noqa: E501
        if include_optional :
            return ModelPrint(
                name = '0', 
                print_id = '0', 
                build_uuid = '0', 
                finished_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                remaining_sec = 56, 
                printed_by = '0', 
                print_order_uuid = '0', 
                print_order_number = '0', 
                status = '0', 
                origin = carbon3d.models.print_origin.Print_origin(
                    cassette_serial = '0', 
                    platform_serial = '0', 
                    printer_serial = '0', 
                    software_version = '0', ), 
                config = carbon3d.models.print_config.Print_config(
                    resin_name = '0', 
                    print_profile = '0', 
                    release_film_nm = 56, 
                    slice_thickness_nm = 56, ), 
                metrics = carbon3d.models.print_metrics.Print_metrics(
                    average_speed_mmhr = 56, 
                    consumed_resin_volume_ml = 1.337, 
                    minimum_required_resin_volume_ml = 1.337, 
                    estimated_total_resin_volume_ml = 1.337, 
                    measured_resin_volume_ml = 1.337, ), 
                feedback = carbon3d.models.print_feedback.Print_feedback(
                    feedback_rating = 1.337, 
                    feedback_message = '0', )
            )
        else :
            return ModelPrint(
        )

    def testModelPrint(self):
        """Test ModelPrint"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
