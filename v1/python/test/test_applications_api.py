# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!  You can find all relevant documentation here: https://github.com/carbon3d/carbon3d-api   # noqa: E501

    The version of the OpenAPI document: 0.4.0
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import carbon3d
from carbon3d.api.applications_api import ApplicationsApi  # noqa: E501
from carbon3d.rest import ApiException


class TestApplicationsApi(unittest.TestCase):
    """ApplicationsApi unit test stubs"""

    def setUp(self):
        self.api = carbon3d.api.applications_api.ApplicationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_applications(self):
        """Test case for get_applications

        Fetch all applications summary  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
