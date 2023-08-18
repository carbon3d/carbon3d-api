# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!   # noqa: E501

    The version of the OpenAPI document: 0.4.7
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import carbon3d
from carbon3d.api.printed_parts_api import PrintedPartsApi  # noqa: E501
from carbon3d.rest import ApiException


class TestPrintedPartsApi(unittest.TestCase):
    """PrintedPartsApi unit test stubs"""

    def setUp(self):
        self.api = carbon3d.api.printed_parts_api.PrintedPartsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_printed_part(self):
        """Test case for get_printed_part

        Fetch a printed Part  # noqa: E501
        """
        pass

    def test_get_printed_parts(self):
        """Test case for get_printed_parts

        Fetch printed parts  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
