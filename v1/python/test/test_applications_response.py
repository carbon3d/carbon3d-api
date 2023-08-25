# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!   # noqa: E501

    The version of the OpenAPI document: 0.4.8
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import carbon3d
from carbon3d.models.applications_response import ApplicationsResponse  # noqa: E501
from carbon3d.rest import ApiException

class TestApplicationsResponse(unittest.TestCase):
    """ApplicationsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ApplicationsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = carbon3d.models.applications_response.ApplicationsResponse()  # noqa: E501
        if include_optional :
            return ApplicationsResponse(
                applications = [
                    {"uuid":"eb9b0cb1-3321-46c8-b022-0f56f67d02d3","name":"example application","description":"an application to use as an example"}
                    ]
            )
        else :
            return ApplicationsResponse(
                applications = [
                    {"uuid":"eb9b0cb1-3321-46c8-b022-0f56f67d02d3","name":"example application","description":"an application to use as an example"}
                    ],
        )

    def testApplicationsResponse(self):
        """Test ApplicationsResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
