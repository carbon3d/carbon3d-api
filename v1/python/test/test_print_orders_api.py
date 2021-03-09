# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!  You can find all relevant documentation here: https://github.com/carbon3d/carbon3d-api   # noqa: E501

    The version of the OpenAPI document: 0.2.9
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import carbon3d
from carbon3d.api.print_orders_api import PrintOrdersApi  # noqa: E501
from carbon3d.rest import ApiException


class TestPrintOrdersApi(unittest.TestCase):
    """PrintOrdersApi unit test stubs"""

    def setUp(self):
        self.api = carbon3d.api.print_orders_api.PrintOrdersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_print_order(self):
        """Test case for create_print_order

        Create a PrintOrder  # noqa: E501
        """
        pass

    def test_get_print_order(self):
        """Test case for get_print_order

        Get a PrintOrder  # noqa: E501
        """
        pass

    def test_get_print_orders(self):
        """Test case for get_print_orders

        Fetch print orders  # noqa: E501
        """
        pass

    def test_update_print_order(self):
        """Test case for update_print_order

        Update a PrintOrder  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
