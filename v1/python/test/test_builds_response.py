# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!   # noqa: E501

    The version of the OpenAPI document: 0.4.16
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import carbon3d
from carbon3d.models.builds_response import BuildsResponse  # noqa: E501
from carbon3d.rest import ApiException

class TestBuildsResponse(unittest.TestCase):
    """BuildsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BuildsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = carbon3d.models.builds_response.BuildsResponse()  # noqa: E501
        if include_optional :
            return BuildsResponse(
                limit = 56, 
                next_cursor = 'dXNlcjpXMDdRQ1JQQTQ=', 
                total_count = 56, 
                builds = [
                    {"uuid":"98d97fe6-83d2-473c-9148-322012ea835b","parts":[{"uuid":"9962b034-e64b-4f81-a40d-26b885239a58","part_number":"B142353","model_uuid":"2ce02977-fad4-4b21-b49c-019144d945a8"}],"attachments":[{"filename":"traveler.pdf","uuid":"10d97fe6-fad4-7721-b49c-017133d945b0"}],"application_uuid":"cf5bcd58-08e8-4b89-a2a0-18a549b405f2","packing_group":"GROUP_1","part_orders":[{"uuid":"3fccab79-e509-4fa4-8be8-5b04159926bb","part_order_numer":"ORDER_1","status":"open"}],"created_at":"2020-03-28T12:25:00.000Z","updated_at":"2020-03-28T12:25:00.000Z"}
                    ]
            )
        else :
            return BuildsResponse(
        )

    def testBuildsResponse(self):
        """Test BuildsResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
