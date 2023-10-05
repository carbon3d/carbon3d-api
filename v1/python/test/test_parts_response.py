# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!   # noqa: E501

    The version of the OpenAPI document: 0.4.12
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import carbon3d
from carbon3d.models.parts_response import PartsResponse  # noqa: E501
from carbon3d.rest import ApiException

class TestPartsResponse(unittest.TestCase):
    """PartsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PartsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = carbon3d.models.parts_response.PartsResponse()  # noqa: E501
        if include_optional :
            return PartsResponse(
                limit = 56, 
                next_cursor = 'dXNlcjpXMDdRQ1JQQTQ=', 
                total_count = 56, 
                parts = [
                    {"uuid":"6401c93f-f340-4da2-8784-bddd4065e75c","part_number":"12345","model_uuid":"3cc663e2-c762-4f8f-8997-30d17bc13e8d"}
                    ]
            )
        else :
            return PartsResponse(
        )

    def testPartsResponse(self):
        """Test PartsResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
