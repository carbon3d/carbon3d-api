# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!   # noqa: E501

    The version of the OpenAPI document: 0.4.10
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import carbon3d
from carbon3d.api.prints_api import PrintsApi  # noqa: E501
from carbon3d.rest import ApiException


class TestPrintsApi(unittest.TestCase):
    """PrintsApi unit test stubs"""

    def setUp(self):
        self.api = carbon3d.api.prints_api.PrintsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_prints(self):
        """Test case for get_prints

        List finished prints information  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
