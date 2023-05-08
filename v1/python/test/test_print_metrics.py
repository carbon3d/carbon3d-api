# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!   # noqa: E501

    The version of the OpenAPI document: 0.4.6
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import carbon3d
from carbon3d.models.print_metrics import PrintMetrics  # noqa: E501
from carbon3d.rest import ApiException

class TestPrintMetrics(unittest.TestCase):
    """PrintMetrics unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PrintMetrics
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = carbon3d.models.print_metrics.PrintMetrics()  # noqa: E501
        if include_optional :
            return PrintMetrics(
                average_speed_mmhr = 56, 
                consumed_resin_volume_ml = 1.337, 
                minimum_required_resin_volume_ml = 1.337, 
                estimated_total_resin_volume_ml = 1.337, 
                measured_resin_volume_ml = 1.337
            )
        else :
            return PrintMetrics(
        )

    def testPrintMetrics(self):
        """Test PrintMetrics"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
