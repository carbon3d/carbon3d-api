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
from carbon3d.models.prints_response import PrintsResponse  # noqa: E501
from carbon3d.rest import ApiException

class TestPrintsResponse(unittest.TestCase):
    """PrintsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PrintsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = carbon3d.models.prints_response.PrintsResponse()  # noqa: E501
        if include_optional :
            return PrintsResponse(
                limit = 10, 
                next_cursor = 'dXNlcjpXMDdRQ1JQQTQ=', 
                total_count = 100, 
                prints = []
            )
        else :
            return PrintsResponse(
        )

    def testPrintsResponse(self):
        """Test PrintsResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
